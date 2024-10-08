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
    print('2. Continue Download')
    print('3. Serve content')
    print('4. Clean up')
    print('5. Open anime folder')
    print('6. Get anime info')
    print('0. Settings')
    print('h. Help/Info')
    print('q. Quit')

    # get the key from the user
    key = input()
    # if the key is not in the list, return
    if key not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'Q', 'h', 'i']:
        print('Invalid key')
        startUi()
        return
    # if the key is 1, run the automatic anime download
    if key == '1':
        main.runAuto()
    # if the key is 2, run the manual anime download
    elif key == 'x':
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
    elif key == '2':
        print('Not implemented yet')
        time.sleep(2)
        startUi()
    # if the key is 3, run the serve content
    elif key == '3':
        functions.serveContent()
    # if the key is 4, run the clean up
    elif key == '4':
        functions.clean()
    # if the key is 5, run the setup anime folder
    elif key == '5':
        # print('Enter the url of the anime')
        # url = input()
        # url = functions.validateUrl(url)
        # if not url:
        #     print(main.bcolors.WARNING + 'Invalid url' + main.bcolors.ENDC)
        #     time.sleep(2)
        #     startUi()
        #     return
        # info = functions.getInfo(url)
        # functions.setup(info)

        # open anime folder, based on the os and the available file explorer
        if os.name == 'nt':
            os.system('start .\\anime')
        elif os.name == 'posix':
            os.system('xdg-open .\\anime')
        else:
            print('Unsupported os')
            print('The anime folder is located in the following directory:')
            # get the current script directory
            print(os.getcwd() + '\\anime')
            print('\nPress enter to continue')
            input()
            startUi()
        startUi()

    elif key == '6':
        print('Enter the url of the anime')
        url = input()
        url = functions.validateUrl(url)
        if not url:
            print(main.bcolors.WARNING + 'Invalid url' + main.bcolors.ENDC)
            time.sleep(2)
            startUi()
            return
        print(functions.getInfo(url))
    elif key == '0':
        functions.showSettings()
        startUi()
    elif key == 'h' or key == 'i':
        functions.clearConsole()
        main.showLogo()
        print(main.bcolors.PRIMARY + 'Info' + main.bcolors.ENDC)
        print('\n')
        print(f'{main.bcolors.OK}This program was made by JMcrafter26 and published by Someone266 on Github{main.bcolors.ENDC}')
        print(f'{main.bcolors.OK}The program is open source and can be found here: https://github.com/Someone266/aniworld-downloader/{main.bcolors.ENDC}')
        print('\n')
        print('This program is still in development, so there might be some bugs')
        print('If you find a bug, please report it on the Github page')
        print('\n')
        # the developer nor the publisher is responsible for any damage caused by the program
        print(f'{main.bcolors.OK}This program is for educational purposes only, the developer nor the publisher is responsible for any damage caused by the program. This program is not affiliated with any of the anime sites. This program is provided as is, without any warranty. Use at your own risk.{main.bcolors.ENDC}')
        print('\n')
        print('Press enter to continue (i to report a bug)')
        key = input()
        if key == 'i':
            print('Opening the Github page...')
            # https://github.com/Someone266/aniworld-downloader/issues
            if os.name == 'nt':
                os.system('start https://github.com/Someone266/aniworld-downloader/issues')
                time.sleep(2)
            elif os.name == 'posix':
                os.system('xdg-open https://github.com/Someone266/aniworld-downloader/issues')
                time.sleep(2)
            else:
                print('Unsupported os')
                print('The Github page is located at the following link:')
                print('https://github.com/Someone266/aniworld-downloader/issues')
                print('\nPress enter to continue')
                input()


        import settings
        functions.clearConsole()
        main.showLogo()
        print(main.bcolors.PRIMARY + 'Info' + main.bcolors.ENDC)
        print('\n')
        print(f'{main.bcolors.OK}Your Version is: {main.thisVersion()}{main.bcolors.ENDC}')
        if(functions.isWindows()):
            print(f'{main.bcolors.OK}You are running the windows version (Congratulations){main.bcolors.ENDC}')
        print(f'{main.bcolors.OK}Your mode is: ' + settings.getSetting("mode") + f'{main.bcolors.ENDC}')
        print(f'{main.bcolors.OK}Your preferred host is: ' + settings.getSetting("prefHost") + f'{main.bcolors.ENDC}')
        if settings.getSetting("autoUpdate") == 'yes':
            print(f'{main.bcolors.OK}Auto update is enabled{main.bcolors.ENDC}')
        else:
            print(f'{main.bcolors.WARNING}Auto update is disabled{main.bcolors.ENDC}')
            print(f'{main.bcolors.WARNING}You might miss out on new features and bug fixes{main.bcolors.ENDC}')
            print(f'{main.bcolors.PRIMARY}Press SPACE to check and download updates{main.bcolors.ENDC}')



        print('\n')
        key = input()
        if key == ' ':
            update.checkForUpdates(True)
            time.sleep(2)
            startUi()
            return

        showInstructions()
        
    elif key == 'q' or key == 'Q':
        print('Quitting, Bye!')
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
    guide4b()

def guide4b():
    functions.clearConsole()
    main.showLogo()
    print(main.bcolors.PRIMARY + 'Select your preferred host' + main.bcolors.ENDC)
    print('1. Voe (Recommended)')
    print('2. Streamtape')
    print('\n')
    print(main.bcolors.SECONDARY + 'Choose an option by pressing the number' + main.bcolors.ENDC)
    option = input()
    if option == '1':
        functions.saveSetting('prefHost', 'voe')
    elif option == '2':
        functions.saveSetting('prefHost', 'streamtape')
    else:
        print('Invalid option, try again')
        guide4b()
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
    print('2. Continue Download')
    print('This option is not implemented yet')
    print('3. Serve content')
    print('This option will start a webserver to serve the content - you can watch the anime in your browser (even offline and other devices)')
    print('4. Clean up')
    print('This option will clean up the program and the assets')
    print('5. Open anime folder')
    print('This option will open the anime folder where the anime is stored')
    print('6. Get anime info')
    print('This option will get the info of the anime from the url')
    print('0. Settings')
    print('This option will allow you to change the settings of the program')
    print('h. Help/Info')
    print('This is the current screen :)')
    print('q. Quit')
    print('\n')
    print('Press enter to continue')
    input()
    startUi()
    return