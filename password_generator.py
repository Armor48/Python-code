import random

# user_data = {
#     "first_name": input("Enter your first name: "),
#     "last_name": input("Enter your last name: "),
#     "num_length": int(input("How many digit you want in your password: "))
# }
user_data = {
    "first_name": "priyanshu",
    "last_name": "kumar",
    "num_length": 3
}
keys = list(user_data.keys())
symbol = ["@", "$", "#", "%", "&"]
number= [1, 2, 3, 4, 5, 6, 7, 8, 9]

def num_genrator(number=number):
    num = ""
    for i in range(user_data["num_length"]):
        num = num + str(random.choice(number))
    return num

def symbol_genrator(symbol=symbol):
    sym = random.choice(symbol)
    return sym

def name_generator(user_data=user_data):
    y = random.randint(0,1)
    if y == 0:
        name = str(user_data[keys[y]]) + str(user_data[keys[1]])
    else:
        name = str(user_data[keys[y]]) + str(user_data[keys[0]])
    return name

def combine_genrator():
    pass_word = ""
    digit = [1,2,3]
    for k in range(3):
        z = random.choice(digit)
        if z == 1:
            digit.remove(1)
            pass_word = pass_word + name_generator()
        elif z == 2:
            digit.remove(2)
            pass_word = pass_word + symbol_genrator()
        else:
            digit.remove(3)
            pass_word = pass_word + num_genrator()
        
    return pass_word
print(combine_genrator())