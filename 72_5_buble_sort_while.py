def bubble_sort_while(grid):
    print(f"Unsorted list is : {grid}")
    n=len(grid)
    i=0
    while i<(n-1):
        print(f"Round {i+1}: Comparing first {n-i} numbers:-")
        j=0
        while j<(n-1-i):
            print(f"comparing of {grid[j]} and {grid[j+1]}:")
            if grid[j]>grid[j+1]:
                print(f"{grid[j]} > {grid[j+1]}")
                print(f"{grid[j]}-----> {grid[j+1]} swap:")
                grid[j],grid[j+1]=grid[j+1],grid[j]
                print(f"The updated list is {grid}")
            else:
                print(f"{grid[j]} < {grid[j+1]}")
                print(f"No swap---> needed")
                print(f"List remain same: {grid}")
            j=j+1
        i=i+1
    print(f" _ "*20)
    return grid

numbers=[45, 3, 58, 14, 37, 8, 40]
print(f"Sorted numbers using while loop : {bubble_sort_while(numbers)}")