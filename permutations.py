a=int(input())
if a==1:
    print(1)
elif a==2 or a==3:
    print('NO SOLUTION')
elif a==4:
    print('3 1 4 2')
else:
    for i in range(1,a+1,2):
        print(str(i),end=' ')
    for i in range(2,a+1,2):
        print(str(i),end=' ')