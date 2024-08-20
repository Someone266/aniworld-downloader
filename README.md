![Icon](https://github.com/Someone266/aniworld-downloader/raw/main/.github/project/icon.png)

# Aniworld Down

Aniworld Down ist ein Tool, um Videos von AniWorld (ehemalig AniCloud) herunterzuladen und zu organisieren.

> Pull Requests sind willkommen

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

- **Windows:** Lade `AniWorld-Down.exe` herunter
- **Linux und co:** Lade `main.py` herunter und installiere die benötigten Python Pakete (`requirements.txt`)

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
<!-- - Folgen werden im falschen Ordner heruntergeladen -->
<!-- - Programmabstürze (z.B. aufgrund von captchas) -->
- ~~Nur voe als Hoster (streamtape api wird bald hinzugefügt)~~
<!-- - Lokale Seite wird nicht richtig angezeigt -->
- ~~Update-Loop: Bitte den `assets` Ordner in `anime/` entfernen~~

## Disclaimer

This Python downloader tool is provided solely for educational and informational purposes. I am not responsible for how it is used or for the content downloaded using this tool. Users are advised to ensure that they have the legal right to download and use any content obtained through this tool and to comply with all applicable laws and regulations. By using this downloader tool, users agree to take full responsibility for their actions and to use the tool in accordance with all relevant terms and conditions. Additionally, users are encouraged to read and understand all terms of use and agreements before utilizing this tool.

## License

MIT License
