# Praktikum II Komputasi Numerik (C) 2022 Teknik Informatika ITS
# Kelompok C04
# - Richie Seputro         [5025211213]
# - Moh. Taslam Gustino P. [5025211011]
# - Ali Hasyimi Assegaf    [5025211131]
# ~ Made with Love ~

# Import modul-modul yang diperlukan
# Pastikan modul-modul beriku telah di-install di komputer Anda
import math
import numpy as np
import matplotlib.pyplot as plt

# Fungsi yang diaproksimasi, harus di hardcode di script python!
f = lambda x: x**10 + 9*x**9 + 3.4*x**8 + 7*x**7 + x**6 - x**5 + 4*x**4 - 2*x**3 + x**2 - 53*x

# Fungsi Integrasi Trapezoida
# n: jumlah pias, a: batas bawah, b: batas atas
def trapezoid_integration(n, a, b):
    # Menghitung delta-x atau h
    # abs() untuk mencegah kesalahan posisi batas bawah dan batas atas
    h = abs(b - a) / n
    
    # Menghitung deret tengah (deret sigma)
    s = 0
    for i in range(1, n):
        s += 2 * f(a + i * h)
    
    # Mengembalikan nilai aproksimasi
    return h / 2 * (f(a) + s + f(b))

# Program dimulai di sini.
def main():
    print("Program aproksimasi Romberg dimulai.")
    # Variable untuk batas atas dan batas bawah integrasi
    # a: batas bawah, b: batas atas
    a = 0
    b = 5
    # Membuat array 2 dimensi 100x100
    arr = np.zeros((100,100))
    # Error aproksimasi (dalam persen)
    err_apr = 100
    # Jumlah pias
    n = 1
    # Pangkat untuk menghitung ulang n
    i = 1
    # Toleransi error
    err_tol = 0.001

    # Hitung elemen pertama di matriks
    arr[1, 1] = trapezoid_integration(n, a, b)

    # Tampilkan header kolom
    print("i\tError\t\tI")

    # Hitung sampai error aproksimasi kurang dari toleransi error
    while err_apr > err_tol:
        # Perbanyak pias
        n = 2 ** i
        # Masukkan nilai aproksimasi Trapezoida selanjutnya ke matriks
        arr[i + 1, 1] = trapezoid_integration(n, a, b)

        # Integrasi Romberg untuk mengisi cell-cell matriks
        for k in range(2, i + 2):
            j = 2 + i - k
            arr[j, k] = (4 ** (k - 1) * arr[j + 1, k - 1] - arr[j, k - 1]) / (4 ** (k - 1) - 1)

        # Hitung error aproksimasi (dalam persen)
        err_apr = abs((arr[1, i + 1] - arr[2, i]) / arr[1, i + 1]) * 100

        # Tampilkan hasil perhitungan
        print("%d\t%f\t%f" % (i, err_apr, arr[1, i + 1]))

        # Tambahkan 1 ke pangkat
        i += 1

    # Menampilkan bentuk fungsi yang ditetapkan di atas
    xlist = np.arange(-100, 100 + 1, 1)
    ylist = f(xlist)
    fig, ax = plt.subplots()
    ax.plot(xlist, ylist)
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.title("Function Plot")
    plt.savefig('plot.png')

    print("Program aproksimasi Romberg selesai.")

# Memanggil fungsi main() ketika pertama kali dijalankan.
if __name__ == "__main__":
    main()
