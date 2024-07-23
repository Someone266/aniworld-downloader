# Streamtape direct link extractor
# Made by JMcrafter26 - https://github.com/JMcrafter26

import requests
import bs4
import js2py
import re
from yt_dlp import YoutubeDL

import dl_voe
import main

# var div = response.match(/<div id="ideoooolink" style="display:none;">([\s\S]*?)<\/div>/)[1];
#             // console.log(div);
            
#             var script = response.match(/<div id="norobotlink" style="display:none;">([\s\S]*?)<\/script>/)[1];
#             var content = script.match(/document.getElementById\('ideoooolink'\).innerHTML = (.*?);/)[1];
#             // content = content.replace(/['"]+/g, '');
#             // console.log(content);

#             // get the content between "+ (" and ").substring(1).substring(2)"
#             content = content.match(/\+ \((.*?)\)\.substring\(1\)\.substring\(2\)/)[1];
            
#             var directUrl = 'https://streamtape.com/get_video?' + content.split('?')[1];
#             // remove the "'" at the end of the string
#             directUrl = directUrl.slice(0, -1);


# <div id="robotlink" style="display:none;">/streamtape.com/get_video?id=rkA0Y8vJR6IbP1z&expires=1721824023&ip=FROODHxKD0gN&token=pQWpE1Z5xcde</div>
# <script>document.getElementById('ideoolink').innerHTML = "/streamtape.com/get_v" + ''+ ('xcdbideo?id=rkA0Y8vJR6IbP1z&expires=1721824023&ip=FROODHxKD0gN&token=pQWpE1Z5x2Jk').substring(1).substring(2);
# document.getElementById('ideoolink').innerHTML = "//streamtape.com/get_" + ''+ ('xnftbideo?id=rkA0Y8vJR6IbP1z&expires=1721824023&ip=FROODHxKD0gN&token=pQWpE1Z5x2Jk').substring(3).substring(1);
# document.getElementById('botlink').innerHTML = '//streamtape.com/get_'+ ('xyzavideo?id=rkA0Y8vJR6IbP1z&expires=1721824023&ip=FROODHxKD0gN&token=pQWpE1Z5x2Jk').substring(4);
# document.getElementById('robotlink').innerHTML = '//streamtape.com/get_'+ ('xcdvideo?id=rkA0Y8vJR6IbP1z&expires=1721824023&ip=FROODHxKD0gN&token=pQWpE1Z5x2Jk').substring(2).substring(1);
# </script>

def sdownload(url, retry=False):
    try:
        directUrl, name = sgetDirectUrl(url)
    except Exception as e:
        print(e)
        if not retry:
            print(main.bcolors.WARNING + 'Error getting direct url, retrying...' + main.bcolors.ENDC)
            return sdownload(url, True)
        else:
            print(main.bcolors.FAIL + 'Failed to get direct url! Try again later or switch to another hoster.' + main.bcolors.ENDC)
            return None
        

    name = name.replace('"', '')
    name = name.replace(' ', '_')
    name = name.replace('\n', '')
    name = name.replace('\r', '')

    ydl_opts = {'outtmpl' : name,}
    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(directUrl)
        except Exception as e:
            pass
            dl_voe.delpartfiles()
    
    return name


def sgetDirectUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=1"
    }
    html_page = requests.get(url, headers=headers)
    directUrl = ''
    soup = bs4.BeautifulSoup(html_page.content, 'html.parser')
    # <meta name="og:title" content="Death.Note.S01E01.German.720p.AAC.WebRip.x264-GSD.mp4">
    title = soup.find('meta', attrs={"name":"og:title"})['content']
    # get the script tag after the div <div id="robotlink" style="display:none;">...</div>
    script = soup.find('div', id='robotlink').find_next('script')
    content = script.text

    # get the last line that starts with 'document.getElementById('ide{...}')' by searching for it
    content = content.split('\n')
    search = []
    for line in content:
        if line.startswith('document.getElementById(\'ide'):
            search.append(line)
    # get the last item in the list
    content = search[-1]

    content = content.split('document.getElementById')[1]
    content = content.split('innerHTML = ')[1]
    content = content.rstrip(';')


    # interpret the js function in python
    content = js2py.eval_js(content)
    content = content.split('?')[1]

    # if it does not start with id=
    if not content.startswith('id='):
        content = 'id=' + re.sub(r'^.*?=', '', content)

    directUrl = 'https://streamtape.com/get_video?' + content
    # directUrl = directUrl.rstrip("'")

    print(directUrl)

    # return direct url and the title
    return directUrl, title

# if __name__ == '__main__':
#     url = 'https://streamtape.com/e/jk4AJe4Pxgcz0ag'
#     sdownload(url)