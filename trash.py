#3.20
print("Hello World")
s="Hello World!"
for i in s:
    print(i)
s="wwwwwwwwwwwwwwwww"
for i in s:
    print(i)
s="A B C D E"
print(s)
s="A,B,C,D,E"
print(s)
s="A-B-C-D-E"
print(s)
for i in range(10):
    print(i,end=' ')
for i in range(10):
    print(i,end=',')

#3.27
#1
print(round(((float(input()))**2)*3.14,2))

#2
a=float(input())
b=float(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#3
print(round(2*3.14*(5**2)+2*3.14*5*10,2))

#4
a = input().split(',')
b = [float(i) for i in a]
b.sort()
print(b[-1])

#5
a = input().split(',')
b = [float(i) for i in a]
b.sort()
print(abs(b[0]))

#6
a = input().split(',')
b = [float(i) for i in a]
print(tuple([(b[0]//b[1]),(b[0]%b[1])]))

$7
from math import *
n = int(input())
j = 0
for i in range(1,n+1):
  j += factorial(i)

print(j)
