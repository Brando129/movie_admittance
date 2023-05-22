"""Write a function that checks whether a person can
watch an MA15+ rated movie. One of the following two conditions
is required for admittance:"""

def can_watch_ma15(age, guardian):

  # conditionals
  if age >= 15:
    return True
  elif guardian:
    return True
  else:
    return False
  
print(can_watch_ma15(13, False))