import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk metode bagi dua dengan kriteria iterasi ke-n
def metode_bagi_dua_iterasi(f, a, b, tol, max_iter):
    iterasi = 0
    while (b - a) / 2 > tol and iterasi < max_iter: # Menggunakan Perulangan
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterasi += 1
    return (a + b) / 2

# Fungsi untuk menampilkan grafik akar
def plot_akar(f, a, b, akar):
    x = np.linspace(a, b, 100)
    y = [f(xi) for xi in x]
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='red', linestyle='--', label='y=0')
    plt.scatter(akar, f(akar), color='green', marker='o', label='Akar')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafik Fungsi dan Akar')
    plt.legend()
    plt.grid()
    plt.show()

# Input oleh user
input_fungsi = input("Masukkan fungsi f(x): ") # Input fungsi 
a = float(input("Masukkan batas awal (a): ")) # Input batas awal
b = float(input("Masukkan batas akhir (b): ")) # Input batas akhir 
toleransi = float(input("Masukkan galat (toleransi): ")) # Input galat
max_iter = int(input("Masukkan iterasi maksimum: ")) # Input iterasi maksimum

# Evaluasi fungsi dengan ekspresi lambdify
import sympy as sp
x = sp.symbols('x')
try:
    f = sp.lambdify(x, sp.sympify(input_fungsi), 'numpy')
except (sp.SympifyError, TypeError):
    print("Fungsi tidak valid.")
else:
    akar = metode_bagi_dua_iterasi(f, a, b, toleransi, max_iter)

    # Pengecekan
    if akar is not None:
        print(f"Akar hampiran dari {input_fungsi} adalah: {akar}")
        plot_akar(f, a, b, akar)
    else:
        print(f"Akar tidak ditemukan di dalam rentang [{a}, {b}] atau pada iterasi ke-{max_iter}.")