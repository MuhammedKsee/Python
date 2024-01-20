class Calisan:

    zam_orani = 1.6
    counter = 0
    def __init__(self,name,surname,price):
        self.name = name
        self.surname = surname
        self.price = price

        Calisan.counter+=1
    def giveNameSurname(self):
        return self.name+" "+self.surname

    def zam_yap(self):
        self.price = (self.price + self.price*self.zam_orani)



calisan1 = Calisan("muhammed","kose",17000)
print("ilk maas : ",calisan1.price)

calisan1.zam_yap()
print("yeni maas: ",calisan1.price)

print("Calisan sayisi: ",Calisan.counter)

calisan2 = Calisan("ali","veli",15000)
print("Calisan sayisi: ",Calisan.counter)

