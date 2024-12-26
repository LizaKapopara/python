from random import randint

class train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"train no: {self.trainNo} is running on time")
    
    def getfare(self, fro, to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")        

a = train(4516531)
a.book("rampur", "delhi")
a.getfare("rampur", "delhi")
a.getstatus()

 