#If Else Statements

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions
Equals					-> x == y
Not Equals              -> x != y
Less Than               -> x <  y
Less Than or Equal to   -> x <= y
Greater than            -> x >  y
Greater than or Equal to-> x >= y

#If Statement 
x = 70
y = 60

if x < y:
	print("x is greater than y")
elif:
	print("y is smaller than x")
else:
	print("y is smaller than x")

#Elif

x = 70
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")

#Else

x = 50 
y = 150
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x is less than y")

#Shot Hand If

if x > y: print("x is greater than y")

----------------------

result = int(input("Enter Your Mark: "))

if 90 < result & result <100: print("A")
elif 70 < result & result < 89: print("B")
elif 60 < result & result < 69: print("C")
elif 40 < result & result < 59: print("D")
else 10 < result & result < 39: print("Fail")

#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > x:
	print("All conditions are True")

#Or is Logical Operator

x = 50
y = 40
z = 100
if x > y or z > x:
	print("One of the conditions is True")

#Nested If is if statements in if statements

x = 50 

if x > 10:
	print("x is ten")
	if x > 20:
	print("x is greater than 20")
	else:
		print("x is not greater than 20")
