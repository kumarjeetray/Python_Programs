def calc(num1, num2, operator):
    if operator == '+':
        res = num1 + num2
    elif operator == '-':
        if num1 > num2:
            res = num1 - num2
        else:
            res = num2 - num1
    elif operator == '/':
        if num1 > num2:
            res = num1 / num2
        else:
            res = num2 / num1
    elif operator == '*':
        res = num1 * num2
    elif operator == '^':
        res = num1 ** num2
    else:
        res="Invalid operator"
    return res

num1, num2 = eval(input("Enter two numbers seperated by ,:"))
op = input("Enter operator:")
res = calc(num1, num2, op)
print("Result:", res)
