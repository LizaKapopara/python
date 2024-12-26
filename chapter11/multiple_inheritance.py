class employee:
    company = "CTC"
    name = "lzia"
    salary = 120000
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

class coder:
    language = "c"
    def printlanguage(self):
        print(f"out of all language here is your language: {self.language}")

class programmer(employee, coder):
    company = "CTC infotech"
    def showlanguage(self):
        print(f"the company name is {self.company}")

a = employee()
b = programmer()

print(a.company,b.company)

b.show()
b.printlanguage()
b.showlanguage()