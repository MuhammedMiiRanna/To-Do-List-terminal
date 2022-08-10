from func import *
import winsound
from time import sleep
import pygame
from os import system


def play():
    pygame.mixer.music.load("../TO DO LIST/fadedNcs.mp3")
    pygame.mixer.music.play()


pygame.mixer.init()
play()
# from pygame import mixer
# mixer.init()
# mixer.music.load('fadedNcs.mp3')
# def play():
#     timer = 1
#     mixer.music.play()
#     timer = 2
#     if timer == 2:
#         play()
# play()
# winsound.PlaySound("water.wav", winsound.SND_ASYNC)
# playMusic()


while(True):
    sleep(2)
    system('cls')
    print("#"*70)
    print("{:=<}{:^30}{:=>}".format("#"*20, "Good Morning", "#"*20))
    print("#"*70)

    print("{:=<}{:^50}{:=>}".format
          ("<"*10, "What do you want to do Today!!!", ">"*10))
    print("<"*35, ">"*34)
    printTasks()
    #######################################################
    # to get a good number
    while(True):
        try:
            task_choice = int(input(">> ").strip())
        except ValueError as identifier:
            print("  §§ PICK A NUMBER DUDE! XD §§")
        else:
            if task_choice in range(1, countTasks()+1):
                break
            print(" §§ lol what Task Is That *-* §§")
    ######################################################
    if task_choice == countTasks():
        break

    performTask(task_choice)
    print("\n\n")

sleep(1)
print("#"*70)
sleep(1)
print("\a{:=<}{:^30}{:=>}".format("#"*20, "Good Bye :)", "#"*20))
sleep(1)
print("#"*70)
sleep(1)


# TO-DO:
# TO-DO: make a class.
# TO-DO: add function to load and show old task with the date.
# TO-DO: make a function to pause the song / replay / lower or higher the volume.
