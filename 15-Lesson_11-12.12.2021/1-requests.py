# # installation : python içindan kurulum yapılmaycak. 
# moduller python dışında yüklenir. doğrudan terminal/command com üzerinde yüklenir.

# # 1. yol
# # python -m pip install requests

# #2. yol
# # pip3 install requests


# bu sayfa test işlemlerinde kullnacaktır.
# https://httpbin.org


import requests

r = requests.get("https://httpbin.org") # requests modülünün get fonksiyonu ile çekilir ve "r" değişkenine eşitlenir.
r2 = requests.get("https://httpbin.org/post", data={"isim":"murat cabuk"})

print(r) # "r" değişkeni yazdırılınca cevap (Response) olarak bize "200" rakamını verir bu rakamların bir anlamı var.

# # Bu kodların anlamları
# Informational responses (100–199) -> 100-199 arası
# Successful responses (200–299) -> 200-299 arası
# Redirection messages (300–399) -> 300-399 arası
# Client error responses (400–499) -> 400-499 arası
# Server error responses (500–599) -> 500-599 arası

# # requestin sonucunu ekrana yazdırıyoruz yani bütün html kodunu yazdırır ekrana.
# print(r.text)

print(r2.text) # Sitenin HTML içeriğini döndürür.



# github üzerinden request modülü

response_github = requests.get("https://api.github.com/events")

status_code = response_github.status_code # İsteğin HTTP durum kodunu döndürür.
print(response_github)

print(dir(response_github))

print(status_code)

if status_code == 200:
    # print(response_github.json()) # print(response_github.text) ile aynı görevi görüyor fakat type liste olarak 

    print(type(response_github.json()))

    print(len(response_github.json())) 
    print(response_github.json()[10])
    print(type(response_github.json()[10]))
    print("-------------------------------------------")
    print(response_github.json()[10]["actor"]["url"])
    print("-------------------------------------------")
    # print(response_github.text)
    print(type(response_github.text)) # string type

    print("------------------------------")
    print(type(response_github.cookies))
    print(dir(response_github.cookies))
    print("------------------------------")
    print(response_github.cookies)

    r = requests.get("https://github.com")
    print(r.cookies.keys())
    print(r.cookies["logged_in"])
    
######################################## REDIRECTION VE HISTORY

print("------------------------------------------------------------redirect history")
request_maps_google = requests.get("https://maps.google.com")
print(request_maps_google.status_code)
print(request_maps_google.history) # Bir istek attınız ve status_code değeri 200 geldi. Ancak belki 2 kere 301 sonra 1 kere 302 yönlendirme ile en son bir sayfaya geldi ve 200 döndü. Buna bakabilmek için bu method kullanılıyor.
print(request_maps_google.history[0]) # İlk istek

request_github = requests.get("http://github.com/")
print(request_github.status_code)
print(request_github.history)

######################################## PARAMETRE GÖNDERME

r = requests.get("http://httpbin.org/redirect/1",allow_redirects=False) # Sayfa yönlendirmesini iptal ediyor.
print(r.status_code) # Status kod yönlenen sayfa ise "302" verir.

r = requests.get("http://httpbin.org/redirect/1",allow_redirects=True) # Sayfa yönlendirmesini izin veriyor.
print(r.status_code) # Status kod yönlenen sayfa ise "200" verir.

r_haberler = requests.get("https://www.haberler.com/ara/", params = {"q":"Türkiye"}) # Sayfa sonuna Türkiye parametresini ekler.
print(r_haberler.text)

r = requests.post("http://httpbin.org/post", data={"username":"cem","password":"asd123"}) # POST için sanki bir HTML formu doldurmuş ve o bilgileri post etmişiz gibi davranalım.
print(r.json())
print(r.json()["form"]) # Çıktıyı 'username': 'cem', 'password': 'asd123' şeklinde verir.

######################################## REQUESTS

print(r_haberler.request) #  Yaptığınız isteğin ne olduğunu döner, GET,POST v.s.
print(r_haberler.request.method)