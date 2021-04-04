# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example:

# persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.
                 
# persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.
                  
# persistence(4) => 0   # Because 4 is already a one-digit number.



def persistence(n):
    list_n = list(map(int, str(n)))
    persistence = 0
    while len(list_n) != 1:
        persistence += 1
        pers = list_n[0]
        for i in range(1, len(list_n)):
            pers = pers * list_n[i]
        list_n = list(map(int, str(pers)))    
    return(persistence)


print(persistence(39))   # => 3
print(persistence(4))   # => 0
print(persistence(25))   # => 2
print(persistence(999))   # => 4