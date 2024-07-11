# Write a program to generate a list of all binary numbers upto a given number n.

from collections import deque

def generate_binary_numbers(n):
    result = []
    queue = deque()
    queue.append("1")

    while n > 0:
        n -= 1
        current = queue.popleft()
        result.append(current)
        queue.append(current + "0")
        queue.append(current + "1")

    return result

n = int(input("Enter the value of n: "))
print(generate_binary_numbers(n))