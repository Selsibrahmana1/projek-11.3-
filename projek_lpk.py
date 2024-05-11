import streamlit as st
import pandas as pd

def main():
    st.title('Kalkulator Kerapatan Larutan')

    num_data = st.number_input('Masukkan jumlah data:', min_value=1, step=1)
    data_input_table = pd.DataFrame(columns=['Konsentrasi (g/mL)', 'Bobot Labu Takar Isi (gram)', 'Bobot Labu Takar Kosong (gram)'])

    for i in range(num_data):
        st.subheader(f'Data {i+1}')
        konsentrasi = st.number_input('Masukkan konsentrasi (g/mL):', format="%.2f")  
        bobot_filled = st.number_input('Masukkan bobot labu takar isi (gram):', format="%.4f")
        bobot_empty = st.number_input('Masukkan bobot labu takar kosong (gram):', format="%.4f")

        data_input_table = data_input_table.append({'Konsentrasi (g/mL)': konsentrasi, 
                                                    'Bobot Labu Takar Isi (gram)': bobot_filled, 
                                                    'Bobot Labu Takar Kosong (gram)': bobot_empty}, 
                                                    ignore_index=True)

    st.write(data_input_table)

if __name__ == "__main__":
    main()
