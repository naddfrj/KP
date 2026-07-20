# Dashboard Visualisasi Graf Kegiatan Riset BRIN

Dashboard interaktif berbasis **Streamlit** untuk memvisualisasikan hubungan antara **peneliti** dan **kegiatan riset** di Pusat Riset Sains Data dan Informasi (PRSDI) BRIN menggunakan pendekatan **graph/network visualization**.

---

## Deskripsi

Proyek ini dikembangkan sebagai bagian dari kegiatan **Kerja Praktik di Badan Riset dan Inovasi Nasional (BRIN)**.

Dashboard bertujuan untuk menyajikan hubungan antara peneliti dan kegiatan riset dalam bentuk graf sehingga memudahkan pengguna dalam mengeksplorasi kolaborasi penelitian secara visual dan interaktif.

---

## Fitur

- Dashboard interaktif menggunakan Streamlit.
- Visualisasi graf menggunakan PyVis.
- Filter berdasarkan nama peneliti.
- Filter berdasarkan kelompok riset.
- Menampilkan hubungan antara peneliti dan kegiatan riset.
- Menampilkan foto profil peneliti PRSDI, logo BRIN untuk peneliti BRIN Non-PRSDI, dan ikon default untuk peneliti eksternal.
- Ukuran node menyesuaikan jumlah keterlibatan peneliti dalam kegiatan riset.
- Tooltip yang menampilkan informasi setiap node.

---

## Informasi Dataset

Dataset yang digunakan terdiri dari:

- **140 Peneliti**
- **5 Kelompok Riset**
- **33 Kegiatan Riset**

### Kelompok Riset

| Kelompok Riset | Jumlah Kegiatan |
|----------------|----------------:|
| Pemerintahan Digital (Digital Government) | 9 |
| Interaksi Manusia-Komputer dan Visualisasi (Human Computer Interaction and Visualisation) | 7 |
| Temu Kembali Informasi (Information Retrieval) | 4 |
| Rekayasa Pengetahuan dan Data (Knowledge and Data Engineering) | 3 |
| Pengolahan Bahasa Alami (Natural Language Processing) | 10 |

---

## Struktur Project

```
KP/
│
├── assets/
│   ├── photos/
│   └── default/
│
├── data/
│   └── dataset_graf.csv
│
├── utils/
│   ├── preprocessing.py
│   ├── image_map.py
│   ├── graph_builder.py
│   └── graph_visualizer.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Alur Sistem

1. Dataset dibaca menggunakan **Pandas**.
2. Data diproses pada modul `preprocessing.py`.
3. Nama peneliti dicocokkan dengan foto menggunakan `image_map.py`.
4. `graph_builder.py` membangun graf menggunakan **NetworkX**.
5. Setiap node diberikan atribut seperti label, ukuran, warna, gambar, dan informasi tambahan (tooltip).
6. `graph_visualizer.py` mengubah graf menjadi visualisasi interaktif menggunakan **PyVis**.
7. Dashboard ditampilkan melalui **Streamlit** sehingga pengguna dapat mengeksplorasi data secara interaktif.

---

## Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- NetworkX
- PyVis

---

## Cara Menjalankan

Clone repository:

```bash
git clone https://github.com/naddfrj/KP.git
```

Masuk ke folder project:

```bash
cd KP
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
streamlit run app.py
```

---

## Visualisasi Graf

Dashboard menggunakan visualisasi **Network Graph** untuk menggambarkan hubungan antara peneliti dan kegiatan riset.

Terdapat dua jenis node:

- **Node Riset**
- **Node Peneliti**

Hubungan (edge) menunjukkan keterlibatan seorang peneliti pada suatu kegiatan riset.

Visualisasi juga membedakan:

- **Warna node** berdasarkan peran (Koordinator dan Anggota).
- **Gambar node** berdasarkan kategori peneliti (PRSDI, BRIN Non-PRSDI, dan Eksternal BRIN).
- **Ukuran node** berdasarkan jumlah keterlibatan peneliti dalam kegiatan riset.

---

## Tujuan

Dashboard ini dikembangkan untuk:

- memvisualisasikan hubungan antara peneliti dan kegiatan riset;
- membantu memahami pola kolaborasi penelitian;
- mempermudah eksplorasi data penelitian melalui visualisasi yang interaktif.

---

## Pengembang

**Nadia Faraj**  
Program Studi Sains Data  
Institut Teknologi Sumatera (ITERA)

Kerja Praktik di  
**Pusat Riset Sains Data dan Informasi (PRSDI) BRIN**