class employee:
    language = str(input())
    salary = 1200000


liza = employee()
liza.name = "liza"
print(liza.salary, liza.name, liza.language)

kriti = employee()
kriti.language = "python"
print(kriti.language)

# here language and salary are class attributes as they directly belongs to the class and name and language are object attribute

# c
# 1200000 liza c
# python
