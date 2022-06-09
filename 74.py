from math import radians
from random import randint

g = (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10))
s = sorted(g)
print(f'Os valores sorteados foram {g}')
print(f'O maior valor foi {s[4]} e o menor foi {s[0]}')
