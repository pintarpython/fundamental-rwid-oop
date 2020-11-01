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

print('mencoba push ke github')


