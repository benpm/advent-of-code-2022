from aocd import submit, get_data
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict
from rich.pretty import pprint

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=7,year=2022).splitlines()

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


# def part_A():
#     dt = defaultdict(list)
#     fs = set()
#     drlst = []
#     cwd = (0, -1, "")
#     cwd_stack = []
#     idx = 0
#     for l in lines:
#         ll = l.split(" ")
#         if "$ cd" in l:
#             if ll[2] == "..":
#                 cwd = cwd_stack.pop()
#             else:
#                 if cwd[0] >= 0: cwd_stack.append(cwd)
#                 for dn in dt[cwd]:
#                     if isinstance(dn, tuple) and dn[2] == ll[2]:
#                         cwd = dn
#         elif "$" not in l:
#             if ll[0] != "dir" and (idx, cwd, ll[1]) not in fs:
#                 dt[cwd].append(int(ll[0]))
#                 fs.add((idx, cwd, ll[1]))
#             elif ll[0] == "dir":
#                 dt[cwd].append((idx, cwd[0] + 1, ll[1]))
#                 drlst.append((idx, cwd[0] + 1, ll[1]))
#         elif "$ ls" in l:
#             idx = 0
#             continue
#         idx += 1

#     def sz(dr):
#         if isinstance(dr, tuple):
#             return sum([sz(d) for d in dt[dr]])
#         else:
#             return dr
#     pprint(dt)
#     pprint(drlst)
#     return sum([sz(d) for d in drlst if sz(d) <= 100000])

def part_A():
    fs = []
    dst = []
    cwd = fs
    for l in lines:
        ll = l.split(" ")
        if "$ cd" in l:
            if ll[2] == "..":
                cwd = dst.pop()
            else:
                dst.append(cwd)
                newdir = []
                cwd.append(newdir)
                cwd = newdir
        elif "$" not in l:
            if ll[0] != "dir":
                cwd.append(int(ll[0]))

    dr = []
    def t(l):
        if isinstance(l, list):
            return sum([t(d) for d in l])
        else:
            return l
    def sz(l):
        dr.append(t(l))
        for ll in l:
            if isinstance(ll, list):
                sz(ll)
    sz(fs)
    return sum([d for d in dr if d <= 100000])


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    fs = []
    dst = []
    cwd = fs
    for l in lines:
        ll = l.split(" ")
        if "$ cd" in l:
            if ll[2] == "..":
                cwd = dst.pop()
            else:
                dst.append(cwd)
                newdir = []
                cwd.append(newdir)
                cwd = newdir
        elif "$" not in l:
            if ll[0] != "dir":
                cwd.append(int(ll[0]))

    dr = []
    def t(l):
        if isinstance(l, list):
            return sum([t(d) for d in l])
        else:
            return l
    def sz(l):
        dr.append(t(l))
        for ll in l:
            if isinstance(ll, list):
                sz(ll)
    sz(fs)
    used = dr[0]
    best_x = 1e9
    best = -1
    t_unused = 70_000_000 - used
    for d in dr:
        new_unused = t_unused + d
        x = new_unused - 30_000_000
        print(f"{d=} {new_unused=} {x=}")
        if x < best_x and x >= 0:
            best_x = x
            best = d
    return best


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)