data = ["2","*", "(", "55", "+", "/""22",")"] 
new_data = []

for i in range(len(data)):
    if data[i] == '(':
        for j in range(i, len(data)):
            if data[j] == ')':
                temp = j
        for x in range(i, j+1):
            if data[x] == "+":
                temp2 = x
                result = int(data[x-1]) + int(data[x+1])
                data[i] = result
            elif data[x] == "-":
                temp2 = x
                result = int(data[x-1]) - int(data[x+1])
                data[i] = result
            elif data[x] == "*":
                temp2 = x
                result = int(data[x-1]) * int(data[x+1])
                data[i] = result
            elif data[x] == "/":
                temp2 = x
                result = int(data[x-1]) / int(data[x+1])
                data[i] = result
                break
        new_data.extend(data[0:i+1])
                
print(new_data)





# data = ["2","+", "(", "2", "+", "6","+","5", ")"]
# new_data = []

# for i in range(len(data)):
#     if data[i] == '(':
#         for j in range(i, len(data)):
#             if data[j] == ')':
#                 temp = j
#         for x in range(i, j+1):
#             if data[x] == "+":
#                 temp2 = x
#                 result = int(data[x-1]) + int(data[x+1])
#                 data[i] = result
#                 break
#         new_data.extend(data[0:i+1])
# print(new_data)