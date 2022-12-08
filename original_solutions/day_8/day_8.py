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

lines = get_data(day=8,year=2022).splitlines()

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
    a = np.array([[int(x) for x in list(l)] for l in lines])
    v = 0
    for r in range(a.shape[0]):
        for c in range(a.shape[1]):
            if r == 0 or c == 0 or r == a.shape[0]-1 or c == a.shape[1]-1:
                v+=1
                continue
            n_max = a[r+1:, c].max()
            e_max = a[r, c+1:].max()
            s_max = a[:r, c].max()
            w_max = a[r, :c].max()
            for m in [n_max, e_max, s_max, w_max]:
                if m < a[r,c]:
                    v += 1
                    break
    return v


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    a = np.array([[int(x) for x in list(l)] for l in lines])
    bs = 0
    for r in range(a.shape[0]):
        for c in range(a.shape[1]):
            if r == 0 or c == 0 or r == a.shape[0]-1 or c == a.shape[1]-1:
                continue
            n_max = a[r+1:, c].max()
            e_max = a[r, c+1:].max()
            s_max = a[:r, c].max()
            w_max = a[r, :c].max()
            v = 0
            for m in [n_max, e_max, s_max, w_max]:
                if m < a[r,c]:
                    v += 1
            if v == 4: continue
            sc = 1
            #print(f"({r},{c})={a[r,c]}:", end=" ")
            ms = [
                a[r+1:, c],
                a[r, c+1:],
                list(reversed(a[:r, c])),
                list(reversed(a[r, :c]))
            ]
            for m in ms:
                i = 1
                for n in m:
                    if n >= a[r,c]:
                        break
                    i += 1
                i = min(i, len(m))
                #print(m, i, end=" ")
                sc *= i
            #print("=", sc)
            bs = max(bs, sc)
    return bs


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)