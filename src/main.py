# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: see version variable below
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

import sys
import time

import functions
import gui
import update

# VERSION
version = "1.2.0"

class bcolors:
    PURPLE = '\033[95m' # #9b59b6
    SECONDARY = '\033[90m' # #7f8c8d

    PRIMARY = '\033[94m' # #3498db
    CYAN = '\033[96m' # #1abc9c
    OK = '\033[92m' # #2ecc71
    WARNING = '\033[93m' # #f1c40f
    FAIL = '\033[91m'  # #e74c3c
    ENDC = '\033[0m' 
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def runMain(url):
    functions.updateAnimeList()
    info = functions.getInfo(url)
    functions.setup(info)
    for season in info['episodes']:
        functions.getSeasonDownloads(url, season, info['episodes'][season], info)
    # functions.downloadSeason(1, info)
    seasons = info['seasons']
    print(seasons)
    for season in range(1, seasons + 1):
        functions.downloadSeason(season, info, url)

    functions.clean()
    showLogo()
    print(bcolors.OK + "Finished downloading all episodes" + bcolors.ENDC)
    print("\n")
    print(bcolors.PRIMARY + "Run 'serve' to watch the episodes in your browser" + bcolors.ENDC)
    return

def runAuto():
    functions.clearConsole()
    showLogo()
    functions.updateAnimeList()
    print(bcolors.OK + "This is the auto mode. It will ask you what to download." + bcolors.ENDC)
    print("\n")
    print("Enter the name of the anime you want to search for or paste the url of the anime")
    choice = input()
    if choice.startswith("http"):
        url = choice
        if 'aniworld.to' not in url:
            print(bcolors.WARNING + 'Invalid url! Please enter a valid aniworld.to url' + bcolors.ENDC)
            time.sleep(2)
            return
        
            # if url contains /filme/, write unsupported (for now)
        if not 'anime/stream' in url:
            print(bcolors.WARNING + 'This type of url is not supported yet. It may be supported in the future' + bcolors.ENDC)
            time.sleep(2)
            return
        # https://aniworld.to/anime/stream/death-note/staffel-1/episode-1
        # if it contains /episode-[number], remove it
        if '/episode-' in url:
            url = url.split('/episode-')[0]
        if '/staffel-' in url:
            url = url.split('/staffel-')[0]
        
    elif choice != "" and choice != None:
        url = functions.searchAnime(choice)
        if url == False:
            print("Quit")
            # return to the main menu
            gui.startUi()
            return
        elif 'aniworld.to' not in url:
            print(bcolors.WARNING + 'Invalid url! There was an error with the search' + bcolors.ENDC)
            time.sleep(2)
            return
    else:
        # main menu
        gui.startUi()
        return
        
    
    info = functions.getInfo(url)
    functions.setup(info)

        
    runAuto1(url, info)
    return

def runAuto1(url, info):
    showLogo()
    print(bcolors.OK + "Setup complete" + bcolors.ENDC)
    print("\n")
    print(bcolors.OK + "We found " + str(info['seasons']) + " seasons and a total of " + str(info['totalEpisodes']) + " episodes" + bcolors.ENDC)
    print("\n")
    print('Do you want to download all episodes? (Y/n)')
    downloadAll = input()
    if downloadAll != 'Y' and downloadAll != 'y' and downloadAll != 'yes' and downloadAll != 'Yes' and downloadAll != '':
        print("Which season do you want to download?")
        season = int(input())
        print("What episode do you want to download? (Enter 0 to download all episodes; use - to download a range of episodes)")
        episode = int(input())
        # check if the season and episode are valid
        if season < 1 or season > info['seasons']:
            print(bcolors.FAIL + "Invalid season" + bcolors.ENDC)
            time.sleep(2)
            runAuto1(url, info)
            return
        if episode == 0:
            functions.downloadSeason(season, info, url)
        # if episode contains a range
        elif '-' in str(episode) or ',' in str(episode):
            if '-' in str(episode):
                start = int(episode.split('-')[0])
                end = int(episode.split('-')[1])
                for e in range(start, end + 1):
                    functions.downloadEpisode(season, e, info, url)
            elif ',' in str(episode):
                # split the string by comma, loop through the list and download each episode
                episodes = episode.split(',')
                for e in episodes:
                    functions.downloadEpisode(season, int(e), info, url)
        else:
            if episode < 1 or episode > info['episodes'][season]:
                print(bcolors.FAIL + "Invalid episode" + bcolors.ENDC)
                time.sleep(2)
                runAuto1(url, info)
                return
            functions.downloadEpisode(season, episode, info, url)
    else:
        print(bcolors.OK + "Downloading all episodes" + bcolors.ENDC)
        for season in range(1, info['seasons'] + 1):
            functions.downloadSeason(season, info, url)

    
    print(bcolors.OK + "Download complete" + bcolors.ENDC)
    print("\n")
    print(bcolors.PRIMARY + "Press enter to return to the main menu" + bcolors.ENDC)
    input()
    # return to the main menu
    gui.startUi()

def thisVersion():
    return version



    
def runGetInfo(url):
    # update the anime list
    functions.updateAnimeList()

    info = functions.getInfo(url)
    return info

def runSetup(url):
    # update the anime list
    functions.updateAnimeList()

    info = functions.getInfo(url)
    functions.setup(info)
    return

def getSeasonStreams(url, season, info = None):
    # update the anime list
    functions.updateAnimeList()

    episodes = None
    if info is not None:
        episodes = info['episodes'][season]

    data = functions.getSeasonDownloads(url, season, episodes)
    return data

def getEpisodeStreams(url, season, episode, info = None):
    # update the anime list
    functions.updateAnimeList()

    if info is not None:
        episode = info['episodes'][season][episode]

    data = functions.getEpisodeDownloads(url, season, episode, info)
    return data

def runSearch():
    functions.clearConsole()
    showLogo()
    print("Enter the name of the anime you want to search for")
    name = input()
    return functions.searchAnime(name)


def showLogo():
    #     AA          W     W         ll     d     DDD                
    #    A  A      ii W     W          l     d     D  D               
    #    AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn 
    #    A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n
    #    A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n
                                                             
        

    print("\n")
    version = thisVersion()

    if functions.isWindows():
        version = version + " (Windows)"

    print(bcolors.CYAN + "    AA          W     W         ll     d     DDD                    " + bcolors.ENDC)
    print(bcolors.CYAN + "   A  A      ii W     W          l     d     D  D                   " + bcolors.ENDC)
    print(bcolors.CYAN + "   AAAA nnn     W  W  W ooo rrr  l   ddd     D  D ooo w   w nnn     " + bcolors.ENDC)
    print(bcolors.CYAN + "   A  A n  n ii  W W W  o o r    l  d  d     D  D o o w w w n  n    " + bcolors.ENDC)
    print(bcolors.CYAN + "   A  A n  n ii   W W   ooo r   lll  ddd     DDD  ooo  w w  n  n    " + bcolors.ENDC)
    print(bcolors.CYAN + "                                                                    " + bcolors.ENDC)
    print("A powerful scraper and downloader for AniWorld")
    print(" ")    
    print("Version: " + version + "                                 Made by JMcrafter26")
    print(bcolors.SECONDARY + "DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code." + bcolors.ENDC)
    print(bcolors.SECONDARY + "Please respect the laws of your country and the country of the website you are scraping." + bcolors.ENDC)
    print("\n")


    
def handleCommands():
    if len(sys.argv) == 1:
        sys.argv.append("ui")
    command = sys.argv[1]
    # if has argument guideUpdateFinished
    if command == "guideUpdateFinished":
        functions.guideUpdateFinished()
        return

    update.checkForUpdates()
    functions.clearConsole()
    showLogo()
    print("\n")


    if command == "getinfo":
        url = sys.argv[3]
        print(runGetInfo(url))
    elif command == "run":
        url = sys.argv[2]
        runMain(url)
    elif command == "ui":
        gui.startUi()
  
    elif command == "search":
        runSearch()
        return
    elif command == "serve":
        functions.serveContent()
    elif command == "clean":
        functions.clean()
    elif command == "setup":
        url = sys.argv[3]
        runSetup(url)
    elif command == "auto":
        runAuto()
    elif command == "getseason":
        url = sys.argv[3]
        season = sys.argv[5]
        info = None
        if len(sys.argv) > 6:
            info = functions.getInfo(url)
        print(getSeasonStreams(url, season, info))
    elif command == "getepisode":
        url = sys.argv[3]
        season = sys.argv[5]
        episode = sys.argv[7]
        info = None
        if len(sys.argv) > 8:
            info = functions.getInfo(url)
        print(getEpisodeStreams(url, season, episode, info))
    elif command == "help":
        print(bcolors.PRIMARY + "Commands:" + bcolors.ENDC)
        print("-----------------")
        print("run -url <url>")
        print("serve")
        print("clean")
        print("search")
        print("setup -url <url>")
        print("getinfo -url <url>")
        print("getseason -url <url> -season <season>")
        print("getepisode -url <url> -season <season> -episode <episode>")
        print("help")

    else:
        print(bcolors.WARNING + "Invalid command" + bcolors.ENDC)
    
    print("\n")
    return

if __name__ == "__main__":
    handleCommands()
    #main()