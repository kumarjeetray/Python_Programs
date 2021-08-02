# Name - Kumarjeet Ray
# Roll Number - 1928170
# Batch - CSSE3
if __name__ == '__main__':
    list1 = []
    flag = 0
    for i in range(5):
        list1.append(input('Enter a word in the list:'))
    ele = input('Enter the word to be replaced:')
    rep = input('Enter the word:')
    for i in range(5):
        if list1[i] == ele:
            list1[i] = rep
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        print('Element not found in the list')
    else:
        print('New List:', list1)