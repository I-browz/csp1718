'''
Tkinter_tutorial.py demonstrates some of the standard widgets  
and the grid() geometry manager
'''
from Tkinter import *

import PIL                # for most of the PIL routines
from PIL import ImageTk   # this submodule is separated from PIL

import matplotlib.pyplot as plt

import os.path              



root = Tk()






# A canvas widget
drawpad = Canvas(root, background='brown')
drawpad.grid(row=0, column=1)


__dir__ = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(__dir__, 'DoraMiracle.jpg')

img = PIL.Image.open(filename)


'''
im = Image.open('DoraMiracle.jpg')
im.
'''

tkimg=PIL.ImageTk.PhotoImage(img)

def stamp(event):
    drawpad.create_image(event.x,event.y,image=tkimg)
    print reduceSlider.get()
drawpad.bind('<ButtonPress-1>', stamp)







# A button. This widget is demonstrating using an event handler with 
# the command argument
times_pressed = 0
def pressed():
    global times_pressed
    times_pressed = 'To unlock the message click on the canvas of mystery above. You have just recived a treasure map, your goal is to decipher it.                     '
    editor.insert(END, times_pressed)
    editor.see(END)
button = Button(root, text='Explorer Ready?', 
                command=pressed)
button.grid(row=1, column=0)

# An editor widget
editor = Text(width=80, height=10)
editor.grid(row=2, column=1, rowspan=2, sticky=SE)


times_pressed = 1
def pressed():
    global times_pressed
    times_pressed = '              How do you find the back of an egg? Click the one of the next two buttons                                '
    editor.insert(END, times_pressed)
    editor.see(END)
button = Button(root, text='Solve this', 
                command=pressed)
button.grid(row=2, column=0)


times_pressed = 1
def pressed():
    global times_pressed
    times_pressed = 'If you said pick the front then you are wrong           '
    editor.insert(END, times_pressed)
    editor.see(END)
button = Button(root, text='Front', 
                command=pressed)
button.grid(row=3, column=0)




times_pressed = 1
def pressed():
    global times_pressed
    times_pressed = 'Correct! You have solved our story that is completley suffiencet to pass Computer Scinece given....everything '
    editor.insert(END, times_pressed)
    editor.see(END)
button = Button(root, text='Who cares', 
                command=pressed)
button.grid(row=4, column=0)

'''
# Radio buttons: you can only select one
radio = [0]*4 # create a list
data = IntVar()
for i in range(4):
    radio[i] = Radiobutton(root, text=str(i),
                           variable=data, value=i)
    radio[i].grid(row=i,column=2)
data.set(3)
'''
root.mainloop()