# request / requirement
# 1. Kullancıdan 2 tane değer alsın.
# 2. Değerlerin ikiside metin ise iki değer arasına boşluk koyup ekrana yazacak
# 3. Eğer değerlerin ikiside sayı ise toplamını yazacak.
# 4. Değerlerden biri metin diğeri sayı ise hata verecek (raise)
# 5. Kullanıcı devamlı program içinde tutulacak (while)
# 6. çıkmak için seçenek sunulacak 

 
while True:
    value1 = input("Değer 1'i giriniz : ")
    value2 = input("Değer 2'yi giriniz : ")

    if (value1.isnumeric() and value2.isnumeric()) == True:
        
        try:
            print(float(value1) / float(value2))
        
        except ZeroDivisionError:
            print("Sayı sıfıra bölünemez")

    elif (value1.isnumeric() and value2.isnumeric()) == False:
        print(value1, value2, sep=" ")
        
    else:
        raise Exception("Girdiğiniz sayıların ikisi de sayı ya da metin olmalı")

    secenek=input("""devam için "e", çıkmak için "h"ye basınız.""")
    if secenek == "h":
        break

# Ya da

while True:
    value1 = input("Değer 1'i giriniz : ")
    value2 = input("Değer 2'yi giriniz : ")

    try:
        if value1.isnumeric() == True and value2.isnumeric() == True: 
            print(float(value1) / float(value2))
        
        elif value1.isnumeric() == False and value2.isnumeric() == False:
            print(value1, value2, sep=" ")
        
        else:
            raise Exception("Girdiğiniz sayıların ikisi de sayı ya da metin olmalı")
    
    except ZeroDivisionError:
        print("Sayı sıfıra bölünemez")

    except:
        print("Hata oluştu")

    secenek=input("""devam için "e", çıkmak için "h"ye basınız.""")
    if secenek == "h":
        break
