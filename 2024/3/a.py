import pyperclip
import re

command = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
# print(command)
ans = 0
with open("input") as f:
    for line in f:
        # find all commands
        muls = re.findall(command, line)
        ans += sum([int(a) * int(b) for a, b in muls])

pyperclip.copy(ans)
print(ans)

