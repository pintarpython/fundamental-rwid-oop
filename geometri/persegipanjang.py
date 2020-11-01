from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):

    def __init__(self, p, l):
        #fungsi yg pertama kali dipanggil saat object diciptakan
        self.p = p
        self.l = l

    def info(self):
        return f'menghitung luas persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l

    def keliling_persegipanjang(self):
        return self.p*2 + self.l*2

