a = 10
b = "2"

liste = [1,2,3]
print(sum(liste))

#print(a+b) #string ile integer toplanmaz!

print(str(a)+b)

k = 10
zero = 0
print(k)#tanımlama yapılmak zorunda
if zero==0:
    a = 0
else:
    a = k/zero
print(a)


try:
    a = k/zero
except ZeroDivisionError:
    a = 0



#index error
list1 = [1,2,3,4]
list1[15]
#listede sınır aşımı

#module not found error

import numpy

#file not found error
import pandas as pd
pd.read_csv("asd")

#type error
"2"+5

#value error
int("asd")


try:
    1/0
except:
    print("Except")
else:
    print("Else")
finally:
    print("Done")



