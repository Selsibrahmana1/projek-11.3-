from turtle import st


def calculate_density_section():
    if 'data_input' not in st.session_state:
        st.session_state.data_input = {
            'num_data': 1,
            'volume': 0.01,
            'data': [[0, 0, 0]]  # Konsentrasi, Bobot Labu Takar Isi, Bobot Labu Takar Kosong
        }
    if 'results' not in st.session_state:
        st.session_state.results = {}

    st.header("Kalkulator Hubungan Kerapatan dan Kepekatan Larutan Garam🧪⚗", divider="violet")
    st.write("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata-rata bobot labu takar untuk menghitung kerapatan larutan.
    Setelah itu, kalkulator akan menampilkan hasil perhitungan kerapatan untuk setiap konsentrasi dan regresi beserta 
    persamaan regresi.
    """)

    # Input jumlah data konsentrasi
    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1, value=st.session_state.data_input['num_data'])
    st.session_state.data_input['num_data'] = num_data

    # Input volume larutan
    volume = st.number_input('Masukkan volume larutan (mL):', min_value=0.01, step=0.01, value=st.session_state.data_input['volume'])
    st.session_state.data_input['volume'] = volume

    # Input data konsentrasi, bobot labu takar isi, dan bobot labu takar kosong
    st.write("Masukkan data konsentrasi, bobot labu takar isi, dan bobot labu takar kosong:")
    data_input = []
    for i in range(num_data):
        if i >= len(st.session_state.data_input['data']):
            st.session_state.data_input['data'].append([0, 0, 0])

        konsentrasi = st.number_input(f'Konsentrasi data {i+1} (mol/L):', format="%.2f", value=st.session_state.data_input['data'][i][0])
        bobot_filled = st.number_input(f'Rerata bobot labu takar isi {i+1} (g):', format="%.4f", value=st.session_state.data_input['data'][i][1])
        bobot_empty = st.number_input(f'Rerata bobot labu takar kosong {i+1} (g):', format="%.4f", value=st.session_state.data_input['data'][i][2])
        
        st.session_state.data_input['data'][i] = [konsentrasi, bobot_filled, bobot_empty]
        data_input.append([konsentrasi, bobot_filled, bobot_empty])

    # Tampilkan tabel input
    st.write("Tabel Input:")
    st.table(data_input)

    # Tombol untuk menghitung hasil
    if st.button('Hitung'):
        # List untuk menyimpan nilai konsentrasi, volume, dan kerapatan
        x_data = []  # Konsentrasi
        y_data = []  # Kerapatan

        # Tampilkan hasil perhitungan kerapatan untuk setiap konsentrasi
        st.header("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi", divider="violet")
        for konsentrasi, bobot_filled, bobot_empty in st.session_state.data_input['data']:
            weight = bobot_filled - bobot_empty
            density = calculate_density(weight, volume) # type: ignore
            if density is not None:
                x_data.append(konsentrasi)
                y_data.append(density)
                st.write(f'Konsentrasi: {konsentrasi:.2f}, Kerapatan: {density:.4f} g/mL')

        # Hitung persamaan regresi
        slope, intercept, r = calculate_regression(x_data, y_data) # type: ignore

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
