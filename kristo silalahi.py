#nomor 1
a = "ini hasil kerja saya"
print(a[4:])

#nomor 2
thistuple = ("nokia", "redmi", "oppo", "samsung")
if "oddo" not in thistuple:
    print("daftar tersebut benar")

#nomor 3
a = 4
b = 13
if b==a:
    print("anda mengantuk")
if a<b:
    print("a dan b tidak sama besar")

#nomor 4
txt = "aku menyelesaikan tugas"
if "tugas" not in txt:
    print("aku terlalu santai")
elif "tugas" in txt:
    print("tugasku selesai semuanya")

#nomor 5
kendaraan = ["sepeda", "mobil", "becak", "kereta", "pesawat"]
for x in kendaraan:
    print(x)
    if x == "becak":
        break

#nomor 6
i = 42
while i < 88:
    i += 1
    if i == 69:
        continue
    print(i)

#nomor 7
j = "tugas"
k = "ujian"
l = "akhir"
m = "semester"
n = j+k+l+m
print(n)

#nomor 8
v = "jangan ada tulisan yang CAPSLOCK"
print(v.lower())

#nomor 9
a = "353259"
b = "2.4"
c = "-11"
d = "6"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())

#nomor 10
myorder = "{subject} will have {object}"
print(myorder.format(subject = "I", object = "order"))

#nomor 11
thistuple = ("siapa", "kapan", "mengapa", "bagaimana")
print(len(thistuple))

#nomor 12
a = 6
b = 9
print(a > b)
print(a ==b)
print(a < b)

#nomor 13
txt = "they will accompany her until dawn"
z = txt.replace("they", "kristo")
print(z)