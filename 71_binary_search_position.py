#search for the position of a value in a list
#binary search only works on a sorted list

def binary_search(numbers,target):
    first=0
    last=len(numbers)-1
    while first<=last:
        mid=(first+last)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            first=mid+1
        else:
            last=mid-1
    return -1


targ=int(input("Enter the target number : "))
grid=[4,9,31,2,6,22,8,2,49,12,25,11,7]
grids=sorted(grid)
print(f"Sorted grids : {grids}")
position=binary_search(grids,targ)
if position!=-1:
    print(f"The target number is at index : ", position)
else:
    print(f"The target number is not found.")