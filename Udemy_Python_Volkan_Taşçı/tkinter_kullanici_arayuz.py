from tkinter import * # tkinter modülünde her şeyi çekiyoruz.
pencere= Tk() # pencere adında bir modülü Tk class ına tanımlıyoruz.

asil_isim="mahmut" #  isim 
asil_parola="mehmet" # parola giriyoruz

def giris_yapma(): # giris yapma fonksiyonu yazıyoruz
    parola = parola_giris.get() #parola_giris objesine get fonksiyonu ile parola objesine eşitliyoruz.
    isim = isim_giris.get() #isim_giris objesine get fonksiyonu ile isim objesine eşitliyoruz.
    if parola == asil_parola and isim == asil_isim: #eğer parola yukarıda tanımladığımız asıl parolaya eşit ise ve isim yukarıda tanımladığımız asıl isme eşit ise bizi aşağıdaki
        giris_durumu.config(text = "Doğru", bg="green") #configürasyonu oluşturuyor, ekranda doğru yazıyor ve text arka planı yeşil ile veriyor.
    else:
        giris_durumu.config(text = "Yanlış", bg="red") #Değilse yanlış veriyor ve text arka planı kırmızı ile veriyor

isim = Label(pencere, text = "adınız") #isim objesi Label class ı ile ekrana bastırılır
isim.grid(row=0,column=0) # ekrana bastırılacak objenin bulunduğu sütun ve kolonda olacağı grid fonksiyonu ile yapılır
isim_giris = Entry(pencere, width="8") # girilen ismin nereye girileceğini ve ne kadar genişlikte karakter yazılabileceği Entry class ı ile yapılır
isim_giris.grid(row = 0, column = 1 ) # girlecek isim alanı hangi sütun ve kolonda olacağı grid fonksiyonu

parola = Label(pencere, text ="parolanız") # yukarıda aynı parametreler
parola.grid(row=1,column=0)
parola_giris = Entry(pencere, width="8",show="*") # isimden farklı olarak yazılan parolanın görünmemesi için * koyulur
parola_giris.grid(row=1,column=1)

sifremi_hatirla = Checkbutton(pencere,text ="şifremi hatırla") # şifremi hatırla butonu, Checkbutton class ı ile eklenir
sifremi_hatirla.grid(row=2,columnspan=2)

giris = Button(pencere, text="giriş",command=giris_yapma) # giriş butonu Button class ı ile eklenir, pencere objesine ekleneceğini, text de giriş yazacağını ve giriş_yapma fonksiyonunu çalıştıracağını ifade eder.
giris.grid(row=3,column=0)
giris_durumu= Label(pencere, text="")
giris_durumu.grid(row=3,column=1)

pencere.mainloop() # pencere objesinin devamlı açık kalması mainloop fonksiyonu ile gerçekleşir.
