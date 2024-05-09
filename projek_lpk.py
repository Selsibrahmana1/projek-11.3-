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

    # Tombol untuk menambahkan baris ke DataFrame
    if st.button('Tambah Baris'):
        for i in range(num_data):
            konsentrasi = st.number_input(f'Masukkan nilai konsentrasi data {i+1}:', format="%.2f")  
            bobot_filled = st.number_input(f'Masukkan nilai rerata bobot labu takar isi (gram) {i+1}:', format="%.4f")
            bobot_empty = st.number_input(f'Masukkan nilai rerata bobot labu takar kosong (gram) {i+1}:', format="%.4f")
            df = df.append({'Konsentrasi (g/mL)': konsentrasi,
                            'Bobot Labu Takar Isi (gram)': bobot_filled,
                            'Bobot Labu Takar Kosong (gram)': bobot_empty}, ignore_index=True)

    # Tampilkan data input dalam bentuk tabel
    st.table(df)

    # Tombol untuk menghitung hasil
    if st.button('Hitung'):
        # List untuk menyimpan nilai konsentrasi, volume, dan kerapatan
        x_data = df['Konsentrasi (g/mL)'].tolist()
        y_data = []

        for index, row in df.iterrows():
            # Menghitung bobot sebenarnya
            weight = row['Bobot Labu Takar Isi (gram)'] - row['Bobot Labu Takar Kosong (gram)']
            # Menghitung kerapatan
            density = calculate_density(weight, volume)
            if density is not None:
                y_data.append(density)

        # Tampilkan hasil perhitungan kerapatan untuk setiap konsentrasi
        st.header("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi", divider="violet")
        for konsentrasi, density in zip(x_data, y_data):
            st.write(f'Konsentrasi: {konsentrasi:.2f}, Kerapatan: {density:.4f} g/mL')

        # Hitung persamaan regresi
        slope, intercept, r = calculate_regression(x_data, y_data)

        # Tampilkan hasil persamaan regresi
        st.header("Persamaan Regresi", divider="violet")
        st.write(f'Persamaan Regresi: y = {slope:.4f}x + {intercept:.4f}')
        st.write(f'Nilai Regresi: {r:.4f}')
        st.write(f'Slope (b): {slope:.4f}')
        st.write(f'Intercept (a): {intercept:.4f}')

        # Simpan hasil perhitungan ke variabel session_state
        st.session_state.results = {
            'x_data': x_data,
            'y_data': y_data,
            'slope': slope,
            'intercept': intercept,
            'r': r
        }

def about_us_section():
    st.header("Kalkulator Hubungan Kerapatan dan Kepekatan Larutan Garam 🧪⚗", divider="rainbow")
    st.write("""
    Ini adalah kalkulator sederhana yang dikembangkan oleh Tim LPK. Terinspirasi dari praktik analisis fisika pangan mengenai praktikum 
    dengan judul hubungan kerapatan dan kepekatan larutan garam. Dengan ini diharapkan dapat memudahkan untuk menghitung kerapatan 
    dan kepekatan garam dalam larutan secara cepat dan tepat. Web Aplikasi disusun oleh :
    1. Dinda Ariyantika              (2302520)
    2. Ibnu Mustofa Giam             (2320529)
    3. Putri Nabila Aji Kusuma       (2320546)
    4. Salima Keisha Arthidia        (2320552)
    5. Selsi Mei Doanna br Brahmana  (2320554)
    """)

if __name__ == "__main__":
    main()
[theme]
base="light"
primaryColor="#fb8e54"
backgroundColor="#f3e9df"
secondaryBackgroundColor="#c99548"
