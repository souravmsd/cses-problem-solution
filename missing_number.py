a=int(input())
l=input().split()
sum1=(a*(a+1))/2
sum2=0
for i in range(a-1):
    sum2=sum2+int(l[i])
print(int(sum1-sum2))
