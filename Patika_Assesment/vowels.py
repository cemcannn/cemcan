def StringChallenge(strParam):
    alphabet    = "abcdefghijklmnopqrstuvwxyz"
    vowels      = "aeiou"
    list_param  = list()

    for i in strParam:
        if i in alphabet:
            alphabet.index(i)
            i = alphabet[alphabet.index(i)+1]
            if i in vowels:
                list_param += i.upper()
            else:
                list_param += i
    
    return list_param

print(StringChallenge(input("Please enter a word in your mind in a moment : ")))

