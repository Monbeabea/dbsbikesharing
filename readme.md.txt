Bike Sharing Data Analysis Dashboard 🚲

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda guna memahami pola penggunaan berdasarkan faktor waktu, cuaca, dan hari. Data yang digunakan berasal dari dataset Bike Sharing Dataset, yang mencakup informasi penyewaan sepeda secara harian dan per jam. Melalui analisis eksploratif, ditemukan bahwa jumlah penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan akhir pekan. Selain itu, pola penggunaan menunjukkan lonjakan signifikan pada jam sibuk, yaitu pukul 08:00 - 09:00 dan 17:00 - 18:00, yang berkaitan dengan mobilitas pekerja. Faktor cuaca juga mempengaruhi jumlah penyewaan, di mana kondisi cerah meningkatkan jumlah penyewaan, sedangkan hujan atau cuaca buruk menurunkannya.  

Untuk menyajikan hasil analisis secara interaktif, dashboard dibuat menggunakan Streamlit. Dashboard ini memungkinkan pengguna untuk mengeksplorasi data penyewaan sepeda dalam berbagai aspek, seperti perbandingan antara hari kerja dan akhir pekan, tren penggunaan berdasarkan jam, serta dampak cuaca terhadap jumlah penyewaan. Dataset yang digunakan untuk dashboard disimpan dalam folder dashboard dengan nama main_data.csv, sementara data mentah tersedia di folder data.  

Agar proyek ini dapat dijalankan dengan baik, diperlukan beberapa dependensi yang telah dicantumkan dalam file requirements.txt. Untuk menjalankan dashboard, langkah pertama adalah memastikan bahwa semua library yang dibutuhkan sudah terinstal dengan perintah:  

pip install -r requirements.txt

Setelah itu, dashboard dapat dijalankan dengan perintah berikut:  

streamlit run dashboard/dashboard.py

Setelah menjalankan perintah ini, Streamlit akan memberikan URL lokal yang dapat dibuka di browser untuk melihat tampilan dashboard.  

Sebagai tambahan, file url.txt berisi referensi sumber dataset serta link laporan Streamlit. Dengan adanya dokumentasi ini, diharapkan proyek dapat digunakan dan dikembangkan lebih lanjut sesuai kebutuhan.