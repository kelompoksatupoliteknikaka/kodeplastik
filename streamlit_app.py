import streamlit as st
from PIL import Image
import numpy as np

# --- Data Kode Plastik ---
CLASS_NAMES = {
    0: "1 (PET atau PETE)",
    1: "2 (HDPE)",
    2: "3 (PVC atau V)",
    3: "4 (LDPE)",
    4: "5 (PP)",
    5: "6 (PS)",
    6: "7 (Lain-lain)"
}

PLASTIC_INFO = {
    "1 (PET atau PETE)": "Polyethylene Terephthalate. Umumnya digunakan untuk botol minuman ringan...",
    "2 (HDPE)": "High-Density Polyethylene. Digunakan untuk botol susu, botol deterjen...",
    "3 (PVC atau V)": "Polyvinyl Chloride. Digunakan dalam pipa, kabel, mainan...",
    "4 (LDPE)": "Low-Density Polyethylene. Digunakan untuk kantong plastik, cling wrap...",
    "5 (PP)": "Polypropylene. Digunakan untuk wadah makanan, tutup botol...",
    "6 (PS)": "Polystyrene (Styrofoam). Digunakan untuk wadah makanan sekali pakai...",
    "7 (Lain-lain)": "Kategori ini mencakup semua jenis plastik lain seperti PC, PLA..."
}

# --- Fungsi Identifikasi Placeholder ---
def identify_plastic_code(image_file):
    image = Image.open(image_file)
    width, height = image.size

    if width * height > 15000 and image.format in ["JPEG", "JPG"]:
        return {"prediction": "1 (PET atau PETE)", "probability": 0.75}
    elif image.format == "PNG":
        return {"prediction": "2 (HDPE)", "probability": 0.82}
    elif "styrofoam" in str(image_file.name).lower():
        return {"prediction": "6 (PS)", "probability": 0.68}
    else:
        return {"prediction": "Tidak dapat mengidentifikasi", "probability": 0.5}

# --- Sidebar Navigasi ---
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Identifikasi", "Tentang Plastik", "Riwayat"])

# --- Halaman: Identifikasi ---
if page == "Identifikasi":
    st.title("Aplikasi Identifikasi Kode Plastik Berbasis Gambar")
    st.write("Unggah gambar dari bagian bawah wadah plastik yang menunjukkan kode daur ulang.")

    uploaded_file = st.file_uploader("Pilih gambar kode plastik...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang Diunggah.", use_column_width=True)

        if st.button("Identifikasi"):
            with st.spinner("Menganalisis gambar..."):
                result = identify_plastic_code(uploaded_file)

            st.subheader("Hasil Identifikasi:")
            if "prediction" in result:
                st.write(f"**Kode Plastik yang Terdeteksi:** *{result['prediction']}*")
                st.write(f"**Probabilitas:** *{result['probability']:.2f}*")
                if result["prediction"] in PLASTIC_INFO:
                    st.info(PLASTIC_INFO[result["prediction"]])
                elif result["prediction"] == "Tidak dapat mengidentifikasi":
                    st.warning("Tidak dapat mengidentifikasi kode plastik. Coba unggah gambar lain.")

                # Simpan ke session_state sebagai riwayat
                if "history" not in st.session_state:
                    st.session_state["history"] = []

                st.session_state["history"].append({
                    "filename": uploaded_file.name,
                    "prediction": result["prediction"],
                    "probability": result["probability"]
                })
            else:
                st.error("Terjadi kesalahan dalam proses identifikasi.")
    else:
        st.info("Silakan unggah gambar kode plastik untuk memulai identifikasi.")

# --- Halaman: Tentang Plastik ---
elif page == "Tentang Plastik":
    st.title("Tentang Kode Daur Ulang Plastik")
    st.write("Berikut adalah informasi tentang berbagai jenis plastik berdasarkan kode daur ulang:")

    for code, info in PLASTIC_INFO.items():
        st.subheader(code)
        st.write(info)

# --- Halaman: Riwayat ---
elif page == "Riwayat":
    st.title("Riwayat Identifikasi")
    if "history" in st.session_state and st.session_state["history"]:
        for idx, item in enumerate(st.session_state["history"], start=1):
            st.write(f"**{idx}. Nama File:** {item['filename']}")
            st.write(f"Prediksi: {item['prediction']} | Probabilitas: {item['probability']:.2f}")
            st.markdown("---")
    else:
        st.info("Belum ada riwayat identifikasi dalam sesi ini.")

# --- Footer ---
st.markdown("---")
st.markdown("Dibuat dengan Streamlit oleh [Kelompok 1/PLI]")

    
