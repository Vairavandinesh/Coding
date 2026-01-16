#Write a Python program to create a class called "Movie" with attributes for title, director, actors, and 
# reviews, and methods for adding and retrieving reviews.
#lets write how the database looks like
#we have to create inheritance
#i feel overwhelmed , just start small

class Movies:
    def __init__(self,title,director,actors):
        self.title=title
        self.director=director
        self.actors=actors
class MovieWithReviews(Movies):
    database={}
    def __init__(self,title,director,actors):
        super().__init__(title,director,actors)
        self.reviews=[]
    def add_review(self,review):
        self.reviews.append(review)
        MovieWithReviews.database[self.title]={
            "director":self.director,
            "actors":self.actors,
            "reviews":self.reviews
        }
obj1=MovieWithReviews("Avatar","James Cameron","Sam")
obj1.add_review("Amazing Movie")
obj2=MovieWithReviews("Goodfellas","Martin scorsese","Ray liotta")
obj1.add_review("Best mafia movie from 90s")
print(MovieWithReviews.database)