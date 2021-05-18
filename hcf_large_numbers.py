'''
To find the hcf of large numbers entered by the user
'''
num1,num2=eval(input("Enter two numbers with a , between them:"))
r=num1%num2
while r!=0:
    num1,num2=num2,r
    r=num1%num2
print("HCF is ",num2)
