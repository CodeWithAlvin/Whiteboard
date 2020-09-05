#=======imports=======#

from tkinter import *
from tkinter.colorchooser import askcolor


root=Tk()

## variable defining####
colour="blue"

#========Theme Bacground========#
def changeBg():
	   (triple, hexstr) = askcolor()
	   if hexstr:
	   	canvas.config(background=hexstr)

def Light():
    root.title("Alvin's Whiteboard")
    canvas.config(background="white")
        
def Dark():
	  root.title("Alvin's blackboard")
	  canvas.config(background="black")

#========fg colour===========#
def changeFg():
	  global colour
	  (triple, hexstr) = askcolor()
	  if hexstr:
	   	colour=hexstr

def blue():
	global colour
	colour="blue"
def white():
	global colour
	colour="white"
def red():
	global colour
	colour="red"
def black():
	global colour
	colour="black"
			  	       	     	
#=======line creating=========#
def paint(event, selected_colour):
    '''Draws a line following the user mouse cursor'''        
    x1,y1=event.x,event.y
    x2, y2 = event.x-1, event.y
    canvas.create_line(x1,y1,x2,y2, fill=selected_colour, width=s1.get(),capstyle=ROUND,smooth=True)
    

# basic size and name of GUI
can_width=1040
can_height=2160
root.geometry(f"{can_width}x{can_height}")
root.minsize(width=500,height=500)
root.title("Alvin's board")

#======width  scale=====#
s1=Scale(root,from_=8,to=25,orient=HORIZONTAL)
s1.pack(anchor="n",ipadx=840,side="top")


#========creating Canvas===========#
canvas = Canvas(root,width=can_width,height=can_height, background='black')
canvas.pack(fill="both")
canvas.bind("<Motion>", lambda event: paint(event,selected_colour=colour))

#=========creating main menu=========#
mainMenu=Menu(root)


#========creating sub menus==========#
m1=Menu(mainMenu)
m2=Menu(mainMenu)
m3=Menu(mainMenu)

mainMenu.add_cascade(label="Colour",menu=m1)
mainMenu.add_cascade(label="Theme",menu=m2)
mainMenu.add_cascade(label="Erase",menu=m3)

#====adding command in menu m1=====#
m1.add_command(label="        ",background="white",command=white)
m1.add_command(label="        ",background="blue",command=blue)
m1.add_command(label="        ",background="red",command=red)
m1.add_command(label="        ",background="black",command=black)
m1.add_command(label="Other",command=changeFg)

#====adding command in menu m2=====#
m2.add_command(label="       ",background="white",command=lambda : canvas.config(background="white"))
m2.add_command(label="       ",background="black",command=lambda : canvas.config(background="black"))
m2.add_command(label="Other",command=changeBg)

#======adding command in menu m3====#
m3.add_command(label="Clear canvas",command=lambda: canvas.delete("all"))

#=========configing Menu===========#
root.config(menu=mainMenu)


#========running mainloop========#
root.mainloop()

