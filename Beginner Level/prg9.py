n=int(input())
k=int(input())
sum=0
arr=[0]*n
for i in range(0,n):
    arr[i]=int(input())
for j in range(0,k):
    sum=sum+arr[j]
print(sum)
