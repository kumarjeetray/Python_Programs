'''
Rick Language
Vowels -> r
'''

def translate(user):
    for letter in user:
        if letter in 'aeiou':
            print('r', end="")
        elif letter in 'AEIOU':
            print('R', end="")
        else:
            print(letter, end="")

user = input("Enter a String:")
print("Before Translation:")
print(user)
print("After Translation:")
translate(user)

