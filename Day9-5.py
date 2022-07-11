from replit import clear
# HIN: You can call clear() to clear the output in the console.abs

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Mitra": 123, "Ali": 234}
    for bidder in bidding_record:
        bit_amount = bidding_record[bidder]
        if bit_amount > highest_bid:
            highest_bid = bit_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid} ")


while not bidding_finished:
    name = input("what's your name?: ")
    price = int(input("What's your bid?:  $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

