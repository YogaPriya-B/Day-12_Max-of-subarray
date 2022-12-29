arr=list(map(int,input().strip().split()))
k=int(input())
l1=[]
c=len(arr)-(k-1)
for i in range(0,c):
   l=[]
   for j in range(0,k):
       l.append(arr[i+j])
   l1.append(max(l))
print(l1)
