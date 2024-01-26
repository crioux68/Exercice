# Tester avec un projet bidon comme les poc avec Sébastiens pour faire marcher
# la traduction, on l'implentera ensuite dans le main.

from langdetect import detect
from deep_translator import GoogleTranslator

# Exemple d'utilisation de la fonction
textTraduit = str
textATraduire = "Guten Morgen"
langue = "en"

# Fonction pour détecter automatiquement la langue d'un texte qui est passé en paramètre
def DetecterLangue(texte):
    langue_detectee = detect(texte)
    return langue_detectee

# Fonction qui prend le texte à traduire, la langue de retour  et retourne le texte traduit
def Traduction(textATraduire,langue):
    langue_detectee = DetecterLangue(textATraduire)
    textTraduit = GoogleTranslator(source=langue_detectee,target=langue).translate(text=textATraduire)
    return textTraduit 

textTraduit = Traduction(textATraduire,langue)
print(textTraduit)