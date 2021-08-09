from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time

root=Tk()
var=Toplevel()

iss=0

class stu:
    def btn(self):
        def exit1():
            root.destroy()
        def a1():
            def exit1():
                var.destroy()
            def a11():
                global iss
                def b11():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e11.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-A brief history of time")
                    Lb.insert(2,"-The selfish gene")
                    Lb.insert(3,"-The Principle")
                    Lb.insert(4,"-Big Bang")
                    Lb.grid(row=2,column=2)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=2)
                def b21():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e11.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Aesop's Fables")
                    Lb.insert(2,"-Grandmother's bag of story")
                    Lb.insert(3,"-Panchtantra")
                    Lb.insert(4,"-The Rainbow fish")
                    Lb.grid(row=2,column=3)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=3)
                def b31():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e11.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Micro economics")
                    Lb.insert(2,"-Macro economics")
                    Lb.insert(3,"-Industial economics")
                    Lb.insert(4,"-Behavirial economics")
                    Lb.grid(row=2,column=4)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=4)
                def b41():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e11.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Vedic maths")
                    Lb.insert(2,"-Trignometry")
                    Lb.insert(3,"-Linear")
                    Lb.insert(4,"-Curves")
                    Lb.grid(row=2,column=5)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=5)
                def b51():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e11.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Basic computer")
                    Lb.insert(2,"-Advance language")
                    Lb.insert(3,"-Data science")
                    Lb.insert(4,"-Developer")
                    Lb.grid(row=2,column=6)
                    b10=Button(var,text="Submit",command=a41) 
                    b10.grid(row=3,column=6)
                b5=Button(var,text="science",bg="light blue",font=('Broadway',10),width=14,command=b11)
                b6=Button(var,text="story books",bg="light blue",font=('Broadway',10),width=14,command=b21)
                b7=Button(var,text="Economics",bg="light blue",font=('Broadway',10),width=14,command=b31)
                b8=Button(var,text="Maths",bg="light blue",font=('Broadway',10),width=14,command=b41)
                b9=Button(var,text="Computer",bg="light blue",font=('Broadway',10),width=14,command=b51)               
                b5.grid(row=1,column=2)
                b6.grid(row=1,column=3)
                b7.grid(row=1,column=4)
                b8.grid(row=1,column=5)
                b9.grid(row=1,column=6)
            def a12():
                global iss
                l7=Label(var,text="You have successfully issued the book",fg="green")
                l7.grid(row=6)
                iss=iss+1
                if(iss==1):
                    l8=Label(var,text="You can issue one more book if you want to:",fg="green")
                    l8.grid(row=7)
                elif(iss==2):
                    l9=Label(var,text="You have issued max number of books!!!!!!",fg="red")
                    l9.grid(row=7)
            var.title("Issue")
            l11=Label(var,text="Enter book name: ",font="bold",fg="purple")
            l11.grid(row=1)
            e11=Entry(var)
            e11.grid(row=1,column=1)
            b11=Button(var,text="Click me\nto issue",bg="light blue",fg="Blue",font="impact",command=a12)
            b11.grid(row=2,column=0)
            b12=Button(var,text="Book List",bg="light green",font=('elephant',10,'bold'),width=12,command=a11)
            b12.grid(row=0,column=2)
            b13=Button(var,text="EXIT",fg="Red",font=('elephant',10,'bold'),width=12,command=exit1)
            b13.grid(row=0,column=1)
        def a2():
            var.title("ReIssue")
            def exit1():
                var.destroy()
            def a21():
                global iss
                def b11():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-A brief history of time")
                    Lb.insert(2,"-The selfish gene")
                    Lb.insert(3,"-The Principle")
                    Lb.insert(4,"-Big Bang")
                    Lb.grid(row=2,column=2)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=2)
                def b21():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Aesop's Fables")
                    Lb.insert(2,"-Grandmother's bag of story")
                    Lb.insert(3,"-Panchtantra")
                    Lb.insert(4,"-The Rainbow fish")
                    Lb.grid(row=2,column=3)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=3)
                def b31():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Micro economics")
                    Lb.insert(2,"-Macro economics")
                    Lb.insert(3,"-Industial economics")
                    Lb.insert(4,"-Behavirial economics")
                    Lb.grid(row=2,column=4)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=4)
                def b41():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Vedic maths")
                    Lb.insert(2,"-Trignometry")
                    Lb.insert(3,"-Linear")
                    Lb.insert(4,"-Curves")
                    Lb.grid(row=2,column=5)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=5)
                def b51():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Basic computer")
                    Lb.insert(2,"-Advance language")
                    Lb.insert(3,"-Data science")
                    Lb.insert(4,"-Developer")
                    Lb.grid(row=2,column=6)
                    b10=Button(var,text="Submit",command=a41) 
                    b10.grid(row=3,column=6)
                b5=Button(var,text="science",bg="light blue",font=('Broadway',10),width=14,command=b11)
                b6=Button(var,text="story books",bg="light blue",font=('Broadway',10),width=14,command=b21)
                b7=Button(var,text="Economics",bg="light blue",font=('Broadway',10),width=14,command=b31)
                b8=Button(var,text="Maths",bg="light blue",font=('Broadway',10),width=14,command=b41)
                b9=Button(var,text="Computer",bg="light blue",font=('Broadway',10),width=14,command=b51)               
                b5.grid(row=1,column=2)
                b6.grid(row=1,column=3)
                b7.grid(row=1,column=4)
                b8.grid(row=1,column=5)
                b9.grid(row=1,column=6)
            def a22():
                if(b==int(e8.get())):
                    d=int(c)-int(e7.get())
                    if(d>14):
                        def a221():
                            l11=Label(var,text="Your book is successfully reissued for next 14 days",fg="black",font="elephant")
                            l11.grid(row=10)
                        e=d-14
                        f=e*5
                        l9=Label(var,text="You have to pay a fine of Rs:",fg="green",font="verdana")
                        l9.grid(row=9)
                        l91=Label(var,text=f,fg="red",font="elephant")
                        l91.grid(row=9,column=1)
                        b9=Button(var,text="Paid and continue",fg="black",font="verda",command=a221)
                        b9.grid(row=9,column=2)
                    else:
                        l10=Label(var,text="Your book is successfully reissued for next 14 days",fg="black",font="elephant")
                        l10.grid(row=10)
                elif(b>int(e8.get())):
                    mn=b-int(e8.get())
                    d=int(c)+(30-int(e7.get()))+(30*(mn-1))
                    if(d>14):
                        def a222():
                            l11=Label(var,text="Your book is successfully reissued for next 14 days",fg="black",font="elephant")
                            l11.grid(row=10)
                        e=d-14
                        f=e*5
                        l9=Label(var,text="You have to pay a fine of Rs:",fg="purple",font="bold")
                        l9.grid(row=9)
                        l91=Label(var,text=f)
                        l91.grid(row=9,column=1)
                        b9=Button(var,text="Paid and continue",fg="dark red",bg="light blue",command=a222)
                        b9.grid(row=9,column=2)
                    else:
                        l10=Label(var,text="Your book is successfully reissued for next 14 days",fg="black",font="elephant")
                        l10.grid(row=10)
            l6=Label(var,text="Enter the book name:",fg="green",font="verdana")
            l6.grid(row=1)
            e6=Entry(var)
            e6.grid(row=1,column=1)
            l7=Label(var,text="Enter date on which book is issued:",fg="green",font="verdana")
            l7.grid(row=2,column=0)
            e7=Entry(var)
            e7.grid(row=2,column=1)
            l8=Label(var,text="Enter month in which book is issued:",fg="green",font="verdana")
            l8.grid(row=3)
            e8=Entry(var)
            e8.grid(row=3,column=1)
            b7=Button(var,text="Submit",bg="light blue",fg="dark red",command=a22)
            b7.grid(row=4)
            b12=Button(var,text="Book List",bg="light green",font=('elephant',10,'bold'),width=12,command=a21)
            b12.grid(row=0,column=2)
            b13=Button(var,text="EXIT",fg="Red",font=('elephant',10,'bold'),width=12,command=exit1)
            b13.grid(row=0,column=1)
            a=time.asctime()
            c=a[8:10]
            if(a[4:7]=='Jan'):
                b=1    
            elif(a[4:7]=='Feb'):
                b=2
            elif(a[4:7]=='Mar'):
                b=3
            elif(a[4:7]=='Apr'):
                b=4    
            elif(a[4:7]=='May'):
                b=5    
            elif(a[4:7]=='Jun'):
                b=6    
            elif(a[4:7]=='Jul'):
                b=7    
            elif(a[4:7]=='Aug'):
                b=8    
            elif(a[4:7]=='Sep'):
                b=9    
            elif(a[4:7]=='Oct'):
                b=10    
            elif(a[4:7]=='Nov'):
                b=11
            elif(a[4:7]=='Dec'):
                b=12
            else:
                print("INVALID")
        def a3():
            var.title("Return")
            def exit1():
                var.destroy()
            def a31():
                global iss
                def b11():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-A brief history of time")
                    Lb.insert(2,"-The selfish gene")
                    Lb.insert(3,"-The Principle")
                    Lb.insert(4,"-Big Bang")
                    Lb.grid(row=2,column=2)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=2)
                def b21():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Aesop's Fables")
                    Lb.insert(2,"-Grandmother's bag of story")
                    Lb.insert(3,"-Panchtantra")
                    Lb.insert(4,"-The Rainbow fish")
                    Lb.grid(row=2,column=3)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=3)
                def b31():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Micro economics")
                    Lb.insert(2,"-Macro economics")
                    Lb.insert(3,"-Industial economics")
                    Lb.insert(4,"-Behavirial economics")
                    Lb.grid(row=2,column=4)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=4)
                def b41():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Vedic maths")
                    Lb.insert(2,"-Trignometry")
                    Lb.insert(3,"-Linear")
                    Lb.insert(4,"-Curves")
                    Lb.grid(row=2,column=5)
                    b10=Button(var,text="Submit",command=a41)
                    b10.grid(row=3,column=5)
                def b51():
                    def a41():
                        selec=Lb.curselection()
                        for i in selec:
                            e6.insert(1,Lb.get(i))
                    Lb=Listbox(var,selectmode=EXTENDED,bg="light blue")
                    Lb.insert(1,"-Basic computer")
                    Lb.insert(2,"-Advance language")
                    Lb.insert(3,"-Data science")
                    Lb.insert(4,"-Developer")
                    Lb.grid(row=2,column=6)
                    b10=Button(var,text="Submit",command=a41) 
                    b10.grid(row=3,column=6)
                b5=Button(var,text="science",bg="light blue",font=('Broadway',10),width=14,command=b11)
                b6=Button(var,text="story books",bg="light blue",font=('Broadway',10),width=14,command=b21)
                b7=Button(var,text="Economics",bg="light blue",font=('Broadway',10),width=14,command=b31)
                b8=Button(var,text="Maths",bg="light blue",font=('Broadway',10),width=14,command=b41)
                b9=Button(var,text="Computer",bg="light blue",font=('Broadway',10),width=14,command=b51)               
                b5.grid(row=1,column=2)
                b6.grid(row=1,column=3)
                b7.grid(row=1,column=4)
                b8.grid(row=1,column=5)
                b9.grid(row=1,column=6)
            def a32():
                if(b==int(e8.get())):
                    d=int(c)-int(e7.get())
                    if(d>14):
                        def a321():
                            l11=Label(var,text="Your book is successfully returned",fg="black",font="elephant")
                            l11.grid(row=10)
                        e=d-14
                        f=e*5
                        l9=Label(var,text="You have to pay a fine of Rs:",fg="green",font="verdana")
                        l9.grid(row=9)
                        l91=Label(var,text=f,fg="red",font="elephant")
                        l91.grid(row=9,column=1)
                        b9=Button(var,text="Paid and continue",fg="black",font="verda",command=a321)
                        b9.grid(row=9,column=2)
                    else:
                        l10=Label(var,text="Your book is successfully returned",fg="black",font="elephant")
                        l10.grid(row=10)
                elif(b>int(e8.get())):
                    mn=b-int(e8.get())
                    d=int(c)+(30-int(e7.get()))+(30*(mn-1))
                    if(d>14):
                        def a322():
                            l11=Label(var,text="Your book is successfully returned",fg="black",font="elephant")
                            l11.grid(row=10)
                        e=d-14
                        f=e*5
                        l9=Label(var,text="You have to pay a fine of Rs:",fg="purple",font="bold")
                        l9.grid(row=9)
                        l91=Label(var,text=f)
                        l91.grid(row=9,column=1)
                        b9=Button(var,text="Paid and continue",fg="dark red",bg="light blue",command=a322)
                        b9.grid(row=9,column=2)
                    else:
                        l10=Label(var,text="Your book is successfully returned",fg="black",font="elephant")
                        l10.grid(row=10)
            
            l6=Label(var,text="Enter the book name to return:",fg="green",font="verdana")
            l6.grid(row=1)
            e6=Entry(var)
            e6.grid(row=1,column=1)
            l7=Label(var,text="Enter date on which book is issued:",fg="green",font="verdana")
            l7.grid(row=2,column=0)
            e7=Entry(var)
            e7.grid(row=2,column=1)
            l8=Label(var,text="Enter month in which book is issued:",fg="green",font="verdana")
            l8.grid(row=3)
            e8=Entry(var)
            e8.grid(row=3,column=1)
            b7=Button(var,text="Submit",bg="light blue",fg="dark red",command=a32)
            b7.grid(row=4)
            b12=Button(var,text="Book List",bg="light green",font=('elephant',10,'bold'),width=12,command=a31)
            b12.grid(row=0,column=2)
            b13=Button(var,text="EXIT",fg="Red",font=('elephant',10,'bold'),width=12,command=exit1)
            b13.grid(row=0,column=1)
            a=time.asctime()
            c=a[8:10]
            if(a[4:7]=='Jan'):
                b=1    
            elif(a[4:7]=='Feb'):
                b=2
            elif(a[4:7]=='Mar'):
                b=3
            elif(a[4:7]=='Apr'):
                b=4    
            elif(a[4:7]=='May'):
                b=5    
            elif(a[4:7]=='Jun'):
                b=6    
            elif(a[4:7]=='Jul'):
                b=7    
            elif(a[4:7]=='Aug'):
                b=8    
            elif(a[4:7]=='Sep'):
                b=9    
            elif(a[4:7]=='Oct'):
                b=10    
            elif(a[4:7]=='Nov'):
                b=11
            elif(a[4:7]=='Dec'):
                b=12
            else:
                print("INVALID")
        messagebox.showinfo("WELCOME","Welcome to Library!!!")
        adn=simpledialog.askinteger("ID number","What is your ID number")
        list1=["Niraj","Siwani","Shreya","Rohit","Mohit","Emran","Shweta","Neha","Pradeep","Shilpa"]
        list2=['01','02','03','04','05','06','07','08','09','10']
        list3=[12,6,8,9,11,7,12,6,8,9]
        list4=[11101,11102,11103,11104,11105,11106,11107,11108,11109,11110]
        if(adn in list4):
            b=list4.index(adn)
            l3=Label(root,text="Name:",fg="purple",font="bold")
            l31=Label(root,text=list1[b])
            l4=Label(root,text="Roll no.:",fg="purple",font="bold")
            l41=Label(root,text=list2[b])
            l5=Label(root,text="Class:",fg="purple",font="bold")
            l51=Label(root,text=list3[b])
            l3.grid(row=2)
            l31.grid(row=2,column=1)
            l4.grid(row=3)
            l41.grid(row=3,column=1)
            l5.grid(row=4)
            l51.grid(row=4,column=1)
            l1=Label(root,text="Choose to move ahead",fg="blue",font=('Algerian'))
            l1.grid(row=0)
            b1=Button(root,text="Issue\nBook",bg="light green",font=('elephant',10,'bold'),width=12,command=a1)
            b2=Button(root,text="Reissue\nBook",bg="light green",font=('elephant',10,'bold'),width=12,command=a2)
            b3=Button(root,text="Return\nBook",bg="light green",font=('elephant',10,'bold'),width=12,command=a3)
            b4=Button(root,text="EXIT",fg="Red",command=exit1,font=('elephant',10,'bold'),width=12)            
            b1.grid(row=1,column=1)
            b2.grid(row=1,column=2)
            b3.grid(row=1,column=3)
            b4.grid(row=0,column=2)
        else:
            l10=Label(root,text="Invalid ID number\nTry again ",fg="red",font="elephant")
            l10.grid(row=2)

a=stu()
a.btn()
root.mainloop()
