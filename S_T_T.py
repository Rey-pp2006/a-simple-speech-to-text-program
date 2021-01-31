# -*- coding: utf-8 -*-
"""
Create a simple speech to text program 
@author: Reyhaneh
"""

#import nessecery modules


import speech_recognition as sr
from tkinter import *
from tkinter import messagebox

#create a window

root=Tk()

#set a title for window

root.title("Speech to Text")

#set the size of the main window

root.geometry("485x225")

#set the smallest size of window

root.maxsize(485,225)

#set the biggest size of window

root.minsize(485,225)


#intilaze the vocice recongizer in the variable
r=sr.Recognizer()

#create a function for voice recongizing
def S_T_T():
    global r
    
    # starting the microphone and using it as source variable 
    with sr.Microphone() as source :
        
        #listen to your voice
        audio=r.listen(source)
        
        try:
            #try to recognize your voice using google_recognizer
            text = r.recognize_google(audio)
            #write the speech on the screen
            say_something=Label(root,text=f"You said : {text}", font ="Calibri 15" ,fg="#99042e")
            say_something.grid(row=1,column=0,pady=(30,0))
            
         #if recogonizing wasn't successful , show an error message   
        except:
            Eror=messagebox.showerror("Error" ,"Sorry could not recogonize your voice!")

            
 #create a button        
ready_button=Button(root ,text="Say something:", command=S_T_T,  font ="Calibri 15 bold" , fg="#ffffff", bg="#99042e" )
ready_button.grid(row=0, column=0 , ipadx=175)

#showing the tkinter window
root.mainloop()        