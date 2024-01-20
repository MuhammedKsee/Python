class Calisan:
    def __init__(self,isim,soyisim,maas):#constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@gmail.com"


    def giveNameSurname(self): #function
        return self.isim+" "+self.soyisim
isci1 = Calisan("ali","veli",12300)

print(isci1.giveNameSurname()+" "+str(isci1.maas)+" "+str(isci1.email))
