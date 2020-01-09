#Set

Sets = {}

#includes a data type for sets.
#Curly braces or the set() function can be use to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

'orange' in basket

'crabgrass' in basket

#Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a              #unique letters in a
a - b          #letters in a but not in b
a | b          #letters in a or b or both
a & b          #letters in both a & b
a ^ b          #letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a
if x in 'abc'
     for x in 'abracadabra'
print(x)



fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)
print("cherry","pineapple" in fruits)

fruits.add("cucumber")
fruits
fruits.insert("cucumber")
Error
fruits.add("cucumber")
fruits
{'orange', 'kiwi', 'apple', 'cherry', 'mango', 'cucumber', 'melon', 'banana'}
fruits.add("water melon")
fruits
{'orange', 'kiwi', 'apple', 'cherry', 'mango', 'cucumber', 'water melon', 'melon', 'banana'}
fruits.update("grape")


>>>Dictionaries

#Dictionaries

#Another useful data type built into python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['jack']
tel['guido'] = 4127

del tel['sape']
tel

list(tel)

sorted(tel)

'guido' in tel

'sape' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)
dict(4139, 4127, 4098)

{x: x**2 for x in (2, 4, 6)}
{x: x**3 for x in (1, 2, 3, 4, 5)}

#When looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)
knights = {'gallahad': 'the pure', 'robin': 'the brave', 'Yangon': 'Myanmar'}
for k, v, z in knights.items():
	print(k, v, z)
