from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
root = Tk()


def qrgen():
    li_name = name_entry.get()
    li = link_entry.get()
    file_name = li_name + ".png"
    url = pyqrcode.create(li)
    url.png(file_name, scale=3)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas1.create_window(200, 350, window=image_label)


canvas1 = Canvas(root, width=400, height=500)
canvas1.pack()
l1 = Label(root, text='QR Code Generator', fg='blue', bg='black', font=30)
canvas1.create_window(200, 50, window=l1)
name = Label(root, text='Link Name')
link = Label(root, text='Link')
canvas1.create_window(200, 100, window=name)
canvas1.create_window(200, 200, window=link)
name_entry = Entry(root)
link_entry = Entry(root)
canvas1.create_window(200, 120, window=name_entry)
canvas1.create_window(200, 220, window=link_entry)
b1 = Button(text='GENERATE', command=qrgen)
canvas1.create_window(200, 250, window=b1)

root.mainloop()
