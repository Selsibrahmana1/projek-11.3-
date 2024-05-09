import streamlit as st
import pandas as pd
import numpy as np

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

# Fungsi untuk menghitung persamaan regresi linear
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
    y_squared_sum = sum(y_val ** 2 for y_val in y)

    # Hitung koefisien korelasi (r)
    r_numerator = n * xy_sum - x_sum * y_sum
    r_denominator = ((n * x_squared_sum - x_sum ** 2) * (n * y_squared_sum - y_sum ** 2)) ** 0.5
    if r_denominator != 0:
        r = r_numerator / r_denominator
    else:
        r = 0

    # Hitung slope (m) dan intercept (c) dari persamaan regresi
    if (n * x_squared_sum - x_sum ** 2) != 0:  # Cek untuk pembagian dengan nol
        slope = r_numerator / (n * x_squared_sum - x_sum ** 2)
    else:
        slope = 0
    intercept = (y_sum - slope * x_sum) / n

    return slope, intercept, r

def main():
    st.sidebar.title('Menu')

    # Sidebar menu
    menu_options = ['Kalkulator Kerapatan dan Kepekatan', 'Tentang Kami']
    selected_menu = st.sidebar.radio('Navigasi', menu_options)

    if selected_menu == 'Kalkulator Kerapatan dan Kepekatan':
        calculate_density_section()
    elif selected_menu == 'Tentang Kami':
        about_us_section()

def calculate_density_section():
    st.header("Kalkulator Hubungan Kerapatan dan Kepekatan Larutan Garam🧪⚗", divider="violet")
    st.write("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata rata bobot labu takar untuk menghitung kerapatan larutan.
    Setelah itu, kalkulator akan menampilkan hasil perhitungan kerapatan untuk setiap konsentrasi dan regresi beserta 
    beserta persamaan regresi.
    """)

    # Input jumlah data konsentrasi
    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1)

    # Input volume larutan
    volume = st.number_input('Masukkan volume larutan (mL):', min_value=0.01, step=0.01)

    # Inisialisasi DataFrame kosong untuk menyimpan data
    df = pd.DataFrame(columns=['Konsentrasi (g/mL)', 'Bobot Labu Takar Isi (gram)', 'Bobot Labu Takar Kosong (gram)'])

    # Membuat tabel untuk memasukkan data
    st.subheader('Masukkan Data:')
    for i in range(num_data):
        st.write(f"**Data ke-{i+1}**")
        with st.form(f"form_data_{i}"):
            konsentrasi = st.text_input(f'Konsentrasi data {i+1} (g/mL):', key=f'conc_{i}')
            bobot_filled = st.text_input(f'Bobot Labu Takar Isi (gram) {i+1}:', key=f'filled_{i}')
            bobot_empty = st.text_input(f'Bobot Labu Takar Kosong (gram) {i+1}:', key=f'empty_{i}')
            st.form_submit_button(label='Simpan')
        df = df.append({'Konsentrasi (g/mL)': konsentrasi,
                        'Bobot Labu Takar Isi (gram)': bobot_filled,
                        'Bobot Labu Takar Kosong (gram)': bobot_empty}, ignore_index=True)

    # Tampilkan data input dalam bentuk tabel
    st.subheader('Data yang Dimasukkan:')
    st.table(df)

    # Tombol untuk menghitung hasil
    if st.button('Hitung'):
        # List untuk menyimpan nilai konsentrasi, volume, dan kerapatan
        x_data = []
        y_data = []

        for index, row in df.iterrows():
            # Menghitung bobot sebenarnya
            weight = float(row['Bobot Labu Takar Isi (gram)']) - float(row['Bobot Labu Takar Kosong (gram)'])
            # Menghitung kerapatan
            density = calculate_density(weight, volume)
            if density is not None:
                x_data.append(float(row['Konsentrasi (g/mL)']))
                y_data.append(density)

        # Tampilkan hasil perhitungan kerapatan untuk setiap konsentrasi
        st.header("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi", divider="violet")
        for konsentrasi, density in zip(x_data, y_data):
            st.write(f'Konsentrasi: {konsentrasi}, Kerapatan: {density:.4f} g/mL')

        # Hitung persamaan regresi
        slope, intercept, r = calculate_regression(x_data, y_data)

        # Tampilkan hasil persamaan regresi
        st.header("Persamaan Regresi", divider="violet")
        st.write(f'Persamaan Regresi: y = {slope:.4f}x + {intercept:.4f}')
        st.write(f'Nilai Regresi: {r:.4f}')

        # Tampilkan plot
        st.header("Grafik Kurva", divider="violet")
        st.line_chart
