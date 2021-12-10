# bir class yazacağız aynı anda hem class 

# atttribute leri hem de orneklem attribute leri olacak


class Human:
    test_attributes = "test values"
    test_attributes2=[]
    print(locals())
    def __init__(self):
        self.name=""
        self.height=""
        self.hobbies=[]
        print(locals())
    
    def write_globals_values(self):
        a = globals()
        for i in a:
            print(i)
            print("----------------------------")
        print("#############------############")
        print(locals())




i1 = Human()

print("####################### globals")
i1.write_globals_values()
print("####################### i1 attributes")

print(dir(i1))

print(i1.test_attributes)

i2 = Human()


print(i2.test_attributes)

i1.test_attributes = "Hello"
print(i1.test_attributes)

print(i2.test_attributes)
i2.test_attributes = "Hello2"
print(i2.test_attributes)


i1.test_attributes2.append("a")
print(i1.test_attributes)
i2.test_attributes2.append("b")
print(i1.test_attributes2)
print(i2.test_attributes2)


# sonuc : eğer init dışında bir değişken tanımlarsak (yani attribute veya nitelik) 
# bu nitelik bu class dan oluşturulan ornek (instance, sample) üzerinden doğrudan değiştirilirse yani aracı bir donksiyon kulalnılmazsa 
# class attribute aolarak çalışır 



