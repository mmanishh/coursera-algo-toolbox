# Uses python3
import sys

def get_change(m):
    #write your code here
    result = []
    d ={1,5,10}
    for each in reversed(sorted(list(d))):
        while(each<=m):
            m -= each
            result.append(each)

    return len(result)

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
