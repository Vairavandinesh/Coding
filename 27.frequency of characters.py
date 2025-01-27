def frequency(string):
    #storing the frequency in a python dictionary
    #in python dictionary,the key is the character and value is its number of occurrences
    
    dict={}
    for i in string:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    return dict
print(frequency("banana"))