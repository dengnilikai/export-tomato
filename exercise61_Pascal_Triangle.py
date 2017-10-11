#encoding=UTF-8
'''
题目：打印出杨辉三角形（要求打印出10行）。
思路：每个数等于它上方两数之和
'''


a=[]
rownum=10
for i in range(rownum):
    a.append([])
    for j in range(i+1):
        if j!=0 and j!=i:
            a[i].append(a[i-1][j-1]+a[i-1][j])
        else:
            a[i].append(1)
        print("%d\t"%(a[i][j]),end='')
    print()
for i in range(rownum):
    del a[rownum-i-1]
del a
