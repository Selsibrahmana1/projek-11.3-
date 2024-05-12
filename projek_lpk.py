
import streamlit as st
import pandas as pd

# Fungsi untuk menghitung kerapatan
def calculate_density(weight, volume):
    """
    Fungsi ini menghitung kerapatan suatu zat berdasarkan berat dan volume.
    
    Parameters:
        weight (float): Berat zat dalam gram.
        volume (float): Volume zat dalam mililiter.
    
    Returns:
        float: Nilai kerapatan zat dalam gram per mililiter.
    """
    if volume != 0:
        return weight / volume
    else:
        return None

def calculate_regression(x, y):
    """
    Fungsi ini menghitung persamaan regresi linear berdasarkan dua set data.
    
    Parameters:
        x (list of float): Data untuk sumbu x.
        y (list of float): Data untuk sumbu y.
    
    Returns:
        tuple: Tuple berisi nilai slope (m), intercept (c), dan koefisien korelasi (r) dari persamaan regresi.
    """
    n = len(x)
    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(x_val * y_val for x_val, y_val in zip(x, y))
    x_squared_sum = sum(x_val ** 2 for x_val in x)
    
    m = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum ** 2)
    c = (y_sum - m * x_sum) / n
    r = (n * xy_sum - x_sum * y_sum) / ((n * x_squared_sum - x_sum ** 2) * (n * sum(y_val ** 2 for y_val in y) - y_sum ** 2)) ** 0.5
    
    return m, c, r

# Contoh penggunaan fungsi
weight = [10, 15, 20, 25, 30]
volume = [5, 7, 10, 12, 15]
density = [calculate_density(w, v) for w, v in zip(weight, volume)]
m, c, r = calculate_regression(weight, volume)

# Tampilkan tabel dengan data
data = {'Berat (g)': weight, 'Volume (mL)': volume, 'Kerapatan (g/mL)': density}
df = pd.DataFrame(data)

st.title("Tabel Contoh")
st.dataframe(df)


Penjelasan:

1. Setelah mendefinisikan fungsi calculate_density() dan calculate_regression(), kita membuat contoh data untuk berat, volume, dan kerapatan.
2. Kemudian, kita membuat dataframe Pandas dengan data tersebut.
3. Terakhir, kita menampilkan tabel menggunakan st.dataframe(df).

