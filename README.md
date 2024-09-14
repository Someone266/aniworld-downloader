<p align="center">
  <img src="https://github.com/Someone266/aniworld-downloader/raw/main/.github/project/icon.png" alt="Icon" height="350px" />
</p>

# Aniworld Down

Aniworld Down ist ein Tool, um Videos von AniWorld (ehemalig AniCloud) herunterzuladen und zu organisieren.

[English](en_README.md)

## Funktionen

- 📺 Offline anschauen
- 🎈 Einfache Bedienung
- 📂 Organisierte Oberfläche
- 💨 Schnelles Herunteladen
- 🔎 Suchfunktion
- 🔄 Automatische Updates

## Screenshots

soon

## Voraussetzungen

> Diese Voraussetzungen gelten nicht für den Windows release (exe), da es bereits in der Datei enthalten ist

- Python installiert (Python 3.11 empfohlen - AniWorld Down wird für diese Version entwickelt)
- Pip

## Installation

Gehe zu [Releases](https://github.com/Someone266/aniworld-downloader/releases/latest).

### Windows

Lade `AniWorld-Down.exe` herunter

### Linux und co

Lade `main.py` herunter und installiere die benötigten Python Pakete (`requirements.txt`)

### iOS

Lade [A-Shell mini](https://apps.apple.com/de/app/a-shell-mini/id1543537943) und führe dieses Skript aus:

```bash
echo This is the AniWorld-Down installer for iOS
echo https://github.com/Someone266/aniworld-downloader
echo 
echo
echo Downloading program...
curl -O "https://raw.githubusercontent.com/Someone266/aniworld-downloader/main/dist/main.py"
echo Downloaded!
echo Installing Depencies...
curl -O "https://raw.githack.com/Someone266/aniworld-downloader/main/dist/requirements.txt"
pip install -r requirements.txt
echo Installed!
echo 
echo IMPORTANT:
echo To launch the program type
echo python3 main.py
echo 
echo Anyway, launching program in 8 seconds...
sleep 8
python3 main.py
```


### Android

Installiere [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=de) und öffne die App.
Fürhre diesen Skript aus, um Python und AnWorld-Down zu installieren:
```bash
echo This is the AniWorld-Down installer for Android
echo https://github.com/Someone266/aniworld-downloader
echo 
echo
echo Installing Python3
pkg install python3
pkg install openssl
echo Done!
echo 
echo Downloading program...
curl -O "https://raw.githubusercontent.com/Someone266/aniworld-downloader/main/dist/main.py"
echo Downloaded!
echo Installing Depencies...
curl -O "https://raw.githack.com/Someone266/aniworld-downloader/main/dist/requirements.txt"
pip install -r requirements.txt
echo Installed!
echo 
echo IMPORTANT:
echo To launch the program type
echo python3 main.py
echo 
echo Anyway, launching program in 8 seconds...
sleep 8
python3 main.py
```


## Bedienung

> **Es wird Python 3.11 empfohlen, da das Programm dafür ausgelegt ist**

### Windows

> Es wird empfohlen, das Windows Terminal zu verwenden, da es die Farben und Symbole korrekt anzeigt.
> Microsoft Store: [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?hl=de-de&gl=DE)
> Exe Download: [Windows Terminal](https://github.com/microsoft/terminal/releases/latest)

- Führe einfach `AniWorld-Down.exe` aus

_Möglicherweise wird die Datei vom Antivirus blockiert, aber keinen Grund zur Panik! Die Datei enthält **keinen** Virus oder ähnliches. Komischerweise denkt Avast, dass sie verdächtig ist, weil das Programm in eine Datei gepackt wurde._

## Python

Öffne das Terminal und ändere den Pfad zu dem Ordner, indem das Script gespeichert ist (z.B. `cd C:/users/test/Desktop/Ani-Down/`)

Führe das Programm aus:

### Windows (cmd)

> Es wird empfohlen, das Windows Terminal zu verwenden, da es die Farben und Symbole korrekt anzeigt.
> Microsoft Store: [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?hl=de-de&gl=DE)
> Exe Download: [Windows Terminal](https://github.com/microsoft/terminal/releases/latest)

```cmd
python main.py
```

### Linux und co

```bash
python3 main.py
```

Alle weiteren Anweisungen befinden sich im Programm

_Ich würde mich über einen ⭐️ und einen Follow riesig freuen 😊_

## Bekannte Bugs

Diese Bugs werden höhstwarscheinlich im nächsten update behoben.

- Filme können nicht heruntergeladen werden
- Clean up von Ordnern die von einer älternen AniWorld Down Version erstellt wurden bringt das Programm zum abstürzen
- Crash bei Auswahl von folgen, z.B. 1-6
<!-- - Folgen werden im falschen Ordner heruntergeladen -->
<!-- - Programmabstürze (z.B. aufgrund von captchas) -->
- ~~Nur voe als Hoster (streamtape api wird bald hinzugefügt)~~
<!-- - Lokale Seite wird nicht richtig angezeigt -->
- ~~Update-Loop: Bitte den `assets` Ordner in `anime/` entfernen~~

### Ziele für zukünftige Versionen

- [ ] Filme herunterladen
- [ ] Sprachauswahl, z.B. Dub/Sub
- [ ] Download fortsetzen
- [ ] Weitere Anbieter (hanashi)
- [ ] Stabiler Release
- Weitere Features können unter _Issues_ vorgeschlagen werden

## Changelog

Der gesammte changelog ist [hier](https://api.jm26.net/update/aniworld-down/updateNotes.json) aufgelistet

## Disclaimer

This Python downloader tool is provided solely for educational and informational purposes. I am not responsible for how it is used or for the content downloaded using this tool. Users are advised to ensure that they have the legal right to download and use any content obtained through this tool and to comply with all applicable laws and regulations. By using this downloader tool, users agree to take full responsibility for their actions and to use the tool in accordance with all relevant terms and conditions. Additionally, users are encouraged to read and understand all terms of use and agreements before utilizing this tool.

## License

MIT License
