# Pandas hizli ve etkili for dataframes
# CSV ve text dosyalarına acip inceleyip sonuclarimiza bu dosya tiplerine rahat bir şekilde kaydedilebilir.
# Pandas bizim işimizi kolaylaştırıyor for missing data
# Reshape yapıp datayı daha etkili şekilde kullanabiliriz
# Slicing indexing kolay
# Time series data analizinde çok yardımcı
# Pandas Hiz açısından optimize edilmiş hızlı bir kütüphane

import pandas as pd
import numpy as np

dictionary = {"Name":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "PRICE":[100,150,240,350,110,220]}

print(dictionary)  # Sözlük yapısını ekrana yazdırır

dataFrame1 = pd.DataFrame(dictionary)  # DataFrame oluşturur

print(dataFrame1)  # DataFrame'i ekrana yazdırır

head = dataFrame1.head()  # DataFrame'in ilk 5 satırını alır
tail = dataFrame1.tail()  # DataFrame'in son 5 satırını alır

print(head)  # İlk 5 satırı ekrana yazdırır
print(tail)  # Son 5 satırı ekrana yazdırır

# Pandas basic method
print(dataFrame1.columns)  # DataFrame sütunlarını ekrana yazdırır
print(dataFrame1.info())  # DataFrame hakkında bilgi verir
print(dataFrame1.dtypes)  # DataFrame'in sütun veri tiplerini ekrana yazdırır
print(dataFrame1.describe())  # Sayısal veri içeren sütunlar için istatistiksel bilgileri ekrana yazdırır

#indexing and slicing

print(dataFrame1["Name"])
print(dataFrame1["AGE"])
print(dataFrame1.AGE)
dataFrame1["new feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1["new feature"])
print(dataFrame1.loc[:,"AGE"])
print(dataFrame1.loc[:3,"AGE"])

print(dataFrame1.loc[:3,"AGE":"Name"])
print(dataFrame1.loc[:,["AGE","Name"]])
print(dataFrame1.loc[::-1,:])
print(dataFrame1.loc[:,:"Name"])

print(dataFrame1.loc[:,"Name"])
print(dataFrame1.iloc[:,2])

#filtering

filtre1 = dataFrame1.PRICE > 200

print(filtre1)
print(type(filtre1))

filtre2 = dataFrame1.AGE<20
print(dataFrame1[filtre1 & filtre2])

print(dataFrame1[dataFrame1.AGE>60])

# List comprehension

ortalamaMaas = (dataFrame1.PRICE.mean())

print(ortalamaMaas)

ortalamaMaasNp = np.mean(dataFrame1.PRICE)

dataFrame1["price level"] = ["Dusuk"if ortalamaMaas > each else "Yuksek" for each in dataFrame1.PRICE]


for each in dataFrame1.PRICE:
    if(ortalamaMaas > each):
        print("Dusuk")
    else:
        print("Yuksek")

print(dataFrame1.columns)
dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

print(dataFrame1.columns)

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if len(each.split())>1 else each for each in dataFrame1.columns]

print(dataFrame1.columns)

# drop and concatenating

print(dataFrame1.drop(["new_feature"],axis=1))
print(dataFrame1.drop(["new_feature"],axis=1,inplace=True))

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical
dataConcat = pd.concat([data1,data2],axis=0)
print(dataConcat)

#horizontal
price = dataFrame1.price
age = dataFrame1.age
dataHConcat = pd.concat([price,age],axis=1)
print(dataHConcat)

#transforimng data
dataFrame1["list_comp"] = [each*2 for each in dataFrame1.age]

#apply()
def multipy(age):
    return age*2

dataFrame1["apply_methodu"] = dataFrame1.age.apply(multipy)
print(dataFrame1)