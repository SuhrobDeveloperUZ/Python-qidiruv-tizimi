from tkinter import *
import webbrowser
oyna = Tk()
oyna.title('Google Clienti')
oyna.geometry('500x300')
oyna.config(bg='deepskyblue')
def bosilish():
 webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % qidiruvSorovi.get())
mavzusi = Label(text='Dasturchi: Obitov Suhrob', fg='mediumblue', bg = 'lightgreen', font=("magneto", 12, 'bold'), relief=SOLID, bd = 3)
mavzusi.place(x=5, y=0, width=245, height=40)
qidiruvMavzusi = Label(text='So`zingizni kiriting...', font=("Times", 14, 'bold'), fg='indigo', bg='deepskyblue')
qidiruvMavzusi.place(x=160, y=80)
qidiruvSorovi = Entry(bg='white', fg='mediumblue', font=('Comic Sans Ms', 10, 'bold'), relief = SOLID)
qidiruvSorovi.place(x=104, y=120, width = 280, height = 30)
qidirish = Button(text='Qidirish', bg='deepskyblue', fg='black', font=('Comic Sans Ms', 10, 'bold'), relief=SOLID, cursor='hand2', width=30, command=bosilish)
qidirish.place(x=123, y=157)
oyna.mainloop()
