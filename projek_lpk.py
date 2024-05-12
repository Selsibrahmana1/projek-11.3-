import streamlit as st
import pandas as pd

# Fungsi untuk menghitung kerapatan
def calculate_density(weight, volume):
    if volume != 0:
        return weight / volume
    else:
        return None

# Fungsi utama
def main():
    st.sidebar.title('Menu')

    # Sidebar menu
    menu_options = ['Kalkulator Kerapatan dan Kepekatan', 'Tentang Kami']
    selected_menu = st.sidebar.radio('Navigasi', menu_options)

    if selected_menu == 'Kalkulator Kerapatan dan Kepekatan':
        calculate_density_section()
    elif selected_menu == 'Tentang Kami':
        about_us_section()

# Bagian untuk menghitung kerapatan dan kepekatan larutan garam
def calculate_density_section():
    if 'data_input' not in st.session_state:
        st.session_state.data_input = pd.DataFrame(columns=['Konsentrasi (g/mL)', 'Bobot Labu Takar Isi (gram)', 'Bobot Labu Takar Kosong (gram)'])
    if 'results' not in st.session_state:
        st.session_state.results = {}

    st.header("Kalkulator Kerapatan dan Kepekatan Larutan Garam")
    st.write("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata-rata bobot labu takar untuk menghitung kerapatan larutan.
    """)

    # Input jumlah data konsentrasi
    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1, value=1)  # Ubah value menjadi 1
    
    # Input volume larutan
    volume = st.number_input('Masukkan volume larutan (mL):', min_value=0.01, step=0.01, value=0.01)

    # Input data konsentrasi, volume, dan bobot
    st.subheader("Masukkan Data Konsentrasi dan Bobot Labu Takar:")
    
    for i in range(num_data):
        st.write(f"**Data {i+1}:**")
        konsentrasi = st.number_input(f'Konsentrasi (g/mL) {i+1}:', format="%.2f")  
        bobot_filled = st.number_input(f'Bobot Labu Takar Isi (gram) {i+1}:', format="%.4f")
        bobot_empty = st.number_input(f'Bobot Labu Takar Kosong (gram) {i+1}:', format="%.4f")
        st.write("---")
        st.session_state.data_input.loc[i] = [konsentrasi, bobot_filled, bobot_empty]

    # Tombol untuk menghitung hasil
    if st.button('Hitung'):
        calculate_results()

# Fungsi untuk menghitung hasil
def calculate_results():
    data_input = st.session_state.data_input
    x_data = []  # Konsentrasi
    y_data = []  # Kerapatan

    for _, row in data_input.iterrows():
        weight = row['Bobot Labu Takar Isi (gram)'] - row['Bobot Labu Takar Kosong (gram)']
        density = calculate_density(weight, st.session_state.volume)
        if density is not None:
            x_data.append(row['Konsentrasi (g/mL)'])
            y_data.append(density)

    st.header("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi")
    for konsentrasi, density in zip(x_data, y_data):
        st.write(f'- Konsentrasi: {konsentrasi:.2f}, Kerapatan: {density:.4f} g/mL')

    slope, intercept, r = calculate_regression(x_data, y_data)

    st.header("Persamaan Regresi")
    st.write(f'- Persamaan Regresi: y = {slope:.4f}x + {intercept:.4f}')
    st.write(f'- Nilai Regresi: {r:.4f}')
    st.write(f'- Slope (b): {slope:.4f}')
    st.write(f'- Intercept (a): {intercept:.4f}')

# Fungsi untuk menghitung regresi
def calculate_regression(x, y):
    n = len(x)
    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(x_val * y_val for x_val, y_val in zip(x, y))
    x_squared_sum = sum(x_val ** 2 for x_val in x)
    y_squared_sum = sum(y_val ** 2 for y_val in y)

    r_numerator = n * xy_sum - x_sum * y_sum
    r_denominator = ((n * x_squared_sum - x_sum ** 2) * (n * y_squared_sum - y_sum ** 2)) ** 0.5
    if r_denominator != 0:
        r = r_numerator / r_denominator
    else:
        r = 0

    if (n * x_squared_sum - x_sum ** 2) != 0:  
        slope = r_numerator / (n * x_squared_sum - x_sum ** 2)
    else:
        slope = 0
    intercept = (y_sum - slope * x_sum) / n

    return slope, intercept, r

# Bagian "Tentang Kami"
def about_us_section():
    st.header("Tentang Kami")
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
