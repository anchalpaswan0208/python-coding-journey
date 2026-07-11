#Strings in python

#join() method is used to join the elements of an iterable (like a list or tuple) into a single string, with a specified separator.
list1 = ['Hello', 'World', 'Python']
print("-".join(list1))

#find() method returns the index of the first occurrence of the specified substring. If the substring is not found, it returns -1.
str1 = "Hello, World!"
print(str1.find("World"))

#Index() is similar to find() but it raises an exception if the substring is not found
str2 = "Hello, World!"
print(str2.index("or"))
# print(str2.index("Python"))  # This will raise a ValueError since "Python" is not in str2

#startswith() and endswith() methods
str3 = "Hello, World!"
print(str3.startswith("Hello"))
print(str3.endswith("rld!"))

#count() method returns the number of occurrences of a substring in the string.
str4 = "Hello, World! Hello, Python!"
print(str4.count("Hello"))
print(str4.count("o"))

#isaplha() methos checks weather all the characters in the string are alphabetic or not. It returns True if all characters are alphabetic, otherwise it returns False.
str5 = "HelloWorld"
print(str5.isalpha())

str5 = "HelloWorld56"
print(str5.isalpha())

#isdigit() method checks whether all the characters in the string are digits or not. It returns True if all characters are digits, otherwise it returns False.
str6 = "123 456"
print(str6.isdigit())

str6 = "123456"
print(str6.isdigit())

str6 = "12345jbjb6"
print(str6.isdigit())

# islower() method checks whether all the characters in the string are lowercase or not. It returns True if all characters are lowercase, otherwise it returns False.
str7 = "hel lo"
print(str7.islower())
print(str7.isupper())

# isalnum() method checks if the string contains chars annd numbers in the string
str8 = "Hello123"
print(str8.isalnum())

# isspace() method checks if the string contains only whitespace characters. It returns True if all characters are whitespace, otherwise it returns False.
str9 = "   "
print(str9.isspace())

#swapcase() method returns a new string with all uppercase characters converted to lowercase and vice versa.
str10 = "Hello, World!" 
print(str10.swapcase())

# center() method returns a new string that is centered within a specified width. It pads the string with spaces on both sides to achieve the desired width.
str11 = "Hello" 
print(str11.center(20, "*"))   #it takes only single letter as a parameter for padding

# zfill() method returns a new string that is left-padded with zeros to achieve a specified width.
str12 = "42"
print(str12.zfill(5))  # Output: "00042"

str12 = "hehe"
print(str12.zfill(5))  # Output: "00hehe"

#format() method is used to format strings by replacing placeholders with specified values.
name = "Anchal"
age = 20
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

#fstring is a way to embed expressions inside string literals, using curly braces {}. It allows for more concise and readable string formatting.
name = "Anchal"
age = 20
print(f"My name is {name} and I am {age} years old.")


#LISTS IN PYTHON

list1 = [1, 2, 3, 4, 5]

#append() method adds an element to the end of the list.
list1.append(6)
print(list1)

#extend() method adds all elements of an iterable (like another list) to the end of the list.
list1.extend([7, 8, 9])
print(list1)

#insert() method adds an element at a specified index in the list.
list1.insert(2, 10)  # Insert 10 at index 2
print(list1)

#remove() method removes the first occurrence of a specified element from the list.
list1.remove(10)  # Remove the first occurrence of 10
print(list1)

#pop() method removes and returns the element at a specified index. If no index is specified, it removes and returns the last element.
popped_element = list1.pop(3)  # Remove and return the element at index 3
print(popped_element)

#clear() method removes all elements from the list, making it empty.
list1.clear()
print(list1)  # Output: []

list2 = [1, 2, 3, 4, 5]
print(list2.index(3))

#count() method returns the number of occurrences of a specified element in the list.
list3 = [1, 2, 3, 2, 4, 2]
count_of_2 = list3.count(2)
print(count_of_2)  # Output: 3
 
#join() method is used to join the elements of an iterable (like a list or tuple) into a single string, with a specified separator.
list4 = ['Hello', 'World', 'Python']
print("-".join(list4))  # Output: "Hello-World-Python"

#sort() method sorts the elements of the list in ascending order by default. It modifies the original list.
list5 = [5, 2, 9, 1,  6]
list5.sort()
print(list5)  # Output: [1, 2, 5, 6, 9]

#reverse() method reverses the order of elements in the list. It modifies the original list.
list5.sort(reverse = True)
print(list5)  # Output: [9, 6, 5, 2, 1]

list5.reverse()  # Reverses the order of elements in the list
print(list5)

#copy() method creates a shallow copy of the list. It returns a new list that contains the same elements as the original list.
a = [1,2,3]
b = a.copy()
print(b)  # Output: [1, 2, 3]

#len() function returns the number of elements in the list.
list6 = [1, 2, 3, 4, 5]
print(len(list6)) 

#max() function returns the largest element in the list.
list7 = [1, 2, 3, 4, 5]
print(max(list7))

#min() 
list8 = [1, 2, 3, 4, 5]
print(min(list8)) 

#sum() function returns the sum of all elements in the list.
list9 = [1, 2, 3, 4, 5]
print(sum(list9))  

#sorted() function returns a new sorted list from the elements of any iterable (like a list, tuple, or string). It does not modify the original iterable.

list10 = [5, 2, 9, 1, 6]
sorted_list = sorted(list10)
print(sorted_list)  
print(list10)