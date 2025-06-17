l1=[10,20,30]
print(l1)

l1=[]
print(l1)

l1=[3.5,True,'abc']
print(l1)

## access list ele
l1=[50,20,80,10,60,40]
print(l1)
print(l1[0])
print(l1[1],l1[2])

## neg idx
print(l1[-1])
print(l1[-2])

## accessing list ele via for loop
for x in l1:
    print(x,end=' ')
print()  ## print new line


## while loop in list
i=0
while i<6:
    print(l1[i],end=' ')
    i+=1  
