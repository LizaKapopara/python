list = ['a','e','i','o','u']

string = str(input("enter any string:"))
s = 0

for i in string:
    if i in list:
        s +=1
print(s)