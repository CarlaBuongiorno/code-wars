'''
    Challenge:
    A family of kookaburras are in my backyard.
    I can't see them all, but I can hear them!
    How many kookaburras are there?

    Hint:
    The trick to counting kookaburras is to listen carefully
    The males sound like HaHaHa...
    The females sound like hahaha...
    And they always alternate male/female

    Examples:
    ha = female => 1
    Ha = male => 1
    Haha = male + female => 2
    haHa = female + male => 2
    hahahahaha = female => 1
    hahahahahaHaHaHa = female + male => 2
    HaHaHahahaHaHa = male + female + male => 3

    ======================

    Problem: (explicit requirements)
    - count the kookaburras based on 'h' for female and 'H' for male
    - Male and female always alternate

    Problem: (implicit requirements)
    - get the sound string
    - break it up into sections at the change between the 'h' and 'H'
    - count the sections

    Setup (input):
    - function call with string to slice as parameter

    Process (intermediate steps):
    - slice the string at the change

    Output (return):
    - count the sections/changes
'''

def main():
    kooka = kooka_sound('HaHaHahahaHaHa')
    print(f'There are {kooka} kookaburras in my backyard.')


def kooka_sound(sound):
    sound = sound.split('a') # ['H', 'H', 'H', 'h', 'h', 'H', 'H', '']
                             #   1    2    3    4    5    6    7   -1   -> is 1 == -1? False
                             #                                             is 2 == 1? True
                             #                                             is 3 == 2? True
                             #                                             is 4 == 3? False
                             #                                             is 5 == 4? True
                             #                                             is 6 == 5? False
                             #                                             is 7 == 6? True
    print(len(sound)-1) # 7
    # create a list of true and false for 7 iterations of the list above.
    sound = [sound[i] == sound[i-1] for i in range(len(sound)-1)] # for i in range(7) -> for 7 iterations
    print(sound) # [False, True, True, False, True, False, True]
    # All False items are the changes, therefore count the Falses to find the number of birds
    count = sound.count(False)
    return count


if __name__ == '__main__':
    main()
