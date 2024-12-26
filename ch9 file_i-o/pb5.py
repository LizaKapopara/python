f = open("hello.txt")

data = f.read()

if('harsh' in data):
    print("yes the harsh is present in the data ")
    
else:
    f = open("hello.txt","w")
    
    data2 = f.write("harsh")
    
    