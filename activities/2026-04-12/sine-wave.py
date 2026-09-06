import math

wave_height = 3

for y in range(50):
    x = int(wave_height + math.cos(y) * wave_height)
    print(x * " " + "*")
