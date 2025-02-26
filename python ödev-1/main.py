print('Kodlamaio')
baslik = 'Taşıt Kredisi'
print(baslik)
#string => metinsel ifade
baslik = 'İhtiyaç Kredisi'
print(baslik)
#int, integer => tam sayı
vade = 36 #numerik ifade
ekVade = 6
vade2 = '36' #metinsel ifade
#float, decimal, double
aylikOdeme = 200.50
#bool, boolean => true veya false
yukselisteMi = False

# Matematiksel Operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# / 
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % =>  mod operatörü
print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# Mantıksal Operatörler / Karşılaştırma Operatörleri
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

# CTRL + K + C birden fazla satırı yorum satırı haline getirir.

print(1 != 1)
print(1 != 2)

# or / and

#or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2) #true

print(1 > 2 and 5 > 2 and 3 > 2) #false

print(2 > 1 or 1 > 2 and 3 >2) #true

# Karar Yapıları
# if / else

sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdir
#condition

#indent = satırın başındaki boşluklar
if sayi1 < sayi2:
    print("sayi 1 sayi 2'den büyüktür")
    print("hala if bloğunun içerisindeyim")
elif sayi1 == sayi2:
    print("iki sayı eşittir")
#eğer if ve else if bloklarından hiç birine girmez ise 
else:
    print("sayi 1 sayi 2'den büyüktür")

print("***********************")

if sayi1 <= sayi2:
    print("sayi 1 sayi 2'den küçüktür")


if sayi1 == sayi2:
    print("iki sayı eşittir")
else:
    print("sayi 1 sayi 2'den büyüktür")

print("burası if bloğunun dışıdır")




