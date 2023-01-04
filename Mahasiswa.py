# membuat class dengan kata kunci class itu sendiri

class Mahasiswa:
    #atribut
   # nama = ""
   # nim = ""
    #rombel = ""
    def __init__(self, nim, nama, rombel):
        #Variabel object
        self.nim = nim
        self.nama = nama
        self.rombel = rombel 
    
    #methode/fungsi
    def lulus(self, nilai):
        if (nilai > 90):
            print("lulus")
        elif (nilai< 1 ):
            print("Keterlaluan")
        else:
            print("tidak lulus")

#Class mahasiswa memiliki 3 atribut dan 1 fungsi
# def = fungsi
    def cetak(self):
        print("Nama :", self.nama)
        print("NIM :", self.nim)
        print("Rombel :", self.rombel)

#Membuat Objek
mahasiswa1 = Mahasiswa("0110", "Jay", "TI-5")

#mencetak Atribut
mahasiswa1.cetak()
mahasiswa1.lulus(0)

# Objek ke-2
mahasiswa2 = Mahasiswa("0111", "Andy", "TI-9")

#Cetak Atribut
mahasiswa2.cetak()
mahasiswa2.lulus(80)
#print(help(mahasiswa1))