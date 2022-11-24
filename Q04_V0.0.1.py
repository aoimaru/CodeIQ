# coding: utf-8
# Your code here!

def rec(n, m, bars):
    if bars >= n:
        return 0
    if bars < m:
        return 1+rec(n, m, bars*2)
    else:
        return 1+rec(n, m, bars+3)
        
def main():
    N, M = map(int, input().split())
    print(rec(N, M, 1))
    
if __name__ == "__main__":
    main()
