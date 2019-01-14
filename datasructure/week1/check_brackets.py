# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    stack_index = []
    for i, next in enumerate(text):
        i+=1
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            stack_index.append(i)

        if next in ")]}":
            # Process closing bracket, write your code here
            #if stack is empty
            if len(opening_brackets_stack) <=0:
                return i
            popped = opening_brackets_stack.pop()
            stack_index.pop()
            if not are_matching(popped,next):
                return i

    if len(opening_brackets_stack) <=0:
        return "Success"
    else:
        return stack_index[0]

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
