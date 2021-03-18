print("NILAI IPK MAHASISWA")
tugas = float(input("\nMasukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilaiAkhir =  (0.30 * tugas) + (0.30 * uts) +  (0.40 * uas)
if nilaiAkhir >= 80:
    indeks = 'A'
elif nilaiAkhir >= 70:
    indeks = 'B'
elif nilaiAkhir >= 55:
    indeks = 'C'
elif nilaiAkhir >= 40:
    indeks = 'D'
else:
    indeks = 'E'

print("\nNilai Akhir  = %0.2f" % nilaiAkhir)
print("Nilai Indeks = %c" % indeks)
