import pyperclip
from pwn import args
try:
    debug = int(args.DBG) or 0
except:
    debug = 0
print("Debug level:", debug)
res = 0
res_ex = 0
letterals_paths = {
    "z": [{"e": [{"r": [{"o": 0}]}]}],
    "o": [{"n": [{"e": 1}]}],
    "t": [{"w": [{"o": 2}]}, {"h": [{"r": [{"e": [{"e": 3}]}]}]}],
    "f": [{"o": [{"u": [{"r": 4}]}]}, {"i": [{"v": [{"e": 5}]}]}],
    "s": [{"i": {"x": 6}}, {"e": {"v": {"e": {"n": 7}}}}],
    "e": [{"i": [{"g": [{"h": [{"t": 8}]}]}]}],
    "n": [{"i": [{"n": [{"e": 9}]}]}],
}
current_path = []
found_number = False
with open("input") as f:
    i = 0
    for line in f:
        ex_line = line.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0")
        numbers_ex = "".join([c for c in ex_line if c.isnumeric()])
        res_ex_line = int(numbers_ex[0])*10 + int(numbers_ex[-1])
        numbers = ""
        # line contains alphanumeric characters, take only the first and the last number
        print("Analyzing line:", line) if debug > 2 else None
        for c in line:
            found_number = False
            input(f"[{c}] {current_path}") if debug > 2 else None
            if c.isnumeric():
                numbers += c
                current_path = []
            elif isinstance(current_path, list):
                new_current_path = current_path.copy()
                for j, path in enumerate(current_path):
                    input(f"[{c}, {j}] new_current_path start {new_current_path}") if debug > 2 else None
                    new_current_path[j] = path.get(c, [None])
                    if isinstance(new_current_path[j], list):
                        new_current_path[j] = new_current_path[j][0]
                input(f"[{c}] new_current_path -> {new_current_path}") if debug > 2 else None
                current_path = [p for p in new_current_path if p is not None]
            
            for path in current_path:
                print(f"[{c}] looking for numbers in {path}") if debug > 2 else None
                if isinstance(path, int):
                    print(f"[!] [{c}] found number {path}") if debug > 2 else None
                    numbers += str(path)
                    current_path.remove(path)
                    # found_number = True
                    break
            if not found_number:
                current_path += letterals_paths.get(c, [])
        print("Numbers:", numbers) if debug > 1 else None
        res_line = int(numbers[0])*10 + int(numbers[-1])
        if res_line != res_ex_line:
            input(f"[{i}] {line} -> {numbers} -> {res_line} | ex: {res_ex_line}") if debug > 0 else None
        res += res_line
        res_ex += res_ex_line
        i += 1

pyperclip.copy(res)
print(res, res_ex)

