def find_max(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    print(arr[-1])


arr = []
num = eval(input("Enter the number of elements:"))
for i in range(0, num):
    user_input = eval(input("Enter a number:"))
    arr.append(user_input)
find_max(arr)
