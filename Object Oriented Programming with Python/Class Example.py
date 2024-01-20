class Worker:
    counter = 0
    zamOrani = 1.6
    def __init__(self,name,surname,price):
        self.name = name
        self.surname = surname
        self.price = price

        Worker.counter +=1

    def giveNameSurname(self):
        return self.name+" "+self.surname
    def zamYap(self):
        self.price= self.price+self.price*self.zamOrani


worker1 = Worker("ali","veli",12000)
worker2 = Worker("ayse","asd",13000)
worker3 = Worker("muhammed","kose",15000)
worker4 = Worker("cemil","duran",14000)

liste = [worker1,worker2,worker3,worker4]

print(liste)

maxiMaas = -1
index = -1
for each in liste:
    if(each.price>maxiMaas):
        maxiMaas = each.price
        index = each
print(maxiMaas)
print(index.giveNameSurname())