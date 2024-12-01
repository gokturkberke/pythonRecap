def urunEkle(urunAdi,fiyat,stoktami,kategoriler):
    urun = {
        "urunAdi": urunAdi,
        "fiyat": fiyat,
        "stoktami": stoktami,
        "kategoriler": kategoriler
    }
    import json
    with open("urunler.json","w") as file:
        json.dump(urun,file,ensure_ascii=False)
        
urunEkle("LG 75",13000,True,["televizyon","elektronik"])

def urunleriGetir():
    import json
    with open("urunler.json") as file:
        urun = json.load(file)
    kategoriler = " ".join([kategori for kategori in urun['kategoriler']])
        
    print(f"Ürün Adı: {urun['urunAdi']} Fiyat: {urun['fiyat']} Stokta mı: {urun['stoktami']} Kategoriler: {urun['kategoriler']}")

urunleriGetir() # Ürün Adı: LG 75 Fiyat: 13000 Stokta mı: True Kategoriler: ['televizyon', 'elektronik']
