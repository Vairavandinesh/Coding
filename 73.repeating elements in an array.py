arr=[2,3,1,2,3]
dicty={}
for i in arr:
    if i not in dicty:
        dicty[i]=1
    else:
        dicty[i]+=1
new=[]
for k,v in dicty.items():
    if v>1:
        new.append(k)
print(new)