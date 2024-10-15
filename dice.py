from tkinter import *
import random

def fname(name):
    img=PhotoImage(file=name)
    dice.config(image=img)
    dice.image=img

def chosedice():
    randvalue = random.randint(1,6)
    choice = {
        1:'dice 1.png', 
        2:'dice 2.png',
        3:'dice 3.png',
        4:'dice 4.png',
        5:'dice 5.png',
        6:'dice 6.png',
    }
    fname(choice[randvalue])

r = Tk()
r.title("Dice rolling simulator")
frm = Frame(r)
btn = Button(frm, text="click me to roll", font=('Arial',10,'bold'), fg='red', bg='black',
             command=chosedice)
img = PhotoImage(file="dice 1.png")
dice = Label(frm, image=img)

btn.pack(pady=10)
dice.pack()

frm.place(relx=0.5, rely=0.5, anchor=CENTER)

r.mainloop()
