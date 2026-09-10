# PRD (Product Requirements Document)
## KAPASITA
**AI Policy Intelligence Dashboard untuk Prioritas Pendidikan Inklusif dan Penguatan Kapasitas Aparatur**

Versi: MVP 1.0

Target Deadline: 13 September 2026

Platform: Web Dashboard (Streamlit)

Pengguna Utama: Analis Kebijakan, Perencana Program, Pengelola Pengembangan Kapasitas, Monev, Pengambil Keputusan Pemerintah.  

# 1. Product Vision
Menyediakan sistem pendukung keputusan yang membantu pemerintah mengidentifikasi wilayah prioritas pendidikan inklusif, memahami penyebab utama permasalahan, menentukan rekomendasi intervensi, memetakan kebutuhan kapasitas aparatur, dan menjelaskan hasil analisis melalui AI Copilot.  

# 2. MVP Scope
## In Scope
### Data Integration
- Dataset pendidikan

- Dataset sosial ekonomi

- Dataset wilayah
### Analytics
- Priority Score

- Root Cause Analysis

- Regional Clustering
### Policy Intelligence
- Rule-based Recommendation

- Capacity Insight
### Visualization
- Executive Dashboard

- Priority Map

- Detail Regional Analysis
### AI
- AI Policy Copilot (RAG sederhana)

## Out of Scope
Jangan dibuat pada MVP.

- Deep Learning

- SHAP Analysis

- Predictive Forecasting

- Auto Data Scraping

- Multi-user Login

- SSO

- Workflow Persetujuan

- PDF Generator

- Mobile App

- Dokumen Kebijakan Otomatis

# 3. Business Process


| 1     `Dataset`2     `  ↓ `3     4     `Scoring Engine`5     `  ↓ `6     7     `Priority Score`8     `  ↓ `9     10     `Root Cause`11     `  ↓ `12     13     `Clustering`14     `  ↓ `15     16     `Policy Recommendation`17     `  ↓ `18     19     `Capacity Insight`20     `  ↓ `21     22     `AI Policy Copilot` |
| --- |
# 4. Data Architecture
## Data Source
### Tabel Pendidikan


| 1     `education_data` |
| --- |
Field:

| 1     `id`2     `kode_wilayah`3     `provinsi`4     `kabupaten_kota`5     `jumlah_siswa_disabilitas`6     `jumlah_sekolah_inklusi`7     `jumlah_gpk`8     `tahun` |
| --- |
### Tabel Sosial Ekonomi


| 1     `social_data` |
| --- |
Field:

| 1     `id`2     `kode_wilayah`3     `persentase_kemiskinan`4     `ipm`5     `angka_putus_sekolah`6     `akses_internet`7     `tahun` |
| --- |
### Tabel Wilayah


| 1     `region` |
| --- |
Field:

| 1     `kode_wilayah`2     `provinsi`3     `kabupaten_kota`4     `latitude`5     `longitude` |
| --- |
# 5. Modul 1
# Priority Score Engine
## Tujuan
Menghasilkan skor prioritas pendidikan inklusif skala 0-100.  

## Input


| 1     `jumlah_gpk`2     `jumlah_siswa_disabilitas`3     `kemiskinan`4     `putus_sekolah`5     `akses_internet` |
| --- |
## Proses
### Langkah 1
Normalisasi

MinMaxScaler

### Langkah 2
Kalkulasi Bobot

MVP:

| 1     `Kemiskinan             35%`2     `Kekurangan GPK         25%`3     `Putus Sekolah          20%`4     `Akses Pendidikan       20%` |
| --- |
### Langkah 3
Hitung Skor

Output:

| 1     `0 - 100` |
| --- |
## Output
Contoh:

| 1     `{`2     `    ``"kabupaten"``:``"Mimika"``,`3     `    ``"priority_score"``:``88`4     `}` |
| --- |
## Acceptance Criteria
- Skor muncul untuk seluruh wilayah.

- Nilai antara 0-100.

- Dapat diurutkan.

# 6. Modul 2
# Priority Ranking
## Tujuan
Mengurutkan wilayah berdasarkan skor prioritas.  

## Logika


| 1     `Priority Score DESC` |
| --- |
## Output


| 1     `1. Kabupaten A`2     `2. Kabupaten B`3     `3. Kabupaten C` |
| --- |
## Acceptance Criteria
- Ranking otomatis.

- Top 10 dapat ditampilkan.

# 7. Modul 3
# Priority Map
## Tujuan
Visualisasi persebaran prioritas wilayah.  

## Library


| 1     `Plotly Choropleth Map` |
| --- |
## Layer
### Layer 1
Wilayah
### Layer 2
Priority Score

## Warna


| 1     `0-49     Hijau`2     `50-79    Kuning`3     `80-100   Merah` |
| --- |
## Interaksi
Klik wilayah:

| 1     `Nama Wilayah`2     `Priority Score`3     `Cluster` |
| --- |
## Acceptance Criteria
- Peta muncul.

- Tooltip muncul.

- Filtering bekerja.

# 8. Modul 4
# Root Cause Analysis
## Tujuan
Menjelaskan faktor yang menyebabkan wilayah menjadi prioritas.  

## Input
Output scoring engine.

## Perhitungan
Kontribusi faktor.

Contoh:

| 1     `Kemiskinan          40%`2     `Kekurangan GPK      30%`3     `Putus Sekolah       20%`4     `Akses               10%` |
| --- |
## Visual


| 1     `Horizontal Bar Chart` |
| --- |
## Output


| 1     `{`2     `   ``"kemiskinan"``:``40``,`3     `   ``"gpk"``:``30``,`4     `   ``"putus_sekolah"``:``20``,`5     `   ``"akses"``:``10`6     `}` |
| --- |
## Acceptance Criteria
- Total kontribusi = 100%.

- Faktor terbesar terlihat jelas.

# 9. Modul 5
# Regional Clustering
## Tujuan
Mengelompokkan wilayah berdasarkan pola permasalahan.  

## Algoritma
KMeans

## Jumlah Cluster


| 1     `3` |
| --- |
## Cluster
### Cluster A
Teacher Capacity Gap

Karakteristik:

| 1     `GPK rendah`2     `Siswa disabilitas tinggi` |
| --- |
### Cluster B
Access Limitation

Karakteristik:

| 1     `Akses rendah`2     `Infrastruktur rendah` |
| --- |
### Cluster C
Multi-Dimensional Risk

Karakteristik:

| 1     `Kemiskinan tinggi`2     `Putus sekolah tinggi` |
| --- |
## Output


| 1     `{`2     `   ``"cluster"``:``"Teacher Capacity Gap"`3     `}` |
| --- |
## Acceptance Criteria
- Seluruh wilayah memiliki cluster.

- Cluster dapat divisualisasikan.

# 10. Modul 6
# Policy Recommendation Engine
## Tujuan
Menghasilkan rekomendasi kebijakan berbasis aturan.  

## Metode
Rule-based Engine

## Rule 1


| 1     `IF GPK < threshold`2     3     `THEN`4     5     `Pelatihan Guru Inklusif` |
| --- |
## Rule 2


| 1     `IF Kemiskinan > threshold`2     3     `THEN`4     5     `Bantuan Pendidikan Inklusif` |
| --- |
## Rule 3


| 1     `IF Akses < threshold`2     3     `THEN`4     5     `Penguatan Sarana Inklusif` |
| --- |
## Output


| 1     `[`2     `  { `3     `    ``"priority"``:``1``,`4     `    ``"recommendation"``:``"Pelatihan Guru Inklusif"`5     `  } `6     `]` |
| --- |
## Acceptance Criteria
- Minimal 10 rule aktif.

- Rule dapat dijelaskan.

# 11. Modul 7
# Capacity Insight
## Tujuan
Menghubungkan masalah wilayah dengan kebutuhan pengembangan kapasitas aparatur.  

## Struktur


| 1     `Masalah`2     `↓`3     `Kompetensi`4     `↓`5     `Program Pengembangan` |
| --- |
## Mapping
### Gap


| 1     `Guru Inklusif` |
| --- |
### Kompetensi


| 1     `Pembelajaran Inklusif` |
| --- |
### Program


| 1     `Pelatihan Guru Inklusif Mahir` |
| --- |
## Output


| 1     `{`2     `   ``"issue"``:``"GPK rendah"``,`3     `   ``"competency"``:``"Pendidikan Inklusif"``,`4     `   ``"training"``:``"Pelatihan Guru Inklusif"`5     `}` |
| --- |
## Acceptance Criteria
- Minimal 10 mapping tersedia.

- Tampil otomatis berdasarkan masalah wilayah.

# 12. Modul 8
# Executive Dashboard
## Komponen
### KPI


| 1     `Total Wilayah`2     `Rata-rata Skor`3     `Prioritas Tinggi`4     `Prioritas Sedang`5     `Prioritas Rendah` |
| --- |
### Grafik


| 1     `Distribusi Prioritas`2     `Top 10 Wilayah`3     `Trend Nasional` |
| --- |
## Acceptance Criteria
- Load < 3 detik.

- Semua KPI konsisten.

# 13. Modul 9
# Regional Analysis Dashboard
## Filter


| 1     `Provinsi`2     `Kabupaten/Kota`3     `Tahun` |
| --- |
## Section
### Overview


| 1     `Priority Score`2     `Cluster`3     `Kategori` |
| --- |
### Root Cause


| 1     `Bar Chart` |
| --- |
### Recommendation


| 1     `Daftar Intervensi` |
| --- |
### Capacity Insight


| 1     `Kompetensi`2     `Pelatihan` |
| --- |
# 14. Modul 10
# AI Policy Copilot
## Tujuan
Menjelaskan hasil analitik menggunakan bahasa natural.  

## Model


| 1     `Google Gemini API` |
| --- |
sesuai proposal.  

## Input Context


| 1     `{`2     `   ``"wilayah"``:``"Mimika"``,`3     `   ``"score"``:``88``,`4     `   ``"cluster"``:``"Teacher Capacity Gap"``,`5     `   ``"root_cause"``:[``...``],`6     `   ``"recommendation"``:[``...``]`7     `}` |
| --- |
## Prompt Guardrail
AI tidak boleh:

| 1     `Mengarang kebijakan baru`2     `Mengubah skor`3     `Mengubah rekomendasi` |
| --- |
AI hanya boleh:

| 1     `Menjelaskan`2     `Meringkas`3     `Menginterpretasikan` |
| --- |
## Contoh Pertanyaan


| 1     `Mengapa Mimika prioritas?` |
| --- |


| 1     `Intervensi apa yang harus didahulukan?` |
| --- |


| 1     `Kapasitas apa yang perlu diperkuat?` |
| --- |
## Acceptance Criteria
- Response < 10 detik.

- Jawaban berbasis data wilayah aktif.

- Tidak menghasilkan informasi di luar konteks.

# 15. Database Design MVP


| 1     `education_data`2     `social_data`3     `region`4     `score_result`5     `cluster_result`6     `recommendation_result`7     `capacity_mapping`8     `chat_history` |
| --- |
SQLite sesuai proposal.  

# 16. Technology Stack
## Backend


| 1     `Python`2     `Pandas`3     `Numpy`4     `Scikit-Learn`5     `SQLite` |
| --- |
sesuai proposal.  

## Frontend


| 1     `Streamlit`2     `Plotly` |
| --- |
sesuai proposal.  

## AI


| 1     `Google Gemini` |
| --- |
sesuai proposal.  

# 17. Non Functional Requirements
## Performance
- Dashboard loading < 3 detik

- Peta loading < 5 detik
## Security
- API Key disimpan di .env

- Tidak hardcode credential
## Reliability
- Error handling untuk data kosong

- Error handling Gemini timeout
## Maintainability
- Modular architecture

- Semua engine dipisahkan dalam module terpisah

# 18. Definisi MVP Selesai
MVP dinyatakan selesai apabila:

✅ Data wilayah berhasil dimuat ke sistem

✅ Priority Score 0-100 berhasil dihitung

✅ Ranking wilayah tersedia

✅ Priority Map berfungsi

✅ Root Cause Analysis tampil

✅ Clustering 3 kelompok berjalan

✅ Recommendation Engine menghasilkan intervensi

✅ Capacity Insight menghasilkan penguatan kapasitas

✅ AI Policy Copilot menjelaskan hasil analisis

✅ Dashboard dapat didemokan end-to-end dari pemilihan wilayah sampai rekomendasi kebijakan

Ini adalah scope minimum yang langsung selaras dengan seluruh deliverable yang tertulis dalam proposal KAPASITA tanpa menambah fitur yang belum direncanakan.  
