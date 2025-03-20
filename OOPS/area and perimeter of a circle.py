class Mensuration:
    def __init__(self):
        radius=None
    def Area(self,radius):
        return radius**2
    def Perimeter(self,radius):
        return 2*3.14*radius
uia=Mensuration()
print(uia.Area(2))
print(uia.Perimeter(2))