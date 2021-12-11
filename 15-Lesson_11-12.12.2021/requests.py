# # installation : python içindan kurulum yapılmaycak. 
# moduller python dışında yüklenir. doğrudan terminal/command com üzerinde yüklenir.

# # 1. yol
# # python -m pip install requests

# #2. yol
# # pip3 install requests


# bu sayfa test işlemlerinde kullnacaktır.
# https://httpbin.org



import requests

r = requests.get("https://httpbin.org/get")
r2 = requests.get("https://httpbin.org/post", data={"isim":"murat cabuk"})

print(r)

# requestin soınucunu ekrana yazdırıyoruz
print(r.text)


print(r2.text)



# github üzerinden request modülü

response_github = requests.get("https://api.github.com/events")

status_code = response_github.status_code
print(response_github)

print(dir(response_github))

print(status_code)

if status_code == 200:
    #print(response_github.json())

    print(type(response_github.json()))

    print(len(response_github.json()))
    #print(response_github.json()[10])
    print(type(response_github.json()[10]))
    print("-------------------------------------------")
    print(response_github.json()[10]["actor"]["url"])
    print("-------------------------------------------")
    #print(response_github.text)
    print(type(response_github.text))

    print("------------------------------")
    print(type(response_github.cookies))
    print(dir(response_github.cookies))
    print("------------------------------")
    print(response_github.cookies)

    r = requests.get("https://github.com")
    print(r.cookies.keys())
    print(r.cookies["logged_in"])
    

##############################################3 redirection ve history
print("------------------------------------------------------------redirect history")
request_maps_google = requests.get("https://maps.google.com")
print(request_maps_google.status_code)
print(request_maps_google.history)
print(request_maps_google.history[0])



request_github = requests.get("http://github.com/")
print(request_github.status_code)
print(request_github.history)



#####################################33 post işlemi

r = requests.post('https://httpbin.org/post', data={'isim': 'murat çabuk', 'yil':'2021'})
print(r.text)




r_haberler = requests.get("https://www.haberler.com/ara/", params = {"q":"Türkiye"})
print(r_haberler.text)

requests.


