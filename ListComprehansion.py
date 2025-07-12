# using for loop
a=[1,2,3,4,5]
arr=[]
for i in a:
    arr.append(i*2)
print(arr)    


## using list comprehandsion
ans=[i*2 for i in a ]
print (ans)


##  2d list comp




## matrix transposition
mat=[[1,2,3],
   [4,5,6]]
row=len(mat)
col=len(mat[0])
ans=[]
for j in range(col):
     temp=[]
     for i in range(row):
          temp.append(mat[i][j])
     ans.append(temp)    
print(ans)   


## using list comprensive
ans=[[mat[i][j]for i in range(row) ]for j in range(col)]
print(ans)


## 3d list comp hackrank rank
x = int(input())
y = int(input())
z = int(input())
n = int(input())
ans=[[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(ans)


