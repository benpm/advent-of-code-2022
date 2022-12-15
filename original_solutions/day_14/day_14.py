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

lines = get_data(day=14,year=2022).splitlines()

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
    WALL, EMPTY, SAND = 1, 0, 2
    SYMBOL = {
        WALL: "#",
        EMPTY: ".",
        SAND: "+",
    }
    bounds = [np.inf, -np.inf, np.inf, -np.inf]
    walls = []
    for l in lines:
        w = []
        for d in l.split(" -> "):
            x,y = [int(v) for v in d.split(",")]
            w.append((x,y))
            bounds = [
                min(bounds[0], x),
                max(bounds[1], x),
                min(bounds[2], y),
                max(bounds[3], y),
            ]
        walls.append(w)
    source = (500, 0)
    bounds = [
        min(bounds[0], source[0]) - 2,
        max(bounds[1], source[0]) + 2,
        min(bounds[2], source[1]),
        max(bounds[3], source[1]) + 2,
    ]
    min_x, max_x, min_y, max_y = bounds
    w = max_x - min_x + 1
    h = max_y - min_y + 1
    walls = [[(x-min_x, y-min_y) for x,y in w] for w in walls]
    source = (0, 500-min_x)
    a = np.ndarray((h, w), dtype=int)
    a.fill(EMPTY)
    for wall in walls:
        for i in range(len(wall) - 1):
            dx1, dy1 = wall[i]
            dx2, dy2 = wall[i+1]
            dx1, dx2 = min(dx1, dx2), max(dx1, dx2)
            dy1, dy2 = min(dy1, dy2), max(dy1, dy2)
            if dx1 == dx2:
                for y in range(dy1, dy2+1):
                    a[y,dx1] = WALL
            elif dy1 == dy2:
                for x in range(dx1, dx2+1):
                    a[dy1,x] = WALL
    
    fallen = False
    while not fallen:
        a[source] = SAND
        rested = False

        while not rested and not fallen:
            for r in range(h):
                for c in range(w):
                    if a[r,c] == SAND:
                        a[r,c] = EMPTY
                        if r == h-1:
                            fallen = True
                        elif a[r+1,c] == EMPTY:
                            a[r+1,c] = SAND
                        elif a[r+1,c-1] == EMPTY:
                            a[r+1,c-1] = SAND
                        elif a[r+1,c+1] == EMPTY:
                            a[r+1,c+1] = SAND
                        else:
                            a[r,c] = SAND
                            rested = True
        # for r in range(h):
        #     for c in range(w):
        #         print(SYMBOL[a[r,c]], end="")
        #     print()
    return np.sum(a == SAND)


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    WALL, EMPTY, SAND = 1, 0, 2
    SYMBOL = {
        WALL: "#",
        EMPTY: ".",
        SAND: "+",
    }
    bounds = [np.inf, -np.inf, np.inf, -np.inf]
    walls = []
    for l in lines:
        w = []
        for d in l.split(" -> "):
            x,y = [int(v) for v in d.split(",")]
            w.append((x,y))
            bounds = [
                min(bounds[0], x),
                max(bounds[1], x),
                min(bounds[2], y),
                max(bounds[3], y),
            ]
        walls.append(w)
    source = (500, 0)
    bounds = [
        min(bounds[0], source[0]) - 200,
        max(bounds[1], source[0]) + 200,
        min(bounds[2], source[1]),
        max(bounds[3], source[1]) + 1,
    ]
    min_x, max_x, min_y, max_y = bounds
    w = max_x - min_x + 1
    h = max_y - min_y + 1
    walls = [[(x-min_x, y-min_y) for x,y in w] for w in walls]
    source = (0, 500-min_x)
    a = np.ndarray((h, w), dtype=int)
    a.fill(EMPTY)
    for wall in walls:
        for i in range(len(wall) - 1):
            dx1, dy1 = wall[i]
            dx2, dy2 = wall[i+1]
            dx1, dx2 = min(dx1, dx2), max(dx1, dx2)
            dy1, dy2 = min(dy1, dy2), max(dy1, dy2)
            if dx1 == dx2:
                for y in range(dy1, dy2+1):
                    a[y,dx1] = WALL
            elif dy1 == dy2:
                for x in range(dx1, dx2+1):
                    a[dy1,x] = WALL
    
    while a[source] != SAND:
        a[source] = SAND
        rested = False
        s = source

        while not rested:
            r,c = s
            a[r,c] = EMPTY
            if r == h-1:
                a[r,c] = SAND
                rested = True
            elif a[r+1,c] == EMPTY:
                r += 1
                a[r,c] = SAND
            elif a[r+1,c-1] == EMPTY:
                r += 1
                c -= 1
                a[r,c] = SAND
            elif a[r+1,c+1] == EMPTY:
                r += 1
                c += 1
                a[r,c] = SAND
            else:
                a[r,c] = SAND
                rested = True
            s = (r,c)
        
        # print()
        # for r in range(h):
        #     for c in range(w):
        #         print(SYMBOL[a[r,c]], end="")
        #     print()
    return np.sum(a == SAND)


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)