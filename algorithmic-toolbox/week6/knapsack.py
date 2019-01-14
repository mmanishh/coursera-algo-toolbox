# Uses python3
import sys

def optimal_weight_naive(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight(W,w):
    n = len(w)
    value = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):
            #print("i: {0},j: {1}".format(i,j))
            value[i][j]=value[i-1][j]

            if w[i-1] <= j:
                val = value[i-1][j-w[i-1]] + w[i-1]  # replacing v[i] with w[i] because weight itself is value here

                if val>value[i][j]:
                    value[i][j] = val

    #print(np.array(value))
    #print(np.array(value).shape)
    
    return value[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
