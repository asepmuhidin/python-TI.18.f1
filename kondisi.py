absen=100
tugas=100
uts=60
uas=60

na=(0.4*absen)+(0.1*tugas)+(0.2*uts)+(0.3*uas)

if na >=60:
    ket="Lulus"
else:
    ket="Tidak Lulus"

print ("Nilai akhir anda :" , na, " anda dinyatakan ", ket)

if na >=80:
    grade="A"
elif na>=70:
    grade="B"
elif na>=55:
    grade="C"
elif na>=40:
    grade="D"
else:
    grade="E"
print ("Nilai huruf anda :", grade)   