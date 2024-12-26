f = open("hello.txt")

data = f.read()


f = open("hello_copy.txt","w")

f.write(data)
