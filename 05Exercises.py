# 5.10. Exercises: Booleans and Conditionals
line_start = "<-------------"
line_end = "-------------->"

# 5.10.1. Part A: Basic Selection
print(line_start, "PART A", line_end)

# 5.10.1.1. if Only
user_entry = input('Enter a word: ')
if len(user_entry) > 5:
    print(user_entry, "is longer than 5 characters.")
print()

# 5.10.1.2. Binary Selection
num_entry = int(input('Enter a number larger than 100: '))
if num_entry >= 100:
    print("Valid entry!")
else:
    print("Number too small.")
print()

user_char_entry = input('Enter a lowercase character: ')
vowels = 'aeiou'
if user_char_entry.lower() in vowels:
    print(user_char_entry, "is a vowel.")
else:
    print(user_char_entry, "is NOT a vowel.")
print()

# 5.10.2. Part B: Logical Operators
print(line_start, "PART B", line_end)
num_entry = int(input('\nEnter a number: '))
if num_entry%2 == 0:
    print(num_entry, "is an even number.")
else:
    print(num_entry, "is NOT an even number.")

user_entry = input('\nEnter something: ')
if len(user_entry) > 9 and ' ' not in user_entry:
    print(user_entry, "is a really long word!")
else: 
    print(f"'{user_entry}' is either short, or it contains multiple words.")

print('\nRefactor letter code:')

letter = 'A'
cap_consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
vowels = 'aeiou'

if letter not in cap_consonants or letter in vowels:
   print("'" + letter + "'", "is either a lowercase vowel OR a capital consonant.")
else:
   print("Pick a capital consonant or a lowercase vowel.")

print('''
Refactor: Added 'not' in line 50.
Question: How does making this change affect the if/else code blocks?
Answer: Before if 'letter' was a lowercase consonant such as 'b', the if statement would return
    as true. 
        After refactor, now if only vowels would return true for the if statement.
''')

print('\nIf num = 5, indicate whether each of following expressions returns True or False.')
num = 5
print('num >= 0 and num*2 <= 50 and num%2 == 0   False, Actual:', num >= 0 and num*2 <= 50 and num%2 == 0)
print('num >= 0 or num*2 <= 50 or num%2 == 0   True, Actual:', num >= 0 or num*2 <= 50 or num%2 == 0)
print('num >= 0 and num*2 <= 50 or num%2 == 0   True, Actual:', num >= 0 and num*2 <= 50 or num%2 == 0)
print('num >= 0 or num*2 <= 50 and num%2 == 0   True, Actual:', num >= 0 or num*2 <= 50 and num%2 == 0)
print('not num < 0 and num%3 != 0   True, Actual:', not num < 0 and num%3 != 0)
print('not (num%3 == 0 or num*4 >= 20)   False, Actual:', not (num%3 == 0 or num*4 >= 20))
print()

# 5.10.3. Part C: Chained Conditionals
print(line_start, "PART C", line_end)

print('\n#1:')
num = 6 # Try the values 10, 15, and 7 as well.
if num%2 == 0 and num%3 == 0:
   print(num, "is divisible by 2 and 3.")
elif num%2 == 0:
   print(num, "is divisible by 2.")
elif num%3 == 0:
   print(num, "is divisible by 3.")
else:
   print(num, "is NOT divisible by 2 or 3.")

print('\n#2')
score_input = float(input('Enter percent score: '))
if score_input >= 90:
    letter_grade = 'A'
elif score_input >= 80:
    letter_grade = 'B'
elif score_input >= 70:
    letter_grade = 'C'
elif score_input >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print(str(score_input) + '% = ' + letter_grade)

print('\n#3')
temp = 'cold'
wetness = 'rainy'

if temp == 'hot' and wetness == 'rainy':
    activity = 'go watch Netflix'
elif temp == 'hot' and wetness == 'dry':
    activity = 'go swimming'
elif temp == 'cold' and wetness == 'rainy':
    activity = 'get under a blanket and read'
else:
    activity = 'go hang out with a friend'
print(f'The weather conditions are {temp} and {wetness} today. You should {activity}.')
print()

# 5.10.4. Part D: Nested Conditionals
print(line_start, "PART D", line_end)
print('\n#1')
lunch_selection = input('Would you rather have a burger or salad for lunch today? ').lower()
if lunch_selection == 'salad' or lunch_selection == 's':
    dressing = input('Which one: ranch or italian? ').lower()
    if dressing == 'ranch' or dressing == 'r':
        order = 'Salad with ranch dressing'
    else:
        order = 'Salad with italian dressing'
else:
    cheese = input('(Y/N) Would you like cheese on your burger? ').lower()
    if cheese == 'y'or cheese == 'yes':
        order = 'Cheeseburger'
    else:
        order = 'Hamburger'
print(f'Your order: {order}')

print('\n#2')
if order == 'Salad with ranch dressing':
    cost = 8.99
elif order == 'Salad with italian dressing':
    cost = 9.99
elif order == 'Cheeseburger':
    cost = 11.99
else:
    cost = 10.99
print(f'Bill for order: {order} is {cost}')

print('\n#3')
print('''The best place to ask if the customer would like a drink would be:
    c. As a separate conditional outside of the nested statements
    because it doesn't matter what they order for the lunch selection.
    It is separate from the food portion of the order''')