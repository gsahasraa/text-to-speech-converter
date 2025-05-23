import pyttsx3
from tkinter import *
from tkinter import ttk
import threading

window = Tk()
window.title("TEXT TO SPEECH")
window.geometry('390x540')

v = IntVar()
v.set("0")


def cls1():
    textbox.delete(1.0, END)

def cls2():
    textboxp.delete(1.0, END)

def audio_():
    speaker = pyttsx3.init()
    # Voice
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate + range1.get())
    # Rate
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[v.get()].id)
    speaker.say(textboxp.get("1.0",END))
    speaker.runAndWait()

def thread():
    x = threading.Thread(target=audio_)
    x.start()

def text_():
    speaker = pyttsx3.init()
    #Voice
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate + range1.get())
    # Rate
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[v.get()].id)
    speaker.say(textbox.get("1.0",END))
    speaker.runAndWait()

def rbutton(value):
    if value==0:
        label1= Label(tab3, text = "Voice: Male  ")
        label1.grid(row =12)
    else:
        label1 = Label(tab3, text="Voice: Female")
        label1.grid(row=12)

def scale(s):
    label = Label(tab3, text="Rate: " + str(range1.get()))
    label.grid(row=10, column=0)


tab_control = ttk.Notebook(window)

tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)

tab_control.add(tab1, text='Text')
tab_control.add(tab3, text='Settings')

#tab1

label1 = Label(tab1, text = "\u2193Enter text here \u2193", font = ("Arial", 15),background = 'white')
label1.grid(row = 0, column = 0, sticky=E+W)


scroll = Scrollbar(tab1)
scroll.grid(row = 1 , column = 1, sticky= "ns")
textbox= Text(tab1, height = 20, width = 41, wrap = "word",yscrollcommand = scroll.set)
textbox.grid(row= 1 , column = 0, sticky = "nsew")

button1 = Button(tab1, text = "Convert",command = text_)
button1.grid(pady = 20,row = 2)
button1 = Button(tab1, text = "Clear",command = cls1)
button1.grid(pady = 10,padx=10,row = 3, column = 0, sticky = W)
button1 = Button(tab1, text = "Close",command = window.quit)
button1.grid(pady = 10,padx=10,row = 3, column = 0, sticky=E)


#tab2

scroll = Scrollbar(tab2)
scroll.grid(row = 1 , column = 1, sticky= "ns")
textboxp= Text(tab2, height = 15, width = 41, wrap = "word",yscrollcommand = scroll.set)
textboxp.grid(row= 1 , column = 0, sticky = "nsew")



#tab3
label1 = Label(tab3, text = "Select the setting you want to apply", font = ("Arial", 15),background = 'white', foreground = "black")
label1.grid(row = 0, column = 0, sticky=E+W)

label1 = Label(tab3, text = "Rate", font = ("Arial", 15),background = 'white')
label1.grid(pady = 10,row = 1, column = 0, sticky=E+W)
range1= Scale(tab3, from_ = -200 ,to =200, orient = HORIZONTAL, command= scale,length= 300)
range1.grid(row= 2 , column = 0, sticky = W, padx =10)

label1 = Label(tab3, text = "Voice", font = ("Arial", 15),background = 'white')
label1.grid(pady = 10,row = 3, column = 0, sticky=E+W)
rbutton1 = Radiobutton(tab3, text = "Male", variable = v, value = 0, command=lambda: rbutton(v.get()))
rbutton1.grid(row = 4, sticky= W)
rbutton2 = Radiobutton(tab3, text = "Female", variable = v, value = 1,command=lambda: rbutton(v.get()))
rbutton2.grid(row = 5, sticky = W)

rlabel = Label(tab3, text="Rate: 0")
rlabel.grid(row=10, column=0)
vlabel= Label(tab3, text = "Voice: Male")
vlabel.grid(row =12)

#Ver
label1 = Label(tab3, text = "Ver:0.1.0", font = ("Arial", 8),background = 'white')
label1.grid(pady = 190,row = 20, column = 0, sticky=E+W)

tab_control.grid(row = 0, column = 0)

window.mainloop()
