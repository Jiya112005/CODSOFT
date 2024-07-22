import random 
from tkinter import *
from tkinter import messagebox

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
numbers = ['0','1','2','3','4','5','6','7','8','9']
specials = ['!',',','#','$','%','^','&','*','(',')','~','+','[',']','{','}',';',':','.','<','>','@','`',' ']


def gen():
    try:
        total_letters = int(second.get())
        total_symbols = int(four.get())
        total_numbers = int(third.get())
        length = int(first.get())
        password_list =[]
        
        # for i in range(1,len+1):
        for char in range(1,total_letters+1):
                password_list.append(random.choice(letters))
        for char in range(1,total_symbols+1):
                password_list+=random.choice(specials)
        for char in range(1,total_numbers+1):
                password_list += random.choice(numbers)
        
        random.shuffle(password_list)
        print(password_list)
        print(length)
        password=""
        for char in password_list:
            password+=char
        if len(password) != length:
            resultlbl.config(text="all lengths must be sum up to total length")
        else:
            resultlbl.config(text=f"Password is: {password}")
        
        # lengthlabel.config(text=f"Total Length:{length}")
    except ValueError:
        messagebox.showerror("Enter valid number")



#window fundamentals
window = Tk()
window.title("Password Generator")
window.minsize(width=1000,height=350)
#label for heading 
head = Label(window,text="Generate your password!",bg="lightgreen",font=("Times New Roman bold",25))
head.pack()

#label for taking inputs password
lengthlabel = Label(window,text="Enter the total length: ",bg="violet",font=("calibri",18))
lengthlabel.place(x=10,y=50)
letterlbl = Label(window,text="Enter no. of Letters: ",bg="violet",font=("calibri",18))
letterlbl.place(x=10,y=90)
numlabel = Label(window,text="Enter no. of Numbers: ",bg="violet",font=("calibri",18))
numlabel.place(x=10,y=130)
speciallbl = Label(window,text="Enter no. of special character: ",bg="violet",font=("calibri",18))
speciallbl.place(x=10,y=170)

#label for the generated passsword
resultlbl = Label(window,text="Generated password here ",bg="yellow",font=("calibri bold",18))
resultlbl.place(x=190,y=270)
# ans = Label(window,text="",bg="pink",font=("calibri",18))
# ans.place(x=490,y=270)
#entry textboxes for inputs
first = Entry(window,width=30,bd=3)
second = Entry(window,width=30,bd=3)
third = Entry(window,width=30,bd=3)
four = Entry(window,width=30,bd=3)

#setting position for the textboxes
first.place(x=260,y=60)
second.place(x=260,y=100)
third.place(x=260,y=140)
four.place(x=310,y=180)

#making button for generator
btngen = Button(window,text="Generate",font=("calibri bold",18),bg="lightgrey",command=lambda:gen())
btngen.place(x=200,y=210)
window.mainloop()
