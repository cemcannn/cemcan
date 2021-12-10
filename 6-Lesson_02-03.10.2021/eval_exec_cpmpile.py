#expression (ifade): değer üreten bir kod bloğunuz varsa bu expression
#statement (deyim): değer üretmezler ifadeleri de kapsayan bir kavramdır.

# eval() : sadece expresiion çalıştır ---------------------------------------------------

eval("a = 5") # değer üretmediği patlar

eval("a = [1,2,3,4]") # değer üretmediği patlar

print(eval("5+7"))

metin = input("matemetiksel işlemi giriniz:")

print(eval(metin))


# exec() : statemen de  çalıştırır ---------------------------------------------------

exec("a = [1,2,3] \nprint(a)")

# compile() :code compile eder daha sonra kullanıma sunar---------------------------------------------------

abc = compile("a = [1,2,3] \nprint(a)","abc","exec")

print(type(abc))

exec(abc)

# üstteki kodu input olarak alıyoruz

code = input("kod bloğu giriniz")
code = "a = [1,2,3] \nprint(a)"

abc = compile(code,"abc","exec")

print(type(abc))

exec(abc)


#https://python-istihza.yazbel.com/gomulu_fonksiyonlar.html