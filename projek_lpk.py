import streamlit as st
import pandas as pd

# Fungsi untuk menghitung kerapatan
def calculate_density(weight, volume):
    if volume != 0:
        return weight / volume
    else:
        return None

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
    st.header("Kalkulator Kerapatan dan Kepekatan Larutan Garam")
    st.write("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata-rata bobot LTI dan LTK untuk menghitung kerapatan larutan.
    """)

    # Input jumlah data konsentrasi
    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1, value=1)  # Ubah value menjadi 1
    
    # Input volume larutan
    volume = st.number_input('Masukkan volume larutan (mL):', min_value=0.01, step=0.01, value=0.01)

    # Input data konsentrasi, volume, dan bobot
    st.subheader("Masukkan Data Konsentrasi dan Bobot LTI dan LTK:")
    
    data_input = []
    for i in range(num_data):
        st.write(f"*Data {i+1}:*")
        konsentrasi = st.number_input(f'Konsentrasi (g/mL) {i+1}:', format="%.2f")  
        bobot_filled = st.number_input(f'Bobot LTI (gram) {i+1}:', format="%.4f")
        bobot_empty = st.number_input(f'Bobot LTK (gram) {i+1}:', format="%.4f")
        data_input.append([konsentrasi, bobot_filled, bobot_empty])

    # Tombol untuk menghitung hasil
    if st.button('Hitung'):
        calculate_results(data_input, volume)

# Fungsi untuk menghitung hasil
def calculate_results(data_input, volume):
    st.header("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi")

    results_data = []
    for i, data in enumerate(data_input):
        weight = data[1] - data[2]
        density = calculate_density(weight, volume)
        if density is not None:
            results_data.append([data[0], density])

    # Tampilkan tabel hasil
    df_results = pd.DataFrame(results_data, columns=['Konsentrasi (g/mL)', 'Kerapatan (g/mL)'])
    st.dataframe(df_results)

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
