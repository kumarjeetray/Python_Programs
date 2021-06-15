try:
    num=int(input("Enter a number:"))
    print(num)
    cal=num/0
except ZeroDivisionError:
    print("Division by 0 error")
except ValueError:
    print("Wrong Input type")