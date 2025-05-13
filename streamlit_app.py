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
    .stRadio > label {
        font-weight: bold;
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
        "recycling_difficulty": "Mudah",
        "recycling_method": "Cuci, cacah, lelehkan. Hasil daur ulang: serat sintetis (polyester), karpet, tali plastik, wadah non-makanan."
    },
    "2": {
        "material": "High-Density Polyethylene (HDPE)",
        "example": "Botol susu, galon air, wadah deterjen.",
        "health_risk": "Umumnya aman dan stabil.",
        "recycling_difficulty": "Mudah",
        "recycling_method": "Cacah, lelehkan, jadi pipa, ember, produk rumah tangga."
    },
    "3": {
        "material": "Polyvinyl Chloride (PVC)",
        "example": "Pipa, lantai vinyl, mainan.",
        "health_risk": "Mengandung ftalat, berisiko jika dibakar (dioksin).",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Daur ulang terbatas, bisa jadi panel atau selang."
    },
    "4": {
        "material": "Low-Density Polyethylene (LDPE)",
        "example": "Kantong plastik, pembungkus makanan.",
        "health_risk": "Aman, tapi sering tidak didaur ulang.",
        "recycling_difficulty": "Sedang",
        "recycling_method": "Lelehkan, jadi ubin, kantong sampah."
    },
    "5": {
        "material": "Polypropylene (PP)",
        "example": "Wadah microwave, sedotan, tutup botol.",
        "health_risk": "Umumnya aman.",
        "recycling_difficulty": "Sedang",
        "recycling_method": "Cacah, jadi komponen otomotif, wadah."
    },
    "6": {
        "material": "Polystyrene (PS)",
        "example": "Styrofoam, gelas kopi, wadah cepat saji.",
        "health_risk": "Berpotensi bahaya (mengandung stirena).",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Beberapa bisa jadi bahan isolasi."
    },
    "7": {
        "material": "Other (PC, PLA, dll.)",
        "example": "Botol bayi (PC), galon keras, PLA bio.",
        "health_risk": "Bervariasi (PC bisa mengandung BPA).",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Tergantung bahan; PLA bisa dikomposkan industri."
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
        st.write(f"*Contoh Penggunaan:* {info['example']}")
        st.write(f"*Risiko Kesehatan:* {info['health_risk']}")
        st.write(f"*Tingkat Daur Ulang:* {info['recycling_difficulty']}")
        st.write(f"*Metode Daur Ulang:* {info['recycling_method']}")
        st.markdown("---")

# --- Halaman Riwayat ---
elif page == "Riwayat":
    st.title("Riwayat Pencarian")
    if "history" in st.session_state and st.session_state["history"]:
        for idx, item in enumerate(st.session_state["history"], start=1):
            st.write(f"{idx}. Kode: {item['input_code']} — Material: {item['material']}")
            st.markdown("---")
    else:
        st.info("Belum ada riwayat pencarian dalam sesi ini.")

# --- Footer ---
st.markdown("---")
st.markdown("Dibuat dengan Streamlit oleh [Kelompok 1/PLI]")





    
