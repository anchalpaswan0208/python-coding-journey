#
# Q1. Find the Product
def Find_Prod(arr):
    product = 1

    for num in arr:
        product *= num

    return product
#Q2. Find the Sum
def Find_Sum(arr):
    total = 0

    for num in arr:
        total += num

    return total
#Q3. Count Occurrences
def findCount(arr, k):
    count = 0

    for num in arr:
        if num == k:
            count += 1

    return count
#Q4. Even Odd
def findEvenOdd(arr):
    even_sum = 0
    odd_sum = 0

    for num in arr:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return [even_sum, odd_sum]
#Q5. Find whether the number is present or not
def Find_Num(arr, m):
    if m in arr:
        return "YES"
    else:
        return "NO"
#Q6. Higher Age
def highAge(arr):
    result = []

    for age in arr:
        if age >= 18:
            result.append(age)

    return result
#Q7. Increment the List Elements
def Inc_Arr(arr):
    for i in range(len(arr)):
        arr[i] += 1

    return arr
#Q8. Pass or Fail
def isAllPass(arr):
    for marks in arr:
        if marks < 32:
            return "NO"

    return "YES"
#Q9. Unique Color Shirt
def uniqueShirts(arr):
    freq = {}

    for color in arr:
        freq[color] = freq.get(color, 0) + 1

    count = 0

    for value in freq.values():
        if value == 1:
            count += 1

    return count
#Q10. Min and Max
def findMinMax(arr):
    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return [minimum, maximum]