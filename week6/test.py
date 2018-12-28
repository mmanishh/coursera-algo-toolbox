
import numpy as np
def test(n):

    arr = [[0 for i in range(n)] for j in range(n)]
    count = 1
    for s in range(n):
        for i in range(n-s):
            j = s+ i
            arr[i][j] = count
            count +=1
    
    print(np.array(arr))


if __name__ == "__main__":

    test(6)