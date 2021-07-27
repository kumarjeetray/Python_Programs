# Name - Kumarjeet Ray
# Roll - 1928170
# Batch - CSSE 3


if __name__ == '__main__':
    print("Break Example:")
    for i in range(10):
        if i == 6:
            break
        else:
            print(i,end=',')
    print('\n')
    print("Continue Example:")
    for i in range(10):
        if i == 6:
            continue
        else:
            print(i, end=',')