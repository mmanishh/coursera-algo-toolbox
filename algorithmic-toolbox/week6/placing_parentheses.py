# Uses python3
import numpy as np
import sys

def evalt(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    digits = dataset[0:len(dataset):2]
    ops = dataset[1:len(dataset):2]

    n = len(digits)

    min_mx = [[0 for i in range(n)] for j in range(n)]
    max_mx = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                min_mx[i][j] = digits[i]
                max_mx[i][j] = digits[i]

    for s in range(1,n):
        for i in range(n-s):
            j = i+s

            min_mx[i][j] , max_mx[i][j] = minandmax(i,j,min_mx,max_mx,ops)
            
            # print("iteration ",s)
            # print(minandmax(i,j,min_mx,max_mx,ops))
            # print(np.array(min_mx))
            # print("-"*6)
            # print(np.array(max_mx))
    
    return max_mx[0][n-1]

def minandmax(i,j,min_mx,max_mx,ops):

    minimum = sys.maxsize
    maximum = -sys.maxsize - 1

    for k in range(i,j):

        a = evalt(max_mx[i][k],max_mx[k+1][j],ops[k])
        b = evalt(max_mx[i][k],min_mx[k+1][j],ops[k])
        c = evalt(min_mx[i][k],max_mx[k+1][j],ops[k]) 
        d = evalt(min_mx[i][k],min_mx[k+1][j],ops[k])

        minimum = min(minimum,a,b,c,d)
        maximum = max(maximum,a,b,c,d)
    
    return minimum,maximum

        


if __name__ == "__main__":
    print(get_maximum_value(input()))
