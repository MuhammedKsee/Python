num = 5

num_sqrt = num ** 2
num_sqrt2 = num ** 0.5

print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt2))

# for real or complex

import cmath

num2 = 1+2j

num_sqrt3 = cmath.sqrt(num2)

print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))