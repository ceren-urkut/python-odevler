def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return f"Sonuç: {sayi1 + sayi2}"
    elif islem == '-':
        return f"Sonuç: {sayi1 - sayi2}"
    elif islem == '*':
        return f"Sonuç: {sayi1 * sayi2}"
    elif islem == '/':
        if sayi2 == 0:
            return "Hata: Bölme işlemi için ikinci sayı 0 olamaz!"
        return f"Sonuç: {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü!"
    
print(hesap_makinesi(8, 7, '+'))  
print(hesap_makinesi(7, 2, '-'))
print(hesap_makinesi(6, 7, '-'))
print(hesap_makinesi(20, 5, '/')) 
print(hesap_makinesi(9, 0, '/'))  
print(hesap_makinesi(3, 7, '%'))  