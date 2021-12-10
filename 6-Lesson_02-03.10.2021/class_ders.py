# Firs letter of Class is upper
# Class is block 

# Basic class

# class Insan:
#     pass

# class Insan():
#     pass

# It has 2 type of using.

## (Class Attribute)

# class Humanbeing:
#     name        = ""
#     height      = 0
#     weight      = 0
#     eye_colour  = ""
#     hobbies     = ""


# Humanbeing.name         = "Cem"
# Humanbeing.height       = 1.76
# Humanbeing.weight       = 78
# Humanbeing.eye_colour   = "brown"
# Humanbeing.hobbies      = ["shooting", "swimming","reading"] 

# print(Insan)
# print(dir(Insan))
# print(dir(Insan.__dict__))
# print(dir(Insan.__dict__.items()))
# print(dir(Insan.__dict__.keys()))

# cem = Humanbeing
# print(cem.height)

# cem.height=2
# print(cem.height)

# print("Human Being      : ", id(Humanbeing))
# print("Human Being Cem  : ", id(cem))

# print(hex(id(Humanbeing))) # Hex is transform to hexademical system and indicate in system adresses

# def writeonscreen(name:str, height:int, eye_colour:str,hobbies:list[str]):
#     print(f"{name},{height},{eye_colour},{hobbies}")

# writeonscreen("cem",1.70,"brown","shooting")

# Or you can write like below

# def writeonscreen(a:Humanbeing):
#     print(f"{a.name},{a.height},{a.eye_colour},{a.hobbies}")

# writeonscreen(cem)

## Instantiation (Instance, Sampling, Örnekleme)

# class Humanbeing:
#     name        = "Human"
#     height      = 0
#     weight      = 0
#     eye_colour  = ""
#     hobbies     = ""

# cem     = Humanbeing()
# gozde   = Humanbeing()

# cem.name    ="Cem"
# cem.height  =1.76
# cem.hobbies  =["riding on the storms"]

# gozde.name  ="Gözde"
# gozde.height  =1.60
# gozde.hobbies  =["working"]

# cem.hobbies.append("ada")

# print(cem.name)
# print(gozde.name)
# print(Humanbeing.name)
# print(Humanbeing().name)

# def writeonscreen(a:Humanbeing):
#     print(f"{a.name},{a.height},{a.eye_colour},{a.hobbies}")

# writeonscreen(cem)
# writeonscreen(gozde)

## Instation Attributes (Örnek nitelikleri)

# __init__ , self  # "double under score" = 2 alt çizgi, shortcut = "dunder"

#__init__(): Inıtializing, it is object, ilk kez  oluşturulduğunda çalışan fonksiyon.
# self : oluşturulan objenin (nesnenin) bizzat kendisini ifade eder. Self sadece bir kavram, bu kelime kullanılmak zorunda değil.

class Humanbeing():
    def __init__(self):    
        self.name        = "insan"
        self.height      = 0
        self.weight      = 0
        self.eye_colour  = ""
        self.hobbies     = []

cem     = Humanbeing()
gozde   = Humanbeing()

cem.hobbies.append("Soccer")
gozde.hobbies.append("Volleyball")

print(cem.hobbies)
print(gozde.hobbies)

print(type(cem))
print(type(Humanbeing))

