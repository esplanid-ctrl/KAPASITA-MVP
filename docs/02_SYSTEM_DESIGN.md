\# SYSTEM DESIGN



\## High Level Architecture



```text

Dataset Repository

&#x20;       ↓

AI Data Discovery

&#x20;       ↓

ETL Pipeline

&#x20;       ↓

Master Dataset

&#x20;       ↓

Feature Store

&#x20;       ↓

Analytics Engine

&#x20;       ↓

SQLite

&#x20;       ↓

Streamlit Dashboard

&#x20;       ↓

Gemini Copilot

```



\## Data Layer



\### Raw Data



Github Dataset Repository



\### Clean Data



Hasil cleaning dan harmonisasi.



\### Feature Store



Fitur analitik terstandarisasi.



\### Data Mart



Output untuk dashboard.



\---



\## Modules



\### ETL



\- extract.py

\- transform.py

\- merge.py

\- pipeline.py



\### Analytics



\- scoring.py

\- rootcause.py

\- clustering.py

\- recommendation.py

\- capacity\_mapping.py



\### Dashboard



\- executive.py

\- regional.py

\- capacity.py

\- copilot.py



\### AI



\- gemini\_client.py

\- prompt\_builder.py



\---



\## Database



SQLite



Tables:



\- master\_dataset

\- feature\_store

\- priority\_score

\- cluster\_result

\- recommendation\_result

\- capacity\_result

\- chat\_history



\---



\## Technology Stack



\### Backend



\- Python

\- Pandas

\- NumPy

\- Scikit Learn



\### Database



\- SQLite



\### Frontend



\- Streamlit

\- Plotly



\### AI



\- Gemini



\### Deployment



\- Streamlit Cloud

