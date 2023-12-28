import numpy as np
def solve_equation(f_str, a, b, tolerance):
    x = sp.symbols('x') # Konversi input fungsi menjadi bentuk simbolik
    f = sp.sympify(f_str) # Hitung turunan pertama fungsi
    f_prime = sp.diff(f, x)

    iteration = 0
    x_val = a

    while abs(f.subs(x, x_val)) > tolerance and iteration < 1000:
        x_val = x_val - f.subs(x, x_val) / f_prime.subs(x, x_val)
        iteration += 1

    if iteration < 1000:
        return x_val
    else:
        return None


# Input pengguna
f_str = input("Masukkan fungsi f(x): ")
a = float(input("Masukkan batas bawah akar: "))
b = float(input("Masukkan batas atas akar: "))
tolerance = float(input("Masukkan galat yang diinginkan: "))

result = solve_equation(f_str, a, b, tolerance)

if result is not None:
    print(f"Akar yang ditemukan adalah: {result:.6f}")
else:
    print("Metode tidak konvergen setelah 1000 iterasi.")