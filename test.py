# def calculator(s):
#     result = 0
#     sign = 1
#     stack = []
#     operationStack = []

#     for i in range(len(s)):
#         curr = s[i]
#         if curr == " ":
#             continue
#         elif curr == "+":
#             sign = 1
#         elif curr == "-":
#             sign = -1
#         elif curr >= "0" and curr <= "9":
#             num = curr
#             while i + 1 < len(s) and s[i + 1] >= "0" and s[i + 1] <= "9":
#                 num += s.charAt(i + 1)
#                 i += 1

#             result += sign * int(num)
#         elif curr == "(":
#             stack.append(result)
#             result = 0
#             operationStack.append(sign)
#             sign = 1
#         elif curr == ")":
#             result = operationStack.pop() * result + stack.pop()
#             sign = 1

#     return result


# import unittest

# expression3 = [9,'+',3,'(',5,')','+',4]
# print(f"{expression3} = {calculate(expression3)}")

# class Test(unittest.TestCase):
#     def test_1(self):
#         assert calculator("2 + 2") == 4
#         print("PASSED: assert calculator('2 + 2') == 4")

#     def test_2(self):
#         assert calculator("(2+2) - 3") == 1
#         print("PASSED: assert calculator('(2+2) - 3') == 1")

#     def test_3(self):
#         assert calculator("-2-(-2)+(-5)") == -5
#         print("PASSED: Negatives")


# if __name__ == "__main__":
#     unittest.main(verbosity=2)
#     print("Nice job, 3/3 tests passed!")