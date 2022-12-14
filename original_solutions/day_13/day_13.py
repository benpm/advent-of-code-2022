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

lines = get_data(day=13,year=2022).splitlines()

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

def cmp(a, b, l=0):
    # print(f"{'  ' * l}- Compare {a} vs {b}")
    if isinstance(a, int) and isinstance(b, int):
        return b - a
    if not isinstance(a, list):
        return cmp([a], b, l+1)
    if not isinstance(b, list):
        return cmp(a, [b], l+1)
    for i in range(max(len(a), len(b))):
        if i >= len(a): return 1
        if i >= len(b): return -1
        c = cmp(a[i], b[i], l+1)
        if c != 0:
            # if c > 0: print(f"{'  ' * (l+2)}- [{c}] Left smaller, right order")
            # if c < 0: print(f"{'  ' * (l+2)}- [{c}] Right smaller, wrong order")
            return c
    return 0

def part_A():
    count = 0
    for i in range(0, len(lines), 3):
        # print()
        if cmp(eval(lines[i]), eval(lines[i+1])) >= 0:
            # print((i // 3) + 1)
            count += (i // 3) + 1
    return count


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------

# quicksort with a given comparison function
def qsort(ls, cmp):
    if len(ls) <= 1:
        return ls
    pivot = ls[0]
    left = [a for a in ls[1:] if cmp(a, pivot) < 0]
    right = [a for a in ls[1:] if cmp(a, pivot) >= 0]
    return qsort(left, cmp) + [pivot] + qsort(right, cmp)

def part_B():
    ls = [eval(l) for l in lines if len(l) > 0] + [[[2]], [[6]]]
    ls = qsort(ls, lambda a,b: -cmp(a,b))
    d1 = 0
    d2 = 0
    for i,v in enumerate(ls):
        if len(v) == 1 and v[0] == [2]: d1 = i + 1
        if len(v) == 1 and v[0] == [6]: d2 = i + 1
    pprint(ls)
    return d1 * d2


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)