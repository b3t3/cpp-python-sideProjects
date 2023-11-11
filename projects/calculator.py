def multi(a):
  total = 1
  while a != 'end':
    a = input("Enter a number: ")
    if a == 'end':
      print("\nMultiplication is: ",total)
      break
    elif a == '':
      print("\nYou have entered an invalid integer\n")
      continue
    total *= int(a)


def addon(a):
  total = 0
  while a != 'end':
    a = input("Enter a number: ")
    if a == 'end':
      print("\nAddition is: ",total)
      break
    elif a == '':
      print("\nYou have entered an invalid integer\n")
      continue
    total += int(a)
    
def divi(a):
  total = []
  while a != 'end':
    a = input("Enter a number: ")
    if a == 'end':
      res = total[0] / total[1]
      if len(total) > 2:
        ind = 0
        for num in total:
          if ind == 0 or ind == 1:
            ind += 1
            continue
          else:
            res /= num
      print("\nDivision is: ",res)
      break
    elif a == '':
      print("\nYou have entered an invalid integer\n")
      continue
    total.append(int(a))

def sqr(a):
  total = 0
  while a != 'end':
    a = input("Enter a number: ")
    if a == 'end':
      print("\nAddition is: ",total)
      break
    elif a == '':
      print("\nYou have entered an invalid integer\n")
      continue
    total += int(a)

print('\nThis is a basic calculator attempt.\nYou can choose to make an adittion,multiplication or a divison.\nWhen wanting to end the input of numbers type "end"')
a = input("\nEnter an action: ").lower()
if a == 'multiplication':
  multi(a)

elif a == 'addition':
  addon(a)
  
elif a == 'division':
  divi(a)

elif a == 'square root':
  sqr(a)
elif a not in ['multiplication','addition','division']:
  print()
  print("You have entered an unsupported action or made a mistake in the\ngrammar of the existing ones. ")
  exit("Return to the beginning. English!")
