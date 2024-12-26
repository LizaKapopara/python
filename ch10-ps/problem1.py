class Programmer:
    company = "microsoft"
    
    def __init__(self,name,pin,phone):
        self.name = name
        self.pin = pin
        self.phone = phone
    

        


liza = Programmer("liza", 395006, 8713423372)
print(liza.name,liza.pin,liza.phone)
kriti = Programmer("kriti", 395006, 8713423372)
print(kriti.name,kriti.phone,kriti.pin)