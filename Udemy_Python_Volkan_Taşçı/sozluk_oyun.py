zırhlar = {"demir":10,"çelik":20}

karakterler = {
    "karakter1" :{
    "sağlık"    : 100,
    "güç"       : 30,
    "silah"     : "kılıç",
    "kalkan"    : zırhlar["çelik"]
    },
    "karakter2" : {
    "sağlık"    : 100,
    "güç"       : 30,
    "silah"     : "kılıç",
    "kalkan"    : zırhlar["demir"]
    }
}

def vur(saldiran,saldirilan):
    guc = saldiran["güç"]
    saglik = saldirilan["sağlık"]
    zirh = saldirilan ["kalkan"]
    damage = guc - zirh
    saglik = saglik - damage
    saldirilan["sağlık"] = saglik

vur(karakterler["karakter1"],karakterler["karakter2"])

print(karakterler["karakter2"])