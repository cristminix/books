# 3 Melibatkan asisten GPT

## Bab ini mencakup
- Memperkenalkan platform Asisten GPT OpenAI dan UI ChatGPT 
- Membangun GPT yang dapat menggunakan kemampuan interpretasi kode
- Memperluas asisten melalui tindakan khusus 
- Menambahkan pengetahuan ke GPT melalui unggahan file
- Mengkomersialkan GPT Anda dan menerbitkannya ke GPT Store 

Saat kita menjelajahi perang salib OpenAI ke dalam asisten dan apa yang telah diisyaratkan, pada akhirnya, sebuah platform agen yang disebut Asisten GPT, kita akan memperkenalkan asisten GPT melalui antarmuka ChatGPT. Kemudian, kita akan menambahkan beberapa asisten yang dikembangkan sepenuhnya yang dapat menyarankan resep dari bahan-bahan, menganalisis data sepenuhnya sebagai ilmuwan data, memandu pembaca melalui buku, dan diperluas dengan tindakan khusus. Pada akhir bab, kita akan siap untuk membangun agen yang berfungsi penuh yang dapat diterbitkan ke Toko GPT OpenAI.

## 3.1 Menjelajahi asisten GPT melalui ChatGPT

ChatGPT (ChatGPT Plus, pada saat penulisan) memungkinkan Anda untuk membangun asisten GPT, menggunakan asisten lain, dan bahkan menerbitkannya, seperti yang akan Anda lihat di akhir bab. Ketika OpenAI mengumumkan perilisan platform Asisten GPT, itu membantu mendefinisikan dan memperkuat kemunculan agen AI. Dengan demikian, ini layak ditinjau secara serius oleh siapa pun yang tertarik untuk membangun dan menggunakan sistem agen. Pertama, kita akan melihat membangun asisten GPT melalui ChatGPT Plus, yang memerlukan langganan premium. Jika Anda tidak ingin membeli langganan, jelajahi bab ini sebagai pengantar, dan bab 6 akan menunjukkan penggunaan layanan API nanti.

Gambar 3.1 menunjukkan halaman untuk Toko GPT di dalam ChatGPT (https://chatgpt.com/gpts). Dari sini, Anda dapat mencari dan menjelajahi berbagai GPT untuk hampir semua tugas. Jumlah penggunaan biasanya akan menunjukkan seberapa baik setiap GPT bekerja, jadi nilailah mana yang paling cocok untuk Anda. 

![Gambar 3.1](Images/3-1.png "Antarmuka utama ke Toko GPT")

*Gambar 3.1 Antarmuka utama ke Toko GPT*

Membuat Asisten GPT pertama Anda semudah mengklik tombol Buat dan mengikuti antarmuka obrolan Pembangun GPT. Gambar 3.2 menunjukkan penggunaan Pembangun untuk membuat GPT. Mengerjakan latihan ini beberapa kali bisa menjadi cara yang bagus untuk mulai memahami persyaratan asisten.

![Gambar 3.2](Images/3-2.png "Berinteraksi dengan Pembangun GPT untuk membuat asisten")

*Gambar 3.2 Berinteraksi dengan Pembangun GPT untuk membuat asisten*

Setelah bekerja dengan Pembangun, Anda dapat membuka panel konfigurasi manual, yang ditunjukkan pada gambar 3.3, dan mengedit GPT secara langsung. Anda akan melihat nama, deskripsi, instruksi, dan pemula percakapan diisi dari percakapan Anda dengan Pembangun. Ini bisa menjadi awal yang baik, tetapi umumnya, Anda akan ingin mengedit dan mengubah properti ini secara manual.

![Gambar 3.3](Images/3-3.png "Panel Konfigurasi antarmuka platform Asisten GPT")

*Gambar 3.3 Panel Konfigurasi antarmuka platform Asisten GPT*

Jika Anda ingin mengikuti serta membangun Pendamping Kuliner Anda sendiri, masukkan teks dari daftar 3.1 ke dalam instruksi. Instruksi ini sebagian dibuat dengan bercakap-cakap dengan Pembangun dan ditambahkan berdasarkan output eksplisit. Output eksplisit ditambahkan ke instruksi sebagai aturan. 

### Daftar 3.1 Instruksi untuk Pendamping Kuliner

```
Culinary Companion membantu pengguna dengan nada ramah dan menarik, 
mengingatkan pada koki terkenal Julia Child.    #1
Ini memberikan ide makanan cepat dan menyederhanakan resep kompleks, dengan fokus pada 
bahan-bahan yang sudah dimiliki pengguna. GPT ini menekankan saran kuliner yang praktis dan mudah
diikuti serta beradaptasi dengan preferensi diet. Ini 
dirancang untuk membuat memasak menjadi pengalaman yang lebih mudah diakses dan menyenangkan, 
mendorong pengguna untuk bereksperimen dengan makanan mereka sambil menawarkan kiat-kiat 
bermanfaat dengan cara yang hangat dan mudah didekati.    #2

ATURAN:
Saat membuat resep, selalu buat gambar dari resep akhir yang sudah disiapkan
.                                                                  #3
Saat membuat resep, perkirakan kalori dan nilai gizi 
per porsi.                                                             
Saat membuat resep, berikan daftar belanja bahan-bahan dengan 
perkiraan harga yang dibutuhkan untuk menyelesaikan resep.                          
Saat membuat resep, perkirakan total biaya per porsi berdasarkan 
daftar belanja.
```

- #1 Kepribadian atau persona asisten Anda
- #2 Pedoman umum peran dan tujuan agen 
- #3 Seperangkat aturan yang akan diikuti agen saat menyarankan resep

Menentukan aturan untuk asisten/agen pada dasarnya membuat templat untuk apa yang akan dihasilkan agen. Menambahkan aturan memastikan bahwa output GPT konsisten dan selaras dengan harapan Anda tentang bagaimana agen harus beroperasi. Mendefinisikan dan memberikan persona kepada asisten/agen memberi mereka kepribadian yang unik dan mudah diingat.

> **Catatan** Memberikan kepribadian tertentu kepada asisten/agen dapat membuat perbedaan dalam jenis dan bentuk output. Meminta agen memasak untuk berbicara sebagai koki selebriti pertama, Julia Child, tidak hanya memberikan nada yang menyenangkan tetapi juga melibatkan lebih banyak referensi yang mungkin menyebutkan atau membicarakan gaya memasak dan pengajarannya. Saat membangun asisten/agen, memberikan persona/kepribadian tertentu dapat membantu.

Hanya dengan beberapa langkah ini, kita memiliki pendamping kuliner yang tidak hanya memberi kita resep untuk bahan-bahan yang kita miliki tetapi juga menghasilkan gambar resep yang sudah jadi, memperkirakan nilai gizi, membuat daftar belanja dengan perkiraan harga, dan merinci biaya per porsi.

Coba asisten dengan meminta resep dan memberikan daftar bahan yang Anda miliki atau sukai. Daftar 3.2 menunjukkan contoh permintaan sederhana dengan informasi tambahan untuk mengatur suasana hati. Tentu saja, Anda dapat menambahkan bahan atau situasi apa pun yang Anda suka dan kemudian melihat hasilnya.

### Daftar 3.2 Mendorong resep

```
Saya punya sekantong potongan ayam beku yang sudah disiapkan dan saya ingin membuat 
makan malam romantis untuk dua orang.
```

Gambar 3.4 menunjukkan hasil output yang diformat dari GPT yang disediakan oleh prompt. Ini tentu terlihat cukup enak untuk dimakan. Semua output ini dihasilkan karena instruksi yang kami berikan kepada agen. 

![Gambar 3.4](Images/3-4.png "Hasil output dari GPT Pendamping Kuliner")

*Gambar 3.4 Hasil output dari GPT Pendamping Kuliner*

Meskipun hasil outputnya terlihat bagus, mungkin tidak semuanya faktual dan benar, dan hasil Anda mungkin berbeda. Misalnya, GPT menambahkan potongan ayam ke daftar belanja padahal kami sudah menyarankan untuk memiliki bahan-bahan tersebut. Selain itu, harga dan perkiraan informasi nutrisi hanyalah perkiraan, tetapi ini dapat diselesaikan nanti jika Anda tertarik.

Namun, di luar kotak, Asisten GPT cukup mengesankan untuk membangun asisten atau agen bukti konsep dengan cepat. Seperti yang akan Anda lihat nanti di bab ini, ini juga menyediakan platform yang sangat baik untuk menggunakan asisten di luar ChatGPT. Di bagian selanjutnya, kita akan melihat fitur-fitur yang lebih mengesankan yang disediakan GPT, seperti unggahan file dan interpretasi kode.

## 3.2 Membangun GPT yang dapat melakukan ilmu data

Platform Asisten GPT telah dan kemungkinan akan diperluas untuk mencakup berbagai komponen agen. Saat ini, Asisten GPT mendukung apa yang disebut sebagai pengetahuan, memori, dan tindakan. Di bab 8, kita akan membahas detail pengetahuan dan memori, dan di bab 5, kita membahas konsep penggunaan alat melalui tindakan.

Dalam latihan kita berikutnya, kita akan membangun asisten untuk melakukan tinjauan ilmu data pass pertama dari setiap dokumen CSV yang kita berikan. Agen ini akan menggunakan kemampuan atau tindakan yang memungkinkan untuk pengkodean dan interpretasi kode. Saat Anda mengaktifkan interpretasi kode, asisten akan mengizinkan unggahan file secara default.

Namun, sebelum kita melakukannya, kita ingin merancang agen kita, dan cara apa yang lebih baik untuk melakukannya selain meminta LLM untuk membangunkan kita seorang asisten? Daftar 3.3 menunjukkan prompt yang meminta ChatGPT (GPT-4) untuk merancang asisten ilmu data. Perhatikan bagaimana kita tidak meminta semuanya dalam satu prompt tetapi malah mengulangi informasi yang dikembalikan oleh LLM.

### Daftar 3.3 Mendorong asisten ilmu data

```
PROMPT PERTAMA:    
apa eksperimen ilmu data dasar dan menarik yang bagus 
yang dapat Anda tugaskan kepada seseorang dengan satu 
file csv yang berisi data menarik?    #1
PROMPT KEDUA:    
oke, bisakah Anda sekarang menulis semua langkah itu ke dalam instruksi 
untuk digunakan untuk Agen GPT (agen LLM) untuk mereplikasi semua 
langkah di atas     #2

PROMPT KETIGA:    
Siapakah tokoh terkenal yang dapat mewujudkan agen 
ilmuwan data dan mampu menyajikan data kepada pengguna?     #3
```

- #1 Pertama, minta LLM untuk meletakkan fondasi.
- #2 Kemudian, minta LLM untuk mengubah langkah-langkah sebelumnya menjadi proses yang lebih formal.
- #3 Terakhir, minta LLM untuk memberikan kepribadian yang dapat mewakili proses tersebut.

Hasil dari percakapan itu memberikan instruksi asisten yang ditunjukkan pada daftar 3.4. Dalam hal ini, asisten itu bernama Data Scout, tetapi jangan ragu untuk menamai asisten Anda apa yang menarik bagi Anda. 

### Daftar 3.4 Instruksi Data Scout

```
GPT ini, bernama Data Scout, dirancang untuk membantu pengguna dengan menganalisis file CSV 
dan memberikan wawasan seperti Nate Silver, seorang ahli statistik terkenal yang dikenal 
karena pendekatannya yang mudah diakses dan menarik terhadap data. Data Scout menggabungkan 
analisis yang ketat dengan gaya komunikasi yang jelas dan mudah didekati, 
membuat wawasan data yang kompleks dapat dimengerti. Ini dilengkapi untuk menangani 
pengujian statistik, pemodelan prediktif, visualisasi data, dan banyak lagi, 
menawarkan saran untuk eksplorasi lebih lanjut berdasarkan bukti 
yang kuat berdasarkan data.

Data Scout mengharuskan pengguna untuk mengunggah file csv data yang ingin mereka 
analisis. Setelah pengguna mengunggah file, Anda akan melakukan tugas-tugas 
berikut:
Akuisisi Data
    Minta pengguna untuk mengunggah file csv data.
    Instruksi: Gunakan pustaka pandas untuk membaca data dari file CSV 
. Pastikan data dimuat dengan benar dengan menampilkan beberapa baris 
pertama menggunakan df.head().

2. Analisis Data Eksplorasi (EDA)
Pembersihan Data
    Tugas: Mengidentifikasi dan menangani nilai yang hilang, memperbaiki tipe data.
    Instruksi: Periksa nilai yang hilang menggunakan df.isnull().sum(). Untuk 
data kategorikal, pertimbangkan untuk mengisi nilai yang hilang dengan mode, dan untuk 
data numerik, gunakan median atau mean. Konversikan tipe data jika perlu 
menggunakan df.astype().

Visualisasi
    Tugas: Buat visualisasi untuk menjelajahi data.
    Instruksi: Gunakan matplotlib dan seaborn untuk membuat histogram, plot sebar, dan plot kotak. Misalnya, gunakan sns.histplot() untuk histogram dan 
sns.scatterplot() untuk plot sebar.

Statistik Deskriptif
    Tugas: Hitung ukuran statistik dasar.
    Instruksi: Gunakan df.describe() untuk mendapatkan ringkasan statistik dan 
df.mean(), df.median() untuk perhitungan spesifik.

3. Pengujian Hipotesis
    Tugas: Uji hipotesis yang dirumuskan berdasarkan kumpulan data.
    Instruksi: Tergantung pada jenis data, lakukan uji statistik 
seperti uji-t atau uji chi-kuadrat menggunakan scipy.stats. Misalnya, gunakan 
stats.ttest_ind() untuk uji-t antara dua kelompok.

4. Pemodelan Prediktif
Rekayasa Fitur
    Tugas: Tingkatkan kumpulan data dengan fitur-fitur baru.
    Instruksi: Buat kolom baru di DataFrame berdasarkan data yang ada 
untuk menangkap informasi atau hubungan tambahan. Gunakan operasi 
seperti df['fitur_baru'] = df['fitur1'] / df['fitur2'].

Pemilihan Model
    Tugas: Pilih dan konfigurasikan model pembelajaran mesin.
    Instruksi: Berdasarkan tugas (klasifikasi atau regresi), pilih 
model dari scikit-learn, seperti RandomForestClassifier() atau 
LinearRegression(). Konfigurasikan parameter model.

Pelatihan dan Pengujian
    Tugas: Bagi data menjadi set pelatihan dan pengujian, lalu latih model.
    Instruksi: Gunakan train_test_split dari scikit-learn untuk membagi 
data. Latih model menggunakan model.fit(X_train, y_train).

Evaluasi Model
    Tugas: Menilai kinerja model.
    Instruksi: Gunakan metrik seperti mean squared error (MSE) atau akurasi. 
Hitung ini menggunakan metrics.mean_squared_error(y_test, y_pred) atau 
metrics.accuracy_score(y_test, y_pred).

5. Wawasan dan Kesimpulan
    Tugas: Menafsirkan dan merangkum temuan dari analisis dan pemodelan.
    Instruksi: Diskusikan koefisien model atau pentingnya fitur. 
Buat kesimpulan tentang hipotesis dan analisis prediktif. Sarankan 
implikasi atau tindakan dunia nyata berdasarkan hasilnya.

6. Presentasi
    Tugas: Siapkan laporan atau presentasi.
    Instruksi: Rangkum proses dan temuan dalam format yang jelas dan 
mudah diakses, menggunakan plot dan poin-poin. Pastikan presentasi 
dapat dimengerti oleh pemangku kepentingan non-teknis.
```

Setelah membuat instruksi, Anda dapat menyalin dan menempelkannya ke panel Konfigurasi pada gambar 3.5. Pastikan untuk memberikan alat (keterampilan) Interpretasi Kode kepada asisten dengan memilih kotak centang yang sesuai. Anda tidak perlu mengunggah file di sini; asisten akan mengizinkan unggahan file saat kotak centang Interpretasi Kode diaktifkan.

![Gambar 3.5](Images/3-5.png "Menghidupkan alat/keterampilan Penerjemah Kode")

*Gambar 3.5 Menghidupkan alat/keterampilan Penerjemah Kode*

Sekarang, kita dapat menguji asisten dengan mengunggah file CSV dan mengajukan pertanyaan tentangnya. Folder kode sumber untuk bab ini berisi file bernama `netflix_titles.csv`; beberapa baris teratas dirangkum dalam daftar 3.5. Tentu saja, Anda dapat menggunakan file CSV apa pun yang Anda inginkan, tetapi latihan ini akan menggunakan contoh Netflix. Perhatikan bahwa kumpulan data ini diunduh dari Kaggle, tetapi Anda dapat menggunakan CSV lain jika Anda mau.

### Daftar 3.5 `netflix_titles.csv` (baris data teratas)

```
show_id,type,title,director,cast,country,date_added,
release_year,rating,duration,listed_in,description    #1
s1,Movie,Dick Johnson Is Dead,Kirsten Johnson,,
United States,"September 25, 2021",2020,PG-13,90 min,
Documentaries,"As her father nears the end of his life, 
filmmaker Kirsten Johnson stages his death in inventive 
and comical ways to help them both face the inevitable."    #2
```

- #1 Daftar kolom yang dipisahkan koma
- #2 Contoh baris data dari kumpulan data

Kita bisa mengunggah file dan meminta asisten untuk melakukan tugasnya, tetapi untuk latihan ini, kita akan lebih spesifik. Daftar 3.6 menunjukkan prompt dan mengunggah file untuk melibatkan asisten (termasuk `Netflix_titles.csv` dalam permintaan). Contoh ini memfilter hasil ke Kanada, tetapi Anda tentu saja dapat menggunakan negara mana pun yang ingin Anda lihat.

### Daftar 3.6 Mendorong Data Scout

```
Analisis CSV terlampir dan filter hasilnya ke 
negara Kanada dan keluarkan setiap penemuan signifikan 
dalam tren, dll.    #1
```

- #1 Anda dapat memilih negara yang berbeda untuk memfilter data.

Jika Anda mengalami masalah dengan asisten yang mengurai file, segarkan jendela browser Anda dan coba lagi. Tergantung pada data dan filter Anda, asisten sekarang akan menggunakan Penerjemah Kode seperti yang dilakukan oleh seorang ilmuwan data untuk menganalisis dan mengekstrak tren dalam data. 

Gambar 3.6 menunjukkan output yang dihasilkan untuk prompt pada daftar 3.5 menggunakan file `netflix_titles.csv` untuk data. Output Anda mungkin terlihat sangat berbeda jika Anda memilih negara yang berbeda atau meminta analisis lain.

![Gambar 3.6](Images/3-6.png "Output yang dihasilkan oleh asisten saat menganalisis data CSV")

*Gambar 3.6 Output yang dihasilkan oleh asisten saat menganalisis data CSV*

Plot ilmu data yang sedang dibangun oleh asisten dibuat dengan menulis dan menjalankan kode dengan Penerjemah Kode. Anda dapat mencoba ini dengan file CSV lain atau, jika Anda mau, berbagai bentuk data untuk dianalisis. Anda bahkan dapat terus melakukan iterasi dengan asisten untuk memperbarui plot secara visual atau menganalisis tren lain.

Interpretasi kode adalah keterampilan yang menarik yang kemungkinan akan Anda tambahkan ke banyak agen Anda untuk segala hal mulai dari perhitungan hingga pemformatan khusus. Di bagian selanjutnya, kita akan melihat cara memperluas kemampuan GPT melalui tindakan khusus.

## 3.3 Menyesuaikan GPT dan menambahkan tindakan khusus

Dalam latihan kita berikutnya, kita akan menunjukkan penggunaan tindakan khusus, yang dapat secara signifikan memperluas jangkauan asisten Anda. Menambahkan tindakan khusus ke agen memerlukan beberapa komponen, mulai dari memahami titik akhir spesifikasi OpenAPI hingga menghubungkan ke layanan. Oleh karena itu, sebelum kita menambahkan tindakan khusus, kita akan membangun GPT lain di bagian selanjutnya untuk membantu kita.

### 3.3.1 Membuat asisten untuk membangun asisten

Mengingat kemampuan GPT, masuk akal jika kita menggunakan salah satunya untuk membantu membangun yang lain. Di bagian ini, kita akan membangun GPT yang dapat membantu kita membuat layanan yang dapat kita hubungkan sebagai tindakan khusus ke GPT lain. Dan ya, kita bahkan akan menggunakan LLM untuk mulai membangun GPT pembantu kita.

Daftar berikut menunjukkan prompt untuk membuat instruksi untuk GPT pembantu kita. Prompt ini dimaksudkan untuk menghasilkan instruksi untuk asisten.

### Daftar 3.7 Mendorong desain pembantu (di Pembangun GPT atau ChatGPT)

```
Saya ingin membuat asisten GPT yang dapat menghasilkan layanan FastAPI yang 
akan melakukan beberapa tindakan untuk ditentukan. Sebagai bagian dari pembuatan kode 
FastAPI, saya ingin asisten menghasilkan spesifikasi OpenAPI untuk 
titik akhir. Harap uraikan serangkaian instruksi untuk agen ini.
```

Daftar 3.8 menunjukkan sebagian besar instruksi yang dihasilkan untuk prompt. Output tersebut kemudian dimodifikasi dan sedikit diperbarui dengan informasi spesifik dan detail lainnya. Salin dan tempel instruksi tersebut dari file (`assistant_builder.txt`) ke dalam GPT Anda. Pastikan untuk memilih kemampuan Penerjemah Kode juga.

### Daftar 3.8 Instruksi asisten tindakan khusus

```
GPT ini dirancang untuk membantu pengguna dalam menghasilkan layanan FastAPI yang 
disesuaikan dengan tindakan spesifik, lengkap dengan 
spesifikasi OpenAPI yang sesuai untuk titik akhir. Asisten akan memberikan cuplikan 
kode dan panduan tentang penataan dan pendokumentasian layanan API menggunakan FastAPI, 
memastikan bahwa layanan yang dihasilkan siap untuk integrasi dan 
penyebaran.

1.   Tentukan Tindakan dan Titik Akhir: Pertama, tentukan tindakan spesifik yang 
harus dilakukan oleh layanan FastAPI. Ini bisa berupa apa saja mulai dari mengambil 
data, memproses informasi, atau berinteraksi dengan API atau basis data lain.

2.    Rancang Titik Akhir API: Tentukan metode HTTP (GET, POST, PUT, 
DELETE, dll.) dan struktur URI titik akhir. Tentukan parameter input 
(parameter path, query, atau body) dan struktur respons yang diharapkan.

3. Hasilkan Kode FastAPI:
        Pengaturan FastAPI: Impor FastAPI dan pustaka lain yang diperlukan.
        Buat Fungsi API: Tulis fungsi Python yang melakukan 
tindakan yang diinginkan. Fungsi ini harus menerima parameter input yang ditentukan 
dan mengembalikan respons yang sesuai.
4. Hiasi Fungsi: Gunakan dekorator FastAPI (mis., 
@app.get("/endpoint")) untuk menautkan fungsi dengan titik akhir yang ditentukan 
dan metode HTTP.
        Tentukan Model Input dan Output: Gunakan model Pydantic untuk menentukan 
struktur data input dan output. Ini memastikan validasi dan 
serialisasi data.

5. Hasilkan Spesifikasi OpenAPI:
        FastAPI secara otomatis menghasilkan spesifikasi OpenAPI berdasarkan 
definisi titik akhir dan model Pydantic. Pastikan semua 
parameter fungsi dan model didokumentasikan dengan baik menggunakan docstring dan deskripsi 
field.
        Secara opsional, sesuaikan spesifikasi OpenAPI dengan menambahkan 
metadata, tag, atau respons tambahan langsung di dekorator FastAPI.

6. Penyebaran:
        Jelaskan kepada pengguna cara mempersiapkan aplikasi FastAPI untuk 
penyebaran. 
        Instruksikan mereka tentang cara menggunakan ngrok untuk menyebarkan 
layanan dan menyajikannya di mesin lokal pengguna.     #1
```

- #1 Ini menggunakan ngrok sebagai contoh untuk menyebarkan layanan secara lokal.

Setelah mempersiapkan asisten, pastikan semuanya diatur di panel Konfigurasi (termasuk menyetel kotak centang Penerjemah Kode), lalu segarkan jendela browser Anda. Ini akan mempersiapkan asisten untuk sesi baru. Anda dapat meminta jenis layanan yang ingin Anda bangun dari sini.

Daftar 3.9 menunjukkan permintaan ke Asisten Tindakan Kustom untuk membuat titik akhir tugas harian. Jika Anda memahami cara kerja API, Anda dapat menyarankan opsi lain, seperti `POST`. Tentu saja, Anda juga dapat meminta asisten untuk memandu Anda dan membuat layanan Anda.

### Daftar 3.9 Permintaan cepat layanan titik akhir tugas

```
Saya ingin mendefinisikan titik akhir GET yang membalas dengan daftar tugas harian saya
```

Setelah Anda memasukkan prompt, asisten akan menghasilkan kode dan instruksi untuk membuat dan menjalankan titik akhir FastAPI. Daftar berikut menunjukkan contoh kode yang dihasilkan dari permintaan sebelumnya.

### Daftar 3.10 `daily_tasks_api.py` (dihasilkan dari asisten)

```
dari fastapi impor FastAPI
dari pydantic impor BaseModel
dari mengetik impor Daftar

app = FastAPI()

kelas Tugas(BaseModel):   #1
    id: int
    deskripsi: str
    selesai: bool

tugas = [    #2
    Tugas(id=1, deskripsi="Beli bahan makanan", selesai=Salah),
    Tugas(id=2, deskripsi="Baca buku", selesai=Benar),
    Tugas(id=3, deskripsi="Selesaikan proyek FastAPI", selesai=Salah),
]

@app.get("/tasks", response_model=List[Task])   #3
async def get_tasks():
    """
    Ambil daftar tugas harian.
    """
    kembalikan tugas
```

- #1 Gunakan Pydantic untuk membuat tipe untuk tugas tersebut.
- #2 Ini adalah daftar tugas statis untuk didemonstrasikan.
- #3 Titik akhir tugas

Masukkan kode ke dalam Visual Studio Code (VS Code), dan konfirmasikan bahwa `fastapi` dan `uvicorn` diinstal dengan `pip`. Kemudian, jalankan API menggunakan perintah yang ditunjukkan pada daftar berikut, yang menjalankan API di file sumber bab.

### Daftar 3.11 Menjalankan API

```
uvicorn daily_tasks_api:app –reload     #1
```

- #1 Ubah nama modul/file jika Anda menggunakan sesuatu yang berbeda.

Buka browser ke http://127.0.0.1:8000/docs, lokasi default untuk titik akhir Swagger, seperti yang ditunjukkan pada gambar 3.7.

![Gambar 3.7](Images/3-7.png "Menavigasi dokumen Swagger dan mendapatkan dokumen openapi.json")

*Gambar 3.7 Menavigasi dokumen Swagger dan mendapatkan dokumen openapi.json*

Mengklik tautan `/openapi.json` akan menampilkan spesifikasi OpenAPI untuk titik akhir, seperti yang ditunjukkan pada daftar 3.12 (JSON dikonversi ke YAML). Anda harus menyalin dan menyimpan dokumen ini untuk digunakan nanti saat menyiapkan tindakan khusus pada agen. Titik akhir menghasilkan JSON, tetapi Anda juga dapat menggunakan spesifikasi yang ditulis dalam YAML.

### Daftar 3.12 Spesifikasi OpenAPI untuk API tugas 

```
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
paths:
  /tasks:
    get:
      summary: Dapatkan Tugas
      description: Ambil daftar tugas harian.
      operationId: get_tasks_tasks_get
      responses:
        '200':
          description: Respons Berhasil
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Task'
                title: Respons Dapatkan Tugas Tugas Dapatkan
components:
  schemas:
    Task:
      type: object
      properties:
        id:
          type: integer
          title: Id
        description:
          type: string
          title: Deskripsi
        completed:
          type: boolean
          title: Selesai
      required:
        - id
        - description
        - completed
      title: Task
```

Sebelum menghubungkan asisten ke layanan, Anda harus menyiapkan dan menggunakan ngrok untuk membuka terowongan ke mesin lokal Anda yang menjalankan layanan. Minta GPT untuk memberikan instruksi dan membantu Anda menyiapkan ngrok, dan jalankan aplikasi untuk membuka titik akhir ke port 8000 di mesin Anda, seperti yang ditunjukkan pada daftar 3.13. Jika Anda mengubah port atau menggunakan konfigurasi yang berbeda, Anda harus memperbaruinya.

### Daftar 3.13 Menjalankan ngrok (mengikuti pengaturan instruksi)

```
./ngrok authtoken <TOKEN_AUTH_ANDA>     #1
./ngrok http 8000     #2
```

- #1 Masukkan token otentikasi Anda yang diperoleh dari ngrok.com.
- #2 Membuka terowongan di port 8000 ke lalu lintas internet eksternal

Setelah Anda menjalankan ngrok, Anda akan melihat URL eksternal yang sekarang dapat Anda gunakan untuk mengakses layanan di mesin Anda. Salin URL ini untuk digunakan nanti saat menyiapkan asisten. Di bagian selanjutnya, kita akan membuat asisten yang menggunakan layanan ini sebagai tindakan khusus.

### 3.3.2 Menghubungkan tindakan khusus ke asisten

Dengan layanan yang aktif dan berjalan di mesin Anda dan dapat diakses secara eksternal melalui terowongan ngrok, kita dapat membangun asisten baru. Kali ini, kita akan membuat asisten sederhana untuk membantu kita mengatur tugas harian kita, di mana tugas-tugas tersebut akan dapat diakses dari layanan tugas yang berjalan secara lokal.

Buka antarmuka GPT dan panel Konfigurasi, lalu salin dan tempel instruksi yang ditunjukkan pada daftar 3.14 ke asisten baru. Pastikan untuk memberi nama asisten dan memasukkan deskripsi yang bermanfaat juga. Selain itu, aktifkan kemampuan Penerjemah Kode untuk memungkinkan asisten membuat plot akhir, yang menunjukkan tugas-tugas tersebut.

### Daftar 3.14 Pengatur Tugas (`task_organizer_assistant.txt`)

```
Task Organizer dirancang untuk membantu pengguna memprioritaskan tugas harian mereka 
berdasarkan urgensi dan ketersediaan waktu, memberikan panduan terstruktur tentang 
cara mengkategorikan tugas berdasarkan urgensi dan menyarankan blok waktu yang optimal untuk 
menyelesaikan tugas-tugas ini. Ini mengadopsi persona yang terinspirasi oleh Tim Ferriss, yang dikenal 
karena fokusnya pada produktivitas dan efisiensi. Ini menggunakan bahasa yang jelas dan langsung 
dan menghindari membuat asumsi tentang waktu luang pengguna.
Ketika Anda selesai mengatur tugas, buat plot 
yang menunjukkan kapan dan bagaimana tugas akan diselesaikan.     #1
```

- #1 Fitur ini memerlukan Penerjemah Kode untuk diaktifkan.

Klik tombol Buat Tindakan Baru di bagian bawah panel. Gambar 3.8 menunjukkan antarmuka untuk menambahkan tindakan khusus. Anda harus menyalin dan menempelkan spesifikasi OpenAPI untuk layanan Anda ke dalam jendela. Kemudian, Anda harus menambahkan bagian baru yang disebut `server` dan mengisinya dengan URL Anda, seperti yang ditunjukkan pada gambar.

![Gambar 3.8](Images/3-8.png "Menambahkan tindakan kustom baru")

*Gambar 3.8 Menambahkan tindakan kustom baru*

Setelah spesifikasi diatur, Anda dapat mengujinya dengan mengklik tombol Uji. Ini akan menjalankan pengujian, dan Anda akan melihat hasilnya ditampilkan di jendela percakapan, seperti yang ditunjukkan pada gambar 3.9.

![Gambar 3.9](Images/3-9.png "Menguji titik akhir layanan API dikonfigurasi dengan benar sebagai tindakan khusus")

*Gambar 3.9 Menguji titik akhir layanan API dikonfigurasi dengan benar sebagai tindakan khusus*

Setelah Anda puas, semuanya sudah diatur. Segarkan jendela browser Anda untuk mengatur ulang sesi, dan masukkan sesuatu seperti prompt yang ditunjukkan pada daftar 3.15. Ini akan meminta agen untuk memanggil layanan untuk mendapatkan tugas harian Anda, merangkum output, dan menyelesaikan dilema organisasi tugas Anda.

### Daftar 3.15 Prompt Pengatur Tugas

```
bagaimana saya harus mengatur tugas saya untuk hari ini?
```

Asisten harus menghasilkan plot jadwal tugas di akhir. Jika salah atau formatnya tidak sesuai dengan keinginan Anda, Anda dapat menambahkan instruksi untuk menentukan format/gaya yang harus dikeluarkan oleh asisten.

Anda dapat meningkatkan layanan, tetapi jika Anda membuat perubahan apa pun pada API, spesifikasi dalam tindakan khusus asisten perlu diperbarui. Dari sini, Anda dapat menambahkan layanan tindakan khusus yang dijalankan dari komputer Anda atau dihosting sebagai layanan.

> **Catatan** Sadarilah bahwa pengguna yang tidak dikenal dapat mengaktifkan tindakan khusus jika Anda menerbitkan asisten untuk konsumsi publik, jadi jangan mengekspos layanan yang membebankan biaya layanan kepada Anda atau mengakses informasi pribadi kecuali itu adalah niat Anda. Demikian juga, layanan yang dibuka melalui terowongan ngrok akan diekspos melalui asisten, yang mungkin menjadi perhatian. Harap berhati-hati saat menerbitkan agen yang menggunakan tindakan khusus.

Tindakan khusus adalah cara yang bagus untuk menambahkan fungsionalitas dinamis ke asisten, baik untuk penggunaan pribadi maupun komersial. Unggahan file adalah opsi yang lebih baik untuk memberikan pengetahuan statis kepada asisten. Bagian selanjutnya akan membahas penggunaan unggahan file untuk memperluas pengetahuan asisten.

## 3.4 Memperluas pengetahuan asisten menggunakan unggahan file

Jika Anda pernah terlibat dengan LLM, Anda mungkin pernah mendengar tentang pola generasi yang ditambah dengan pengambilan (RAG). Bab 8 akan membahas RAG secara rinci untuk penerapan pengetahuan dan memori. Pengetahuan terperinci tentang RAG tidak diperlukan untuk menggunakan kemampuan unggah file, tetapi jika Anda memerlukan beberapa dasar, lihat bab itu.

Platform Asisten GPT menyediakan kemampuan pengetahuan yang disebut *unggahan file*, yang memungkinkan Anda mengisi GPT dengan basis pengetahuan statis tentang apa pun dalam berbagai format. Pada saat penulisan, platform Asisten GPT memungkinkan Anda mengunggah hingga 512 MB dokumen. Dalam dua latihan berikutnya, kita akan melihat dua GPT berbeda yang dirancang untuk membantu pengguna dalam mengonsumsi buku.

### 3.4.1 Membangun GPT Kalkulus Menjadi Mudah

Buku dan pengetahuan tertulis akan selalu menjadi tulang punggung basis pengetahuan kita. Tetapi membaca teks adalah upaya sungguh-sungguh penuh waktu yang tidak dimiliki banyak orang. Buku audio membuat konsumsi buku dapat diakses kembali; Anda dapat mendengarkan sambil melakukan banyak tugas, tetapi tidak semua buku bertransisi dengan baik ke audio.

Masuki dunia AI dan asisten cerdas. Dengan GPT, kita dapat menciptakan pengalaman interaktif antara pembaca dan buku. Pembaca tidak lagi dipaksa untuk mengonsumsi buku halaman demi halaman tetapi secara keseluruhan.

Untuk mendemonstrasikan konsep ini, kita akan membangun GPT berdasarkan teks matematika klasik berjudul *Calculus Made Easy*, oleh Silvanus P. Thompson. Buku ini tersedia secara gratis melalui situs web Gutenberg Press. Meskipun usianya lebih dari seratus tahun, buku ini masih memberikan latar belakang materi yang solid.

> **Catatan** Jika Anda serius ingin belajar kalkulus tetapi asisten ini masih terlalu mahir, lihat buku bagus karya Clifford A. Pickover berjudul *Calculus and Pizza*. Ini adalah buku yang bagus untuk belajar kalkulus atau hanya untuk penyegaran yang sangat baik. Anda juga bisa mencoba membuat asisten Kalkulus dan Pizza Anda sendiri jika Anda memiliki versi eBook. Sayangnya, undang-undang hak cipta akan mencegah Anda menerbitkan GPT ini tanpa izin.

Buka ChatGPT, buka GPT Saya, buat GPT baru, klik tab Konfigurasi, lalu unggah file, seperti yang ditunjukkan pada gambar 3.10. Unggah buku dari folder kode sumber bab: `bab _03/calculus_made_easy.pdf`. Ini akan menambahkan buku ke pengetahuan GPT.

![Gambar 3.10](Images/3-10.png "Menambahkan file ke pengetahuan asisten")

*Gambar 3.10 Menambahkan file ke pengetahuan asisten*

Gulir ke atas dan tambahkan instruksi yang ditunjukkan pada daftar 3.16. Teks pembukaan awal dibuat dengan bercakap-cakap dengan Pembangun GPT. Setelah memperbarui teks pembukaan, kepribadian ditambahkan dengan menanyakan ChatGPT tentang matematikawan terkenal. Kemudian, akhirnya, aturan ditambahkan untuk memberikan panduan tambahan kepada GPT tentang hasil eksplisit apa yang kita inginkan.

### Daftar 3.16 Instruksi untuk GPT Kalkulus Menjadi Mudah

```
GPT ini dirancang untuk menjadi guru dan mentor ahli 
kalkulus berdasarkan buku 'Calculus Made Easy' oleh 
Silvanus Thompson. Salinan buku diunggah di 
calculus_made_easy.pdf dan memberikan panduan terperinci 
dan penjelasan tentang berbagai topik kalkulus seperti 
turunan, integral, limit, dan banyak lagi. GPT dapat 
mengajarkan konsep kalkulus, memecahkan masalah, dan menjawab 
pertanyaan yang berkaitan dengan kalkulus, membuat topik yang kompleks 
dapat diakses dan dimengerti. Ini dapat menangani 
pertanyaan terkait kalkulus, dari dasar hingga mahir, 
dan sangat berguna bagi siswa dan pendidik
 yang ingin memperdalam pemahaman mereka tentang kalkulus.     #1
Jawab sebagai matematikawan terkenal Terence Tao. 
Terence Tao terkenal karena kecerdasan briliannya, 
kemudahan didekati, dan kemampuan luar biasa untuk secara efektif
 menyederhanakan dan mengkomunikasikan konsep matematika yang kompleks.    #2

ATURAN    #3
1) Selalu ajarkan konsep seolah-olah Anda sedang mengajar anak kecil.
2) Selalu tunjukkan konsep dengan menunjukkan plot fungsi dan grafik.
3) Selalu tanyakan apakah pengguna ingin mencoba soal contoh sendiri. 
Beri mereka soal yang setara dengan konsep pertanyaan yang sedang Anda diskusikan.
```

- #1 Pembukaan awalnya dibuat oleh Pembangun dan kemudian diubah sesuai kebutuhan.
- #2 Pastikan untuk selalu memberikan persona/kepribadian yang sesuai kepada asisten dan agen Anda.
- #3 Mendefinisikan kondisi dan aturan eksplisit dapat membantu memandu GPT dengan lebih baik sesuai keinginan Anda.

Setelah memperbarui asisten, Anda dapat mencobanya di jendela pratinjau atau versi buku dengan mencari Calculus Made Easy di GPT Store. Gambar 3.11 menunjukkan contoh potongan interaksi dengan GPT. Gambar tersebut menunjukkan bahwa GPT dapat menghasilkan plot untuk mendemonstrasikan konsep atau mengajukan pertanyaan.

![Gambar 3.11](Images/3-11.png "Output dari meminta GPT untuk mengajar kalkulus")

*Gambar 3.11 Output dari meminta GPT untuk mengajar kalkulus*

GPT ini menunjukkan kemampuan seorang asisten untuk menggunakan buku sebagai referensi pengajaran pendamping. Hanya satu buku yang diunggah dalam latihan ini, tetapi beberapa buku atau dokumen lain dapat diunggah. Seiring dengan matangnya fitur ini dan teknologinya, di masa depan, mungkin saja seluruh mata kuliah dapat diajarkan menggunakan GPT.

Kita akan beralih dari teknis dan merangkul fiksi untuk mendemonstrasikan penggunaan pengetahuan. Di bagian selanjutnya, kita akan melihat bagaimana pengetahuan tentang unggahan file dapat digunakan untuk pencarian dan referensi.

### 3.4.2 Pencarian pengetahuan dan lebih banyak lagi dengan unggahan file

Kemampuan unggah file platform Asisten GPT mendukung unggahan hingga 512 MB untuk satu asisten. Fitur ini saja menyediakan kemampuan yang kuat untuk pencarian dokumen dan aplikasi lain dalam ukuran bisnis/proyek pribadi dan kecil hingga menengah. 

Bayangkan mengunggah seluruh koleksi file. Anda sekarang dapat mencari, membandingkan, membedakan, mengatur, dan menyusun semuanya dengan satu asisten. Fitur ini saja di dalam Asisten GPT akan mengganggu cara kita mencari dan menganalisis dokumen. Di bab 6, kita akan memeriksa bagaimana akses langsung ke API Asisten OpenAI dapat meningkatkan jumlah dokumen.

Untuk latihan berikutnya, kita akan menggunakan asisten dengan pengetahuan tentang banyak buku atau dokumen. Teknik ini dapat diterapkan pada dokumen apa pun yang didukung, tetapi asisten ini akan menggunakan teks klasik tentang robot. Kita akan menamai asisten ini GPT Bacaan Robot Klasik.

Mulai dengan membuat asisten GPT baru di antarmuka ChatGPT. Kemudian, unggah instruksi di daftar 3.17, dan beri nama serta deskripsikan asisten. Instruksi ini dibuat sebagian melalui Pembangun GPT dan kemudian diedit. 

### Daftar 3.17 Instruksi Bacaan Robot Klasik

```
GPT ini, Bacaan Robot Klasik dan menggunakan persona 
Isaac Asimov dan akan menjawab sebagai penulis robot terkenal.    #1
GPT ini hanya akan merujuk dan membahas buku-buku 
di basis pengetahuannya dari file yang diunggah.                  #2
Itu tidak menyebutkan atau membahas buku atau teks lain yang 
tidak ada dalam basis pengetahuannya.                        #2

ATURAN
Merujuk hanya pada teks dalam basis pengetahuan Anda         #2    
Selalu berikan 3 contoh dari setiap permintaan yang diajukan penggunaan    #3
Selalu tanyakan kepada pengguna apakah mereka memerlukan sesuatu lebih lanjut     #4
```

- #1 Ingatlah untuk selalu memberikan persona/kepribadian pada GPT Anda.
- #2 Pastikan asisten hanya merujuk pada pengetahuan dalam unggahan file.
- #3 Tambahkan beberapa aturan ekstra untuk pilihan gaya.
- #4 Jadikan asisten lebih membantu dengan juga memberi mereka nuansa dan gaya.

Setelah menyelesaikan langkah-langkah tersebut, Anda dapat mengunggah file dari sumber bab yang disebut `gutenberg_robot_books`. Gambar 3.12 menunjukkan pengunggahan beberapa file sekaligus. Jumlah maksimum file yang dapat Anda unggah sekaligus akan bervariasi sesuai dengan ukuran file. 

![Gambar 3.12](Images/3-12.png "Mengunggah dokumen ke pengetahuan asisten")

*Gambar 3.12 Mengunggah dokumen ke pengetahuan asisten*

Anda dapat mulai menggunakannya setelah mengunggah dokumen, mengatur instruksi, dan memberi nama dan gambar pada asisten. Pencarian adalah aplikasi paling dasar dari asisten pengetahuan, dan kasus penggunaan lain dalam bentuk prompt ditunjukkan pada tabel 3.1.

| Kasus penggunaan | Contoh prompt | Hasil |
|----------|----------------|---------|
| Cari | Cari frasa ini dalam pengetahuan Anda: "pelayan robot." | Mengembalikan dokumen dan kutipan |
| Bandingkan | Identifikasi tiga buku paling mirip yang memiliki gaya penulisan yang sama. | Mengembalikan tiga dokumen yang paling mirip |
| Kontras | Identifikasi tiga buku yang paling berbeda. | Mengembalikan buku-buku dalam koleksi yang paling berbeda |
| Urutan | Urutan apa yang harus saya baca buku-bukunya? | Mengembalikan urutan buku yang berurutan |
| Klasifikasi | Manakah dari buku-buku ini yang paling modern? | Mengklasifikasikan dokumen |
| Generasi | Hasilkan paragraf fiksi yang meniru pengetahuan Anda tentang pelayan robot. | Menghasilkan konten baru berdasarkan basis pengetahuannya |

Kasus penggunaan ini hanyalah contoh dari banyak hal yang mungkin dilakukan dengan asisten pengetahuan AI. Meskipun fitur ini mungkin tidak siap untuk mengganggu pencarian perusahaan, fitur ini memberi organisasi dan individu yang lebih kecil lebih banyak akses ke dokumen mereka. Ini memungkinkan pembuatan asisten sebagai bentuk pengetahuan yang dapat diekspos secara publik. Di bagian selanjutnya, kita akan melihat cara membuat asisten dapat dikonsumsi oleh semua orang.

## 3.5 Menerbitkan GPT Anda

Setelah Anda puas dengan GPT Anda, Anda dapat menggunakannya atau membagikannya dengan orang lain dengan memberikan tautan. Mengkonsumsi asisten GPT melalui ChatGPT saat ini memerlukan langganan Plus. Untuk mempublikasikan GPT Anda untuk orang lain, klik tombol Bagikan, dan pilih opsi berbagi Anda, seperti yang ditunjukkan pada gambar 3.13.

![Gambar 3.13](Images/3-13.png "Opsi berbagi GPT")

*Gambar 3.13 Opsi berbagi GPT*

Baik Anda membagikan GPT Anda dengan teman dan kolega atau secara publik di Toko GPT, penggunaan asisten diambil dari akun yang menggunakannya, bukan penerbit. Ini berarti jika Anda memiliki GPT yang sangat mahal yang menghasilkan banyak gambar, misalnya, itu tidak akan memengaruhi akun Anda saat orang lain menggunakannya.

### 3.5.1 Asisten GPT yang Mahal

Pada saat penulisan, OpenAI melacak penggunaan sumber daya akun ChatGPT Anda, termasuk yang digunakan untuk GPT. Jika Anda mencapai batas penggunaan sumber daya dan diblokir, akun ChatGPT Anda juga akan diblokir. Pemblokiran biasanya hanya berlangsung beberapa jam, tetapi ini tentu saja bisa lebih dari sedikit mengganggu.

Oleh karena itu, kami ingin memastikan bahwa pengguna yang menggunakan GPT Anda tidak melebihi batas penggunaan sumber daya mereka untuk penggunaan reguler. Berikut adalah daftar fitur yang meningkatkan penggunaan sumber daya saat menggunakan GPT:

- *Membuat gambar* —Pembuatan gambar masih merupakan layanan premium, dan pembuatan gambar berturut-turut dapat dengan cepat membuat pengguna Anda diblokir. Umumnya disarankan agar Anda memberi tahu pengguna Anda tentang potensi risiko dan/atau mencoba mengurangi seberapa sering gambar dibuat. 
- *Interpretasi kode* —Fitur ini memungkinkan pengunggahan file dan menjalankan kode untuk analisis data. Jika Anda pikir pengguna Anda akan memerlukan penggunaan alat pengkodean secara konstan, maka beri tahu mereka tentang risikonya. 
- *Visi, mendeskripsikan gambar* —Jika Anda membangun asisten yang menggunakan visi untuk mendeskripsikan dan mengekstrak informasi dari gambar, rencanakan untuk menggunakannya dengan hemat. 
- *Unggahan file* —Jika GPT Anda menggunakan banyak file atau memungkinkan Anda mengunggah beberapa file, ini dapat menyebabkan pemblokiran. Seperti biasa, arahkan pengguna menjauh dari apa pun yang mencegah mereka menikmati GPT Anda. 

> **Catatan** Hukum Moore menyatakan bahwa komputer akan berlipat ganda kekuatannya setiap dua tahun dengan biaya setengahnya. LLM sekarang berlipat ganda kekuatannya sekitar setiap enam bulan dari optimisasi dan peningkatan daya GPU. Ini, dikombinasikan dengan biaya yang dikurangi setidaknya setengahnya dalam periode yang sama, kemungkinan berarti batas sumber daya saat ini pada model visi dan pembuatan gambar tidak akan dipertimbangkan. Namun, layanan seperti interpretasi kode dan unggahan file kemungkinan akan tetap sama.

Membuat asisten Anda sadar akan penggunaan sumber daya bisa sesederhana menambahkan aturan yang ditunjukkan pada daftar 3.18 ke instruksi asisten. Instruksi bisa hanya berupa pernyataan yang menyampaikan peringatan kepada pengguna dan membuat asisten sadar. Anda bahkan bisa meminta asisten untuk membatasi penggunaan fitur-fitur tertentu.

### Daftar 3.18 Contoh aturan penggunaan sumber daya

```
ATURAN:
Saat membuat gambar, pastikan pengguna sadar bahwa membuat banyak 
gambar dengan cepat dapat memblokir sementara akun mereka.
```

Membimbing asisten Anda untuk lebih sadar sumber daya pada akhirnya membuat asisten Anda lebih dapat digunakan. Ini juga membantu mencegah pengguna yang marah yang tanpa sadar diblokir menggunakan asisten Anda. Ini mungkin penting jika Anda berencana merilis GPT Anda, tetapi sebelum itu, mari kita selidiki ekonominya di bagian selanjutnya.

### 3.5.2 Memahami ekonomi GPT

Setelah perilisan Asisten GPT dan Toko GPT, OpenAI mengumumkan potensi program bagi hasil di masa depan bagi mereka yang menerbitkan GPT. Meskipun kami masih menunggu untuk mendengar lebih banyak tentang program ini, banyak yang berspekulasi seperti apa program ini nantinya.

Beberapa orang menyarankan toko tersebut mungkin hanya mengembalikan 10% hingga 20% dari keuntungan kepada para pembangun. Ini jauh lebih kecil dari persentase di platform aplikasi lain tetapi membutuhkan pengetahuan teknis dan sumber daya yang jauh lebih sedikit. Toko GPT dibanjiri dengan asisten yang pada dasarnya gratis, asalkan Anda memiliki langganan Plus, tetapi itu mungkin berubah di masa depan. Terlepas dari itu, ada juga beberapa alasan mengapa Anda mungkin ingin membangun GPT publik:

- *Portofolio pribadi* —Mungkin Anda ingin menunjukkan pengetahuan Anda tentang rekayasa prompt atau kemampuan Anda untuk membangun gelombang aplikasi AI berikutnya. Memiliki beberapa GPT di Toko GPT dapat membantu menunjukkan pengetahuan dan kemampuan Anda untuk membuat aplikasi AI yang bermanfaat. 
- *Pengetahuan dan pengalaman* —Jika Anda memiliki pengetahuan mendalam tentang suatu subjek atau topik, ini bisa menjadi cara yang bagus untuk mengemasnya sebagai asisten. Jenis asisten ini akan bervariasi popularitasnya berdasarkan bidang keahlian Anda. 
- *Pemasaran silang dan ikatan komersial* —Ini menjadi lebih umum di Toko dan memberi perusahaan kemampuan untuk memimpin pelanggan menggunakan asisten. Seiring perusahaan mengintegrasikan lebih banyak AI, ini pasti akan lebih umum. 
- *Asisten yang membantu untuk produk/layanan Anda* —Tidak semua perusahaan atau organisasi dapat menanggung biaya hosting chatbot. Meskipun mengkonsumsi asisten saat ini terbatas pada pelanggan ChatGPT, mereka kemungkinan akan lebih mudah diakses di masa depan. Ini mungkin berarti memiliki GPT untuk semuanya, mungkin seperti masa-masa awal internet di mana setiap perusahaan bergegas membangun kehadiran web. 

Sementara bentuk Toko GPT saat ini adalah untuk pelanggan ChatGPT, jika tren saat ini dengan OpenAI berlanjut, kita kemungkinan akan melihat Toko GPT yang sepenuhnya publik. GPT publik berpotensi mengganggu cara kita mencari, menyelidiki produk dan layanan, dan mengonsumsi internet. Di bagian terakhir bab ini, kita akan memeriksa cara menerbitkan GPT dan beberapa pertimbangan penting.

### 3.5.3 Merilis GPT

Oke, Anda puas dengan GPT Anda dan cara kerjanya, dan Anda melihat manfaat nyata dari memberikannya kepada orang lain. Menerbitkan GPT untuk konsumsi publik (pelanggan) mudah, seperti yang ditunjukkan pada gambar 3.14. Setelah memilih Toko GPT sebagai opsi dan mengklik Simpan, Anda sekarang akan memiliki opsi untuk mengatur kategori dan memberikan tautan kembali kepada Anda.

![Gambar 3.14](Images/3-14.png "Memilih opsi setelah mengklik Simpan untuk menerbitkan ke Toko GPT")

*Gambar 3.14 Memilih opsi setelah mengklik Simpan untuk menerbitkan ke Toko GPT*

Itu mudah, jadi berikut adalah beberapa hal lagi yang ingin Anda pertimbangkan sebelum menerbitkan GPT Anda:

- *Deskripsi GPT* —Buat deskripsi yang bagus, dan Anda bahkan mungkin ingin meminta ChatGPT untuk membantu Anda membangun deskripsi yang meningkatkan optimisasi mesin pencari (SEO) GPT Anda. GPT sekarang muncul di pencarian Google, jadi optimisasi mesin pencari yang baik dapat membantu meningkatkan paparan asisten Anda. Deskripsi yang baik juga akan membantu pengguna memutuskan apakah mereka ingin meluangkan waktu untuk menggunakan asisten Anda. 
- *Logo* —Logo yang bagus dan bersih yang mengidentifikasi apa yang dilakukan asisten Anda tentu dapat membantu. Desain logo untuk GPT pada dasarnya adalah layanan gratis, tetapi meluangkan waktu untuk mengulangi beberapa gambar dapat membantu menarik pengguna ke asisten Anda. 
- *Kategori* —Secara default, kategori akan sudah dipilih, tetapi pastikan itu sesuai dengan asisten Anda. Jika Anda merasa tidak cocok, ubah kategorinya, dan Anda bahkan mungkin ingin memilih Lainnya dan menentukan kategori Anda sendiri. 
- *Tautan* —Pastikan untuk mengatur tautan referensi untuk media sosial Anda dan mungkin bahkan repositori GitHub yang Anda gunakan untuk melacak masalah untuk GPT. Menambahkan tautan ke GPT Anda menunjukkan kepada pengguna bahwa mereka dapat menghubungi pembuatnya jika mereka mengalami masalah atau memiliki pertanyaan. 

Persyaratan lebih lanjut kemungkinan akan muncul seiring dengan matangnya Toko GPT. Model bisnisnya masih harus ditetapkan, dan pembelajaran lain kemungkinan akan menyusul. Baik Anda memutuskan untuk membangun GPT untuk diri sendiri atau orang lain, melakukannya dapat membantu meningkatkan pemahaman Anda tentang cara membangun agen dan asisten. Seperti yang akan kita lihat di sisa buku ini, asisten GPT adalah fondasi yang berguna untuk pengetahuan Anda.

## 3.6 Latihan

Selesaikan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- *Latihan 1* —Bangun Asisten GPT Pertama Anda 

  *Tujuan* —Buat asisten GPT sederhana menggunakan antarmuka ChatGPT.

  *Tugas:*

  - Daftar untuk langganan ChatGPT Plus jika Anda belum memilikinya. 
  - Arahkan ke platform Asisten GPT, dan klik tombol Buat. 
  - Ikuti antarmuka obrolan Pembangun untuk membuat asisten Pendamping Kuliner yang memberikan saran makanan berdasarkan bahan yang tersedia. 
  - Konfigurasikan asisten secara manual untuk menambahkan aturan khusus untuk pembuatan resep, seperti menyertakan informasi nutrisi dan perkiraan biaya. 

- *Latihan 2* —Asisten Analisis Data 

  *Tujuan* —Kembangkan asisten GPT yang dapat menganalisis file CSV dan memberikan wawasan.

  *Tugas:*

  - Rancang asisten ilmu data yang dapat memuat dan menganalisis file CSV, mirip dengan contoh Data Scout di bab ini. 
  - Aktifkan alat Interpretasi Kode, dan unggah file CSV sampel (mis., kumpulan data dari Kaggle). 
  - Gunakan asisten untuk melakukan tugas-tugas seperti pembersihan data, visualisasi, dan pengujian hipotesis. 
  - Dokumentasikan proses dan temuan Anda, catat setiap tantangan atau perbaikan yang diperlukan. 

- *Latihan 3* —Buat Tindakan Kustom 

  *Tujuan* —Perluas asisten GPT dengan tindakan khusus menggunakan layanan FastAPI.

  *Tugas:*

  - Ikuti langkah-langkah untuk membuat layanan FastAPI yang menyediakan fungsi tertentu, seperti mengambil daftar tugas harian. 
  - Hasilkan spesifikasi OpenAPI untuk layanan tersebut, dan terapkan secara lokal menggunakan ngrok. 
  - Konfigurasikan asisten baru untuk menggunakan tindakan khusus ini, pastikan asisten terhubung dengan benar ke titik akhir FastAPI. 
  - Uji asisten dengan memintanya untuk melakukan tindakan dan memverifikasi output. 

- *Latihan 4* —Asisten Pengetahuan Unggahan File 

  *Tujuan* —Bangun asisten dengan pengetahuan khusus dari dokumen yang diunggah.

  *Tugas:*

  - Pilih e-book yang tersedia secara gratis atau kumpulan dokumen yang terkait dengan topik tertentu (mis., sastra klasik, manual teknis). 
  - Unggah file-file ini ke asisten GPT baru, dan konfigurasikan asisten untuk bertindak sebagai ahli pada konten yang diunggah. 
  - Buat serangkaian prompt untuk menguji kemampuan asisten untuk merujuk dan merangkum informasi dari dokumen. 
  - Evaluasi kinerja asisten, dan buat penyesuaian yang diperlukan untuk meningkatkan akurasi dan kegunaannya. 

- *Latihan 5* —Publikasikan dan Bagikan Asisten Anda 

  *Tujuan* —Publikasikan asisten GPT Anda ke Toko GPT dan bagikan dengan orang lain.

  *Tugas:*

  - Selesaikan konfigurasi dan pengujian asisten Anda untuk memastikannya berfungsi sebagaimana mestinya. 
  - Tulis deskripsi yang menarik, dan buat logo yang sesuai untuk asisten Anda. 
  - Pilih kategori yang benar, dan siapkan tautan yang diperlukan ke media sosial atau repositori GitHub Anda. 
  - Publikasikan asisten ke Toko GPT, dan bagikan tautannya dengan teman atau kolega. 
  - Kumpulkan umpan balik dari pengguna, dan sempurnakan asisten berdasarkan masukan mereka untuk meningkatkan kegunaan dan fungsionalitasnya. 

## Ringkasan

- Platform Asisten GPT OpenAI memungkinkan pembangunan dan penyebaran agen AI melalui UI ChatGPT, dengan fokus pada pembuatan asisten yang menarik dan fungsional. 
- Anda dapat menggunakan kemampuan interpretasi kode GPT untuk melakukan analisis data pada file CSV yang diunggah pengguna, memungkinkan asisten berfungsi sebagai ilmuwan data. 
- Asisten dapat diperluas dengan tindakan khusus, memungkinkan integrasi dengan layanan eksternal melalui titik akhir API. Ini termasuk menghasilkan layanan FastAPI dan spesifikasi OpenAPI yang sesuai. 
- Asisten dapat diperkaya dengan pengetahuan khusus melalui unggahan file, memungkinkan mereka untuk bertindak sebagai sumber otoritatif pada teks atau dokumen tertentu. 
- Mengkomersialkan GPT Anda melibatkan penerbitannya ke Toko GPT, di mana Anda dapat berbagi dan memasarkan asisten Anda ke audiens yang lebih luas. 
- Membangun asisten fungsional melibatkan iterasi melalui prompt desain, mendefinisikan persona yang jelas, menetapkan aturan, dan memastikan output asisten selaras dengan harapan pengguna. 
- Membuat tindakan khusus memerlukan pemahaman dan penerapan spesifikasi OpenAPI, menyebarkan layanan secara lokal menggunakan alat seperti ngrok, dan menghubungkan layanan ini ke asisten Anda. 
- Asisten pengetahuan dapat menangani berbagai tugas, mulai dari mencari dan membandingkan dokumen hingga menghasilkan konten baru berdasarkan basis pengetahuan mereka. 
- Menerbitkan asisten memerlukan pertimbangan cermat terhadap penggunaan sumber daya, pengalaman pengguna, dan faktor ekonomi untuk memastikan keefektifan dan keberlanjutannya untuk penggunaan publik. 
- Toko GPT, yang tersedia untuk pelanggan ChatGPT Plus, adalah platform berharga untuk belajar dan memperoleh kemahiran dalam membangun asisten AI, dengan potensi peluang bagi hasil di masa depan.