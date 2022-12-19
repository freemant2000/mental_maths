import random 

def get_rand(no_digits):
  non_0_digits="123456789"
  digits="0"+non_0_digits
  s=random.choice(non_0_digits)
  for i in range(no_digits-1):
    s+=random.choice(digits)
  return int(s)

def addition(no_digits1, no_digits2):
  n1=get_rand(no_digits1)
  n2=get_rand(no_digits2)
  m=max(no_digits1, no_digits2)
  extra=2
  cols=m+1+extra
  print(str(n1).rjust(cols))
  print("+"+str(n2).rjust(cols-1))
  print("-"*cols)
  print(("_"*m).rjust(cols))

def multiply(no_digits1, no_digits2, show_ans_lines):
  n1=get_rand(no_digits1)
  n2=get_rand(no_digits2)
  m=no_digits1+no_digits2+1
  extra=0
  cols=m+1+extra
  print(str(n1).rjust(cols))
  print("*"+str(n2).rjust(cols-1))
  print("-"*cols)
  for i in range(show_ans_lines):
    d=str(n2)[-(i+1)]
    v=str(n1*int(d))
    print(v.rjust(cols-i))
  print(("_"*m).rjust(cols))


def addition_worksheet(no_questions):
  for i in range(no_questions):
    addition(2, 2)
    print()

#addition_worksheet(60)

multiply(2, 3, 2)