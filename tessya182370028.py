" Program Kalkulator Sederhana Untuk Menghitung Penjumlahan, Pengurangan, Perkalian, dan Pembagian Dengan Menggunakan Fungsi "
# fungsi penjumlahan
def tambah(x, y):
   return x + y
# fungsi pengurangan
def kurang(x, y):
   return x - y
# fungsi perkalian
def kali(x, y):
   return x * y
# fungsi pembagian
def bagi(x, y):
   return x / y
# menu operasi
print("Pilih Operasi.")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
# Meminta input dari user
choice = input("Masukkan Pilihan (1/2/3/4): ")
num1 = int(input("Masukkan Bilangan Pertama: "))
num2 = int(input("Masukkan Bilangan Kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", tambah(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", kurang(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", kali(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", bagi(num1,num2))
else:
   print("Input salah")