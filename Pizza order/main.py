
import pizza


class Main():
    
    def __init__(self):
        pizza1=pizza.Pizza('1','Small',5,'Tomato','Cheese')
        pizza2=pizza.Pizza('2','Medium',8,'Tomato','Cheese')
        pizza3=pizza.Pizza('3','Large',12,'Tomato','Cheese')
        self.allpizza=[pizza1,pizza2,pizza3]

    def extratoppings(self):
        topping1=pizza.Topping('11',"Bacon",1)
        topping2=pizza.Topping('12',"Olives",1)
        topping3=pizza.Topping('13',"Ham",1)
        topping4=pizza.Topping('14',"Muchroom",1)
        topping5=pizza.Topping('15',"Pineapple",1)
        topping6=pizza.Topping('16',"Salami",1)
        topping7=pizza.Topping('17',"Anchovies",1)
        self.alltoppings=[topping1,topping2,topping3,topping4,topping5,topping6,topping7]

    def selectpizza(self,allpizza):
        selectedPizzaList=[]
        try:
            while True:
                pizzaj=pizza.PizzaOrder()
                pizzalist=pizzaj.choosepizza(allpizza)
                selectedPizzaList.append(pizzalist)
                #extartopping()
                morePizzaOption=input("\nDo you want to add more pizza to this order? (Y/N)")
                if(morePizzaOption.upper()=="Y"):
                    continue
                elif(morePizzaOption.upper()=="N"):
                    return selectedPizzaList
                else:
                    print("You have entered wrong option.")
        except ValueError as err:
            print("Pizza Id should be Number.")


    def extartopping(self,alltoppings):
        selectedtopinglist=[]
        try:
            while True:
                pizzaj=pizza.PizzaOrder()
                toppinglist=pizzaj.choosetoppings(alltoppings);
                selectedtopinglist.append(toppinglist)
                moreToppings=input("\nDo you want to add more pizza to this order? (Y/N)")
                if(moreToppings.upper()=="Y"):
                    continue
                elif(moreToppings.upper()=="N"):
                    return selectedtopinglist
        except ValueError as err:
            print("Topping id should be number.")


    def calculatetotalprice(self,pizzalist,toppinglist):
        totalvalue=0
        for item in pizzalist:
            for items in item:
                totalvalue += items.getPizzaPrice()
        if(toppinglist):
            for item in toppinglist:
                for items in item:
                    totalvalue += items.getToppingPrice()
        return totalvalue;
            

    def collect(self):
        contact_detail=[]
        name=input("Your Name: ")
        contact_detail.append(name)
        phone_no=input("Your Phone No: ")
        contact_detail.append(phone_no)
        return contact_detail

    def deliver(self):
        contact_detail=[]
        name=input("Your Name: ")
        contact_detail.append(name)
        phone_no=input("Your Phone No: ")
        contact_detail.append(phone_no)
        address=input("Your Address: ")
        contact_detail.append(address)
        return contact_detail


pizzashop=Main()
print("\nWelcome to Pizza Shop")
print("please enter 1 for Small pizza")
print("please enter 2 for Medium pizza")
print("please enter 3 for Large pizza")
allpizzas=pizzashop.allpizza

while True:
    orderpizaalist=pizzashop.selectpizza(allpizzas)
    if(orderpizaalist):
        break
    else:
        continue
extra_topping_decision=input("\nDo you want extra toppings for your pizza? (Y/N)")
if(extra_topping_decision=="Y" or extra_topping_decision=="y"):
    print("please select 11 for bacon, 12 for  Olives, 13 for ham, 14 for mushroom, 15 for pineapple, 16 for pineapple, 17 for anchovies")
       
    pizzashop.extratoppings()
    alltopping=pizzashop.alltoppings
    selectedtoppings=pizzashop.extartopping(alltopping)
else:
    selectedtoppings=[]
#print(orderpizaalist)
#print(selectedtoppings)
totalpriceofpizza=pizzashop.calculatetotalprice(orderpizaalist,selectedtoppings)
print("Total price of pizza: ", totalpriceofpizza)
collectordeliver=input("\nYou want to collect it from store. (Y/N) ")
if(collectordeliver=="Y" or collectordeliver=="y"):
    contactdetails=pizzashop.collect()
else:
    contactdetails=pizzashop.deliver()
length=len(contactdetails)
if(length==2):
    print("Name:     ",contactdetails[0])
    print("Phone No: ",contactdetails[1])
else:
    print("Name:     ",contactdetails[0])
    print("Phone No: ",contactdetails[1])
    print("Address:  ",contactdetails[2])
