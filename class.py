class Mashina:
    def __init__(self, rang, model, tezlik):
        self.rang = rang
        self.model = model
        self.tezlik = tezlik
      #1-metod gaz_ber
    def gaz_ber(self, miqdor):
        self.tezlik += miqdor
        # 2-metod tormozlar
    def tormozla(self, miqdor):
        self.tezlik -= miqdor
        if self.tezlik < 0:
            self.tezlik = 0

gentra = Mashina("Qora", "Gentra", 200)
nexia = Mashina("Oq", "Nexia 3", 180)
damas = Mashina("oq", "Damas 2", 300)

damas.gaz_ber(50)
damas.tormozla(400)

print(f"Gentra rang: {gentra.rang}\nGentra model: {gentra.model}\nGentra tezlik: {gentra.tezlik} km/s")
print(f"Nexia rangi: {nexia.rang}\nNexia modeli: {nexia.model}\nNexia tezlik: {nexia.tezlik} km/s")
print(f"Damas rangi: {damas.rang}\nDamas modeli: {damas.model}\nDamas tezlik: {damas.tezlik} km/s")
