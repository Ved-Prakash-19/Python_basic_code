from random import randint

class train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
    def book(ved, fro, to):
        print(f"the ticket is booked in trainno: {ved.trainNo} from {fro} to {to}")
        
    def getstatus(ved):
        print(f"the status of trainno: {ved.trainNo} is running on time")
        
    def getfare(ved, fro, to):
        print(f"the fare of trainno: {ved.trainNo} from {fro} to {to} is {randint(180, 222)}")
        
t = train(12023)
t.book("jamui", "howrah")
t.getstatus()
t.getfare("jamui", "howrah")


# not any changes in output if i change self parameter to something else. but readability of program is very poor.