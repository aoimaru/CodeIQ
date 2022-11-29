# coding: utf-8
# Your code here!
import copy

DIR = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
    ]

_LOGS = list()

def rec(LOGS):
    if len(LOGS) >= N:
        return 1
    count = 0
    for D in DIR:
        HG, WD = map(int, LOGS[-1].split(":"))
        LOG = "{}:{}".format(HG+D[0], WD+D[1])
        if LOG in LOGS:
            continue
        NEXTS = copy.copy(LOGS)
        NEXTS.append(LOG)
        count += rec(NEXTS)
    return count
        
def main():
    global N
    N = int(input())+1
    count = rec(["0:0"])
    print(count)

if __name__ == "__main__":
    main()
