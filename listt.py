'''
#Given a list of integers,
find and print the sum of all elements in the list.

l=[1,2,3,4,5]
sum=0
for i in l:
    sum+=i
print(sum)

 
#Given a list of integers, find and print the largest element

while True:
    l = list(map(int, input("Enter numbers: ").split()))
    l1=l[0]
    for i in l:
        if i>l1:
            l1=i
    print(l1)
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break

#Given a list of integers, count the number of even elements.

while True:
    n=list(map(int,input("enter number:").split()))
    count=0
    for i in n:
        if i%2==0:
            count+=1
    print(count)
    
    n=input("enter the input:")
    if n="yes":
        continue
    else:
        break
        
#Count Positive Numbers       
while True:
    n=list(map(int,input("enter the numbers:").split()))
    count=0
    for i in n:
        if i>0:
            count+=1
    print(count)
    n1=input("enter the yes/no:")
    if n1=="yes":
        continue

    else:
        break


#Reverse a List

while True:
    n=list(map(int,input("enter the numbers:").split()))
    rev=[]
    for i in range(len(n)-1,-1,-1):
        rev.append(n[i])
    print(rev)
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break
enter the numbers:1 2 3 4 5
[5, 4, 3, 2, 1]
enter the yes/no:yes
enter the numbers:10 20 30
[30, 20, 10]
enter the yes/no:yes
enter the numbers:7 8 
[8, 7]

#Find the Smallest Element
while True:
    l = list(map(int, input("Enter numbers: ").split()))
    l1=l[0]
    for i in l:
        if i<l1:
            l1=i
    print(l1)
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break
Enter numbers: 8 3 12 5 1
1
enter the yes/no:yes
Enter numbers: 20 15 30 10
10
enter the yes/no:yes
Enter numbers: -5 -2 -10 -1
-10

#Count Occurrences of an Element
while True:
    l=list(map(int,input("enter the number:").split()))
    t=int(input("enter  the target:"))
    count=0
    for i in l:
        if t==i:
            count+=1
    print(count)
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break
enter the number:1 2 3 2 2 4
enter  the target:2
3
enter the yes/no:yes
enter the number:5 5 1 2 5 
enter  the target:5
3
enter the yes/no:yes
enter the number:10 20 30
enter  the target:5
0

#Print Odd Elements:

while True:
    n=list(map(int,input("enter number:").split()))
    l=[]
    for i in n:
        if i%2!=0:
            l.append(i)
    print(l)
    
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break
enter number:1 2 3 4 5
[1, 3, 5]
enter the yes/no:yes
enter number:10 15 20 25 30
[15, 25]
enter the yes/no:yes
enter number:2 4 6 8
[]

#Calculate the Average
while True:
    n=list(map(int,input("enter the numbers:").split()))
    l=len(n)
    sum=0
    for i in n:
        sum+=i
        avg=sum/l
    print(avg)
    n1=input("enter the yes/no:")
    if n1=="yes":
        continue
    else:
        break
enter the numbers:10 20 30 40
25.0
enter the yes/no:yes
enter the numbers:5 10 15
10.0
enter the yes/no:yes
enter the numbers:2 4
3.0

#Check Whether an Element Exists
while True:
    l=list(map(int,input("enter the number:").split()))
    t=int(input("enter  the target:"))
    count=0
    for i in l:
        if t==i:
            True
    print(True)
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break
        
# Find the Second Largest Element:

while True:
    l = list(map(int, input("Enter numbers: ").split()))
    l1=float("-inf")
    s1=float("-inf")
    for i in l:
        if i>l1:
            s1=l1
            l1=i
        elif i>s1 and i!=l1:
            s1=i
    print(s1)
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break
Enter numbers: 10 20 5 30 25
25
enter the yes/no:yes
Enter numbers: 4 8 2 10 6
8
enter the yes/no:yes
Enter numbers: 15 15 10 20 5
15

Remove Duplicate Elements:

while True:
    l=list(map(int,input("enter the number:").split()))
    rev=[]
    for i in range(len(l)):
        if l[i] not in rev:
            rev.append(l[i])
    print(rev)
    n=input("enter the yes/no:")
    if n=="no":
        break
enter the number:1 2 2 3 1 4
[1, 2, 3, 4]
enter the yes/no:yes
enter the number:5 5 5 2 2 1
[5, 2, 1]
enter the yes/no:yes
enter the number:10 20 10 30 20
[10, 20, 30]

#Move All Zeros to the End:

l=list(map(int,input("enter the number:").split()))
l1=[]
count=0
for i in l:
    if i!=0:
        l1.append(i)
    else:
        count+=1
for i in range(count):
    l1.append(0)
print(l1)

enter the number: 0 1 0 3 12 0
[1, 3, 12, 0, 0, 0]

#Find the Missing Number:

l=list(map(int,input("enter the number:").split()))
for i in range(len(l)+1):
    if i not in l:
        print(i,end=" ")

#Q14.Find the Missing Number
numbers=[9, 6, 4, 2, 3, 5, 7, 0, 1]
n=10
total=0
for i in range(n):
    total+=i
actual=0
for i in numbers:
    actual+=i
missing=total-actual
print("missing numbers",missing)

        
#Q15 Find Common Elements
l=list(map(int,input("enter the number:").split()))
l1=list(map(int,input("enter the number:").split()))
l2=[]
for i in l:
    for j in l1:
        if i==j:
            l2.append(i)
print(l2)


#nested list:
lis=[[1,2,3],[2,3,4],[4,5,6],31,(1,2)]
r=[]
for i in range(len(lis)):
    if type(lis[i])==list:
        for j in range(len(lis[i])):
            r.append(lis[i][j])
    elif type(lis[i])==tuple:
        for k in range(len(lis[i])):
            r.append(lis[i][k])
    else:
        r.append(lis[i])
print(r)



l=[[1,2,3],[2,3,4],[1,2,3],[1,2,3,[1,2,3],31]]
r=[]
for i in range(len(l)):
    if type(l[i])==list:
        for j in range(len(l[i])):
            if type(l[i][j])==list:
                for k in range(len(l[i][j])):
                    r.append(l[i][j][k])
            else:
                r.append(l[i][j])
                
    else:
        r.append(l[i])
print(r)
[1, 2, 3, 2, 3, 4, 1, 2, 3, 1, 2, 3, 1, 2, 3, 31]

#Find the Majority Element:
l=list(map(int,input("enter the numbers:").split()))
majorit=0
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if l[i] not in l[:i]:
        print(l[i],count)
if count>majorit:
    print("majority number:",l[i])
enter the numbers:1 2 3 3 2 3
1 1
2 2
3 3
majority number: 3   
        

#the Pair With a Given Sum

l=list(map(int,input("enter the numbers:").split()))
target=9
l2=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            l2.append(l[i])
            l2.append(l[j])
print(l2)

enter the numbers:2 7 11 15
[2, 7]

while True:
    l=list(map(int,input("enter the number:").split()))
    pos=[]
    neg=[]
    for i in range(len(l)):
        if l[i]>0:
            pos.append(l[i])
        else:
            neg.append(l[i])
    print("positive:",pos)
    print("negitive:",neg)
    
    n=input("enter the yes/no:")
    if n=="yes":
        continue
    else:
        break
enter the number:-2 5 -7 8 0 3
positive: [5, 8, 3]
negitive: [-2, -7, 0]
enter the yes/no:yes
enter the number:10 -5 -2 7 4
positive: [10, 7, 4]
negitive: [-5, -2]
enter the yes/no:yes
enter the number:-1 -2 -3
positive: []
negitive: [-1, -2, -3]

#the First Repeated Element
l=list(map(int,input("enter the number:").split()))
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if count>1:
        print(l[i],count)
        break
enter the number:1 2 3 4 2 5
2 2

Rotate a List to the Right       
l=[1,2,3,4,5]
k=2
for i in range(k):
    x=l.pop()
    l.insert(0,x)
print(l)
[4, 5, 1, 2, 3]

#Rotate a List to the left:
l=[1,2,3,4,5]
k=2
for i in range(k):
    x=l.pop(0)
    l.append(x)
print(l)'''

        





