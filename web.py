import streamlit as st
import csv
import functools
from PIL import Image

st.title("TUBES PEMROGRAMAN FUNGSIONAL")
images = ['Anggoro.jpg', 'Atoekss.jpg', 'bayu.jpg']

for image_name in images:
    image = Image.open(image_name)
    st.image(image, width=300)
    if image_name == 'Anggoro.jpg':
        st.write("Muhammad Anggoro Chandravita (21102179)")
    elif image_name == 'Atoekss.jpg':
        st.write("M. Ato' Ulloh (21102165)")
    elif image_name == 'bayu.jpg':
        st.write("Tri Bayu Priangga (21102158)")

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
    st.title("Data Stock Vaksin COVID-19")
    st.header("Menu:")
    st.write("1. Tampilkan Data Keseluruhan Stock Vaksin Covid 19")
    st.write("2. Tampilkan Data Kabupaten Stock Vaksin Covid 19")
    st.write("3. Total Data Stock Vaksin Covid 19")
    st.write("4. Filter Huruf Berdasarkan Kabupaten")
    st.write("5. Urutkan Sesuai Abjad")
    st.write("6. Huruf Kecil")
    st.write("7. Huruf Besar")
    st.write("8. Cari Data Kabupaten")

#menampilkan data
def tampil_datas():
    st.header("Data Stock Vaksin COVID-19")
    for data in database:
        kabupaten = str(data['kabupaten'])
        penerimaan = int(data['penerimaan'])
        pemakaian = int(data['pemakaian'])
        st.write("=======================================")
        st.write("\n")
        st.write("kabupaten : ", kabupaten)
        st.write("penerimaan\t : ", penerimaan, "orang")
        st.write("pemakaian\t : ", pemakaian, "orang\n")
        st.write("=======================================")

def tampil_data():
    kabupaten_input = st.text_input("Masukkan nama kabupaten yang ingin ditampilkan: ")
    for data in database:
        kabupaten = str(data['kabupaten'])
        if kabupaten.lower() == kabupaten_input.lower():
            penerimaan = int(data['penerimaan'])
            pemakaian = int(data['pemakaian'])
            st.write("=======================================") 
            st.write("kabupaten : ", kabupaten)
            st.write("penerimaan\t : ", penerimaan, "orang")
            st.write("pemakaian\t : ", pemakaian, "orang")
            st.write("=======================================")

#menghitung total penduduk
def total_pd():
    total_penerimaan = []
    total_pemakaian = []
    a = functools.reduce(lambda x, y: x + y, penerimaan)
    b = functools.reduce(lambda i, u: i + u, pemakaian)

    total_penerimaan.append(a)
    total_pemakaian.append(b)

    hasil = (lambda x, y : x - y)(a, b)
    st.header("Total Data Stock Vaksin COVID-19")
    st.write("===========================================")
    st.write("DATA STOCK VAKSIN COVID TAHUN 2023")
    st.write("===========================================")
    st.write("Total Stock Vaksin : ", hasil)
    st.write("Jumlah Penerimaan Vaksin : ", a)
    st.write("Jumlah Pemakaian Vaksin : ", b)
    st.write("Rasio Stock Vaksin : ", list(map(lambda x, y : x/y*100, total_penerimaan, total_pemakaian)))
    st.write("===========================================")

#mencari data
def cari():
    kabupaten = st.text_input("Masukkan Kabupaten yang akan dicari : ")
    found = False
    for data in database:
        if data['kabupaten'] == kabupaten:
            found = True
            st.success("Data Kabupaten Berhasil Dicari")
            st.write("Kabupaten \t : ", data['kabupaten'])
            st.write("Penerimaan\t : ", data['penerimaan'], "orang")
            st.write("Pemakaian\t : ", data['pemakaian'], "orang")
    if not kabupaten:
        st.warning("Silahkan masukkan Kabupaten")
    else:
        if not found:
            st.error("Data tidak ditemukan")

#mencari huruf vokal dari nama kabupaten
def filter_pd():
    kabupaten = st.text_input("Masukkan nama kabupaten yang ingin Anda filter: ")
    def filter_vocal(abjad):
        vocal = ['a', 'i', 'u', 'e', 'o']
        if abjad in vocal:
            return True
        else:
            return False
    vocal_filter = filter(filter_vocal, kabupaten)
    st.write(kabupaten, 'Huruf vokal yang tersaring adalah :')
    for vocal in vocal_filter:
        st.write(vocal)

    def filter_novocal(abjad):
        novocal = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        if abjad in novocal:
            return True
        else:
            return False
    nonvocal_filter = filter(filter_novocal, kabupaten)
    st.write(kabupaten, 'Huruf non-vokal yang tersaring adalah :')
    for nonvocal in nonvocal_filter:
        st.write(nonvocal)

def sorted_list():
    kabupaten = st.text_input("Masukkan nama kabupaten yang ingin Anda urutkan ejaannya: ")
    for data in database:
        if data['kabupaten'] == kabupaten:
            kabupaten_sorted = sorted(kabupaten.upper())
            if st.checkbox('Urutkan dari bawah ke atas'):
                kabupaten_sorted.reverse()
                st.write(kabupaten,'\n')
                st.write('\t',kabupaten_sorted)
                break
            else:
                st.write(kabupaten,'\n')
                st.write('\t',kabupaten_sorted)
    else:
        st.write("Kabupaten tidak ditemukan dalam basis data.")


#mengubah nama kabupaten menjadi huruf kecil
def huruf_kecil():
    kabupaten_input = st.text_input("Masukkan nama kabupaten: ")
    for data in database:
        if kabupaten_input.lower() == data['kabupaten'].lower():
            kabupaten = str(data['kabupaten'])
            st.write(kabupaten,'\n', list(map(str.lower, kabupaten)))
            break
    else:
        st.write("Kabupaten tidak ditemukan.")

#mengubah nama kabupaten menjadi huruf besar
def huruf_besar():
    kabupaten_input = st.text_input("Masukkan nama kabupaten: ")
    for data in database:
        if kabupaten_input.upper() == data['kabupaten'].upper():
            kabupaten = str(data['kabupaten'])
            st.write(kabupaten,'\n', list(map(str.upper, kabupaten)))
            break
    else:
        st.write("Kabupaten tidak ditemukan.")

#menjalankan program
menu()
pilihan = st.number_input("Masukkan Pilihan : ")
if pilihan == 1:
    tampil_datas()
elif pilihan == 2:
    tampil_data()
elif pilihan == 3:
    total_pd()
elif pilihan == 4:
    filter_pd()
elif pilihan == 5:
    sorted_list()
elif pilihan == 6:
    huruf_kecil()
elif pilihan == 7:
    huruf_besar()
elif pilihan == 8:
    cari()
else:
    st.error("Input tidak valid, silahkan coba lagi")