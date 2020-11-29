# import user defined module
import module

print(module.a)
module.a = [i - 5 for i in module.a]
print(module.a)

# pandas package
import pandas as p

b = ['h', 'e', 'm', 'a']
c = p.Series(b)
print(c)

# random module
import random as r

x = list(range(1, 101))
print(r.choice(x))

# sys package and python path
import sys

for p in sys.path:
   print(p)
