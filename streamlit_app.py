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

# Data lengkap untuk masing-masing kode RIC
ric_info = {
    "1": {
        "material": "Polyethylene Terephthalate (PET)",
        "example": "Botol air mineral, botol minuman ringan, kemasan minyak goreng",
        "health_risk": "Aman untuk sekali pakai. Pemakaian ulang atau panas bisa lepas antimon.",
        "recycling_difficulty": "Mudah",
        "recycling_method": "Cuci, cacah, lelehkan; jadi serat, karpet, wadah non-makanan"
    },
    "2": {
        "material": "High-Density Polyethylene (HDPE)",
        "example": "Botol susu, galon air, wadah deterjen",
        "health_risk": "Umumnya aman dan stabil",
        "recycling_difficulty": "Mudah",
        "recycling_method": "Cacah, lelehkan, jadi pipa, ember, produk rumah tangga"
    },
    "3": {
        "material": "Polyvinyl Chloride (PVC)",
        "example": "Pipa, lantai vinyl, mainan",
        "health_risk": "Mengandung ftalat, berisiko jika dibakar (dioksin)",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Daur ulang terbatas, jadi panel, selang"
    },
    "4": {
        "material": "Low-Density Polyethylene (LDPE)",
        "example": "Kantong plastik, pembungkus makanan",
        "health_risk": "Aman, tapi sering tidak didaur ulang",
        "recycling_difficulty": "Sedang",
        "recycling_method": "Lelehkan, jadi ubin, kantong sampah"
    },
    "5": {
        "material": "Polypropylene (PP)",
        "example": "Wadah microwave, sedotan, tutup botol",
        "health_risk": "Umumnya aman",
        "recycling_difficulty": "Sedang",
        "recycling_method": "Cacah, jadi komponen otomotif, wadah"
    },
    "6": {
        "material": "Polystyrene (PS)",
        "example": "Styrofoam, gelas kopi, wadah cepat saji",
        "health_risk": "Berpotensi bahaya (mengandung stirena)",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Beberapa bisa jadi bahan isolasi"
    },
    "7": {
        "material": "Other (PC, PLA, dll.)",
        "example": "Botol bayi (PC), galon keras, PLA bio",
        "health_risk": "Bervariasi (PC bisa mengandung BPA)",
        "recycling_difficulty": "Sulit",
        "recycling_method": "Tergantung bahan; PLA bisa dikomposkan industri"
    }
}


# --- Fungsi Identifikasi Placeholder ---
def identify_plastic_code(image_file):
    image = Image.open(image_file)
    width, height = image.size

    if width * height > 15000 and image.format in ["JPEG", "JPG"]:
        return {"prediction": "1", "probability": 0.75}  # Mengembalikan kode saja
    elif image.format == "PNG":
        return {"prediction": "2", "probability": 0.82}  # Mengembalikan kode saja
    elif "styrofoam" in str(image_file.name).lower():
        return {"prediction": "6", "probability": 0.68}  # Mengembalikan kode saja
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
                predicted_code = result["prediction"]
                st.write(f"*Kode Plastik yang Terdeteksi:* {predicted_code}")
                st.write(f"*Probabilitas:* {result['probability']:.2f}")
                if predicted_code in ric_info:
                    st.info(f"*Informasi Tambahan:*\n\n"
                            f"*Material:* {ric_info[predicted_code]['material']}\n"
                            f"*Contoh Penggunaan:* {ric_info[predicted_code]['example']}\n"
                            f"*Risiko Kesehatan:* {ric_info[predicted_code]['health_risk']}\n"
                            f"*Tingkat Daur Ulang:* {ric_info[predicted_code]['recycling_difficulty']}\n"
                            f"*Metode Daur Ulang:* {ric_info[predicted_code]['recycling_method']}")
                elif predicted_code == "Tidak dapat mengidentifikasi":
                    st.warning("Tidak dapat mengidentifikasi kode plastik. Coba unggah gambar lain.")

                # Simpan ke session_state sebagai riwayat
                if "history" not in st.session_state:
                    st.session_state["history"] = []

                st.session_state["history"].append({
                    "filename": uploaded_file.name,
                    "prediction": predicted_code,
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

    for code, info in ric_info.items():
        st.subheader(f"Kode {code}: {info['material']}")
        st.write(f"*Contoh Penggunaan:* {info['example']}")
        st.write(f"*Risiko Kesehatan:* {info['health_risk']}")
        st.write(f"*Tingkat Daur Ulang:* {info['recycling_difficulty']}")
        st.write(f"*Metode Daur Ulang:* {info['recycling_method']}")
        st.markdown("---")

# --- Halaman: Riwayat ---
elif page == "Riwayat":
    st.title("Riwayat Identifikasi")
    if "history" in st.session_state and st.session_state["history"]:
        for idx, item in enumerate(st.session_state["history"], start=1):
            st.write(f"{idx}. *Nama File:* {item['filename']}")
            st.write(f"Prediksi Kode: {item['prediction']} | Probabilitas: {item['probability']:.2f}")
            if item['prediction'] in ric_info:
                st.write(f"Material: {ric_info[item['prediction']]['material']}")
            st.markdown("---")
    else:
        st.info("Belum ada riwayat identifikasi dalam sesi ini.")


# --- Footer ---
st.markdown("---")
st.markdown("Dibuat dengan Streamlit oleh [Kelompok 1/PLI]")




    
