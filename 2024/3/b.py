import pyperclip
import re

command = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
# print(command)
ENABLED = 'do()'
DISABLED = 'don\'t()'
enabled = True
ans = 0
with open("input") as f:
    for line in f:
        # find all enabled lines
        parts = line.split(DISABLED)

        # first line is enabled by default unless it is disabled from the previous line
        enabled_line = parts[0] if enabled else ""
        input(enabled_line)
        for i, part in enumerate(parts[1:]):
            if i != 0:
                enabled = False
            input(part)
            if ENABLED in part:
                print(f"Found at least one do() in part #{i}")
                enabled = True
                enabled_line += "".join(part.split(ENABLED)[1:])
            else:
                print(f"Didn't find do() in part #{i}")
                enabled = False
            input(enabled_line)
        input(enabled_line)
        # find all enabled commands
        muls = re.findall(command, enabled_line)
        ans += sum([int(a) * int(b) for a, b in muls])

pyperclip.copy(ans)
print(ans)

