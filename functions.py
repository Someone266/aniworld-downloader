import wget
import requests
import os
import re
import json
import time
import sys
import bs4
import main
import dl_a
import http.server
import shutil
import zipfile

def setTitle(title = 'AniWorld Scraper'):
    # set the title of the console
    if os.name == 'nt':
        os.system(f'title {title}')
    else:
        print(f'\033]0;{title}\007')
    return


def getInfo(url):    
    # get the html content of the page
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # extract the title by finding the element with the class series-title and getting the inner text
    title = soup.find('div', class_='series-title').text
    # get the inner text of the title
    title = title.strip()
    # get the span element inside the title
    title = title.split('\n')[0]
    print('Getting info for:', title)
    # extract the description by finding the element with the class seri_des and data-full-description using bs4
    description = soup.find('p', class_='seri_des').get('data-full-description')
    # get the start and enddate, startdate itemprop="startDate"
    startdate = soup.find('span', itemprop='startDate').text
    enddate = soup.find('span', itemprop='endDate').text

    # if enddate is 'heute', set the status to ongoing, else set it to finished
    if enddate == 'heute':
        status = 'ONGOING'
    else:
        status = 'FINISHED'

    # get the number of seasons
    # seasons = soup.find('meta', itemprop='numberOfSeasons').get('content') # not working
    # get the number of seasons by counting the number of li elements
    seasons = soup.find('strong', text='Staffeln:').parent.parent.parent.find_all('li')
    # check if li text is not numeric, if it is remove it
    seasons = [season.text for season in seasons]
    # remove all spaces from the list
    seasons = [season.replace(' ', '') for season in seasons]
    # remove all empty strings from the list
    seasons = [season for season in seasons if season]
    # remove all non numeric strings from the list
    seasons = [season for season in seasons if season.isnumeric()]
    # get the number of seasons by counting the number of li elements
    seasons = len(seasons)

    # get the number of episodes
    episodes = {}
    for season in range(1, int(seasons) + 1):
        episodes[season] = getEpisodesFromSeason(url, season)
    episodes = episodes
    total_episodes = sum(episodes.values())


    # get the picture of the anime (class="seriesCoverBox" get the src attribute)
    picture = soup.find('div', class_='seriesCoverBox').find('noscript').find('img').get('src')
    picture = 'https://aniworld.to' + picture

    # get the trailer class="trailerButton"
    trailer = soup.find('a', class_='trailerButton').get('href')

    # get the tags (itemprop="genre")
    tags = soup.find_all('a', itemprop='genre')
    tags = [tag.text for tag in tags]

    # get the producer (class="seriesProducer")
    producer = soup.find('strong', class_='seriesProducer').text
    
    # get the fsk rating (data-fsk="16")
    fsk = soup.find('div', class_='fsk').get('data-fsk')

    # get imdb link class="imdb-link"
    imdb = soup.find('a', class_='imdb-link')
    if imdb is not None:
        imdb = imdb.get('href')
    else:
        imdb = ''



    print(status + ' (' + startdate + ' - ' + enddate + ') - ' + str(total_episodes) + ' episodes - ' + str(seasons) + ' seasons')
    

    result = {
        'title': title,
        'description': description,
        'animeSeason': {
            'year': int(startdate[:4]),
            'season': startdate[5:],
        },
        'status': status,
        'episodes': episodes,
        'totalEpisodes': total_episodes,
        'seasons': seasons,
        'startdate': startdate,
        'enddate': enddate,
        'picture': picture,
        'trailer': trailer,
        'tags': tags,
        'producer': producer,
        'fsk': fsk,
        'imdb': imdb,
        'url': url,
    }

    # add the image to the json object
    return result

def setup(info):
    print('Setting up anime folder...')

    # print(info)
    # exit()

    # setup a folder for the anime, if it doesn't exist and create a info.json and info.html file
    # pathname is the title of the anime and the season info (year-season)
    pathname = f'{info["title"]} ({info["startdate"]}-{info["enddate"]})'

    # remove special characters from the pathname
    pathname = re.sub(r'[<>:"/\\|?*]', '', pathname)

    # the pathname is inside the current directory / anime / title (year-season)
    pathname = f'anime/{pathname}'

    # create the folder
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    # create the info.json file, but first utf-8 encode the data
    with open(f'{pathname}/info.json', 'w') as f:
        json.dump(info, f, indent=4)

    # get the filetype of the image
    filetype = info['picture'].split('.')[-1]
    # download the image, but first check if the image exists
    if not os.path.exists(f'{pathname}/image.{filetype}'):
        wget.download(info['picture'], f'{pathname}/image.{filetype}')
    
    # replace picture with the image path
    info['picture'] = f'image.{filetype}'
    info['pathname'] = pathname

    # save info
    with open(f'{pathname}/info.json', 'w') as f:
        json.dump(info, f, indent=4)


    # add the folder to index.json
    if os.path.exists('./anime/index.json'):
        with open('./anime/index.json', 'r') as f:
            data = json.load(f)
    else:
        data = []
    # add the folder, title and tags to the index.json file
    newData = {
        'title': info['title'],
        'tags': info['tags'],
        'startdate': info['startdate'],
        'enddate': info['enddate'],
        'status': info['status'],
        'description': info['description'],
        'totalEpisodes': info['totalEpisodes'],
        'seasons': info['seasons'],
        'pathname': pathname,
    }
    # if it already exists, update the data
    for i, item in enumerate(data):
        if item['title'] == info['title']:
            data[i] = newData
            break
    else:
        data.append(newData)
    with open('./anime/index.json', 'w') as f:
        json.dump(data, f, indent=4)


    # get template.html and replace the placeholders with the info; e.g. %title% with the title of the anime
    with open('./assets/template.html', 'r') as f:
        template = f.read()
    
    # replace the placeholders with the info
    template = template.replace('%title%', info['title'])
    template = template.replace('%description%', info['description'])
    template = template.replace('%startDate%', info['startdate'])
    template = template.replace('%endDate%', info['enddate'])
    template = template.replace('%status%', info['status'])
    template = template.replace('%totalEpisodes%', str(info['totalEpisodes']))
    template = template.replace('%seasons%', str(info['seasons']))
    template = template.replace('%picture%', f'image.{filetype}')
    template = template.replace('%trailer%', info['trailer'])
    template = template.replace('%producer%', info['producer'])
    template = template.replace('%fsk%', info['fsk'])
    template = template.replace('%imdb%', info['imdb'])
    template = template.replace('%tags%', ', '.join(info['tags']))

    # create the info.html file, but first utf-8 encode the data
    template = template.encode('utf-8')
    with open(f'{pathname}/info.html', 'wb') as f:
        f.write(template)
    print('Anime folder setup complete')
    return

def getSeasonDownloads(url, season, episodes = None, info = None):
    if episodes is None:
        # get the episodes of the season
        response = requests.get(url)
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        # get the ul where Episoden is in the span
        episodes = soup.find('strong', text='Episoden:').parent.parent.parent
        # get the number of episodes by counting the number of li elements
        episodes = episodes.find_all('li')
        # get the number of episodes by counting the number of li elements
        episodes = len(episodes) - 1
    
    print(f'Getting streams for season {season} with {episodes} episodes...')

    # foreach episode, get the download links
    data = {}
    for episode in range(1, episodes + 1):
        if info is not None:
            data[episode] = getEpisodeDownloads(url, season, episode, info)
        else:
            data[episode] = getEpisodeDownloads(url, season, episode)
        updateProgress(episode / episodes)
    print('\n')
    print('Done with season', season)
    return data

    
def updateProgress(percent):
    bar_length = 50
    block = int(round(bar_length * percent))
    progress = '=' * block + '-' * (bar_length - block)
    sys.stdout.write(f'\rProgress: [{progress}] {percent * 100:.2f}%')
    sys.stdout.flush()


def getEpisodeDownloads(url, season, episode, info = None):
    url = url + f'/staffel-{season}/episode-{episode}'

    # get the html content of the page
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # get the parent of i element class="icon VOE"
    download = soup.find('i', class_='icon VOE')
    # if the download element is not found, return
    if download is None:
        print('No voe download found, skipping...')
        return
    # get the parent of the i element
    download = download.parent
    # get the href of the a element
    download = download.get('href')
    download = 'https://aniworld.to' + download
    streamUrl = redirectUrl(download)
    if streamUrl is None:
        print('No stream url found')
        return
    
    # save link to json file
    if info is not None:
        pathname = f'{info["title"]} ({info["startdate"]}-{info["enddate"]})'

        # remove special characters from the pathname
        pathname = re.sub(r'[<>:"/\\|?*]', '', pathname)
        pathname = f'anime/{pathname}/stream.json'
    else:
        pathname = f'stream.json'

    # add the stream url inside the season array
    # e.g.
    # {
    #    "1": {
    #        "1": "https://voe.sx/e/1234567890",
    #        "2": "https://voe.sx/e/1234567891",
    #    }
    # }
    if os.path.exists(pathname):
        with open(pathname, 'r') as f:
            data = json.load(f)
    else:
        data = {}
    if str(season) not in data:
        data[str(season)] = {}
    data[str(season)][str(episode)] = streamUrl
    with open(pathname, 'w') as f:
        json.dump(data, f, indent=4)
    
    return streamUrl

def redirectUrl(url):
    # get header of the url, if it starts with 3, it's a redirect, if not return the url
    response = requests.head(url)
    if response.status_code != 302 and response.status_code != 301:
        print('No redirect found')
        return
    else:
        # get the location of the redirect
        location = response.headers['Location']
        
        # check if redirect is not aniworld.to
        if 'aniworld.to' in location:
            print('Something went wrong with the redirect')
            return
        else:
            # print('Got stream link:', location)
            return location

def getEpisodesFromSeason(url, season):
    url = url + f'/staffel-{season}'

    # get the html content of the page
    response = requests.get(url)
    html = response.text

    # save html to file, utf-8 encode the data
    # with open('temp.html', 'w', encoding='utf-8') as f:
    #     f.write(html)

    soup = bs4.BeautifulSoup(html, 'html.parser')

    # get the episodes of the season
    # get the ul where Episoden is in the span
    episodes = soup.find('strong', text='Episoden:').parent.parent.parent
    # get the number of episodes by counting the number of li elements
    episodes = episodes.find_all('li')
    episodes = len(episodes) - 1
    return episodes

def downloadEpisode(season, episode, info = None):
    clearConsole()
    main.showLogo()
    if info is None:
        with open('stream.json', 'r') as f:
            data = json.load(f)
    else:
        pathname = f'{info["title"]} ({info["startdate"]}-{info["enddate"]})'
        pathname = re.sub(r'[<>:"/\\|?*]', '', pathname)
        pathname = f'anime/{pathname}'
        with open(pathname + '/stream.json', 'r') as f:
            data = json.load(f)
    print(f'Downloading season {season} episode {episode}...')
    # get the stream url from the json file
    streamUrl = data[str(season)][str(episode)]
    print(streamUrl)
    dl_a.download(streamUrl, pathname, season, episode)

def downloadSeason(season, info = None):
    if info is None:
        with open('stream.json', 'r') as f:
            data = json.load(f)
    else:
        pathname = f'{info["title"]} ({info["startdate"]}-{info["enddate"]})'
        pathname = re.sub(r'[<>:"/\\|?*]', '', pathname)
        pathname = f'anime/{pathname}'
        with open(pathname + '/stream.json', 'r') as f:
            data = json.load(f)
    # get the stream url from the json file
    for episode in data[str(season)]:
        streamUrl = data[str(season)][episode]
        clearConsole()
        main.showLogo()
        print(f'Downloading season {season} episode {episode}...')
        updateProgress(int(episode) / len(data[str(season)]))
        print("\n")
        dl_a.download(streamUrl, pathname, season, episode)

def downloadRange(season, start, end, info = None):
    if info is None:
        with open('stream.json', 'r') as f:
            data = json.load(f)
    else:
        pathname = f'{info["title"]} ({info["startdate"]}-{info["enddate"]})'
        pathname = re.sub(r'[<>:"/\\|?*]', '', pathname)
        pathname = f'anime/{pathname}'
        with open(pathname + '/stream.json', 'r') as f:
            data = json.load(f)
    # get the stream url from the json file
    for episode in range(start, end + 1):
        streamUrl = data[str(season)][str(episode)]
        clearConsole()
        main.showLogo()
        print(f'Downloading season {season} episode {episode}...')
        updateProgress((episode - start) / (end - start))
        print("\n")
        dl_a.download(streamUrl, pathname, season, episode)
    
    return

def searchAnime(query):
    # debug
    # query = 'Solo Leveling'
    # query = '+'.join(query.split(' '))

    if query == '':
        print(main.bcolors.WARNING + 'No query entered' + main.bcolors.ENDC)
        return
    
    
    # curl:
#     curl 'https://aniworld.to/ajax/search' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-US,en;q=0.9' \
#   -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
#   -H 'cookie: __ddg1_=bn4u2ftGLDvlbZOy7bsJ; rememberLogin=xLS0M2m2zAdS9AH3WtMX2DozHHIMXxoRpeCBLmNAWv5zRrfDJQEGbFL0sDN9CERjxE9RgErQn8ktydToUvtNbXVxENkCgTUB5kfzRjfr21DH2AddBbyYVRCR; aniworld_session=el75m9n2773pnqckbaba28bjnn' \
#   -H 'origin: https://aniworld.to' \
#   -H 'referer: https://aniworld.to/search?q=solo+leveling' \
#   -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
#   -H 'x-requested-with: XMLHttpRequest' \
#   --data-raw 'keyword=solo+leveling'

    # get the search results
    url = 'https://aniworld.to/ajax/search'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://aniworld.to',
        'referer': f'https://aniworld.to/search?q={query}',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'keyword': query,
    }
    data = requests.post(url, headers=headers, data=data)
    
    # utf decode the data
    data = data.text
    # print(data)
    # parse the json data
    data = json.loads(data)
    # print(data)


    
    return searchAnime1(query, data)


def searchAnime1(query, data):

    # example response:
    # [
    # {
    #     "title": "<em>Solo Leveling</em>",
    #     "description": "Es ist \u00fcber ein Jahrzehnt her, dass die \u201eGates\u201c \u2013 Pfade, die die reale Welt mit einer anderen Dimension verbinden \u2013 pl\u00f6tzlich erschienen sind. Seitdem sind einige Menschen mit \u00fcbernat\u00fcrlichen Kr\u00e4ften erwacht.&#8230;",
    #     "link": "/anime/stream/solo-leveling"
    # },
    # {
    #     "title": "habe eine frage \u00fcber <em>Solo Leveling</em>",
    #     "description": "Wir helfen dir bei Problemen: Besuche unseren Support-Bereich.",
    #     "link": "/support/frage/habe-eine-frage-ber-solo-leveling"
    # },
    # ...
    # ]
    # remove all items that don't have /anime/stream/ in the link
    data = [item for item in data if '/anime/stream/' in item['link']]
    # remove all items that have /support/ in the link
    data = [item for item in data if '/support/' not in item['link']]
    # remove all items that have /user/ in the link
    data = [item for item in data if '/user/' not in item['link']]
    # remove all items that have /search/ in the link
    data = [item for item in data if '/search/' not in item['link']]
    # remove all links that have /episode-[number] in the link
    data = [item for item in data if '/episode-' not in item['link']]
    # remove all links that have /staffel-[number] in the link
    data = [item for item in data if '/staffel-' not in item['link']]


    
    # debug, save the data to a file
    with open('search.txt', 'w') as f:
        json.dump(data, f, indent=4)
    
    clearConsole()
    main.showLogo()
    print('Search results for:', query)
    print('\n')
    # list the top 5 results for the user to select by number
    for i, item in enumerate(data):
        # remove <em> and </em> from the title
        item['title'] = item['title'].replace('<em>', '').replace('</em>', '')
        print(i + 1, main.bcolors.OK + item['title'] + main.bcolors.ENDC)
        print(item['description'])
        print('---')
    print(main.bcolors.PRIMARY + 'Select a number to continue, or press q to quit' + main.bcolors.ENDC)
    number = input()
    if number == 'q':
        return
    elif not number.isnumeric():
        print('Invalid number, try again')
        time.sleep(2)
        searchAnime1(query, data)
        return
    elif int(number) < 1 or int(number) > len(data):
        print('Invalid number, try again')
        time.sleep(2)
        searchAnime1(query, data)
        return
    number = int(number)
    # get the link of the selected item
    link = data[number - 1]['link']
    print('Selected:', data[number - 1]['title'])
    print(link)
    # e.g. url: /anime/stream/solo-leveling
    url = 'https://aniworld.to' + link
    print('url:', url)
    return url


def serveContent():
    # start a http server with document root to the anime folder
    PORT = 3333
    Handler = http.server.SimpleHTTPRequestHandler
    # web_dir = os.path.join(os.path.dirname(__file__), 'anime')
    # os.chdir(web_dir)
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        print("serving at http://localhost:" + str(PORT) + "/anime/")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()
    return

def clean():
    clearConsole()
    main.showLogo()
    print('Running cleanup...')

    files = [f for f in os.listdir('.') if f.endswith('.part') or f.endswith('.ytdl')]
    # if there are no files, return
    if files:
        print(main.bcolors.WARNING + 'This will delete non finished downloads, after deleting you can\'t resume the download' + main.bcolors.ENDC)
        print('Do you want to continue? (y/N)')
        answer = input()
        if answer.lower() == 'y':
            # get all files that end with .part or .ytdl
            print('Deleting files...')
            for file in files:
                os.remove(file)
                print('Deleted:', file)
    

    
    print('Rebuilding index.json...')
    # get all folders in the anime folder
    folders = [f for f in os.listdir('anime') if os.path.isdir(os.path.join('anime', f))]
    data = []
    for folder in folders:
        # if folder is empty, remove it
        if not os.listdir(f'anime/{folder}'):
            os.rmdir(f'anime/{folder}')
            continue
        # if info.json doesn't exist, remove the folder
        if not os.path.exists(f'anime/{folder}/info.json'):
            # os.rmdir(f'anime/{folder}')
            continue
        with open(f'anime/{folder}/info.json', 'r') as f:
            info = json.load(f)
        # if info.json does not contain the an item, run setup -u <url>

        # if info does not include url, skip
        if 'url' not in info:
            print('No url found for:', '/' + folder + '/ (' + info['title'] +  ')' + ', should we remove it? (Y/n)')
            answer = input()
            if answer.lower() == 'n':
                continue
            print('Removing:', info['title'])
            # remove with shutil.rmtree to remove the folder and all files inside
            shutil.rmtree(f'anime/{folder}')
            continue

        required = ['title', 'description', 'animeSeason', 'status', 'episodes', 'totalEpisodes', 'seasons', 'startdate', 'enddate', 'picture', 'trailer', 'tags', 'producer', 'fsk', 'imdb']
        if not all(key in info for key in required):    
            print('Rebuilding info.json for:', info['title'])
            info = getInfo(info['url'])
            setup(info)

        

        data.append({
            'title': info['title'],
            'tags': info['tags'],
            'startdate': info['startdate'],
            'enddate': info['enddate'],
            'status': info['status'],
            'description': info['description'],
            'totalEpisodes': info['totalEpisodes'],
            'seasons': info['seasons'],
            'pathname': f'anime/{folder}',
        })
    with open('./anime/index.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print('Done')
    return
    
def startUi():
    clearConsole()
    main.showLogo()
    print('Press one of the following keys:')
    # userselect with navigation
    print('1. Download Assistant')
    print('2. Manual Download')
    print('3. Continue Download')
    print('4. Serve content')
    print('5. Clean up')
    print('6. Setup anime folder')
    print('7. Get anime info')
    print('0. Settings')
    print('q. Quit')

    # get the key from the user
    key = input()
    # if the key is not in the list, return
    if key not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'Q']:
        print('Invalid key')
        startUi()
        return
    # if the key is 1, run the automatic anime download
    if key == '1':
        main.runAuto()
    # if the key is 2, run the manual anime download
    elif key == '2':
        print('This mode will download everything from the given url')
        print('Enter the url of the anime')
        url = input()
        url = validateUrl(url)
        if not url:
            print(main.bcolors.WARNING + 'Invalid url' + main.bcolors.ENDC)
            time.sleep(2)
            startUi()
            return
        main.runMain(url)
    elif key == '3':
        print('Not implemented yet')
        time.sleep(2)
        startUi()
    # if the key is 3, run the serve content
    elif key == '4':
        serveContent()
    # if the key is 4, run the clean up
    elif key == '5':
        clean()
    # if the key is 5, run the setup anime folder
    elif key == '6':
        print('Enter the url of the anime')
        url = input()
        url = validateUrl(url)
        if not url:
            print(main.bcolors.WARNING + 'Invalid url' + main.bcolors.ENDC)
            time.sleep(2)
            startUi()
            return
        info = getInfo(url)
        setup(info)
    # if the key is 6, run the get anime info
    elif key == '7':
        print('Enter the url of the anime')
        url = input()
        url = validateUrl(url)
        if not url:
            print(main.bcolors.WARNING + 'Invalid url' + main.bcolors.ENDC)
            time.sleep(2)
            startUi()
            return
        print(getInfo(url))
    # if the key is 7, run the get season streams
    elif key == 'q' or key == 'Q':
        print('Quitting...')
        exit()
    else:
        print(main.bcolors.WARNING + 'Invalid key' + main.bcolors.ENDC)
        time.sleep(2)
        startUi()
        return
    return






def validateUrl(url):
    # check if it is a valid url

    # check if the url is a valid aniworld.to url
    if 'aniworld.to' not in url:
        print('Invalid url')
        return False
    # if the url has staffel in it, remove it and everything after it
    if 'staffel' in url:
        url = url.split('staffel')[0]
    # if the url has episode in it, remove it and everything after it
    if 'episode' in url:
        url = url.split('episode')[0]
    return url

def firstRun():
    # check if settings.json exists, if not guide the user through the setup
    if not os.path.exists('settings.json'):
        guide1()
        return
    else:
        # check if the anime folder exists, if not create it
        if not os.path.exists('./anime'):
            os.makedirs('./anime')
        # check if the assets folder exists, if not create it
        if not os.path.exists('./assets'):
            os.makedirs('./assets')
    

def guide1():
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Hi and welcome to AniWorld-Down v' + main.thisVersion() + main.bcolors.ENDC)
    print('It looks like this is your first time running this program, or you have deleted some files :)')
    print('This guide will help you get started with the program\n')
    print(main.bcolors.WARNING + 'This directory will be used to store the anime and the assets' + main.bcolors.ENDC)
    print(main.bcolors.SECONDARY + 'Press enter to continue' + main.bcolors.ENDC)
    input()

    # check if the anime folder exists, if not create it
    if not os.path.exists('./anime'):
        os.makedirs('./anime')
    # check if the assets folder exists, if not create it
    if not os.path.exists('./assets'):
        os.makedirs('./assets')


    guide2()

def guide2():
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Step 1: Checking for updates and downloading assets' + main.bcolors.ENDC)
    print('We promise, it will be quick')

    version = getLatestVersion()
    # example response:
    # {
    #     "status": "outdated",
    #     "message": "Outdated program",
    #     "update": {
    #         "program": true,
    #         "assets": false
    #     },
    #     "updateNotes": {
    #         "program": "- Added update check feature \\n- Bug fixes\n- Added search feature \\n- Bug fixes\n",
    #         "assets": ""
    #     },
    #     "updateHash": {
    #         "program": "815c838037b739f29d33901ddcc50d952a958729c6eb25ce9b711d170a55dd02"
    #     }
    # }

    if version is None:
        print('Hmm, something went wrong with the update check')
        print('Do you have an internet connection? \n')
        print(main.bcolors.SECONDARY + 'PS: We need an internet connection to download the assets' + main.bcolors.ENDC)
        print(main.bcolors.SECONDARY + 'Press enter to exit' + main.bcolors.ENDC)
        input()
        exit()
    # check if the version is the same as the current version
    if version['status'] == 'error':
        print(main.bcolors.WARNING + 'Something went wrong with the update check' + main.bcolors.ENDC)
        print('Error:', version['message'])
        print('Please try again later\n')
        print(main.bcolors.SECONDARY + 'Press enter to exit' + main.bcolors.ENDC)
        input()
        exit()
    elif version['status'] == 'success':
        print('You are up to date')
        print(main.bcolors.SECONDARY + 'Press enter to continue' + main.bcolors.ENDC)
        input()
        guide3()
        return
    else:
        if version['update']['assets']:
            print(main.bcolors.OK + 'Downloading assets...' + main.bcolors.ENDC)
            print('Update notes:')
            print(version['updateNotes']['assets'] + '\n')
            downloadUpdate('assets', version['updateHash']['assets'])
        if version['update']['program']:
            print(main.bcolors.OK + 'There is a program update available' + main.bcolors.ENDC)
            print('Update notes:')
            print(version['updateNotes']['program'] + '\n')
            downloadUpdate('program', version['updateHash']['program'])
        else:
            print('No program update available')


        print(main.bcolors.SECONDARY + 'Press enter to continue' + main.bcolors.ENDC)
        input()
        guide3()
        return
    
def guide3():
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Step 2: Configuring the program' + main.bcolors.ENDC)
    print('We need to configure the program before we can continue')
    print('It is very simple, just answer a few questions')
    print(main.bcolors.SECONDARY + 'Press enter to continue' + main.bcolors.ENDC)
    input()
    guide4a()

def guide4a():
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Choose the option that describes you the best' + main.bcolors.ENDC)
    print('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)')
    print('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)')
    print('\n')
    print(main.bcolors.SECONDARY + 'Choose an option by pressing the number' + main.bcolors.ENDC)
    option = input()
    if option == '1':
        saveSetting('mode', 'archive')
    elif option == '2':
        saveSetting('mode', 'download')
    else:
        print('Invalid option, try again')
        guide4a()
        return
    guide5()

def guide5():
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Thats it, you are ready to go' + main.bcolors.ENDC)
    print('You can now start downloading anime')
    print('\n')
    print('Press i to read the instructions')
    print('Press enter to just freakin start the program')
    key = input()
    if key == 'i':
        showInstructions()
    startUi()
    return



def showInstructions():
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Instructions' + main.bcolors.ENDC)
    print('1. Download Assistant')
    print('This option will guide you through the download process, you just need to enter the url of the anime')
    print('2. Manual Download')
    print('This option will download everything from the given url')
    print('3. Continue Download')
    print('This option will continue the download from the last download')
    print('4. Serve content')
    print('This option will start a http server with document root to the anime folder')
    print('5. Clean up')
    print('This option will delete non finished downloads, after deleting you can\'t resume the download')
    print('6. Setup anime folder')
    print('This option will setup the anime folder with the given url')
    print('7. Get anime info')
    print('This option will get the anime info from the given url')
    print('0. Settings')
    print('This option will show the settings')
    print('q. Quit')
    print('\n')
    print('Press enter to continue')
    input()
    startUi()
    return
        

def saveSetting(key, value):
    # save the setting to the settings.json file
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
    data[key] = value
    with open('settings.json', 'w') as f:
        json.dump(data, f, indent=4)
    return    

def guideUpdateFinished():
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Update finished' + main.bcolors.ENDC)
    print('The program has been updated, YIPPIE!')
    print('Press enter to continue')
    input()
    guide3()

def checkForUpdates():
    firstRun()
    clearConsole()
    main.showLogo()
    print('Loading...')
    version = getLatestVersion()
    if version is None:
        print('No internet connection, skipping update check')
        return
    if version['status'] == 'error':
        print('Something went wrong with the update check')
        print('Error:', version['message'])
        time.sleep(2)
        return
    elif version['status'] == 'success':
        print('You are up to date')
        return
    else:
        if version['update']['assets']:
            print('Downloading assets...')
            downloadUpdate('assets', version['updateHash']['assets'])
        if version['update']['program']:
            print('There is a program update available')
            downloadUpdate('program', version['updateHash']['program'])
    return

def getLatestVersion():
    print('Checking for updates...', end='')
    # check if an internet connection is available
    try:
        requests.get('https://api.jm26.net/status.txt')
    except requests.exceptions.ConnectionError:
        print(' Skipped')
        print(main.bcolors.WARNING + 'No internet connection' + main.bcolors.ENDC)
        time.sleep(2)
        return

    url = 'https://api.jm26.net/update/aniworld-down/check/'
    programVersion = main.thisVersion()
    # get assets version from assets/.version file
    if not os.path.exists('./assets/.version'):
        with open('./assets/.version', 'w') as f:
            f.write('0.0.0')
    with open('./assets/.version', 'r') as f:
        assetsVersion = f.read()
    data = {
        'program': programVersion,
        'assets': assetsVersion,
    }
    response = requests.post(url, data=data)
    data = response.json()
    print(' Done')
    return data

def downloadUpdate(type, hash):
    print('Downloading update...')
    url = f'https://api.jm26.net/update/aniworld-down/download/?type={type}&hash={hash}'
    filepath = './update/update.zip'

    if isWindows():
        url = url + '&os=windows'

    # create the update folder if it doesn't exist
    if not os.path.exists('./update'):
        os.makedirs('./update')
    # download the file
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(main.bcolors.WARNING + 'No internet connection' + main.bcolors.ENDC)
        print('Please try again later')
        print('Press enter to exit')
        input()
        exit()

    # if response is json, something went wrong
    if response.headers['Content-Type'] == 'application/json':
        print(main.bcolors.WARNING + 'Something went wrong with the download' + main.bcolors.ENDC)
        print('Error:', response.text)
        print('Please try again later')
        print('Press enter to exit')
        input()
        exit()
    print(main.bcolors.OK + 'Download complete' + main.bcolors.ENDC)
    
    # write the file
    with open(filepath, 'wb') as f:
        f.write(response.content)
    # extract the file
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall('./update')

    # remove the zip file
    os.remove(filepath)
    # move the files and overwrite the old files
    for file in os.listdir('./update'):
        # if is a folder, move the files inside to the root folder / [folder] / [file]
        if os.path.isdir(f'./update/{file}'):
            # check if the folder exists in the root folder
            if not os.path.exists(f'./{file}'):
                os.makedirs(f'./{file}')
            # move the files inside the folder to the folder in the root folder
            for f in os.listdir(f'./update/{file}'):
                # overwrite the files
                shutil.move(os.path.join(f'./update/{file}', f), os.path.join(f'./{file}', f))

            # remove the folder
            os.rmdir(f'./update/{file}')
        else:
            # overwrite the files
            shutil.move(os.path.join('./update', file), os.path.join('./', file))

    # remove the update folder
    os.rmdir('./update')

    print(main.bcolors.OK + 'Update complete' + main.bcolors.ENDC)


    # if type is program, restart the program
    if type == 'program':
        # sleep 5 seconds but also allow user to skip the wait
        for i in range(3):
            print(f'\rRestarting in {3 - i} seconds', end='')
            time.sleep(1)
        print('\rRestarting program...')

        # if file settings.json doesn't exist
        if not os.path.exists('settings.json'):
            # check if main.exe exists, if it does, run it
            if isWindows():
                # run the exe file with guideUpdateFinished as argument
                os.system(f'{os.getcwd()}/AniWorld-Down.exe guideUpdateFinished')
            else:
            # start main.py with guideUpdateFinished as argument
                if os.name == 'nt':
                    os.system('py main.py guideUpdateFinished')
                else:
                    os.system(f'python3 main.py guideUpdateFinished')
        else:
            # restart the program with the same arguments
            if isWindows():
                os.system(f'{os.getcwd()}/AniWorld-Down.exe ' + ' '.join(sys.argv[1:]))
            else:
                if os.name == 'nt':
                    os.system('py main.py ' + ' '.join(sys.argv[1:]))
                else:
                    os.system('python3 main.py ' + ' '.join(sys.argv[1:]))
    return

def isWindows():
    # IS WINDOWS
    return False
    

def updateAnimeList():
    return
    print('Checking for updates...')
    file = 'https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database-minified.json'
    
    url = 'https://api.github.com/repos/manami-project/anime-offline-database/commits?path=anime-offline-database-minified.json&page=1&per_page=1'
    # get the latest commit date
    response = requests.get(url)
    data = response.json()
    last_commit_date = data[0]['commit']['committer']['date'][:10] # e.g. 2024-01-01

    # get the date from animeList.json
    # check if file exists
    if os.path.exists('./assets/animeList.json'):
        with open('./assets/animeList.json', 'r') as f:
            data = json.load(f)
        last_updated = data['lastUpdate'] # e.g. 2024-01-01
        # check if the file is up to date with the latest commit
        if last_updated == last_commit_date:
            print('Anime list is up to date')
            return
    
    # download the file
    print('Downloading anime list...')
    
    # download and display the progress bar
    wget.download(file, './assets/animeList.json')
    # decode unicode characters
    data = json.load(open('./assets/animeList.json', 'r', encoding='utf-8'))
    with open('./assets/animeList.json', 'w') as f:
        json.dump(data, f, indent=4)

    print('Anime list downloaded')
    return


def clearConsole():
    print('\033[H\033[J')
    return


# if file is run directly, run the main.py file instead
if __name__ == '__main__':
    main.handleCommands()
