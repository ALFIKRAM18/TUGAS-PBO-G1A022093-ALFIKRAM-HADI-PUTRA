class Mobil:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def info(self):
        print("Ini adalah mobil", self.merk, "tahun", self.tahun, "dengan warna", self.warna)

    def set_tahun(self, tahun_baru):
        self.tahun = tahun_baru
        print("Tahun mobil", self.merk, "telah diubah menjadi", self.tahun)

# membuat objek Mobil
mobil1 = Mobil("Toyota", 2021, "merah")
mobil2 = Mobil("Honda", 2019, "hitam")

# mengakses atribut dari objek Mobil
print(mobil1.merk)
print(mobil2.warna)

# memanggil method pada objek Mobil
mobil1.info()
mobil2.set_tahun(2022)
