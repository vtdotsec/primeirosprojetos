import gtts
import playsound

# Sintetizar texto em voz
tts = gtts.gTTS('teste teste teste', lang='pt-br')

# Salvar
tts.save('teste.mp3')

# Tocar
playsound.playsound('teste.mp3')
