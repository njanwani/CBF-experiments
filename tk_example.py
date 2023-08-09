#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("650x250")

#Create an frame
frame1= Frame(win, bg= "red")
frame2= Frame(win, bg="black")

#Create an label inside the frame
Label(frame2, text= "Line:1", font=('Lucida font',20)).pack(pady=20)
Label(frame1, text= "Line:2", font=('Lucida font',20)).pack(pady=20)

frame1.pack()
frame2.pack()

win.mainloop()