class Pegawai(object):
    def __init__(self, nama, jaga, jabatan):
        self.nama = nama
        self.jaga = jaga
        self.jabatan = jabatan

    def datang(self):
        print("Pegawai Masuk")

    def nanti(self):
        print("Pegawai Belum Datang")
	


# class Set turunan dari class Pegawai
class Set(Pegawai):
    pass
	
a = Set("Budi", "Pagi", "Kepala Perpustakaan")
print()
print("Nama:", a.nama)
print("Jabatan:", a.jabatan)
print("Jadwal Masuk:", a.jaga)
a.datang()

b = Set("Eko", "Siang", "Penjaga Perpustakaan")
print()
print("Nama:", b.nama)
print("Jabatan:", b.jabatan)
print("Jadwal Masuk:", b.jaga)
b.nanti()