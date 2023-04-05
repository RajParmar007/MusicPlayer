from tkinter import *
from tkinter import filedialog

import mutagen
import pygame
import tkinter.font
import time
from mutagen.mp3 import MP3
from tkinter import messagebox
import tkinter.ttk


root = Tk()
root.title("Music Player")
root.geometry("780x740")
root["bg"] = "black"


#Initializing mixer
pygame.mixer.init()


#Functions
global state
state = False




#Function for help menu
def help_funct():

    helpwindow = Toplevel(root)
    helpwindow.geometry("300x140")
    helpwindow.title("Help!")

    help1 = Label(helpwindow, text = "Step 1: Add songs from Menu.\n\n")
    help1["font"] = tkinter.font.Font(family = "Bahnschrift Semibold", size = 10)
    help1.place(x = 10, y =20)

    help2 = Label(helpwindow, text="Step 2: Choose songs from the folder.\n\n")
    help2["font"] = tkinter.font.Font(family="Bahnschrift Semibold", size=10)
    help2.place(x = 10, y =40)

    help3 = Label(helpwindow, text="Step 3: Play your favourite song!\n\n")
    help3["font"] = tkinter.font.Font(family="Bahnschrift Semibold", size=10)
    help3.place(x = 10, y =60)

    help4 = Label(helpwindow, text="Step 4: Pause, Play, in whatever order!\n\n")
    help4["font"] = tkinter.font.Font(family="Bahnschrift Semibold", size=10)
    help4.place(x = 10, y =80)

    help5 = Label(helpwindow, text="Step 5: Remove songs OR clear queue!")
    help5["font"] = tkinter.font.Font(family="Bahnschrift Semibold", size=10)
    help5.place(x = 10, y =100)






#Function for opening a new window on clicking the label button
def openwindow():
    messagebox.showinfo("HELLO!", "Welcome to our Music Player!")





#Function for adding song in the playlist
def addsong():

    #Opening files for user to choose the song/songs
    song = filedialog.askopenfilenames(initialdir="C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic",
                                      title="Choose the song you want to add", filetypes=(("mp3 Files", "*.mp3"),))

    #Removing the location of the song and .mp3 from the song name
    for x in song:
        x = x.replace(".mp3", "")
        x = x.replace("C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/", "")

        #Adding the chosen song in the song list
        list_songs.insert(END, x)




#Rap Playlist
def trapsongs():

    #Opening files for user to choose the song/songs
    song = filedialog.askopenfilenames(initialdir="C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/trap",
                                      title="Choose the song you want to add", filetypes=(("mp3 Files", "*.mp3"),))

    #Removing the location of the song and .mp3 from the song name
    for x in song:
        x = x.replace(".mp3", "")
        x = x.replace("C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/trap/", "")

        #Adding the chosen song in the song list
        list_songs.insert(END, x)



#Pop Playlist
def popsongs():

    #Opening files for user to choose the song/songs
    song = filedialog.askopenfilenames(initialdir="C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/pop",
                                      title="Choose the song you want to add", filetypes=(("mp3 Files", "*.mp3"),))

    #Removing the location of the song and .mp3 from the song name
    for x in song:
        x = x.replace(".mp3", "")
        x = x.replace("C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/pop/", "")

        #Adding the chosen song in the song list
        list_songs.insert(END, x)





#Function for removing a song from the playlist
def removesong():
    list_songs.delete(ANCHOR)
    pygame.mixer.music.stop()

    slider.config(value=0)
    time_bar.config(text = "")




def clearall():
    try:
        list_songs.delete(0,END)
        pygame.mixer.music.stop()
        slider.config(value=0)
        time_bar.config(text = "")

    except FileNotFoundError and mutagen.MutagenError:
        messagebox.showinfo("Done Already?", "You have cleared your music queue")



#Function for playing a song
def playsong():
    global stop
    stop = False
    #Getting the song selected by user
    song = list_songs.get(ACTIVE)

    #Adding the location and .mp3 back to the song name
    song = f"C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/{song}.mp3"

    #Loading and playing the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songtime()




#Function for playing the previous song
def previoussong():
    slider.config(value=0)
    time_bar.config(text="")
    #Selecting the previous song
    previous_song = list_songs.curselection()
    previous_song = previous_song[0]-1
    song = list_songs.get(previous_song)

    #Adding the location and .mp3 back to the name of the song
    song = f"C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Moving the selection to the previous song
    list_songs.selection_clear(0, END)
    list_songs.activate(previous_song)
    list_songs.selection_set(previous_song, last=None)



global stop
stop = False
def stopsong():

    time_bar.config(text="")
    slider.config(value = 0)
    #Stopping the current song
    pygame.mixer.music.stop()

    #Clearing the selection list
    list_songs.selection_clear(ACTIVE)
    time_bar.config(text = "")
    global stop
    stop = True





#Function for playing the next song
def nextsong():

    slider.config(value=0)
    time_bar.config(text="")
    # Selecting the next song
    next_song = list_songs.curselection()
    next_song = next_song[0] + 1
    song = list_songs.get(next_song)

    # Adding the location and .mp3 back to the name of the song
    song = f"C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Moving the selection to the next song
    list_songs.selection_clear(0, END)
    list_songs.activate(next_song)
    list_songs.selection_set(next_song, last=None)





#Function for pausing song
def pausesong(what_is_state):

    global state
    state = what_is_state

    if state:
        # If song is paused it will unpause it
        pygame.mixer.music.unpause()
        state = False

    else:
        # If song is unpaused it will pause it
        pygame.mixer.music.pause()
        state = True






#Function for displaying song time
def songtime():
    if stop:
        return
    playing_time = pygame.mixer.music.get_pos() / 1000
    displaying_time = time.strftime('%M:%S', time.gmtime(playing_time))

    song = list_songs.get(ACTIVE)

    song = f"C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/{song}.mp3"
    song_title = MP3(song)

    global length
    length = song_title.info.length
    song_length = time.strftime('%M:%S', time.gmtime(length))
    playing_time += 1

    if int(slider.get())== int(length):
        time_bar.config(text=f'{song_length}')

    elif state:
        pass

    elif int(slider.get()) == int(playing_time):
        slider_position = int(length)
        slider.config(to=slider_position, value=int(playing_time))

    else:
        slider_position = int(length)
        slider.config(to=slider_position, value=int(slider.get()))
        displaying_time = time.strftime('%M:%S', time.gmtime(int(slider.get())))
        time_bar.config(text=f'{displaying_time}/{song_length}')

        time_bar_time = int(slider.get())+1
        slider.config(value = time_bar_time)



    time_bar.after(1000, songtime)





#Function for slider
def slider_funct(x):
    song = list_songs.get(ACTIVE)
    song = f"C:/Users/chopm/OneDrive/Desktop/Raj/rajmusic/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))


#Music player label
music_player_label = Button(root, text = "Music Player", fg = "#33c1f5", bg = "black", bd = 0,  command = openwindow)
music_player_label["font"]= tkinter.font.Font(family = "Harlow Solid Italic", size = 35)
music_player_label.pack(pady = 10)






#Listbox of songs
list_songs = Listbox(root, bg = "#1e1818", width = 75, height = 18, fg = "white", highlightbackground = "black", selectbackground = "black", bd = 10, selectforeground = "light blue")
list_songs["font"] = tkinter.font.Font(family = "Impact", size = 13)
list_songs.pack(padx = 25, pady = 0)



#Frame
frame = Frame(root, bg = "black")
frame.pack()



#Buttons

#Play button
play_button_image = PhotoImage(file = "mplay.png")
play_button = Button(frame, image = play_button_image, borderwidth = 0, bg = 'black', command = playsong)
play_button.grid(row = 0, column =0, pady =20)




#Previous button
previous_button_image = PhotoImage(file = "mprevious.png")
previous_button = Button(frame, image = previous_button_image, borderwidth = 0,bg = 'black', command = previoussong)
previous_button.grid(row = 0, column =1, pady =20)



#Pause button
pause_button_image = PhotoImage(file = "mpause.png")
pause_button = Button(frame, image = pause_button_image, borderwidth = 0, bg = 'black', command = lambda: pausesong(state))
pause_button.grid(row = 0, column =2, pady =20)




#Next button
next_button_image = PhotoImage(file = "mnext.png")
next_button = Button(frame, image = next_button_image, borderwidth = 0, bg = 'black', command = nextsong)
next_button.grid(row = 0, column =3, pady =20)



#Stop button
stop_button_image = PhotoImage(file = "mstop.png")
stop_button = Button(frame, image = stop_button_image, borderwidth = 0, bg = 'black', command = stopsong)
stop_button.grid(row = 0, column = 4, pady =20)



#Music slider
slider = tkinter.ttk.Scale(root, from_=0, to=100, orient = HORIZONTAL, value = 0, command = slider_funct, length = 360)
slider.pack(pady = 10)



#Label for displaying time of the song
time_bar = Label(root, bg = "#33c1f5")
time_bar["font"] = tkinter.font.Font(family = "Comic Sans MS", size = 12)
time_bar.pack(side = RIGHT)



#Menu for control panel
the_menu = Menu(root)
root.config(menu = the_menu)

menu_song = Menu(the_menu)
the_menu.add_cascade(label = "SONGS", menu = menu_song)
menu_song.add_command(label = "Add songs", command = addsong)
menu_song.add_command(label = "Trap playlist", command = trapsongs)
menu_song.add_command(label = "Pop playlist", command = popsongs)
menu_song.add_command(label = "Remove Song", command = removesong)
menu_song.add_command(label = "Clear all", command = clearall)
menu_song.add_command(label = "Help", command = help_funct)




root.mainloop()