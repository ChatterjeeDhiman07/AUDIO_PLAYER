import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *
from mutagen.id3 import ID3

root = Tk()
root.configure(background="#a1dbcd")


index = 0
listofsongs = []
flag = 0

def directory_chooser():
    global listofsongs
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
            print(files)
    for items in listofsongs:
        list_of_songs.insert(0, items)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

    return listofsongs


def next_button():
    global index
    global listofsongs
    if index == len(listofsongs):
        index = 0
    else:
        index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def play_stop():
    global flag
    if flag == 0:
        pygame.mixer.music.pause()
        flag = 1
    elif flag == 1:
        pygame.mixer.music.play()
        flag = 0




# For assigning minimum size and title of window

root.minsize(500, 500)
root.maxsize(500, 500)
root.wm_iconbitmap("adios.ico")
root.title("Adios")

label_1 = Label(root, text="Title", bg="#a1dbcd")
label_1.pack()

frame = Frame(root)
frame.pack()
frame.place(x=160, y=300)

list_of_songs = Listbox(root, width=50)
list_of_songs.pack()
list_of_songs.place(x=100, y=100)

# creation of buttons
rewind = PhotoImage(file="rewind.png")
button_3 = Button(frame, image=rewind, relief=GROOVE)
button_3.pack(side=LEFT)

play = PhotoImage(file="play.png")
button_1 = Button(frame, image=play, relief=GROOVE, command=play_stop)
button_1.pack(side=LEFT)

fast_forward = PhotoImage(file="fastforward.png")
button_2 = Button(frame, image=fast_forward, relief=GROOVE, command=next_button)
button_2.pack(side=LEFT)

folder = PhotoImage(file="folder.png")
button_4 = Button(root, image=folder, relief=GROOVE, command=directory_chooser)
button_4.pack()
button_4.place(x=450, y=450)
root.mainloop()



