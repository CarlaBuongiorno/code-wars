'''
    Challenge:
    Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only if the original word was capitalized 
    (known as Upper Camel Case, also often referred to as Pascal case). 
    The next words should be always capitalized.

    Examples:
    "the-stealth-warrior" gets converted to "theStealthWarrior"
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
    "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
'''

def main():
    convert_to_camel_casing("the-stealth-warrior") # ['the', 'stealth', 'warrior']
    convert_to_camel_casing("The_Stealth_Warrior") # ['The', 'Stealth', 'Warrior']
    convert_to_camel_casing("The_Stealth-Warrior") # ['The', 'Stealth', 'Warrior']

def convert_to_camel_casing(string_to_convert):
    string_to_convert = string_to_convert.replace('-', ' ').replace('_', ' ').split()
    if string_to_convert[0][0].islower():
        conversion = [string_to_convert[i].capitalize() for i in range(1, len(string_to_convert))]
        print(string_to_convert[0] + ''.join(conversion))
    else:
        print(''.join(string_to_convert))

if __name__ == '__main__':
    main()