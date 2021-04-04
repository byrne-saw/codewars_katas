# https://www.codewars.com/kata/52fba66badcd10859f00097e/python

"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""

def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_list = list(string)
    disemvowel_list = []
    for i in range(len(string_list)):
        if string_list[i].lower() in vowels:
            continue
        else:
            disemvowel_list.append(string_list[i])
    return ''.join(disemvowel_list)

print(disemvowel("This website is for losers LOL!")) # => "Ths wbst s fr lsrs LL!"

# def disemvowel(string):
#     return string.translate(None, 'aeiouAEIOU')
# https://www.codewars.com/kata/reviews/54587841888e98707300020b/groups/54593fae52756d1cf4000b8c
# https://www.w3schools.com/python/ref_string_translate.asp

