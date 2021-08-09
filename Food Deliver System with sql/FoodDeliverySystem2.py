from tkinter import *
#import messagebox
import tkinter.messagebox
import mysql.connector
messagebox.showinfo("Welcome","Welcome to food delivery system")
root=Tk()
p=0
amount=0
operator=" "

#function if the user forget the password.
def forget():
    def okay():
        var.destroy()
    var=Tk()
    l11=Label(var,text="FORGET PASSWORD",fg="blue",font="Algerian")
    l11.grid(row=0)
    l12=Label(var,text="PLEASE SIGNUP AGAIN.",font="bold",fg="red")
    l12.grid(row=1)
    b11=Button(var,text="okay",fg="dark red",bg="light blue",command=okay)
    b11.grid(row=2)
#function for signup of new users.   
def signup():
    def submit():
        #signup is successfull only if new password is equal to confirm password.
        if(e22.get()==e23.get()):
            global result
            messagebox.showinfo("Succesfully register","You are Successfully registered!\nNow Login")
            #MySql connectivity
            db=mysql.connector.connect(host="localhost",user="root",password="Nirajkumar28@",database="FoodUser_record")
            cur=db.cursor()
            sq=cur.execute("INSERT INTO Foodtable(name,password,email_id) VALUES(%s %s %s)",
                       (e21.get(),e23.get(),e24.get()))
            ds=[(e21.get(),e23.get(),e24.get())]
            cur.executemany(sq,ds)
            cur.execute("select * from entries")
            result=cur.fetchall()
            for x in result:
                print(x)
            db.commit()
            db.close()               
        else:
            messagebox.showinfo("OOPS!","Something went wrong")
        var.destroy()
    #format for thenew user to signup.
    var=Tk()
    v321=Frame(var)
    v321.grid(row=0)
    v322=Frame(var)
    v322.grid(row=1)
    l21=Label(v321,text="FOOD FOR FOODIES",font="algerian",fg="blue")
    l21.grid(row=0)
    l22=Label(v322,text="Enter Username:",font="arial")
    l23=Label(v322,text="new Password:",font="arial")
    l24=Label(v322,text="confirm Password:",font="arial")
    l25=Label(v322,text="Email id:",font="arial")
    l22.grid(row=1)
    l23.grid(row=2)
    l24.grid(row=3)
    l25.grid(row=4)
    e21=Entry(v32)
    e22=Entry(v322)
    e23=Entry(v322)
    e24=Entry(v322)
    e21.grid(row=1,column=1)
    e22.grid(row=2,column=1)
    e23.grid(row=3,column=1)
    e24.grid(row=4,column=1)
    b21=Button(v322,text="Submit",command=submit)
    b21.grid(row=5,column=1)

def login():
    def click():
        #functions for the selection of dish.
        def indian():
            #the dish selected by user will go to the entry widget of selected dish.
            def c11():
                global p
                e31.insert(0,"CholeBhature")
                p=p+100            
            def c12():
                global p
                e31.insert(1,"Idli Sambhar")
                p=p+120
            def c13():
                global p
                e31.insert(2,"Dal Chawal")
                p=p+80
            def c14():
                global p
                e31.insert(3,"Vada Pav")
                p=p+60
            c311=Checkbutton(v32,text="CholeBhature    Rs.100/-",font=('georgia',12),fg="dark green",bg="white",command=c11)
            c312=Checkbutton(v32,text="Idli Sambhar    Rs.120/-",font=('georgia',12),fg="dark green",bg="white",command=c12)
            c313=Checkbutton(v32,text="Dal Chawal      Rs.80/-",font=('georgia',12),fg="dark green",bg="white",command=c13)
            c314=Checkbutton(v32,text="Vada Pav        Rs.60/-",font=('georgia',12),fg="dark green",bg="white",command=c14)
            c311.grid(row=2)
            c312.grid(row=3)
            c313.grid(row=4)
            c314.grid(row=5)
        def chinese():
          #the dish selected by user will go to the entry widget of selected dish.
            def c21():
                global p
                e31.insert(0,"Noodles")
                p=p+60 
            def c22():
                global p
                e31.insert(1,"Hakka Noodles")
                p=p+120 
            def c23():
                global p
                e31.insert(2,"Manchurein")
                p=p+120 
            def c24():
                global p
                e31.insert(3,"Chinese")
                p=p+100 
            c321=Checkbutton(v32,text="Noodles         Rs.60",font=('georgia',12),fg="dark green",bg="white",command=c21)
            c322=Checkbutton(v32,text="Hakka Noodles   Rs.120/-",font=('georgia',12),fg="dark green",bg="white",command=c22)
            c323=Checkbutton(v32,text="Manchurein      Rs.120/-",font=('georgia',12),fg="dark green",bg="white",command=c23)
            c324=Checkbutton(v32,text="Chinese         Rs.100/-",font=('georgia',12),fg="dark green",bg="white",command=c24)
            c321.grid(row=2,column=1)
            c322.grid(row=3,column=1)
            c323.grid(row=4,column=1)
            c324.grid(row=5,column=1)
        def italian():
          #the dish selected by user will go to the entry widget of selected dish.
            def c31():
                global p
                e31.insert(0,"Pizza")
                p=p+150 
            def c32():
                global p
                e31.insert(1,"Lasagne")
                p=p+120 
            def c33():
                global p
                e31.insert(2,"Risstto")
                p=p+120 
            def c34():
                global p
                e31.insert(3,"Bottargo")
                p=p+120 
            c331=Checkbutton(v32,text="Pizza      Rs.150",font=('georgia',12),fg="dark green",bg="white",command=c31)
            c332=Checkbutton(v32,text="Lasagna    Rs.120/-",font=('georgia',12),fg="dark green",bg="white",command=c32)
            c333=Checkbutton(v32,text="Risotto    Rs.120/-",font=('georgia',12),fg="dark green",bg="white",command=c33)
            c334=Checkbutton(v32,text="Bottarga   Rs.120/-",font=('georgia',12),fg="dark green",bg="white",command=c34)
            c331.grid(row=2,column=2)
            c332.grid(row=3,column=2)
            c333.grid(row=4,column=2)
            c334.grid(row=5,column=2)
        def fastfood():
             #the dish selected by user will go to the entry widget of selected dish.
            def c41():
                global p
                e31.insert(0,"Veg Burger")
                p=p+60 
            def c42():
                global p
                e31.insert(1,"Veg Maggie")
                p=p+40 
            def c43():
                global p
                e31.insert(2,"Egg Maggie")
                p=p+70 
            def c44():
                global p
                e31.insert(3,"Paneer Roll")
                p=p+80 
            c341=Checkbutton(v32,text="Veg Burger    Rs.60",font=('georgia',12),fg="dark green",bg="white",command=c41)
            c342=Checkbutton(v32,text="Veg Maggie    Rs.40/-",font=('georgia',12),fg="dark green",bg="white",command=c42)
            c343=Checkbutton(v32,text="Egg Maggie    Rs.70/-",font=('georgia',12),fg="dark green",bg="white",command=c43)
            c344=Checkbutton(v32,text="panner roll   Rs.80/-",font=('georgia',12),fg="dark green",bg="white",command=c44)
            c341.grid(row=2,column=3)
            c342.grid(row=3,column=3)
            c343.grid(row=4,column=3)
            c344.grid(row=5,column=3)
        def desert():
             #the dish selected by user will go to the entry widget of selected dish.
            def c51():
                global p
                e31.insert(0,"Strawberry icecream")
                p=p+40
            def c52():
                global p
                e31.insert(1,"vanilla icecream")
                p=p+40
            def c53():
                global p
                e31.insert(2,"pastry")
                p=p+45
            def c54():
                global p
                e31.insert(3,"choclate")
                p=p+20
            c351=Checkbutton(v32,text="Strwaberry icecream    Rs.40",font=('georgia',12),fg="dark green",bg="white",command=c51)
            c352=Checkbutton(v32,text="Vanilla               Rs.40/-",font=('georgia',12),fg="dark green",bg="white",command=c52)
            c353=Checkbutton(v32,text="Pastry                Rs.45/-",font=('georgia',12),fg="dark green",bg="white",command=c53)
            c354=Checkbutton(v32,text="choclate              Rs.20/-",font=('georgia',12),fg="dark green",bg="white",command=c54)
            c351.grid(row=7,column=0)
            c352.grid(row=8,column=0)
            c353.grid(row=9,column=0)
            c354.grid(row=10,column=0)
        def softdrink():
            #the dish selected by user will go to the entry widget of selected dish.
            def c61():
                global p
                e34.insert(0,"cocacola")
                p=p+25
            def c62():
                global p
                e34.insert(1,"sprite")
                p=p+30
            def c63():
                global p
                e34.insert(2,"sprite")
                p=p+80
            def c64():
                global p
                e34.insert(3,"Dew")
                p=p+25
            c361=Checkbutton(v32,text="Cocacola        Rs.25",font=('georgia',12),fg="dark green",bg="white",command=c61)
            c362=Checkbutton(v32,text="sprite(250ml)   Rs.30/-",font=('georgia',12),fg="dark green",bg="white",command=c62)
            c363=Checkbutton(v32,text="Sprite(2L)      Rs.80/-",font=('georgia',12),fg="dark green",bg="white",command=c63)
            c364=Checkbutton(v32,text="Dew(250ml)       Rs.25/-",font=('georgia',12),fg="dark green",bg="white",command=c64)
            c361.grid(row=7,column=3)
            c362.grid(row=8,column=3)
            c363.grid(row=9,column=3)
            c364.grid(row=10,column=3)
        def pay():
            global p
            global amount
            n=1
            n=e32.get()
            amount=amount+int(n)*p
            l30=Label(v32,text=amount)
            l30.grid(row=11,column=2)
        def calci():
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
                sumup=str(eval(operator))
                text_input.set(sumup)
                operator=""
            
            b41=Button(v34,text="1",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(1))
            b42=Button(v34,text="2",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(2))
            b43=Button(v34,text="3",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(3))
            b44=Button(v34,text="+",fg="Black",bg="Blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme("+"))
            b45=Button(v34,text="4",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(4))
            b46=Button(v34,text="5",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(5))
            b47=Button(v34,text="6",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(6))
            b48=Button(v34,text="-",fg="Black",bg="Blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme("-"))
            b49=Button(v34,text="7",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(7))
            b410=Button(v34,text="8",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(8))
            b411=Button(v34,text="9",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(9))
            b412=Button(v34,text="*",fg="Black",bg="Blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme("*"))
            b413=Button(v34,text="0",fg="Black",bg="Sky blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme(0))
            b414=Button(v34,text="/",fg="Black",bg="Blue",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=lambda:clickme("/"))
            b415=Button(v34,text="=",fg="Black",bg="Green",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=equals)
            b416=Button(v34,text="C",fg="Black",bg="Red",bd="6px",width="3",height="3",font=('Algerian',15,'bold'),command=clrdisplay)
            b41.grid(row=3,column=1)
            b42.grid(row=3,column=2)
            b43.grid(row=3,column=3)
            b44.grid(row=3,column=4)
            b45.grid(row=4,column=1)
            b46.grid(row=4,column=2)
            b47.grid(row=4,column=3)
            b48.grid(row=4,column=4)
            b49.grid(row=5,column=1)
            b410.grid(row=5,column=2)
            b411.grid(row=5,column=3)
            b412.grid(row=5,column=4)
            b413.grid(row=6,column=1)
            b414.grid(row=6,column=2)
            b415.grid(row=6,column=3)
            b416.grid(row=6,column=4)
            e41=Entry(v34,textvariable=text_input,font=('Broadway',15,'bold'),bg="Light Green")
            e41.grid(row=7,columnspan=6)
        #here we will destroy the login poage.
        root.destroy() 
        var=Tk()
        text_input=StringVar()
        v31=Frame(var)
        v32=Frame(var)
        v33=Frame(var)
        v34=Frame(var)
        v31.grid(row=0)
        v32.grid(row=1)
        v33.grid(row=0,column=1)
        v34.grid(row=1,column=1)
        #v31 frame.
        l31=Label(v31,text="FOOD FOR FOODIES",font=('algerian',80),fg="blue",bg="white")
        l31.grid(row=1)
        l32=Label(v31,text="INDIA'S best restaurent,",fg="red",font=('arial',25),bg="white")
        l32.grid(row=2)
        l33=Label(v31,text="Choose your cuisine",fg="dark red",font=('arial',20),bg="white")
        l33.grid(row=3)
        #v32 frame.
        b31=Button(v32,text="INDIAN",width="18",fg="Brown",font="ravie",bg="pink",command=indian)
        b32=Button(v32,text="CHINESE",width="18",fg="Brown",font="ravie",bg="pink",command=chinese)
        b33=Button(v32,text="ITALIAN",width="18",fg="Brown",font="ravie",bg="pink",command=italian)
        b34=Button(v32,text="Fast Food",width="18",fg="Brown",font="ravie",bg="pink",command=fastfood)
        b35=Button(v32,text="Deserts",width="18",fg="Brown",font="ravie",bg="pink",command=desert)
        b36=Button(v32,text="Softdrink",width="18",fg="Brown",font="ravie",bg="pink",command=softdrink) 
        b31.grid(row=1)
        b32.grid(row=1,column=1)
        b33.grid(row=1,column=2)
        b34.grid(row=1,column=3)
        b35.grid(row=6,column=0)
        b36.grid(row=6,column=3)   
        l34=Label(v32,text="Selected Dish:",font="ravie",bg="white") 
        e31=Entry(v32)
        l35=Label(v32,text="Enter the no.of plate:",font="ravie",bg="white")
        e32=Entry(v32)
        l36=Label(v32,text="Enter Promocode you have:",font="ravie",bg="white")
        e33=Entry(v32)
        l37=Label(v32,text="Softdrink:",font="ravie",bg="white")
        e34=Entry(v32)
        l34.grid(row=7,column=1)
        e31.grid(row=7,column=2)
        l35.grid(row=8,column=1)
        e32.grid(row=8,column=2)
        l36.grid(row=9,column=1)
        e33.grid(row=9,column=2)
        #grid for softdrink column.
        l37.grid(row=10,column=1)
        e34.grid(row=10,column=2)
        b37=Button(v32,text="bill:",font="ravie",bg="white",command=pay)
        b37.grid(row=11,column=1)
        #v3 Frame.
        b38=Button(v33,text="NEED CALCULATOR",font=('elephant',20),command=calci)
        b38.grid(row=0)
            
    #creating the list of names who are already registered.
    names=["siwani","niraj"]
    password=["niraj","siwani"]
    email=["siwani1022000@gmail.com","nirajlathar28@gmail.com"]
    #comparing username and password with the list.
    if(e01.get() in names):
        if(e02.get() in password):
            ni=names.index(e01.get())
            pi=password.index(e02.get())
            if ni==pi:
                b04=Button(root,text="click to conitnue",font="elephant",fg="dark red",bg="light blue",command=click)
                b04.grid(row=5,columnspan=4)               
            else:
                messagebox.showinfo("OOPs!","Wrong Username or Password")
    else:
        messagebox.showinfo("OOPs!","Wrong Username or Password")
        
#Entering username and password for registered user.
l01=Label(root,text="Food For Foodies",fg="violet",font="algerian",height="2")
l02=Label(root,text="UserName:",font="elephant")
l03=Label(root,text="Password",font="elephant")
e01=Entry(root)
e02=Entry(root)
b01=Button(root,text="Login",fg="dark red",bg="light blue",font="elephant",command=login)
b02=Button(root,text="Signup",fg="dark red",bg="light blue",font="elephant",command=signup)
b03=Button(root,text="forgot Password?",fg="red",command=forget)
l01.grid(row=0,columnspan=4)
l02.grid(row=1)
l03.grid(row=2)
e01.grid(row=1,column=1)    
e02.grid(row=2,column=1)
b01.grid(row=3)
b02.grid(row=3,column=1)
b03.grid(row=4,column=1)          
root.mainloop()        
