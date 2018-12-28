def check_parentheses(a):


    inputs = a.split()
    print(inputs)
    stack = []
    for i,input in enumerate(inputs):

        if input == '{' or input=='(' or input=='[':
            stack.append(input)
        print(i,stack)
        if input == '}' or input==')' or input==']':
            if len(stack) <=0:
                return False
            elif not is_matching(stack.pop(),input):
                return False
        
    print('final:',stack)
    if len(stack) <=0:
        return True
    else:
        return False


def is_matching(char1,char2):
    if char1 == '(' and char2==')':
        return True
    elif char1 == '{' and char2=='}': 
        return True
    elif char1 == '[' and char2==']':
        return True
    else:
        return False
    

if __name__ == "__main__":

    if check_parentheses('{ ( ) } ( ) [ ]'):
        print("balanced")

    else :
        print("not balanced")



