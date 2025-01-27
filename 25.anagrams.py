def anagrams(a,b):
    if sorted(a)==sorted(b):
        return "anagrams"
    else:
        return "not anagrams"
print(anagrams("hello","ellho"))