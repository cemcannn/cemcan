class Humanbeing:
    def __init__(self):
        self.name=""
        self.height=""
        self.hobbies=[]
    def do_sport(self, sport_branches:str, hours: int): #It is name is sampling methods and it is started to written with self
        print(str(hours), "hours", sport_branches, "played", )
    def walk(self, step_numbers:int):
        print(str(step_numbers), "steps taken")
    def show_persons_name(self):
        print(self.name)

cem = Humanbeing()
cem.name="Cem"
cem.height=1.76
cem.hobbies.append("soccer")
cem.hobbies.append("pingpong")

print(f"name: {cem.name}, height:{cem.height}, hobbies: {cem.hobbies}")
cem.do_sport("pingpong",1)
cem.do_sport("soccer",2)

cem.walk(100)

cem.show_persons_name()
