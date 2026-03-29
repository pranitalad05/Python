# QUESTION 1 :

# Using for loop, write and run a Python program for this algorithm.
# Here is an algorithm to print out n! from 0! to 10!


num=int(input('Enter no : '))
fact=1
for i in range(num,1,-1):
    fact=fact*i
print(fact)


# =======================================================================================================


# QUESTION 2 :

# Count Digits, Even/Odd, Sum
# e.g. 23456
# output digits : 5
# sum : 20
# Even digits : 3
# odd digits :2


num=int(input('Enter no : '))
count=0
sum=0
even=0
odd=0

temp=num
while temp>0:
    digit=temp%10

    count+=1
    sum=sum+digit
    if digit%2==0:
        even+=1
    else:
        odd+=1
    temp=temp//10

print("count =", count)
print("sum =", sum)
print("even =", even)
print("odd =", odd)


# =======================================================================================================


# QUESTION 3 :

#  Find prime numbers between a given range - start(take start no) , end (take end number)


start=int(input('Enter start no : '))
end=int(input('Enter end no : '))
num=start

for num in range (start , end+1):
    is_prime=True
    if num>1:
        for i in range (2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime == True :
            print(num)


# =======================================================================================================


# QUESTION 4 :

# Write a python program to swap a 3 digit number
# input 321
# output 123


num=int(input('Enter no : '))
a=num//100
b=(num%100)//10
c=num%10
num=c*100+b*10+a
print(num)


# =======================================================================================================


# QUESTION 5 :

# Find LCM and GCD for given numbers [take 2 numbers] using loops only

a=int(input('Enter 1st no : '))
b=int(input('Enter 2nd no : '))
mn=min(a,b)

for i in range(1,mn+1):
    if a%i==0 and b%i==0:
        gcd = i
print("GCD : ",gcd)

mx=max(a,b)
while True:
    if mx%a==0 and mx%b==0:
        break
    mx+=1
print('LCM : ',mx)


# =======================================================================================================