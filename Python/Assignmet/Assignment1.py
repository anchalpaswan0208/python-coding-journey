#Problem1
def AddTwoNumbers(A, B):
    return A+B

result = AddTwoNumbers(5, 3)
print(result)
 
#Problem2
def IsValid(A, B):
    return A > 10 and A > B

result = IsValid(15 , 5)
print(result)


#Problem3
def check(A, B):
    if A % 10 == 0 and B % 10 == 0:
        return True
    elif A % 10 == 0 or B % 10 == 0:
        return True
    else:
        return False

result = check(20, 15)
print(result)

#Problem4
def First_Digit(N):
    return N // 1000

result  = First_Digit(12345)
print(result)

#Problem5
def Last_Digit(N):
    return N % 10
result = Last_Digit(12345)
print(result)

#Problem6
def Find_the_remainder(A, B):
    return A % B
result = Find_the_remainder(10, 3)
print(result)

#Problem7
def Multiply_two_number(A, B):
    return A * B
result = Multiply_two_number(5, 3)
print(result)

#Problem8
def SUM_Average(A, B ,C):
    total = A + B + C
    average = total / 3
    return total, average

result = SUM_Average(5, 10, 15)
print(result)
