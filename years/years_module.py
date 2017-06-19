"""Exercise:

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Write a function called "years", which contains the main logic: calculates the year from the age.

Extras:

1) Add on to the previous program by asking the user for another number and printing
out that many copies of the previous message.
(Hint: order of operations exists in Python)

2) Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime


def years(age):
    date = datetime.datetime.now()
    year = date.year
    x = year - age + 100
    return x


def main():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    turning_100 = years(age)
    print ("Dear {}, you will be 100 years old in {}".format(name, turning_100))


if __name__ == '__main__':
    main()
