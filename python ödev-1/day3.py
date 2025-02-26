# sınıflar => classlar
# modules
# paket yönetimi
# self => this

class Human:
    name = "Ceren"
     # built-in
     # constructor
     # initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'ı üretildi")
    def __str__(self):
        return f"Str Fonksiyonundan dönen değer: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

# instance => örnek
human1 = Human("Ceren")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Kerem")
human2.talk("Selam")
human2.walk()
print(human2)

