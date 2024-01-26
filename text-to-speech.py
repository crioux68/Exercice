from gtts import gTTS

# Module avec la bonne version de Playsound a installer
# >> pip install playsound==1.2.2
from playsound import playsound

# Modifier cette variable pour dire a voix haute le haute le texte
textToSpeech = "allo"

tts = gTTS(textToSpeech, lang='fr', tld='ca')
tts.save('hello.mp3')
playsound('hello.mp3')

# le text to speech, on l'implentera ensuite dans le main.