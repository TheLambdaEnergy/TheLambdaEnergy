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

#2026.4.3
#1
for num in range(100, 1000):
    a = num // 100         
    b = (num // 10) % 10    
    c = num % 10            
if a**3 + b**3 + c**3 == num:
    print(num, end=" ")

#2
n = int(input())
j = [i for i in range(1,n) if i%3==0 and i%5==0]
if len(j) == 0:
    print("10以内没有3和5的最小公倍数")
else:
    print("{}以内存在3和5的最小公倍数，该数是{}".format(str(n),str(j[0])))

#3
n = int(input())
denom = [1, 2]
for i in range(2, n):
    denom.append(denom[-1] + denom[-2])

total = 0.0
for i in range(n):
    if i == 0:
        numerator = 1
    else:
        numerator = i
    if i % 2 == 0:
        total += numerator / denom[i]
    else:
        total -= numerator / denom[i]

print("{:.6f}".format(total))

#4
s = input().split(',')
x = int(s[0])
y = int(s[1])
r = 0

for i in range(1,max([int(j) for j in s])):
  if x%i == 0 and y%i == 0:
    r += i

print(r)

#5
n = int(input())
if n == 1 or n == 2:
    total = 1
else:
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    total = b
print(f"该月兔子的总对数是: {total}")

#6
print('''1*1= 1 
2*1= 2 2*2= 4 
3*1= 3 3*2= 6 3*3= 9 
4*1= 4 4*2= 8 4*3=12 4*4=16 
5*1= 5 5*2=10 5*3=15 5*4=20 5*5=25 
6*1= 6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 
7*1= 7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 
8*1= 8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 
9*1= 9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81''')

#4.10
#1
def p(num):
    if num<2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True

def find_next_prime(n):
    candidate=n+1
    while True:
        if p(candidate):
            return candidate
        candidate+=1

n=int(input())
next_prime=find_next_prime(n)
print(f"大于n的最小的素数是{next_prime}")

#2
t=float(input())

def e_approx(t):
    e=1
    term=1
    n=1
    while term>=t:
        term/=n
        e+=term
        n+=1
    return e

print(f"{e_approx(t):.8f}")

#3
def p(num):
    if num<2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True

N=int(input())
count=0
num=2
total=0
while count<N:
    if p(num):
        total+=num
        count+=1
    num+=1
print(total)

#4
m,w=eval(input())
if m<=3:
    f=13
elif m<=15:
    f=13+(m-3)*2.3
else:
    f=13+(15-3)*2.3+(m-15)*2.3*1.5
f+=w
print(f"车费为 {f:.2f}")

#4.17
#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def print_palindrome_prime(n):
    if str(n) == str(n)[::-1]:
        if is_prime(n):
            print("{}是回文素数".format(n))

num = int(input("请输入一个数："))
for i in range(num):
    print_palindrome_prime(i)

#2
def find_self_power_numbers(n):
    print(n, "位的自幂数有：",sep="")
    start = 10**(n - 1)
    end = 10**n
    for num in range(start, end):
        temp = num
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** n
            temp //= 10
        if total == num:
            print(num)
 
n_input = int(input())
find_self_power_numbers(n_input)

#3
import math
 
def sqrt_binary(n, error):
    low = 0.0
    high = n + 0.25
    while True:
        mid = (low + high) / 2
        if abs(mid * mid - n) <= error:
            return mid
        if mid * mid < n:
            low = mid
        else:
            high = mid
 
input_data = input().split(',')
n = float(input_data[0])
error = float(input_data[1])
 
result1 = sqrt_binary(n, error)
result2 = math.sqrt(n)
 
print("%.8f" % result1)
print("%.8f" % result2)

#4
def solve_apples(n,c):
  if n == 0:
    print("苹果总数为",c,"个",end="")
    return c
  print("卖完第",n,"家，苹果剩余数为",c,"个",end="")
  pl = c*2+1
  return solve_apples(n-1,pl)

solve_apples(5,8)
