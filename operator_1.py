input =   ['(','9','+','(','9','+','6',')',')']


def paranthesis(input):
    for stuff in input:
        if stuff == '(':
            if stuff.isdigit()
        
            
            
class Calculator:


    def calculate(self, s):

        result = 0
        current = 0
        sign = 1
        stack = []
        for ss in s:
            if ss.isdigit():
                current = int(ss) + 10*current [7-82]
            elif ss in ["-", "+"]:
                result += sign * current
                current = 0
                if ss =="+":
                    sign = 1
                else:
                    sign = -1
            elif ss == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ss == ")":
                result += current * sign
                result *= stack.pop()
                result += stack.pop()
                current = 0
        return result + current * sign
            
                

