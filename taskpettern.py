'''Nested for Loop — Easy Level Practice Questions

1. Print the following numbers using nested for loops:

1 2 3
1 2 3
1 2 3
n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()

2. Print the following:

* * *
* * *
* * *


3. Print numbers from 1 to 5 in 3 rows:

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
n=3
m=5
for i in range(1,n+1):
    for j in range(1,m+1):
        print(j,end="")
    print()

4. Print the following pattern:

1 1 1
2 2 2
3 3 3
n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()

5. Print the following pattern:

1 2
1 2
1 2
1 2
n=4
m=2
for i in range(1,n+1):
    for j in range(1,m+1):
        print(j,end="")
    print()


6. Print a 4 × 4 square of *:

* * * *
* * * *
* * * *
* * * *


7. Print the multiplication tables from 1 to 3, with each table containing numbers from 1 to 5.
n=3
m=5
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i*j,end="")
    print()

8. Print all numbers from 1 to 9 in the following format:

1 2 3
4 5 6
7 8 9
n=3
num=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(num,end=" ")
        num+=1
    print()


9. Print the following pattern:

A A A
B B B
C C C
n=3
char=65
for i in range(0,n):
    for j in range(0,n):
        print(chr(char+i),end="")
    print()

10. Print the following pattern:



A B C
A B C
A B C

11. Print the numbers from 1 to 4 in 4 rows, where each row contains the same number.


12. Print the following pattern:



* *
* *
* *
* *
* *

13. Print a 5 × 5 grid containing numbers from 1 to 5 in every row.


14. Print the following pattern:



1
2 2
3 3 3
n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
15. Print the following pattern:



*
* *
* * *

16. Print the following pattern:



1
1 2
1 2 3
n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
    

17. Print the following pattern:



A
A B
A B C

n=3
char=65
for i in range(1,n+1):
    for j in range(0,i):
        print(chr(char+j),end="")
    print()
        

18. Print the following pattern:



1 2 3 4
1 2 3
1 2
1
n=4
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(j,end="")
    

19. Print the following pattern:



* * * *
* * *
* *
*
n=5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("*",end="")
    print()

20. Print the following pattern:



1
2 3
4 5 6


n=3
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
    
21. Print a 3 × 3 multiplication table.


22. Print the following:



1 2 3 4
2 3 4 5
3 4 5 6

n=3
m=4
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i*j,end="")
    print()

23. Print the following:



5 5 5 5
4 4 4 4
3 3 3 3
2 2 2 2
1 1 1 1

n=5
m=4
for i in range(n,0,-1):
    for j in range(m,0,-1):
        print(i,end="")
    print()
    
24. Print the following pattern:
A B
C D
E F
n=3
m=2
char=65
num=0
for i in range(0,n):
    for j in range(0,m):
        print(chr(char+num),end="")
        num+=1
    print()
25. Print a rectangle of * having 3 rows and 5 columns.
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()
    '''