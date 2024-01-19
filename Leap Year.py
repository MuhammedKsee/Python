year = input("Please enter a year")

if(int(year)%4==0) or (int(year)%100==0):
    print("%d is a leap year"%int(year))
else:
    print("%d is not a leap year"%int(year))