# Question 1: Creating and Modifying Lists
from tabnanny import check

fruits = ["Apple","Banana","Orange","Pear","Peach"]

fruits[4] = "Mango"

fruits.insert(0, 'Apricot')

fruits.remove("Orange")

print(fruits)



# Question 2: List Operations

numbers = [1,2,3,4,5]

number_squared = [1*1,2*2,3*3,4*4,5*5]

total_numbers = sum(numbers)

average = total_numbers / len(numbers)

print("Total of numbers:",total_numbers)
print("Average of numbers:",average)



# Question 3: Creating and Modifying Dictionaries

countries_capitals = {
    'Canada': 'Ottawa',
    'United Kingdom':'London',
    'Germany':'Berlin',
    'Australia':'Canberra'
}

countries_capitals['France'] = 'Paris'

countries_capitals['Canada'] = 'Toronto'

del countries_capitals['Germany']

print(countries_capitals)




# Question 4: Dictionary Operations

fruit_colors = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Orange': 'Orange',
    'Lemon': 'Yellow',
    'Cherry': 'Red'}





for fruit in fruit_colors.keys():
    print(fruit)

for fruit in fruit_colors.values():
    print(fruit)

for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}.")

check_fruit = "Banana"

if check_fruit in fruit_colors:
    print(f"The color of {check_fruit} is {fruit_colors[check_fruit]}. " )
else:
    print(f"{check_fruit} is not int he dictionary.")


