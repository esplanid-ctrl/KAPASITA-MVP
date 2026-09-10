# Data Architecture & ETL Blueprint KAPASITA (MVP)
Dokumen ini adalah kelanjutan langsung dari PRD dan menjadi **blueprint teknis yang akan dipakai untuk implementasi**.

Tujuan utama blueprint ini:

| 1     `Data Mentah`2     `↓`3     `Data Bersih`4     `↓`5     `Master Dataset`6     `↓`7     `Priority Score`8     `↓`9     `Analitik`10     `↓`11     `Dashboard`12     `↓`13     `AI Copilot` |
| --- |
# 1. Arsitektur Sistem End-to-End


| 1     `                    GITHUB REPOSITORY`2     3     `         ┌─────────────────────────────────────┐`4     `         │ Dataset BPS                         │`5     `         │ Dataset Kemendikdasmen              │`6     `         │ Dataset Sosial Ekonomi              │`7     `         │ Dataset Pendidikan                  │`8     `         └─────────────────────────────────────┘`9     `                          │`10     `                          ▼`11     `                  DATA INGESTION`12     `                          │`13     `                          ▼`14     `                 RAW DATA STORAGE`15     `                          │`16     `                          ▼`17     `                     ETL ENGINE`18     `           (Cleaning + Standardization)`19     `                          │`20     `                          ▼`21     `                 MASTER REGION MAP`22     `                          │`23     `                          ▼`24     `                   DATA MERGING`25     `                          │`26     `                          ▼`27     `                 FEATURE ENGINEERING`28     `                          │`29     `                          ▼`30     `                PRIORITY SCORE ENGINE`31     `                          │`32     `         ┌────────────────┼───────────────┐`33     `         ▼                ▼               ▼`34     35     `ROOT CAUSE      CLUSTERING ENGINE     RULE ENGINE`36     `  ANALYSIS                                `37     `         ▼                ▼               ▼`38     39     `        ANALYTICS DATA MART`40     `                          │`41     `                          ▼`42     43     `                      SQLITE`44     `                          │`45     `                          ▼`46     47     `                    STREAMLIT`48     `                          │`49     `                          ▼`50     51     `                 GEMINI COPILOT` |
| --- |
# 2. Repository Structure
Yang saya sarankan:

| 1     `kapasita/`2     3     `├── data/`4     `│`5     `├── raw/`6     `│   ├── pendidikan/`7     `│   ├── sosial/`8     `│   └── wilayah/`9     `│`10     `├── processed/`11     `│`12     `├── master/`13     `│   └── master_region.csv`14     `│`15     `├── etl/`16     `│   ├── extract.py`17     `│   ├── transform.py`18     `│   ├── merge.py`19     `│   └── pipeline.py`20     `│`21     `├── features/`22     `│   └── feature_engineering.py`23     `│`24     `├── scoring/`25     `│   └── priority_score.py`26     `│`27     `├── clustering/`28     `│   └── clustering.py`29     `│`30     `├── recommendations/`31     `│   └── rules.py`32     `│`33     `├── database/`34     `│   └── kapasita.db`35     `│`36     `├── dashboard/`37     `│   ├── executive.py`38     `│   ├── map.py`39     `│   ├── analysis.py`40     `│   ├── capacity.py`41     `│   └── copilot.py`42     `│`43     `├── app.py`44     `│`45     `└── requirements.txt` |
| --- |
# 3. Data Layer Design
## Layer 1 - Raw Data
Data hasil download GitHub.

Tidak boleh diubah.

Contoh:

| 1     `raw/`2     3     `kemiskinan_2025.csv`4     `gpk_2025.csv`5     `disabilitas_2025.csv`6     `internet_2025.csv`7     `ipm_2025.csv` |
| --- |
Tujuan:

| 1     `Single Source of Truth` |
| --- |
# Layer 2 - Clean Data
Data sudah dibersihkan.

Contoh:

| 1     `processed/`2     3     `clean_kemiskinan.csv`4     `clean_gpk.csv`5     `clean_disabilitas.csv` |
| --- |
Semua memiliki struktur:

| 1     `kode_wilayah`2     `provinsi`3     `kabupaten_kota`4     `tahun`5     `nilai` |
| --- |
# Layer 3 - Master Dataset
Dataset utama proyek.

| 1     `master_dataset.csv` |
| --- |
Contoh:

| 1     `kode_wilayah`2     `provinsi`3     `kabupaten_kota`4     5     `kemiskinan`6     `ipm`7     `akses_internet`8     `putus_sekolah`9     10     `jumlah_siswa_disabilitas`11     `jumlah_gpk`12     `jumlah_sekolah_inklusi` |
| --- |
Semua analitik hanya membaca file ini.

# 4. Master Region Strategy
Ini kritikal.

90% proyek pemerintah gagal di tahap ini.

Karena:

| 1     `Kab. Bandung`2     3     `Bandung`4     5     `KAB BANDUNG`6     7     `Kabupaten Bandung` |
| --- |
Dianggap berbeda.

Buat satu master:

| 1     `master_region.csv` |
| --- |
Struktur:

| 1     `kode_bps`2     `provinsi`3     `kabupaten_kota`4     5     `latitude`6     `longitude` |
| --- |
Contoh:

| 1     `3204`2     `Jawa Barat`3     `Kabupaten Bandung`4     `-6.914`5     `107.608` |
| --- |
Seluruh ETL harus mengacu ke key ini.

# 5. Data Transformation Rules
## Rule 1
Nama kolom dinormalisasi.

Sebelum:

| 1     `KABUPATEN`2     `Kabupaten`3     `nama_kab` |
| --- |
Menjadi:

| 1     `kabupaten_kota` |
| --- |
## Rule 2
Format numerik.

Sebelum:

| 1     `12,5` |
| --- |
Menjadi:

| 1     `12.5` |
| --- |
## Rule 3
Missing Value

Jika kosong:

| 1     `median()` |
| --- |
atau

| 1     `0` |
| --- |
sesuai definisi indikator.

## Rule 4
Duplicate

| 1     `drop_duplicates()` |
| --- |
# 6. Feature Engineering Layer
Ini tahap paling penting.

## Feature 1
Rasio GPK

| 1     `jumlah_siswa_disabilitas`2     `/`3     `jumlah_gpk` |
| --- |
Contoh:

| 1     `200 / 10`2     3     `= 20` |
| --- |
Interpretasi:

| 1     `20 siswa per GPK` |
| --- |
Semakin tinggi = semakin buruk.

## Feature 2
Inclusion Access Ratio

| 1     `jumlah_siswa_disabilitas`2     `/`3     `jumlah_sekolah_inklusi` |
| --- |
Semakin tinggi = semakin buruk.

## Feature 3
Socioeconomic Risk

Gabungan:

| 1     `kemiskinan`2     `+`3     `putus_sekolah` |
| --- |
## Output


| 1     `feature_table.csv` |
| --- |
# 7. Priority Score Engine
Input:

| 1     `rasio_gpk`2     `akses_inklusi`3     `kemiskinan`4     `putus_sekolah` |
| --- |
## Normalisasi


| 1     `MinMaxScaler()` |
| --- |
Output:

| 1     `0 sampai 1` |
| --- |
## Bobot MVP


| 1     `Kemiskinan           35%`2     `Rasio GPK            25%`3     `Putus Sekolah        20%`4     `Akses Inklusi        20%` |
| --- |
Formula:

| 1     `Score =`2     `(`3     `0.35 × Kemiskinan`4     5     `+`6     `0.25 × Rasio GPK`7     8     `+`9     `0.20 × Putus Sekolah`10     11     `+`12     `0.20 × Akses Inklusi`13     `)`14     15     `× 100` |
| --- |
Output:

| 1     `priority_score` |
| --- |
# 8. Clustering Layer
Input:

| 1     `kemiskinan`2     `rasio_gpk`3     `akses`4     `putus_sekolah` |
| --- |
Model:

| 1     `KMeans` |
| --- |
Jumlah cluster:

| 1     `3` |
| --- |
Output:

| 1     `cluster_id`2     `cluster_name` |
| --- |
Contoh:

| 1     `1`2     `Teacher Capacity Gap` |
| --- |
# 9. Recommendation Engine
Tidak menggunakan AI.

Menggunakan rule.

Contoh:

| 1     `IF rasio_gpk > 15`2     3     `THEN`4     5     `Pelatihan Guru Inklusif` |
| --- |


| 1     `IF kemiskinan > 20%`2     3     `THEN`4     5     `Bantuan Pendidikan Inklusif` |
| --- |


| 1     `IF akses_inklusi rendah`2     3     `THEN`4     5     `Penambahan Sekolah Inklusi` |
| --- |
Output:

| 1     `recommendation_result` |
| --- |
# 10. Capacity Mapping Engine
Hubungan:

| 1     `Masalah`2     `↓`3     `Kompetensi`4     `↓`5     `Program` |
| --- |
Contoh:

| 1     `GPK rendah` |
| --- |
↓

| 1     `Kompetensi Pendidikan Inklusif` |
| --- |
↓

| 1     `Pelatihan Pendidikan Inklusif` |
| --- |
Buat tabel:

| 1     `capacity_mapping.csv` |
| --- |
# 11. Database Design
SQLite cukup.

Tabel:

| 1     `region`2     `education`3     `social`4     5     `master_dataset`6     7     `score_result`8     `cluster_result`9     10     `recommendation_result`11     12     `capacity_result` |
| --- |
