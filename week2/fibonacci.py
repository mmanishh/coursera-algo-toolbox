# Uses python3
import array as arr
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fiblist(n):
    F = []
    if (n <= 1):
        return n
    F.append(0)
    F.append(1)

    for i in range(2,n+1):
        F.insert(i,F[i-1] + F[i-2])
    return F[n]

def last_digit_fib(n):
    F = []
    if (n <= 1):
        return n
    F.append(0)
    F.append(1)

    for i in range(2,n+1):
        F.insert(i,(F[i-1] + F[i-2])%10)
    return F[n]

def fib_again(n,m):
    return fiblist(n) % m

def fiblist_sum(n):
    F = []
    total = 0
    if (n <= 1):
        return n
    F.append(0)
    F.append(1)
    total +=1

    for i in range(2,n+1):
        
        F.insert(i,F[i-1] + F[i-2])
        total += F[i-1] + F[i-2]
    return total

def last_digit_sum_fib(n):

    fib = fiblist_sum(n)
    return fib % 10

if __name__ == "__main__":
        
    # n = int(input())
    input = input()
    a, b = map(int, input.split())
    print(fib_again(a,b)) 