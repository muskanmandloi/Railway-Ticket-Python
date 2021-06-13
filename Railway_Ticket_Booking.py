# Railway Ticket Booking in Python
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare =fare
        self.seats=seats

    def getStatus(self):
        print(".........")
        print(f"The name of train is {self.name}")
        print(f"the seats available in the train are {self.seats}")
        print("..........")
    def fareInfo(self):
        print(f"the price of the tickets is : Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket has been booked!!!!!!!! your seat number is : {self.seats}")
            self.seats =self.seats - 1
        else:
            print("Sorry this train is full !!")
    def cancelTicket(self,seatNo):
        pass

intercity = Train("Intercity Express : 14520", 90,2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()