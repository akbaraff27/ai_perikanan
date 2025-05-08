import base64
import streamlit as st

# Fungsi untuk mendapatkan base64 dari file biner
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as file:
        binary_data = file.read()
        base64_data = base64.b64encode(binary_data).decode('utf-8')
    return base64_data

# Fungsi untuk menampilkan gambar dengan penyesuaian jumlah card
def image(file_paths):
    # Memulai kode CSS untuk styling gambar
    style_block = f"""
        <style>
        .LogoContainer {{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            padding: 10px;
            background: #fff;
            margin: -3rem -4rem 0 -4rem;
        }}
        .Logo {{
            height: 100px; /* Tinggi tetap 100px */
            width: auto;  /* Lebar menyesuaikan proporsi */
            margin-right: 15px;
        }}
        @media (max-width: 768px) {{
            .Logo {{
                height: 80px; /* Tinggi lebih kecil untuk layar kecil */
            }}
        }}
        </style>
        <div class="LogoContainer">"""

    # Looping untuk menambahkan setiap gambar sebagai card
    for file_path in file_paths:
        image_base64 = get_base64_of_bin_file(file_path)
        style_block += f"""<div class="card">
                <img src="data:image/png;base64,{image_base64}" class="Logo">
            </div>
        """

    # Menutup div LogoContainer
    style_block += "</div>"

    # Render dengan markdown dan memperbolehkan HTML tidak aman
    st.markdown(style_block, unsafe_allow_html=True)

# Contoh pemanggilan fungsi dengan daftar file paths
# file_paths = ["path/to/image1.png", "path/to/image2.png"]
# image(file_paths)