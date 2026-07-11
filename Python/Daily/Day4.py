# list comprehension

#method1
squares = [x*x for x in range(5)]
print(squares)


#method2
square1 =[]
number = [1,2,3,4,5]

for i in number:
    square1.append(i*i)
print(square1)

#method3
num = [1,2,3,4]

square = [x*x for x in number]
print(square)

#method 4

sq2 = []
for i in range(5):
    sq2.append(i*i)
print(sq2)

#method 5
sq4 =[x*x for x in range(1,6)]
print(sq4)
 
#method 6
even = [x for x in range(1,11) if x%2==0]
print(even)

#method 7
odd = [x for x in range(1,11) if x%2 ==1]
print(odd)

#method 8
names = ["anchal" , "anuj" , "shubh"]
upper_name =[name.upper() for name in names]
print(upper_name)

#method 9
names = ["anchal" , "anuj" , "shubh"]
cap_name = [name.capitalize() for name in names]
print(cap_name)

#method 10
words = ['apple','banana', 'mango' , 'strawberry']

word_length =[len(word) for word in words]
print(word_length)

# Condtitional Expression
result = [f"Even, {x}" if x%2 == 0 else f"Odd,{x}" for x in range(1,6)]
print(result)

#Nested List Comprehension
matrix = [[i for i in range(3)] for j in range(3)]
print(matrix)

# functions
def greet(name, age):
    return f"Hello, {name} and my age is {age}"

message = greet("Anchal", 20)
print(message)

#  in python there ar two types of function ; Built-in and user Defined

#lambda functions: These are one line anonyous function which does not have a name 

square = lambda x:x*x
print(square(5))

multipy = lambda a, b: a*b
print(multipy(3,7))

students = [
    ("Aman", 80),("Rahul", 95),("Priya" , 88)
]
students.sort(key = lambda x:x[1])
print(students)


