def guess(x):
    import random
    random_number = random.randint(1,x)
    user = input("Enter your name :")

    while x!=random_number:
        guess = int(input("Enter your guess :"))
        if guess == random_number:
            print(f"congrats!, {user.capitalize()} you guessed the number {random_number}")
            quit()
        elif guess < random_number:
            print("Sorry,guess smaller :")
        elif guess > random_number:
            print("Sorry,guess larger :")
guess(10)