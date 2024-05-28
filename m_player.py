import os 
from tkinter import * 
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.geometry("485x700+300+10")
root.title("Music Player")
root.config(bg="#000000")
root.resizable(False, False)
mixer.init()

def playmusic():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

def addmusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

lbl = Label(root)
lbl.place(x=0, y=0)

menu = PhotoImage(file="menu.png")
mu = Button(root, image=menu, bg="#0f0f0f", height=50, width=50,borderwidth=5, relief="raised", command=menu)
mu.place(x=390, y=487)

music = Frame(root, bd=2, relief=RIDGE, width=485, height=100)
music.place(x=0, y=580)

play = PhotoImage(file="play.png")
p = Button(root, image=play, bg="#0f0f0f", height=50, width=50,borderwidth=5, relief="raised", command=playmusic)
p.place(x=20, y=487)

stop = PhotoImage(file="stop.png")
s = Button(root, image=stop, bg="#0f0f0f", height=50, width=50,borderwidth=5, relief="raised", command=mixer.music.stop)
s.place(x=200, y=487)

volume = PhotoImage(file=r"D:\10_PYTHON PROJECTS\MUSIC_PLAYER\volume.png")
v = Button(root, image=volume, bg="#0f0f0f", height=50, width=50,borderwidth=5, relief="raised", command=mixer.music.unpause)
v.place(x=296, y=487)

pause = PhotoImage(file="pause.png")
ps = Button(root, image=pause, bg="#0f0f0f", height=50, width=50,borderwidth=5, relief="raised", command=mixer.music.pause)
ps.place(x=110, y=487)

browse = Button(root, text="Browse music", font=("Arial,bold", 15),fg="Black", bg="#838383", width=42, borderwidth=10, relief="raised", command=addmusic)
browse.place(x=0, y=560)

scroll = Scrollbar(music)
playlist = Listbox(music, width=100, font=("Arial,bold", 10), bg="#BEBEBE", selectbackground="#064F57", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=RIGHT, fill=BOTH)

l_frame = Frame(root, bg="#000000", width=485, height=10)
l_frame.place(x=0, y=0)

frmcount = 30
frms = [PhotoImage(file="MIND.gif", format='gif -index %i' % i) for i in range(frmcount)]

def update(ind):
    frame = frms[ind]
    ind += 1
    if ind == frmcount:
        ind = 0
    lbl.config(image=frame)
    root.after(40, update, ind)

update(0) 

root.mainloop()