import random

# # 1. A D&D Ability Check

# DC = int(input("Enter DC value"))
# roll = random.randint(1,21)

# if roll >= DC:
#     print("Failed")
# else:
#     print("Succeeded")



# # 2. Tournament Selection (CCC 2016 - J1)

# win_counter = 0
# for i in range(1,7): 
#     result = input(f"Enter the result for game {i}: ")

#     if result == "W":
#         win_counter += 1 

# group = 0 

# match result:
#     case result if win_counter > 4:
#         group = 1
#     case result if win_counter > 2:
#         group = 2
#     case result if win_counter > 0:
#         group = 3


# if group == 0:
#     print("Eliminated")
# else:
#     print(f"Group {group}")

# 3. Rock Paper Scissors

choices = {'rock' : 0, 'paper': 1, 'scissors' : 2}


while True:
    player_choice = input("Enter a choice of rock, paper, or scissors: ")

    if player_choice in choices.keys():
        player_choice = choices[player_choice]
        break

computer_choice = random.randint(0,2)
print(f"The computer chose {computer_choice}.")
print(f"{list(choices.keys())[computer_choice]}")

if player_choice == computer_choice:
    print("Tie")
else:
    result = player_choice - computer_choice
    if result == -2 or result == 1:
        print("You won")
    else:
        print("You lost")
