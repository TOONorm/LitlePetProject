from tkinter import *
import time
import random

def clic():
    global count, b, bt, count2, bt2, coc1, coc2, kluck1
    count += 1
    coc2 += 1
    txt.configure(text=count)
    txt3.configure(text='')
    if coc1 != 0:
        for i in range(coc1):
            coc1 -= 1
    if count == kluck1:
        b += 1
        bt.configure(bg=colors[b])
        kluck1 += 20
        txt3.configure(text='Молодец')
        time.sleep(1)
    if coc2 >= 10:
        bt2.configure(text='Ну пожалуйста')
    if coc2 < 10:
        bt2.configure(text='Kliker')
    if count == 300:
        txt_win.configure(text="!победа!")
    print(coc1)
    print(coc2)

def clic2():
    global count2, b, bt2, count, bt, coc1, coc2, kluck2
    count2 += 1
    coc1 += 1
    txt2.configure(text=count2)
    txt3.configure(text='')
    if coc2 != 0:
        for i in range(coc2):
            coc2 -= 1
    if count2 == kluck2:
        b += 1
        bt2.configure(bg=colors[b])
        kluck2 += 20
        txt3.configure(text='Молодец')
        time.sleep(1)
    if coc1 >= 10:
        bt.configure(text='Ну пожалуйста')
    if coc1 < 10:
        bt.configure(text='Кликер')
    if count2 == 300:
        txt_win.configure(text="!победа!")
    print(coc1)
    print(coc2)

coc1 = 0
coc2 = 0
count2 = 0
count = 0
b = 0
kluck1 = 20
kluck2 = 20

window = Tk()
window.title("Кликер")
window.geometry('250x250')

txt = Label(text=count)
txt.place(x=166,)

txt3 = Label(window, text='', fg='yellow', bg='purple',)
txt3.place(x=95,y=35, width=70, height=20,)

txt_win = Label(window, text='', fg='yellow', bg='purple')
txt_win.place(x=95,y=75, width=70, height=20)

txt2 = Label(text=count2)
txt2.place(x=83,)

colors = random.choices(['white', 'red', 'blue', 'green', 'yellow'], k= 35)
print(colors)

bt = Button(window, text='Кликер', bg=colors[b], command=clic)
bt.place(width=100, height=50, x=150, y=100)

bt2 = Button(window, text='Kliker', bg=colors[b], command=clic2)
bt2.place(width=100, height=50, x=0, y=100)

window.mainloop()
#фууух! Я целый вечер на это убил. Хотел бы сделать это более играбельным в плане
#смены цветов, а так я полностью доволен, т.к. у меня теперь всё работает как надо
# и без багов. Надеюсь вам понравиться)