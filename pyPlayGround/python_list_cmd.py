#########################################################################
### Python List Methods                                               ### 
### List methods to work with Python List                             ### 
### Source: https://www.programiz.com/python-programming/methods/list ### 
#########################################################################

###-------------Python List copy() -------------####
####-- returns a shallow copy of the list ---###
####--Example 1 
# mixed list
prime_numbers = [2, 3, 5]
# copying a list
numbers = prime_numbers.copy()
print('Copied List:', numbers)
## Output: Copied List: [2, 3, 5]

####--Example 2
# mixed list
my_list = ['cat', 0, 6.7]
# copying a list
new_list = my_list.copy()
print('Copied List:', new_list)
##Output: Copied List: ['cat', 0, 6.7]
####--------------------------------------####



########################Python List count()########################
############## returns count of the element in the list ######
####--Example 1
# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]
# check the count of 2
count = numbers.count(2)
print('Count of 2:', count)
## Output: Count of 2: 3


####Example 2
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count)
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count)
##Output:
##The count of i is: 2
##The count of p is: 0
############################################################



######################## Python List append() ########################
########### Add a single element to the end of the list #########
#### Example 1
currencies = ['Dollar', 'Euro', 'Pound']
# append 'Yen' to the list
currencies.append('Yen')
print(currencies)
# Output: ['Dollar', 'Euro', 'Pound', 'Yen']
###--------------------------------------###



###------------- Python List clear() -------------####
###------- Removes all Items from the List ------###
prime_numbers = [2, 3, 5, 7, 9, 11]
# remove all elements
prime_numbers.clear()
# Updated prime_numbers List
print('List after clear():', prime_numbers)
# Output: List after clear(): []
###--------------------------------------###



###------------- Python List extend() -------------###
###---- adds iterable elements to the end of the list ---###
numbers1 = [3, 4, 5]
numbers2 = [10, 20]
# add the items of numbers1 to the number2 list
numbers2.extend(numbers1)
print(f"numbers1 = {numbers1}")
print(f"numbers2 = {numbers2}")
## Output:
## numbers1 = [3, 4, 5]
## numbers2 = [10, 20, 3, 4, 5]
###--------------------------------------###



###------------- Python List index() -------------###
###------- returns the index of the element in the list ------###
animals = ['cat', 'dog', 'rabbit', 'horse']
# get the index of 'dog'
index = animals.index('dog')
print(index)
# Output: 1
###--------------------------------------###



###------------- Python List insert() -------------###
###------- insert an element to the list ------###
# create a list of vowels
vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')
print('List:', vowel)
# Output: List: ['a', 'e', 'i', 'o', 'u']
###--------------------------------------###



###------------- Python List pop() -------------###
###------- Removes element at the given index ------###
prime_numbers = [2, 3, 5, 7]
# remove the element at index 2
removed_element = prime_numbers.pop(2)
print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)
# Output: 
# Removed Element: 5
# Updated List: [2, 3, 7]
###--------------------------------------###



###------------- Python List remove() -------------###
###------- Removes item from the list ------###
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]
# remove 9 from the list
prime_numbers.remove(9)
# Updated prime_numbers List
print('Updated List: ', prime_numbers)
# Output: Updated List:  [2, 3, 5, 7, 11]
###--------------------------------------###



###------------- Python List reverse() -------------###
###------- reverses the list ------###
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
# reverse the order of list elements
prime_numbers.reverse()
print('Reversed List:', prime_numbers)
# Output: Reversed List: [7, 5, 3, 2]

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
# List Reverse
systems.reverse()
# updated list
print('Updated List:', systems)
##Output:
##Original List: ['Windows', 'macOS', 'Linux']
##Updated List: ['Linux', 'macOS', 'Windows']

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]
# updated list
print('Updated List:', reversed_list)
##Output:
##Original List: ['Windows', 'macOS', 'Linux']
##Updated List: ['Linux', 'macOS', 'Windows']

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)
##Output:
##Linux
##macOS
##Windows
###--------------------------------------###



###------------- Python List sort() -------------###
###------- sorts elements of a list ------###
prime_numbers = [11, 3, 7, 5, 2]
# sort the list in ascending order
prime_numbers.sort()
print(prime_numbers)
# Output: [2, 3, 5, 7, 11]

numbers = [7, 3, 11, 2, 5]
# reverse is set to True
numbers.sort(reverse = True)
print(numbers)
#Output:[11, 7, 5, 3, 2]

cities = ["Tokyo", "London", "Washington D.C"]
# sort in dictionary order
cities.sort()
print(f"Dictionary order: {cities}")
# sort in reverse dictionary order
cities.sort(reverse = True)
print(f"Reverse dictionary order: {cities}")
##output:
##Dictionary order: ['London', 'Tokyo', 'Washington D.C']
##Reverse dictionary order: ['Washington D.C', 'Tokyo', 'London']

text = ["abc", "wxyz", "gh", "a"]
# stort strings based on their length
text.sort(key = len)
print(text)
##Output: ['a', 'gh', 'abc', 'wxyz']
###--------------------------------------###