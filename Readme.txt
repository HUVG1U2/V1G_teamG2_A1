______ _____  ___ _________  ___ _____ 
| ___ \  ___|/ _ \|  _  \  \/  ||  ___|
| |_/ / |__ / /_\ \ | | | .  . || |__  
|    /|  __||  _  | | | | |\/| ||  __| 
| |\ \| |___| | | | |/ /| |  | || |___ 
\_| \_\____/\_| |_/___/ \_|  |_/\____/ 

=====================================                                                          
 _   _  _____   _   __                 _              _                              _   
| \ | |/  ___| | | / /                | |            | |                            | |  
|  \| |\ `--.  | |/ /  __ _  __ _ _ __| |_ __ _ _   _| |_ ___  _ __ ___   __ _  __ _| |_ 
| . ` | `--. \ |    \ / _` |/ _` | '__| __/ _` | | | | __/ _ \| '_ ` _ \ / _` |/ _` | __|
| |\  |/\__/ / | |\  \ (_| | (_| | |  | || (_| | |_| | || (_) | | | | | | (_| | (_| | |_ 
\_| \_/\____/  \_| \_/\__,_|\__,_|_|   \__\__,_|\__,_|\__\___/|_| |_| |_|\__,_|\__,_|\__|

=========================================================================================
                                                                                         
Vetrektijden NS.py release 1.0
===========================
Met deze applicatie kunnen reizigers van de NS actuele reistijden opvragen voor elk station. Ook is het mogelijk de eventuele vetragingen te zien. 



Softwarevereisten
=================
Python 3.5.0 of hoger
PyCharm Educational Edition 1.0.1 of hoger



Download
========
https://www.python.org/downloads/
https://www.jetbrains.com/pycharm-edu/download/



Voordat je de Kaarautomaat gaat openen
======================================
Om de kaartautomaat correct werkend te krijgen moeten de volgende packages geïnstalleerd worden in pycharm. 
- pillow
- xmltodict
- requests

Er zijn 2 manieren om deze packages te installeren:

1
- Open het bestand NSbestand.py 
- Klik linksboven op file
- Klik op settings
- Vouw het tabje Project uit
- Klik op Project Interpreter
- Klik rechts op de groene +
- Typ Pillow
- Klik linksonder op Install Package
- Typ xmltodict
- Klik linksonder op Install Package
- Typ requests
- Klik linksonder op Install Package
- Sluit dit venster af, en klik op OK

2
- Open windows verkenner
- C:\Python34\Scripts
- Shift + rechtermuisknop
- Opdrachtvenster hier openen
- Voer de volgende commando's uit:
  pip install pillow
  pip install xmltodict
  pip install requests



De kaartautomaat gebruiken
==========================
- Open het bestand NS.py
- Klik op de groene afspeelknop bij regel 1 en de applicatie start
- Met de help functie in de python console, kunnen de docstrings van de functies aangeroepen worden.