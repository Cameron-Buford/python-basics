print('Cam')
print('o----')
print(' ||||')
print('*' * 10)

price = 10

print(price)
price = 20
print(price)

price = 10
rating= 4.9
name = 'Cam'
is_published = False
print(price)


full_name = "John Smith"
age = 20
is_new = True

name = input('What is your name? ')
print('Hi ' + name)

color = input('what is your favorite color? ')
print('Cam likes ' + color)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input('weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

course = "python's course for beginners"
print(course)


course = ''' 
Hi Cam,
this is the first email
thank you
'''

print(course)

print(course[3])
print(course[0])

print(course[0:4])

print(course[1:5])
print(course[:])

name = 'jennifer'
print(name[1:-1])

print(len(course))

print(course.upper())
print(course.lower())

print(course.find('b'))


print(course.replace('beginners', 'noobs'))


# to check if there is a specific thing in a string and returns it as a boolean
print('python' in course)

# integers

#goes by order of operations but calls it operator prececdent. exponentials run first, then multiplication and division and then subtraction and addition



# if statements

is_hot = False
is_cold = False

if is_hot:
    print("it is a hot day")
    print("drink plenty of water")
elif is_cold:
    print('its a cold day')
    print('wear warm clothes')
else:
    print("its a lovely day")
print("enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: {down_payment}")