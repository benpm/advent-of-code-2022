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

lines = get_data(day=2,year=2022).splitlines()

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
    # A X rock
    # B Y paper
    # C Z scissors
    cost = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    outcome  = {
        ("A", "X"): 3, # rock ties with rock
        ("A", "Y"): 6, # paper beats rock
        ("A", "Z"): 0, # scissors lose to rock
        ("B", "X"): 0, # rock loses to paper
        ("B", "Y"): 3, # paper ties with paper
        ("B", "Z"): 6, # scissors beats paper
        ("C", "X"): 6, # rock beats scissors
        ("C", "Y"): 0, # paper loses to scissors
        ("C", "Z"): 3, # scissors ties with scissors
    }
    s = 0
    for l in lines:
        a, b = l.split()
        print((a, b), cost[b], outcome[(a, b)])
        s += cost[b] + outcome[(a, b)]
    return s


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    # A X rock
    # B Y paper
    # C Z scissors
    cost = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    choice = {
        "A": ["Z", "X", "Y"],
        "B": ["X", "Y", "Z"],
        "C": ["Y", "Z", "X"]
    }
    outcome  = {
        ("A", "X"): 3, # rock ties with rock
        ("A", "Y"): 6, # paper beats rock
        ("A", "Z"): 0, # scissors lose to rock
        ("B", "X"): 0, # rock loses to paper
        ("B", "Y"): 3, # paper ties with paper
        ("B", "Z"): 6, # scissors beats paper
        ("C", "X"): 6, # rock beats scissors
        ("C", "Y"): 0, # paper loses to scissors
        ("C", "Z"): 3, # scissors ties with scissors
    }
    v = ["X", "Y", "Z"]
    s = 0
    for l in lines:
        a, c = l.split()
        b = choice[a][v.index(c)]
        s += cost[b] + outcome[(a, b)]
    return s


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)