# Name - Kumarjeet Ray
# Roll Number - 1928170
# Batch - CSSE3
if __name__ == '__main__':
    cars = ['Ford', 'BMW', 'Volvo','tata', 'FERRARI', 'hyundai']
    print('Original List:', cars)
    cars.pop()
    print('After Pop:', cars)
    cars2 = ['Skoda', 'Mazda', 'AUDI', 'Porsche', 'mercedes', 'TESLA']
    cars.extend(cars2)
    print('After Extend:', cars)
    cars.append('hyundai')
    print('After Append:', cars)