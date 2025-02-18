def stringer(i,s):
    if i==len(s):
        return ""
    stringer(i+1,s)
    print(s[i],end="")
stringer(0,"Hello")