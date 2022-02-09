#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 12
y = 42

if x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
elif x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x == y:
    print('x == y: x is {} and y is {}'.format(x, y))
else:
    print('do something else')


if x == 5:
    print('do five stuff')
elif x == 6:
    print('do six stuff')
elif x == 7:
    print('do 7 stuff')
elif x == 8:
    print('do 8 stuff')
elif x == 42:
    print('do 42 stuff')
else:
    print('do that other thing')
