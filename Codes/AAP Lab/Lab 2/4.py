# Name - Kumarjeet Ray
# Roll - 1928170
# Batch - CSSE 3


if __name__ == '__main__':
    fee = 100000
    grade = input("Enter Grade:")
    if grade.upper() == 'O' or grade.upper() == 'E':
        fee = fee * 0.80
    else:
        fee = fee * 0.90
    print('Fees = ' + str(fee))
