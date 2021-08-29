a=input()
b=len(a)
count=0
max_count=0
for i in range(b-1):
    if a[i]==a[i+1]:
        count=count+1
    else:
        count=0
    if max_count<count:
        max_count=count
print(max_count+1)        

