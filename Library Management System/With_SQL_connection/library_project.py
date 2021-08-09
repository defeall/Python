from tkinter import *
import tkinter.messagebox
import time
import mysql.connector
ta=time.asctime()
tc=ta[8:10]
if(ta[4:7]=='Jan'):
    tb=1    
elif(ta[4:7]=='Feb'):
    tb=2
elif(ta[4:7]=='Mar'):
    tb=3
elif(ta[4:7]=='Apr'):
    tb=4    
elif(ta[4:7]=='May'):
    tb=5    
elif(ta[4:7]=='Jun'):
    tb=6    
elif(ta[4:7]=='Jul'):
    tb=7    
elif(ta[4:7]=='Aug'):
    tb=8    
elif(ta[4:7]=='Sep'):
    tb=9    
elif(ta[4:7]=='Oct'):
    tb=10    
elif(ta[4:7]=='Nov'):
    tb=11
elif(ta[4:7]=='Dec'):
    tb=12
root=Tk()       #first window
f1=Frame(root)
f2=Frame(root)
f1.grid(row=0)
f2.grid(row=0)
def dest():                                         #To close at any time of program
    root.destroy()
def update_lib():                                   #To update anything in any section of library this function is called
    b2.destroy()  
    def usn():
        def database():
            db=mysql.connector.connect(host="localhost",user="root",passwd="Nirajkumar28@",database="library")
            cur=db.cursor()
            sq=cur.execute("insert into stdetails(id,name,rollno,year) values(%s,%s,%s,%s)",(int(e13.get()),e11.get(),int(e14.get()),int(e12.get())))
            db.commit()
            db.close()
        b12.destroy()
        b13.destroy()
        b14.destroy() 
        l11=Label(f2,text="Enter Name of student:")
        l12=Label(f2,text="Enter year of student:")
        l13=Label(f2,text="Enter id number: ")
        l14=Label(f2,text="Enter roll number: ")
        l11.grid(row=2)
        l12.grid(row=3)
        l13.grid(row=4)
        l14.grid(row=5)
        e11=Entry(f2)
        e12=Entry(f2)
        e13=Entry(f2)
        e14=Entry(f2)
        e11.grid(row=2,column=1)
        e12.grid(row=3,column=1)
        e13.grid(row=4,column=1)
        e14.grid(row=5,column=1)
        b15=Button(f2,text="Submit",command=database)
        b15.grid(row=6,column=1)
    def rsn():
        def sub():
            if(int(e12.get())==1):
                name1_list.remove(e11.get())
                id1_list.remove(e13.get())
                l14=Label(f2,text="Student removed succesfully")
                l14.grid(row=6)
            elif(int(e12.get())==2):
                name2_list.remove(e11.get())
                id2_list.remove(e13.get())
                l14=Label(f2,text="Student removed succesfully")
                l14.grid(row=6)
            elif(int(e12.get())==3):
                name3_list.remove(e11.get())
                id3_list.remove(e13.get())
                l14=Label(f2,text="Student removed succesfully")
                l14.grid(row=6)
            elif(int(e12.get())==4):
                name4_list.remove(e11.get())
                id4_list.remove(e13.get())
                l14=Label(f2,text="Student removed succesfully")
                l14.grid(row=6)
            else:
                l14=Label(f2,text="Invalid entry in year")
                l14.grid(row=6)
        b12.destroy()
        b13.destroy()
        b14.destroy() 
        l11=Label(f2,text="Enter Name of student:")
        l12=Label(f2,text="Enter year of student:")
        l13=Label(f2,text="Enter id number: ")
        l11.grid(row=2)
        l12.grid(row=3)
        l13.grid(row=4)
        e11=Entry(f2)
        e12=Entry(f2)
        e13=Entry(f2)
        e11.grid(row=2,column=1)
        e12.grid(row=3,column=1)
        e13.grid(row=4,column=1)
        b15=Button(f2,text="Submit",command=sub)
        b15.grid(row=5,column=1)
        
    b11=Button(f2,text="Add Student\nname",bg="light blue",font=('elephant',10,'bold'),width=12,command=usn)
    b12=Button(f2,text="Remove Student\nname",bg="light blue",font=('elephant',10,'bold'),width=12,command=rsn)
    b13=Button(f2,text="Add\n book",bg="light blue",font=('elephant',10,'bold'),width=12)
    b14=Button(f2,text="Remove\n book",bg="light blue",font=('elephant',10,'bold'),width=12)
    b11.grid(row=1)
    b12.grid(row=1,column=1)
    b13.grid(row=1,column=2)
    b14.grid(row=1,column=3)

def stu_login():
    def book_issue():
        def issued():
            global tb,tc
            l210=Label(f2,text="Book Issued!!!")
            l210.grid(row=5,column=1)
            l212=Label(f2,text="Kindly sumbit this book by:")
            l212.grid(row=6)
            if((int(tc)+15)>30):
                l213=Label(f2,text=(int(tc)+15)-30)
                l214=Label(f2,text="of next coming month")
                l213.grid(row=6,column=1)
                l214.grid(row=6,column=2)
            else:
                l213=Label(f2,text=int(tc)+15)
                l214=Label(f2,text="of this month")
                l213.grid(row=6,column=1)
                l214.grid(row=6,column=2)
        b21.grid(row=0,column=1)
        b22.destroy()
        b23.destroy()
        l211=Label(f2,text="Enter book name:")
        e211=Entry(f2)
        b211=Button(f2,text="Issue",command=issued)
        l211.grid(row=4)
        e211.grid(row=4,column=1)
        b211.grid(row=5)
    def book_reissue():
        def reissued():
            global tb,tc
            l220=Label(f2,text="Book Reissued!!!")
            l220.grid(row=5,column=1)    
            l222=Label(f2,text="Kindly sumbit this book by:")
            l222.grid(row=6)
            if((int(tc)+15)>30):
                l223=Label(f2,text=(int(tc)+15)-30)
                l224=Label(f2,text="of next coming month")
                l223.grid(row=6,column=1)
                l224.grid(row=6,column=2)
            else:
                l223=Label(f2,text=int(tc)+15)
                l224=Label(f2,text="of this month")
                l223.grid(row=6,column=1)
                l224.grid(row=6,column=2)
        b22.grid(row=0,column=1)
        b21.destroy()
        b23.destroy()
        l221=Label(f2,text="Enter book name:")
        e221=Entry(f2)
        b221=Button(f2,text="ReIssue",command=reissued)
        l221.grid(row=4)
        e221.grid(row=4,column=1)
        b221.grid(row=5)
    def book_return():
        def returned():
            global tb,tc
            if(tb==int(e233.get())):
                td=int(tc)-int(e232.get())
                if(td>15):
                    te=td*3
                    l234=Label(f2,text="You have to pay a fine of Rs:")
                    l235=Label(f2,text=te)
                    l234.grid(row=8)
                    l235.grid(row=8,column=1)
                else:
                    l234=Label(f2,text="Book returned successfully")
                    l234.grid(row=8)
            else:
                td=(30-int(e232.get()))+int(tc)
                if(td>15):
                    te=(td-15)*3
                    l234=Label(f2,text="You have to pay a fine of Rs:")
                    l235=Label(f2,text=te)
                    l234.grid(row=8)
                    l235.grid(row=8,column=1)
                else:
                    l234=Label(f2,text="Book returned successfully")
                    l234.grid(row=8)
        b23.grid(row=0,column=1)
        b21.destroy()
        b22.destroy()
        l231=Label(f2,text="Enter book name:")
        l232=Label(f2,text="Enter date on which book issued:")
        l233=Label(f2,text="Enter month in which book issued:")
        e231=Entry(f2)
        e232=Entry(f2)
        e233=Entry(f2)
        b231=Button(f2,text="Return",command=returned)
        l231.grid(row=4)
        l232.grid(row=5)
        l233.grid(row=6)
        e231.grid(row=4,column=1)
        e232.grid(row=5,column=1)
        e233.grid(row=6,column=1)
        b231.grid(row=7)
    global name_list,id_list,roll_list,year_list
    b1.destroy()
    b2.grid(row=0,column=0)
    b3.grid(row=0,column=3)
    adn=simpledialog.askinteger("ID number","What is your ID number")
    if(adn in id_list):
        a=id_list.index(adn)
        l21=Label(f2,text="Name:")
        l22=Label(f2,text="Roll number:")
        l23=Label(f2,text="Year:")
        l24=Label(f2,text=name_list[a])
        l25=Label(f2,text=roll_list[a])
        l26=Label(f2,text=year_list[a])
        b21=Button(f2,text="Issue\nBook",bg="light green",font=('elephant',10,'bold'),width=12,command=book_issue)
        b22=Button(f2,text="Reissue\nBook",bg="light green",font=('elephant',10,'bold'),width=12,command=book_reissue)
        b23=Button(f2,text="Return\nBook",bg="light green",font=('elephant',10,'bold'),width=12,command=book_return)
        l21.grid(row=1,column=1)
        l22.grid(row=2,column=1)
        l23.grid(row=3,column=1)
        l24.grid(row=1,column=2)
        l25.grid(row=2,column=2)
        l26.grid(row=3,column=2)
        b21.grid(row=5,column=0)
        b22.grid(row=5,column=1)
        b23.grid(row=5,column=2)
    else:
        l10=Label(f2,text="Invalid ID number\nTry again ",fg="red",font="elephant")
        l10.grid(row=2)
c=Canvas(f1,width=840,height=560,bg="black")    #Creating  a canvas
c.grid()
p=PhotoImage(file="31.png")                     #Giving background an image
i=c.create_image(0,0,anchor=NW,image=p)
name_list=["Niraj","Siwani","Shreya","Rohit","Mohit","Emran","Shweta","Neha","Pradeep","Shilpa","Rahul","Niharika","Naveen","Sikha","Mahima","Subham"] #name of students in each year
id_list=[11101,11102,11103,11104,11105,11106,11107,11108,11109,11110,11111,11112,11113,11114,11115,11116]   #id numbers of those students
roll_list=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']
year_list=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
b1=Button(f2,text="Update Library",bg="light green",font=('Algerian',10,'bold'),width=15,command=update_lib)        #Button on Front page
b2=Button(f2,text="Student Login",bg="light green",font=('Algerian',10,'bold'),width=15,command=stu_login)
b3=Button(f2,text="EXIT",bg="Red",font=('Algerian',10,'bold'),width=15,command=dest)
b1.grid(row=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
root.mainloop()
