import streamlit as st

# Ini bagian heading aplikasi Streamlit
st.title("Kuliah Praktikum Big Data")
st.write("Indah")
st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")
st.write('#### Heading 4')
st.write('##### Heading 6')

# Kinerja Unit
st.metric("Kinerja", 40,-1)
st.metric("Response Time", 30, 20)

# Pilihan
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

"""
Ini komentar harusnya
"""

makanan = st.radio('Makanan kesukaan',['Bakso','Nasi goreng', 'Mie ayam'])

minuman = st.selectbox('Pilih minuman yang akan dipesan',
                       ['Es teh', 'Kopi', 'Jus'])
st.write(minuman)

bayar = st.multiselect('Bayar pakai:',
                       ['Tunai', 'Ovo', 'GoPay'])
st.write(bayar)
