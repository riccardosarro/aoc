
import pyperclip

safe_reports = 0
debug = False

def check(x, y):
    # return 0 if unsafe, 1 if safe increasing, -1 if safe decreasing
    diff = x - y
    if abs(diff) < 4 and abs(diff) > 0:
        if diff > 0:
            return -1
        else:
            return 1
    return 0


def check_numbers(numbers):
    # return 0 if unsafe, 1 if safe
    input(f"checking numbers: {numbers}") if debug else None
    checks = [check(a,b) for a,b in zip(numbers, numbers[1:])]
    input(f"checks: {checks}") if debug else None
    # check there is no 0 in checks
    if checks.count(0) == 0:
        if abs(sum(checks)) == len(checks):
            return 1 # there is no incongruence
    return 0

with open("input1") as f:
    for line in f:
        numbers = line.split(" ")
        numbers = [int(x) for x in numbers]
        # do stuff
        if check_numbers(numbers):
            safe_reports += 1


pyperclip.copy(safe_reports)
print(safe_reports)

