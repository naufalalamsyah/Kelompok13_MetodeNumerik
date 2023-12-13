def f(x):
    return x**3 - 2*x + 1 #fungsi dari soal nomor 1a

def solve_equation_n_iterations(n):
    x = 0  # Nilai awal atau pertama dari x
    iterasi = 0  # Inisialisasi iterasi hitungan

    while iterasi < n: # perulangan
        x_baru = x - f(x) / (3*x**2 - 2)  # Metode untuk mencari akar
        if abs(x_baru - x) < 1e-6:  # Kondisi dimana program akan berhenti jika perbedaan sangat kecil
            break
        x = x_baru
        iterasi += 1

    return x

n = 5  # Menggantikan dengan nilai n yang Anda mau
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}")