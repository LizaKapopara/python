f = open("hello.txt")

r = f.read()
 
if("harsh" in r):
    print("yes the owner name in the file")
    
else:
    print("no the owner nameis not in the list ")
    
    f.close()




