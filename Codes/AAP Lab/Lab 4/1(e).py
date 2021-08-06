# Name - Kumarjeet Ray
# Roll Number - 1928170
# Batch - CSSE3
if __name__ == '__main__':
    cars = ['Ford', 'BMW', 'Volvo']
    print('Original List:', cars)
    cars_new = []
    for i in range(len(cars)+1):
        if i == 2:
            cars_new.append('Porsche')
        elif i < 2:
            cars_new.append(cars[i])
        else:
            cars_new.append(cars[i - 1])
    print('After changing List:', cars_new)