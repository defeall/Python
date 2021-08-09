from tkinter import *
from tkinter import messagebox
import math
root=Tk()
fm=Frame(root)
fm.grid(row=5,columnspan=1)
fm1=Frame(root)
fm1.grid(row=0)
messagebox.showinfo("Welcome","Welcome to Calculator")

operator=""
class calci:
    def lg(self):
        def clickme(numbers):
            global operator
            operator=operator+str(numbers)
            text_input.set(operator) 
        def clrdisplay():
            global operator
            operator=""
            text_input.set("")
        def equals():
            global operator
            if '^' in operator:
                b=operator.index('^')
                c=operator[0:b]
                d=operator[b+1:]
                a=math.pow(int(c),int(d))
                text_input.set(str(a))
            elif 'log' in operator:
                c=operator[4:]
                d=math.log(int(c))
                text_input.set(str(d))
            elif '√' in operator:
                b=operator.index('√')
                c=operator[b+1:]
                a=math.sqrt(int(c))
                text_input.set(str(a))
            elif 'sin' in operator:
                c=operator[4:]
                d=math.sin(int(c))
                text_input.set(str(d))
            elif 'cos' in operator:
                c=operator[4:]
                d=math.cos(int(c))
                text_input.set(str(d))
            elif 'tan' in operator:
                c=operator[4:]
                d=math.tan(int(c))
                text_input.set(str(d))
            elif 'rad' in operator:
                c=operator[4:]
                d=math.radians(int(c))
                text_input.set(str(d))
            else:
                sumup=str(eval(operator))
                text_input.set(sumup)
            operator=""
            

        text_input=StringVar()

        b1=Button(fm1,text="1",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(1))
        b2=Button(fm1,text="2",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(2))
        b3=Button(fm1,text="3",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(3))
        b4=Button(fm1,text="+",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("+"))
        b5=Button(fm1,text="4",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(4))
        b6=Button(fm1,text="5",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(5))
        b7=Button(fm1,text="6",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(6))
        b8=Button(fm1,text="-",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("-"))
        b9=Button(fm1,text="7",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(7))
        b10=Button(fm1,text="8",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(8))
        b11=Button(fm1,text="9",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(9))
        b12=Button(fm1,text="*",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("*"))
        b13=Button(fm1,text=".",width=2,height=2,fg="Black",bg="Green",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("."))
        b14=Button(fm1,text="0",width=2,height=2,fg="Black",bg="Sky blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(0))
        b15=Button(fm1,text="=",width=2,height=2,fg="Black",bg="Green",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=equals)
        b16=Button(fm1,text="/",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("/"))
        b17=Button(fm1,text="C",width=2,height=2,fg="Black",bg="Red",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=clrdisplay)
        b18=Button(fm1,text="(",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("("))
        b19=Button(fm1,text=")",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(")"))
        b20=Button(fm1,text="π",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(3.141592653))
        b21=Button(fm1,text="log",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("log("))
        b22=Button(fm1,text="√",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("√"))
        b23=Button(fm1,text="e",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme(2.7182818))
        b24=Button(fm1,text="^",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("^"))
        b25=Button(fm1,text="sin",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("sin("))
        b26=Button(fm1,text="cos",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("cos("))
        b27=Button(fm1,text="tan",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("tan("))
        b28=Button(fm1,text="rad",width=2,height=2,fg="Black",bg="Blue",bd=8,font=('Calibri',15,'bold'),relief=SUNKEN,command=lambda:clickme("rad("))
        b1.grid(row=0,column=0)
        b2.grid(row=0,column=1)
        b3.grid(row=0,column=2)
        b4.grid(row=0,column=3)
        b18.grid(row=0,column=4)
        b21.grid(row=0,column=5)
        b25.grid(row=0,column=6)
        b5.grid(row=1,column=0)
        b6.grid(row=1,column=1)
        b7.grid(row=1,column=2)
        b8.grid(row=1,column=3)
        b19.grid(row=1,column=4)
        b22.grid(row=1,column=5)
        b26.grid(row=1,column=6)
        b9.grid(row=2,column=0)
        b10.grid(row=2,column=1)
        b11.grid(row=2,column=2)
        b12.grid(row=2,column=3)
        b20.grid(row=2,column=4)
        b23.grid(row=2,column=5)
        b27.grid(row=2,column=6)
        b13.grid(row=3,column=0)
        b14.grid(row=3,column=1)
        b15.grid(row=3,column=2)
        b16.grid(row=3,column=3)
        b24.grid(row=3,column=4)
        b28.grid(row=3,column=5)
        b17.grid(row=3,column=6)
        l1=Label(fm,text="Output",bg="Yellow",fg="Black",font=('Algerian',15,'bold'),bd=10)
        l1.grid(row=5,column=1)
        e1=Entry(fm,textvariable=text_input,font=('Broadway',15,'bold'),bg="Light Green")
        e1.grid(row=6,column=1)
        
abc=calci()
abc.lg()
root.mainloop()
           
