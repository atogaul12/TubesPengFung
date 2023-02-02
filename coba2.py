#library
import csv
import os
import functools

#variabel
database = []
kabupaten = []
penerimaan = []
pemakaian = []

#membuka file csv
with open(r"E:/TubesPengFung/stockvaksin.csv") as csvfile:
    readCSV = csv.DictReader(csvfile)
    for row in readCSV:
        database.append(row)

    for data in database:        
        kabupaten1 = str(data['kabupaten'])
        penerimaan1 = int(data['penerimaan'])
        pemakaian1 = int(data['pemakaian'])

        kabupaten.append(kabupaten1)
        penerimaan.append(penerimaan1)
        pemakaian.append(pemakaian1)

def menu():
    print("\n")
    print("=============DATA STOCK VAKSIN COVID 19==========")
    print("1. Tampilkan Data Keseluruhan Stock Vaksin Covid 19")
    print("2. Tampilkan Data Kabupaten Stock Vaksin Covid 19")
    print("3. Total Data Stock Vaksin Covid 19")
    print("4. Filter Huruf Berdasarkan Kabupaten")
    print("5. Urutkan Sesuai Abjad")
    print("6. Huruf Kecil")
    print("7. Huruf Besar")
    print("8. Cari Data Kabupaten")
    print("9. Exit")
    print("\n")
    print("=====================Terima Kasih======================")
    print("\n")

#menampilkan data
def tampil_datas():
    for data in database:
        kabupaten = str(data['kabupaten'])
        penerimaan = int(data['penerimaan'])
        pemakaian = int(data['pemakaian'])
        print("=======================================") 
        print("\n")
        print("kabupaten : ", kabupaten)
        print("penerimaan\t : ", penerimaan, "orang")
        print("pemakaian\t : ", pemakaian, "orang\n")
        print("=======================================") 
    os.system('pause')
    os.system('cls')

def tampil_data():
    kabupaten_input = input("Masukkan nama kabupaten yang ingin ditampilkan: ")
    for data in database:
        kabupaten = str(data['kabupaten'])
        if kabupaten.lower() == kabupaten_input.lower():
            penerimaan = int(data['penerimaan'])
            pemakaian = int(data['pemakaian'])
            print("=======================================") 
            print("\n")
            print("kabupaten : ", kabupaten)
            print("penerimaan\t : ", penerimaan, "orang")
            print("pemakaian\t : ", pemakaian, "orang\n")
            print("=======================================") 
    os.system('pause')
    os.system('cls')

functools.lru_cache

#menghitung total penduduk
def total_pd():
    total_penerimaan = []
    total_pemakaian = []

    a = functools.reduce(lambda x, y: x + y, penerimaan)
    b = functools.reduce(lambda i, u: i + u, pemakaian)

    total_penerimaan.append(a)
    total_pemakaian.append(b)
    
    hasil = (lambda x, y : x - y)(a, b)

    print("===========================================")
    print("DATA STOCK VAKSIN COVID TAHUN 2023")
    print("===========================================")
    print("Total Stock Vaksin : ", hasil)
    print("Jumlah Penerimaan Vaksin : ", a)
    print("Jumlah Pemakaian Vaksin : ", b)
    print("Rasio Stock Vaksin : ", list(map(lambda x, y : x/y*100, total_penerimaan, total_pemakaian)))
    print("===========================================")
    print("\n")
    os.system('pause')
    os.system('cls')

def duplicates(lst, item):
        return [i for i, x in enumerate(lst) if x == item]

#mencari data
def cari():
    kab = input("Masukkan Kabupaten yang akan dicari : ")
    a = duplicates(kabupaten, kab)
    if kab in kabupaten:
        for i in a:
            print("Kabupaten \t : ", kabupaten[i])
            print("Penerimaan\t : ", penerimaan[i], "orang")
            print("Pemakaian\t : ", pemakaian[i], "orang \n")
            os.system('pause')
            os.system('cls')
    else :
        print("Data tidak ditemukan")
        os.system('pause')
        os.system('cls')

#mencari huruf vokal dari nama kabupaten
def filter_pd():
    kabupaten = input("Masukkan nama kabupaten yang ingin Anda filter: ")
    def filter_vocal(abjad):
        vocal = ['a', 'i', 'u', 'e', 'o']
        if abjad in vocal:
            return True
        else:
            return False
    vocal_filter = filter(filter_vocal, kabupaten)
    print(kabupaten, 'Huruf vokal yang tersaring adalah :')
    for vocal in vocal_filter:
        print(vocal)

    def filter_novocal(abjad):
        novocal = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        if abjad in novocal:
            return True
        else:
            return False
    nonvocal_filter = filter(filter_novocal, kabupaten)
    print(kabupaten, 'Huruf non-vokal yang tersaring adalah :')
    for nonvocal in nonvocal_filter:
        print(nonvocal)
    os.system('pause')
    os.system('cls')

#mengurutkan ejaan nama kabupaten
def sorted_list():
    kabupaten = input("Masukkan nama kabupaten yang ingin Anda urutkan ejaannya: ")
    for data in database:
        if data['kabupaten'] == kabupaten:
            kabupaten_sorted = sorted(kabupaten.upper())
            kabupaten_sorted.reverse()
            print(kabupaten,'\n','\t',kabupaten_sorted,'\n')
            break
    else:
        print("Kabupaten tidak ditemukan dalam basis data.")
    os.system('pause')
    os.system('cls')
    
#mengubah nama kabupaten menjadi huruf kecil
def huruf_kecil():
    kabupaten_input = input("Masukkan nama kabupaten: ")
    for data in database:
        if kabupaten_input.lower() == data['kabupaten'].lower():
            kabupaten = str(data['kabupaten'])
            print(kabupaten,'\n', list(map(str.lower, kabupaten)))
            break
    else:
        print("Kabupaten tidak ditemukan.")
    os.system('pause')
    os.system('cls')

#mengubah nama kabupaten menjadi huruf besar
def huruf_besar():
    kabupaten_input = input("Masukkan nama kabupaten: ")
    for data in database:
        if kabupaten_input.upper() == data['kabupaten'].upper():
            kabupaten = str(data['kabupaten'])
            print(kabupaten,'\n', list(map(str.upper, kabupaten)))
            break
    else:
        print("Kabupaten tidak ditemukan.")
    os.system('pause')
    os.system('cls')

#pilihan menu

jawab=True
while(jawab):
    menu()
    pilih_menu = input("Masukkan Pilihan Anda : ")

    if (pilih_menu=="1"):
        tampil_datas()

    elif (pilih_menu=="2"):
        tampil_data()

    elif (pilih_menu=="3"):
        total_pd()

    elif (pilih_menu=="4"):
        filter_pd()
    
    elif (pilih_menu=="5"):
        sorted_list()

    elif(pilih_menu=="6"):
        huruf_kecil()

    elif(pilih_menu=="7"):
        huruf_besar()

    elif(pilih_menu=="8"):
        cari()