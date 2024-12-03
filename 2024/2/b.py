
import pyperclip

debug_level = 1
debug = True
debug = False

safe_reports = 0

def check(x, y):
    # return 0 if unsafe, 1 if safe increasing, -1 if safe decreasing
    diff = x - y
    if abs(diff) < 4 and abs(diff) > 0:
        if diff > 0:
            return -1
        else:
            return 1
    return 0

def check_numbers(numbers, tolerance=0):
    # return 0 if unsafe, 1 if safe
    input(f"checking numbers: {numbers}") if debug and debug_level == 1 else None
    checks = [check(a,b) for a,b in zip(numbers, numbers[1:])]
    input(f"checks: {checks}") if debug else None
    # check there is no 0 in checks
    if checks.count(0) <= tolerance:
        if abs(sum(checks)) >= len(checks) - tolerance:
            return 1 # there is at most <tolerance> zero
    return 0

def small_filter(numbers):
    checks = [check(a,b) for a,b in zip(numbers, numbers[1:])]
    return checks.count(0) <= 2 and abs(sum(checks)) >= len(checks) - 3 # at most one zero and one incongruence or two zeros

j = 0
with open("input1") as f:
    for line in f:
        numbers = line.split(" ")
        numbers = [int(x) for x in numbers]
        # if not small_filter(numbers):
        #     print(f"[{j}] skipping {numbers}") if debug else None
        #     j += 1
        #     continue
        increasing = sum([check(a,b) for a,b in zip(numbers, numbers[1:])]) > 0
        # do stuff
        input(f"[{j}] numbers: {numbers}") if debug else None
        i = 0
        while i < len(numbers) - 1:
            a = numbers[i]
            b = numbers[i+1]
            diff = a - b
            if abs(diff) < 4 and abs(diff) > 0:
                # safe
                if diff > 0:
                    # decreasing
                    if increasing:
                        break
                else:
                    # increasing
                    if not increasing:
                        break
            else:
                # unsafe
                break
            i += 1
        input(f"ended loop at i: {i} - breaked == {i < len(numbers) - 1}") if debug and debug_level == 1 else None
        if i < len(numbers) - 1: # breaked before end
            print(f"incongruence found between {numbers[i]} and {numbers[i+1]}") if debug and debug_level >= 1 else None
            if check_numbers(numbers[:i] + numbers[i+1:]) or check_numbers(numbers[:i+1] + numbers[i+2:]):
                safe_reports += 1
                print("[+]", end=" ") if debug else None
            else:
                print("[-]", end=" ") if debug else None
        else:
            # safe report found
            safe_reports += 1
            print("[+]", end=" ") if debug else None
        input(f"safe_reports: {safe_reports}") if debug else None
        j += 1



pyperclip.copy(safe_reports)
print(safe_reports)

