import time
from time import sleep
import tkinter
from tkinter import messagebox
import pygame as pg


def music_play(music, vol=0.2):
    pg.mixer.init(44100, -16, 2, 2020)
    pg.mixer.music.set_volume(vol)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music)
        # print("Music File {} loaded!".format(music))
    except pg.error:
        #print(" Music File {} not found! ({})".format(music, pg.get_error()))
        return
    pg.mixer.music.play()

#music source from: https://www.bensound.com/royalty-free-music/track/summer
music = "bensound-summer.mp3"

pom_tk = tkinter.Tk()
pom_tk.withdraw()
pom_tk.title("Pomodoro your way through stressful assignments and tasks!!")
pom_tk.configure(background = "red")
messagebox.showinfo("Pomodoro Work Session of 25 mins is on!!","\n Work hard!")
pom_tk.resizable(0,0)

checkmark = 0
total_poms = 0
mini_breaks = 0
big_breaks = 0
sess_choice = "Yes"

while(sess_choice == "Yes" or "yes"):
    messagebox.showinfo("Pomodoro Work Session of 25 mins is on!!","\n Work hard!")
    sleep(25*60)
    messagebox.showinfo("Good job!!","\n Session End!")
    checkmark +=1
    total_poms +=1
    if(checkmark == 4):
        messagebox.showinfo("You've completed 4 pomodoros!!","\n Long Break for 30 mins!")
        big_breaks += 1
        music_play(music, vol)
    # 30 minute long break with Music :D
        sleep(30*60)
    # reset checkmark
        checkmark = 0
    else:
        messagebox.showinfo("Pomodoro Break Session for 5 mins!!","\n Play hard!")
        mini_breaks += 1
        # 5 minute short break with Music :D
        music_play(music, vol)
        sleep(5*60)
    sess_choice = input("Keep going?:(Yes/No)")
    if(sess_choice == "No" or "no"):
        break
messagebox.showinfo(title = "Otsukaresama!",message = "Task Successful!!")
messagebox.showinfo(title = "Pomodoro Log Today", message = "Pomodoro for today included: " + str(total_poms) + "pomos, " + str(mini_breaks) +
                    "mini-breaks, " + str(big_breaks) +" long breaks")

