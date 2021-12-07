# a=[9,3,5,6]
# summa=sum(a)
# import numpy as np
# l = [1,2,3,4,5]
# print("Summa:",summa)
# print("Reizinājums:",np.prod(l))
# 

# Vārds = 'Alberts'[::-1]
# print(Vārds)

patskani = ['a','ā','e','ē','u','ū','i','ī','o']
teikums = input("Ievadiet tekstu: ")
count = 0
for letter in teikums:
  if letter in patskani:
    count += 1
print(count)