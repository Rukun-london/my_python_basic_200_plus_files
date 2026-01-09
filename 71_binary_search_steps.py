#binary search of a number in a list, showing the steps
def binary_search_steps(grid,target):
    steps=1
    first,last=0,len(grid)-1
    while first<=last:
        print(f"Step : {steps}")
        print(f"First index : {grid[first]}")
        print(f"Last index : {grid[last]}")
        mid=(first+last)//2
        print(f"Middle index : {grid[mid]}")
        if grid[mid]==target:
            print(f" Both the middle index : {grid[mid]} and target : {target} are the same")
            print(f"So the target found at index {mid}")
            return mid
            steps+=1
        elif grid[mid]>target:
            print(f"middle index {grid[mid]} is greater than target {target}, so target {target} should be found on the left")
            last=mid-1
        else:
            print(f"Middle index {grid[mid]} is less than target {target}, so target {target} should be found on the right")
            first=mid+1
        steps+=1
    return -2

nums=[3,5,8,12,18,25,36,40]
find=int(input("target number: "))
if binary_search_steps(nums,find)== -2:
    print(f"Target number {find} is not in the list. ")