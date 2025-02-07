#string = "the sky is blue"
#reversed = "blue is sky the"
def reversal(string):
    a=string.split()
    b=a[::-1]
    c=" ".join(b)
    return c
print(reversal("the sky is blue"))
