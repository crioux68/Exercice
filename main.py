#Ici William va faire l'interface graphique.
#Quand l'interface sera finit on créera une branche pour chaque fonctionalité
# pour les murges au projet principal, si ce n'est pas clair
# je vous expliquerez rendu là.
# On pourrais aussi faire des branches tout de suite et travailler dessus
# mais je ne pense pas que ce soit nécésaire pour l'instant.

import PySimpleGUI as sg

# Module avec la bonne version de Playsound a installer
# >> pip install playsound==1.2.2
from playsound import playsound

from gtts import gTTS, lang
import os
from langdetect import detect
from deep_translator import GoogleTranslator

langues = lang.tts_langs()
keys = lang.tts_langs().keys

def TextToSpeech(input, langue):
    tts = gTTS(input, lang=langue)
    tts.save('hello.mp3')
    playsound('hello.mp3')
    os.remove('hello.mp3')

list = langues
newList = []

for key,values in list.items():
    newList.append((key + ": " + values))
# Pour enlever le mandatrin qui marche pas
newList.pop(-1)
play = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByElEQVRoge3ZMWsUQRjG8Z8RFSKCgoJp0qSJjVpoZ2clkk8g5CtYpU+TD5DSUkvbVCFNYiM2dhZqY6GFQooEISGai8Xu4HgmcnM3c+su+4fj2L2dmedhb+Z95x16enp6hljBxaZF5OAE7/GoaSGTchJ9tnCrWTnjE0zs19+HWMPlJkWNQzAyh2c4rq+/YBnnmpOWRjASuIfX0f0d3GlAVzLDRmBG9Ta+1r8d4wVuTFdaGqcZCVzFOn7Uz+ziKc5PR1oa/zISWMRm9OxbPCisK5lRjASW8Clqs4H5MrLSSTECs1jFQd3ue319KbewVFKNBBbwMmr/EY8z6kpmXCOBh3gX9dNYdjCpEbigWs326r6OVKvdlQn7TSKHkcCcKt4MNJAd5DQSuI83Ud87uJ15jL8oYYTf2cE3f2YH1wuMhXJGAtdU8+WnwtlBaSOBu3gVjZc9O5iWEapJ/wSf6zEHeI6bZzWYmY6u/4v+rzUirZ/snVh+hwPitpYFxNanKJ1IGk9L4xcz6Eom18bqg5ZtrDqx1Y2LDwPVG2lV8aH15aDWF+jOKpkWi8o5GKWIXTwq56BzxwqdOejpxNFbJw5DO3M83dPT02J+AbN50HbYDxzCAAAAAElFTkSuQmCC'

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Application de Traduction et Text to Speech')],
            [sg.Text('')],
            [sg.Text('Écrire le texte à traduire'), sg.Multiline(size = (40, 20), key='-textATraduire-'),sg.Multiline(size = (40, 20),key='-textTraduire-', disabled=True)],
            [sg.Text(' '*50), sg.Button(image_data=play, key='-PLAY-', button_color=sg.theme_background_color(), border_width=5),sg.Text(' '*50), sg.Button('Traduite',image_data=play, key='-PLAY2-',  button_color=sg.theme_background_color(), border_width=5)],
            [sg.Text('Sélectionner la langue   '), sg.Combo(newList, enable_events=True, key='some_key', size=(85, 10))],  # there must be items
            [sg.Text('')],
            [sg.Button('Convertir'), sg.Button('Annuler')] ]

# Create the Window
window = sg.Window('Application de Traduction et Text to Speech ', layout, resizable=True)
window.size = (800, 600)

# Initialisation 
textTraduit = str
langue = ""

# Fonction pour détecter automatiquement la langue d'un texte qui est passé en paramètre
def DetecterLangue(texte):
    langue_detectee = detect(texte)
    return langue_detectee

# Fonction qui prend le texte à traduire, la langue de retour  et retourne le texte traduit
def Traduction(textATraduire,langue):
    langue_detectee = DetecterLangue(textATraduire)
    textTraduit = GoogleTranslator(source=langue_detectee,target=langue).translate(text=textATraduire)
    return textTraduit 



# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Annuler': # if user closes window or clicks cancel
        break
    if event == '-PLAY-':
        if(values['-textATraduire-'] == ""):
            sg.Popup("Aucun texte")
        else:
            TextToSpeech(values['-textATraduire-'], DetecterLangue(values['-textATraduire-']))
    elif event == "-PLAY2-":
        if(values['-textATraduire-'] == ""):
            sg.Popup("Aucun texte")
        else:
            TextToSpeech(values['-textTraduire-'], values['some_key'][0:2])
    elif event == "Convertir":
        textATraduire =values["-textATraduire-"]
        test = values["some_key"]
        test = test.split(":")
        langue = test[0]
        if(langue == ""):
            sg.Popup("selectionner une langue")
        else:
            textTraduit = Traduction(textATraduire,langue)
            window['-textTraduire-'].update(textTraduit)
            #Ici on met les fonctions liés au convertissement et compagnie pour continuer la boucle
            #print('Vous avez entré ', values[0])

# On fini en retirant l'écran
window.close()

    

