# coding: utf-8
# Your code here!

TABLES = [
    [0, 0],
    [11000, 40],
    [8000, 30],
    [400, 30],
    [800, 20],
    [900, 14],
    [1800, 16],
    [1000, 15],
    [7000, 40],
    [100, 10],
    [300, 12]
    ]
LIMIT = 150

def main():
    DP = [[0]*(LIMIT+1) for _ in range(len(TABLES))]
    for hg in range(1, len(TABLES)):
        for wd in range(LIMIT+1):
            if wd-TABLES[hg][1]<0:
                DP[hg][wd] = DP[hg-1][wd]
            else:
                DP[hg][wd] = max(DP[hg-1][wd], DP[hg-1][wd-TABLES[hg][1]]+TABLES[hg][0])
    
    print(DP[-1][-1])

if __name__ == "__main__":
    main()
