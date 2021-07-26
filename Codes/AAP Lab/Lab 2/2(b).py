# Name - Kumarjeet Ray
# Roll - 1928170
# Batch - CSSE 3


if __name__ == '__main__':
    sen = input("Enter a String:")
    count = 0
    for i in range(len(sen)):
        if sen[i] != ' ':
            count += 1
    print('Number of letters:' + str(count))
