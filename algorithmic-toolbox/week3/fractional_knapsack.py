# Uses python3
import sys

def get_optimal_value_naive(capacity, weights, values):
    value = 0.
    # write your code here
    A = []
    unit_value = [a/b for a,b in zip(values,weights)]
    unit_value = sorted(unit_value, key=int, reverse=True)

    # ext = [1,2,0]
    # weights = sorted(weights, key=lambda e: (ext.index(e[2]), -e[1]),reverse= True)
    # values = sorted(values, key=lambda e: (ext.index(e[2]), -e[1]),reverse= True)

    for i in range(len(weights)):

        if capacity ==0:
            return value

        a = min(weights[i],capacity)

        value = value + a * unit_value[i]

        weights[i] = weights[i] - a

        A.insert(i,) 

    return value


def get_optimal_value(capacity, weights, values):
    value = 0

    newlist = sorted(list(zip(values, weights)), key = lambda x : x[0] / x[1], reverse = True)

    values =[t[0] for t in newlist]
    weights =[t[1] for t in newlist]

    

    
    for i in range(len(weights)):
        if capacity==0:
            return value
        a = min(weights[i],capacity)
        value +=a * values[i]/weights[i]

        weights[i] -=a
        capacity -= a


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
