# 1. Rational, it can be presented as a fraction.
# 2. 10^2
# 3. 9
# 4. 125
# 5. 1000 * 1.05^36

p = 1000
r = .05
t = 3
n = 12
a = p * (1 + (r/n))**(n * t)
print(a)

# 6. 1000 * e^0.05*3

from math import exp

p = 1000 # principal, starting amount
r = .05 # interest rate, by year
t = 3.0 # time, number of years
a = p * exp(r*t)

print(a)

# 7. 18

from sympy import *
# Declare 'x' to SymPy
x = symbols('x')
# Now just use Python syntax to declare function
f = 3*x**2 + 1
# Calculate the derivative of the function
dx_f = diff(f)
print(dx_f) # prints 6*x
print(dx_f.subs(x,3)) # 18

# 8.

from sympy import *
# Declare 'x' to SymPy
x = symbols('x')
# Now just use Python syntax to declare function
f = 3*x**2 + 1
# Calculate the integral of the function with respect to x
# for the area between x = 0 and 2
area = integrate(f, (x, 0, 2))
print(area) # prints 10












