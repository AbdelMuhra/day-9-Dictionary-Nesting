from replit import clear
from art import logo

#creating a dictionary to store the bid amount and name
bids = {}

live_auction = True

def highest_bidder(bids_record):
  highest_bid = 0
  winner = ""
  for bidder in bids_record:
    bid_amount = bids_record[bidder]
    if bid_amount > highest_bid:
      bid_amount = highest_bid
      winner = bidder
  print(f"The highest bidder is {winner} with {highest_bid}")

while live_auction:
  #display logo
  print(logo)
  name = input("What is your name?: ")
  bid_amount = int(input("What is your bid: $"))
  bids[name] = bid_amount
  question = input("Any other Bidder? (Y|N)?")
  clear()
  if question == "N":
    highest_bidder(bids)
    live_auction = False



