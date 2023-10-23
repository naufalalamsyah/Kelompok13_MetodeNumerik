def f(x):
    return e**x - x # fungsi dari soal 1b

def solve_equation_n_iterations(n):
    x = 0  # Nilai awal dari x
    iterasi = 0  # Inisialisasi dari iterasi hitungan

    while iterasi < n: # Metode Perulangan untuk menghitung akar
        x_new = x - f(x) / (3*x**2 - 2)  # Metode untuk mencari akar dengan mengggunakan Newton-Raphson
        if abs(x_new - x) < 1e-6:  # Sebuah kondisi, dimana program akan berhenti ketika perbedaannya sangat kecil
            break
        x = x_new
        iterasi += 1

    return x

n = 5  # Menggantikan dengan nilai n yang diingikan user
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}")