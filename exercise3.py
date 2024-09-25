# 1. FizzBuzz

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# 2.  Average Calculator

total_sum = 0
counter = 0

while True:
    user_input = input("Enter the mark (enter EXIT to exit): ")

    if user_input.lower() == "exit":
        break 

    else:
        mark = int(user_input)
        if 0 <= mark <= 100:
            total_sum += mark
            counter += 1
        else:
            print("Invalid input")


print(f"Your average is: {total_sum / counter}.")


# 3. Longest Name Finder


longest_len = 0 
longest_name = ""

while name != 'X':
    # get name as user input
    name = input("Enter your name or 'X' to exit.: ")

    if name == "X":
        break
    else:
        current_len = len(name)

        if current_len > longest_len:
            longest_len = current_len
            longest_name = name

print(longest_name)

