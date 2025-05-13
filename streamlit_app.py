import streamlit as st

# --- CSS Kustom ---
st.markdown(
    """
    <style>
    .streamlit-container {
        max-width: 1000px;
        padding-top: 20px;
    }
    h1, h2, h3 {
        color: #336699;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput > div > div > input {
        border: 2px solid #ddd;
        border-radius: 5px;
        padding: 10px;
    }
    .info-box {
        background-color: #f0f8ff;
        border: 1px solid #e0e0e0;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .warning-box {
        background-color: #ffe0b2;
        border: 1px solid #ffc107;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Data Kode Plastik ---
ric_info = {
    "1": {
        "material": "Polyethylene Terephthalate (PET)",
        "example": "Botol air mineral, botol soda, kemasan minyak goreng.",
        "health_risk": "Aman untuk sekali pakai, tidak dianjurkan digunakan ulang terutama untuk air panas.",
        "environment_risk": "PET banyak ditemukan di perairan dan mudah terbawa angin. Tidak terurai secara alami, mengancam hewan laut, serta bisa menjadi mikroplastik.",
        "recycling_difficulty": "Mudah",
        "recycling_method": "Cuci, cacah, lelehkan. Hasil daur ulang: serat sintetis (polyester), karpet, tali plastik, wadah non-makanan."
    },
    "2": {
        "material": "High-Density Polyethylene (HDPE)",
        "example": "Botol susu, galon, wadah deterjen, sampo.",
        "health_risk": "Umumnya aman, tetapi bisa berbahaya jika dibakar karena menghasilkan gas beracun.",
        "environment_risk": "Tidak mudah terurai, jika dibakar menghasilkan racun. Jika tidak didaur ulang dengan baik dapat mencemari tanah dan air.",
        "recycling_difficulty": "Mudah",
        "recycling_method": "Dicuci, dilelehkan. Produk baru: pipa, ember, tempat sampah, mainan, furnitur taman."
    },
    "3": {
        "material": "Polyvinyl Chloride (PVC)",
        "example": "Pipa, lantai vinyl, mainan, botol minyak.",
        "health_risk": "Berisiko tinggi jika dibakar karena menghasilkan dioksin yang karsinogenik.",
        "environment_risk": "Sulit didaur ulang, mengandung klorin. Jika dibakar menghasilkan racun berbahaya.",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Daur ulang terbatas, menjadi panel, selang, atau bahan bangunan lain."
    },
    "4": {
        "material": "Low-Density Polyethylene (LDPE)",
        "example": "Kantong plastik, pembungkus makanan.",
        "health_risk": "Cenderung aman, tapi sering tidak didaur ulang.",
        "environment_risk": "Sangat umum sebagai limbah plastik yang berterbangan atau menyumbat saluran air. Tidak mudah terurai.",
        "recycling_difficulty": "Sedang",
        "recycling_method": "Dilelehkan, dijadikan kantong sampah, ubin plastik, dan film daur ulang."
    },
    "5": {
        "material": "Polypropylene (PP)",
        "example": "Wadah makanan, tutup botol, sedotan.",
        "health_risk": "Aman untuk makanan, namun perlu pengawasan pada produk daur ulang.",
        "environment_risk": "Tidak terurai alami, namun lebih stabil dan tahan panas. Bisa jadi limbah jika tidak didaur ulang.",
        "recycling_difficulty": "Sedang",
        "recycling_method": "Dicacah, dilelehkan menjadi kontainer non-makanan, komponen otomotif, ember."
    },
    "6": {
        "material": "Polystyrene (PS)",
        "example": "Styrofoam, gelas kopi, wadah makanan cepat saji.",
        "health_risk": "Mengandung stirena yang diduga karsinogenik. Tidak disarankan untuk makanan panas.",
        "environment_risk": "Sangat ringan dan mudah mencemari perairan. Tidak bisa terurai, menjadi mikroplastik berbahaya.",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Jarang didaur ulang. Bisa diproses menjadi bahan isolasi atau material bangunan."
    },
    "7": {
        "material": "Other (PC, PLA, dll.)",
        "example": "Botol bayi, galon keras, PLA (bio-based).",
        "health_risk": "Tergantung jenis. PC bisa mengandung BPA yang berisiko hormonal.",
        "environment_risk": "Campuran bahan membuat daur ulang sulit. PLA bisa dikomposkan, tapi butuh fasilitas industri.",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Bervariasi: PC melalui proses kimia, PLA bisa dikomposkan di fasilitas industri."
    }
}

# --- Navigasi Sidebar ---
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Home", "Identifikasi", "Tentang Plastik", "Riwayat"])

# --- Halaman Home ---
if page == "Home":
    st.title("Selamat Datang di Aplikasi Kode Plastik!")
    st.markdown("""
    Aplikasi ini memberikan informasi tentang kode daur ulang plastik (Resin Identification Code - RIC).
    Dengan memahami kode ini, kita dapat mengelola sampah plastik dengan lebih bijak dan mendukung daur ulang.
    """)

# --- Halaman Identifikasi ---
elif page == "Identifikasi":
    st.title("Identifikasi Kode Plastik")
    st.write("Masukkan nomor kode plastik (1-7) yang tertera di bawah wadah.")

    plastic_code_input = st.text_input("Nomor Kode Plastik:")
    if st.button("Cari Informasi"):
        if plastic_code_input in ric_info:
            st.subheader(f"Informasi Kode Plastik: {plastic_code_input}")
            info = ric_info[plastic_code_input]
            st.markdown(
                f"<div class='info-box'>"
                f"<strong>Material:</strong> {info['material']}<br>"
                f"<strong>Contoh Penggunaan:</strong> {info['example']}<br>"
                f"<strong>Risiko Kesehatan:</strong> {info['health_risk']}<br>"
                f"<strong>Risiko Lingkungan:</strong> {info['environment_risk']}<br>"
                f"<strong>Tingkat Daur Ulang:</strong> {info['recycling_difficulty']}<br>"
                f"<strong>Metode Daur Ulang:</strong> {info['recycling_method']}"
                f"</div>", unsafe_allow_html=True
            )

            if "history" not in st.session_state:
                st.session_state["history"] = []

            st.session_state["history"].append({
                "input_code": plastic_code_input,
                "material": info['material']
            })
        elif plastic_code_input:
            st.markdown(
                "<div class='warning-box'>Kode plastik tidak valid. Masukkan angka 1 hingga 7.</div>",
                unsafe_allow_html=True
            )

# --- Halaman Tentang Plastik ---
elif page == "Tentang Plastik":
    st.title("Tentang Kode Daur Ulang Plastik")
    for code, info in ric_info.items():
        st.subheader(f"Kode {code}: {info['material']}")
        st.write(f"**Contoh Penggunaan:** {info['example']}")
        st.write(f"**Risiko Kesehatan:** {info['health_risk']}")
        st.write(f"**Risiko Lingkungan:** {info['environment_risk']}")
        st.write(f"**Tingkat Daur Ulang:** {info['recycling_difficulty']}")
        st.write(f"**Metode Daur Ulang:** {info['recycling_method']}")
        st.markdown("---")

# --- Halaman Riwayat ---
elif page == "Riwayat":
    st.title("Riwayat Pencarian")
    if "history" in st.session_state and st.session_state["history"]:
        for idx, item in enumerate(st.session_state["history"],





    
