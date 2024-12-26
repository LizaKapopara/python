class employee:
    language = "python"
    salary = 1200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("liza here")
        
    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary} ")
    
    @staticmethod
    def greet():
        print("good morning")


liza = employee("liza", 1300000, "python")
print(liza.language,liza.salary)

kriti = employee("kriti", 12000, "c")
print(kriti.language,kriti.salary)
