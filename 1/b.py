import pyperclip

a1 = {}
a2 = {}
score = 0

with open("input1") as f:
    for line in f:
        n1, n2 = map(int, line.split())
        # do stuff
        if n1 in a1:
            a1[n1] += 1
        else:
            a1[n1] = 1
        if n2 in a2:
            a2[n2] += 1
        else:
            a2[n2] = 1

for i in a1:
    if a2.get(i) is not None:
        score += a2[i] * (i ** a1[i])

pyperclip.copy(score)
print(score)

