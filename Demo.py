
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

#Magical code-4 we need check the order we are adding the things
s = "abc"
n = ""
m = ""
for i in s:
    n = i + n
    m = m + i
print(n, m)

#Magical code-5 After removal next one moved to the removal place it will skip
colorss = ['red', 'rose', 'green', 'blue','red']
for c in colorss:
    if c.startswith('r'):
        colorss.remove(c)
print(colorss)