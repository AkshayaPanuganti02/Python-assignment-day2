# Assignment: Take a string input and print the number of occurrences of each character.
x="pythonprogrammer"
res = {}   
for keys in x: 
    res[keys] = res.get(keys, 0) + 1
print (str(res))