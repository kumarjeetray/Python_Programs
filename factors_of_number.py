'''
To find the factors of a number entered by the user
'''
num=eval(input("Enter a number:"))
print("Factors:",end="")
for i in range(1,num+1):
    if num%i==0:
        print(i,end=",")
