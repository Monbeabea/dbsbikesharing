import os
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
data_path = os.path.join(os.path.dirname(__file__), "D:/Submission/Dashboard/main_data.csv")
if not os.path.exists(data_path):
    st.error(f"File tidak ditemukan: {data_path}")
    st.stop()

df = pd.read_csv(data_path)

# Pastikan semua kolom yang diperlukan ada
df.columns = df.columns.str.strip()  # Bersihkan spasi di nama kolom
expected_columns = {"instant", "dteday", "season", "yr", "mnth", "holiday", "weekday", "workingday", "weathersit", "temp", "atemp", "hum", "windspeed", "casual", "registered", "cnt"}
missing_columns = expected_columns - set(df.columns)
if missing_columns:
    st.error(f"Kolom berikut tidak ditemukan dalam dataset: {missing_columns}")
    st.stop()

# Tampilkan kolom yang ada
st.write(f"Kolom yang tersedia dalam dataset: {df.columns.tolist()}")

# Sidebar
st.sidebar.title("📌 Filter Data")
selected_day = st.sidebar.selectbox("Pilih Hari:", ["Semua"] + sorted(df["weekday"].unique()))
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca:", ["Semua"] + sorted(df["weathersit"].unique()))

# Filter data
filtered_df = df.copy()
if selected_day != "Semua":
    filtered_df = filtered_df[filtered_df["weekday"] == selected_day]
if selected_weather != "Semua":
    filtered_df = filtered_df[filtered_df["weathersit"] == selected_weather]

# Periksa apakah data setelah filter kosong
if filtered_df.empty:
    st.warning("Tidak ada data yang tersedia dengan filter yang dipilih.")
else:
    # Header
    st.title("📊 Dashboard Penyewaan Sepeda")
    st.markdown("---")

    # Summary Metrics
    col1, col2 = st.columns(2)
    col1.metric("🚴 Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
    col2.metric("📅 Rata-rata Harian", f"{filtered_df['cnt'].mean():.0f}")

    # Visualisasi Penyewaan per Hari
    st.subheader("📅 Penyewaan Sepeda Berdasarkan Hari")
    avg_rentals_by_day = filtered_df.groupby("weekday")["cnt"].mean().reset_index()
    avg_rentals_by_day = avg_rentals_by_day.sort_values(by="cnt", ascending=False)

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=avg_rentals_by_day, x="cnt", y="weekday", palette="coolwarm", ax=ax)
    ax.set_xlabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)

    # Visualisasi Penyewaan per Bulan
    st.subheader("📅 Penyewaan Sepeda Berdasarkan Bulan")
    avg_rentals_by_month = filtered_df.groupby("mnth")["cnt"].mean().reset_index()
    avg_rentals_by_month = avg_rentals_by_month.sort_values(by="cnt", ascending=False)

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=avg_rentals_by_month, x="mnth", y="cnt", palette="coolwarm", ax=ax)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)

    # Visualisasi Pola Penyewaan Sepeda Berdasarkan Jam (jika ada kolom 'hour')
    if "hr" in filtered_df.columns:
        st.subheader("⏰ Pola Penyewaan Sepeda Harian")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.lineplot(data=filtered_df, x="hour", y="cnt", ci=None, marker="o", ax=ax)
        ax.set_xlabel("Jam")
        ax.set_ylabel("Jumlah Penyewaan")
        st.pyplot(fig)

    st.markdown("---")
    st.write("Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda berdasarkan faktor waktu dan cuaca.")
