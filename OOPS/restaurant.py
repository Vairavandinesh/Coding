#Write a Python program to create a class called "Restaurant" with attributes for 
# menu items, prices, and ratings, and methods to add and remove items, and 
# to calculate average rating.
class Restaurant:
    def __init__(self):
        self.item=None
        self.price=None
        
class food:
    database={}
    def __init__(self,item,price):
        super().__init__(item,price)
        self.ratings=[]
    def add_item(self,rating):
        self.ratings.append(rating)
        food.database[self.title]={
            "item":[self.item],
            "price":[self.price]
        }
    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings)/len(self.ratings)
class Restaurant:
    def __init__(self):
        self.item = None
        self.price = None

class Food(Restaurant):
    database = {}

    def __init__(self, item, price):
        super().__init__()
        self.item = item
        self.price = price
        self.ratings = []

    def add_item(self, rating=None):
        if rating is not None:
            self.ratings.append(rating)
        Food.database[self.item] = {
            "price": self.price,
            "ratings": self.ratings
        }

    # Method to calculate average rating
    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

# ✅ Creating an object for Food
burger = Food("Burger", 150)
burger.add_item(8)
burger.add_item(9)
burger.add_item(7)

# Print database
print(Food.database)

# Print average rating of the object
print("Average rating of Burger:", burger.average_rating())
