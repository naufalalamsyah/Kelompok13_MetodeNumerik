import numpy as np

def lagrange_interpolation(x, y, xi): #mendefinisikan fungsi
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (xi - x[j]) / (x[i] - x[j])
        result += term

    return result


x = [.0, 6.0, 7.0, 8.0] # Contoh data input
y = [1.0, 8.0, 27.0, 64.0]


xi = 2.5 # Nilai yang akan diinterpolasi


interpolated_value = lagrange_interpolation(x, y, xi)# Melakukan interpolasi

print(f"Hasil interpolasi pada x = {xi} adalah y = {interpolated_value}") #mencetak hasil interpolasi