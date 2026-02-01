#Magical code-1
total = 0.1 + 0.2
print(total)
if total == 0.3:
    print('Hi')
else:
    print('Hello')

#Magical code-2 These are non-empty strings so always true
name = "Ravi"
if name == "Kumar" or "Allam":
    print('Correct Name')
else:
    print('Wrong Name')

x="False"
if x:
    print('Coding')
else:
    print('Non Coding')

#Magical code-3 strings are immutable. If we are not storing it will unchange
food = "Pizza"
b= food.replace("z","s")
print(food,b)