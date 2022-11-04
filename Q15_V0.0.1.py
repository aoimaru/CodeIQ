# coding: utf-8
# Your code here!

def rec(A, B):
    if A > B:
        return 0
    if A == B:
        return 1
    cnt = 0
    for a in range(1, 5):
        for b in range(1, 5):
            cnt += rec(A+a, B-b)
    return cnt
            
def main():
    # N = int(input())
    N = 20
    A = 0
    B = N
    cnt = rec(A, B)
    print(cnt)
    


if __name__ == "__main__":
    main()
