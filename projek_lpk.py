import streamlit as st
import pandas as pd

def calculate_density(weight, volume):
    if volume != 0:
        return weight / volume
    else:
        return None

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

def main():
    st.sidebar.title('Menu')

    menu_options = ['Kalkulator Kerapatan dan Kepekatan', 'Tentang Kami']
    selected_menu = st.sidebar.radio('Navigasi', menu_options)

    if selected_menu == 'Kalkulator Kerapatan dan Kepekatan':
        calculate_density_section()
    elif selected_menu == 'Tentang Kami':
        about_us_section()

def calculate_density_section():
    if 'data_input' not in st.session_state:
        st.session_state.data_input = {
            'num_data': 1,
            'volume': 0.01,
            'data': pd.DataFrame(columns=['Konsentrasi (g/mL)', 'Bobot Labu Takar Isi (gram)', 'Bobot Labu Takar Kosong (gram)'])
        }
    if 'results' not in st.session_state:
        st.session_state.results = {}

    st.markdown(
        "<h1 style='text-align: center; color: white; background-color: #7544F3; padding: 0.5rem; border-radius: 0.5rem;'>"
        "Kalkulator Hubungan Kerapatan dan Kepekatan Larutan Garam🧪⚗</h1>",
        unsafe_allow_html=True
    )
    st.markdown("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata-rata bobot labu takar untuk menghitung kerapatan larutan.
    Setelah itu, kalkulator akan menampilkan hasil perhitungan kerapatan untuk setiap konsentrasi dan regresi beserta 
    persamaan regresi.
    """)

    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1, value=st.session_state.data_input['num_data'])
    st.session_state.data_input['num_data'] = num_data

    volume = st.number_input('Masukkan volume larutan (mL):', min_value=0.01, step=0.01, value=st.session_state.data_input['volume'])
    st.session_state.data_input['volume'] = volume

    data_input_table = st.session_state.data_input['data']
    for i in range(num_data):
        konsentrasi = st.number_input(f'Konsentrasi Data {i+1} (g/mL):', format="%.2f")  
        bobot_filled = st.number_input(f'Rerata Bobot Labu Takar Isi (gram) {i+1}:', format="%.4f")
        bobot_empty = st.number_input(f'Rerata Bobot Labu Takar Kosong (gram) {i+1}:', format="%.4f")
        data_input_table.loc[i] = [konsentrasi, bobot_filled, bobot_empty]
    
    st.write(data_input_table)

    if st.button('Hitung'):
        x_data = data_input_table['Konsentrasi (g/mL)']
        y_data = []  

        for bobot_filled, bobot_empty in zip(data_input_table['Bobot Labu Takar Isi (gram)'], data_input_table['Bobot Labu Takar Kosong (gram)']):
            weight = bobot_filled - bobot_empty

            density = calculate_density(weight, volume)
            if density is not None:
                y_data.append(density)

        st.markdown("<h2 style='color: #7544F3;'>Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi</h2>", unsafe_allow_html=True)
        for konsentrasi, density in zip(x_data, y_data):
            st.write(f'Konsentrasi: {konsentrasi:.2f}, Kerapatan: {density:.4f} g/mL')

        slope, intercept, r = calculate_regression(x_data, y_data)

        st.markdown("<h2 style='color: #7544F3;'>Persamaan Regresi</h2>", unsafe_allow_html=True)
        st.write(f'Persamaan Regresi: y = {slope:.4f}x + {intercept:.4f}')
        st.write(f'Nilai Regresi: {r:.4f}')
        st.write(f'Slope (b): {slope:.4f}')
        st.write(f'Intercept (a): {intercept:.4f}')

        st.session_state.results = {
            'x_data': x_data,
            'y_data': y_data,
            'slope': slope,
            'intercept': intercept,
            'r': r
        }

def about_us_section():
    st.markdown(
        "<h1 style='text-align: center; color: white; background-color: #7544F3; padding: 0.5rem; border-radius: 0.5rem;'>"
        "Tentang Kami</h1>",
        unsafe_allow_html=True
    )
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
import streamlit as st
import pandas as pd

def calculate_density(weight, volume):
    if volume != 0:
        return weight / volume
    else:
        return None

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

def main():
    st.sidebar.title('Menu')

    menu_options = ['Kalkulator Kerapatan dan Kepekatan', 'Tentang Kami']
    selected_menu = st.sidebar.radio('Navigasi', menu_options)

    if selected_menu == 'Kalkulator Kerapatan dan Kepekatan':
        calculate_density_section()
    elif selected_menu == 'Tentang Kami':
        about_us_section()

def calculate_density_section():
    if 'data_input' not in st.session_state:
        st.session_state.data_input = {
            'num_data': 1,
            'volume': 0.01,
            'data': pd.DataFrame(columns=['Konsentrasi (g/mL)', 'Bobot Labu Takar Isi (gram)', 'Bobot Labu Takar Kosong (gram)'])
        }
    if 'results' not in st.session_state:
        st.session_state.results = {}

    st.markdown(
        "<h1 style='text-align: center; color: white; background-color: #7544F3; padding: 0.5rem; border-radius: 0.5rem;'>"
        "Kalkulator Hubungan Kerapatan dan Kepekatan Larutan Garam🧪⚗</h1>",
        unsafe_allow_html=True
    )
    st.markdown("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata-rata bobot labu takar untuk menghitung kerapatan larutan.
    Setelah itu, kalkulator akan menampilkan hasil perhitungan kerapatan untuk setiap konsentrasi dan regresi beserta 
    persamaan regresi.
    """)

    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1, value=st.session_state.data_input['num_data'])
    st.session_state.data_input['num_data'] = num_data

    volume = st.number_input('Masukkan volume larutan (mL):', min_value=0.01, step=0.01, value=st.session_state.data_input['volume'])
    st.session_state.data_input['volume'] = volume

    data_input_table = st.session_state.data_input['data']
    for i in range(num_data):
        konsentrasi = st.number_input(f'Konsentrasi Data {i+1} (g/mL):', format="%.2f")  
        bobot_filled = st.number_input(f'Rerata Bobot Labu Takar Isi (gram) {i+1}:', format="%.4f")
        bobot_empty = st.number_input(f'Rerata Bobot Labu Takar Kosong (gram) {i+1}:', format="%.4f")
        data_input_table.loc[i] = [konsentrasi, bobot_filled, bobot_empty]
    
    st.write(data_input_table)

    if st.button('Hitung'):
        x_data = data_input_table['Konsentrasi (g/mL)']
        y_data = []  

        for bobot_filled, bobot_empty in zip(data_input_table['Bobot Labu Takar Isi (gram)'], data_input_table['Bobot Labu Takar Kosong (gram)']):
            weight = bobot_filled - bobot_empty

            density = calculate_density(weight, volume)
            if density is not None:
                y_data.append(density)

        st.markdown("<h2 style='color: #7544F3;'>Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi</h2>", unsafe_allow_html=True)
        for konsentrasi, density in zip(x_data, y_data):
            st.write(f'Konsentrasi: {konsentrasi:.2f}, Kerapatan: {density:.4f} g/mL')

        slope, intercept, r = calculate_regression(x_data, y_data)

        st.markdown("<h2 style='color: #7544F3;'>Persamaan Regresi</h2>", unsafe_allow_html=True)
        st.write(f'Persamaan Regresi: y = {slope:.4f}x + {intercept:.4f}')
        st.write(f'Nilai Regresi: {r:.4f}')
        st.write(f'Slope (b): {slope:.4f}')
        st.write(f'Intercept (a): {intercept:.4f}')

        st.session_state.results = {
            'x_data': x_data,
            'y_data': y_data,
            'slope': slope,
            'intercept': intercept,
            'r': r
        }

def about_us_section():
    st.markdown(
        "<h1 style='text-align: center; color: white; background-color: #7544F3; padding: 0.5rem; border-radius: 0.5rem;'>"
        "Tentang Kami</h1>",
        unsafe_allow_html=True
    )
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
