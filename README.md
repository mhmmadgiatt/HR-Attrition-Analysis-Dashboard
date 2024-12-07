# Proyek Akhir: Analisis Faktor-Faktor yang Mempengaruhi Attrition Karyawan pada Perusahaan Jaya Jaya Maju

## Business Understanding

### Latar Belakang Bisnis

**Jaya Jaya Maju** adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun perusahaan terus berkembang, mereka menghadapi tantangan besar dalam mengelola karyawan, salah satunya adalah **tingginya tingkat attrition (perputaran karyawan)** yang mencapai lebih dari 10%. Tingginya tingkat attrition ini menyebabkan perusahaan harus terus-menerus menghadapi biaya tinggi untuk perekrutan dan pelatihan karyawan baru.

**Manajemen HR** ingin memahami lebih dalam tentang faktor-faktor yang menyebabkan karyawan keluar dan mencari cara untuk mengurangi tingkat attrition. Oleh karena itu, penting untuk menganalisis data karyawan untuk mengidentifikasi faktor-faktor utama yang berhubungan dengan **attrition**.

### Permasalahan Bisnis

Berikut adalah beberapa permasalahan bisnis yang perlu diselesaikan:

1. **Tingginya Tingkat Attrition**:
   Perusahaan menghadapi tantangan besar dengan tingkat attrition yang lebih dari 10%, yang berdampak pada biaya perekrutan dan pelatihan karyawan baru.

2. **Identifikasi Faktor Penyebab Attrition**:
   Untuk merumuskan strategi yang lebih baik, perusahaan perlu memahami faktor-faktor yang mempengaruhi keputusan karyawan untuk keluar. Beberapa faktor yang mungkin mempengaruhi attrition antara lain demografi, gaji, jenis kelamin, pekerjaan, kepuasan kerja, dan lainnya.

3. **Peningkatan Retensi Karyawan**:
   Dengan mengetahui faktor-faktor penyebab attrition, perusahaan dapat merancang kebijakan yang lebih efektif untuk meningkatkan retensi karyawan dan mengurangi perputaran karyawan.

4. **Pembuatan Dashboard Bisnis**:
   Manajer HR memerlukan **business dashboard** yang dapat membantu mereka memantau faktor-faktor yang mempengaruhi attrition secara real-time.

### Cakupan Proyek

Proyek ini berfokus pada **analisis data karyawan** untuk mengidentifikasi faktor-faktor yang mempengaruhi **attrition karyawan** dan mengembangkan **business dashboard** untuk memonitor data tersebut. Cakupan proyek ini meliputi:

**1. Eksplorasi dan Pembersihan Data**
- **Sumber Data**: [Dataset karyawan dengan berbagai atribut demografis dan pekerjaan](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)
- **Proses Pembersihan**:
  - Menghapus kolom yang tidak relevan
  - Menangani nilai yang hilang
  - Melakukan encoding untuk variabel kategorikal
  - Normalisasi data numerik

**2. Analisis Deskriptif**
#### Statistik Kunci
- **Total Karyawan**: [Jumlah dari Dataset]
- **Tingkat Attrition**: [Persentase Karyawan yang Keluar]
- **Usia Rata-Rata**: [Rata-Rata Usia Karyawan]

#### Visualisasi Utama
1. **Distribusi Attrition Berdasarkan Gender**
   - Membandingkan tingkat keluar karyawan antara pria dan wanita
   - Mengidentifikasi perbedaan signifikan dalam pola attrition

2. **Attrition Berdasarkan Perjalanan Bisnis**
   - Menganalisis hubungan antara frekuensi perjalanan bisnis dan keputusan karyawan untuk keluar

3. **Peran Pekerjaan dengan Attrition Tertinggi**
   - Menampilkan departemen dan peran yang paling rentan terhadap pergantian karyawan

**3. Identifikasi Faktor Penyebab Attrition**
#### Analisis Statistik
- **Faktor Kunci yang Mempengaruhi Attrition**:
   - Perjalanan Bisnis
   - Peran Pekerjaan
   - Lembur
   - Pendapatan Bulanan
   - Usia

#### Model Prediksi
- **Algoritma**: AdaBoost Classifier dengan Random Forest sebagai base estimator
- **Metrik Evaluasi**:
  - Akurasi Model
  - Laporan Klasifikasi
  - Confusion Matrix

**4. Dashboard Bisnis Interaktif**

#### Fitur Utama Dashboard
1. **Metrik Utama**
   - Total Karyawan
   - Tingkat Attrition
   - Usia Rata-Rata

2. **Visualisasi Interaktif**
   - Attrition berdasarkan Gender
   - Attrition berdasarkan Perjalanan Bisnis
   - Peran Pekerjaan dengan Attrition Tertinggi
   - Attrition berdasarkan Lembur
   - Distribusi Pendapatan dan Usia

**5. Temuan Utama**

#### Insights Kunci
1. **Faktor Dominan Attrition**:
   - Perjalanan bisnis yang intens
   - Beban kerja (lembur)
   - Ketidaksesuaian kompensasi

2. **Rekomendasi**:
   - Tinjau ulang kebijakan perjalanan bisnis
   - Evaluasi beban kerja di departemen dengan attrition tinggi
   - Kembangkan strategi retensi yang disesuaikan untuk peran berisiko tinggi

**6. Metodologi Teknis**

#### Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python
- **Pustaka Utama**:
  - Pandas (Manipulasi Data)
  - Scikit-learn (Pemodelan Prediktif)
  - Plotly (Visualisasi Interaktif)
  - Streamlit (Antarmuka Dashboard)

#### Alur Kerja Analisis
1. Pembersihan Data
2. Encoding Fitur
3. Splitting Data
4. Pelatihan Model
5. Evaluasi Model
6. Visualisasi Hasil

### Persiapan

**Sumber Data**:  
Data yang digunakan berasal dari dataset internal perusahaan yang berisi informasi mengenai karyawan, termasuk faktor demografi, data pekerjaan, dan status attrition.

**Setup Environment**:

1. **Clone Repository**:

   Jika Anda menggunakan Git untuk mengelola proyek, clone repository ini ke komputer lokal Anda.

   ```bash
   git clone https://github.com/mhmmadgiatt/HR-Attrition-Analysis-Dashboard.git
   ```

2. **Install Dependencies**:

   Install semua dependensi yang diperlukan dengan menjalankan:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Dashboard**:

   Setelah menginstal dependensi, jalankan dashboard menggunakan:

   ```bash
   streamlit run app.py
   ```

atau terdapat pada Streamlit : [Link Business Dashboard](https://hr-attrition-analysis-dashboard-ibtobvhkxtmwqixcwluyz9.streamlit.app/)

---

## Business Dashboard

Dashboard ini menyediakan analisis komprehensif tentang attrisi karyawan menggunakan alat visualisasi interaktif berbasis Streamlit. Dashboard memanfaatkan pustaka Python seperti Streamlit, Pandas, dan Plotly untuk menciptakan visualisasi dan metrik yang informatif.

### Komponen Dashboard

#### Metrik Utama
- **Total Karyawan**: Menampilkan jumlah total karyawan dalam departemen yang dipilih
- **Tingkat Attrisi**: Persentase karyawan yang telah meninggalkan perusahaan
- **Rata-rata Usia**: Usia rata-rata karyawan dalam dataset

### Visualisasi

#### 1. Attrition by Gender
- **Jenis**: Bagan Batang Berkelompok
- **Wawasan**: 
  - Membandingkan tingkat attrisi antara karyawan laki-laki dan perempuan
  - Membantu mengidentifikasi tren attrisi berdasarkan jenis kelamin

#### 2. Attrition by Business Travel
- **Jenis**: Bagan Batang Berkelompok
- **Wawasan**:
  - Mengeksplorasi hubungan antara frekuensi perjalanan bisnis dan attrisi karyawan
  - Mengungkapkan bagaimana pola perjalanan memengaruhi retensi karyawan

#### 3. Attrition by Job Role
- **Jenis**: Bagan Batang Vertikal
- **Wawasan**:
  - Menyoroti peran pekerjaan dengan tingkat attrisi tertinggi
  - Membantu mengidentifikasi posisi yang paling rentan terhadap pergantian karyawan

#### 4. Attrition by Overtime
- **Jenis**: Bagan Pai
- **Wawasan**:
  - Menunjukkan proporsi attrisi terkait dengan pekerjaan lembur
  - Membantu memahami dampak jam kerja yang diperpanjang terhadap retensi karyawan

#### 5. Monthly Income vs Attrition
- **Jenis**: Scatter Plot
- **Wawasan**:
  - Memvisualisasikan hubungan antara pendapatan bulanan, usia, dan status attrisi
  - Membantu mengidentifikasi korelasi potensial antara kompensasi dan pergantian karyawan

---

## Conclusion

Dari hasil analisis yang dilakukan melalui dashboard, berikut adalah beberapa **kesimpulan utama** terkait faktor-faktor yang memengaruhi **attrition** karyawan di perusahaan **Jaya Jaya Maju**:

1. **Attrition Rate**: Perusahaan memiliki **attrition rate** sebesar **16,92%**, dengan 179 karyawan yang keluar dari total 1.058 karyawan.
2. **Gender**: Karyawan pria memiliki tingkat pengunduran diri yang lebih tinggi dibandingkan wanita, dengan 108 pria yang keluar, menunjukkan bahwa **gender** memainkan peran penting dalam keputusan karyawan untuk bertahan atau keluar.
3. **Business Travel**: Karyawan yang **jarang melakukan perjalanan bisnis** lebih cenderung keluar dibandingkan dengan karyawan yang sering bepergian, yang menunjukkan adanya hubungan antara **frekuensi perjalanan bisnis** dan tingkat attrition.
4. **Job Role**: **Laboratory Technician** memiliki tingkat attrition tertinggi, dengan posisi ini menjadi yang paling rentan terhadap pengunduran diri. Hal ini mengindikasikan bahwa posisi tertentu lebih terdampak oleh berbagai faktor seperti beban kerja atau ketidakpuasan.
5. **Overtime**: Karyawan yang **bekerja lembur** lebih cenderung keluar, yang menunjukkan bahwa **jam kerja yang lebih panjang** dapat berdampak negatif pada retensi karyawan.
6. **Monthly Income**: Karyawan dengan penghasilan bulanan **antara 2000-2999** lebih banyak yang keluar, yang bisa menunjukkan bahwa **kompensasi yang lebih rendah** dapat menjadi faktor pemicu pengunduran diri.
7. **Work-Life Balance**: Karyawan dengan tingkat **work-life balance rendah** memiliki risiko attrition yang lebih tinggi, mengindikasikan pentingnya keseimbangan antara pekerjaan dan kehidupan pribadi untuk mempertahankan karyawan.

---

## Rekomendasi Action Items

Untuk mengurangi tingkat **attrition** dan meningkatkan retensi karyawan, perusahaan dapat mempertimbangkan beberapa langkah berikut berdasarkan hasil analisis di dashboard:

1. **Evaluasi Program Work-Life Balance**:
   - **Implementasi kebijakan kerja fleksibel** seperti jam kerja yang dapat disesuaikan dan opsi kerja jarak jauh untuk meningkatkan keseimbangan kehidupan kerja dan mengurangi **attrition** yang dipengaruhi oleh work-life balance.
  
2. **Tinjau Penghasilan dan Insentif**:
   - **Review struktur gaji** terutama untuk karyawan di rentang penghasilan rendah (2000-2999), dan pastikan bahwa **insentif dan tunjangan** yang diberikan kompetitif dengan industri, guna mengurangi pengunduran diri karyawan.
  
3. **Kurangi Jam Kerja Lembur**:
   - Mengurangi beban **lembur** bagi karyawan yang bekerja lebih dari jam normal dan memastikan kompensasi yang adil. Pekerjaan lembur yang berlebihan dapat memengaruhi kesejahteraan karyawan dan meningkatkan **attrition**.
  
4. **Fokus pada Departemen Rentan**:
   - **Identifikasi masalah di Departemen RnD** yang memiliki tingkat **attrition** tertinggi. Fokus pada **perbaikan lingkungan kerja** atau **peningkatan kompensasi** bagi karyawan yang bekerja di departemen ini.
  
5. **Perbaiki Kepuasan Kerja dan Lingkungan Kerja**:
   - Lakukan survei rutin untuk mengetahui tingkat **kepuasan karyawan** dan identifikasi faktor-faktor yang mempengaruhi ketidakpuasan di tempat kerja. **Kepuasan lingkungan kerja** yang buruk dapat menyebabkan tingginya tingkat pengunduran diri.

6. **Kembangkan Program Pengembangan Karir**:
   - **Fasilitasi peluang pengembangan karir** untuk posisi dengan tingkat attrition tertinggi, seperti **Laboratory Technician**, dengan memberikan pelatihan lebih lanjut atau jalur promosi yang jelas untuk meningkatkan **retensi karyawan**.

Dengan langkah-langkah ini, perusahaan dapat **menurunkan tingkat attrition**, meningkatkan **kesejahteraan karyawan**, dan menciptakan **lingkungan kerja yang lebih baik** serta lebih produktif.

---
