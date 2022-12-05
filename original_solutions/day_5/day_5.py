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

lines = get_data(day=5,year=2022).splitlines()

if EXAMPLE:
    with open("test.txt", "r") as f:
        lines = f.readlines()
    data = "\n".join(lines)

lines = [l.replace("\n", "") for l in lines]

if lines[-1] == "":
    lines = lines[:-1]


# ---------------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------------


def part_A():
    st = defaultdict(list)
    stcount = 0
    for l in lines:
        for i in range(len(l)):
            if re.search(r'[A-Z]', l[i]):
                st[((i - 1) // 4) + 1].append(l[i])
                stcount = max(stcount, ((i - 1) // 4) + 1)
        if not l: break
    for k in st:
        st[k] = list(reversed(st[k]))
    for l in lines:
        if "move" in l:
            b, fs, ts = re.match(r'move (\d+) from (\d+) to (\d+)', l).groups()
            for i in range(int(b)):
                bb = st[int(fs)].pop()
                st[int(ts)].append(bb)
    return "".join([st[i][-1] for i in range(1, stcount+1)])


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    st = defaultdict(list)
    stcount = 0
    for l in lines:
        for i in range(len(l)):
            if re.search(r'[A-Z]', l[i]):
                st[((i - 1) // 4) + 1].append(l[i])
                stcount = max(stcount, ((i - 1) // 4) + 1)
        if not l: break
    for k in st:
        st[k] = list(reversed(st[k]))
    for l in lines:
        if "move" in l:
            b, fs, ts = re.match(r'move (\d+) from (\d+) to (\d+)', l).groups()
            ss = []
            for i in range(int(b)):
                ss.append(st[int(fs)].pop())
            st[int(ts)].extend(reversed(ss))
    return "".join([st[i][-1] for i in range(1, stcount+1)])


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)