def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} asal değil."
    for i in range(2, sayi):
        if sayi % i == 0:
            return f"{sayi} asal bir sayı değildir."
    return f"{sayi} asal bir sayıdır."

deger1 = 8
deger2 = 1
deger3 = 3

print(asal_mi(deger1))
print(asal_mi(deger2))
print(asal_mi(deger3))