'''
1. The password has atleast 3 numbers
2. The length of password is more than or equal to 8
3. The password should contain atleast one upper case and one lower case letter
'''

def is_password_valid(password):
    flag_num = 0
    flag_upper = 0
    flag_lower = 0
    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].isnumeric() == True:
                flag_num += 1
            if password[i].isupper() == True:
                flag_upper += 1
            if password[i].islower() == True:
                flag_lower += 1
    else:
        return False
    if flag_num >= 3 and flag_upper >= 1 and flag_lower >= 1:
        return True
    else:
        return False

password = input()
print(is_password_valid(password))
