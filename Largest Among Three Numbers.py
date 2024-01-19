var1 = 123
var2 = 120
var3 = 134

if(var1>var2) and(var2>var3):
    print("%d is a largest number"%var1)
elif(var2>var1) and (var2>var3):
    print("%d is a largest number" % var2)
else:
    print("%d is a largest number" % var3)
