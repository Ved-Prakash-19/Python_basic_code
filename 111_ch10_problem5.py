from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"the ticket is booked in trainno: {self.trainNo} from {fro} to {to}")
        
    def getstatus(self):
        print(f"the status of trainno: {self.trainNo} is running on time")
        
    def getfare(self, fro, to):
        print(f"the fare of trainno: {self.trainNo} from {fro} to {to} is {randint(180, 222)}")
        
t = train(12023)
t.book("jamui", "howrah")
t.getstatus()
t.getfare("jamui", "howrah")