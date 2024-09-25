import random

# 1. A D&D Ability Check

DC = int(input("Enter DC value"))
roll = random.randint(1,21)

if roll >= DC:
    print("Failed")
else:
    print("Succeeded")



# # 2. Tournament Selection (CCC 2016 - J1)

win_counter = 0
for i in range(1,7): 
    result = input(f"Enter the result for game {i}: ")

    if result == "W":
        win_counter += 1 

group = 0 

match result:
    case result if win_counter > 4:
        group = 1
    case result if win_counter > 2:
        group = 2
    case result if win_counter > 0:
        group = 3


if group == 0:
    print("Eliminated")
else:
    print(f"Group {group}")

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

# 4. Telemarketer or Not (CCC 2018 - J1)
phone = input()

if phone[-1] in {'8', '9'} and phone[0] in {'8', '9'}:
    if phone[1] == phone[2]:
        print("A telemarketer")
    else:
        print("Not a telemarketer")

# 5. Quadrant Selection (CCC 2017 - J1)

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print("1")
    else:
        print(f"4")
else:
    if y > 0:
        print("2")
    else:
        print("3")

# 6. Triangle Times (CCC 2014 - J1)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

angle_sum = angle1 + angle2 + angle3

if angle_sum != 180:
    print("Error")
else:
    if angle1 == angle2 == angle3:
        print("Equilateral")
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        print("Scalene")
    else:
        print("Isosceles")


# 7. Special Day (CCC 2015 - J1)
month = int(input())
day = int(input())

if month == 2 and day == 18:
    print("Special")
else:
    if month < 2:
        print("Before")
    elif month > 2:
        print("After")
    else:
        # in the month of february
        if day < 18:
            print("Before")
        else:
            print("After")



            