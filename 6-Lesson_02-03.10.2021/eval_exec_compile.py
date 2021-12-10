# expression (ifade) : eğer değer üreten bir kod bloğumuzvar ise buna expression deniir.
# statement ( deyim) : tek başına değer üretmez fakat ifadeleri de kapsar.

# eval() 



# print(eval("5+7"))

# metin = input("Yapmak istediğiniz işlemi giriniz")
# print(eval(metin))

# exec() : statemen de çalıştırır

# exec ("a = [1,2,3] \nprint(a)")

## compile() : code compile eder daha sonra

# abc = compile("a=[1,2,3] \nprint(a)","abc","exec")

# print(type(abc)) # type code olduğu görünür.

# exec(abc)

# Üstteki kodu input alarak yazacağız.

code = input("code bloğu giriniz : ")

abc = compile(code,"abc","exec")

exec(abc)

