marks = int(input("Enter your marks out of 50:"))

if marks >= 41 and marks <= 50:
    print("Grade A")
elif marks >= 33 and marks <= 40:
    print("Grade B")
elif marks >= 21 and marks <= 30:
    print("Grade C")
elif marks >= 11 and marks <= 20:
    print("Grade D")
else:
    print("Grade F")


getValueFunction ={
        "P":"PrepBytes",
        "Z":"Zenith",
        "E":"Expert Coder",
        "D":"Data Structure"
    }
word = input("Enter a word: ").upper()

if word in getValueFunction:    
    print(getValueFunction[word])
else:
    print("Invalid Key")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if (a >= b and a >= c):
    print("a is the largest value")
elif(b >= a and b >= c):
    print("b is the largest value")
else:
    print("c is the largest value")


list1 = [23 ,10 ,5 ]
print(len(list1))
list1.sort()
print(list1[1])

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if(a <90 and b <90 and c <90):
    print("Acute Triangle")
else:
    print("Obtuse Triangle")






