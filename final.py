
n = int(input("enter no: "))
sq=lambda s:s**2
sr=[]
sr.append(sq(n))
print(sr)

n=3
for i in range(1,n+1):
     print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1): 
     print(" "*(n-i)+"*"*(2*i-1))
print()

for i in range(1,51):
    if i%5==0:
       print(i)

um=[23,45,7,9,89]
no=list(map(int,input("enter no").split()))
total=[]
for i in no:
   if  i in um:
     total.append(i)
print(total)

no=30
for i in range(5,35,5):
      print(i)

#no=int(input("enter no"))
i=1
while i<=10:
  print("6x",i,"=",6*i)
  i+=1

text=input("enter string")
vowels='aeiou'
result=''
for char in text:
    if not char in vowels:
        result+=char
print(result)
        
text=input("enter string").split()
count=0
for word in text:
    if word==word[::-1]:
        count+=1
print(count)

no=input("enter no")
digits=list(map(int,no))
print(min(digits))
print(max(digits))

no=int(input("enter no"))
fact=1
for i in range(1,no+1):
  fact*=i
  print(fact)

no=input("enert no")
digit=list(map(int,no))
odd=0
even=0
for num in digit:
    if num%2==0:
      even+=1
    else:
      odd+=1
print(even)
print(odd)

a=int(input("emeter no"))
b=int(input("emeter no"))
while b!=0:
    a,b=b,a%b
print(a)

text=input("enter string")
word=text[::-1]
print(word)

text=input("enter string").split()
pali=[]
for word in text:
    if word == word[::-1]:
        pali.append(word)
print(pali)

no=int(input("enter no"))
if no>=1:
    print("positive")
else:
    print("negative")

digits=list(map(int,input("enter no").split()))
pos=0
neg=0
for digit in digits:
 if digit>=0:
    pos+=1
 else:
    neg+=1
print(pos)
print(neg)


no=list(map(int,input("entr no").split()))
print(min(no))
print(max(no))

a=int(input("enter no"))
b=int(input("enter no"))      
c=int(input("enter no"))
if (a>b) and (a>c):
      print(a)
elif (b>a) and(b>c):
      print(b)
else:
      print(c)

no=input("enter string")
if no== no[::-1]:
 print("palin")
else:
 print("not pali")

no=list(map(int,input("enter no").split()))
if 20 in no:
    print("present")

n=1
while n<=5:
   print(n)
   n+=2
      
no=list(map(int,input("enter no").split()))
total=0
for num in no:
    total+=num
print(total)

mark1=int(input("enter mark"))
mark2=int(input("enter mark"))
mark3=int(input("enter mark"))
total=mark1+mark2+mark3
print(total)
percent=(total/300)*100
print(percent)
average=total/3
print(average)

def fact(no):
    fact=1
    for i in range(1,no+1):
       fact*=i
    return fact
no=int(input("enter no"))
print(fact(no))

for i in range(1,51):
    if i%5==0:
        print(i)

no=list(map(int,input("enter no").split()))
sq=lambda s :s**2
sr=[]
for num in no:
    sr.append(sq(num))
print(no)
print(sr)


no=list(map(int,input("enter no").split()))
big=lambda s: s in no
res=max(no)
print(res)

n = int(input("enter no: "))
for i in range(n,0,-1):
    for j in range(1, i+ 1):
        print(j, end=" ")
    print()


n = int(input("enter no: "))
total=0
for i in range(1,n+1):
    total+=2*i-1
print(total)

senten="madam level high "
word=senten.split()
tt=[]
count=0
for words in word:
    if words == words[::-1]:
        tt.append(words)
        count+=1
print(tt)
print(count)

text=input("enter string")
vowels='aeiouAEIOU'
v=0
c=0
for char in text:
  if char.isalpha():  
    if char in vowels:
        v+=1
    else:
        c+=1
print(v)
print(c)

no1=list(map(int,input("enter no").split()))
no2=list(map(int,input("enter no").split()))
common=[]
for list in no1:
    if list not in no2:
        common.append(list)
for list in no2:
    if list not in no1:
        common.append(list)
print(common)


no=list(map(int,input("enter no").split()))
even=[]
odd=[]
for i in no:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
print(len(even))
print(len(odd))

no=list(map(int,input("enter no").split()))
if no[0]>no[1]:
    large=no[0]
    snd=no[1]
else:
     large=no[1]
     snd=no[0]
for i in no[2:]:
   if i>large:
       snd=large
       large=i
   elif i>snd:
       snd=i
print(large)
print(snd)

words="apple cat baba zebra monkey"
word=words.split()
sort=sorted(word,key=len)
print(sort)

no=int(input("enter no"))
if no<1:
    print("not prime")
else:
    for i in range(2,int(no**0.5)+1):
        if no%i==0:
            print("not prime")
            break
    else:
            print("prime")

no=int(input("enter no"))
pri=[]
notpri=[]
for no in range(1,no+1):
    if no<=1:
        notpri.append(no)
        continue
    else:
        for i in range(2,int(no**0.5)+1):
            if no%i==0:
                notpri.append(no)
                break
        else:
             pri.append(no)

print(pri)
print(notpri)

no=list(map(int,input("enter no").split()))
pri=0
notpri=0
if no<=1:
        notpri+=1
        continue
else:
        for i in range(2,int(no**0.5)+1):
            if no%i==0:
                notpri+=1
                break
        else:
             pri+=1

print(pri)
print(notpri)

num=int(input("enter no"))
total=0
while num>0:
        total+=num%10
        num//=10
print(total)

no=int(input("enter no"))
fact=1
sum=0
for i in range(1,no+1):
  fact*=i
  sum+=fact
print(fact)
print(sum)

no=int(input("enter no"))
temp=no
sumfact=0
while temp>0:
        total=temp%10
        fact=1
        for i in range(1,total+1):
                fact*=i
        sumfact+=fact
        temp//=10
                
if sumfact == no:
    print("Strong number")
else:
    print("Not a Strong number")

no=int(input("enter no"))
temp=no
n=len(str(temp))
arm=0
while temp>0:
        digit=temp%10
        arm+=int(digit)**n
        temp//=10
if arm == no:
    print("arm number")
else:
    print("Not a arm number")

def show(a):
    print("value:",a)
show(100)


show=lambda a:print("value:",a)
show(100) 

k=[10,20,13,19,14,24,29,30]
res=[]
n=len(k)
for i in range(n):
    if k[i]%2==0:
        res.append(k[i])
print("normal function:",res)

res=list(filter(lambda s:s%2==0,k))
print("lambda function:",res)

print(list(filter(lambda s:s%2==1,k)))

res=list(map(lambda m:m+10,k))
print(res)


n = 4
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
      
n = 4
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()    

class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Year: {self.year}")
car1 = Car("Honda", "City", 2020)
car2 = Car("Tata", "Nexon", 2022)
car1.display_details()
car2.display_details()














