def find_nth_smallest(list, n):
    if n < len(list) and n > 0:
        sorted_list = sorted(set(list))
        print(f"{n}'th smallest element is {sorted_list[n-1]}")
    else:
        print("Invalid input")

input_list = list(map(int, input("Enter the list of numbers: ").split()))
n = int(input("Enter the value of n: "))

find_nth_smallest(input_list, n)
