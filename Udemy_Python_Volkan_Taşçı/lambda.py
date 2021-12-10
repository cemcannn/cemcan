def ucgen_mi(a,b,hipotenus):
    if a**2 + b**2 == hipotenus**2:
        return True
    else:
        return False

fonk = lambda a,b,hipotenus : a**2 + b**2 == hipotenus**2

print(fonk(3,4,5))