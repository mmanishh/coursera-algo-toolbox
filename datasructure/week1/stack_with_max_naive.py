#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max = -sys.maxsize- 1
        self.max_list = []

    def Push(self, a):
        if a >= self.max:
            self.max = a
            self.max_list.append(a)
        self.__stack.append(a)

    def Pop(self):
        # print('max_list',self.max_list)
        # print('max',self.max)


        assert(len(self.__stack))
        popped = self.__stack.pop()
        if popped == self.max:
            self.max_list.pop()
            self.max = self.max_list[-1]

    def Max(self):
        assert(len(self.__stack))
        return self.max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
