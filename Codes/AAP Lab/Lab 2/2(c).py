# Name - Kumarjeet Ray
# Roll - 1928170
# Batch - CSSE 3


if __name__ == '__main__':
    sen = input("Enter a sentence:")
    word = input("Enter the word to be replaced:")
    replace = input("Enter the replacement word:")
    if word in sen:
        replaced = sen.replace(word, replace)
    print("After changes:"+replaced)
