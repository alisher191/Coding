import gtts

text = 'Hello world'

tts = gtts.gTTS(text, lang='en')
tts.save('converted_text.mp3')
