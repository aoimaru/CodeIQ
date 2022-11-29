# coding: utf-8
# Your code here!

def rec(hg, wd, de):
    # print("hg:", hg, "wd:", wd, "de:", de)
    if hg>H:
        return 0
    if de>=N:
        return 1
    count = 0
    count += rec(hg+wd, wd, de+1)
    count += rec(hg+wd, hg, de+1)
    return count
    

def main():
    global N
    N = int(input())
    global H
    H = int(input())
    count = rec(1, 1, 1)
    print(count//2)
    
        
if __name__ == "__main__":
    main()
