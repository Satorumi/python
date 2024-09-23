import math 

# 1. Introductory Python Program

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
age = 2024 - birth_year


print(f"Hello {first_name} {last_name}")
print(f"You are {age} years old.")

if age >= 19:
    print("You are old enough to drink!")
else:
    print("You are not old enough to drink!")


# 2. Squares (CCC 2004 - J1)
n_tiles = int(input())
max_length = math.floor(math.sqrt(n_tiles))
print(f"Max length: {max_length}")


# 3. Painting Fences
total_cans = 0

for _ in range(3):
    fences = input()
    total_cans += len(fences)

n_dozen = tottotal_cansal_can // 12

if total_cans % 12 != 0:
    n_dozen += 1

print(total_can)
print(n_dozen*12 - total_cans)
print(n_dozen*14.95)

# 4. Selling Cookies
start = int(input())
num_cookies = input()
num_big = input()


n_cookie = len(num_cookies)
n_big = len(num_big)
profit = (n_cookie * 1.25 - n_cookie * 0.5) + (n_big * 2 - n_big * 0.75)

print(f"Total cookies sold: {n_cookie + n_big}")
print(f"Profit: {profit}")
print(f"Total money: {start + profit}")
