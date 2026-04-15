1-m
class Kitob:
    def __init__(self, nomi, muallif, sahifa_soni):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def infolar(self):
        print(f"Nomi: {self.nomi}")
        print(f"Muallif: {self.muallif}")
        print(f"Shifa_soni: {self.sahifa_soni}")

k1 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy", 300)
k1.infolar()



# 2-m
class Talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

    def infolar(self):
        print(f"Ismi: {self.ism}")
        print(f"Yosh: {self.yosh}")
        print(f"Kurs: {self.kurs}")

t1 = Talaba("Ali", 20, 2)
t1.infolar()

t2 = Talaba("Vali", 22, 3)
t2.infolar()


# 3-m
class Telefon:
    def __init__(self, model, rang, narx):
        self.model = model
        self.rang = rang
        self.narx = narx

    def infolar(self):
        print(f"Madeli: {self.model}")
        print(f"rang: {self.rang}")
        print(f"narx: {self.narx}")

t1 = Telefon("iPhone 13", "qora", 1200)
t1.infolar()

t2 = Telefon("Samsung S21", "oq", 900)
t2.infolar()


# 4-m
class Mashina:
    def __init__(self, marka, rang, yil):
        self.marka = marka
        self.rang = rang
        self.yil = yil

    def infolar(self):
        print(f"marka: {self.marka}")
        print(f"rang: {self.rang}")
        print(f"yil: {self.yil}")

t1 = Mashina("Cobalt", "oq", 2022)
t1.infolar()

t2 = Mashina("Malibu", "qora", 2023)
t2.infolar()


# 5-m
class Xodim:
    def __init__(self,ism, lavozim, maosh):
        self.ism = ism
        self.lavozim = lavozim
        self.maosh = maosh

    def infolar(self):
        print(f"ism: {self.ism}")
        print(f"lavozim: {self.lavozim}")
        print(f"maosh: {self.maosh}")

t1 = Xodim("Ali", "Dasturchi", 1000)
t1.infolar()

t2 = Xodim("Vali", "Manager", 1500)
t2.infolar()
