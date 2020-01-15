from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import RPi.GPIO as GPIO
import tkinter.font
import pygame, sys
import pygame.camera
from pygame.locals import *
from PIL import Image, ImageTk
import os

GPIO.setwarnings(False)
#####################################

Sig1 = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Sig1, GPIO.IN)

Sig2 = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Sig2, GPIO.IN)

Sig3 = 21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Sig3, GPIO.IN)

Sig4 = 24
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Sig4, GPIO.IN)

Sig5 = 26
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Sig5, GPIO.IN)

########################################
out1 = 11# pin11
GPIO.setmode(GPIO.BOARD) # We are accessing GPIOs according to their physical location
GPIO.setup(out1, GPIO.OUT) # We have set our LED pin mode to output
GPIO.output(out1, GPIO.HIGH)

out2 = 12# pin11
GPIO.setmode(GPIO.BOARD) # We are accessing GPIOs according to their physical location
GPIO.setup(out2, GPIO.OUT) # We have set our LED pin mode to output
GPIO.output(out2, GPIO.HIGH)

out3 = 13# pin11
GPIO.setmode(GPIO.BOARD) # We are accessing GPIOs according to their physical location
GPIO.setup(out3, GPIO.OUT) # We have set our LED pin mode to output
GPIO.output(out3, GPIO.HIGH)

out4 = 15# pin11
GPIO.setmode(GPIO.BOARD) # We are accessing GPIOs according to their physical location
GPIO.setup(out4, GPIO.OUT) # We have set our LED pin mode to output
GPIO.output(out4, GPIO.HIGH)

out5 = 16# pin11
GPIO.setmode(GPIO.BOARD) # We are accessing GPIOs according to their physical location
GPIO.setup(out5, GPIO.OUT) # We have set our LED pin mode to output
GPIO.output(out5, GPIO.HIGH)
timeout = time.time() + 60*5
while True:
    gui = Tk()
    gui.title("System Vitals")
    gui.config(background = "gray84")
    gui.minsize(1370,750)

    Font1 = tkinter.font.Font(family = 'Courier 10 Pitch', size = 20, weight = 'bold')
    Font2 = tkinter.font.Font(family = 'Courier 10 Pitch', size = 18, weight = 'bold')
    Font3 = tkinter.font.Font(family = 'Courier 10 Pitch', size = 9, weight = 'bold')

    photo = PhotoImage(file="finalimg.png")
    label = Label(gui, image=photo)
    label.pack()
    label.place(x=1150,y=0)
    #####################################################
    def func1_on():
        GPIO.output(out1, GPIO.LOW) # led on
        Text1 = Label(gui,text=' ON ', font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text1.grid(row=8,column=1)
        
    def func1_off():
        GPIO.output(out1, GPIO.HIGH) # led off
        Text2 = Label(gui,text='OFF', font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text2.grid(row=8,column=1)
        
    def func2_on():
        GPIO.output(out2, GPIO.LOW) # led on
        Text1 = Label(gui,text=' ON ', font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text1.grid(row=12,column=1)
        
    def func2_off():
        GPIO.output(out2, GPIO.HIGH) # led off
        Text2 = Label(gui,text='OFF', font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text2.grid(row=12,column=1)
        
    def func3_on():
        GPIO.output(out3, GPIO.LOW) # led on
        Text1 = Label(gui,text=' ON ', font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text1.grid(row=16,column=1)
        
    def func3_off():
        GPIO.output(out3, GPIO.HIGH) # led off
        Text2 = Label(gui,text='OFF', font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text2.grid(row=16,column=1)

    def function():
        pygame.init()
        pygame.camera.init()
        screen = pygame.display.set_mode((320,240))
        cam = pygame.camera.Camera("/dev/video4",(320,240))
        cam.start()
        timeout = time.time() + 10
        while True:
            image = cam.get_image()
            screen.blit(image,(0,0))
            pygame.display.set_caption(str("OBJECT DETECTION CAM"))
            pygame.display.update()
            if time.time() > timeout:
                break
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT or (event.type == K_ESCAPE):
                    #sys.exit()
        
    #def func4_on():
        #GPIO.output(out4, GPIO.LOW) # led on
        #Text1 = Label(gui,text=' ON ', font = Font2, bg = 'gray84', fg='green3', padx = 0)
        #Text1.grid(row=20,column=1)
        
    def func4_off():
        GPIO.output(out4, GPIO.HIGH) # led off
        Text2 = Label(gui,text='OFF', font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text2.grid(row=20,column=1)
        
    def func5_on():
        GPIO.output(out5, GPIO.LOW) # led on
        Text1 = Label(gui,text=' ON ', font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text1.grid(row=24,column=1)
        
    def func5_off():
        GPIO.output(out5, GPIO.HIGH) # led off
        Text2 = Label(gui,text='OFF', font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text2.grid(row=24,column=1)

    def close_window():
        gui.destroy()
    ######################################################    
    label_1 = Label(gui,text='KLE TECHNOLOGICAL UNIVERSITY\nAutonomous Electric Vehicle',relief = "groove", font = Font1, fg='gray25', bg = 'gray84',anchor=N)
    label_1.grid(row=0,column=9)

    #######################################################

    label_2 = Label(gui,text='Ignition Status:', font = Font2, fg='gray40', bg = 'gray84', padx = 10, pady = 10)
    label_2.grid(row=6,column=0)

    label_3 = Label(gui,text='Primary Motors:', font = Font2, fg='gray40', bg = 'gray84', padx = 10, pady = 10)
    label_3.grid(row=10,column=0)

    label_4 = Label(gui,text='Radar:', font = Font2, fg='gray40', bg = 'gray84', padx = 10, pady = 10)
    label_4.grid(row=14,column=0)

    label_5 = Label(gui,text='Cameras:', font = Font2, fg='gray40', bg = 'gray84', padx = 10, pady = 10)
    label_5.grid(row=18,column=0)

    label_6 = Label(gui,text='Lidar:', font = Font2, fg='gray40', bg = 'gray84', padx = 10, pady = 10)
    label_6.grid(row=22,column=0)

    ######################################################
  
   
    if GPIO.input(Sig1) == True:
        Text3 = Label(gui,text=' Active ',relief = "raised", font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text3.grid(row=6,column=1)
    else:
        Text4 = Label(gui,text=' Inactive ',relief = "raised", font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text4.grid(row=6,column=1)
        ####  
    if GPIO.input(Sig2) == True:
        Text5 = Label(gui,text=' Active ',relief = "raised", font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text5.grid(row=10,column=1)
    else:
        Text6 = Label(gui,text=' Inactive ',relief = "raised", font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text6.grid(row=10,column=1)
    ####   
    if GPIO.input(Sig3) == True:
        Text7 = Label(gui,text=' Active ',relief = "raised", font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text7.grid(row=14,column=1)
    else:
        Text8 = Label(gui,text=' Inactive ',relief = "raised", font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text8.grid(row=14,column=1)
    ####   
    if GPIO.input(Sig4) == True:
        Text9 = Label(gui,text=' Active ',relief = "raised", font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text9.grid(row=18,column=1)
    else:
        Text10 = Label(gui,text=' Inactive ',relief = "raised", font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text10.grid(row=18,column=1)
    ####
    if GPIO.input(Sig5) == True:
        Text9 = Label(gui,text=' Active ',relief = "raised", font = Font2, bg = 'gray84', fg='green3', padx = 0)
        Text9.grid(row=22,column=1)
    else:
        Text10 = Label(gui,text=' Inactive ',relief = "raised", font = Font2, bg = 'gray84', fg='red', padx = 0)
        Text10.grid(row=22,column=1)
    ######################################################
    Button1 = Button(gui, text='Switch On', font = Font3, command = func1_on, bg='gray74', height = 1, width = 7)
    Button1.grid(row=8,column=0)
    Button2 = Button(gui, text='Switch Off', font = Font3, command = func1_off, bg='gray74', height = 1, width = 7)
    Button2.grid(row=9,column=0)

    Button3 = Button(gui, text='Switch On', font = Font3, command = func2_on, bg='gray74', height = 1, width = 7)
    Button3.grid(row=12,column=0)
    Button4 = Button(gui, text='Switch Off', font = Font3, command = func2_off, bg='gray74', height = 1, width = 7)
    Button4.grid(row=13,column=0)

    Button5 = Button(gui, text='Switch On', font = Font3, command = func3_on, bg='gray74', height = 1, width = 7)
    Button5.grid(row=16,column=0)
    Button6 = Button(gui, text='Switch Off', font = Font3, command = func3_off, bg='gray74', height = 1, width = 7)
    Button6.grid(row=17,column=0)

    Button7 = Button(gui, text='Switch On', font = Font3, command = function, bg='gray74', height = 1, width = 7)
    Button7.grid(row=20,column=0)
    Button8 = Button(gui, text='Switch Off', font = Font3, command = func4_off, bg='gray74', height = 1, width = 7)
    Button8.grid(row=21,column=0)

    Button9 = Button(gui, text='Switch On', font = Font3, command = func5_on, bg='gray74', height = 1, width = 7)
    Button9.grid(row=24,column=0)
    Button10 = Button(gui, text='Switch Off', font = Font3, command = func5_off, bg='gray74', height = 1, width = 7)
    Button10.grid(row=25,column=0)

    button11 = Button(gui, text='refresh',font = Font3,command = close_window, bg='gray74', height = 1, width = 7)
    button11.grid(row=30,column=1)

    #button12 = Button(gui, text='Quit',font = Font3,command = gui.quit, bg='gray74', height = 1, width = 7)
    #button12.grid(row=30,column=2)

    # if(Sig1 and Sig2 and Sig3 and Sig4 and Sig5) == True:
    #     label_7 = Label(gui,text='System Initated!', font = Font2, fg='green3', bg = 'gray84', padx = 10, pady = 10)
    #     label_7.grid(row=15,column=10)
    # else:
    #     label_8 = Label(gui,text='System Failed To Initate!', font = Font2, fg='red', bg = 'gray84', padx = 10, pady = 10)
    #     label_8.grid(row=15,column=10)
        
    gui.after(6000,close_window)
    ######################################################
    if time.time() > timeout:
        break
    gui.mainloop()
