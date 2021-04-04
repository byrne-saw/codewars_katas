#https://www.codewars.com/kata/5390bac347d09b7da40006f6/solutions/python
quote = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(string):
    wordList = string.split()
    jadenCase = ''
    count = 0

    for word in wordList:
        if count == 0:
            jadenCase = jadenCase + word.capitalize()
            count += 1
        else:
            jadenCase = jadenCase + ' ' + word.capitalize()



    return(jadenCase)

print(to_jaden_case(quote))
        
