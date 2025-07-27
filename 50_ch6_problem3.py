p1 = "make a lot of money"
p2 = "buy now"
p3 = "limited time offer"
p4 = "subscribe this channel"
p5 = "click this"

message = input("enter your comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message)):
    print("this is a spam comment: ")
    
else:
    print("this is not a spam comment: ")