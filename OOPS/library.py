#Write a Python program to create a class called "Library" with a collection of books 
# and methods to add and remove books.
#lets create a library class
#we have to create a dictionary with book title and author
class Library:
    dicty={}
    def __init__(self,title,author,genre):
        self.title=title
        self.author=author
        self.genre=genre
        
    def addbooks(self):
        Library.dicty[self.title]=[self.author,self.genre]
        return Library.dicty
    def removebooks(self):
        if self.title in Library.dicty:
            del Library.dicty[self.title]
        return Library.dicty
    @classmethod
    def printer(cls):
        print(cls.dicty)
obj1=Library("Harry Potter","J K Rowling","Fantasy")
obj1.addbooks()
obj2=Library("Lord Of The Rings","John Tolkien","Fantasy")
obj2.addbooks()
Library.printer()