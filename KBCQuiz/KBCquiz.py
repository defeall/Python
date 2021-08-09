for i in range(1,2):
    print("\t\t\tWELCOME TO TANGO CHARLIE")
    a=str(input("Enter Your Name: "))
    print(a,"You have 100 points to save!!!!\n\nEach wrong answer will deduct 10 points from your account\n")
    b=100
    a1=int(input("\nQ1.What is national Capital of India?\n1.New Delhi\t 2.Mumbai\n"))
    if(a1==1):
        print("It's a right answer.....You have saved your point",b)
    elif(a1==2):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a2=int(input("\nQ2.What is national Capital of Haryana?\n1.Chandigarh\t 2.Hisar\n"))
    if(a2==1):
        print("It's a right answer.....You have saved your point",b)
    elif(a2==2):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a3=int(input("\nQ3.Who is our current Prime Minister?\n1.Manmohan Singh\t 2.Narendara Modi\n"))
    if(a3==2):
        print("It's a right answer.....You have saved your point",b)
    elif(a3==1):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a4=int(input("\nQ4.How much world cup India won in cricket?\n1.3\t 2.2\n"))
    if(a4==2):
        print("It's a right answer.....You have saved your point",b)
    elif(a4==1):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a5=int(input("\nQ5.Who is President of USA?\n1.George Bush\t 2.Donald Trump\n"))
    if(a5==2):
        print("It's a right answer.....You have saved your point",b)
    elif(a5==1):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a6=int(input("\nQ6.What is national sports of India?\n1.Hockey\t 2.Cricket\n"))
    if(a6==1):
        print("It's a right answer.....You have saved your point",b)
    elif(a6==2):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a7=int(input("\nQ7.Who is the first President of India?\n1.Pandit Jawahar Lal Nehru\t 2.Dr. Rajendra Prasad\n"))
    if(a7==2):
        print("It's a right answer.....You have saved your point",b)
    elif(a8==1):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a8=int(input("\nQ8.What is national Bird of India?\n1.Peacock\t 2.Sparrow\n"))
    if(a8==1):
        print("It's a right answer.....You have saved your point",b)
    elif(a8==2):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a9=int(input("\nQ9.Who is the father of nation?\n1.Mahatma Gandhi \t 2.Premchand\n"))
    if(a9==1):
        print("It's a right answer.....You have saved your point",b)
    elif(a9==2):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    a10=int(input("\nQ10.When did India won it's first world cup in cricket?\n1.2011\t 2.1983\n"))
    if(a10==2):
        print("It's a right answer.....You have saved your point",b)
    elif(a10==1):
        b=b-10
        print("Ohh!! You lost your 10 points and current amount of point in your account is",b)
    else:
        break
    print("\n",a,"Thank you for playing with us\n\n You have won points",b)     
print("INVALID INPUT.......You are out of game and won nothing")    
