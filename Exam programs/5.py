n=int(input("Enter the number of rows :"))
for r in range(n):
    print(' '*(n-r),end=' ')
    print(' '.join(map(str,str(11**r))))
