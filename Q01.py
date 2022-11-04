# coding: utf-8
# Your code here!
from collections import Counter

def main():
    N = int(input())
    COUNT = 0
    for i in range(0, N+1):
        for j in range(0, N+1-i):
            COMB = Counter([i, j, N-(i+j)])
            if len(COMB) == 1:
                continue
            if len(COMB) == 2:
                if [key for key, value in COMB.items() if value==2][0] < [key for key, value in COMB.items() if value==1][0]:
                    COUNT += 1
            if len(COMB) == 3:
                COUNT += 1
    
    print(COUNT)
            
if __name__ == "__main__":
    main()