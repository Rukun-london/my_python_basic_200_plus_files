n1=0
n2=1
i=1
while i <= 10:
    if i==10:
        print (n1)
        break
    else:
        nxt=n1 + n2
        print(n1, end=' , ')
        n1=n2
        n2=nxt
        i=i+1