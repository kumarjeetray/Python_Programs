import random
user_val=0
generate_val=random.randint(1,100)
#print(generate_val)
while(user_val!=generate_val):
    user_val=eval(input("Enter a number:"))
    if(user_val<generate_val):
        print("Too low")
    elif(user_val=generate_val):
        print("Value Equal")
    else:
        print("Too High")
