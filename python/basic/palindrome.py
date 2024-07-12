# Write a program to check if a given string is a palindrome or not.

def is_palindrome(string):
    return string == string[::-1]

string = input("Enter the string: ")
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")