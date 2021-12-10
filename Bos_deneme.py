num = int(input("sayı giriniz"))

def prime_number(num):
    list1= []
    x = 1
    for x in range(2,num):
        if int(num) % x == 0:
            list1.append(x)
        if len(list1) == 0:
            return True
        else:
            return False

print(prime_number(num))