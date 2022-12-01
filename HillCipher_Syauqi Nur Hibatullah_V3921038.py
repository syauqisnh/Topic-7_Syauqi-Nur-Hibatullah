#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import numpy as np

# untuk enkripsi
def cipher_encryption():
  #mendenifisikan variable msg sebagai inputan
    msg = input("Enter message: ").upper()
    msg = msg.replace(" ", "")

    # jika panjang pesan/berjumlah ganjil, tambahkan 0 di akhir
    len_chk = 0 #variable len_chk didefinisikan sebagai nol
    if len(msg) % 2 != 0: 
        msg += "0"
        len_chk = 1

    # hasil dari msg/inputan diteruskan ke matriks 2x2
    row = 2 #baris 2
    col = int(len(msg)/2) #kolom 2
    # msg2d didefinisikan sebagai matriks 2x2 yang sudah terdapat value inputan
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0: #kondisi jika matriks pada bagian i adalah hur
            msg2d[0][itr1] = int(ord(msg[i])-65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i])-65)
            itr2 += 1

    # memasukkan kunci
    # mendefinisikan variable key sebagai inputan untuk memasukkan key/kunci
    # pada program ini key yang dimasukkan berupa huruf bukan angka
    # misalnya ada key dengan [6] [1] [3] [2] berarti key yang dimasukkan adalah GBDC
    key = input("Enter 4 letter Key String: ").upper()
    key = key.replace(" ", "")

    # perhitungan matriks 2x2 untuk key/kunci 
    # key2d sebagai nilai dari kunci dengan matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3])-65
            itr3 += 1

    # mencek validasi dari kunci/key
    # perhitungan untuk determinan
    # variable deter didefinisikan untuk perhitungan determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]  #setiap kunci akan dikalikan dengan matriks dari inputan plaintext 
    # hasil dari perhitungan tadi di mod 26
    deter = deter % 26

    # perhitungan perkalian invers
    # mul_inv didefinisikan = -1
    mul_inv = -1
    for i in range(26): #kondisi untuk nilai i pada range (26)
        temp_inv = deter * i # temp_inv didefinisikan sebagai perhitungan deter (hasil tadi) dengan i
        if temp_inv % 26 == 1: # jika value temp_inv di mod sama dengan 1 maka akan dilakukan break
            mul_inv = i # disini i memiliki value sama dengan mul_inv yaitu -1
            break
        else:
          # jika keadaan lainnya maka akan dilakukan continue
            continue

    # jika mul-inv bernilai sama dengan -1 maka akan print invalid key
    if mul_inv == -1:
        print("Invalid key")
        sys.exit()

    # if
    # memasukkan enkripsi teks
    encryp_text = ""
    itr_count = int(len(msg)/2) #dari inputan plainteks tersebut akan dibagi menjadi 2 huruf 2 huruf
    if len_chk == 0:
        #perhitungan untuk jumlah genap
        for i in range(itr_count): 
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    else:
      #perhitungan untuk jumlah ganjil
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    # if else
    # print hasil
    print("Encrypted Text: {}".format(encryp_text))

# Untuk dekripsi
def cipher_decryption():
    msg = input("Enter message: ").upper()
    msg = msg.replace(" ", "")

    # jika panjang teks adalah angka ganjil, tambahkan 0 di akhir
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # inputan teks pada matriks 2x2
    row = 2
    col = int(len(msg) / 2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    #perhitungan dalam matriks 2x2
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i]) - 65)
            itr2 += 1
    # for
    #memasukkan kunci/key
    # pada program ini key yang dimasukkan berupa huruf bukan angka
    # misalnya ada key dengan [6] [1] [3] [2] berarti key yang dimasukkan adalah GBDC
    key = input("Enter 4 letter Key String: ").upper()
    key = key.replace(" ", "")

    # Perhitungan kunci untuk matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1
    # for

    # Perhitungan determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # Perhitungan perkalian invers
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    # matriks adjoin
    # pertukaran pada matriks
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

    # mengubah tanda minus/memberi tanda minus 
    key2d[0][1] *= -1
    key2d[1][0] *= -1

    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    # perkalian invers dengan matriks yang sudah di adjoin
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv

    # perhitungan mod
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    # perhitungan ke dektipsi teks
    decryp_text = ""
    itr_count = int(len(msg) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    # if else
    # menampilkan hasil dekripsi
    print("Decrypted Text: {}".format(decryp_text))

# menu untuk memilih no 1 untuk enkripsi no 2 untuk dekripsi
def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("---Encryption---")
        cipher_encryption()
    elif choice == 2:
        print("---Decryption---")
        cipher_decryption()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()