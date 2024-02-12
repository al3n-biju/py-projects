from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas = Canvas(root, width=480, height=360)
canvas.pack()


def tts():
    text = entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('output2.mp4')
    os.system('start output2.mp4')


entry = Entry(root)
canvas.create_window(200, 180, window=entry)
b1 = Button(text='start', command=tts)
canvas.create_window(200, 240, window=b1)
root.mainloop()
