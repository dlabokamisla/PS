import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# first solution
characters = letters + symbols + numbers
password = ''.join(random.choice(letters) for i in range(nr_letters))
password += ''.join(random.choice(symbols) for a in range(nr_symbols))
password += ''.join(random.choice(numbers) for n in range(nr_numbers))

# Please find the code below to shuffle the string.
# The code will take the string and convert that string to list.
# Then shuffle the string contents and will print the string.
string = list(password)
random.shuffle(string)
print(''.join(string))

# second solution
# password_list = []
# for char in range(nr_letters):
#     password_list += random.choice(letters)
# for char in range(nr_symbols):
#     password_list += random.choice(symbols)
# for char in range(nr_numbers):
#     password_list += random.choice(numbers)
#
# password = ""
# random.shuffle(password_list)
# for char in password_list:
#     password += char
#
# print(password)

