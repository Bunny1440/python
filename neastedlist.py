'''#1. Print Every Element One by One
numbers = [[1,2],[3,4],[5,6]]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j])
        
#2. Print Each Inner List:
numbers = [[10, 20], [30, 40], [50, 60]]
for i in range(len(numbers)):
    print(numbers[i])

#3.Find how many elements are present in the entire nested list. 
numbers=[[1,2,3],[4,5,],[6,7,8]]
count=0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        count+=1
print("no.of elements:",count)

#4. Calculate Sum of All Elements:
numbers=[[1,2],[3,4],[5,6]]
sum=0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        sum+=numbers[i][j]
print(sum)

#Find the largest number from the entire nested
numbers=[[10,5],[25,15],[8,30]]
lar=float("-inf")
for i in numbers:
    for j in i:
        if j>lar:
            lar=j
print(lar)

#Find the smallest number from the nested 
numbers=[[10,5],[25,15],[8,30]]
small=float("inf")
for i in numbers:
    for j in i:
        if j<lar:
            small=j
print(small)

#7. Count Even Numbers :
numbers = [[1, 2, 3], [4, 5, 6], [7, 8]]
count=0
for i in numbers:
    for j in i:
        if j%2==0:
            count+=1
print(count)

#9. Search for an Element:

numbers = [[10, 20], [30, 40], [50, 60]]
search=40
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j]==search:
            print("found:",numbers[i][j])
        
#10.Count how many times a particular number :
numbers = [[1, 2, 2], [3, 2, 4], [2, 5]]
search = 2
count=0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j]==search:
            count+=1
print("search element:",search,"count:",count)

#11)Print the first element from each inner list
numbers = [[10, 20], [30, 40], [50, 60]] 
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j])
        break   

#12)Print the last element from each inner list.
numbers = [[10, 20], [30, 40], [50, 60]] 
for i in range(len(numbers)):
    for j in range(len(numbers[i])-1,-1,-1):
        print(numbers[i][j])
        break 

#13)Calculate the sum separately for every inner list
numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]
for i in range(len(numbers)):
    sum=0
    for j in range(len(numbers[i])):
        sum+=numbers[i][j]
    print(sum)


#14)Find the largest element from each inner list.
numbers = [[10, 20, 5], [30, 15], [8, 25, 12]]

for i in range(len(numbers)):
    lar=float("-inf")
    for j in numbers[i]:
        if j>lar:
            lar=j
    print(lar)

#15)Find the smallest element from each inner list.
numbers = [[10, 20, 5], [30, 15], [8, 25, 12]]
for i in range(len(numbers)):
    lar=float("inf")
    for j in numbers[i]:
        if j<lar:
            lar=j
    print(lar)

#16)Print all positive numbers from the nested
numbers = [[-2, 5, -8], [10, -3, 7], [-1, 4]] 
for i in range(len(numbers)):
    for j in numbers[i]:
        if j>0:
            print(j)
#17)Print all numbers greater than 10
numbers = [[5, 15, 20], [8, 25], [30, 3]]
for i in range(len(numbers)):
    for j in numbers[i]:
        if j>10:
            print(j)
#18)the average of all numbers in the nested list.
numbers = [[10, 20], [30, 40]]
l=len(numbers)
sum=0
count=0
for i in range(len(numbers)):
    for j in numbers[i]:
        sum+=j
        count+=1
avg=sum/count
print(avg)'''