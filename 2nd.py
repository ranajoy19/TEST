'''
0
1 4
5 8 12
13 16 20 25
26 29 33 38 44
'''
n=int(input("enter the column number:"))
per_line=1
root=0
for i in range(n):
    inc=3
    for j in range(per_line):
        if j==0:
            print(root,end=' ')
        else:
            root+=inc
            print(root,end=' ')
            inc+=1
    root+=1
    per_line+=1
    print()
