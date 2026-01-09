def buble_sort(grid):
    print(f"bubble sort of the list {grid}")
    for i in range(len(grid)-1):
        print(f"pass:{i+1}: Will compare first {len(grid)-i} numbers ")
        for j in range(len(grid)-i-1):
            print(f"Comparing number {grid[j]} and {grid[j+1]}")
            if grid[j] > grid[j+1]:
                print(f"{grid[j]} > {grid[j+1]}, so they swap")
                grid[j], grid[j+1] = grid[j+1], grid[j]
                print(f"{grid[j+1]},{grid[j]} become {grid[j]},{grid[j+1]}")
                print(f"updated list is: {grid}")
            else:
                print(f" {grid[j]} < {grid[j+1]}, already in ascending order,NO swapping!")
                print(f"The list remain same: {grid}")
    return grid
    print(f"sorting is completed")



numbers=[45,3,58,14,37,8,40]

print(f" buble sorted number list: {buble_sort(numbers)}")