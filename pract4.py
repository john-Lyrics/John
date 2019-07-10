def boolean(mystring):
    for letter in mystring:
        if letter == "a":
            return True
    return False
        
    
hasa = boolean("chi")
print(hasa)

print(boolean("johnny"))
print(boolean("francis"))

name=input ("Enter a word")
y= boolean(name)
print(y)
