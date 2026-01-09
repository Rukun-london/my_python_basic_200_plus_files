def list_operation(num:list ):
    return {
        "sum" : sum(num),
        "average":sum(num)/len(num),
        "max":max(num),
        "min":min(num),
        "count":len(num),
        "sorted": sorted(num),
        "reversed": num[::-1]
    }
num=[2,5,3,9,6,4]
result=list_operation(num)
print(f" list operation are: {result}")
for key, value in result.items():
    print(f"{key}: {value}")


