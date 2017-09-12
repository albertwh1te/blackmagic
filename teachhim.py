L = ['Hello', 'World',18, 'IBM', 'Apple']
A = []
for i in L:
  if isinstance(i, str) == True:  
   print(i.lower())
   A.append(i.lower())
  else:
   print(i)
   A.append(i)
print(A)