def romtointeger(roman):
    rom={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer=0
    i=0
    while i<len(roman):
        if i+1<len(roman) and rom[roman[i]]<rom[roman[i+1]]:
            integer+=rom[roman[i+1]]-rom[roman[i]]
            i+=2
        else:
            integer+=rom[roman[i]]
            i+=1
    return integer
print(romtointeger("IV"))