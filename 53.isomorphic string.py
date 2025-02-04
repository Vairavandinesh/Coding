#isomorphic string - replacing the letters wont affect the alignment of the string
# example: in "egg" if we swap e to a and g to d its an isomorphic string
s="foo"
t="bar"
#creating 2 dictionaries to map the isomorphic strings
st={}
ts={}
#iterate both strings and map the elements in s to its adjacent element in t and map elements in t to its adjacent elements in s
for i,j in zip(s,t):
    #check for mismatching
    if ((i in st and st[i]!=j) or (j in ts and ts[j]!=i)):
        print(False)
    break
    st[i]=j
    ts[j]=i
print(True)   
    