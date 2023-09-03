ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
print("\n")

# your code here

ft_list[1] = "World!"
ft_tuple = ("Hello", "Germany!")

ft_set.remove("tutu!")
ft_set.add("Heilbronn!")

ft_dict["Hello"] = "42 Heilbronn!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Tuples are immutable, which means that their elements cannot be changed
# once they are created. Tuples are often used to store data that does
# not need to be changed, such as the coordinates of a point on a map.

# Lists are mutable, which means that their elements can be changed after
# they are created. Lists are often used to store data that needs to be
# changed frequently, such as the items in a shopping cart.

# Dictionaries are a type of data structure that stores data in key-value
# pairs. The keys are unique, and the values can be of any type. Dictionaries
# are often used to store data that can be looked up by a unique key,
# such as the names and phone numbers of contacts.

# Sets are a type of data structure that stores unique elements.
# Sets are often used to store data that does not need to be ordered,
# such as the letters in a word.

# In the case of the tuple ft_tuple, the first assignment creates a
# reference to the tuple ("Hello", "toto!"). The second assignment
# creates a new tuple ("Hello", "Germany!) and assigns it to the variable
# ft_tuple. The first tuple is still referenced by the variable ft_tuple,
# but it is not printed because the print function only prints the value
# that is currently referenced by the variable.
