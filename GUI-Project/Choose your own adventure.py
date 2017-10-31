#Dice Sim/ Choose own adventure
# Nathan.B_Keaton.C

from Tkinter import *          #don't import like this except for Tkinter
root = Tk()                      #create main window

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.grid() #Puts the canvas in the main Tk window

'''
# Make four objects on the canvas
checkbox = canvas.create_rectangle(100, 200, 200, 300, dash=[1,4])
check = canvas.create_line(100, 250, 150, 300, 220, 150, fill='red', width=20)
message = canvas.create_text(380, 250, text='Try this!', font=('Arial', -100))
shadow = canvas.create_oval(100, 450, 500, 550, fill='#888888', outline='#888888')
'''



canvas = Canvas(root, height=600, width=600,bg='cyan') canvas.grid(column=1, row=0, rowspan=4, sticky=W) canvas.imglist=[] #to prevent garbage collection 

character = raw_input("Who do you choose (Explorer, Villan, Fugitive)")

if character == " Explorer":
    print " You have just recived a treasure map, your goal is to decipher it"
    raw_input("Ready")
    Answer = raw_input("Yes or no")
    if Answer == " yes":
        print "Solve these equations"
        Equation1 = raw_input("X+5=10 what does X equal")
        if Equation1 == " 5":
            print "Correct on to the next one"
            '''
            elif break
                Equation2 = raw_input("X^2=64")
                if Equation2 == " 8":
                print "correct last one"
                   elif break
'''
# Enter event loop. This displays the GUI and starts listening for events.
# The program ends when you close the window.


# Demonstrate changing a property of canvas' item.
canvas.itemconfig(circles[2], outline='black') # Change color
a, b, c, d = canvas.coords(circles[2]) # Get coordinates
canvas.coords(circles[2], a-15, b-11, c, d-11) # Change coordinates
 
# Enter event loop. This displays the GUI and starts listening for events.
root.mainloop() 
























