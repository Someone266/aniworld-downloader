import os
import json

import main
import functions

description = {
    "mode": "The mode of AniDown\n'archive' will organize the anime with filestructure, pictures and an offline webserver\n'download' will download anime fast and continue watching",
    "prefHost": "The preferred host to download from",
}
options = {
    "mode": ['archive', 'download'],
    "prefHost": ['voe', 'streamtape']
}
# type of the setting (option, text, number)
type = {
    "mode": "option",
    "prefHost": "option"
}

def menu():
    path = f'{os.getcwd()}\\settings.json'
    functions.clearConsole()

    print('Settings:')
    print('Path:', path)
    print('\n')

    with open('settings.json', 'r') as f:
        data = json.load(f)
    
    for key, value in data.items():
        # count is the number of the key in the dictionary
        count = list(data.keys()).index(key) + 1
        print(f'{main.bcolors.PRIMARY}({count}) - {key}: {value}{main.bcolors.ENDC}')
        print(f'{main.bcolors.OK}Description: {main.bcolors.ENDC}{main.bcolors.SECONDARY}{description[key]}{main.bcolors.ENDC}')
        print(f'{main.bcolors.OK}Options: {main.bcolors.ENDC}{main.bcolors.SECONDARY}{options[key]}{main.bcolors.ENDC}')
        print('---')
    print('Choose an option by pressing the number (q to quit):')
    option = input()
    # if input is not a number, return to the menu
    # if input is q or 0, exit the program
    if not option or option == 'q':
        return
    if not option.isdigit():
        return menu()
    changeSetting(int(option), data)
    return menu()

def changeSetting(option, data):
    # get the key from the dictionary
    key = list(data.keys())[option - 1]
    functions.clearConsole()
    print(f'Changing \'{key}\'')
    if type[key] == 'option':
        print(f'{main.bcolors.OK}Options:\n{main.bcolors.ENDC}')
        for i, option in enumerate(options[key]):
            print(f'({i + 1}) - {option}')
        print('Choose an option by pressing the number:')
        option = input()
        if not option.isdigit():
            return changeSetting(option, data)
        if int(option) > len(options[key]):
            return changeSetting(option, data)
        data[key] = options[key][int(option) - 1]
    else:
        if type[key] == 'text':
            print('Enter the new value (Text/String):')
        elif type[key] == 'number':
            print('Enter the new value (Number):')
        value = input()
        data[key] = value
    with open('settings.json', 'w') as f:
        json.dump(data, f)
    return

def getSetting(key):
    with open('settings.json', 'r') as f:
        data = json.load(f)
    # if key is not set, create it with the default value
    if key not in data:
        data[key] = options[key][0]
        with open('settings.json', 'w') as f:
            json.dump(data, f)
    return data[key]

def defaultSettings():
    data = {}
    for key in description:
        data[key] = options[key][0]
    with open('settings.json', 'w') as f:
        json.dump(data, f)
    return data