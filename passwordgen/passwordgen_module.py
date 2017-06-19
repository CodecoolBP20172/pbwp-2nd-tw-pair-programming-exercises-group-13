import random


def passwordgen():
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = lower_letters.upper()
    numbers = "0123456789"
    symbols = "!#&@$@{€¤*"
    password = []
    for i in range(random.randint(8,20)):
        random_n = random.randint(1, 4)
        if random_n == 1:
            password.append(random.choice(lower_letters))
        elif random_n == 2:
            password.append(random.choice(numbers))
        elif random_n == 3:
            password.append(random.choice(symbols))
        elif random_n == 4:
            password.append(random.choice(upper_letters))
    printed_password = "".join(password)
    return printed_password


def main():
    user_password = passwordgen()
    print (user_password)
    while True:
        user_input = input("Would you like to have a new password? (y/n): ")
        if user_input == "y":
            user_password = passwordgen()
            print (user_password)
            continue
        elif user_input == "n":
            break
        else:
            print("Invalid input.")
            continue


if __name__ == '__main__':
    main()
