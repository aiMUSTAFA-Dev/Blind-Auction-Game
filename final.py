# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print("Welcome To The Secret Auction Program")
from art import logo
print(logo)

my_dict = {}
end_auction = False
while not end_auction:
    name = input("Enter What is Your name? : ")
    bid = int(input("Enter What is You bid? : "))

    my_dict[name] = bid

    ask = input("Are there any other bidders? Type 'Yes' or 'No' ").lower()
    if ask == "no":
        end_auction = True

    if ask == "yes":
        print("\n"*100)

print(my_dict)

highest_bid = 0
winner = ""
for bidder in my_dict:
    if highest_bid < my_dict[bidder]:
        highest_bid = my_dict[bidder]
        winner = bidder

print(f"The winner is {winner} with bid of {highest_bid}")



# ...........................or..............................



print("Welcome To The Secret Auction Program")
from art import logo
print(logo)

my_dict = {}
end_auction = False
while not end_auction:
    name = input("Enter What is Your name? : ")
    bid = int(input("Enter What is You bid? : "))

    my_dict[name] = bid

    ask = input("Are there any other bidders? Type 'Yes' or 'No' ").lower()
    if ask == "no":
        end_auction = True

    if ask == "yes":
        print("\n"*100)

print(my_dict)

highest_bid = max(my_dict.values())
winner = ""
for k in my_dict:
    if my_dict[k] == highest_bid:
        winner = k
print(f"The winner is {winner} with bid of {highest_bid}")


# # same step for highest
# mylist = []
# for k in my_dict:
#     mylist.append(my_dict[k])
# highest_bid = max(mylist)