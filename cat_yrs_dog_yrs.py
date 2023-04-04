'''
Challenge:
I have a cat and a dog which I got as a  kitten / puppy.
I forget when that was, but I do know their current ages as 'cat_years' and 'dog_years'.
Find how long I have owned each of my pets and return as a list [owned_cat, owned_dog].

NOTES:
Results are truncated whole numbers of 'human' years

Cat Years:
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years:
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that

Problem: (explicit requirements)
- Current ages in cat_years and dog_years are known
- How long have I owned each of my pets in 'human' years
- Return the result as a list [owned_cat, owned_dog] in truncated whole numbers

Example:
Cat is 32 cat_years
1 human_years = 15 cat_years (0 + 15)
2 human_years = 24 cat_years (0 + 15 + 9)
3 human_years = 28 cat_years (0 + 15 + 9 + 4)
4 human_years = 32 cat_years (0 + 15 + 9 + 4 + 4)

Work backwards to zero:
(32 - 15) cat_years =              32 - 15 = 17 cat_years => 1 human_years
(32 - 15 - 9) cat_years =          17 - 9 = 8 cat_years => 2 human_years
(32 - 15 - 9 - 4) cat_years =      8 - 4 = 4 cat_years => 3 human_years
(32 - 15 - 9 - 4 - 4) cat_years =  4 - 4 = 0 cat_years => 4 human_years

Problem: (implicit requirements)
- Convert the age of the cat and dog to human years
- The age in human years is the same for how long you've owned the cat and dog

Setup (input):
- get the ages of the cat and dog in cat years and dog years
    - How old is your cat in cat years?
    - How old is your dog in dog years?

Process (intermediate steps):
- use cat_years and dog_years as parameters to function that converts cat/dog age into human years
- to find the 1st human_year, subtract 15 (cat_years) for the age of cat
- subtract 9 from the result to find the 2nd human_year
- subtract 4 from the result to find the 3rd human_year
- keep subtracting 4 from the result until the result is zero and add 1 human_year each time.
- append the human_years number to a list
repeat for dog_years with different subtracting numbers for each human_year

Output (return):
- when you reach zero cat_years, you will have a number of human_years
- append the human_years number to a list
- return [owned_cat, owned_dog]
'''

def main():
    pet_dict = pet_age() # {'cat': 36, 'dog': 78}
    original_pet_dict = dict(pet_dict)
    initial_years = first_years(pet_dict) # {'cat': 2, 'dog': 2}
    total_human_years = older_pet(original_pet_dict, initial_years) # {'cat': 2, 'dog': 2} -> {'cat': 36, 'dog': 78} -> {'cat': 3, 'dog': 10}
    print(total_human_years)
    

def pet_age():
    cat_years = int(input('How old is your cat in cat years? '))
    dog_years = int(input('How old is your dog in dog years? '))
    return {'cat': cat_years, 'dog': dog_years}



def first_years(pet_dict): # {'cat': 36, 'dog': 78}, {'cat': 3, 'dog': 10}
    for pet, age in pet_dict.items():
        if age <= 15:
            pet_dict[pet] = 1
        elif age > 15:
            pet_dict[pet] = 2
    return pet_dict # {'cat': 2, 'dog': 2}


def older_pet(original_pet_dict, initial_years):
    print(original_pet_dict)
    print(initial_years)
    if original_pet_dict['cat'] > 24:
        original_pet_dict['cat'] -= 24
        original_pet_dict['cat'] //= 4
        initial_years['cat'] += original_pet_dict['cat']
    if original_pet_dict['dog'] > 24:
        original_pet_dict['dog'] -= 24
        original_pet_dict['dog'] //= 5
        initial_years['dog'] += original_pet_dict['dog']
    return [initial_years['cat'], initial_years['dog']]


if __name__ == '__main__':
    main()
