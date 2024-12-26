student = {}
n = int(input("enter the number of students:"))
for i in range(1, n+1):
    a = input("name: ")
    b = input("language: ")
    student[a] = b   
    for a,b in student.items():
        dict1 = print(f"{a}: {b}",end = " ")

# set can not contain list in it
