import voe
import settings
import main

import os
import shutil
import time
import json

def main(path, season, episode):
    # if path and season and episode are set, check if the file already exists
    if path is not None and season is not None and episode is not None:
        if os.path.exists(f"{path}/video/{season}/{episode}.mp4"):
            print(f"{main.bcolors.WARNING}File {path}/video/{season}/{episode}.mp4 already exists. Skipping...{main.bcolors.ENDC}")
            return
    
    # check if download folder exists
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # get the last part of path (after anime)
    name = path.split('anime/')[1]
    # check if the folder in downloads exists
    if not os.path.exists(f'downloads/{name}'):
        os.makedirs(f'downloads/{name}')
    
    prefHost = settings.getSetting('prefHost')
    with open(f'{path}/stream.json', 'r') as f:
        streams = json.load(f)

    os.chdir(f'downloads/{name}')


    # get the preferred host
    prefHost = 'voe' # only voe is supported for now



    if prefHost == 'voe':
        # get the download link from streams.json

        url = streams['voe'][str(season)][str(episode)]
        fileName = voe.download(url)
    elif prefHost == 'streamtape':
        # streamtape.download(url)
        pass
    else:
        print('Invalid host')
        time.sleep(2)
        return
    
    if fileName is None:
        print(f'{main.bcolors.FAIL}Download failed{main.bcolors.ENDC}')
        time.sleep(2)
        return
    
    
    # change directory back to the original directory
    os.chdir('../../')
    
    os.makedirs(f"{path}/video/{season}", exist_ok=True)
    # set filename to downloads/[name]/[filename]
    fileName = f"downloads/{name}/{fileName}"
    shutil.move(f"{fileName}", f"{path}/video/{season}/{episode}.mp4")

    print(f"Moved to {path}/video/{season}/{episode}.mp4")

    return    
