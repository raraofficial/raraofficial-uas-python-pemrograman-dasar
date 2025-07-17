## 🅿️ Program 2 — Aplikasi Parkir Kendaraan (GUI)

### 📝 Deskripsi:
Program ini merupakan aplikasi GUI sederhana yang berfungsi untuk menghitung biaya parkir berdasarkan:
- **Tipe kendaraan**
- **Lama parkir (dalam jam)**

Aplikasi dibuat menggunakan pustaka `Tkinter` dan memiliki antarmuka pengguna berupa input box, label, serta tombol untuk menghitung total biaya parkir. Biaya akan ditampilkan secara otomatis setelah pengguna menekan tombol **"Hitung Biaya"**.

### 💻 Fitur Utama:
- Input **tipe kendaraan**: (Sepeda, Motor, Mobil, Bis)
- Input **plat nomor kendaraan**
- Input **lama parkir** (dalam jam)
- Hitung dan tampilkan **total biaya parkir**
- Penanganan input berbasis GUI

### 💰 Tarif Parkir per Jam:
| Tipe Kendaraan | Tarif |
|----------------|--------|
| Sepeda         | Rp 1.000 |
| Motor          | Rp 2.000 |
| Mobil          | Rp 5.000 |
| Bis            | Rp 10.000 |

Jika pengguna mengisi tipe kendaraan yang tidak sesuai dengan daftar di atas, maka tarif akan dianggap **Rp 0** (default).

### 📄 Nama File:
`parkir_kendaraan_gui.py`

### ▶️ Cara Menjalankan:
1. Pastikan Python sudah terinstall.
2. Jalankan perintah berikut di terminal:
```bash
python parkir_kendaraan_gui.py
