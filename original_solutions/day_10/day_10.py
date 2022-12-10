from aocd import submit, get_data
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict
import re
from rich.pretty import pprint

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=10,year=2022).splitlines()

if EXAMPLE:
    with open("test.txt", "r") as f:
        lines = f.readlines()
    data = "\n".join(lines)

lines = [l.strip() for l in lines]

if lines[-1] == "":
    lines = lines[:-1]


# ---------------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------------


def part_A():
    x = 1
    c = 0
    xv = {}
    for l in lines:
        if "addx" in l:
            c += 1
            xv[c] = c * x
            c += 1
            xv[c] = c * x
            x += int(l.split(" ")[1])
        else:
            c += 1
            xv[c] = c * x
    return sum([xv[i] for i in [20, 60, 100, 140, 180, 220]])


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    x = 1
    c = 0
    out = []
    z = 0
    for l in lines:
        if "addx" in l:
            c += 1
            out.append("#" if (x - 1 <= (c-1) % 40 <= x + 1) else ".")
            c += 1
            out.append("#" if (x - 1 <= (c-1) % 40 <= x + 1) else ".")
            x += int(l.split(" ")[1])
        else:
            c += 1
            out.append("#" if (x - 1 <= (c-1) % 40 <= x + 1) else ".")
    print("".join([o + ("\n" if i % 40 == 39 else "") for i,o in enumerate(out)]))
    return 0


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)