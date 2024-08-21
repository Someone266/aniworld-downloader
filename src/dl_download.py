import dl_voe
import settings
import main
import dl_streamtape

import os
import shutil
import time
import json

def dmain(path, season, episode):
    # if path and season and episode are set, check if the file already exists
    if path is not None and season is not None and episode is not None:
        if os.path.exists(f"{path}/video/{season}/{episode}.mp4"):
            print(f"{main.bcolors.WARNING}File {path}/video/{season}/{episode}.mp4 already exists. Skipping...{main.bcolors.ENDC}")
            return

    # check if download folder exists
    if not os.path.exists(os.getcwd() + '/downloads'):
        os.makedirs(os.getcwd() + '/downloads')
    
    # get the last part of path (after anime)
    name = path.split('anime/')[1]
    # check if the folder in downloads exists
    if not os.path.exists(f'downloads/{name}'):
        os.makedirs(f'downloads/{name}')
    
    prefHost = settings.getSetting('prefHost')
    with open(f'{path}/stream.json', 'r') as f:
        streams = json.load(f)

    os.chdir(f'downloads/')

    # check if downloads.json exists
    if not os.path.exists('downloads.json'):
        with open('downloads.json', 'w') as f:
            json.dump({}, f)
    
    # get the downloads.json file
    with open('downloads.json', 'r') as f:
        downloads = json.load(f)
    
    # check if the current anime episode is in the downloads.json file marked as downloading
        # {
    #     "title": "Solo Leveling",
    #     "1": {
    #         "1": "downloaded",    
    #         "2": "downloaded",
    #         "3": "downloaded"
    #     },
    #     "2": {
    #         "1": "downloaded",
    #         "2": "downloading"
    #     }
    # }

    # check if is in downloads[title][season][episode] = downloading
    if name in downloads and season in downloads[name] and episode in downloads[name][season]:
        # do nothing
        print()
    else:
        downloads.setdefault(name, {}).setdefault(season, {})[episode] = 'downloading'
    
    # write the downloads.json file
    with open('downloads.json', 'w') as f:
        json.dump(downloads, f)
    
    # cd to the downloads/[name] folder
    os.chdir(f'{name}')

    # get the preferred host
    # prefHost = 'voe' # only voe is supported for now
    if prefHost == 'voe':
        # get the download link from streams.json

        url = streams['voe'][str(season)][str(episode)]
        fileName = dl_voe.vdownload(url)
    elif prefHost == 'streamtape':
        url = streams['streamtape'][str(season)][str(episode)]
        fileName = dl_streamtape.sdownload(url)
        # pass
    else:
        print('Invalid host')
        time.sleep(2)
        return
    
    if fileName is None:
        print(f'{main.bcolors.FAIL}Download failed{main.bcolors.ENDC}')
        os.chdir('../../')
        time.sleep(2)
        return
    
    
    # change directory back to the original directory
    os.chdir('../../')
    
    os.makedirs(f"{path}/video/{season}", exist_ok=True)
    # set filename to downloads/[name]/[filename]
    fileName = f"downloads/{name}/{fileName}"
    shutil.move(f"{fileName}", f"{path}/video/{season}/{episode}.mp4")

    print(f"Moved to {path}/video/{season}/{episode}.mp4")

    # os.chdir(os.getcwd() + '/downloads')
    # # change it to downloaded
    # with open('downloads.json', 'r') as f:
    #     downloads = json.load(f)

    # downloads.setdefault(name, {}).setdefault(season, {})[episode] = 'downloaded'
    # with open('downloads.json', 'w') as f:
    #     json.dump(downloads, f)

    # os.chdir('../')

    return    
