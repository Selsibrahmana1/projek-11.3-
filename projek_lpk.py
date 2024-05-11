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
    st.set_page_config(page_title="Kalkulator Kerapatan dan Kepekatan Larutan Garam", page_icon=":test_tube:")

    st.sidebar.title('Menu')

    # Sidebar menu
    menu_options = ['Kalkulator Kerapatan dan Kepekatan', 'Tentang Kami']
    selected_menu = st.sidebar.radio('Navigasi', menu_options)

    if selected_menu == 'Kalkulator Kerapatan dan Kepekatan':
        calculate_density_section()
    elif selected_menu == 'Tentang Kami':
        about_us_section()

def calculate_density_section():
    st.header("Kalkulator Hubungan Kerapatan dan Kepekatan Larutan Garam🧪⚗", ":vial:", divider="violet")
    st.write("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata rata bobot labu takar untuk menghitung kerapatan larutan.
    Setelah itu, kalkulator akan menampilkan hasil perhitungan kerapatan untuk setiap konsentrasi dan regresi beserta 
    beserta persamaan regresi.
    """)

    # Initialize an empty DataFrame for data input
    data_input_table = pd.DataFrame({
        'Konsentrasi (g/mL)': [],
        'Bobot Labu Takar Isi (gram)': [],
        'Bobot Labu Takar Kosong (gram)': []
    })

    # Tampilkan data input dalam bentuk tabel
    st.table(data_input_table)

    # Tombol untuk menambah baris data
    if st.button('Tambah Baris Data'):
        new_row = {'Konsentrasi (g/mL)': 0.0, 'Bobot Labu Takar Isi (gram)': 0.0, 'Bobot Labu Takar Kosong (gram)': 0.0}
        data_input_table = data_input_table.append(new_row, ignore_index=True)
        st.table(data_input_table)

    # Tombol untuk menghitung hasil
    if st.button('Hitung'):
        # List untuk menyimpan nilai konsentrasi, volume, dan kerapatan
        x_data = []  # Konsentrasi
        y_data = []  # Kerapatan

        for index, row in data_input_table.iterrows():
            konsentrasi = row['Konsentrasi (g/mL)']
            bobot_filled = row['Bobot Labu Takar Isi (gram)']
            bobot_empty = row['Bobot Labu Takar Kosong (gram)']

            # Menghitung bobot sebenarnya
            weight = bobot_filled - bobot_empty

            # Menghitung kerapatan
            density = calculate_density(weight, volume=1.0)  # Menggunakan volume default 1.0 mL
            if density is not None:
                x_data.append(konsentrasi)
                y_data.append(density)

        # Tampilkan hasil perhitungan kerapatan untuk setiap konsentrasi
        st.header("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi", ":clipboard:", divider="violet")
        result_df = pd.DataFrame({'Konsentrasi (g/mL)': x_data, 'Kerapatan (g/mL)': y_data})
        st.table(result_df)

        # Hitung persamaan regresi
        slope, intercept, r = calculate_regression(x_data, y_data)

        # Tampilkan hasil persamaan regresi
        st.header("Persamaan Regresi", ":chart_with_upwards_trend:", divider="violet")
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
