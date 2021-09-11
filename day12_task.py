import tkinter as ktr
app=ktr.Tk(__name__)
app.geometry('500x300')
i1=ktr.Variable(app)
i2=ktr.Variable(app)
ans=ktr.Variable(app)
ktr.Entry(app, textvariable=i1).place(x=50,y=20)
ktr.Entry(app, textvariable=i2).place(x=300,y=20)
ktr.Label(app, text='input1').place(x=80,y=45)
ktr.Label(app, text='input2').place(x=330,y=45)
def add():
    ans.set(int(i1.get())+int(i2.get()))
def sub():
    ans.set(int(i1.get())-int(i2.get()))
def multiply():
    ans.set(int(i1.get())*int(i2.get()))
def divide():
    ans.set(int(i1.get())/int(i2.get()))

ktr.Button(app, text='  +  ', command=add).place(x=80,y=100)
ktr.Button(app, text='  -  ', command=sub).place(x=160,y=100)
ktr.Button(app, text='  *  ', command=multiply).place(x=240,y=100)
ktr.Button(app, text='  /  ', command=divide).place(x=320,y=100)
ktr.Label(app, textvariable= ans).place(x=230,y=200)
app.mainloop()
