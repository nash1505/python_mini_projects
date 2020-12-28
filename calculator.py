from tkinter import *

def addition():
    result = int(num1.get()) + int(num2.get())
    res.set(result)

def substraction():
    result = int(num1.get()) - int(num2.get())
    res.set(result)

def multiplication():
    result = int(num1.get()) * int(num2.get())
    res.set(result)

def division():
    result = int(num1.get()) / int(num2.get())
    res.set(result)
    
    
root = Tk()
labelframe = LabelFrame(root, text = "CALCULATOR")


root.title('MY CAlCULATOR')

res = StringVar()
num1 = Entry(root,width='10')

num2 = Entry(root, width='10')
num1.grid(row=3,column=1,padx=4,ipady=4)
num2.grid(row=3,column=2,padx=2,ipady=4)

Label(root,text='',textvariable=res).grid(row=3,column=3,ipady=4)





Button(root,text='Addition',width='20',command=addition).grid(row=5,column=0)
Button(root,text='Substraction',width='20',command=substraction).grid(row=5,column=1)

Button(root,text='multiplication',width='20',command=multiplication).grid(row=5,column=2)
Button(root,text='division',width='20',command=division).grid(row=5,column=3)


root.mainloop()