import pyperclip

res = 0

with open("input") as f:
    for line in f:
        # line contains alphanumeric characters, take only the first and the last number
        numbers = "".join([c for c in line if c.isnumeric()])
        res += int(numbers[0])*10 + int(numbers[-1])

pyperclip.copy(res)
print(res)

