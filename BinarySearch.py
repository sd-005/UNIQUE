def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

def fibonacci_search(arr, key):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < key:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > key:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return True

    if fib1 and offset + 1 < n and arr[offset + 1] == key:
        return True

    return False

# Main
n = int(input("Enter number of students attended training: "))
roll_numbers = []

print("Enter roll numbers in sorted order:")
for _ in range(n):
    r = int(input())
    roll_numbers.append(r)

key = int(input("\nEnter roll number to search: "))

# Binary Search
if binary_search(roll_numbers, key):
    print("Binary Search: Student attended the training.")
else:
    print("Binary Search: Student did NOT attend the training.")

# Fibonacci Search
if fibonacci_search(roll_numbers, key):
    print("Fibonacci Search: Student attended the training.")
else:
    print("Fibonacci Search: Student did NOT attend the training.")
