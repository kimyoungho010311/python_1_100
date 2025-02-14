import random

# 52
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 10
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 9
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

result_letters = []
result_symbols = []
result_numbers = []
# TODO : Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
# Generate random number 1 to 52
for _ in range(0, nr_letters):
    result_letters.append(letters[random.randint(0, 51)])
#print(result_letters)

# Generate random symbols 0 to 9
for _ in range(0, nr_symbols):
    result_symbols.append(symbols[random.randint(0,8)])
#print(result_symbols)

# Generate random numbers 0 to 8
for _ in range(0, nr_numbers):
    (result_numbers.append(numbers[random.randint(0,9)]))
#print(result_numbers)

generated_password = result_letters + result_symbols + result_numbers
print("The generated password is -> ")
print("".join(generated_password))

# TODO : The final password does not follow a pattern.

combine_password = result_letters + result_symbols + result_numbers

random.shuffle(combine_password)

print("The randomized password is ->")
print("".join(combine_password))
