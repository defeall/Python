class Pizza():

    
    def __init__(self,pizza_id,pizza_size,pizza_price,pizza_base,pizza_topping):
        self.Pizza_Id=pizza_id
        self.Pizza_Size=pizza_size
        self.Pizza_Price=pizza_price
        self.Pizza_Base=pizza_base
        self.Pizza_Topping=pizza_topping



    
    def getPizzaId(self):
        return self.Pizza_Id
    def getPizzaSize(self):
        return self.Pizza_Size
    def getPizzaPrice(self):
        return self.Pizza_Price
    def getPizzaBase(self):
        return self.Pizza_Base
    def getPizzaTopping(self):
        return self.Pizza_Topping


class Topping():

    
    def __init__(self,topping_id,topping_name,topping_price):
        self.ToppingId=topping_id
        self.ToppingName=topping_name
        self.ToppingPrice=topping_price

    def getToppingId(self):
        return self.ToppingId
    def getToppingName(self):
        return self.ToppingName
    def getToppingPrice(self):
        return self.ToppingPrice

class PizzaOrder():

    def __init__(self):
        pass

    def choosepizza(self,allpizza):
        selected_pizzalist=[]
        while True:
            pizzaid=input("\nEnter pizza id: ")
            if(int(pizzaid)):
                for item in allpizza:
                    if(int(pizzaid)==int(item.getPizzaId())):
                        print("{0} size pizza with {1} base and {2} topping: {3}".format(item.getPizzaSize(),item.getPizzaBase(),item.getPizzaTopping(),item.getPizzaPrice()))
                        selected_pizzalist.append(item)
                        return selected_pizzalist
                         
                print("This id has no pizza.")
                continue
            else:
                raise ValueError("Pizza id should be number")
                

    def choosetoppings(self,alltoppings):
        selected_toppings=[]
        while True:
            topping_id=input("\nEnter topping id: ")
            if(int(topping_id)):
                for item in alltoppings:
                    if(int(topping_id)==int(item.getToppingId())):
                        print(" {0} topping: {1}".format(item.getToppingName(),item.getToppingPrice()))
                        selected_toppings.append(item)
                        return selected_toppings

                print("This id has no topping.")
                continue
            else:
                raise ValueError("Topping Id should be number.")
      
