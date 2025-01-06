import random

user_win = 0
computer_win = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer Picked:", computer_pick + ".")
    
    if user_input == computer_pick:
        print("It's a Draw!")
        
    elif user_input == "rock" and computer_pick == "scissor":
        print("You Won!")
        user_win += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_win += 1
    
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_win += 1
        
    else:
        print("You Lost!")
        computer_win += 1
    
print("You Won:", user_win, "times.")
print("Computer Won:", computer_win, "times.")
print("Goodbye!")
