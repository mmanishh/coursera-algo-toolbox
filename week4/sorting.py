# Uses python3
import sys
import random

def partition3(A, l, r):
    #write your code here
    lt = l
    i = l
    gt = r
    pivot = A[l]

    while i<=gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt +=1
            i +=1
        elif A[i]>pivot:
            A[i], A[gt] = A[gt],A[i]
            gt -=1
        else:
            i +=1
    
    return lt,gt

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    lt, gt = partition3(a,l,r)
    randomized_quick_sort(a, l, lt - 1);
    randomized_quick_sort(a, gt + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
