from gtts import gTTS
import os
text = "HI I am Alen."
output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')
os.system('output.mp3')
