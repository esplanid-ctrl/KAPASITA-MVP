# Google Drive Data Architecture

Recommended folders:
- `/KAPASITA-MVP/DATA/`
- `/KAPASITA-MVP/POLICY/`

The repository contains only logical source keys:
`DATA_DRIVE` and `POLICY_DRIVE`.

Secrets:
- GEMINI_API_KEY
- GEMINI_MODEL
- GOOGLE_DRIVE_DATA_FOLDER_ID
- GOOGLE_DRIVE_POLICY_FOLDER_ID
- GOOGLE_SERVICE_ACCOUNT_JSON

The application downloads approved files into temporary runtime storage, validates them, and never exposes raw private files through the dashboard.
