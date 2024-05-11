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

    return data_input_table  # Mengembalikan data_input_table untuk menangkap perubahan

def main():
    st.set_page_config(page_title="Kalkulator Kerapatan dan Kepekatan Larutan Garam", page_icon=":test_tube:")

    st.sidebar.title('Menu')

    # Sidebar menu
    menu_options = ['Kalkulator Kerapatan dan Kepekatan', 'Tentang Kami']
    selected_menu = st.sidebar.radio('Navigasi', menu_options)

    if selected_menu == 'Kalkulator Kerapatan dan Kepekatan':
        data_input_table = calculate_density_section()  # Menangkap kembali nilai data_input_table
    elif selected_menu == 'Tentang Kami':
        about_us_section()

if __name__ == "__main__":
    main()
