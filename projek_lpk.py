import streamlit as st
import pandas as pd

def calculate_density(weight, volume):
    if volume != 0:
        return weight / volume
    else:
        return None

def main():
    st.sidebar.title('Menu')

    menu_options = ['Kalkulator Kerapatan dan Kepekatan', 'Tentang Kami']
    selected_menu = st.sidebar.radio('Navigasi', menu_options)

    if selected_menu == 'Kalkulator Kerapatan dan Kepekatan':
        calculate_density_section()
    elif selected_menu == 'Tentang Kami':
        about_us_section()

def calculate_density_section():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://th.bing.com/th/id/OIP.MrtvnBnC_7EDBKTshZg_RwAAAA?rs=1&pid=ImgDetMain");
            background-size: cover;
            color: #ffffff; /* Warna putih */
        }
        .stMarkdown h1 {
            color: #F5F5DC !important; /* Warna cream */
            padding-bottom: 10px; /* Spasi antara judul dan konten */
        }
        .stMarkdown {
            background-color: rgba(0, 0, 0, 0.5);
            padding: 1rem;
            border-radius: 0.5rem;
            font-family: 'Bookman Old Style', sans-serif;
        }
        .stButton>button {
            background-color: #007bff;
            color: #ffffff;
        }
        .stTextInput>div>div>input {
            background-color: #A8A9AD; /* Warna silver */
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Kalkulator Kerapatan dan Kepekatan Larutan Garam", anchor='center')
    st.write("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata-rata bobot LTI dan LTK untuk menghitung kerapatan larutan.
    """)

    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1, value=1)  
    
    volume = st.number_input('Masukkan volume larutan (mL):', min_value=0.01, step=0.01, value=0.01)

    df_input = pd.DataFrame(columns=['Konsentrasi (g/mL)', 'Bobot LTI (gram)', 'Bobot LTK (gram)'])

    st.subheader("Masukkan Data Konsentrasi dan Bobot LTI (Labu Takar Isi) dan LTK (Labu Takar Kosong):")
    for i in range(num_data):
        st.write(f"Data {i+1}:")
        konsentrasi = st.number_input(f'Konsentrasi (g/mL) {i+1}:', format="%.2f")  
        bobot_filled = st.number_input(f'Bobot LTI (gram) {i+1}:', format="%.4f")
        bobot_empty = st.number_input(f'Bobot LTK (gram) {i+1}:', format="%.4f")

        df_input.loc[i] = {'Konsentrasi (g/mL)': konsentrasi, 'Bobot LTI (gram)': bobot_filled, 'Bobot LTK (gram)': bobot_empty}

    st.subheader("Data Konsentrasi Sebelum Dihitung:")
    st.table(df_input)

    if st.button('Hitung'):
        calculate_results(df_input, volume)

def calculate_results(data_input, volume):
    st.header("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi")

    results_data = []
    for i, data in data_input.iterrows():
        weight = data['Bobot LTI (gram)'] - data['Bobot LTK (gram)']
        density = calculate_density(weight, volume)
        if density is not None:
            results_data.append([data['Konsentrasi (g/mL)'], density])

    st.write("Konsentrasi (g/mL) | Kerapatan (g/mL)")
    for result in results_data:
        st.write(f"{result[0]} | {result[1]}")

    # Kalkulasi regresi
    x_data = [data[0] for data in results_data]
    y_data = [data[1] for data in results_data]

    slope, intercept, r = calculate_regression(x_data, y_data)

    st.write(f'Persamaan Regresi: y = {slope:.4f}x + {intercept:.4f}')
    st.write(f'Nilai Regresi: {r:.4f}')
    st.write(f'Slope (b): {slope:.4f}')
    st.write(f'Intercept (a): {intercept:.4f}')

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
