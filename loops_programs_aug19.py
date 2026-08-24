#1
n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
print()

#2
m=3
n=7
for i in range(m,n+1):
    print(i,end=" ")
print()

#3
n=5
for i in range(n,0,-1):
    print(i,end=" ")
print()

#4
n=10
m=6
for i in range(n,m-1,-1):
    print(i,end=" ")
print()

#5
n=5
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#6
n=5
f=1
for i in range(1,n+1):
    f=f*i
print(f)

#7
m=3
n=6
sum=0
for i in range(m,n+1):
    sum=sum+i
print(sum)

#8
m=2
n=4
p=1
for i in range(m,n+1):
    p=p*i
print(p)

#9
n=6
for i in range(1,n+1):
    if n%i==0:
        print(i)

#10
n=6
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
print(count)

#11
n=7
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Not Prime")

#12
m=3
n=10
for i in range(m,n+1):
    if i%2==0:
        print(i)

#13
m=3
n=10
for i in range(m,n+1):
    if i%2!=0:
        print(i)

#14
m=3
n=7
even=0
odd=0
for i in range(m,n+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even =",even)
print("Odd =",odd)

#15
s="hello"
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print()

#16
s="madam"
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
if s==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#17
n=123
sum=0
for i in range(3):
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)

#18
n=123
p=1
for i in range(3):
    digit=n%10
    p=p*digit
    n=n//10
print(p)

#19
n=153
temp=n
total=0
for i in range(3):
    digit=temp%10
    total=total+digit**3
    temp=temp//10
if total==n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#20
n=123
temp=n
rev=0
for i in range(3):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
print(rev)

#21
n=121
original=n
temp=n
rev=0
for i in range(3):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if original==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#22
s="apple"
count=0
for ch in s:
    if ch in "aeiou":
        count=count+1
print(count)

#23
s="apple"
count=0
for ch in s:
    if ch.isalpha() and ch not in "aeiou":
        count=count+1
print(count)

#24
s="apple"
vowels=0
consonants=0
for ch in s:
    if ch in "aeiou":
        vowels=vowels+1
    elif ch.isalpha():
        consonants=consonants+1
print("Vowels =",vowels)
print("Consonants =",consonants)

#25
n=28
total=0
for i in range(1,n):
    if n%i==0:
        total=total+i
if total==n:
    print("Perfect Number")
else:
    print("Not Perfect")

#26
n=9
square=n*n
total=0
for i in range(2):
    digit=square%10
    total=total+digit
    square=square//10
if total==n:
    print("Neon Number")
else:
    print("Not Neon")

#27
n=145
temp=n
total=0
for i in range(3):
    digit=temp%10
    fact=1
    for j in range(1,digit+1):
        fact=fact*j
    total=total+fact
    temp=temp//10
if total==n:
    print("Strong Number")
else:
    print("Not Strong")

#28
n=18
temp=n
total=0
for i in range(2):
    digit=temp%10
    total=total+digit
    temp=temp//10
if n%total==0:
    print("Harshad Number")
else:
    print("Not Harshad")

#29
n=5
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c

#30
n=9
square=n*n
total=0
for i in range(2):
    digit=square%10
    total=total+digit
    square=square//10
if total==n:
    print("Neon Number")
else:
    print("Not Neon")
