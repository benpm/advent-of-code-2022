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

lines = get_data(day=9,year=2022).splitlines()

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
    drs = {
        "U": np.array([0, 1]),
        "D": np.array([0, -1]),
        "L": np.array([-1, 0]),
        "R": np.array([1, 0])
    }
    hpos = np.array([0, 0])
    tpos = np.array([0, 0])
    last_hpos = np.array([0, 0])
    ps = set()
    for l in lines:
        dr, n = re.match(r"([UDLR]) (\d+)", l).groups()
        dr = drs[dr]
        for _ in range(int(n)):
            ps.add(tuple(tpos))
            last_hpos = hpos.copy()
            hpos += dr
            cdist = max(abs(hpos[0] - tpos[0]), abs(hpos[1] - tpos[1]))
            if cdist > 1:
                tpos = last_hpos.copy()
            # print()
            # for y in range(4, -1, -1):
            #     for x in range(6):
            #         if x == hpos[0] and y == hpos[1]:
            #             print("H", end=" ")
            #         elif x == tpos[0] and y == tpos[1]:
            #             print("T", end=" ")
            #         else:
            #             print(".", end=" ")
            #     print()
    ps.add(tuple(tpos))
    return len(ps)


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    drs = {
        "U": np.array([1, 0]),
        "D": np.array([-1, 0]),
        "L": np.array([0, -1]),
        "R": np.array([0, 1])
    }
    ps = set()
    k = np.zeros((10, 2), dtype=np.int32)
    lk = np.zeros((10, 2), dtype=np.int32)
    for l in lines:
        print(f"\n--- {l} ---")
        dr, n = re.match(r"([UDLR]) (\d+)", l).groups()
        dr = drs[dr]
        for _ in range(int(n)):
            print()
            lk = k.copy()
            k[-1] += dr
            # print(k)
            while True:
                cdist = np.max(np.abs(np.diff(k, axis=0)), axis=1)
                for i in range(9):
                    # print(f"dist {i} to {i+1}: {cdist[i]}")
                    if cdist[i] > 1:
                        k[i] = lk[i + 1]
                        break
                else:
                    break
            ps.add(tuple(k[0]))
            pa = np.empty((5, 6), dtype=str)
            pa.fill(".")
            for i in range(10):
                pa[tuple(k[i])] = 9 - i if i < 9 else "H"
            for y in range(pa.shape[0]-1, -1, -1):
                for x in range(pa.shape[1]):
                    print(pa[y,x], end="")
                print()
    return len(ps)


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)