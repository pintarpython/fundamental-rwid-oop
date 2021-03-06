import math

from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):

    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Mengitung luas segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi} '

    def hitung_luas(self):
        return self.alas * self.tinggi / 2

    def keliling_segitiga(self):
        return self.alas + self.tinggi + math.sqrt((1 / 2 * self.alas) ** 2 + (self.tinggi) ** 2)
