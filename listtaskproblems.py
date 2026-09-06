#Find the Sum of List Elements
list=[1, 2, 3, 4, 5]
total=0
for i in list:
    total+=i
print(total)

#Find the Largest Element
numbers=[10, 25, 7, 42, 18]
largest=numbers[0]
for i in numbers:
    if i > largest:
        largest=i
print(largest)

#Q3. Count Even Numbers
list=[2,5,6,8,7,4,20,]
count=0
for i in list:
    if i % 2==0:
        count+=1 
print(count)

#Q4.Count Positive Numbers
numbers=[-2, 5, 7, -1, 3]
count=0
for i in numbers:
    if i > 0:
        count+=1
print(count)

#Q5.Reverse a List
list=[1, 2, 3, 4, 5]
reverse=[]
for i in range(4,-1,-1):
    reverse .append(list[i])
print(reverse)

#Q6.Find the Smallest Element
numbers=[5,3,7,2,9,6]
smallest=numbers[0]
for i in numbers:
    if i < smallest:
        smallest=i
print(smallest)

#Q7.Count Occurrences of an Element
list=[1, 2, 2, 3, 2, 4]
count=0
for i in list:
    if i == 2:
        count+=1
print(count)

#Q8.Print Odd Elements
numbers=[1, 2, 3, 4, 5]
for i in numbers:
    if i % 2!=0:
       print(i)

#Q9.Calculate the Average
numbers=[10, 20, 30, 40]
total=0
for i in numbers:
    total+=i
    average=total / len(numbers)
print(average)

#Q10.Check Whether an Element Exists
list=[10, 20, 30, 40]
for i in numbers:
    if i == 30:
        print("exist element")
        break

#Q11 Find the Second Largest Element
numbers=[15, 15, 10, 20, 5]
largest=numbers[0]
second=numbers[0]
for i in numbers:
    if i > largest:
        second=largest
        largest=i
    elif i > second and i != largest:
        second=i
print("second largest number",second)

#Q12.Remove Duplicate Elements
numbers=[1, 2, 2, 3, 1, 4]
result=[]
for i in numbers:
    if i not in result:
        result .append(i)
print(result)

#Q13.Move All Zeros to the End
numbers=[0, 1, 0, 3, 12]
result=[]
zero_count=0
for i in numbers:
    if i != 0:
        result.append(i)
    else:
        zero_count+=1
for i in range(zero_count):
    result.append(0)
print(result)

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

#Q15.Find Common Elements
list1= [1, 2, 3, 4]
list2= [3, 4, 5, 6]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print(common)

#Q16.Find the Majority Element
numbers=[2, 2, 1, 1, 1, 2, 2]
for i in numbers:
    count=0
    for j in numbers:
        if i==j:
            count+=1
    if count > len(numbers)//2:
        print("majority number",i)
        break

#Q17.Find the Pair With a Given Sum
numbers=[2, 7, 11, 15]
target=9
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], "+", numbers[j], "=", target)

#Q18.Separate Positive and Negative Numbers
numbers=[-2, 5, -7, 8, 0, 3]
positive=[]
negative=[]
for i in numbers:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
print("positive number",positive)
print("negative number",negative)
