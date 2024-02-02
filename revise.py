import pandas as pd
import random

L = []
for i in range(10000):
  a = random.randint(1,6)
  b = random.randint(1,6)

  L.append(a + b)

print(len(L))
print(L[:5])

s = (pd.Series(L).value_counts()/pd.Series(L).value_counts().sum()).sort_index()
print(s)
(s.plot(kind='bar'))

print(s.plot(kind='bar'))