# Name - Kumarjeet Ray
# Roll Number - 1928170
# Batch - CSSE3
if __name__ == '__main__':
    cars = ('Ford', 'BMW', 'Volvo')
    print('Original Tuple:', cars)
    cars = list(cars)
    cars.pop(1)
    cars = tuple(cars)
    print('Updated Tuple:', cars)