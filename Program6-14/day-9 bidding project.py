from art import logo_bid

print(logo_bid)

bids = {}
bidding_finished = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        # print(bidder)  key as a bidder name
        bid_amount = bidding_record[bidder]
        # print(f"bid amount { bid_amount}") getting the value of the current bidder
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = False
        find_highest_bidder(bids)
        print(bids)

