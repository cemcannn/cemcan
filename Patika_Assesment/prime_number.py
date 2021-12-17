def MathChallenge(num):
    list_prime_number = list()
    x=1
    for x in range(2,num+1):
        if num % x == 0:
            list_prime_number.append(x)
    if len(list_prime_number)==1:
        return True
    else:
        return False

print(MathChallenge(int(input("Please enter a number in your mind at the moment : "))))
