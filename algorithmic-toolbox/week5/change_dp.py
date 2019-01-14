# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = {1,3,4}

    min_num_coins = [None] * (m+1)
    min_num_coins[0] = 0

    for m in range(1,m+1):
        min_num_coins[m]=float('inf')
        for coin in coins:
            if m >= coin :
                num_coins = min_num_coins[m-coin] +1

                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
