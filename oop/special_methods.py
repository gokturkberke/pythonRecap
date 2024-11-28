liste=[1,2,3,4]
print(len(liste)) # 4

isim = "Berke Korkut"
print(len(isim)) # 11

class Urun:
    def __init__(self,urunKodu,urunAdi,urunFiyati):
        self.urunKodu = urunKodu
        self.urunAdi = urunAdi
        self.urunFiyati = urunFiyati
        
    def __len__(self): #sadece bu class için geçerli   
        return self.urunFiyati
    def __str__(self):
        return f"{self.urunKodu} - {self.urunAdi} - {self.urunFiyati}"
    
    #def __repr__(self): da ayni gorevi yapar str ile
    
    def __del__(self):
        print("Urun silindi")
        

urun1=Urun("P001","Bilgisayar",5000)
print(len(urun1)) # 5000
print(str(urun1)) # P001 - Bilgisayar - 5000

del urun1 # Urun silindi
