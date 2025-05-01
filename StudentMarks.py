def average_score(marks):
    total = 0
    count = 0
    for m in marks:
        if m != -1:
            total += m
            count += 1
    if count == 0:
        return 0
    return total / count

def highest_lowest(marks):
    valid_marks = [m for m in marks if m != -1]
    if not valid_marks:
        return None, None
    return max(valid_marks), min(valid_marks)

def count_absent(marks):
    return marks.count(-1)

def highest_frequency(marks):
    freq = {}
    for m in marks:
        if m != -1:
            freq[m] = freq.get(m, 0) + 1
    if not freq:
        return None
    max_freq = max(freq.values())
    for mark, f in freq.items():
        if f == max_freq:
            return mark

# Main
marks = []

n = int(input("Enter number of students: "))
print("Enter marks (enter -1 if student was absent):")
for _ in range(n):
    m = int(input())
    marks.append(m)

print("\nAverage score:", average_score(marks))

high, low = highest_lowest(marks)
print("Highest score:", high)
print("Lowest score:", low)

print("Number of absent students:", count_absent(marks))

print("Marks with highest frequency:", highest_frequency(marks))