#62_hcf_using_Euclidean_rule
# Highest common factor of 12 and 18 is 6
def hfc(a,b):
    while b:
        a,b=b,a%b
    return a

print(hfc(12,18))


