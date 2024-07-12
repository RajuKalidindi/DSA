# Write a program to reverse a given number.

def reverse_number(number):
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number = number // 10
    return result

number = int(input("Enter the number: "))
print(f"Reversed number: {reverse_number(number)}")