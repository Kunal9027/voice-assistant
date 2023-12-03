from test import *
import tkinter as tk

#------GUI------#

window = tk.Tk()     # Create a window object

window.title("My First GUI Program")    # Set the title of the window
window.minsize(width=500, height=300)   # Set the minimum size of the window
window.configure(bg='#856ff8')          # window background 

def button_click():
    print("Button clicked!")
    
def exit_click():
    #speak("good bye sir")
    window.destroy()    

def esc():
    window.bind('<Escape>', lambda e, w=window: w.destroy())

esc()

# Label
my_label = tk.Label(text="Voice Assistant", font=("Arial", 24, "bold") , bg='#856ff8')

# Buttons
button_1 = tk.Button(text="Click Me",font=("Arial",15 ,"bold") , command=kunal )

button_2 = tk.Button(text="Exit",font=("Arial",15 ,"bold") , command=exit_click )

my_label.pack()
button_1.place(x=200, y=100)
button_2.place(x=220, y=200)

window.mainloop()