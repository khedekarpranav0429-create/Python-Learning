data = [23,56,12,78,34,5]
i=0 
j=len(data)-1
print(j)
temp=0
while(i<j):
    temp=data[i]
    data[i]=data[j]
    data[j]=temp
    i=i+1
    j=j-1
print(data)
