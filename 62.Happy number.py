def happynumber(n):
    def digit_extracter(k):
        x=0
        while k!=0:
            x+=(k%10)**2
            k//=10
        return x
    settt=set()
    while True:
        temp=digit_extracter(n)
        if temp==1:
            return True
        elif temp in settt:
            return False
        settt.add(temp)
        n=temp
print(happynumber(2))
        