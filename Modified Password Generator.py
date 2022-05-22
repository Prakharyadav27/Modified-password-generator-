from tkinter import *
import pyperclip
import random
from password_strength import *
import math
from tkinter import messagebox

root=Tk()
root.geometry('350x350')
root.title('Python MiniProject')

passstr = StringVar()
passlen_smallalpha = IntVar()
passlen_bigalpha = IntVar()
passlen_digits = IntVar()
passlen_specialcharac = IntVar()
passstr2 = StringVar()
passstr1 = StringVar()
passlen_smallalpha.set(0)
passlen_bigalpha.set(0)
passlen_digits.set(0)
passlen_specialcharac.set(0)
def generate():
    list1= []
    small=passlen_smallalpha.get()
    big= passlen_bigalpha.get()
    digits = passlen_digits.get()
    special = passlen_specialcharac.get()
    pass1 =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s''t','u','v','w','x','y','z']
    pass2= ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J','K','L','0','P','Q','R','S','T', 'U', 'V', 'W', 'X', 'y', 'Z']
    pass3= ['1', '2', '3','4','5','6','7','8','9','0']
    pass4 = ['!', 'e','#', 's', '%','&','*']

    password = ""
    mylist=[pass1, pass2,pass3, pass4]
    k=1


    while(k==1):
     random.shuffle (mylist)
     list1=mylist
    for q in range(4):
        if(list1[q][0]== 'A' and big != 0):
                password = password + random.choice(pass2)
                big==1
        if(list1[q][0]== 'a' and small!=0):
                password = password + random.choice(pass1)
                small==1

        if(list1[q][0]=='1' and digits != 0):
                password = password + random.choice(pass3)
                digits==1
        if(list1[q][0]=='!' and special != 0):
                password = password + random.choice(pass4)
                special==1
        if(small==0 and big==0 and digits==0 and special==0):
                break

    passstr.set(password)

def copy_to_clipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

def module_1():
    f1=Frame()
    f1.place(x=0, y=0,width=350,height=350)
    Label(f1, text="Password Generator ", font="calibre 20 bold").pack()

    Label(f1,text="Enter no. of small Alphabets").pack(pady=3)
    Entry(f1, textvariable = passlen_smallalpha).pack(pady=3)

    Label(f1, text="Enter no. of Big Alphabets").pack(pady=3)
    Entry(f1, textvariable=passlen_bigalpha). pack(pady=3)

    Label(f1, text="Enter no. of Digits").pack(pady=3)
    Entry(f1, textvariable=passlen_digits). pack(pady=3)

    Label(f1, text="Enter no. of Special Characters").pack(pady=3)
    Entry(f1, textvariable=passlen_specialcharac).pack(pady=3)

    Button(f1, text="Generate Password", command=generate).pack(pady=7)
    Entry(f1, textvariable=passstr).pack(pady=3)
    Button (f1, text="Copy to clipboard", command=copy_to_clipboard).pack()
    Button(f1, text='->', command=home).place(x=0,y=0)

def strength_checker():
    f1=Frame()
    f1.place(x=0,y=0,width=350,height=350)
    if passstr2.get() == "":
      messagebox.showinfo("Error", "Password Can't be Empty")
    else:
      result = PasswordStats(passstr2.get())
      final = result.strength()
      label1= Label(f1, text="")
      w = Canvas(f1,height=100, width=600)
      w.pack()
      label1.place(x=170, y=100)
      label1["text"]- str(math.ceil(final * 100)) + "%"
      if final >= 0.66:
          w.create_rectangle(70, 50, 280, 100, fill="#27cf54", outline="white")
      elif final > 0.10 and final < 0.40:
          w.create_rectangle(70, 50, 280, 100, fill="#ff007", outline="white")
      elif final <= 0.10:
          w.create_rectangle(70, 50, 280, 100, fill="#de3c3c", outline="white")
      b = Button(f1, text="->", command=module_2)
      b.place(x=0, y=0)


def module_2():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    head = Label(f1, text="Password Strength Calculator", font=("helvetica", 15, "bold"))
    head.pack(ipadx=12, ipady=12)
    label = Label(f1, text="Enter Your Password", font=("helvetica", 10, "bold"))
    label.pack(ipadx=5, ipady=5)
    entry = Entry(f1, textvariable=passstr2)
    entry.pack(ipadx=30, ipady=5)
    button = Button(f1, text="check", command=strength_checker)
    button.pack(ipadx=5, ipady=5)
    b = Button(f1, text="-3", command=home)
    b.place(x=0, y=0)


def check_ch():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    string = passstr.get()
    alphabets = digits = special = 0

    for i in range(len(string)):
        if (string[i].isalpha()):
            alphabets = alphabets + 1
        elif (string[i].isdigit()):
            digits-digits+1
        else:
            special =special+1
    b=Button(f1, text="->", command=module_3)
    b.place(x=0, y=0)
    l1=Label(f1,text={"alphabets",alphabets})
    l1.pack()
    l2=Label(f1, text={" digits ",digits})
    l2.pack()
    l3=Label(f1, text={" special symbol ", special})
    l3.pack()

def module_3():
    f1=Frame()
    f1.place(x=0, y=0,width=350,height=350)
    label=Label(f1, text=" Enter your password ")
    label.pack()
    entry=Entry(f1, textvariable=passstr1)
    entry.pack()
    b1=Button(f1, text="Check Character", command=check_ch)
    b1.place(x=0,y=0)
def home():
    f1=Frame()
    f1.place(x=0,y=0,width=350,height=50)
    label=Label(f1,text="Click on button to select a module")
    label.pack()
    button1=Button(f1, text="Random password generator",command= module_1)
    button1.place(x=100, y=50)
    button2 = Button(f1, text="Password strength check", command=module_2)
    button2.place(x=107, y=100)
    button3=Button(f1, text="Character type  check",command=module_3)
    button3.place(x=117,y=150)
home()
root.mainloop()
