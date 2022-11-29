# coding: utf-8
# Your code here!

COINS = dict()

def rec(COIN, CNT):
    if COIN in COINS:
        return COINS[COIN]
    if COIN == 0:
        return 0
    if CNT == 0:
        return 1
    count = 0
    count += rec(COIN+1, CNT-1)
    count += rec(COIN-1, CNT-1)
    COINS[COIN] = count
    return count

def main(): 
    count = rec(1, 4)
    print(count)

if __name__ == "__main__":
    main()
