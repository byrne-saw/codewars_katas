# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

# Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

charge = 25

def tickets(people):
  cash_register = {
  25: 0,
  50: 0, 
  100: 0
  }

  for payment in people:
    cash_register[payment] += 1
    refund = payment - charge

    if refund == 0:
      continue
    elif refund == 75:
      if cash_register[50] > 0 and cash_register[25] > 0:
        cash_register[50] -= 1
        cash_register[25] -= 1
      elif cash_register[25] >= 3:
        cash_register[25] -= 3
      else:
        return "NO"      
    elif refund == 25:
      if cash_register[25] > 0:
        cash_register[25] -= 1
      else:
        return "NO"
  return "YES"

print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100])) 
