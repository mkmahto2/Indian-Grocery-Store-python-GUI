from Tkinter import *
from sqlite3 import dbapi2 as sqlite
from PIL import ImageTk,Image
import ttk
def again():
    root=Tk()
    root.title('GROCERY STORE')
    img = ImageTk.PhotoImage(Image.open('login.gif'))
    panel = Label(root, image = img).grid(row=0, column=0,columnspan=20)
    un=Entry(root,width=15,font='Times 18 bold italic',bg='gray27',fg='lemon chiffon')
    un.place(x=200, y=303)
    pwd=Entry(root,width=15, show="*",font='Times 18 ',bg='gray27',fg='lemon chiffon')
    pwd.place(x=705, y=303)
    en=Button(root,width=20,text='Enter',command=check,font='Times 10 bold italic')
    en.place(x=300, y=380)
    exi=Button(root,width=20,text='Close',command=root.destroy,font='Times 10 bold italic')
    exi.place(x=505, y=380)
    root.mainloop()
#check the password and login
def check():
    global un, pwd, root
    u=un.get()
    p=pwd.get()
    if 'Sahil'!=u and 'sss'!=p:
        top=Tk()
        Label(top,width=30, text='Wrong Username or Password').grid(row=0, column=0)
        
        top.mainloop()
    else:
        root.destroy()


again()
