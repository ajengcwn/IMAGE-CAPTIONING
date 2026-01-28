# 🎭 Prompting Techniques for Mood Caption Generation

## Overview

File ini menjelaskan modifikasi yang telah dibuat pada sistem mood caption generation untuk menggunakan 4 teknik prompting yang berbeda. Tujuannya adalah untuk membandingkan efektivitas berbagai pendekatan prompting dalam menghasilkan caption yang sesuai dengan mood.

## Files yang Dibuat/Dimodifikasi

### 1. `gemini_mood_caption_generator_prompting_techniques.ipynb`
- **Notebook utama** yang mengimplementasikan 4 teknik prompting
- Menggunakan strategi random selection untuk memastikan fair comparison
- Memproses 10 gambar per mood per technique (total 120 gambar)
- Menyimpan hasil dengan informasi technique yang digunakan

### 2. `prompting_techniques_examples.py`
- **File referensi** yang menunjukkan detail setiap teknik prompting
- Berisi contoh prompt lengkap untuk setiap kombinasi technique-mood
- Menyediakan framework evaluasi dan karakteristik setiap technique

## 4 Teknik Prompting yang Diimplementasikan

### 1. Zero-Shot Prompting
```
"Buat satu caption singkat untuk gambar ini dengan mood gembira dan ceria."
```
- **Pendekatan**: Instruksi langsung tanpa contoh
- **Kelebihan**: Cepat, sederhana, efisien
- **Kekurangan**: Mungkin kurang kreatif, pemahaman konteks terbatas

### 2. Few-Shot Prompting
```
"Ikuti gaya pembuatan caption sesuai contoh berikut:
Mood: Ceria -> 'Hari yang luar biasa untuk memulai petualangan baru! ✨😊'
Mood: Sedih -> 'Terkadang sunyi adalah teman terbaik untuk merenung. 💙😔'
Mood: Terkejut -> 'Subhanallah, keindahan ini benar-benar tak terduga! 😱✨'

Sekarang buat caption untuk mood gembira ->"
```
- **Pendekatan**: Belajar dari contoh, pattern recognition
- **Kelebihan**: Konsistensi style, format yang lebih baik
- **Kekurangan**: Mungkin terlalu mirip dengan contoh, kreativitas terbatas

### 3. Chain-of-Thought Prompting
```
"Analisis gambar ini dengan langkah berikut:
1. Deskripsikan suasana visual utama dalam gambar ini
2. Hubungkan suasana tersebut dengan emosi gembira dan kebahagiaan
3. Buat satu caption final yang paling pas berdasarkan analisis tersebut dengan mood ceria"
```
- **Pendekatan**: Pemikiran analitis, step-by-step reasoning
- **Kelebihan**: Analisis lebih dalam, pemahaman konteks lebih baik
- **Kekurangan**: Waktu processing lebih lama, mungkin terlalu analitis

### 4. Persona Prompting
```
"Anda adalah seorang Influencer Specialist yang ahli dalam psikologi audiens dan content creator berpengalaman. 
Buatlah caption yang sangat engaging untuk gambar ini dengan kesan gembira dan ceria yang dapat meningkatkan engagement rate."
```
- **Pendekatan**: Role-playing dengan expertise domain
- **Kelebihan**: Keahlian domain, konten engaging, kualitas profesional
- **Kekurangan**: Mungkin terlalu promotional, spesifik untuk style influencer

## Struktur Data Output

File hasil (`hasil_mood_captions_prompting_techniques.csv`) berisi kolom:
- `filename`: Nama file gambar
- `mood_type`: Jenis mood (joy, sad, surprised)
- `mood_column`: Kolom mood asli (mood_1, mood_2, mood_3)
- `prompting_technique`: Teknik yang digunakan (zero-shot, few-shot, chain-of-thought, persona)
- `caption`: Caption yang dihasilkan
- `processing_timestamp`: Waktu pemrosesan
- `image_exists`: Status keberadaan file gambar
- `processing_duration`: Durasi pemrosesan
- `success`: Status keberhasilan

## Random Selection Strategy

### Distribusi Gambar:
- **Total**: 120 gambar (10 per mood per technique)
- **Zero-Shot**: Gambar 1-30 (joy: 1-10, sad: 11-20, surprised: 21-30)
- **Few-Shot**: Gambar 31-60 (joy: 31-40, sad: 41-50, surprised: 51-60)
- **Chain-of-Thought**: Gambar 61-90 (joy: 61-70, sad: 71-80, surprised: 81-90)
- **Persona**: Gambar 91-120 (joy: 91-100, sad: 101-110, surprised: 111-120)

### Keunggulan:
- **No Overlap**: Setiap gambar hanya digunakan untuk 1 kombinasi technique-mood
- **Fair Comparison**: Setiap technique mendapat gambar yang berbeda
- **Reproducible**: Menggunakan random seed (42) untuk konsistensi
- **Balanced**: Jumlah gambar sama untuk setiap technique dan mood

## Cara Penggunaan

### 1. Setup dan Konfigurasi
```python
# Jalankan sel pertama untuk import dan setup
# Jalankan sel kedua untuk konfigurasi
```

### 2. Preview Selection (Opsional)
```python
# Uncomment baris berikut untuk preview:
preview_selection = preview_prompting_techniques_selection()
```

### 3. Mulai Processing
```python
# Uncomment baris berikut untuk mulai processing:
result_df = process_prompting_techniques_captions()
```

### 4. Analisis Hasil
```python
# Uncomment untuk analisis:
check_prompting_techniques_processing_status()
results_analysis = analyze_prompting_techniques_results()
comparison_results = compare_prompting_techniques()
```

## Metrics Evaluasi

### Quantitative Metrics:
1. **Success Rate (%)**: Persentase caption yang berhasil dibuat
2. **Average Processing Time**: Waktu rata-rata per gambar
3. **Average Caption Length**: Panjang rata-rata caption
4. **API Call Success Rate**: Tingkat keberhasilan API call

### Qualitative Metrics:
1. **Caption Creativity Score (1-5)**: Tingkat kreativitas caption
2. **Mood Appropriateness (1-5)**: Kesesuaian dengan mood
3. **Engagement Potential (1-5)**: Potensi engagement di media sosial
4. **Language Quality (1-5)**: Kualitas bahasa Indonesia
5. **Emoji Usage Appropriateness (1-5)**: Penggunaan emoji yang tepat

### Comparative Analysis:
1. **Consistency Across Similar Images**: Konsistensi untuk gambar serupa
2. **Variation in Caption Style**: Variasi dalam gaya caption
3. **Adherence to Mood Requirements**: Kepatuhan terhadap requirement mood
4. **Professional Quality Assessment**: Penilaian kualitas profesional

## Expected Results

### Zero-Shot:
- Caption sederhana dan langsung
- Processing time paling cepat
- Konsistensi rendah, variasi tinggi

### Few-Shot:
- Caption mengikuti pattern contoh
- Format lebih konsisten
- Style lebih seragam

### Chain-of-Thought:
- Caption lebih thoughtful dan analyzed
- Processing time lebih lama
- Kualitas analisis lebih baik

### Persona:
- Caption lebih engaging dan professional
- Style influencer yang kuat
- Fokus pada engagement rate

## Tips Penggunaan

1. **Pilih Technique Berdasarkan Kebutuhan**:
   - Zero-Shot: Untuk caption cepat dan sederhana
   - Few-Shot: Untuk konsistensi format
   - Chain-of-Thought: Untuk analisis mendalam
   - Persona: Untuk konten profesional

2. **Kombinasi Technique**:
   - Gunakan hasil terbaik dari setiap technique
   - Sesuaikan dengan jenis gambar dan target audience

3. **Evaluasi Berkelanjutan**:
   - Monitor success rate setiap technique
   - Adjust prompt berdasarkan hasil
   - Test dengan dataset yang berbeda

## Troubleshooting

### Common Issues:
1. **API Rate Limiting**: Sistem sudah menggunakan adaptive delay
2. **Memory Issues**: Garbage collection otomatis setiap 5 gambar
3. **File Not Found**: Check path gambar dan CSV input
4. **Processing Interrupted**: Sistem support resume dari checkpoint

### Solutions:
- Increase delay jika terlalu banyak error
- Reduce batch size jika memory terbatas
- Check file paths dan permissions
- Use checkpoint system untuk resume

## Future Improvements

1. **Additional Techniques**:
   - Self-Consistency Prompting
   - Tree of Thoughts
   - Multi-Modal Prompting

2. **Enhanced Evaluation**:
   - Human evaluation scores
   - A/B testing dengan real users
   - Sentiment analysis validation

3. **Optimization**:
   - Dynamic technique selection
   - Hybrid prompting approaches
   - Real-time performance monitoring

---

**Note**: File ini adalah bagian dari eksperimen prompting techniques untuk mood caption generation. Hasil dapat bervariasi tergantung pada dataset dan konfigurasi yang digunakan.