class employee:  #encapsulation
    a = 1

    @classmethod
    def show(cls):
        print(f"the class value of a is {cls .a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter  #abstraction
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e.a = 45

e.name = "liza kapoapra"
print(e.lname,e.fname)