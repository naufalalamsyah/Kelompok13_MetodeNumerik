def f(x):
    return x**3 - 2*x + 1 #fungsi dari soal 1a

def solve_equation_n_iterations(n):
    x = 0  # nilai awal dari x
    iterasi = 0  # Inisialisasi dari iterasi hitungan

    while iterasi < n: # Metode perulangan untuk menghitung akar
        x_baru = x - f(x) / (3*x**2 - 2)  # Metode untuk mencari akar
        if abs(x_baru - x) < 1e-6:  # Sebuah kondisi, dimana program akan berhenti ketika perbedaannya sangat kecil
            break
        x = x_baru
        iterasi += 1

    return x

n = 5  # Menggantikan dengan nilai n yang diingikan user 
root = solve_equation_n_iterations(n)
print(f"Akar setelah {n} iterasi adalah: {root}") # Menampilkan hasil dari perhitungan