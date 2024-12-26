class employee:
    language = "python"
    salary = 1200000

    def getinfo(slf):
        print(f"the language is {slf.language}. the salary is {slf.salary} ")
    @staticmethod
    def greet():
        print("good morning")


liza = employee()
liza.language = "c"
liza.greet()
liza.getinfo()

kriti = employee()
kriti.language = "java"
kriti.greet()
kriti.getinfo()

