import random,string
from datetime import datetime

class HotelReservation:
  def __init__(self):
    self.responses={
        "greeting":{
            "hi":"Hey",
            "hello":"Hello",
            "is anyone there?":"Hi there, how can i help you?"
        },
        "goodbye":{
            "bye":"See you later, thanks for visiting",
            "goodbye":"Bye! come back again soon"
        },
        "booking":{
            "i would like to make a reservation":"Sure lets begin with reservation",
            "can i book a room":"Lovely. Lets begin with reservation"
        },
        "cancelation":{
            "i would like to cancel my booking":"Sure, what is your reference number?",
            "can i cancel a room?":"I only need to know the reference number of your booking"
        },
        "payments":{
            "when do i have to pay?":"The payment is on arrival. We accept cash & card",
            "can i pay by card?":"Sure, we accept cash and card",
            "when is the payment?":"You can pay on arrival by cash or card"
        }
    }
    self.hotel={
        "rooms":{
            "single":900,
            "double":1500,
            "triple":2900
        },
        "suites":{
            "standard":4000,
            "junior":6000,
            "presidential":9000,
            "penthouse":30000
        }
    }
    self.reservation={}

  def display_rooms(self):
    print("Welcome to Hotel reservation chatbot! here is our room types")
    for category,rooms in self.hotel.items():
      print(f"{category}:")
      for room,price in rooms.items():
        print(f"-{room}:{price}e£")
      print()

  def reference_number(self):
    character_numbers=string.ascii_letters+string.digits
    random_characters_numbers=''.join(random.choice(character_numbers) for _ in range(8))
    return random_characters_numbers

  def reserve_room(self):
    while True:
      user=input("Bot: How can i help you?\n  (type bye or goodbye to exit)\nYou:")
      user=user.lower()
      if user=="bye" or user=="goodbye":
        print("Bot: ",self.responses["goodbye"].get(user))
        break
      else:
        if user in self.responses["greeting"]:
          print("Bot:",self.responses["greeting"].get(user))
        elif user in self.responses["booking"]:
          print("Bot: ",self.responses["booking"].get(user))
        elif user in self.responses["cancelation"]:
          print("Bot: ",self.responses["cancelation"].get(user))
        elif user in self.responses["payments"]:
          print("Bot: ",self.responses["payments"].get(user))
        elif user in self.hotel["rooms"] or user in self.hotel["suites"]:
          check_in=input("Bot: when will you check in?\nYou:")
          check_out=input("Bot: when will you check out?\nYou:")
          quantity=int(input("Bot: how many rooms do you need?\nYou:"))
          check_in=datetime.strptime(check_in,"%d-%m-%Y")
          check_out=datetime.strptime(check_out,"%d-%m-%Y")
          days=check_out-check_in
          reference=self.reference_number()
          res={
                  "room":user,
                  "check-in":check_in.strftime("%d-%m-%Y"),
                  "check-out":check_out.strftime("%d-%m-%Y"),
                  "quantity":quantity,
                  "no of days":days.days
          }
          self.reservation[reference]=res
        else:
          print("Bot: Sorry i didn't get it")

  def calculate_total(self):
    total=0
    for reference, data in self.reservation.items():
      total+=self.hotel["rooms"].get(data["room"],0)*data["quantity"]*data["no of days"]
      total+=self.hotel["suites"].get(data["room"],0)*data["quantity"]*data["no of days"]

      print("Bot: Reciept for reference number:",reference)
      print(" type of room:",data["room"])
      print(" check-in:",data["check-in"])
      print(" check-out:",data["check-out"])
      print(" quantity:",data["quantity"])
      print(" number of days:",data["no of days"])
      print(" total reciept:",total)

  def serve_customer(self):
    self.display_rooms()
    self.reserve_room()
    self.calculate_total()





hotel=HotelReservation()
hotel.serve_customer()

