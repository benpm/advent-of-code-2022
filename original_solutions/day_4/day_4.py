from aocd import submit, get_data
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=4,year=2022).splitlines()

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
    c=0
    for l in lines:
        a, b = l.split(",")
        print(a,b)
        a = [int(i) for i in a.split("-")]
        b = [int(i) for i in b.split("-")]
        if (a[0] <= b[0] <= a[1]) and (a[0] <= b[1] <= a[1]):
            c += 1
        elif (b[0] <= a[0] <= b[1]) and (b[0] <= a[1] <= b[1]):
            c += 1
    return c


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    c=0
    for l in lines:
        a, b = l.split(",")
        print(a,b)
        a = [int(i) for i in a.split("-")]
        b = [int(i) for i in b.split("-")]
        if (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1]):
            c += 1
        elif (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1]):
            c += 1
    return c


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)