# 1. rakamlardan oluşan bir listede sistem rastgele bir sayı seçecek.
# 2. Sistem kullanıcıya seçilen rakamı tahmin edebilmesi için input sunacak.
# 3. Kulanıcının her tahmini sistem tarafından kaydedilecek.
# 4. Sistem her tahminden sonra kullanıcının tahmin ettiği rakamın sistemin seçtiği rakamdan büyük ya da küçük olduğunu kullanıcıya söyleyecek.
# 5. Kullanıcı doğru tahmin ettiğinde sistem kullanıcının bütün tahminlerini listeleyecek.
# 6. Sistem her tahminden sonra kullanıcıya devam edip etmeyeceğini soracak.
import random
rakamlar = list(range(1,21))
rastgele_sayi = random.choice(rakamlar)
t=0
i=0
liste = []
while 1==1:
    kullanici_tahmini = int(input("Lütfen bir rakam giriniz : "))
    i=i+1
    liste.append(kullanici_tahmini)
    
    if kullanici_tahmini == rastgele_sayi:
        print("Doğru rakamı girdiniz,tebrikler.")
        break

    elif kullanici_tahmini <= rastgele_sayi:
        print("girdiğiniz sayı rastgele sayıdan küçük.")
                
    else:
        print("girdiğiniz sayı rastgele sayıdan büyük.")
                
    secenek = input("""
                    devam etmek için    (e) 
                    çıkmak için         (h) 
                    yazıp enter tuşuna basınız : """)
        
    if secenek == "e":
        t = t + 1
        print("programa devam ediyorsunuz")
        pass
    elif secenek == "h":
        print("programdan başarıyla çıktınız.")
        break
    else:
        print("lütfen doğru seçeneği giriniz.")

    

for i in range(len(liste)):
    print(f"{i+1}. denemede {liste[i]} değerini girdiniz.")

