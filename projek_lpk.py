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

def main():
    st.set_page_config(page_title="Kalkulator Kerapatan dan Kepekatan Larutan Garam", page_icon=":test_tube:")

    st.header("Kalkulator Hubungan Kerapatan dan Kepekatan Larutan Garam🧪⚗", ":vial:", divider="violet")
    st.write("""
    Ini adalah kalkulator sederhana untuk menghitung kerapatan dan kepekatan garam dalam larutan. 
    Anda dapat memasukkan data konsentrasi, volume, dan rata-rata bobot labu takar untuk menghitung kerapatan larutan.
    Setelah itu, kalkulator akan menampilkan hasil perhitungan kerapatan untuk setiap konsentrasi.
    """)

    # Initialize an empty DataFrame for data input
    data_input_table = pd.DataFrame({
        'Konsentrasi (g/mL)': [],
        'Bobot Labu Takar Isi (gram)': [],
        'Bobot Labu Takar Kosong (gram)': []
    })

    # Tampilkan data input dalam bentuk tabel
    st.write(data_input_table)

    # Tombol untuk menambah baris data
    if st.button('Tambah Baris Data'):
        new_row = {'Konsentrasi (g/mL)': st.number_input('Konsentrasi (g/mL)', value=0.0, step=0.001),
                   'Bobot Labu Takar Isi (gram)': st.number_input('Bobot Labu Takar Isi (gram)', value=0.0, step=0.001),
                   'Bobot Labu Takar Kosong (gram)': st.number_input('Bobot Labu Takar Kosong (gram)', value=0.0, step=0.001)}
        data_input_table = pd.concat([data_input_table, pd.DataFrame([new_row])], ignore_index=True)
        st.write(data_input_table)

    # Tombol untuk menghitung hasil
    if st.button('Hitung') and not data_input_table.empty:
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
        st.write(result_df)

if __name__ == "__main__":
    main()
