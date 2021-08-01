# Name - Kumarjeet Ray
# Roll Number - 1928170
# Batch - CSSE3
if __name__ == '__main__':
    number = []
    for i in range(10):
        number.append(eval(input("Enter a digit of the mobile number:")))
    number_char = []
    for i in range(len(number)):
        if number[i] == 1:
            number_char.append('one')
        elif number[i] == 2:
            number_char.append('two')
        elif number[i] == 3:
            number_char.append('three')
        elif number[i] == 4:
            number_char.append('four')
        elif number[i] == 5:
            number_char.append('five')
        elif number[i] == 6:
            number_char.append('six')
        elif number[i] == 7:
            number_char.append('seven')
        elif number[i] == 8:
            number_char.append('eight')
        elif number[i] == 9:
            number_char.append('nine')
        elif number[i] == 0:
            number_char.append('zero')
    print('Number:', number)
    print('After conversion:', number_char)
