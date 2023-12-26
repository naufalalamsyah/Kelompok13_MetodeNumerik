import numpy as np

def turunan_maju(fungsi, x, h):
    turunan = (fungsi(x + h) - fungsi(x)) / h
    return turunan

def turunan_mundur(fungsi, x, h):
    turunan = (fungsi(x) - fungsi(x - h)) / h
    return turunan

def turunan_tengah(fungsi, x, h):
    turunan = (fungsi(x + h) - fungsi(x - h)) / (2 * h)
    return turunan

fungsi_input = input("Masukkan fungsi: ")
fungsi = lambda x: eval(fungsi_input)

x_array_input = input("Masukkan nilai x: ")
x_array = np.array([float(x) for x in x_array_input.split(',')])

h_input = float(input("Masukkan jarah dari nilai x: "))

turunan_maju_array = np.vectorize(lambda x: turunan_maju(fungsi, x, h_input))(x_array[1:])  
turunan_mundur_array = np.vectorize(lambda x: turunan_mundur(fungsi, x, h_input))(x_array[:-1]) 
turunan_tengah_array = np.vectorize(lambda x: turunan_tengah(fungsi, x, h_input))(x_array[1:-1]) 

print(f"\nFungsi: {fungsi_input}")
print(f"Nilai x: {x_array}")
print(f"Nilai h: {h_input}")
print("\nTurunan Pertama (Maju):", turunan_maju_array)
print("Turunan Pertama (Mundur):", turunan_mundur_array)
print("Turunan Pertama (Tengah):", turunan_tengah_array)