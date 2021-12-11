# https://docs.python.org/3/library/json.html

kitaplar_json_string='{"tip": "kitap","tur": "roman", "urunler": [ '\
                                    '{"ad": "Ihtiyar Kemanci", "yazar": "Nihat Genc"},'\
                                    '{"ad": "Su Cilgin Turkler", "yazar": "Turgut Ozakman"},'\
                                    '{"ad": "Kar", "yazar": "Orhan Pamuk"}'\
                                ']}'

print(kitaplar_json_string)

################################################3  python a dönüştürme
kisi =  '{ "name":"John", "age":30, "city":"New York"}'

kisi_python = {"name":"John", "age":30, "city":"New York"}

import json

python_object = json.loads(kisi)

print(type(python_object))

print(python_object)
print("---------------------")
print(kisi_python)

kitaplar_python = json.loads(kitaplar_json_string)

print(kitaplar_python)

print(type(kitaplar_python["urunler"]))

print(kitaplar_python["urunler"][0]["ad"])

############################################333 python opbjesini json (str) objesine çevirmek

print("----------------------------- python opbjesini json (str) objesine çevirmek")
kisiler = {
    "başlık":"kişi listesi",
    "açıklama":"kişileri listeler",
    "kişiler":[
            { "name":"John1", "age":10, "city":"New York1"},
            { "name":"John2", "age":20, "city":"New York2"},
            { "name":"John3", "age":30, "city":"New York3"},
            { "name":"John3", "age":40, "city":"New York4"},
            { "name":"John4", "age":50, "city":"New York5"}
    ]
}


kisiler_json = json.dumps(kisiler,indent=2, sort_keys=True, ensure_ascii=False)
print(type(kisiler_json))
print(kisiler_json)

########################33 json validation

def is_json(json_str):
    try:
        json.loads(json_str)
    except ValueError as e:
        return "False"

    return "True"


print("{} : " + is_json("{}"))
print("{asd} : " + is_json("{asd}"))
print("{'yas':'30'} : " + is_json("{'yas':'30'}"))
print("{'\yas\':30} : " + is_json("{'\yas\':30}"))





















