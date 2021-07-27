# Name - Kumarjeet Ray
# Roll - 1928170
# Batch - CSSE 3


if __name__ == '__main__':
    c = eval(input("Enter 1 if the weight is in kg or Enter 2 if weight is in pound:"))
    weight = eval(input("Enter weight:"))
    if c == 1:
        convert = weight * 2.20462
        print("Weight in pound:" + str(convert) + ' lb')
    elif c == 2:
        convert = weight * 0.453592
        print("Weight in kg:" + str(convert) + ' kg')
    else:
        print('Wrong Choice')
