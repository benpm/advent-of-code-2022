from aocd import submit, get_data
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict
import re
from rich.pretty import pprint
from rich.progress import track
from math import lcm, sqrt, ceil, prod
from primefac import primefac

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=11,year=2022).splitlines()

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

class M:
    def __init__(self, idx, items, op, test):
        self.idx = idx
        self.items = items
        self.op = (op[0], int(op[1]) if op[1] != "old" else "old")
        self.test = test
        self.inspect = 0
    
    def __repr__(self) -> str:
        return f"M{self.idx} {self.items}"

# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
def part_A():
    ms: list[M] = []
    for i in range(0, len(lines), 7):
        ms.append(M(
            idx=int(re.search(r"(\d+)", lines[i]).group(1)),
            items=[int(x) for x in re.findall(r"(\d+)", lines[i+1])],
            op=re.search(r"new = old ([*+]) (\w+)", lines[i+2]).groups(),
            test=(
                int(re.search(r"(\d+)", lines[i+3]).group(1)),
                int(re.search(r"(\d+)", lines[i+4]).group(1)),
                int(re.search(r"(\d+)", lines[i+5]).group(1)))
        ))
    
    for i in range(20):
        for m in ms:
            for it in m.items:
                m.inspect += 1
                op = (m.op[0], it) if m.op[1] == "old" else m.op
                it = (it * op[1] if op[0] == "*" else it + op[1]) // 3
                if it % m.test[0] == 0:
                    ms[m.test[1]].items.append(it)
                else:
                    ms[m.test[2]].items.append(it)
            m.items = []

    return np.prod(sorted([m.inspect for m in ms], reverse=True)[:2], axis=0)


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------

def part_B():
    ms: list[M] = []
    for i in range(0, len(lines), 7):
        ms.append(M(
            idx=int(re.search(r"(\d+)", lines[i]).group(1)),
            items=[int(x) for x in re.findall(r"(\d+)", lines[i+1])],
            op=re.search(r"new = old ([*+]) (\w+)", lines[i+2]).groups(),
            test=(
                int(re.search(r"(\d+)", lines[i+3]).group(1)),
                int(re.search(r"(\d+)", lines[i+4]).group(1)),
                int(re.search(r"(\d+)", lines[i+5]).group(1)))
        ))
    
    # FUCK YOU FUCK YOU FUCK YOU FUCK YOU
    ilcm = lcm(*[m.test[0] for m in ms])
    
    for i in range(10_000):
        for m in ms:
            for it in m.items:
                m.inspect += 1
                op = (m.op[0], it) if m.op[1] == "old" else m.op
                it = (it * op[1] if op[0] == "*" else it + op[1]) % ilcm
                if it % m.test[0] == 0:
                    ms[m.test[1]].items.append(it)
                else:
                    ms[m.test[2]].items.append(it)
            m.items = []

    return np.prod(sorted([m.inspect for m in ms], reverse=True)[:2], axis=0)


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)