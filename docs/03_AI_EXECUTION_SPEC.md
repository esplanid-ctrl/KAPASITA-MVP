\# AI EXECUTION SPECIFICATION



\## Objective



AI Agent bertanggung jawab menghasilkan seluruh pipeline KAPASITA dari data mentah hingga dashboard.



\---



\# Agent 1



\## Data Discovery Agent



Tugas:



\- Memindai repository dataset

\- Membaca metadata file

\- Mengidentifikasi level wilayah

\- Mengidentifikasi indikator



Output:



data\_inventory.json



\---



\# Agent 2



\## Data Profiling Agent



Tugas:



\- Missing Value Detection

\- Duplicate Detection

\- Outlier Detection

\- Data Type Detection



Output:



profiling\_report.json



\---



\# Agent 3



\## Data Cleaning Agent



Tugas:



\- Standardisasi Nama Kolom

\- Cleaning

\- Harmonisasi Provinsi



Output:



clean\_dataset



\---



\# Agent 4



\## Master Dataset Agent



Tugas:



\- Menggabungkan seluruh dataset

\- Membentuk master dataset provinsi



Output:



master\_dataset.csv



\---



\# Agent 5



\## Feature Engineering Agent



Fitur:



\- Poverty Risk

\- Education Risk

\- Teacher Gap

\- Inclusion Need

\- Digital Gap



Output:



feature\_store.csv



\---



\# Agent 6



\## Scoring Agent



Formula:



Priority Score



30% Poverty Risk



25% Education Risk



20% Teacher Gap



15% Inclusion Need



10% Digital Gap



Output:



priority\_score.csv



\---



\# Agent 7



\## Explainability Agent



Output:



rootcause.csv



Contoh:



Papua



42% Poverty

28% Teacher

20% Education

10% Digital



\---



\# Agent 8



\## Clustering Agent



Algorithm:



KMeans



Cluster:



\- Teacher Capacity Gap

\- Inclusion Access Gap

\- Multi-Dimensional Risk



Output:



cluster\_result.csv



\---



\# Agent 9



\## Recommendation Agent



Rule Based Engine



Output:



recommendation\_result.csv



\---



\# Agent 10



\## Capacity Agent



Output:



capacity\_result.csv



Mapping:



Masalah

↓

Kompetensi

↓

Program Pengembangan



\---



\# Agent 11



\## Dashboard Agent



Output:



Streamlit Dashboard



Pages:



\- Executive Dashboard

\- Priority Map

\- Regional Analysis

\- Capacity Insight

\- AI Copilot



\---



\# Agent 12



\## Copilot Agent



Model:



Gemini



Input:



\- Priority Score

\- Cluster

\- Root Cause

\- Recommendation



Output:



\- Executive Summary

\- Explanation

\- Policy Insight

