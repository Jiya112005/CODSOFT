#import library
from tkinter import *

def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def product(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "cannot divide by zero!"




def calc(operation):  #operation for buttons
    try:
        n1=float(e1.get())
        n2=float(e2.get())
        
        if operation == "+":
            ans=addition(n1,n2)
        elif operation == "-":
            ans=subtraction(n1,n2)
        elif operation == "*":
            ans=product(n1,n2)
        elif operation == "/":
            ans=divide(n1,n2)
        
        res.config(text=f"Equals to: {ans}")
    except ValueError:
        print("Invalid input")

#creating the root window first
root=Tk()
root.title("Calculator Application")
root.minsize(width=300,height=400)
#Creating a label for heading 
labelhead = Label(root,text="BASIC CALCULATOR",bg="lightblue",font="large")
labelhead.pack()

#creating label for taking input numbers
lbl1=Label(root,text="Enter First number:",font=("calibri",15))
lbl1.place(x=5,y=30)
lbl2=Label(root,text="Enter Second number:",font=("calibri",15))
lbl2.place(x=5,y=90)

#creating textbox for input numbers
e1=Entry(root,width=30,bd=3)
e1.place(x=170,y=35)
e2=Entry(root,width=30,bd=3)
e2.place(x=198,y=95)

#creating buttons for calculation
b1=Button(root,text="Add(+)",font=("calibri bold",15),bg="lightblue",command=lambda:calc("+"))
b1.place(x=140,y=140)
b2=Button(root,text="Subtract(-)",font=("calibri bold",15),bg="lightblue",command=lambda:calc("-"))
b2.place(x=250,y=140)
b3=Button(root,text="Multiply(x)",font=("calibri bold",15),bg="lightblue",command=lambda:calc("*"))
b3.place(x=120,y=190)
b4=Button(root,text="Divide(/)",font=("calibri bold",15),bg="lightblue",command=lambda:calc("/"))
b4.place(x=260,y=190)

#creating a label for result
res=Label(root,text="Equals to: ",font=("calibri",15))
res.place(x=5,y=250)
root.mainloop()