# Uses python3
import sys
import random

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    left = [(s,'l')for s in starts]
    right = [(r,'r')for r in ends]
    p = [(p,'p')for p in points]

    merged = left + right + p

    merged = sorted(merged,key= lambda x:x[0])
    #print(merged)
    count = 0
    for each,label in merged:
        if label == 'l':
            count +=1
        elif label == 'p':
            cnt[points.index(each)] = count
            count = 0
        elif label == 'r':
            count =0
        
    
    return cnt

    
    

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

def stress_test(low=10000,high=100000):
    while True:
        starts = []
        ends = []
        points =[]

        iter = random.randint(1000,10000)

        for i in range(iter):
            start = random.randrange(low, high)
            seg = random.randint(low,high)
            end = start + seg
            p = random.randrange(start,end)
            starts.append(start)
            ends.append(end)
            points.append(p)
        
        print("segments:",seg)
        result_1 = naive_count_segments(starts,ends,points)
        result_2 = fast_count_segments(starts,ends,points)
        
        if result_1 == result_2:
            print("-ok-")
        else:
            print("Wrong answer:",result_1," ",result_2)
            return

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends   = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # #use fast_count_segments
    # cnt = fast_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')


    stress_test()