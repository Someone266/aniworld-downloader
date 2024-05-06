# Aniworld Scraper
# Author: JMcrafter26
# Description: A scraper for aniworld (german anime site)
# Version: 1.1
# License: MIT License
# DISCLAIMER: This is a scraper for educational purposes only. I am not responsible for any misuse of this code.
# Please respect the laws of your country and the country of the website you are scraping.

import functions
import sys
import time

# use auto-py-to-exe to convert this to an exe
# VERSION
version = "1.1.2"

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
        functions.downloadSeason(season, info)

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
    print("Do you want to search for an anime or enter the url directly? (S/u)")
    choice = input()
    if choice == 'S' or choice == 's':
        functions.clearConsole()
        showLogo()
        print("Enter the name of the anime you want to search for")
        name = input()
        url = functions.searchAnime(name)

    else:
        url = input("Enter the url of the anime: ")
    # validate the url
    print(url)

        
    
    info = functions.getInfo(url)
    functions.setup(info)
    for season in info['episodes']:
        functions.getSeasonDownloads(url, season, info['episodes'][season], info)
        
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
    if downloadAll == 'Y' or downloadAll == 'y' or downloadAll == 'yes' or downloadAll == 'Yes':
        print(bcolors.OK + "Downloading all episodes" + bcolors.ENDC)
        for season in range(1, info['seasons'] + 1):
            functions.downloadSeason(season, info)
    else:
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
            functions.downloadSeason(season, info)
        # if episode contains a range
        elif '-' in str(episode):
            start = int(episode.split('-')[0])
            end = int(episode.split('-')[1])
            if start < 1 or end > info['episodes'][season]:
                print(bcolors.FAIL + "Invalid range" + bcolors.ENDC)
                time.sleep(2)
                runAuto1(url, info)
                return
            functions.downloadRange(season, start, end, info)
        else:
            if episode < 1 or episode > info['episodes'][season]:
                print(bcolors.FAIL + "Invalid episode" + bcolors.ENDC)
                time.sleep(2)
                runAuto1(url, info)
                return
            functions.downloadEpisode(season, episode, info)
    print(bcolors.OK + "Script finished! Press any key to exit" + bcolors.ENDC)
    input()
    return

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

    functions.checkForUpdates()
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
        functions.startUi()
  
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