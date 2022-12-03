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

lines = get_data(day=3,year=2022).splitlines()

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
    s = 0
    for l in lines:
        c1 = set()
        c2 = set()
        for i in l[:len(l)//2]:
            c1.add(i)
        for ii in l[len(l)//2:]:
            c2.add(ii)
        for i in c1.intersection(c2):
            s += ord(i) - ord("a") + 1 if ord(i) >= ord("a") else ord(i) - ord("A") + 27
    return s


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    s = 0
    for idx in range(0, len(lines), 3):
        c = []
        for l in (lines[idx], lines[idx+1], lines[idx+2]):
            c.append(set(l))
        for i in c[0].intersection(c[1], c[2]):
            s += ord(i) - ord("a") + 1 if ord(i) >= ord("a") else ord(i) - ord("A") + 27
    return s


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)