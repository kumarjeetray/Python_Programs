# Name - Kumarjeet Ray
# Roll - 1928170
# Batch - CSSE 3


if __name__ == '__main__':
    print("Break Example:")
    i = 0
    while i < 10:
        i = i + 1
        if i == 6:
            break
        else:
            print(i,end=',')
    print('\n')
    print("Continue Example:")
    j = 0
    while j < 10:
        j = j + 1
        if j == 6:
            continue
        else:
            print(j, end=',')
