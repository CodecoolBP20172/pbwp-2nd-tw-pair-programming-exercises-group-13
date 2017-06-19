
"""Exercise:

A palindrome is a string that reads the same forwards and backwards.

Write a function called "palindrome", which decides whether a string is a palindrome or not.
Ask the user for a string and print out the result.
Be aware of white spaces!"""


def palindrome(str):
    formatted_str = str.replace(" ", "").lower()
    lst = list(formatted_str)
    print (lst)
    reversed_lst = lst[::-1]
    print (reversed_lst)
    if lst == reversed_lst:
        return True
    else:
        return False


def main():
    user_input = input("Enter a text: ")
    palindrome(user_input)
    return


if __name__ == '__main__':
    main()
