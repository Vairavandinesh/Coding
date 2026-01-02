#Write a Python program to create a class called "Inventory" with a collection of 
# products and methods to add and remove products, and to check for low inventory. 
#a dictionary datastructure is used to store the products and quantity
class Inventory:
    dicty={}
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
        Inventory.dicty[self.name]=self.quantity
    def adder(self,name,quantity):
        Inventory.dicty[name]=quantity
    def remover(self,name):
        Inventory.dicty.pop(name,None)
    def printer(self):
        print(Inventory.dicty)
    def check_threshold(self,threshold):
        for item,quantity in Inventory.dicty.items():
            if quantity<threshold:
                print(item," is low in stock")
# I think ive accomplish all the requirements, now create an object
obj1=Inventory("Books",5)
obj1.printer()
obj1.adder("pen",2)
obj1.printer()