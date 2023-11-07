from tkinter import *

def lox():
    print('лох')
    height = window.winfo_screenheight()
    width= window.winfo_screenwidth()
    if enter[text] == 'Привет! как прога?':
        text.configure(text='Молодец!\n Прогу через диспечер сам закроешь')
    else:
        text.configure(text='Прогу через диспечер сам закроешь')


window = Tk()
window.geometry('1000x700')
window.title('Спасибо, что открыл)')
window.config(bg='red')
window.resizable(width=False, height=False)

text = Label(text='Расшифруй послание:\n -бдпср лбл _уёгйсР', bg='black',fg='white', font=('',10))
text.place(x=110, y=200,)

enter = Entry(bg='black', fg='white', validate="key", width=80)
enter.place(x=110, y=250,)


window.protocol('WM_DELETE_WINDOW', lox)

window.mainloop()