import time

print("masukkan nama anda : ")
nama = input()
print("masukkan nim anda : ")
nim = input()

print("nama = "+nama + " nim = "+nim)
print("masukkan nilai SMR : ")
smr = input()
print("nilai SMR =  " + smr)

print("menghitung nilai SMR dan Menampilkan rekomendasinya")
time.sleep(2)  # tunggu kode selama 2 detik

for item in range(0, 5):
    print(".")
    time.sleep(1)

print("selesai menghitung")
time.sleep(3)  # tunggu kode selama 2 detik
smr = int(smr)
if (smr > 0) & (smr <= 20):
    print("kelas 5")
    print("sangat buruk")
    print("rekomendasi penguatan = ")
    print("rex walls")
    print("surface drainage")
elif (smr > 20) & (smr <= 40):
    print("kelas 4")
    print("buruk")
    print("rekomendasi penguatan = ")
    if (smr < 30):
        print("rex walls")
    print("surface drainage")
    print("shotcrete dental concrete")
    if (smr > 30):
        print("bolt anchor")
elif (smr > 40) & (smr <= 60):
    print("kelas 3")
    print("normal")
    print("rekomendasi penguatan = ")
    print("shotcrete dental concrete")
    print("bolt anchor")
    if (smr > 45):
        print("toe ditch")
elif (smr > 60) & (smr <= 80):
    print("kelas 2")
    print("baik")
    print("rekomendasi penguatan = ")
    if (smr < 70):
        print("toe ditch")
    if (smr < 75):
        print("bollt anchor")
    if (smr > 65):
        print("scaling none")
elif (smr > 80) & (smr <= 100):
    print("kelas 1")
    print("sangat baik")
    print("rekomendasi penguatan = ")
    print("scaling none")
else:
    print("nilai yang anda masukkan salah")
    print("silahkan periksa kembali nilai SMR")
