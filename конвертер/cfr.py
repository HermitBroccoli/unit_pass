#Libraries
from math import *
from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
import time
from tkinter import ttk

#time
#xx = time.localtime()
xx =time.strftime("%H:%M:%S")

#операции                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#--------------------------------------------------------------------------------------------------------------------------------------------------} 
def win2():
    tiime = Tk()
    tiime.title('Время')
    w = tiime.winfo_screenwidth()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    h = tiime.winfo_screenheight()
    w = w // 2
    h = h // 2 
    w = w - 300
    h = h - 300
    tiime.geometry('500x400+{}+{}'.format(w, h))
    tiime.iconbitmap('g.ico')
    tiime.focus_force()
    #=======================================================================================================
    def star(event):
        try:
            if tr.get() == 0:
                if tr1.get() == 3:
                    Ms.msVs()
                elif tr1.get() == 5:
                    Ms.msVmin()
                elif tr1.get() == 7:
                    Ms.msVh()
                elif tr1.get() == 9:
                    Ms.msVd()
                elif tr1.get() == 11:
                    Ms.msVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 2:
                if tr1.get() == 1:
                    S.sVms()
                elif tr1.get() == 5:
                    S.sVmin()
                elif tr1.get() == 7:
                    S.sVh()
                elif tr1.get() == 9:
                    S.sVd()
                elif tr1.get() == 11:
                    S.sVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 4:
                if tr1.get() == 1:
                    Min.minVms()
                elif tr1.get() == 3:
                    Min.minVs()
                elif tr1.get() == 7:
                    Min.minVh()
                elif tr1.get() == 9:
                    Min.minVd()
                elif tr1.get() == 11:
                    Min.minVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 6:
                if tr1.get() == 1:
                    H.hVms()
                elif tr1.get() == 3:
                    H.hVs()
                elif tr1.get() == 5:
                    H.hVmin()
                elif tr1.get() == 9:
                    H.hVd()
                elif tr1.get() == 11:
                    H.hVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 8:
                if tr1.get() == 1:
                    D.dVms()
                elif tr1.get() == 3:
                    D.dVs()
                elif tr1.get() == 5:
                    D.dVmin()
                elif tr1.get() == 7:
                    D.dVh()
                elif tr1.get() == 11:
                    D.dVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 10:
                if tr1.get() == 1:
                    Wk.wkVms()
                elif tr1.get() == 3:
                    Wk.wkVs()
                elif tr1.get() == 5:
                    Wk.wkVmin()
                elif tr1.get() == 7:
                    Wk.wkVh()
                elif tr1.get() == 9:
                    Wk.wkVd()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не  кажется что это одно и тоже?')
        except:
            EntryA.delete(0, END)
            showinfo("Ошибка", "Введены не верные данные!\n                 Дурак!")
    #=======================================================================================================
    def star1():
        try:
            if tr.get() == 0:
                if tr1.get() == 3:
                    Ms.msVs()
                elif tr1.get() == 5:
                    Ms.msVmin()
                elif tr1.get() == 7:
                    Ms.msVh()
                elif tr1.get() == 9:
                    Ms.msVd()
                elif tr1.get() == 11:
                    Ms.msVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 2:
                if tr1.get() == 1:
                    S.sVms()
                elif tr1.get() == 5:
                    S.sVmin()
                elif tr1.get() == 7:
                    S.sVh()
                elif tr1.get() == 9:
                    S.sVd()
                elif tr1.get() == 11:
                    S.sVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 4:
                if tr1.get() == 1:
                    Min.minVms()
                elif tr1.get() == 3:
                    Min.minVs()
                elif tr1.get() == 7:
                    Min.minVh()
                elif tr1.get() == 9:
                    Min.minVd()
                elif tr1.get() == 11:
                    Min.minVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 6:
                if tr1.get() == 1:
                    H.hVms()
                elif tr1.get() == 3:
                    H.hVs()
                elif tr1.get() == 5:
                    H.hVmin()
                elif tr1.get() == 9:
                    H.hVd()
                elif tr1.get() == 11:
                    H.hVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 8:
                if tr1.get() == 1:
                    D.dVms()
                elif tr1.get() == 3:
                    D.dVs()
                elif tr1.get() == 5:
                    D.dVmin()
                elif tr1.get() == 7:
                    D.dVh()
                elif tr1.get() == 11:
                    D.dVwk()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif tr.get() == 10:
                if tr1.get() == 1:
                    Wk.wkVms()
                elif tr1.get() == 3:
                    Wk.wkVs()
                elif tr1.get() == 5:
                    Wk.wkVmin()
                elif tr1.get() == 7:
                    Wk.wkVh()
                elif tr1.get() == 9:
                    Wk.wkVd()
                else:
                    tr1.set(' ')
                    showinfo('?','А тебе не  кажется что это одно и тоже?')
        except:
            EntryA.delete(0, END)
            showinfo("Ошибка", "Введены не верные данные!\n                 Дурак!")
    #=======================================================================================================
    def sbros():
        tr.set(' ')
        tr1.set(' ')
        EntryA.delete(0, END)
    #=======================================================================================================
    def back():
        tiime.destroy()
        home()
    #=======================================================================================================
    def exit():
        if askyesno("Выход", "Ты точно хочешь выйти?"):
            tiime.destroy()
    #=======================================================================================================
    #операции
    class Ms():
        def zero():
            EntryA.delete(0, END)
            showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
        #============================================
        def msVs():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ms.zero()
            else:
                result = a/1000
                Label23.config(text = 'Результат: ' + str('{:.3f}'.format(result)) + ' ' + 's')
        #============================================
        def msVmin():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ms.zero()
            else:
                result = a/60000
                Label23.config(text = 'Рузультат: ' + str('{:.6f}'.format(result)) + ' ' + 'min')
        #============================================
        def msVh():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ms.zero()
            else:
                result = a/(3.6*10**6)
                Label23.config(text = 'Результат: ' + str('{:.6f}'.format(result)) + ' ' + 'h')
        #============================================
        def msVd():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ms.zero()
            else:
                result = a/(8.64*10**7)
                Label23.config(text = 'Рузультат: ' + str('{:.8f}'.format(result)) + ' ' + 'd')
        #============================================
        def msVwk():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ms.zero()
            else:
                result = a/(6.048*10**6)
                Label23.config(text = 'Результат: ' + str('{:.6f}'.format(result)) + ' ' + 'wk')
        #============================================
    class S():
        def zero():
            EntryA.delete(0, END)
            showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
        #============================================
        def sVms():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                S.zero()
            else:
                result = str(a*1000) + str(' ms')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def sVmin():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                S.zero()
            else:
                result = str('{:.7f}'.format(a/60)) + str(' min')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def sVh():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                S.zero()
            else:
                result = str('{:.9f}'.format(a/3600)) + str(' h')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def sVd():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                S.zero()
            else:
                result = str('{:.6f}'.format(a/86400)) + str(' d')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def sVwk():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                S.zero()
            else:
                result = str('{:.6f}'.format(a/604800)) + str(' wk')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class Min():
        def zero():
            EntryA.delete(0, END)
            showinfo("Нуль", "Да, ноль будет( \nУдивительно?")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        #============================================
        def minVms():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Min.zero()
            else:
                result = str(a/60000) + str(' ms')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def minVs():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Min.zero()
            else:
                result = str(a*60) + str(' s')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def minVh():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Min.zero()
            else:
                result = str('{:.7f}'.format(a/60)) + str(' h')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def minVd():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Min.zero()
            else:
                result = str('{:.9f}'.format(a/1440)) + str(' d')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def minVwk():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Min.zero()
            else:
                result = str('{:.6f}'.format(a/10080)) + str(' wk')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class H():
        def zero():
            EntryA.delete(0, END)
            showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
        #============================================
        def hVms():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                H.zero()
            else:
                result = str('{:.4f}'.format(a*(3.6*10**6))) + str(' ms')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def hVs():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Min.zero()
            else:
                result = str(a*3600) + str(' s')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def hVmin():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                H.zero()
            else:
                result = str(a*60) + str(' min')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def hVd():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                H.zero()
            else:
                result = str('{:.7f}'.format(a/24)) + str(' d')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def hVwk():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                H.zero()
            else:
                result = str('{:.8f}'.format(a/168)) + str(' wk')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class D():
        def zero():
            EntryA.delete(0, END)
            showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
        #============================================
        def dVms():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                D.zero()
            else:
                result = str('{:.5f}'.format(a*(8.64*10**7))) + str(' ms')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def dVs():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                D.zero()
            else:
                result = str('{:.6f}'.format(a/86400)) + str(' s')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def dVmin():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                D.zero()
            else:
                result = str(a*1440) + str(' min')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def dVh():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                D.zero()
            else:
                result = str(a*24) + str(' h')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def dVwk():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                D.zero()
            else:
                result = str('{:.6f}'.format(a/7)) + str(' wk')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class Wk():
        def zero():
            EntryA.delete(0, END)
            showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
        #============================================
        def wkVms():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Wk.zero()
            else:
                result = str('{:.6f}'.format(a*(6.048*10**8))) + str(' wk')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def wkVs():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Wk.zero()
            else:
                result = str(a*604800) + str(' s')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def wkVmin():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Wk.zero()
            else:
                result = str(a*10080) + str(' min')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def wkVh():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Wk.zero()
            else:
                result = str(a*168) + str(' h')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def wkVd():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Wk.zero()
            else:
                result = str(a*7) + str(' d')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    #=======================================================================================================
    #Label
    Label(tiime, text = 'Число', font = 'Aril 16').grid(row = 0, sticky = W, padx = 42, pady = 10)
    Label23 = Label(tiime, text = 'Результат:', font = 'Aril 16').grid(row = 1, sticky = W)
    #=======================================================================================================
    #Entry
    EntryA = Entry(tiime, width = 60)
    #EntryB = Entry(tiime, width = 60)
    #=======================================================================================================
    EntryA.focus_set()
    EntryA.grid(row = 0,sticky = W, padx = 115)
    EntryA.bind('<Return>', star)
    #EntryB.grid(row = 1,sticky = W, padx = 115)
    #=======================================================================================================
    #Button
    star2 = Button(tiime, text = 'Поехали', width = 8, height = 2, command = star1).grid(row = 3, sticky = W, padx = 305)
    sbros2 = Button(tiime, text = 'Сброс', width = 8, height = 2, command = sbros).grid(row = 3, sticky = W, padx = 380)
    exit1 = Button(tiime, text = 'Выход', width = 8, height = 2, command = exit).grid(row = 12, sticky = W, padx = 380, pady = 5)
    back1 = Button(tiime, text = 'Назад', width = 8, height = 2, command = back).grid(row = 12, sticky = W, padx = 305)
    #=======================================================================================================
    tr = IntVar()
    tr.set(' ')
    #=======================================================================================================
    ms = Radiobutton(text = 'миллисекунды', variable = tr, value = 0).grid(row = 4, sticky = W, padx = 30, pady = 5)
    s = Radiobutton(text = 'секунды', variable = tr, value = 2).grid(row = 5, sticky = W, padx = 30, pady = 5)
    min = Radiobutton(text = 'минуты', variable = tr, value = 4).grid(row = 6, sticky = W, padx = 30, pady = 5)
    h1 = Radiobutton(text = 'часы', variable = tr, value = 6).grid(row = 7, sticky = W, padx = 30, pady = 5)
    d = Radiobutton(text = 'дни', variable = tr, value = 8).grid(row = 8, sticky = W, padx = 30, pady = 5)
    wk = Radiobutton(text = 'недели', variable = tr, value = 10).grid(row = 9, sticky = W, padx = 30, pady = 5)
    #=======================================================================================================
    tr1 = IntVar()
    tr1.set(' ')
    #=======================================================================================================
    ms1 = Radiobutton(text = 'миллисекунды', variable = tr1, value = 1).grid(row = 4, sticky = W, padx = 380, pady = 5)
    s1 = Radiobutton(text = 'секунды', variable = tr1, value = 3).grid(row = 5, sticky = W, padx = 380, pady = 5)
    min1 = Radiobutton(text = 'минуты', variable = tr1, value = 5).grid(row = 6, sticky = W, padx = 380, pady = 5)
    h2 = Radiobutton(text = 'часы', variable = tr1, value = 7).grid(row = 7, sticky = W, padx = 380, pady = 5)
    d1 = Radiobutton(text = 'дни', variable = tr1, value = 9).grid(row = 8, sticky = W, padx = 380, pady = 5)
    wk1 = Radiobutton(text = 'недели', variable = tr1, value = 11).grid(row = 9, sticky = W, padx = 380, pady = 5)
    #=======================================================================================================
    tiime.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------}
def gra_vic():
    gravic = Tk()
    gravic.title('График')
    w = gravic.winfo_screenwidth()
    h = gravic.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 300
    h = h - 300
    gravic.geometry('500x300+{}+{}'.format(w, h))
    gravic.iconbitmap('g.ico')
    #сам график
    def t_r():
        tr = Tk()
        tr.title('График')
        w = tr.winfo_screenwidth()
        h = tr.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 300
        h = h - 300
        tr.geometry('500x300+{}+{}'.format(w, h))
        tr.iconbitmap('g.ico')

    #Label
    Label(gravic, text = 'Это временное окно. Не факт что будет работать!', font = 'Aril 22').grid(row = 0, sticky = W, padx = 20)
    #Entry
    EntryA = Entry(gravic, width = 50)

    EntryA.grid(row = 1, sticky = W, padx = 60, pady = 10)
    #Button
    t1 = Button(gravic, text = 'поехали', width = 8, height = 2)
    t1.grid(row = 1, sticky = W, padx = 380)
#--------------------------------------------------------------------------------------------------------------------------------------------------}
def win3():
    dav = Tk()
    dav.title('Давление')
    w = dav.winfo_screenwidth()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    h = dav.winfo_screenheight()
    w = w // 2
    h = h // 2 
    w = w - 300
    h = h - 300
    dav.geometry('500x400+{}+{}'.format(w, h))
    dav.iconbitmap('g.ico')
    dav.focus_force()
    #=======================================================================================================
    def provarca():
        try:
            if DV.get() == 0:
                if DV1.get() == 3:
                    Atm.atmVbar()
                elif DV1.get() == 5:
                    Atm.atmVpa()
                elif DV1.get() == 7:
                    Atm.atmVtorr()
                elif DV1.get() == 9:
                    Atm.atmVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 2:
                if DV1.get() == 1:
                    Bar.barVatm()
                elif DV1.get() == 5:
                    Bar.barVpa()
                elif DV1.get() == 7:
                    Bar.barVtorr()
                elif DV1.get() == 9:
                    Bar.barVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 4:
                if DV1.get() == 1:
                    Pa.paVatm()
                elif DV1.get() == 3:
                    Pa.paVbar()
                elif DV1.get() == 7:
                    Pa.paVtorr()
                elif DV1.get() == 9:
                    Pa.paVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 6:
                if DV1.get() == 1:
                    Torr.torrVatm()
                elif DV1.get() == 3:
                    Torr.torrVbar()
                elif DV1.get() == 5:
                    Torr.torrVpa()
                elif DV1.get() == 9:
                    Torr.torrVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 8:
                if DV1.get() == 1:
                    Inch.inchVatm()
                elif DV1.get() == 3:
                    Inch.inchVbar()
                elif DV1.get() == 5:
                    Inch.inchVpa()
                elif DV1.get() == 7:
                    Inch.inchVtorr()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
        except:
            EntryA.delete(0, END)
            EntryB.delete(0, END)
            showinfo("Ошибка", "Введены не верные данные!\n                 Дурак!")
    #=======================================================================================================
    def provarca1(event):
        try:
            if DV.get() == 0:
                if DV1.get() == 3:
                    Atm.atmVbar()
                elif DV1.get() == 5:
                    Atm.atmVpa()
                elif DV1.get() == 7:
                    Atm.atmVtorr()
                elif DV1.get() == 9:
                    Atm.atmVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 2:
                if DV1.get() == 1:
                    Bar.barVatm()
                elif DV1.get() == 5:
                    Bar.barVpa()
                elif DV1.get() == 7:
                    Bar.barVtorr()
                elif DV1.get() == 9:
                    Bar.barVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 4:
                if DV1.get() == 1:
                    Pa.paVatm()
                elif DV1.get() == 3:
                    Pa.paVbar()
                elif DV1.get() == 7:
                    Pa.paVtorr()
                elif DV1.get() == 9:
                    Pa.paVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 6:
                if DV1.get() == 1:
                    Torr.torrVatm()
                elif DV1.get() == 3:
                    Torr.torrVbar()
                elif DV1.get() == 5:
                    Torr.torrVpa()
                elif DV1.get() == 9:
                    Torr.torrVinch()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif DV.get() == 8:
                if DV1.get() == 1:
                    Inch.inchVatm()
                elif DV1.get() == 3:
                    Inch.inchVbar()
                elif DV1.get() == 5:
                    Inch.inchVpa()
                elif DV1.get() == 7:
                    Inch.inchVtorr()
                else:
                    DV1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
        except:
            EntryA.delete(0, END)
            EntryB.delete(0, END)
            showinfo("Ошибка", "Введены не верные данные!\n                 Дурак!")
    #=======================================================================================================
    #операции
    class Atm():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #============================================
        def atmVbar():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Atm.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*1.013)) + str(' bar')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def atmVpa():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Atm.zero()
            else:
                result = str(a*101325) + str(' pa')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def atmVtorr():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Atm.zero()
            else:
                result = str(a*760) + str(' torr')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def atmVinch():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Atm.zero()
            else:
                result = str('{:.4f}'.format(a*14.696)) + str(' inch')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class Bar():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #============================================
        def barVatm():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Bar.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*1.013)) + str(' atm')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def barVpa():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Bar.zero()
            else:
                result = str(a*100000) + str(' pa')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def barVtorr():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Bar.zero()
            else:
                result = str('~') + str('{:.3f}'.format(a/750)) + str(' torr')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def barVinch():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Bar.zero()
            else:
                result = str('~') + str('{:.4f}'.format(a*14.504)) + str(' inch')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class Pa():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #============================================
        def paVatm():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Pa.zero()
            else:
                result = str('{:.6f}'.format(a/101325)) + str(' atm')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def paVbar():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Pa.zero()
            else:
                result = str('{:.6f}'.format(a/100000)) + str(' bar')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def paVtorr():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Pa.zero()
            else:
                result = str('~') + str('{:.8f}'.format(a/133)) + str(' torr')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def paVinch():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Pa.zero()
            else:
                result = str('~') + str('{:.9f}'.format(a/6895)) + str(' inch')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class Torr():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #============================================
        def torrVatm():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Torr.zero()
            else:
                result = str('{:.8f}'.format(a/760)) + str(' atm')
                EntryB.delete(0, END)
                EntryB.insert(0, END)
        #============================================
        def torrVbar():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Torr.zero()
            else:
                result = str('~') + str('{:.8f}'.format(a/750)) + str(' bar')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def torrVpa():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Torr.zero()
            else:
                result = str('~') + str('{:.3f}'.format(a*133)) + str(' pa')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def torrVinch():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Torr.zero()
            else:
                result = str('{:.7f}'.format(a/51.715)) + str(' inch')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
    class Inch():
        def zero():
            EntryA.get()
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #============================================
        def inchVatm():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Inch.zero()
            else:
                result = str('{:.6f}'.format(a/14.696)) + str(' atm')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def inchVbar():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Inch.zero()
            else:
                result = str('~') + str('{:.7f}'.format(a/14.504)) + str(' bar')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def inchVpa():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Inch.zero()
            else:
                result = str('~') + str('{:.2f}'.format(a*6895)) + str(' pa')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #============================================
        def inchVtorr():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Inch.zero()
            else:
                result = str('{:.4f}'.format(a*51.715)) + str(' torr')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
    #=======================================================================================================
    def sbros():
        DV.set(' ')
        DV1.set(' ')
        EntryA.delete(0, END)
        EntryB.delete(0, END)
    #=======================================================================================================
    def back():
        dav.destroy()
        home()
    #=======================================================================================================
    def exit():
        if askyesno("Выход", "Ты точно хочешь выйти?"):
            dav.destroy()
    #=======================================================================================================
    #Label
    Label(dav, text = 'Число', font = 'Aril 16').grid(row = 0, sticky = W, padx = 42)
    Label(dav, text = 'Результат', font = 'Aril 16').grid(row = 1, sticky = W)
    #=======================================================================================================
    #Entry
    EntryA = Entry(dav, width = 60)
    EntryB = Entry(dav, width = 60)
    #=======================================================================================================
    EntryA.focus_set()
    EntryA.grid(row = 0, sticky = W, padx = 115)
    EntryA.bind('<Return>', provarca1)
    EntryB.grid(row = 1, sticky = W, padx = 115)
    #=======================================================================================================
    #Button
    sbros1 = Button(dav, text = 'Сброс', width = 8, height = 2, command = sbros).grid(row = 2, sticky = W, padx = 380, pady = 5)
    star = Button(dav, text = 'Поехали', width = 8, height = 2, command = provarca).grid(row = 2, sticky = W, padx = 305)
    exit1 = Button(dav, text = 'Выход', width = 8, height = 2, command = exit).grid(row = 12, sticky = W, padx = 380, pady = 5)
    back1 = Button(dav, text = 'Назад', width = 8, height = 2, command = back).grid(row = 12, sticky = W, padx = 305)
    #=======================================================================================================
    #кнопки
    DV = IntVar()
    DV.set(' ')
    atm = Radiobutton(text = 'атмосферв', variable = DV, value = 0).grid(row = 3, sticky = W, padx = 30, pady = 5)
    bar = Radiobutton(text = 'бар', variable = DV, value = 2).grid(row = 4, sticky = W, padx = 30, pady = 5)
    pa = Radiobutton(text = 'паскаль', variable = DV, value = 4).grid(row = 5, sticky = W, padx = 30, pady = 5)
    torr = Radiobutton(text = 'торр', variable = DV, value = 6).grid(row = 6, sticky = W, padx = 30, pady = 5)
    inch = Radiobutton(text = 'фунт-силы на\nквадартный дюйм', variable = DV, value = 8).grid(row = 7, sticky = W, padx = 30, pady = 5)
    #=======================================================================================================
    DV1 = IntVar()
    DV1.set(' ')
    atm1 = Radiobutton(text = 'атмосфера', variable = DV1, value = 1).grid(row = 3, sticky = W, padx = 360, pady =5)
    bar1 = Radiobutton(text = 'бар', variable = DV1, value = 3).grid(row = 4, sticky = W, padx = 360, pady = 5)
    pa1 = Radiobutton(text = 'паскаль', variable = DV1, value = 5).grid(row = 5, sticky = W, padx = 360, pady = 5)
    torr1 = Radiobutton(text = 'торр', variable = DV1, value = 7).grid(row = 6, sticky = W, padx = 360, pady = 5)
    inch1 = Radiobutton(text = 'фунт-силы на\nквадрытный дюйм', variable = DV1, value = 9).grid(row = 7, sticky = W, padx = 360, pady = 5)
#--------------------------------------------------------------------------------------------------------------------------------------------------}
def win4():
    mas = Tk()
    mas.title('масса')
    w = mas.winfo_screenwidth()
    h = mas.winfo_screenheight()
    w = w // 2
    h = h //  2
    w = w - 300
    h = h - 300
    mas.geometry('500x500+{}+{}'.format(w, h))
    mas.iconbitmap('g.ico')
    mas.focus_force()
    #=======================================================================================================
    def exit():
        if askyesno("Выход", "Ты точно хочешь выйти?"):
            mas.destroy()
    #=======================================================================================================
    def back():
        mas.destroy()
        home()
    #=======================================================================================================
    def sbros():
        dv.set(' ')
        dv1.set(' ')
        EntryA.delete(0, END)
        EntryB.delete(0, END)
    #=======================================================================================================
    def proverca():
        try:
            if dv.get() == 0:
                if dv1.get() == 3:
                    T.tVkg()
                elif dv1.get() == 5:
                    T.tVg()
                elif dv1.get() == 7:
                    T.tVmg()
                elif dv1.get() == 9:
                    T.tVqg()
                elif dv1.get() == 11:
                    T.tVus()
                elif dv1.get() == 13:
                    T.tVusa()
                elif dv1.get() == 15:
                    T.tVib()
                elif dv1.get() == 17:
                    T.tVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 2:
                if dv1.get() == 1:
                    Kg.kgVt()
                elif dv1.get() == 5:
                    Kg.kgVg()
                elif dv1.get() == 7:
                    Kg.kgVmg()
                elif dv1.get() == 9:
                    Kg.kgVqg()
                elif dv1.get() == 11:
                    Kg.kgVust()
                elif dv1.get() == 13:
                    Kg.kgVusat()
                elif dv1.get() == 15:
                    Kg.kgVib()
                elif dv1.get() == 17:
                    Kg.kgVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 4:
                if dv1.get() == 1:
                    G.gVt()
                elif dv1.get() == 3:
                    G.gVkg()
                elif dv1.get() == 7:
                    G.gVmg()
                elif dv1.get() == 9:
                    G.gVqg()
                elif dv1.get() == 11:
                    G.gVust()
                elif dv1.get() == 13:
                    G.gVusat()
                elif dv1.get() == 15:
                    G.gVib()
                elif dv1.get() == 17:
                    G.gVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 6:
                if dv1.get() == 1:
                    Mg.mgVt()
                elif dv1.get() == 3:
                    Mg.mgVkg()
                elif dv1.get() == 5:
                    Mg.mgVg()
                elif dv1.get() == 9:
                    Mg.mgVqg()
                elif dv1.get() == 11:
                    Mg.mgVust()
                elif dv1.get() == 13:
                    Mg.mgVusat()
                elif dv1.get() == 15:
                    Mg.mgVib()
                elif dv1.get() == 17:
                    Mg.mgVoz()
                else:
                    dv1.set()
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 8:
                if dv1.get() == 1:
                    Qg.qgVt()
                elif dv1.get() == 3:
                    Qg.qgVkg()
                elif dv1.get() == 5:
                    Qg.qgVg()
                elif dv1.get() == 7:
                    Qg.qgVmg()
                elif dv1.get() == 11:
                    Qg.qgVust()
                elif dv1.get() == 13:
                    Qg.qgVusat()
                elif dv1.get() == 15:
                    Qg.qgVib()
                elif dv1.get() == 17:
                    Qg.qgVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 10:
                if dv1.get() == 1:
                    Ust.ustVt()
                elif dv1.get() == 3:
                    Ust.ustVkg()
                elif dv1.get() == 5:
                    Ust.ustVg()
                elif dv1.get() == 7:
                    Ust.ustVmg()
                elif dv1.get() == 9:
                    Ust.ustVqg()
                elif dv1.get() == 13:
                    Ust.ustVusat()
                elif dv1.get() == 15:
                    Ust.ustVib()
                elif dv1.get() == 17:
                    Ust.ustVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 12:
                if dv1.get() == 1:
                    Usat.usatVt()
                elif dv1.get() == 3:
                    Usat.usatVkg()
                elif dv1.get() == 5:
                    Usat.usatVg()
                elif dv1.get() == 7:
                    Usat.usatVmg()
                elif dv1.get() == 9:
                    Usat.usatVqg()
                elif dv1.get() == 11:
                    Usat.usatVust()
                elif dv1.get() == 15: 
                    Usat.usatVib()
                elif dv1.get() == 17:
                    Usat.usatVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 14:
                if dv1.get() == 1:
                    Ib.ibVt()
                elif dv1.get() == 3:
                    Ib.ibVkg()
                elif dv1.get() == 5:
                    Ib.ibVg()
                elif dv1.get() == 7:
                    Ib.ibVmg()
                elif dv1.get() == 9:
                    Ib.ibVqg()
                elif dv1.get() == 11:
                    Ib.ibVust()
                elif dv1.get() == 13:
                    Ib.ibVusat()
                elif dv1.get() == 17:
                    Ib.ibVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 16:
                if dv1.get() == 1:
                    Oz.ozVt()
                elif dv1.get() == 3:
                    Oz.ozVkg()
                elif dv1.get() == 5:
                    Oz.ozVg()
                elif dv1.get() == 7:
                    Oz.ozVmg()
                elif dv1.get() == 9:
                    Oz.ozVqg()
                elif dv1.get() == 11:
                    Oz.ozVust()
                elif dv1.get() == 13:
                    Oz.ozVusat()
                elif dv1.get() == 15:
                    Oz.ozVib()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
        except:
            EntryA.delete(0, END)
            EntryB.delete(0, END)
            showinfo("Ошибка", "Введены не верные данные!\n                 Дурак!")            
    #=======================================================================================================
    def proverca1(event):
        try:
            if dv.get() == 0:
                if dv1.get() == 3:
                    T.tVkg()
                elif dv1.get() == 5:
                    T.tVg()
                elif dv1.get() == 7:
                    T.tVmg()
                elif dv1.get() == 9:
                    T.tVqg()
                elif dv1.get() == 11:
                    T.tVus()
                elif dv1.get() == 13:
                    T.tVusa()
                elif dv1.get() == 15:
                    T.tVib()
                elif dv1.get() == 17:
                    T.tVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 2:
                if dv1.get() == 1:
                    Kg.kgVt()
                elif dv1.get() == 5:
                    Kg.kgVg()
                elif dv1.get() == 7:
                    Kg.kgVmg()
                elif dv1.get() == 9:
                    Kg.kgVqg()
                elif dv1.get() == 11:
                    Kg.kgVust()
                elif dv1.get() == 13:
                    Kg.kgVusat()
                elif dv1.get() == 15:
                    Kg.kgVib()
                elif dv1.get() == 17:
                    Kg.kgVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 4:
                if dv1.get() == 1:
                    G.gVt()
                elif dv1.get() == 3:
                    G.gVkg()
                elif dv1.get() == 7:
                    G.gVmg()
                elif dv1.get() == 9:
                    G.gVqg()
                elif dv1.get() == 11:
                    G.gVust()
                elif dv1.get() == 13:
                    G.gVusat()
                elif dv1.get() == 15:
                    G.gVib()
                elif dv1.get() == 17:
                    G.gVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 6:
                if dv1.get() == 1:
                    Mg.mgVt()
                elif dv1.get() == 3:
                    Mg.mgVkg()
                elif dv1.get() == 5:
                    Mg.mgVg()
                elif dv1.get() == 9:
                    Mg.mgVqg()
                elif dv1.get() == 11:
                    Mg.mgVust()
                elif dv1.get() == 13:
                    Mg.mgVusat()
                elif dv1.get() == 15:
                    Mg.mgVib()
                elif dv1.get() == 17:
                    Mg.mgVoz()
                else:
                    dv1.set()
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 8:
                if dv1.get() == 1:
                    Qg.qgVt()
                elif dv1.get() == 3:
                    Qg.qgVkg()
                elif dv1.get() == 5:
                    Qg.qgVg()
                elif dv1.get() == 7:
                    Qg.qgVmg()
                elif dv1.get() == 11:
                    Qg.qgVust()
                elif dv1.get() == 13:
                    Qg.qgVusat()
                elif dv1.get() == 15:
                    Qg.qgVib()
                elif dv1.get() == 17:
                    Qg.qgVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 10:
                if dv1.get() == 1:
                    Ust.ustVt()
                elif dv1.get() == 3:
                    Ust.ustVkg()
                elif dv1.get() == 5:
                    Ust.ustVg()
                elif dv1.get() == 7:
                    Ust.ustVmg()
                elif dv1.get() == 9:
                    Ust.ustVqg()
                elif dv1.get() == 13:
                    Ust.ustVusat()
                elif dv1.get() == 15:
                    Ust.ustVib()
                elif dv1.get() == 17:
                    Ust.ustVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 12:
                if dv1.get() == 1:
                    Usat.usatVt()
                elif dv1.get() == 3:
                    Usat.usatVkg()
                elif dv1.get() == 5:
                    Usat.usatVg()
                elif dv1.get() == 7:
                    Usat.usatVmg()
                elif dv1.get() == 9:
                    Usat.usatVqg()
                elif dv1.get() == 11:
                    Usat.usatVust()
                elif dv1.get() == 15: 
                    Usat.usatVib()
                elif dv1.get() == 17:
                    Usat.usatVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 14:
                if dv1.get() == 1:
                    Ib.ibVt()
                elif dv1.get() == 3:
                    Ib.ibVkg()
                elif dv1.get() == 5:
                    Ib.ibVg()
                elif dv1.get() == 7:
                    Ib.ibVmg()
                elif dv1.get() == 9:
                    Ib.ibVqg()
                elif dv1.get() == 11:
                    Ib.ibVust()
                elif dv1.get() == 13:
                    Ib.ibVusat()
                elif dv1.get() == 17:
                    Ib.ibVoz()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
            elif dv.get() == 16:
                if dv1.get() == 1:
                    Oz.ozVt()
                elif dv1.get() == 3:
                    Oz.ozVkg()
                elif dv1.get() == 5:
                    Oz.ozVg()
                elif dv1.get() == 7:
                    Oz.ozVmg()
                elif dv1.get() == 9:
                    Oz.ozVqg()
                elif dv1.get() == 11:
                    Oz.ozVust()
                elif dv1.get() == 13:
                    Oz.ozVusat()
                elif dv1.get() == 15:
                    Oz.ozVib()
                else:
                    dv1.set(' ')
                    showinfo('?','А тебе не кажется что это одно и тоже?')
        except:
            EntryA.delete(0, END)
            EntryB.delete(0, END)
            showinfo("Ошибка", "Введены не верные данные!\n                 Дурак!")
    #=======================================================================================================
    class T():
        def zero():
            EntryA.delete(0,END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def tVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str(a*1000) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def tVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str('{:.6f}'.format(a*(1*10**6))) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def tVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str('{:.6f}'.format(a*(1*10**9))) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def tVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*(1*10**12))) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def tVus():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str('{:.6f}'.format(a/1.016)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def tVusa():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str('{:.5f}'.format(a/1.102)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def tVib():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str('~') + str('{:.2f}'.format(a*2205)) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def tVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                T.zero()
            else:
                result = str('~') + str(a*35274) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class Kg():
        def zero():
            EntryA.delete(0,END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def kgVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str('{:.3f}'.format(a/1000)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def kgVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str(a*1000) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def kgVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str('{:.6f}'.format(a*(1*10**6))) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def kgVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*(1*10**9))) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def kgVust():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str('~') + str('{:.9f}'.format(a*1016)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def kgVusat():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str('~') + str('{:.8f}'.format(a*907)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def kgVib():
            a =  EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str('~') + str('{:.5f}'.format(a*2.205)) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def kgVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Kg.zero()
            else:
                result = str('{:.3f}'.format(a*35.274)) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class G():
        def zero():
            EntryA.delete(0,END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def gVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str('{:.6f}'.format(a/(1*10**6))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def gVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str('{:.3f}'.format(a/1000)) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def gVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str(a*1000) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def gVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str('{:.6f}'.format(a*(1*10**6))) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def gVust():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str('{:.6f}'.format(a*(1.016*10**6))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def gVusat():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a/907185)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def gVib():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str('~') + str('{:.8f}'.format(a/454)) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def gVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                G.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a/28,35)) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class Mg():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def mgVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Mg.zero()
            else:
                result = str('{:.6f}'.format(a*(1*10**9))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def mgVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Mg.zero()
            else:
                result = str('{:.6f}'.format(a*(1*10**-6))) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def mgVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Mg.zero()
            else:
                result = str('{:.3f}'.format(a/1000)) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result) 
        #================================================
        def mgVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Mg.zero()
            else:
                result = str(a*1000) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def mgVust():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Mg.zero()
            else:
                result = str('{:.6f}'.format(a/(1.016*10**6))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def mgVusat():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Mg.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a/(9.072*10**8))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def mgVib():
             a = EntryA.get()
             a = float(a)
             if a == 0:
                Mg.zero()
             else:
                result = str('~') + str('{:.6f}'.format(a/453592)) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def mgVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Mg.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a/28350)) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class Qg():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def qgVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Qg.zero()
            else:
                result = str('{:.4f}'.format(a*(1*10**12))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def qgVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Qg.zero()
            else:
                result = str('{:.4f}'.format(a*(1*10**9))) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def qgVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Qg.zero()
            else:
                result = str('{:.4f}'.format(a/(1*10**6))) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def qgVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Qg.zero()
            else:
                result = str('{:.3f}'.format(a/1000)) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def qgVust():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Qg.zero()
            else:
                result = str('{:.6f}'.format(a*(1.016*10**12))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def qgVusat():
            a = EntryA.get()
            a = float(a) 
            if a == 0:
                Qg.zero()
            else:
                result = str('~') + str('{:.4f}'.format(a*(9.072*10**11))) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def qgVib():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Qg.zero()
            else:
                result = str('{:.6f}'.format(a*(4.536*10**8))) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def qgVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Qg.zero()
            else:
                result = str('{:.6f}'.format(a/(2.835*10**7))) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class Ust():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def ustVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ust.zero()
            else:
                result = str('{:.5f}'.format(a*1.016)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ustVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ust.zero()
            else:
                result = str('~') + str('{:.2f}'.format(a*1016)) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ustVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ust.zero()
            else:
                result = str('~') + str(a*907185) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ustVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ust.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*(1.016*10**8))) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ustVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ust.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*(9.072*10**11))) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ustVusat():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ust.zero()
            else:
                result = str('{:.2f}'.format(a*1.12)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ustVib():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ust.zero()
            else:
                result = str(a*2240) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ustVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Uts.zero()
            else:
                result = str(a*35840) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class Usat():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def usatVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usa.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*1.102)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def usatVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usat.zero()
            else:
                result = str('~') + str('{:.3f}'.format(a*907)) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def usatVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usat.zero()
            else:
                result = str('~') + str(a*907185) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def usatVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usat.zero()
            else:
                result = str('~') + str('{:.4f}'.format(a*(9.072*10**8))) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def usatVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usat.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*(9.072*10**11))) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def usatVust():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usat.zero()
            else:
                result = str('{:.6f}'.format(a*1.12)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def usatVib():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usat.zero()
            else:
                result = str(a*2000) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def usatVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Usat.zero()
            else:
                result = str(a*32000) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class Ib():
        def zero():
            EntryA.get(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def ibVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str('~') + str('{:.9f}'.format(a*2205)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result) 
        #================================================
        def ibVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a/2.205)) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ibVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str('~') + str('{:.3f}'.format(a*454)) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ibVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str('~') + str(a*453592) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ibVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str('{:.5f}'.format(a*(4.536*10**8))) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ibVust():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str('{:.9f}'.format(a*2240)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ibVusat():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str('{:.4f}'.format(a/2000)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ibVoz():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ib.zero()
            else:
                result = str(a*16) + str(' oz')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
    class Oz():
        def zero():
            EntryA.delete(0, END)
            showinfo('Нуль','Да, будет ноль( \nУдивительно?')
        #================================================
        def ozVt():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*35274)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ozVkg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('{:.7f}'.format(a/35.274)) + str(' kg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ozVg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('~') + str('{:.4f}'.format(a*28.35)) + str(' g')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ozVmg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('~') + str('{:.1f}'.format(a*28350)) + str(' mg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ozVqg():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('{:.6f}'.format(a*(2.835*10**7))) + str(' qg')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ozVust():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('{:.7f}'.format(a/35840)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ozVusat():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('{:.6f}'.format(a/32000)) + str(' t')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #================================================
        def ozVib():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Oz.zero()
            else:
                result = str('{:.4f}'.format(a/16)) + str(' ib')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
            #================================================

     #=======================================================================================================
    #Label
    Label(mas, text = 'Число', font = 'Aril 16').grid(row = 0, sticky = W, padx = 42)
    Label(mas, text = 'Результат', font = 'Aril 16').grid(row = 1, sticky = W)
    #=======================================================================================================
    #Entry
    EntryA = Entry(mas, width = 60)
    EntryB = Entry(mas, width = 60)
    #=======================================================================================================
    EntryA.focus_set()
    EntryA.grid(row = 0, sticky = W, padx = 115)
    EntryA.bind('<Return>', proverca1)
    EntryB.grid(row = 1, sticky = W, padx = 115)
    #=======================================================================================================
    #Button
    star = Button(mas, text = 'Поехали', width = 8, height = 2, command = proverca).grid(row = 2, sticky = W, padx = 305)
    sbros1 = Button(mas, text = 'Сброс', width = 8, height = 2, command = sbros).grid(row = 2, sticky = W, padx = 380)
    exit1 = Button(mas, text = 'Выход', width = 8, height = 2, command = exit).grid(row = 12, sticky = W, padx = 380)
    back1 = Button(mas, text = 'Назад', width = 8, height = 2, command = back).grid(row = 12, sticky = W, padx = 305)
    #=======================================================================================================
    dv = IntVar()
    dv.set(' ')
    #=======================================================================================================
    t = Radiobutton(text = 'тонны', variable = dv, value = 0).grid(row = 3, sticky = W, padx = 30, pady = 5)
    kg = Radiobutton(text = 'килограммы', variable = dv, value = 2).grid(row = 4, sticky = W, padx = 30, pady = 5)
    g = Radiobutton(text = 'граммы', variable = dv, value = 4).grid(row = 5, sticky = W, padx = 30, pady = 5)
    mg = Radiobutton(text = 'миллиграмы', variable = dv, value = 6).grid(row = 6, sticky = W, padx = 30, pady = 5)
    qg = Radiobutton(text = 'микрограммы', variable = dv, value = 8).grid(row = 7, sticky = W, padx = 30, pady = 5)
    us = Radiobutton(text = 'английские\nтонны', variable = dv, value = 10).grid(row = 8, sticky = W, padx = 30, pady = 5)
    usa = Radiobutton(text = 'американские\nтонны', variable = dv, value = 12).grid(row = 9, sticky = W, padx = 30, pady = 5)
    lb = Radiobutton(text = 'фунт', variable = dv, value = 14).grid(row = 10, sticky = W, padx = 30, pady = 5)
    oz = Radiobutton(text = 'унции', variable = dv, value = 16).grid(row = 11, sticky = W, padx = 30, pady = 5)
    #=======================================================================================================
    dv1 = IntVar()
    dv1.set(' ')
    #=======================================================================================================
    t1 = Radiobutton(text = 'тонны', variable = dv1, value = 1).grid(row = 3, sticky = W, padx = 380, pady = 5)
    kg1 = Radiobutton(text = 'киллограммы', variable = dv1, value = 3).grid(row = 4, sticky = W, padx = 380, pady = 5)
    g1 = Radiobutton(text = 'граммы', variable = dv1, value = 5).grid(row = 5, sticky = W, padx = 380, pady = 5)
    mg1 = Radiobutton(text = 'миллиграмы', variable = dv1, value = 7).grid(row = 6, sticky = W, padx = 380, pady = 5)
    us1 = Radiobutton(text = 'микрограммы', variable = dv1, value = 9).grid(row = 7, sticky = W, padx = 380, pady = 5)
    usa1 = Radiobutton(text = 'английские\nтонны', variable = dv1, value = 11).grid(row = 8, sticky = W, padx = 380, pady = 5)
    usat = Radiobutton(text = 'американские\nтонны', variable = dv1, value = 13).grid(row = 9, sticky = W, padx = 380, pady = 5)
    ib1 = Radiobutton(text = 'фунт', variable = dv1, value = 15).grid(row = 10, sticky = W, padx = 380, pady = 5)
    oz1 = Radiobutton(text = 'унции', variable = dv1, value = 17).grid(row = 11, sticky = W, padx = 380, pady = 5)
    #=======================================================================================================
    mas.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------}
def win5():
    plosygol = Tk()
    plosygol.title('Плоский угол')
    w = plosygol.winfo_screenwidth()
    h = plosygol.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 300
    h = h - 300
    plosygol.geometry('500x450+{}+{}'.format(w, h))
    plosygol.iconbitmap('g.ico')
    plosygol.focus_force()
    #=======================================================================================================
    def sbros():
        EntryA.delete(0, END)
        EntryB.delete(0, END)
        er.set(' ')
        er1.set(' ')
    #=======================================================================================================
    def exit():
        if askyesno("Выход", "Ты точно хочешь выйти?"):
            plosygol.destroy()
    #=======================================================================================================
    def proverca():
        pass
    #=======================================================================================================
    def back():
        plosygol.destroy()
        home()
    #=======================================================================================================
    class Ac():
        def zero():
            EntryA.delete(0, END)
            showinfo('Ноль','Да, будет ноль( \nУдивительно')
        #===================================================================================================
        def acVa():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ac.zero()
            else:
                result = str('~') + str('{:.4f}'.format(a*40.469)) + str(' a')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #===================================================================================================
        def acVha():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ac.zero()
            else:
                result = str('{:.6f}'.format(a/2.471)) + str(' ha')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #===================================================================================================
        def acVcm2():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ac.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*(4.047*10**7))) + str(' cm^2')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #===================================================================================================
        def acVtf2():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ac.zero()
            else:
                result = str(a*43560) + str(' ft^2')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #===================================================================================================
        def acVin2():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ac.zero()
            else:
                result = str('~') + str('{:.6f}'.format(a*(6.273*10**6))) + str(' in^2')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #===================================================================================================
        def acVm2():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Ac.zero()
            else:
                result = str('~') + str('{:.2f}'.format(a*4047)) + str(' m^2')
                EntryB.delete(0, END)
                EntryB.insert(0, result)
        #===================================================================================================
    class A():
        pass
    #=======================================================================================================
    Label(plosygol, text = 'Число', font = 'Aril 16').grid(row = 0, sticky = W, padx = 42)
    Label(plosygol, text = 'Результат', font = 'Aril 16').grid(row = 1, sticky = W)
    #=======================================================================================================
    EntryA = Entry(plosygol, width = 60)
    EntryB = Entry(plosygol, width = 60)
    #=======================================================================================================
    EntryA.focus_set()
    EntryA.grid(row = 0, sticky = W, padx = 115)
    EntryA.bind('<Return>')
    EntryB.grid(row = 1, sticky = W, padx = 115)
    #=======================================================================================================
    star1 = Button(plosygol, text = 'Поехали', width = 8, height = 2, command = proverca).grid(row = 2, sticky = W, padx = 305)
    sbros1 = Button(plosygol, text = 'Сброс', width = 8, height = 2, command = sbros).grid(row = 2, sticky = W, padx = 380)
    back1 = Button(plosygol, text = 'Назад', width = 8, height = 2, command = back).grid(row = 15, sticky = W, padx = 305)
    exit1 = Button(plosygol, text = 'Выход', width = 8, height = 2, command = exit).grid(row = 15, sticky = W, padx = 380)
    #=======================================================================================================
    er = IntVar()
    er.set(' ')
    #--------------------------------------------------------------------------------
    ac = Radiobutton(text = 'Акры', variable = er, value = 0).grid(row = 3, sticky = W, padx = 10, pady = 5)
    a = Radiobutton(text = 'Ары', variable = er, value = 2).grid(row = 4, sticky = W, padx = 10, pady = 5)
    ha = Radiobutton(text = 'Гектары', variable = er, value = 4).grid(row = 5, sticky = W, padx = 10, pady = 5)
    cm2 = Radiobutton(text = 'Квадратные \nсантиметры', variable = er, value = 6).grid(row = 6, sticky = W, padx = 10, pady = 5)
    ft2 = Radiobutton(text = 'Квадратные \nфунты', variable = er, value = 8).grid(row = 7, sticky = W, padx = 10, pady = 5)
    in2 = Radiobutton(text = 'Квадратные \nдюймы', variable = er, value = 10).grid(row = 8, sticky = W, padx = 10, pady = 5)
    m2 = Radiobutton(text = 'Квадратные \nметры', variable = er, value = 12).grid(row = 9, sticky = W, padx = 10, pady = 5)
    #=======================================================================================================
    er1 = IntVar()
    er1.set(' ')
    #--------------------------------------------------------------------------------
    ac1 = Radiobutton(text = 'Акры', variable = er1, value = 1).grid(row = 3, sticky = W, padx = 380, pady = 5)
    a1 = Radiobutton(text = 'Ары', variable = er1, value = 3).grid(row = 4, sticky = W, padx = 380, pady = 5)
    ha1 = Radiobutton(text = 'Гектары', variable = er1, value = 5).grid(row = 5, sticky = W, padx = 380, pady = 5)
    cm21 = Radiobutton(text = 'Квадратные \nсантиметры', variable = er1, value = 7).grid(row = 6, sticky = W, padx = 380, pady = 5)
    ft21 = Radiobutton(text = 'Квадратные \nфунты', variable = er1, value = 9).grid(row = 7, sticky = W, padx = 380, pady = 5)
    in21 = Radiobutton(text = 'Квадратные \nдюймы', variable = er1, value = 11).grid(row = 8, sticky = W, padx = 380, pady = 5)
    m21 = Radiobutton(text = 'Квадратные \nдюймы', variable = er1, value = 13).grid(row = 9, sticky = W, padx = 380, pady = 5)
#--------------------------------------------------------------------------------------------------------------------------------------------------}
def home():
    window = Tk()
    window.title('home')
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2 
    w = w - 300
    h = h - 300
    window.geometry('500x300+{}+{}'.format(w, h))
    window.iconbitmap('g.ico')
    window.focus_force()
    xx =time.strftime("%H:%M:%S")
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    def window1():
        window.destroy()
        win1()
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    def window2():
        window.destroy()
        win2()
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    def window3():
        window.destroy()
        win3()
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    def window4():
        window.destroy()
        win4()
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    def window5():
        window.destroy()
        win5()
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    def gra__vic():
        window.destroy()
        gra_vic()
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    def quit():
        if askyesno('Выход','Ты точно хочешь выйти?'):
            time.sleep(0.00000001)
            window.destroy()
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    Label1 = Label(window, text='Добро пожаловать', font = 'Aril 22').grid(row = 0, sticky = W, padx = 120, ipady = 5)
    Label2 = Label(window, text = 'Преобразование', font = 'Aril 16').grid(row = 1, sticky = W, padx = 160, ipady = 0.0001)
    Label3 = Label(window, text = 'v6.1.1', font = 'Aril 8').grid(row = 5, sticky = W, padx = 460, pady = 120)
    Label4 = Label(window, text = xx, font = 'Aril 8').grid(row = 5, sticky = W)
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    #кнопки
    but1 = Button(window, text = 'Длина', width = 10, height = 2, command = window1).grid(row = 2, sticky = W, padx = 10, pady = 10)
    but2 = Button(window, text = 'Время', width = 10, height = 2, command = window2).grid(row = 2, sticky = W, padx = 100)
    but3 = Button(window, text = 'Давление', width = 10, height = 2, command = window3).grid(row = 2, sticky = W, padx = 190)
    but4 = Button(window, text = 'Масса', width = 10, height = 2, command = window4).grid(row = 2, sticky = W, padx = 280)
    but5 = Button(window, text = 'Площадь', width = 10, height = 2, command = window5).grid(row = 2, sticky = W, padx = 370)
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    #butgravic = Button(window, text = 'График', width = 10, height = 2, command = gra__vic)
    #butgravic.grid(row = 4, sticky = W, padx = 10, pady = 10)
    #----------------------------------------------------------------------------------------------------------------------------------------------}
    #Button exit
    butexit = Button(window, text = 'Выход', width = 10, height = 2, command = quit).grid(row = 5, sticky = W, padx = 380, pady = 100)
    #-----------------------------------------------------------------------------------------------------------------------------------------------}
    window.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------}
#home
#home()

homein = Tk()
homein.title('Конвертер велечин')

class Cm():
    def zero():
        EntryA.delete(0, END)
        showinfo("Нуль", "Да, ноль будет( \nУдивительно?")            
    #============================================
    def mm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Cm.zero()
        else:
            result = a * 10
            Label22.config(text = 'Результа: ' + str(result) + ' ' + 'mm')
    #============================================
    def cmVm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Cm.zero()
        else:
            result = a/100
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'm')
    #============================================
    def cmVmila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Cm.zero()
        else:
            result = a/160934
            Label22.config(text = 'Результат: ' + str('{:.7f}'.format(result)) + ' ' + 'mi')              
    #============================================
    def cm_v_mormila():
            a = EntryA.get()
            a = float(a)
            if a == 0:
                Cm.zero()
            else:
                result = a/185200
                Label22.config(text = 'Результат: ' + str('{:.5f}'.format(result) + ' ' + 'NM'))
    #============================================
    def cmVkm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Cm.zero()
        else:
            result = a/(1*10**5)
            Label22.config(text = 'Результат: ' + str('{:.5f}'.format(result) + ' ' + 'km'))
    #============================================
    def cmVduim():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Dlina.zero()
        else:
            result = a/2.54
            Label22.config(text = 'Результат: ' + str('{:.5f}'.format(result)) + ' ' + 'in')
    #============================================

class Mm():
    def mmVcm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mm.zero()
        else:
            result = a/10
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'cm')
    #============================================
    def mmVmila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mm.zero()
        else:
            result = a/(1.609*10**6)
            Label22.config(text = 'Результа: ' + str('{:.7f}'.format(result)) + ' ' + 'mi')
    #============================================
    def mmVkm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mm.zero()
        else:
            result = a/(1*10**(-6))
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'km')
    #============================================
    def mmVmormila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mm.zero()
        else:
            result = a/(1.852*10**6)
            Label22.config(text = 'Результат: ' + str('{:.7f}'.format(result))+ ' ' + 'NM')
    #============================================
    def mmVm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mm.zero()
        else:
            result = a/1000
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'm')
    #============================================
    def mmVduim():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mm.zero()
        else:
            result = a/25.4
            Label22.config(text = 'Результат: ' + str('{:.7f}'.format(result)) + ' ' + 'in')
    #============================================
    def zero():
        EntryA.delete(0, END)
        showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
    #============================================

class M():
    def mVcm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            M.zero()
        else:
            result = a*100
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'cm')   
    #============================================
    def mVkm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            M.zero()
        else:
            result = a/1000
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'km')
    #============================================
    def mVmm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            M.zero()
        else:
            result = a*1000
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'mm')
    #============================================
    def mVmila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            M.zero()
        else:
            result = a/1609
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.9f}'.format(result)) + ' ' + 'mi')
    #============================================
    def mVduim():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            M.zero()
        else:
            result = a*39.37
            Label22.config(text = 'Результат: ' + str('{:.4f}'.format(result) + ' ' + 'in'))
    #============================================
    def mVmormila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            M.zero()
        else:
            result = a/1852
            Label22.config(text = 'Результат: ' + str('{:.9f}'.format(result)) + ' ' + 'NM')
    #============================================
    def zero():
        EntryA.delete(0, END)
        showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
    #============================================

class Km():
    def kmVduim():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Km.zero()
        else:
            result = a*39370
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.1f}'.format(result)) + ' ' + 'in')
    #============================================
    def kmVmm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Km.zero()
        else:
            result = a*(1*10**6)
            Label22.config(text = 'Результат: ' + str('{:.9f}'.format(result)) + ' ' + 'mm')
    #============================================
    def kmVm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Km.zero()
        else:
            result = a*1000
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'm')
    #============================================
    def kmVcm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Km.zero()
        else:
            result = a*100000
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'cm')
    #============================================
    def kmVm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Km.zero()
        else:
            result = a*1000
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'm')
    #============================================
    def kmVmila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Km.zero()
        else:
            result = a/1.609
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.6f}'.format(result)) + ' ' + 'mi')
    #============================================
    def km_V_mor_milla():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Km.zero()
        else:
            result = a/1.852
            Label22.config(text = 'Результат ' + str('{:.6f}'.format(result)) + ' ' + 'NM')
    #============================================
    def zero():
        EntryA.delete(0, END)
        showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
    #============================================

class Mila():
    def milaVcm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mila.zero()
        else:
            result = a*160934
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.0f}'.format(result)) + ' ' + 'cm')
    #============================================
    def milaVmm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mila.zero()
        else:
            result = a*(1.609*10**6)
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.6f}'.format(result)) + ' ' + 'mm')
    #============================================
    def milaVm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mila.zero()
        else:
            result =  a*1609
            Label22.config(text = 'Результат: ' + '~' + ' ' + str(('{:.2f}'.format(result)) + ' ' + 'm'))
    #============================================
    def milaVkm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mila.zero()
        else:
            result = a*1.609
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.5f}'.format(result)) + ' ' + 'km')
    #============================================
    def milaVmormila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mila.zero()
        else:
            result = a/1.151
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.6f}'.format(result)) + ' ' + 'NM')
    #============================================
    def milaVduim():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Mila.zero()
        else:
            result = a*63360
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'in')
    #============================================
    def zero():
        EntryA.delete(0, END)
        showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
    #============================================

class Mmm():
    def zero():
        EntryA.delete(0, END)
        showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
    #============================================
    def mmmVcm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            MorMila.zero()
        else:
            result = a*185200
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'cm')
    #============================================
    def mmmVmm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            MorMila.zero()
        else:
            result = a*(1.852*10**6)
            Label22.config(text = 'Результат: ' + str(result) + ' ' + 'mm')
    #============================================
    def mmmVm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            MorMila.zero()
        else:
            result = a*1852
            Label22.config(text = 'Результа: ' + str(result) + ' ' + 'm')
    #============================================
    def mmmVmila():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            MorMila.zero()
        else:
            result = a*1.151
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.5f}'.format(result)) + ' ' + 'mi')
    #============================================
    def mmmVduim():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            MorMila.zero()
        else:
            result = a*72913
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.1f}'.format(result)) + ' ' + 'in')
    #============================================
    def mmmVkm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            MorMila.zero()
        else:
            result = a*1.852
            Label22.config(text = 'Результат: ' + str('{:.3f}'.format(result)) + ' ' + 'km')
    #============================================

class Duim():
    def zero():
        EntryA.delete(0, END)
        showinfo("Нуль", "Да, ноль будет( \nУдивительно?")
    #============================================
    def inVcm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Duim.zero()
        else:
            result = a*2.54
            Label22.config(text = 'Результат: ' + str('{:.4f}'.format(result)) + ' ' + 'cm')
    #============================================
    def inVmm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Duim.zero()
        else:
            result = a*25.4
            Label22.config(text = 'Результат: ' + str('{:.1f}'.format(result)) + ' ' + 'mm')
    #============================================
    def inVm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Duim.zero()
        else:
            result = a/39.37
            Label22.config(text = 'Результат: ' + str('{:.4f}'.format(result)) + ' ' + 'm')
    #============================================
    def inVkm():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Duim.zero()
        else:
            result = a/39370
            Label22.config(text = 'Результат: ' + str('{:.4f}'.format(result)) + ' ' + 'km')
    #============================================
    def inVmi():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Duim.zero()
        else:
            result = a*63360
            Label22.config(text = 'Результат: ' + str('{:.6f}'.format(result)) + ' ' + 'mi')
    #============================================
    def inVNM():
        a = EntryA.get()
        a = float(a)
        if a == 0:
            Duim.zero()
        else:
            result = a*72913
            Label22.config(text = 'Результат: ' + '~' + ' ' + str('{:.6f}'.format(result)) + ' ' + 'NM')
    #============================================

def proverca1():
        try:
            if rt.get() == 0:
                if rt1.get() == 3:
                    Cm.mm()
                elif rt1.get() == 5:
                    Cm.cmVm()
                elif rt1.get() == 7:
                    Cm.cmVkm()
                elif rt1.get() == 9:
                    Cm.cmVmila()
                elif rt1.get() == 11:
                     Cm.cm_v_mormila()
                elif rt1.get() == 13:
                    Cm.cmVduim()
                else:
                    rt1.set(' ')
                    showinfo('?','А тебе не кажется, что это одно и тоже?')
            elif rt.get() == 2:
                if rt1.get() == 1:
                    Mm.mmVcm()
                elif rt1.get() == 5:
                    Mm.mmVm()
                elif rt1.get() == 7:
                    Mm.mmVkm()
                elif rt1.get() == 9:
                    Mm.mmVmila()
                elif rt1.get() == 11:
                    Mm.mmVmormila()
                elif rt1.get() == 13:
                    Mm.mmVduim()
                else:
                    rt1.set(' ')
                    showinfo('?','А тебе не кажется, что это одно и тоже?')
            elif rt.get() == 4:
                if rt1.get() == 1:
                    M.mVcm()
                elif rt1.get() == 3:
                    M.mVmm()
                elif rt1.get() == 7:
                    M.mVkm()
                elif rt1.get() == 9:
                    M.mVmila()
                elif rt1.get() == 11:
                    M.mVmormila()
                elif rt1.get() == 13:
                    M.mVduim()
                else:
                    rt1.set(' ')
                    showinfo('?','А тебе не кажется, что это одно и тоже?')
            elif rt.get() == 6:
                if rt1.get() == 1:
                    Km.kmVcm()
                elif rt1.get() == 3:
                    Km.kmVmm()
                elif rt1.get() == 5:
                    Km.kmVm()
                elif rt1.get() == 9:
                    Km.kmVmila()
                elif rt1.get() == 11:
                    Km.km_V_mor_milla()
                elif rt1.get() == 13:
                    Km.kmVduim()
                else:
                    rt1.set(' ')
                    showinfo('?','А тебе не кажется, что это одно и тоже?')
            elif rt.get() == 8:
                if rt1.get() == 1:
                    Mila.milaVcm()
                elif rt1.get() == 3:
                    Mila.milaVmm()
                elif rt1.get() == 5:
                    Mila.milaVm()
                elif rt1.get() == 7:
                    Mila.milaVkm()
                elif rt1.get() == 11:
                    Mila.milaVmormila()
                elif rt1.get() == 13:
                    Mila.milaVduim()
                else:
                    rt1.set(' ')
                    showinfo('?','А тебе не кажется, что это одно и тоже?')
            elif rt.get() == 10:
                if rt1.get() == 1:
                    Mmm.mmmVcm()
                elif rt1.get() == 3:
                    Mmm.mmmVmm()
                elif rt1.get() == 5:
                    Mmm.mmmVm()
                elif rt1.get() == 7:
                    Mmm.mmmVkm()
                elif rt1.get() == 9:
                    Mmm.mmmVmila()
                elif rt1.get() == 13:
                    Mmm.mmmVduim()
                else:
                    rt1.set(' ')
                    showinfo('?','А тебе не кажется, что это одно и тоже?')
            elif rt.get() == 12:
                if rt1.get() == 1:
                    Duim.inVcm()
                elif rt1.get() == 3:
                    Duim.inVmm()
                elif rt1.get() == 5:
                    Duim.inVm()
                elif rt1.get() == 7:
                    Duim.inVkm()
                elif rt1.get() == 9:
                    Duim.inVmi()
                elif rt1.get() == 11:
                    Duim.inVNM()
                else:
                    rt1.set(' ')
                    showinfo('?','А тебе не кажется, что это одно и тоже?')
        except:
            EntryA.delete(0, END)
            showinfo("Ошибка", "Странные данные")

def exit1():
        if askyesno("Выход", "Ты точно хочешь выйти?"):
            homein.destroy()

def sbros1():
    rt.set(' ')
    rt1.set(' ')
    EntryA.delete(0, END)
    Label22.config(text = 'Результат: ')

tab_control = ttk.Notebook(homein)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text = 'Начальное окно')
tab_control.add(tab2, text = 'Длина')

#dlina
#label tab2
Label1 = Label(tab2, text = 'Число', font = 'Aril 16').grid(row = 0, column = 0, sticky = E)
Label22 = Label(tab2, text = 'Результат:', font = 'Aril 16')
Label22.grid(row = 1, column = 0, columnspan = 4, sticky = W)

#Entry tab2
EntryA = Entry(tab2, width = 40)

EntryA.grid(row = 0, column = 1, columnspan = 3)
#ntryA.bind('<Return>', proverca)

#Button tab2
star = Button(tab2, text = 'Поехали', width = 8, command = lambda: proverca1()).grid(row = 0, column = 4, padx = 5)
sbros1 = Button(tab2, text = 'Сброс', width = 8, command = sbros1).grid(row = 1, column = 4, padx = 5)
exit1 = Button(tab2, text = 'Выход', width = 8, command = lambda: exit1()).grid(row = 13, column = 4)

#radiobutton
rt = IntVar()
rt.set(' ')

cm = Radiobutton(tab2, text = 'сантиметры', variable = rt, value = 0).grid(row = 4, column = 0, sticky = W)
mm = Radiobutton(tab2, text = 'миллиметры', variable = rt, value = 2).grid(row = 5, column = 0, sticky = W)
milli = Radiobutton(tab2, text = 'метры', variable = rt, value = 4).grid(row = 6, column = 0, sticky = W)
km = Radiobutton(tab2, text = 'киллометры', variable = rt, value = 6).grid(row = 7, column = 0, sticky = W)
mila = Radiobutton(tab2, text = 'миля', variable = rt, value = 8).grid(row = 8, column = 0, sticky = W)
mormila = Radiobutton(tab2, text = 'морская \nмиля', variable = rt, value = 10).grid(row = 9, column = 0, sticky = W)
duim = Radiobutton(tab2, text = 'дюйм', variable = rt, value = 12).grid(row = 10, column = 0, sticky = W)

rt1 = IntVar()
rt1.set(' ')

cm1 = Radiobutton(tab2, text = 'сантиметры', variable = rt1, value = 1).grid(row = 4, column = 4, sticky = W)
mm1 = Radiobutton(tab2, text =  'миллиметры', variable = rt1, value = 3).grid(row = 5, column = 4, sticky = W)
milli1 = Radiobutton(tab2, text = 'метры', variable = rt1, value = 5).grid(row = 6, column = 4, sticky = W)
km1 = Radiobutton(tab2, text = 'киллометры', variable = rt1, value = 7).grid(row = 7, column = 4, sticky = W)
mila1 = Radiobutton(tab2, text = 'миля', variable = rt1, value = 9).grid(row = 8, column = 4, sticky = W)
mormila1 = Radiobutton(tab2, text = 'морская \nмиля', variable = rt1, value = 11).grid(row = 9, column = 4, sticky = W)
duim1 = Radiobutton(tab2, text = 'дюйм', variable = rt1, value = 13).grid(row = 10, column = 4, sticky = W)


tab_control.pack(expand = 1, fill = 'both')
homein.mainloop()
