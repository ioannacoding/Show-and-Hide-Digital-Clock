from tkinter import*
from tkinter.ttk import*
from time import strftime

#setting up the tkinter window and title
win=Tk()
win.title('digital clock')

win.iconbitmap('clock.ico')

#Define function to hide the widget    
def hide_widget(kouti):
   kouti.pack_forget()


#This method counttime gives the format of the label and it
#refreshes the label every one thousand mile-seconds
def counttime():
    string=strftime('%H:%M:%S %p')
    Lemoni.config(text=string)
    Lemoni.after(1000,counttime)

#Define a function to show the widget
def show_widget(kouti):
   kouti.pack()
   
#Here the label is placed inside the window position 
Lemoni=Label(win,font=("ds-digital",70),background="black",foreground="green")
Lemoni.pack(anchor="center")

#Create a button Widget
button_hide= Button(win, text= "Hide", command= lambda:hide_widget(Lemoni))
button_hide.pack(pady=20)

button_show= Button(win, text= "Show", command= lambda:show_widget(Lemoni))
button_show.pack()

#This is the first call of countime method
counttime()
