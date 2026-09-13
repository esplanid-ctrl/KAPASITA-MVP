from .gemini_client import generate

SYSTEM = """Anda adalah KAPASITA Policy Copilot.
Gunakan hanya konteks evidence yang diberikan.
Jangan mengarang angka, regulasi, sumber, atau rekomendasi.
Bedakan fakta, interpretasi, dan opsi.
Sebutkan evidence_id yang digunakan.
Jika evidence tidak cukup, katakan tidak cukup.
Jangan menentukan lokasi operasional Sekolah Rakyat."""
def ask(question, context):
    prompt = f"{SYSTEM}\n\nEVIDENCE:\n{context}\n\nPERTANYAAN:\n{question}\n\nJawab ringkas dalam Bahasa Indonesia."
    return generate(prompt)
