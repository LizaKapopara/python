f = open("donkey.txt", "r")

data  = f.read()

a =  data.replace("donkey", "monkey")
    

b = open("donkey.txt","w")

b.write(a)

f.close()    