# 🔐 Setup API Key - Panduan Lengkap

## ✅ Setup Sudah Selesai!

Saya sudah setup keamanan API key untuk Anda dengan metode `.env` file.

---

## 📋 LANGKAH YANG HARUS ANDA LAKUKAN

### **STEP 1: Install Library `python-dotenv`**

Buka terminal/command prompt dan jalankan:

```bash
pip install python-dotenv
```

Atau jika menggunakan conda:

```bash
conda install python-dotenv
```

---

### **STEP 2: Buat API Key Baru**

1. Buka: https://aistudio.google.com/app/apikey
2. Login dengan akun Google Anda
3. Klik **"Create API Key"** atau **"Get API Key"**
4. Copy API key yang baru (contoh: `AIzaSyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567`)

---

### **STEP 3: Edit File `.env`**

1. Buka file `.env` di root project Anda
2. Ganti `YOUR_API_KEY_HERE` dengan API key baru Anda

**Sebelum:**
```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

**Sesudah:**
```
GEMINI_API_KEY=AIzaSyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567
```

**PENTING:** 
- Tidak ada spasi sebelum/sesudah `=`
- Tidak ada tanda kutip
- Simpan file setelah edit

---

### **STEP 4: Verifikasi Setup**

Buka notebook `Code_Labelling/notebooks/multi_emotion_caption_generation.ipynb` dan:

1. Restart kernel
2. Jalankan Cell 1 (import libraries)
3. Jalankan Cell 2 (logging setup)
4. Jalankan Cell 3 (change directory)
5. Jalankan Cell 4 (configuration)

**Jika berhasil, akan muncul:**
```
Configuration completed!
Images: 10, Captions: 120
Output: data/multi_emotion_run1.csv
```

**Jika gagal, akan muncul:**
```
ValueError: API key not found! Please set GEMINI_API_KEY in .env file
```

---

## 🔒 KEAMANAN

### **File yang AMAN untuk di-share:**
✅ `multi_emotion_caption_generation.ipynb` (sudah tidak ada API key)
✅ `.gitignore` (sudah include `.env`)
✅ Semua file lain di project

### **File yang TIDAK BOLEH di-share:**
❌ `.env` (berisi API key Anda)
❌ File apapun yang berisi API key

### **Cara memastikan `.env` tidak ter-upload ke GitHub:**
1. Cek file `.gitignore` sudah ada baris `.env`
2. Sebelum commit, jalankan: `git status`
3. Pastikan `.env` TIDAK muncul di list file yang akan di-commit

---

## 📝 PERUBAHAN YANG SUDAH DILAKUKAN

### **1. File `.env` (BARU)**
Lokasi: Root project
Isi: `GEMINI_API_KEY=YOUR_API_KEY_HERE`

### **2. File `.gitignore` (SUDAH ADA)**
Sudah include `.env` (tidak perlu diubah)

### **3. Notebook (DIUBAH)**
Lokasi: `Code_Labelling/notebooks/multi_emotion_caption_generation.ipynb`

**Cell 1 - Ditambahkan:**
```python
from dotenv import load_dotenv
```

**Cell 4 - Diubah:**
```python
# SEBELUM
API_KEY = "AIzaSyABAI_PQAryjzvw7UIeStI_Lbl13douv04"

# SESUDAH
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

if not API_KEY:
    raise ValueError("API key not found! Please set GEMINI_API_KEY in .env file")
```

---

## 🎯 CHECKLIST

Sebelum run notebook, pastikan:

- [ ] Install `python-dotenv` (`pip install python-dotenv`)
- [ ] Buat API key baru di https://aistudio.google.com/app/apikey
- [ ] Edit file `.env` dengan API key baru
- [ ] Verifikasi setup dengan run Cell 1-4
- [ ] File `.env` ada di `.gitignore`

---

## ❓ TROUBLESHOOTING

**Error: "No module named 'dotenv'"**
→ Install library: `pip install python-dotenv`

**Error: "API key not found!"**
→ Cek file `.env` sudah ada dan berisi `GEMINI_API_KEY=...`

**Error: "403 Your API key was reported as leaked"**
→ API key lama masih terpakai, pastikan sudah ganti dengan API key baru di `.env`

**File `.env` tidak terbaca**
→ Pastikan file `.env` ada di root project (sejajar dengan folder `Code_Labelling`, `data`, dll)

---

## 📞 BANTUAN

Jika masih ada masalah, tanyakan ke saya dengan menyertakan:
1. Error message yang muncul
2. Output dari Cell 4 (configuration)
3. Apakah file `.env` sudah dibuat dan diisi

---

**Setup selesai! Selamat menggunakan notebook dengan aman! 🔐**
