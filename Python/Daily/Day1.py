print("Hello, World!")

num1 = 89
print(type(num1))
print(num1)

num2 = 3.14
print(type(num2))
print(num2)

name = "Anchal"
print(type(name))
print(name)

list1 = [1,2,3,4,5,6]
print(type(list1))
print(list1)

list1.append(23)
print(list1)

tup1 = (2,4,5,6,7)
print(type(tup1))
print(tup1)

dict1 = {
    "name" : "Anchal",
    "age" : 25
    }
print(type(dict1))
print(dict1)

set1 = { 2, 2, 4 , 5 ,6,7,8,8}
print(type(set1))
print(set1)

a =  12
b = 23
result = a + b
print(result) 

a = 200
b = 23
result = a % b
print(result) 

a = 20
b = 4
result = a**b
print(result)

a = 20
b = 4
result = a//b
print(result)

a = 20
b = 4
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print(a > b)
print(a < b)

a = 45
b= 7
res = a>=b or a<=b
print(res)


age = 18
if(age >= 18 and age < 60):
    print("Eligible to vote")
else:
    print("Not Eligible")

num = 23
num += 4
print(num)

num = 23
num = -4
print(num)

print("IDENTITY OPERATOR")
a = 40
b = 20
print( a is b)
print(a is not b)

print("IN AND NOT IN (MEMBERHSHIP OPERATOR)")
list2 = [22, 34 ,56, 30 , 57 , 12]
print(56 in list2)
print(60 in list2)

print("CONTROL STATEMENTS")
print("IF, ELSE , ELIF")

x = 10
if(x > 10):
    print("Greater than 10")
elif(x == 10):
    print("Equals to 10")
else:
    print("Less than 10") 

print("Loops")
for i in range(5):
    print(i, end=" ")

print("Pratice Problems")



