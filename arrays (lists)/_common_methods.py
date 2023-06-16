# Built in list methods

# append()
# Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits) # -> ['apple', 'banana', 'cherry', 'orange']

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a) # -> ['apple', 'banana', 'cherry', ["Ford", "BMW", "Volvo"]]


# clear()
# Removes all the elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits) # -> []


# copy()
# Returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy) # -> ['apple', 'banana', 'cherry']


# count()
# Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x) # -> 1


# extend()
# Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits) # -> ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']


# index()
# Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
y = fruits.index("cherry")
print(y) # -> 2


# insert()	
#Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits) # -> ['apple', 'orange', 'banana', 'cherry']


# pop()	
# Removes the element at the specified position, default is -1
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits) # -> ['apple', 'cherry']


# remove()	
# Removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits) # -> ['apple', 'cherry']


# reverse()	
# Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) # -> ['cherry', 'banana', 'apple']


# sort()	
# Sorts the list; optional reverse=True argument
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars) # -> ['BMW', 'Ford', 'Volvo']

cars.sort(reverse=True)
print(cars) # -> ['Volvo', 'Ford', 'BMW']