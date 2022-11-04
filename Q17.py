# coding: utf-8
# Your code here!

def rec(row):
    if len(row) == N:
        return 1
    count = 0
    if row[-1] == "B":
        count += rec(row+"G")
    count += rec(row+"B")
    return count
        
def main():
    global N
    N = int(input())
    ans = 0
    ans += rec("B")
    ans += rec("G")
    print(ans)

if __name__ == "__main__":
    main()
