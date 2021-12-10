# lazy evalution : yani çağrıldıüında veri üretmek demektir.
# generator lar lazy evaluation a sahiptir.
# yield keyword u kullanılarak yazılırlar

def yavas_calis():
    print("bir")
    yield
    print("iki")
    yield
    print("üç")
    yield


a  = iter(yavas_calis())
print(a)

print(next(a))
print(next(a))
print(next(a))

# generator ile fibonacci sayısı üretme

def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b


fibo_generator = fibo()

iter_fibo = iter(fibo_generator)
print(next(iter_fibo))
print(next(iter_fibo))
print(next(iter_fibo))
print(next(iter_fibo))
print(next(iter_fibo))
print(next(iter_fibo))
print(next(iter_fibo))

for i in fibo_generator:
    if i < 30:
        print(i)
    else:
        break



def yavas_calis():
    return 1

def yavas_calis():
    g = 10+2
    yield g
    yield 2
    yield 3

a = iter(yavas_calis())
print(next(a))
print(next(a))
print(next(a))
