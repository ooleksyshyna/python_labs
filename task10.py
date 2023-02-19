#10
import math

x1 = 39.9075000
x2 = 116.3972300

y1 = 50.4546600
y2 = 30.5238000

a1= math.radians(x1)
a2= math.radians(x2)

b1= math.radians(y1)
b2= math.radians(y2)

distance = 6371.032 * math.acos(math.sin(a1) * math.sin(a2)
                                 + math.cos(a1) * math.cos(a2) * math.cos(b1 - b2))

print(distance)
