import tkinter
from tkinter import *

#действия
def end():
    global action, mem, fin, mem2, memus, memus2
    if action == '+':
        fin = mem+mem2
    label.configure(text=fin)

def sum():
    global action, label
    action = '+'
    label.configure(text='0')
    print(0)

'''
def sub():
def mult():
def div():
def root():
def deg():
'''
#цифры
def num1():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '1')
        mem2 += '1'
    else:
        label.configure(text=mem + '1')
        mem += '1'
def num2():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '2')
        mem2 += '2'
    else:
        label.configure(text=mem + '2')
        mem += '2'
def num3():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '3')
        mem2 += '3'
    else:
        label.configure(text=mem + '3')
        mem += '3'
def num4():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '4')
        mem2 += '4'
    else:
        label.configure(text=mem + '4')
        mem += '4'
def num5():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '5')
        mem2 += '5'
    else:
        label.configure(text=mem + '5')
        mem += '5'
def num6():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '6')
        mem2 += '6'
    else:
        label.configure(text=mem + '6')
        mem += '6'
def num7():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '7')
        mem2 += '7'
    else:
        label.configure(text=mem + '7')
        mem += '7'
def num8():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '8')
        mem2 += '8'
    else:
        label.configure(text=mem + '8')
        mem += '8'
def num9():
    global label, a, mem, mem2
    if action == '+':
        label.configure(text=mem2 + '9')
        mem2 += '9'
    else:
        label.configure(text=mem + '9')
        mem += '9'

#переменные
mem = str()
action = str()
mem2 = str()
memus = int()
memus2 = int()
#ТКинтер
window = Tk()
window.geometry('450x580')
window.title('Калькулятор by BloodyMen')
window.resizable(width=False, height=False)

#поле ввода
label = Label(text='0',width=60, height=4, bg='black', fg='white')
label.place(x=10,y=0)

#кнопки
bt1 = Button(text='1', width=8, height=4, command=num1)
bt2 = Button(text='2', width=8, height=4, command=num2)
bt3 = Button(text='3', width=8, height=4, command=num3)
bt4 = Button(text='4', width=8, height=4, command=num4)
bt5 = Button(text='5', width=8, height=4, command=num5)
bt6 = Button(text='6', width=8, height=4, command=num6)
bt7 = Button(text='7', width=8, height=4, command=num7)
bt8 = Button(text='8', width=8, height=4, command=num8)
bt9 = Button(text='9', width=8, height=4, command=num9)
btsum = Button(text='+', width=8, height=4, command=sum())
btfin = Button(text='=', width=8, height=4, command=end())

#размещение кнопок
bt1.place(x=10, y=100)
bt2.place(x=80, y=100)
bt3.place(x=150, y=100)
bt4.place(x=10, y=170)
bt5.place(x=80, y=170)
bt6.place(x=150, y=170)
bt7.place(x=10, y=240)
bt8.place(x=80, y=240)
bt9.place(x=150, y=240)
btsum.place(y=240, x=230)
btfin.place(x=310, y=240)


window.mainloop()
'''
сделать кнопки для действий
'''

