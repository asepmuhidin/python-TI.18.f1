class Nilai :
    nim=""
    nama=""
    __tugas=0
    __absen=0
    __uts=0
    __uas=0

    def __init__(self,vnim,vnama) :
        self.nim=vnim
        self.nama=vnama

    def set_Tugas(self,nilai):
        self.__tugas=nilai    

    def get_Tugas(self):
        return self.__tugas  

    def set_Absen(self,nilai):
        self.__absen=nilai    

    def get_Absen(self):
        return self.__absen  

    def set_uts(self,nilai):
        self.__uts=nilai    

    def get_uts(self):
        return self.__uts

    def set_uas(self,nilai):
        self.__uas=nilai    

    def get_uas(self):
        return self.__uas 

    def getNilaiAngka(self) :
        return (0.4* self.get_Absen()) + (0.1* self.get_Tugas())+(0.2* self.get_uts())+(0.3* self.get_uas())            

    def getNilaiHuruf(self):
        ##jika nilai angka saya lebih besar sama dengan 85 maka nilai huruf adalah A
        if (self.getNilaiAngka() >=85) :
            return "A"
        ##jika salah apakah nilai angka >=75, maka nilai hurup B    
        elif(self.getNilaiAngka()>=70) :
            return "B"
        ##jika salah apakah nilai angka >=50, maka nilai hurup C    
        elif(self.getNilaiAngka()>=50) :
            return "C"
        ##jika salah apakah nilai angka >=40, maka nilai hurup D    
        elif(self.getNilaiAngka()>=40) :
            return "D"
        else :
            return "E"

NilaiAlfin=Nilai("0001","Alfin Liau")
print "NIM :",NilaiAlfin.nim
print "Nama :",NilaiAlfin.nama
NilaiAlfin.set_Tugas(100)
NilaiAlfin.set_Absen(80)
NilaiAlfin.set_uts(50)
NilaiAlfin.set_uas(80)
print "Nilai tugas :",NilaiAlfin.get_Tugas()
print "Nilai absen :",NilaiAlfin.get_Absen()
print "Nilai uts :",NilaiAlfin.get_uts()
print "Nilai uas :",NilaiAlfin.get_uas()
print "Nilai Angka :",NilaiAlfin.getNilaiAngka()
print "Nilai Huruf :",NilaiAlfin.getNilaiHuruf()
