def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Main
n = int(input("Enter number of students: "))
percentages = []

print("Enter percentages:")
for _ in range(n):
    p = float(input())
    percentages.append(p)

# Sort using quick sort
sorted_percentages = quick_sort(percentages)

# Display all in ascending order
print("\nPercentages in ascending order:")
for p in sorted_percentages:
    print(p)

# Display top 5 scores
print("\nTop five scores:")
for score in sorted_percentages[-1:-6:-1]:  # last 5 in reverse
    print(score)
