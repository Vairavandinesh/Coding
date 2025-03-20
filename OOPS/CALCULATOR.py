class OOPSCALCI:
    def __init__(self):
        n1=None
        n2=None
    def add(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        if n1>n2:
            return n1-n2
        else:
            return n2-n1
    def mul(self,n1,n2):
        return n1*n2
    def divi(self,n1,n2):
        if n1>n2:
            return n1//n2
        else:
            return n2//n1
    def modulo(self,n1,n2):
        if n1>n2:
            return n1%n2
        else:
            return n2%n1
uia=OOPSCALCI()
print(uia.add(1,2))
print(uia.sub(1,2))
print(uia.mul(1,2))
print(uia.divi(1,2))
print(uia.modulo(1,2))