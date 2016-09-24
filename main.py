from math import pi

try:
    radius = float(input('what is the radius?'))
    print('The area is ' + str(pi * radius ** 2))

except:
    print('you fool, that isn\'t a number')


