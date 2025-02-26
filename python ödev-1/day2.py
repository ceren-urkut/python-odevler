faiz = 1.59
vade = "36"
krediAdi = "ihtiyaç kredisi"

print(type(faiz)) # type faiz değişkeninin tipini yazdırır
print(type(vade))
print(type(krediAdi))

print(int(vade)+12) #vade değişkeninin türünü int e çevirir ve işlemi yapar
# print(int(krediAdi)) hatalı
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz:"))
print(type(vade))
print(vade + 12)

# string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade:" + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "ceren" #input("isminizi girin:")
metin = "merhaba {name}".format(name=isim)
print(metin)

# f-string
metin = f"Hoşgeşdiniz {1+1}"
print(metin)
print("************************")

# LİSTELER

dizi = ["ihtiyaç kredisi", 10, 5.2, True]
print(dizi)

krediler = ["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length
# print(krediler[3]) => hata verir

krediler.append("Özel Kredi") #append=>listenin sonuna yeni girdi ekler
print(krediler)

krediler.append("x kredisi")
print(krediler)

krediler.pop(0) #pop=> girilen index değerini listeden siler, bir index girmezsen listenin son elemanını siler
print(krediler)

krediler.remove("taşıt kredisi") #remove=> index sırasına göre girilen elemanı bulduğunda değeri listeden siler
print(krediler)

krediler.extend(["y kredisi", "z kredisi"])
print(krediler)

# for
# i=0 i<10

for i in range(10):
    print("xx")
    print(i)
print("**********************")
for i in range(5,10):
    print(i)
print("**********************")
for i in range(0,51,10): #0 ve 51 arasında 10'ar arttırarak döngü kur
    print(i)
#1.eleman=başlangıç
#2.eleman=bitiş
#3.eleman=ilgili değişkenin kaçar artacağına karar verilen kısım

krediler = ["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi"]
for kredi in krediler:
    print(kredi)
print("**********************")
for i in range(len(krediler)):
    print(krediler[i])

for i in range(10):
    print(i)
print("**********************")

# sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("**********************")

while True:
    print("X")
    break

print("*********************")

i = 0
while i < len(krediler):
    if krediler[i] == "konut kredisi":
        break
    print(krediler[i])
    i += 1

print("******* Son Döngü *******")

krediler = ["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi"]
i = 0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    if krediler[i] == "konut kredisi":
        break

# FONKSİYONLAR

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat, indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Ceren")
sayHello("Özlay")
sayHello("Kerem")

def calculateAndReturn(fiyat, indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat + 10) 

# void
def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("***************")
fonk1 = calculatePrice(100, 50)
fonk2 = calculatePriceAndReturn(300, 100)
print(f"159.satır: {fonk1}")
print(f"160.satır: {fonk2+100}")
print("****************")

