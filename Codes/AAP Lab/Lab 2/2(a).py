# Name - Kumarjeet Ray
# Roll - 1928170
# Batch - CSSE 3


if __name__ == '__main__':
    flag = 0
    word = input("Enter the word to be searched:")
    sen = 'I am a student of KIIT University'
    if word in sen:
        flag = 1
    else:
        flag = 0
    if flag == 1:
        print("Word Present")
    else:
        print('Word Absent')