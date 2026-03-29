                                               # Strings


# QUESTION 1 :

# Write a program that asks the user how many days are in a particular month, and
# what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then
# prints a calendar for that month. For example, here is the output for a 30-day month that begins on day 3 (Thursday):
# M  T  W  T  F  S  S
#       	 1  2  3  4
# 5  6  7  8  9 10 11


days=int(input('Enter no of days :'))
start=int(input('enter the day where you want to start :'))

my_str="M\tT\tW\tT\tF\tS\tS"
print(my_str)
for i in range(start):
    print('\t',end='')

for i in range(1,days+1):
    print(i,end='\t')

    if (start+i)%7==0:
        print()


# =======================================================================================================

# QUESTION 2 :

# Check if all letters in a string are uppercase


my_str=input('Enter the string : ')
print(my_str)
is_upper=True
my_str=my_str.replace(' ','')
for ch in my_str:
    if not 'A'<=ch<='Z':
        is_upper = False

print(is_upper)


# =======================================================================================================

# QUESTION 3 :

# Write a version of a palindrome recognizer
# that also accepts phrase palindromes such as : Was it a rat I saw? or
# Dammit, I'm mad! Note that punctuation, capitalization, and spacing are usually ignored.


my_str=input('Enter string : ')
print(my_str)
new_str=''
for ch in my_str:
    if ch.isalpha():
        new_str+=ch

new_str=new_str.lower()
print(new_str)

if new_str==new_str[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')


#Another Way
cleaned=[ch.lower() for ch in my_str if ch.isalpha()]
print(''.join(cleaned))
if cleaned==cleaned[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')


# =======================================================================================================
# =======================================================================================================

                                          # Lists and Tuple


# QUESTION 1 :

# Write a Python function that takes a list of words and returns the length of the longest one

def longest_word_length(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length
words = input("Enter words separated by space: ").split()

print("List of words:", words)

print("Length of longest word:", longest_word_length(words))


# =======================================================================================================

# QUESTION 2 :

# Write a Python program to remove duplicates from a list


num=int(input("Enter the no of words : "))
words=[]
for i in range(1,num+1):
    word=input(f"Enter the {i} word : ")
    words.append(word)
print(words)

u_words = []
for word in words:
    if word not in u_words:
        u_words.append(word)

print("List after removing duplicates : ", u_words)


# =======================================================================================================

# QUESTION 3 :

# Create a list of books
# e.g. booklist =[['Java 8', 700], ['Python for Beginners', 500],....]

# Perform following operations on the list
# 1. Add a new book with price
# 2. Remove entry for a book
# 3. update price for a book
# 4. Sort the list by book names
# 5. Sort the list by prices
# 6. Print the book with max and min price [hint : you may use min()/max() functions of python]


booklist=[]
num=int(input('No of books you want to add : '))

for i in range(num):
    name=input('Book Name : ')
    price =int(input('Price : '))
    booklist.append([name,price])

booklist=[['Java 8',700],['Python',500], ['C++', 555]]
print(booklist)


# 1
booklist.append(['C++',400])
print(booklist)


# 2
for book in booklist :
    if book[0]=='C++':
        booklist.remove(book)
        break
print("After removing : ", booklist)


# 3
for book in booklist:
    if book[0]=='Java 8':
        book[1]=788
        break
print("After updating price : ",booklist)


# 4
def sort_name(book):
    return book[0]
booklist.sort(key=sort_name)
print('After sorting by name',booklist)


# 5
def sort_price(book):
    return book[1]
booklist.sort(key=sort_price)
print('After sorting by price',booklist)


# 6
def price(book):
    return book[1]
max_book=max(booklist,key=price)
min_book=min(booklist,key=price)
print('Max price book:',max_book)
print('Min price book:',min_book)


# =======================================================================================================

# QUESTION 4 :

# Write a Python program to compute element-wise sum of given tuples, using “zip()” function
# Original tuples:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)


t1=(1, 2, 3, 4)
t2=(3, 5, 2, 1)
t3=(2, 2, 3, 1)
print(t1,'\n',t2,'\n',t3)
result=tuple(a+b+c for a,b,c in zip(t1,t2,t3))
print(result)


# =======================================================================================================

# QUESTION 5 :

# Write a Python program to find the repeated items of a tuple.


t1=tuple(input('Enter the tuple elements : '))
print(t1)

repeat=[]
for i in range(len(t1)):
    for j in range(i+1,len(t1)):
        if t1[i]==t1[j]and t1[i] not in repeat:
            repeat.append(t1[i])
repeat=tuple(repeat)
print('Repeated items : ',repeat)


# =======================================================================================================

