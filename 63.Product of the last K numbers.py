import math
class Productoflastknumbers:
    a=[]
    def addition(self,num):
        self.a.append(num)
    def multi(self,k):
        if k>len(self.a):
            return "not enough elements"
        return math.prod(self.a[len(self.a)-k:len(self.a)])
obj=Productoflastknumbers()
obj.addition(3)
obj.addition(2)
obj.addition(5)
obj.addition(4)

print(obj.multi(3))
print(obj.multi(3))
print(obj.multi(5))