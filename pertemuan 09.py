import streamlit as st

st.title("Kuliah Praktikum Big Data")
st.write("Indah")
st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")

pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

st.radio('Makanan kesukaan',['Bakso','Nasi goreng', 'Mie ayam'])

minuman = st.selectbox('Pilih minuman yang akan dipesan',
                       ['Es teh', 'Kopi', 'Jus'])
st.write(minuman)

bayar = st.multiselect('Bayar pakai:',
                       ['Tunai', 'Ovo', 'GoPay'])
st.write(bayar)