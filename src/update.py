import os
import sys
import time
import zipfile
import shutil
import requests

import main
import functions



def checkForUpdates():
    functions.firstRun()
    functions.clearConsole()
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
    # check if an endpoint is reachable
    try:
        # if https://api.jm26.net/status.txt status is 200, continue (5 seconds timeout)
        requests.get('https://api.jm26.net/status.txt', timeout=5)
    except requests.exceptions.ConnectionError:
        print(' Skipped')
        print(main.bcolors.WARNING + 'No internet connection' + main.bcolors.ENDC)
        time.sleep(2)
        return

    url = 'https://api.jm26.net/update/aniworld-down/check/'
    programVersion = main.thisVersion()
    # get assets version from assets/.version file
    if not os.path.exists('./anime/assets/.version'):
        assetsVersion = '0.0.0'
    else:
        with open('./anime/assets/.version', 'r') as f:
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

    if functions.isWindows():
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
    print('\n')
    # recommend the clean function
    print(f'{main.bcolors.WARNING}It is recommended to run the {main.bcolors.ENDC}{main.bcolors.OK}clean option{main.bcolors.ENDC}{main.bcolors.WARNING} after updating{main.bcolors.ENDC}')
    print('\n')


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
            if functions.isWindows():
                # run the exe file with guideUpdateFinished as argument
                # os.system(f'{os.getcwd()}/AniWorld-Down.exe guideUpdateFinished')
                # start update.bat in a new window
                os.system(f'start update.bat guideUpdateFinished')
            else:
            # start main.py with guideUpdateFinished as argument
                if os.name == 'nt':
                    os.system('py main.py guideUpdateFinished')
                else:
                    os.system(f'python3 main.py guideUpdateFinished')
        else:
            # restart the program with the same arguments
            if functions.isWindows():
                # os.system(f'{os.getcwd()}/AniWorld-Down.exe ' + ' '.join(sys.argv[1:]))
                # os.system(f'{os.getcwd()}/update.bat ' + ' '.join(sys.argv[1:]))
                os.system(f'start update.bat ' + ' '.join(sys.argv[1:]))
            else:
                if os.name == 'nt':
                    os.system('py main.py ' + ' '.join(sys.argv[1:]))
                else:
                    os.system('python3 main.py ' + ' '.join(sys.argv[1:]))
    return