from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga


print('Menggunakan OOP')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(f'luas persegi panjang = {p1.hitung_luas()}')
print(f'keliling persegi panjang = {p1.keliling_persegipanjang()}')

s1 = Segitiga(4, 3)
print(f'\n{s1.info()}')
print(f'luas segitiga = {s1.hitung_luas()}')
print(f'Keliling segitiga = {s1.keliling_segitiga()}')

b1 = BangunRuang()
print(f'\n{b1.info()}')
print(b1.hitung_luas())

#Polymorphism = kemampuan object untuk merespon berbeda, terhadap pemanggilan method yg sama
print('\nPolymorphism')
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

for dbr in daftar_bangun_ruang:
    print(dbr.info())


