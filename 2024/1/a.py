import pyperclip

a1 = []
a2 = []
distance = 0

def sort_append(a, n):
    length = len(a)
    for i in range(length):
        if n > a[length - i - 1]:
            a.insert(length - i, n)
            return
    a.insert(0, n)

with open("input1") as f:
    for line in f:
        n1, n2 = map(int, line.split())
        # do stuff
        sort_append(a1, n1)
        sort_append(a2, n2)

for i in range(len(a1)):
    distance += abs(a1[i] - a2[i])

pyperclip.copy(distance)
print(distance)

