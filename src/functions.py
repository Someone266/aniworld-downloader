import wget
import requests
import os
import re
import json
import time
import sys
import bs4
import http.server
import shutil

import main
import gui
import main
import dl_download
import settings

def setTitle(title = 'AniWorld Scraper'):
    # set the title of the console
    if os.name == 'nt':
        os.system(f'title {title}')
    else:
        print(f'\033]0;{title}\007')
    return


def getInfo(url):

    
    # if url has not aniworld.to in it, return
    if 'aniworld.to' not in url:
        print(main.bcolors.WARNING + 'Invalid url! Please enter a valid aniworld.to url' + main.bcolors.ENDC)
        time.sleep(2)
        return
    
        # if url contains /filme/, write unsupported (for now)
    if not 'anime/stream' in url:
        print(main.bcolors.WARNING + 'This type of url is not supported yet. It may be supported in the future' + main.bcolors.ENDC)
        time.sleep(2)
        return

    # get the html content of the page
    response = requests.get(url)
    html = response.text
    # DEBUG: save the html to a file
    # with open('temp.html', 'w', encoding='utf-8') as f:
        # f.write(html)

    if 'DDoS-Guard' in html:
            print(f'{main.bcolors.WARNING}DDoS-Guard detected{main.bcolors.ENDC}')
            print('Or paste your cookie key in the settings')
            time.sleep(2)
            return

    soup = bs4.BeautifulSoup(html, 'html.parser')
    # extract the title by finding the element with the class series-title and getting the inner text
    title = soup.find('div', class_='series-title').find('h1').string
    # get the inner text of the title
    title = title.strip()
    # get the span element inside the title
    title = title.split('\n')[0]
    print('Getting info for:', title)
    # extract the description by finding the element with the class seri_des and data-full-description using bs4
    description = soup.find('p', class_='seri_des').get('data-full-description')
    # get the start and enddate, startdate itemprop="startDate"
    startdate = soup.find('span', itemprop='startDate').string
    enddate = soup.find('span', itemprop='endDate').string

    # if enddate is 'heute', set the status to ongoing, else set it to finished
    if enddate == 'heute':
        status = 'ONGOING'
    else:
        status = 'FINISHED'

    # get the number of seasons
    # seasons = soup.find('meta', itemprop='numberOfSeasons').get('content') # not working
    # get the number of seasons by counting the number of li elements
    seasons = soup.find('strong', string='Staffeln:').parent.parent.parent.find_all('li')
    # check if li text is not numeric, if it is remove it
    seasons = [season.text for season in seasons]

    # print(seasons)
    # input()
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
    tags = [tag.string for tag in tags]

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
    relPath = f'./{pathname}'

    # create the folder
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    # create the info.json file, but first utf-8 encode the data
    with open(f'{pathname}/info.json', 'w') as f:
        json.dump(info, f, indent=4)

    # get the filetype of the image
    filetype = info['picture'].split('.')[-1]
    # download the image, but first check if the image exists
    if not os.path.exists(f'{relPath}/image.{filetype}'):
        wget.download(info['picture'], f'{relPath}/image.{filetype}')
    
    # replace picture with the image path
    info['picture'] = f'image.{filetype}'
    info['pathname'] = relPath

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
        'pathname': relPath,
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
    # with open('./assets/template.html', 'r') as f:
    #     template = f.read()
    
    # # replace the placeholders with the info
    # template = template.replace('%title%', info['title'])
    # template = template.replace('%description%', info['description'])
    # template = template.replace('%startDate%', info['startdate'])
    # template = template.replace('%endDate%', info['enddate'])
    # template = template.replace('%status%', info['status'])
    # template = template.replace('%totalEpisodes%', str(info['totalEpisodes']))
    # template = template.replace('%seasons%', str(info['seasons']))
    # template = template.replace('%picture%', f'image.{filetype}')
    # template = template.replace('%trailer%', info['trailer'])
    # template = template.replace('%producer%', info['producer'])
    # template = template.replace('%fsk%', info['fsk'])
    # template = template.replace('%imdb%', info['imdb'])
    # template = template.replace('%tags%', ', '.join(info['tags']))

    # # create the info.html file, but first utf-8 encode the data
    # template = template.encode('utf-8')
    # with open(f'{pathname}/info.html', 'wb') as f:
    #     f.write(template)
    print('Anime folder setup complete')
    return

def getSeasonDownloads(url, season, episodes = None, info = None):
    if episodes is None:
        # get the episodes of the season
        response = requests.get(url)
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        # get the ul where Episoden is in the span
        episodes = soup.find('strong', string='Episoden:').parent.parent.parent
        # get the number of episodes by counting the number of li elements
        episodes = episodes.find_all('li')
        # get the number of episodes by counting the number of li elements
        episodes = len(episodes) - 1
    
    print(f'Getting streams for season {season} with {episodes} episodes...')

    path = f'{info["title"]} ({info["startdate"]}-{info["enddate"]})'
    path = re.sub(r'[<>:"/\\|?*]', '', path)
    print('Path:', path)

    # check if season already exists in the json file
    if os.path.exists('anime/' + path + '/stream.json'):
        with open('anime/' + path + '/stream.json', 'r') as f:
            data = json.load(f)
            print('Found stream.json')
            print('Checking if season already exists...')
            if "voe" in data:
                # check if it has minimum episodes of 1
                if len(data["voe"][str(season)]) >= 1:
                    print('Season stream urls already exist')
                    return data
            if "streamtape" in data:
                # check if it has minimum episodes of 1
                if len(data["streamtape"][str(season)]) >= 1:
                    print('Season stream urls already exist')
                    return data         
    else:
        data = {}

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

    if 'DDoS-Guard' in html:
        print(f'{main.bcolors.WARNING}DDoS-Guard detected{main.bcolors.ENDC}')
        print('Or paste your cookie key in the settings')
        time.sleep(2)
        return

    soup = bs4.BeautifulSoup(html, 'html.parser')
    # save link to json file
    if info is not None:
        pathname = f'{info["title"]} ({info["startdate"]}-{info["enddate"]})'

        # remove special characters from the pathname
        pathname = re.sub(r'[<>:"/\\|?*]', '', pathname)
        pathname = f'anime/{pathname}/stream.json'
    else:
        pathname = f'stream.json'

    # get the parent of i element class="icon VOE"
    voeDownloadLink = soup.find('i', class_='icon VOE')
    # if the download element is not found, return
    if voeDownloadLink is None:
        print('No voe download found, skipping...')
        return
    # get the parent of the i element
    voeDownloadLink = voeDownloadLink.parent
    # get the href of the a element
    voeDownloadLink = voeDownloadLink.get('href')
    voeDownloadLink = 'https://aniworld.to' + voeDownloadLink
    streamUrl = redirectUrl(voeDownloadLink)
    if streamUrl is None:
        print('No stream url found')
        return
    
    

    # add the stream url inside the season array
    # e.g.
    # {
    #   "voe": {
    #        "1": {
    #            "1": "https://voe.sx/e/1234567890",
    #           "2": "https://voe.sx/e/1234567891",
    #       }  
    #   }
    # }
    if os.path.exists(pathname):
        with open(pathname, 'r') as f:
            data = json.load(f)
    else:
        data = {}
    if str("voe") not in data:
        data["voe"] = {}
    if str(season) not in data["voe"]:
        data["voe"][str(season)] = {}
    data["voe"][str(season)][str(episode)] = streamUrl
    
    with open(pathname, 'w') as f:
        json.dump(data, f, indent=4)
    
    # get streamtape download link
    streamtapeDownloadLink = soup.find('i', class_='icon Streamtape')
    # if the download element is not found, return
    if streamtapeDownloadLink is None:
        print('No streamtape download found, skipping...')
        return
    # get the parent of the i element
    streamtapeDownloadLink = streamtapeDownloadLink.parent
    # get the href of the a element
    streamtapeDownloadLink = streamtapeDownloadLink.get('href')
    streamtapeDownloadLink = 'https://aniworld.to' + streamtapeDownloadLink
    streamUrl = redirectUrl(streamtapeDownloadLink)
    if streamUrl is None:
        print('No stream url found')
        return
    

    # add the stream url inside the season array
    if os.path.exists(pathname):
        with open(pathname, 'r') as f:
            data = json.load(f)
    else:
        data = {}
    if str("streamtape") not in data:
        data["streamtape"] = {}
    if str(season) not in data["streamtape"]:
        data["streamtape"][str(season)] = {}
    data["streamtape"][str(season)][str(episode)] = streamUrl

    with open(pathname, 'w') as f:
        json.dump(data, f, indent=4)
    
    if data["voe"][str(season)][str(episode)] is not None:
        return data["voe"][str(season)][str(episode)]
    else:
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
    episodes = soup.find('strong', string='Episoden:').parent.parent.parent
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
    # streamUrl = data[str(season)][str(episode)]
    # print(streamUrl)
    dl_download.dmain(pathname, season, episode)

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
    for episode in data["voe"][str(season)]:
        # streamUrl = data[str(season)][episode]
        clearConsole()
        main.showLogo()
        print(f'Downloading season {season} episode {episode}...')
        updateProgress(int(episode) / len(data["voe"][str(season)]))
        print("\n")
        dl_download.dmain(pathname, season, episode)

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
        # streamUrl = data[str(season)][str(episode)]
        clearConsole()
        main.showLogo()
        print(f'Downloading season {season} episode {episode}...')
        updateProgress((episode - start) / (end - start))
        print("\n")
        dl_download.dmain(pathname, season, episode)
    
    return

def searchAnime(query):
    # debug
    # query = 'Solo Leveling'
    # query = '+'.join(query.split(' '))

    if query == '' or query == None:
        print(main.bcolors.WARNING + 'No query entered' + main.bcolors.ENDC)
        time.sleep(2)
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
    # DEBUG: save the data to a file
    # with open('search.html', 'w', encoding='utf-8') as f:
        # f.write(data)
        
    try:
        data = json.loads(data)
    except:
        # if data contains DDoS-Guard
        if 'DDoS-Guard' in data:
            print(f'{main.bcolors.WARNING}DDoS-Guard detected{main.bcolors.ENDC}')
            print('Or paste your cookie key in the settings')
            time.sleep(2)
            return
        print(f'{main.bcolors.WARNING}Error parsing JSON{main.bcolors.ENDC}')
        print('Try again later')
        time.sleep(2)
        return

    
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
    # with open('search.txt', 'w') as f:
        # json.dump(data, f, indent=4)
    
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
    url = 'https://aniworld.to' + link
    print('Aniworld URL:', url)
    return url


def serveContent():
    # start a http server with document root to the anime folder
    PORT = 3333
    Handler = http.server.SimpleHTTPRequestHandler
    web_dir = os.path.join(os.getcwd(), 'anime')
    os.chdir(web_dir)
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        print("serving at http://localhost:" + str(PORT) + "/")
        # get the network ip assigned to the computer (usually 192.168.1.x)

        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()
    return

def clean():
    clearConsole()
    main.showLogo()
    print('Running cleanup...')

    # get files in ./downloads/ and its subdirs that end with .part
    files = [os.path.join(root, f) for root, dirs, files in os.walk('./downloads') for f in files if f.endswith('.part') or f.endswith('.ytdl')]

    # if there are no files, return
    if files:
        print(main.bcolors.WARNING + 'Do you want to delete non finished downloads? After deleting you have to restart the download' + main.bcolors.ENDC)
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
        # remove stream.json
        if os.path.exists(f'anime/{folder}/stream.json'):
            os.remove(f'anime/{folder}/stream.json')
        
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

        # if pathname includes anime/, remove anime/
        if 'anime/' in info['pathname']:
            info['pathname'] = info['pathname'].replace('anime/', '')



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
            'pathname': f'{folder}',
        })
    with open('./anime/index.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print('Cleaning file structure...')
            # if index.html exists, remove it
    if os.path.exists('index.html'):
        os.remove('index.html')
    
    # remove files
    removeFiles = [
        # 'functions.py',
        # 'voe.py'
        'urls.txt',
        'search.html',
        'search.txt',
        'temp.html',
        'update.bat',
        'update.exe',
    ]
    print('Removing unused files...')
    for file in removeFiles:
        if os.path.exists(file):
            os.remove(file)
            print('Removed:', file)
    
    # if assets folder exists, remove it
    if os.path.exists('assets'):
        # remove all files inside the assets folder and the folder itself
        shutil.rmtree('assets')
        print('Removed: assets/')
    
    # check if downloads folder exists
    if os.path.exists('downloads'):
        # check for empty folders inside downloads/
        folders = [f for f in os.listdir('downloads') if os.path.isdir(os.path.join('downloads', f))]
        for folder in folders:
            if not os.listdir(f'downloads/{folder}'):
                os.rmdir(f'downloads/{folder}')
                print('Removed:', f'downloads/{folder}')
    
    buildDownloadsJson()
    
    print('Done')
    print('Press enter to continue')
    # return to main menu
    input()
    gui.startUi()
    return

def buildDownloadsJson():
    # get all the episodes inside anime/[animename]/video/[season]/[episode].mp4 and set the status to downloaded
    # e.g.:
    # {
    #     "title": "Solo Leveling",
    #     "1": {
    #         "1": "downloaded",    
    #         "2": "downloaded",
    #         "3": "downloaded"
    #     },
    #     "2": {
    #         "1": "downloaded",
    #         "2": "downloaded"
    #     }
    # }
    # get all folders in the anime folder
    folders = [f for f in os.listdir(os.path.join(os.getcwd(), 'anime')) if os.path.isdir(os.path.join(os.getcwd(), 'anime', f))]
    # remove assets from folders
    if 'assets' in folders:
        folders.remove('assets')
    

    data = {}
    for folder in folders:
        # get all files in the video folder
        videos = [f for f in os.listdir(os.path.join(os.getcwd(), 'anime', folder, 'video')) if os.path.isfile(os.path.join(os.getcwd(), 'anime', folder, 'video', f))]
        # get all seasons
        seasons = [f for f in os.listdir(os.path.join(os.getcwd(), 'anime', folder, 'video')) if os.path.isdir(os.path.join(os.getcwd(), 'anime', folder, 'video', f))]
        data[folder] = {}
        for season in seasons:
            data[folder][season] = {}
            episodes = [f for f in os.listdir(os.path.join(os.getcwd(), 'anime', folder, 'video', season)) if os.path.isfile(os.path.join(os.getcwd(), 'anime', folder, 'video', season, f))]
            for episode in episodes:
                epName = episode.split('.')[0]
                data[folder][season][epName] = 'downloaded'
    # if path downloads does not exist, create it
    if not os.path.exists(os.path.join(os.getcwd(), 'downloads')):
        os.makedirs(os.path.join(os.getcwd(), 'downloads'))
    
    # save the data to downloads.json
    with open(os.path.join(os.getcwd(), 'downloads/downloads.json'), 'w') as f:
        json.dump(data, f, indent=4)

    print('downloads.json rebuilt')
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
        gui.guide1()
        return
    # if file update.bat exists, delete it
    if os.path.exists('update.bat'):
        os.remove('update.bat')
    else:
        # check if the anime folder exists, if not create it
        if not os.path.exists('./anime'):
            os.makedirs('./anime')
        # check if the assets folder exists, if not create it
        # if not os.path.exists('./assets'):
            # os.makedirs('./assets')

    
        

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
    # if file update.bat exists, delete it
    if os.path.exists('update.bat'):
        os.remove('update.bat')
    clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Update finished' + main.bcolors.ENDC)
    print('The program has been updated, YIPPIE!')
    print('Press enter to continue')
    input()
    gui.guide3()

def showSettings():
    settings.menu()
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


# # if file is run directly, run the main.py file instead
# if __name__ == '__main__':
#     main.handleCommands()
