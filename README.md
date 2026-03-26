# Emotion-Aware Image Captioning Dataset

Repository ini berisi pipeline untuk membangun dataset image captioning yang dilengkapi dengan label emosi multi-dimensi. Dataset dibangun di atas Flickr8k dan diperkaya menggunakan teknik prompting LLM (Google Gemini) serta clustering berbasis sentence embeddings.

---

## Struktur Repository

```
├── data/
│   ├── raw/                        # Dataset mentah dan hasil labeling awal
│   │   ├── dataset.csv             # Dataset Flickr8k (image + captions)
│   │   ├── captions.txt            # Captions dalam format teks
│   │   ├── dataset_clean.csv       # Dataset setelah cleaning
│   │   ├── dataset_with_mood_enhanced.csv  # Dataset dengan label emosi dari clustering
│   │   └── filenames_with_mood.csv # Mapping filename ke label mood
│   ├── multi_emotion_run_new1.csv  # Hasil run caption generation (run 1)
│   ├── multi_emotion_run_new2.csv  # Hasil run caption generation (run 2)
│   ├── multi_emotion_run_new1.json # Log lengkap run 1
│   ├── multi_emotion_run_new2.json # Log lengkap run 2
│   ├── multi_emotion_selection_run_new1.json  # Seleksi caption terbaik run 1
│   ├── multi_emotion_selection_run_new2.json  # Seleksi caption terbaik run 2
│   └── processed_images_mapping.csv           # Mapping gambar setelah preprocessing
├── Code_Labelling/
│   ├── notebooks/
│   │   ├── image_scaling_preprocessing.ipynb         # Preprocessing & scaling gambar
│   │   ├── code_labeling_dataset_enhanced.ipynb      # Clustering & labeling emosi
│   │   └── multi_emotion_caption_generation_new.ipynb # Generasi caption multi-emosi
│   └── images/                     # Visualisasi hasil clustering
├── src/
│   └── labelling_cnn_clip.py       # Script labeling menggunakan CNN + CLIP
├── scaled_images/                  # Output gambar setelah scaling (224x224)
├── .env                            # API key (tidak di-commit)
├── SETUP_API_KEY.md                # Panduan setup API key Gemini
└── README.md
```

---

## Pipeline

### 1. Preprocessing Gambar
Notebook: `image_scaling_preprocessing.ipynb`

Gambar dari Flickr8k di-resize ke ukuran **224x224** menggunakan metode padding agar rasio aspek tetap terjaga. Output disimpan ke folder `scaled_images/`.

### 2. Labeling Emosi via Clustering
Notebook: `code_labeling_dataset_enhanced.ipynb`

Caption teks di-embed menggunakan model **`all-MiniLM-L6-v2`** (SentenceTransformer), lalu di-cluster menggunakan **KMeans**. Setiap cluster kemudian diberi label emosi (contoh: Joy, Love, Confidence, Sadness, dll).

### 3. Generasi Caption Multi-Emosi
Notebook: `multi_emotion_caption_generation_new.ipynb`

Untuk setiap gambar dan emosi target, caption baru di-generate menggunakan **Google Gemini API** dengan 4 teknik prompting:
- `zero-shot`
- `few-shot`
- `chain-of-thought`
- `persona`

---

## Setup

### 1. Install dependencies

```bash
pip install python-dotenv google-generativeai sentence-transformers pandas scikit-learn
```

### 2. Setup API Key

Buat file `.env` di root repository:

```
GEMINI_API_KEY=your_api_key_here
```

Lihat `SETUP_API_KEY.md` untuk panduan lengkap mendapatkan API key dari [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## Dataset

Berbasis **Flickr8k** — dataset publik berisi 8.000 gambar dengan masing-masing 5 caption deskriptif.

Setiap entri pada dataset akhir memiliki:
- `filename` — nama file gambar
- `emotion` — label emosi target
- `technique` — teknik prompting yang digunakan
- `caption` — caption yang di-generate
- `timestamp` & `success` — metadata eksekusi

---

## Visualisasi

Hasil clustering tersedia di `Code_Labelling/images/`:

| File | Deskripsi |
|------|-----------|
| `cluster_distribution.png` | Distribusi jumlah data per cluster |
| `cluster_visualization_2d.png` | Visualisasi cluster dalam 2D (PCA/UMAP) |
| `cluster_wordclouds.png` | Word cloud per cluster emosi |
| `clustering_metrics.png` | Metrik evaluasi clustering |
| `final_emotion_distribution.png` | Distribusi label emosi final |
