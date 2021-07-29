import tkinter 
from tkinter import *
import random
from tkinter import messagebox

answers=[
    'assam',
    'bihar',
    'goa',
    'gujarat',
    'jammu',
    'kashmir',
    'jharkhand',
    'karnataka',
    'kerala',
    'maharashtra',
    'manipur',
    'meghalaya',
    'mizoram',
    'nagaland',
    'orissa',
]

words=[
    'ssama',
    'bhari',
    'oga',
    'ratguja',
    'majmu',
    'shimkar',
    'jhandkhar',
    'takanakar',
    'kaaler',
    'mashtraha',
    'anipurm',
    'layaghame',
    'zorammi',
    'ganadanl',
    'ssoria',

]

num = random.randrange(0,len(words),1)

def res():
    global words,answers,num
    num=random.randrange(0,len(words),1)
    lb1.config(text=words[num])
    e1.delete(0,END)

def default():
    global words,answers,num
    lb1.config(text=words[num])

def checkans():
    global words,answers,num
    var=e1.get()
    if var==answers[num]:
        messagebox.showinfo("Success","This is a correct answer")
        res()
    else:
        messagebox.showinfo("Error","This is not correct")
        e1.delete(0,END)

root=tkinter.Tk()
root.geometry('500x500+500+150')
root.title('Jumbbbled')
root.config(bg='black')

lb1=Label(
    root,
    text='your text here',
    font=('Verdana',18),
    bg='#000000',
    fg='#ffffff',
)
lb1.pack(pady=30)


ans1 = StringVar()
e1=Entry(
    root,
    font=("Verdana",16),
    textvariable=ans1,
)
e1.pack(ipadx=6 , ipady=6)

btncheck=Button(
    root,
    text="Check",
    font=("Comic sans ms",16),
    width=16,
    bg="#4C4B4B",
    fg="#6ab04c",
    relief=GROOVE,
    command=checkans,
)
btncheck.pack(pady=30)

btnreset=Button(
    root,
    text="Reset",
    font=("Comic sans ms",16),
    width=16,
    bg="#4C4B4B",
    fg="#EA425C",
    relief=GROOVE,
    command=res,
)
btnreset.pack()

default()

root.mainloop()