# Tester avec un projet bidon comme les poc avec Sébastiens pour faire marcher
# la traduction, on l'implentera ensuite dans le main.

from langdetect import detect
from deep_translator import GoogleTranslator
""" 


def detecter_langue(texte):
    langue_detectee = GoogleTranslator(source='auto').detect(texte)
    return langue_detectee

# Exemple d'utilisation de la fonction
texte = "Hello, how are you?"
langue_detectee = detecter_langue(texte)
print("Langue détectée :", langue_detectee) """




# Fonction pour détecter automatiquement la langue d'un texte
def detecter_langue(texte):
    langue_detectee = detect(texte)
    return langue_detectee

# Exemple d'utilisation de la fonction
textTraduit = str
textATraduire = "Guten Morgen"
langue = "en"

def Traduction(textATraduire,langue):
    langue_detectee = detecter_langue(textATraduire)
    textTraduit = GoogleTranslator(source=langue_detectee,target=langue).translate(text=textATraduire)
    return textTraduit 

textTraduit = Traduction(textATraduire,langue)
print(textTraduit)