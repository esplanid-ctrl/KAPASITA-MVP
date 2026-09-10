# Data Architecture & ETL Blueprint KAPASITA (MVP)
Dokumen ini adalah kelanjutan langsung dari PRD dan menjadi **blueprint teknis yang akan dipakai untuk implementasi**.

Tujuan utama blueprint ini:

| 1     `Data Mentah`2     `↓`3     `Data Bersih`4     `↓`5     `Master Dataset`6     `↓`7     `Priority Score`8     `↓`9     `Analitik`10     `↓`11     `Dashboard`12     `↓`13     `AI Copilot` |
| --- |

# 12. ETL Pipeline
## extract.py
Tugas:

| 1     `Download`2     `Clone`3     `Copy` |
| --- |
dari GitHub.

Output:

| 1     `raw/` |
| --- |
## transform.py
Tugas:

| 1     `Cleaning`2     `Standardisasi`3     `Normalisasi Nama Wilayah` |
| --- |
Output:

| 1     `processed/` |
| --- |
## merge.py
Tugas:

| 1     `Join semua dataset` |
| --- |
berdasarkan:

| 1     `kode_bps` |
| --- |
Output:

| 1     `master_dataset.csv` |
| --- |
## pipeline.py
Menjalankan semuanya.

| 1     `python pipeline.py` |
| --- |
Proses:

| 1     `Extract`2     `↓`3     `Transform`4     `↓`5     `Merge`6     `↓`7     `Feature Engineering`8     `↓`9     `Priority Score`10     `↓`11     `Clustering`12     `↓`13     `Recommendation`14     `↓`15     `Load SQLite` |
| --- |
# 13. Dashboard Data Flow
Saat user membuka dashboard:

| 1     `Dashboard`2     `↓`3     `SQLite`4     `↓`5     `score_result`6     `↓`7     `cluster_result`8     `↓`9     `recommendation_result` |
| --- |
Dashboard tidak menghitung ulang.

Keuntungan:

| 1     `Cepat`2     `Ringan`3     `Stabil` |
| --- |
# 14. Deliverable Berikutnya yang Harus Anda Buat
Sebelum coding apa pun, saya sangat menyarankan membuat 3 dokumen teknis berikut:
### D1 - Dataset Inventory


| 1     `Nama Dataset`2     `Sumber`3     `Link GitHub`4     `Format`5     `Update Terakhir` |
| --- |
### D2 - Data Dictionary


| 1     `Nama Kolom`2     `Tipe Data`3     `Definisi`4     `Satuan` |
| --- |
### D3 - Indicator Definition Sheet


| 1     `Nama Indikator`2     `Formula`3     `Bobot`4     `Arah Nilai`5     `Threshold` |
| --- |
Setelah ketiga dokumen ini selesai, kita sudah bisa masuk ke fase **implementasi ETL dan struktur kode proyek**, lalu membangun dashboard tanpa risiko mengubah arsitektur di tengah jalan.
