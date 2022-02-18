from replit import clear
from art import logo

#creating a dictionary to store the bid amount and name
bid = {
  "Name": "abdel",
  "Bid amount": 0,
}

def auction():
  highest_bidder = 0
  highest_bidder_name = ""
  #get username
  live_auction = True
  
  while live_auction:
    #display logo
    print(logo)
    name = input("What is your name?")
    #get user's bid
    bid_amount = int(input("What is your bid?"))
    question = input("Any other Bidder? (Y|N)?")
    if question == "N":
      live_auction = False
      print(f"The highest bidder is {highest_bidder_name} with {highest_bidder}")
    
    #to clear console after user has inputed their details
    clear()
  for buyer in bid:
    bid["Name"] = name
    bid["Bid amount"] = bid_amount
    if highest_bidder > bid["Bid amount"]:
      highest_bidder = bid["Bid amount"]
      highest_bidder_name = bid["Name"]

    
    
auction()
print(bid)

