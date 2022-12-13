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

lines = get_data(day=12,year=2022).splitlines()

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
    a = np.array([[ord(c) for c in l] for l in lines])
    S = np.where(a == ord("S"))
    E = np.where(a == ord("E"))
    a[S] = ord("a")
    a[E] = ord("z")
    a -= (ord("a") - 1)
    cost = a.copy()
    cost.fill(1e9)
    cost[E] = 0
    print(a)
    while np.any(cost == 1e9):
        old = cost.copy()
        for r in range(a.shape[0]):
            for c in range(a.shape[1]):
                for l in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= l[0] < a.shape[0] and 0 <= l[1] < a.shape[1]:
                        dh = a[l] - a[r,c]
                        if dh <= 1:
                            cost[r, c] = min(cost[l] + 1, cost[r, c])
        print(np.sum(cost < 1e9))
        if np.all(old == cost):
            break
    print(cost)
    # np.savetxt("cost.csv", cost, fmt="%d", delimiter=",")
    return cost[S][0]


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    a = np.array([[ord(c) for c in l] for l in lines])
    S = np.where(a == ord("S"))
    E = np.where(a == ord("E"))
    a[S] = ord("a")
    a[E] = ord("z")
    a -= (ord("a") - 1)
    cost = a.copy()
    cost.fill(1e9)
    cost[E] = 0
    print(a)
    while np.any(cost == 1e9):
        old = cost.copy()
        for r in range(a.shape[0]):
            for c in range(a.shape[1]):
                for l in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= l[0] < a.shape[0] and 0 <= l[1] < a.shape[1]:
                        dh = a[l] - a[r,c]
                        if dh <= 1:
                            cost[r, c] = min(cost[l] + 1, cost[r, c])
        print(np.sum(cost < 1e9))
        if np.all(old == cost):
            break
    
    return cost[np.where(a == 1)].min()


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)