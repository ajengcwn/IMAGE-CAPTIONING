# Dokumentasi: Code Labeling Dataset

## Deskripsi
Notebook ini melakukan pelabelan otomatis dataset caption dengan menggunakan teknik clustering berbasis AI. Sistem ini menganalisis teks caption dan secara otomatis mengelompokkannya ke dalam 4 kategori emosi: Joy, Sad, Surprise, dan Love.

## Tujuan
- Melakukan pelabelan emosi otomatis pada dataset caption
- Menggunakan AI untuk menganalisis sentimen dan emosi dalam teks
- Menghasilkan dataset berlabel yang siap digunakan untuk training model

## Teknologi yang Digunakan
- **Sentence Transformers**: Model AI untuk mengubah teks menjadi embedding
- **Scikit-learn**: Library untuk clustering K-Means
- **Pandas**: Manipulasi dan analisis data
- **Model**: all-MiniLM-L6-v2 (model pre-trained untuk sentence embedding)

## Alur Kerja

### 1. Persiapan Data
```python
# Memuat dataset dari file CSV
file_path = '../data/raw/dataset_clean.csv'
df = pd.read_csv(file_path)
```
- Memuat dataset yang sudah dibersihkan (158,915 data)
- Menggunakan kolom 'caption_desc' sebagai input

### 2. Inisialisasi Model AI
```python
model = SentenceTransformer('all-MiniLM-L6-v2')
```
- Menggunakan model pre-trained untuk sentence embedding
- Model ini dapat memahami makna semantik dari teks

### 3. Proses Embedding
```python
embeddings = model.encode(df['caption_desc'].tolist(), show_progress_bar=True)
```
- Mengubah setiap caption menjadi vektor numerik (embedding)
- Proses ini memungkinkan AI memahami makna teks secara matematis

### 4. Clustering dengan K-Means
```python
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters, n_init='auto', random_state=42)
clusters = kmeans.fit_predict(embeddings)
```
- Mengelompokkan caption ke dalam 4 cluster berdasarkan kemiripan makna
- Menggunakan algoritma K-Means untuk clustering

### 5. Mapping Emosi
```python
mood_map = {
    0: "Joy",
    1: "Sad", 
    2: "Surprise",
    3: "Love"
}
```
- Memetakan setiap cluster ke label emosi yang sesuai
- Menghasilkan kolom 'emotion_label' baru

### 6. Penyimpanan Hasil
```python
output_path = current_dir.parent / 'data' / 'raw' / 'dataset_with_mood.csv'
df.to_csv(output_path, index=False)
```
- Menyimpan dataset berlabel ke file baru
- Output: `dataset_with_mood.csv`

## Input dan Output

### Input
- **File**: `../data/raw/dataset_clean.csv`
- **Kolom utama**: `caption_desc` (teks caption yang akan dilabeli)
- **Jumlah data**: 158,915 records

### Output  
- **File**: `../data/raw/dataset_with_mood.csv`
- **Kolom baru**: `emotion_label` (Joy, Sad, Surprise, Love)
- **Format**: CSV dengan semua kolom asli + label emosi

## Keunggulan Pendekatan

### 1. Otomatisasi
- Tidak memerlukan pelabelan manual yang memakan waktu
- Dapat memproses ribuan data dalam hitungan menit

### 2. Konsistensi
- Menggunakan model AI yang konsisten dalam penilaian
- Mengurangi subjektivitas manusia dalam pelabelan

### 3. Skalabilitas
- Dapat dengan mudah diterapkan pada dataset yang lebih besar
- Model dapat digunakan kembali untuk dataset serupa

## Limitasi

### 1. Akurasi
- Hasil clustering mungkin tidak 100% akurat
- Memerlukan validasi manual untuk memastikan kualitas label

### 2. Bahasa
- Model dioptimalkan untuk bahasa Inggris
- Performa mungkin berbeda untuk bahasa Indonesia

### 3. Konteks
- Clustering berdasarkan kemiripan semantik, bukan emosi eksplisit
- Mapping ke emosi dilakukan secara manual

## Penggunaan

### Prasyarat
```bash
pip install sentence-transformers scikit-learn pandas
```

### Menjalankan Notebook
1. Pastikan file `dataset_clean.csv` tersedia di `../data/raw/`
2. Jalankan semua cell secara berurutan
3. Hasil akan tersimpan di `../data/raw/dataset_with_mood.csv`

## Pengembangan Selanjutnya

### 1. Validasi Kualitas
- Implementasi metrik evaluasi clustering
- Validasi manual sampel hasil pelabelan
- Analisis distribusi emosi yang dihasilkan

### 2. Optimisasi Model
- Eksperimen dengan model embedding yang berbeda
- Fine-tuning untuk bahasa Indonesia
- Penyesuaian jumlah cluster optimal

### 3. Integrasi Pipeline
- Otomatisasi proses dari data mentah hingga berlabel
- Implementasi monitoring kualitas pelabelan
- Integrasi dengan sistem training model

## Catatan Teknis
- Proses embedding memakan waktu ~4 menit untuk 158K data
- Memory usage cukup tinggi untuk dataset besar
- Hasil clustering bersifat deterministik (random_state=42)