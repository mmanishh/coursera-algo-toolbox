# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    mid = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, mid)
    number_of_inversions += get_number_of_inversions(a, b, mid, right)
    #write your code here
    number_of_inversions+= merge(a,b,left,mid+1,right)
    return number_of_inversions

def merge(a,temp,left,mid,right):
    print("left:{0},mid:{1},right:{2}".format(left,mid,right))
    inv = 0
    i = left
    j = mid
    k = left

    while i<= mid-1 and j<=right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            k +=1
            i +=1
        else:
            temp[k] = a[j]
            k +=1
            j +=1
            inv = inv + (mid-1)
    
    while i<= mid-1:
        temp[k] = a[i]
        k +=1
        i +=1
    
    while j<= right:
        temp[k] = a[j]
        k +=1
        j +=1
    
    for i in range(left,right+1):
        a[i] = temp[i]
    
    return inv




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
