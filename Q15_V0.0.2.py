# coding: utf-8
# Your code here!

Q15 = dict()

def rec(A, B):
    _KEY = "{}:{}".format(A, B)
    if _KEY in Q15:
        return Q15[_KEY]
    if A > B:
        return 0
    if A == B:
        return 1
    cnt = 0
    for a in range(1, 5):
        for b in range(1, 5):
            cnt += rec(A+a, B-b)
    Q15[_KEY] = cnt
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
