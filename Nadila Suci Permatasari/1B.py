def f(x):
    return e**x - x # fungsi dari soal 1b

def solve_equation_n_iterations(n):
    x = 0  # Nilai awal atau pertama x
    iterasi = 0  # Inisialisasi iterasi hitungan

    while iterasi < n: # perulangan
        x_new = x - f(x) / (3*x**2 - 2)  # Metode Newton-Raphson untuk mencari akar
        if abs(x_new - x) < 1e-6:  # Kondisi berhenti jika perbedaan sangat kecil
            break
        x = x_new
        iterasi += 1

    return x

n = 5  # Menggantikan dengan nilai n yang Anda mau
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}")