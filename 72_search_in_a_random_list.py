#find the position of an item in a random list
def buble_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

grid=[47,3,60,18,22,58,6]
print(f"The sorted grid is: {buble_sort(grid)}")