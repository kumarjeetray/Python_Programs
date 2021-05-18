import random
user_val=eval(input("Enter a number:"))
generate_val=random.randint(1,100)
if(user_val<generate_val):
    print("Too low")
elif(user_val==generate_val):
    print("Equal")
else:
    print("Too High")
