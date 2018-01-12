EPSILON = 1e-14

for i in range(1000000):
    x = int((i**3)**(1/3) *(1+ EPSILON))
    assert x == i

