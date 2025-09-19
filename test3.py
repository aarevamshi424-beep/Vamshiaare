#wap to product of 2 matrices
l=[]
n=2
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
print(l)
#wap to get nearest prime number
def isprime(n):
    if n<2:return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input('enter a number:'))
if isprime(n):
    print(n)
else:
    left=n-1
    right=n+1
    while True:
        if isprime(left):
            print(left)
            break
        if isprime(right):
            print(right)
            break
        left -= 1
        right += 1
#wap to print hallow diamond
n=5
for i in range(1,n+1):
    print(' '*(n-i),end='')
    if i==1:
        print('*')
    else:
        top=2*i-3
        print('*' + ' '* top + '*')
for i in range(n-1,0,-1):
    print(' ' * (n-i),end='')
    if i==1:
        print('*')
    else:
        bottom=2*i-3
        print('*' + ' ' * bottom + '*')
#wap for replace built in function of string
s='iam a java trainer'
old="java"
new="python"
print(s.replace(old,new))

