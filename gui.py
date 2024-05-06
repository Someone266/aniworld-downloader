import os
import time

import main
import functions
import update


def startUi():
    functions.clearConsole()
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
        url = functions.validateUrl(url)
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
        functions.serveContent()
    # if the key is 4, run the clean up
    elif key == '5':
        functions.clean()
    # if the key is 5, run the setup anime folder
    elif key == '6':
        print('Enter the url of the anime')
        url = input()
        url = functions.validateUrl(url)
        if not url:
            print(main.bcolors.WARNING + 'Invalid url' + main.bcolors.ENDC)
            time.sleep(2)
            startUi()
            return
        info = functions.getInfo(url)
        functions.setup(info)
    # if the key is 6, run the get anime info
    elif key == '7':
        print('Enter the url of the anime')
        url = input()
        url = functions.validateUrl(url)
        if not url:
            print(main.bcolors.WARNING + 'Invalid url' + main.bcolors.ENDC)
            time.sleep(2)
            startUi()
            return
        print(functions.getInfo(url))
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




def guide1():
    functions.clearConsole()
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
    functions.clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Step 1: Checking for updates and downloading assets' + main.bcolors.ENDC)
    print('We promise, it will be quick')

    version = update.getLatestVersion()
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
            update.downloadUpdate('assets', version['updateHash']['assets'])
        if version['update']['program']:
            print(main.bcolors.OK + 'There is a program update available' + main.bcolors.ENDC)
            print('Update notes:')
            print(version['updateNotes']['program'] + '\n')
            update.downloadUpdate('program', version['updateHash']['program'])
        else:
            print('No program update available')


        print(main.bcolors.SECONDARY + 'Press enter to continue' + main.bcolors.ENDC)
        input()
        guide3()
        return
    
def guide3():
    functions.clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Step 2: Configuring the program' + main.bcolors.ENDC)
    print('We need to configure the program before we can continue')
    print('It is very simple, just answer a few questions')
    print(main.bcolors.SECONDARY + 'Press enter to continue' + main.bcolors.ENDC)
    input()
    guide4a()

def guide4a():
    functions.clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Choose the option that describes you the best' + main.bcolors.ENDC)
    print('1. I want to archive anime and have it nicely organized (with filestructure, prictures and an offline webserver)')
    print('2. I just want to download anime fast and continue watching (No filestructure, ready to watch or move)')
    print('\n')
    print(main.bcolors.SECONDARY + 'Choose an option by pressing the number' + main.bcolors.ENDC)
    option = input()
    if option == '1':
        functions.saveSetting('mode', 'archive')
    elif option == '2':
        functions.saveSetting('mode', 'download')
    else:
        print('Invalid option, try again')
        guide4a()
        return
    guide5()

def guide5():
    functions.clearConsole()
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
    functions.clearConsole()
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