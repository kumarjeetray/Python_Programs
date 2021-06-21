def max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("Larger number:", num1)
    elif num2 > num3 and num2 > num1:
        print("Larger number:", num2)
    else:
        print("Larger number:", num3)

num1, num2, num3 = eval(input("Enter three numbers followed by ,:"))
max(num1, num2, num3)