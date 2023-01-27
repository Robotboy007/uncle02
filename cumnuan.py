from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('cumนวน')
GUI.geometry('600x500')

bg = PhotoImage(file='car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='put your number',font=(None,20))
L.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack(pady=20)


def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 39
        messagebox.showinfo('Result','The Number I Gave You Is {}'.format(calc))
        v_quantity.set('1')
        E1.focus()
    except:
        messagebox.showwarning('wrong!','I Said Number!!!')
        v_quantity.set('1')
        E1.focus()

B = ttk.Button(GUI, text='calculate',command=Cal)
B.pack(ipadx=30,ipady=20)


GUI = mainloop()