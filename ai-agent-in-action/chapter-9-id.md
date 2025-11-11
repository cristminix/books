# Menguasai prompt agen dengan alur prompt

## Bab ini mencakup
- Memahami rekayasa prompt sistematis dan menyiapkan alur prompt pertama Anda
- Membuat profil/persona prompt yang efektif
- Mengevaluasi profil: Rubrik dan landasan
- Landasan evaluasi profil model bahasa besar
- Membandingkan prompt: Mendapatkan profil yang sempurna

Dalam bab ini, kita akan mendalami strategi rekayasa prompt Uji Perubahan Secara Sistematis. Jika Anda ingat, kita telah membahas strategi besar dari kerangka kerja rekayasa prompt OpenAI di bab 2. Strategi-strategi ini sangat penting dalam membantu kita membangun prompt yang lebih baik dan, akibatnya, profil dan persona agen yang lebih baik. Memahami peran ini adalah kunci perjalanan rekayasa prompt kita.

Uji Perubahan Secara Sistematis adalah aspek inti dari rekayasa prompt sehingga Microsoft mengembangkan alat di sekitar strategi ini yang disebut *alur prompt*, yang dijelaskan kemudian di bab ini. Sebelum membahas alur prompt, kita perlu memahami mengapa kita memerlukan rekayasa prompt sistemik.

## 9.1 Mengapa kita memerlukan rekayasa prompt sistematis

Rekayasa prompt, pada dasarnya, adalah proses berulang. Saat membuat prompt, Anda akan sering mengulang dan mengevaluasi. Untuk melihat konsep ini dalam tindakan, pertimbangkan penerapan sederhana rekayasa prompt pada pertanyaan ChatGPT.

Anda dapat mengikuti dengan membuka browser Anda ke ChatGPT (https://chat.openai.com/), memasukkan prompt (teks) berikut ke ChatGPT, dan mengklik tombol Kirim Pesan (contoh percakapan ini ditunjukkan pada gambar 9.1, di sisi kiri):

```
bisakah kamu merekomendasikan sesuatu
```

![gambar](Images/9-1.png)

**Gambar 9.1** Perbedaan dalam menerapkan rekayasa prompt dan iterasi

Kita dapat melihat bahwa respons dari ChatGPT meminta informasi lebih lanjut. Silakan buka percakapan baru dengan ChatGPT, dan masukkan prompt berikut, seperti yang ditunjukkan pada gambar 9.1, di sisi kanan:

```
Bisakah Anda merekomendasikan film perjalanan waktu yang berlatar di abad pertengahan.
```

Hasil pada gambar 9.1 menunjukkan perbedaan yang jelas antara menghilangkan detail dan menjadi lebih spesifik dalam permintaan Anda. Kami baru saja menerapkan taktik Menulis Instruksi yang Jelas dengan sopan, dan ChatGPT memberi kami rekomendasi yang bagus. Tetapi perhatikan juga bagaimana ChatGPT sendiri memandu pengguna ke dalam prompt yang lebih baik. Layar yang diperbarui yang ditunjukkan pada gambar 9.2 menunjukkan strategi rekayasa prompt OpenAI.

![gambar](Images/9-2.png)

**Gambar 9.2** Strategi rekayasa prompt OpenAI, dipecah berdasarkan komponen agen

Kami baru saja menerapkan iterasi sederhana untuk meningkatkan prompt kami. Kita dapat memperluas contoh ini dengan menggunakan prompt/pesan sistem. Gambar 9.3 menunjukkan penggunaan dan peran prompt sistem dalam komunikasi berulang. Di bab 2, kami menggunakan pesan/prompt sistem dalam berbagai contoh.

![gambar](Images/9-3.png)

**Gambar 9.3** Pesan ke dan dari percakapan LLM dan iterasi pesan

Anda juga dapat mencoba ini di ChatGPT. Kali ini, masukkan prompt berikut dan sertakan kata *sistem* dalam huruf kecil, diikuti dengan baris baru (masukkan baris baru di jendela pesan tanpa mengirim pesan dengan menekan Shift-Enter):

```
sistem
```

```
Anda adalah seorang ahli film perjalanan waktu.
```

ChatGPT akan merespons dengan beberapa komentar yang menyenangkan, seperti yang ditunjukkan pada gambar 9.4. Karena itu, ia dengan senang hati menerima peran barunya dan meminta pertanyaan lanjutan. Sekarang masukkan prompt generik berikut seperti yang kita lakukan sebelumnya:

```
bisakah kamu merekomendasikan sesuatu
```

![gambar](Images/9-4.png)

**Gambar 9.4** Efek menambahkan prompt sistem ke percakapan kita sebelumnya

Kita baru saja melihat iterasi penyempurnaan prompt, rekayasa prompt, untuk mengekstrak respons yang lebih baik. Ini dicapai melalui tiga percakapan berbeda menggunakan UI ChatGPT. Meskipun bukan cara yang paling efisien, ini berhasil.

Hamun, kami belum mendefinisikan alur berulang untuk mengevaluasi prompt dan menentukan kapan sebuah prompt efektif. Gambar 9.5 menunjukkan metode rekayasa prompt sistemik menggunakan sistem iterasi dan evaluasi.

![gambar](Images/9-5.png)

**Gambar 9.5** Metode rekayasa prompt sistemik

Sistem iterasi dan evaluasi prompt mencakup strategi Uji Perubahan Secara Sistematis yang luas. Mengevaluasi kinerja dan keefektifan prompt masih baru, tetapi kami akan menggunakan teknik dari pendidikan, seperti rubrik dan landasan, yang akan kami jelajahi di bagian selanjutnya dari bab ini. Namun, seperti yang dijelaskan di bagian berikutnya, kita perlu memahami perbedaan antara persona dan profil agen sebelum kita melakukannya.

## 9.2 Memahami profil dan persona agen

*Profil agen* adalah enkapsulasi dari komponen prompt atau pesan yang mendeskripsikan agen. Ini mencakup persona agen, instruksi khusus, dan strategi lain yang dapat memandu pengguna atau konsumen agen lainnya.

Gambar 9.6 menunjukkan elemen utama dari profil agen. Elemen-elemen ini memetakan ke strategi rekayasa prompt yang dijelaskan dalam buku ini. Tidak semua agen akan menggunakan semua elemen dari profil agen lengkap.

![gambar](Images/9-6.png)

**Gambar 9.6** Bagian komponen dari profil agen

Pada tingkat dasar, *profil agen* adalah seperangkat prompt yang mendeskripsikan agen. Ini mungkin termasuk elemen eksternal lain yang terkait dengan tindakan/alat, pengetahuan, memori, penalaran, evaluasi, perencanaan, dan umpan balik. Kombinasi elemen-elemen ini membentuk seluruh profil prompt agen.

Prompt adalah jantung dari fungsi agen. Sebuah prompt atau seperangkat prompt mendorong setiap komponen agen dalam profil. Untuk tindakan/alat, prompt ini didefinisikan dengan baik, tetapi seperti yang telah kita lihat, prompt untuk memori dan pengetahuan dapat sangat bervariasi berdasarkan kasus penggunaan.

Definisi profil agen AI lebih dari sekadar prompt sistem. Alur prompt dapat memungkinkan kita untuk membangun prompt dan kode yang menyusun profil agen tetapi juga menyertakan kemampuan untuk mengevaluasi keefektifannya. Di bagian selanjutnya, kita akan membuka alur prompt dan mulai menggunakannya.

## 9.3 Menyiapkan alur prompt pertama Anda

Alur prompt adalah alat yang dikembangkan oleh Microsoft dalam platform Azure Machine Learning Studio-nya. Alat ini kemudian dirilis sebagai proyek sumber terbuka di GitHub, di mana ia telah menarik lebih banyak perhatian dan penggunaan. Meskipun pada awalnya dimaksudkan sebagai platform aplikasi, ia telah menunjukkan kekuatannya dalam mengembangkan dan mengevaluasi prompt/profil.

Karena alur prompt pada awalnya dikembangkan untuk berjalan di Azure sebagai layanan, ia memiliki arsitektur inti yang kuat. Alat ini mendukung pemrosesan batch multi-utas, yang membuatnya ideal untuk mengevaluasi prompt dalam skala besar. Bagian berikut akan membahas dasar-dasar memulai dengan alur prompt.

### 9.3.1 Memulai

Ada beberapa prasyarat yang harus dilakukan sebelum mengerjakan latihan dalam buku ini. Prasyarat yang relevan untuk bagian dan bab ini ditunjukkan dalam daftar berikut; pastikan untuk menyelesaikannya sebelum mencoba latihan:

- *Visual Studio Code (VS Code)* —Lihat apendiks A untuk instruksi instalasi, termasuk ekstensi tambahan.
- *Alur prompt, ekstensi VS Code* —Lihat apendiks A untuk detail tentang menginstal ekstensi.
- *Lingkungan virtual Python* —Lihat apendiks A untuk detail tentang menyiapkan lingkungan virtual.
- *Instal paket alur prompt* —Dalam lingkungan virtual Anda, lakukan `pip` `install` cepat, seperti yang ditunjukkan di sini:

```
pip install promptflow promptflow-tools
```

- *LLM (GPT-4 atau lebih tinggi)* —Anda akan memerlukan akses ke GPT-4 atau lebih tinggi melalui OpenAI atau Azure OpenAI Studio. Lihat apendiks B jika Anda memerlukan bantuan untuk mengakses sumber daya ini.
- *Kode sumber buku* —Kloning kode sumber buku ke folder lokal; lihat apendiks A jika Anda memerlukan bantuan untuk mengkloning repositori.

Buka VS Code ke folder kode sumber buku, `chapter` `3`. Pastikan Anda memiliki lingkungan virtual yang terhubung dan telah menginstal paket dan ekstensi alur prompt.

Pertama, Anda akan ingin membuat koneksi ke sumber daya LLM Anda dalam ekstensi alur prompt. Buka ekstensi alur prompt dalam VS Code, lalu klik untuk membuka koneksi. Kemudian, klik tanda plus di samping sumber daya LLM untuk membuat koneksi baru, seperti yang ditunjukkan pada gambar 9.7.

![gambar](Images/9-7.png)

**Gambar 9.7** Membuat koneksi LLM alur prompt baru

Ini akan membuka file YAML di mana Anda perlu mengisi nama koneksi dan informasi lain yang relevan dengan koneksi Anda. Ikuti petunjuknya, dan jangan masukkan kunci API ke dalam dokumen, seperti yang ditunjukkan pada gambar 9.8.

![gambar](Images/9-8.png)

**Gambar 9.8** Mengatur informasi koneksi untuk sumber daya LLM Anda

Saat informasi koneksi dimasukkan, klik tautan Buat Koneksi di bagian bawah dokumen. Ini akan membuka prompt terminal di bawah dokumen, meminta Anda untuk memasukkan kunci Anda. Tergantung pada konfigurasi terminal Anda, Anda mungkin tidak dapat menempel (Ctrl-V, Cmd-V). Atau, Anda dapat menempelkan kunci dengan mengarahkan kursor mouse ke terminal dan mengklik kanan di Windows.

Sekarang kita akan menguji koneksi dengan terlebih dahulu membuka alur sederhana di folder `chapter_09/promptflow/simpleflow`. Kemudian, buka file `flow.dag.yaml` di VS Code. Ini adalah file YAML, tetapi ekstensi alur prompt menyediakan editor visual yang dapat diakses dengan mengklik tautan Editor Visual di bagian atas file, seperti yang ditunjukkan pada gambar 9.9.

![gambar](Images/9-9.png)

**Gambar 9.9** Membuka editor visual alur prompt

Setelah jendela editor visual dibuka, Anda akan melihat grafik yang mewakili alur dan blok alur. Klik dua kali blok pemberi rekomendasi, dan atur nama koneksi, jenis API, dan nama model atau penerapan, seperti yang ditunjukkan pada gambar 9.10.

![gambar](Images/9-10.png)

**Gambar 9.10** Mengatur detail koneksi LLM

Alur prompt terdiri dari satu set blok yang dimulai dengan blok `Input` dan diakhiri dengan blok `Output`. Dalam alur sederhana ini, blok `pemberi rekomendasi` mewakili koneksi LLM dan prompt yang digunakan untuk berkomunikasi dengan model. Blok `gema` untuk contoh sederhana ini menggemakan input.

Saat membuat koneksi ke LLM, baik di alur prompt atau melalui API, berikut adalah parameter penting yang selalu perlu kita pertimbangkan (dokumentasi alur prompt: https://microsoft.github.io/promptflow/):

- *Koneksi* —Ini adalah nama koneksi, tetapi juga mewakili layanan yang Anda sambungkan. Alur prompt mendukung beberapa layanan, termasuk LLM yang diterapkan secara lokal.
- *API* —Ini adalah jenis API. Pilihannya adalah `obrolan` untuk API penyelesaian obrolan, seperti GPT-4, atau `penyelesaian` untuk model penyelesaian yang lebih lama, seperti OpenAI Davinci.
- *Model* —Ini mungkin nama model atau penerapan, tergantung pada koneksi layanan Anda. Untuk OpenAI, ini akan menjadi nama model, dan untuk Azure OpenAI, ini akan mewakili nama penerapan.
- *Suhu* —Ini mewakili stokastisitas atau variabilitas respons model. Nilai `1` mewakili variabilitas respons yang tinggi, sedangkan `0` menunjukkan keinginan untuk tidak ada variabilitas. Ini adalah parameter penting untuk dipahami dan, seperti yang akan kita lihat, akan bervariasi berdasarkan kasus penggunaan.
- *Berhenti* —Pengaturan opsional ini memberitahu panggilan ke LLM untuk berhenti membuat token. Ini lebih sesuai untuk model yang lebih lama dan sumber terbuka.
- *Token maks* —Ini membatasi jumlah token yang digunakan dalam percakapan. Pengetahuan tentang berapa banyak token yang Anda gunakan sangat penting untuk mengevaluasi bagaimana interaksi LLM Anda akan bekerja saat diskalakan. Menghitung token mungkin tidak menjadi perhatian jika Anda sedang menjelajahi dan melakukan penelitian. Namun, dalam sistem produksi, token mewakili beban pada LLM, dan koneksi yang menggunakan banyak token mungkin tidak dapat diskalakan dengan baik.
- *Parameter lanjutan* —Anda dapat mengatur beberapa opsi lagi untuk menyempurnakan interaksi Anda dengan LLM, tetapi kami akan membahas topik itu di bagian selanjutnya dari buku ini.

Setelah mengonfigurasi blok LLM, gulir ke atas ke bagian blok Input, dan tinjau input utama yang ditunjukkan di bidang user_input, seperti yang ditunjukkan pada gambar 9.11. Biarkan sebagai default, lalu klik tombol Putar di bagian atas jendela.

![gambar](Images/9-11.png)

**Gambar 9.11** Mengatur input dan memulai alur

Semua blok dalam alur akan berjalan, dan hasilnya akan ditampilkan di jendela terminal. Yang seharusnya menarik bagi Anda adalah bahwa output menunjukkan rekomendasi untuk film perjalanan waktu. Ini karena blok pemberi rekomendasi sudah memiliki profil sederhana yang ditetapkan, dan kita akan melihat cara kerjanya di bagian berikutnya.

### 9.3.2 Membuat profil dengan templat Jinja2

Alur merespons dengan rekomendasi film perjalanan waktu karena prompt atau profil yang digunakannya. Secara default, alur prompt menggunakan templat Jinja2 untuk menentukan konten prompt atau apa yang akan kita sebut *profil.* Untuk tujuan buku ini dan eksplorasi kita tentang agen AI, kita akan merujuk ke templat ini sebagai profil alur atau agen.

Meskipun alur prompt tidak secara eksplisit menyebut dirinya sebagai mesin asisten atau agen, ia tentu memenuhi kriteria untuk menghasilkan proksi dan jenis agen umum. Seperti yang akan Anda lihat, alur prompt bahkan mendukung penerapan alur ke dalam kontainer dan sebagai layanan.

Buka VS Code ke `chapter_09/promptflow/simpleflow/flow.dag.yaml`, dan buka file di editor visual. Kemudian, temukan bidang Prompt, dan klik tautan `direkomendasikan` `.jinja2`, seperti yang ditunjukkan pada gambar 9.12.

![gambar](Images/9-12.png)

**Gambar 9.12** Membuka templat Jinja2 prompt dan memeriksa bagian-bagian dari profil/prompt

Jinja adalah mesin templat, dan Jinja2 adalah versi khusus dari mesin itu. Templat adalah cara terbaik untuk mendefinisikan tata letak dan bagian dari segala bentuk dokumen teks. Mereka telah digunakan secara luas untuk menghasilkan HTML, JSON, CSS, dan bentuk dokumen lainnya. Selain itu, mereka mendukung kemampuan untuk menerapkan kode langsung ke dalam templat. Meskipun tidak ada cara standar untuk membuat prompt atau profil agen, preferensi kami dalam buku ini adalah menggunakan mesin templat seperti Jinja.

Pada titik ini, ubah peran dalam prompt sistem dari templat `direkomendasikan.jinja2`. Kemudian, jalankan semua blok alur dengan membuka alur di editor visual dan mengklik tombol Putar. Bagian selanjutnya akan melihat cara lain menjalankan alur prompt untuk pengujian atau penerapan aktual.

### 9.3.3 Menerapkan API alur prompt

Karena alur prompt juga dirancang untuk diterapkan sebagai layanan, ia mendukung beberapa cara untuk menerapkan sebagai aplikasi atau API dengan cepat. Alur prompt dapat diterapkan sebagai aplikasi web lokal dan API yang berjalan dari terminal atau sebagai kontainer Docker.

Kembali ke file `flow.dag.yaml` di editor visual dari VS Code. Di bagian atas jendela di samping tombol Putar ada beberapa opsi yang ingin kita selidiki lebih lanjut. Klik tombol Bangun seperti yang ditunjukkan pada gambar 9.13, lalu pilih untuk menerapkan sebagai aplikasi lokal. File YAML baru akan dibuat untuk mengonfigurasi aplikasi. Biarkan default, dan klik tautan Mulai Aplikasi Lokal.

![gambar](Images/9-13.png)

**Gambar 9.13** Membangun dan memulai alur sebagai aplikasi lokal

Ini akan meluncurkan alur sebagai aplikasi web lokal, dan Anda akan melihat tab browser terbuka, seperti yang ditunjukkan pada gambar 9.14. Masukkan beberapa teks ke dalam bidang user_input, yang ditandai sebagai wajib dengan tanda bintang merah. Klik Enter dan tunggu beberapa detik untuk balasan.

![gambar](Images/9-14.png)

**Gambar 9.14** Menjalankan alur sebagai aplikasi web lokal

Anda akan melihat balasan seperti yang ditunjukkan sebelumnya pada gambar 9.12, di mana alur atau agen membalas dengan daftar film perjalanan waktu. Ini bagus—kita baru saja mengembangkan profil agen pertama kita dan setara dengan agen proksi. Namun, kita perlu menentukan seberapa berhasil atau berharganya rekomendasi tersebut. Di bagian selanjutnya, kita akan mengeksplorasi cara mengevaluasi prompt dan profil.

## 9.4 Mengevaluasi profil: Rubrik dan landasan

Elemen kunci dari setiap profil prompt atau agen adalah seberapa baik ia melakukan tugas yang diberikan. Seperti yang kita lihat dalam contoh rekomendasi kita, meminta profil agen untuk memberikan daftar rekomendasi relatif mudah, tetapi mengetahui apakah rekomendasi tersebut bermanfaat mengharuskan kita untuk mengevaluasi responsnya.

Untungnya, alur prompt telah dirancang untuk mengevaluasi prompt/profil dalam skala besar. Infrastruktur yang kuat memungkinkan evaluasi interaksi LLM untuk diparalelkan dan dikelola sebagai pekerja, memungkinkan ratusan evaluasi dan variasi profil terjadi dengan cepat.

Di bagian selanjutnya, kita akan melihat bagaimana alur prompt dapat dikonfigurasi untuk menjalankan variasi prompt/profil satu sama lain. Kita perlu memahami ini sebelum mengevaluasi kinerja profil.

Alur prompt menyediakan mekanisme untuk memungkinkan beberapa variasi dalam prompt/profil LLM. Alat ini sangat baik untuk membandingkan perbedaan halus atau signifikan antara variasi profil. Ketika digunakan dalam melakukan evaluasi massal, ini bisa sangat berharga untuk menilai kinerja profil dengan cepat.

Buka file `recommender_with_variations/flow.dag.yaml` di VS Code dan editor visual alur, seperti yang ditunjukkan pada gambar 9.15. Kali ini, kami membuat profil lebih umum dan memungkinkan penyesuaian di tingkat input. Ini memungkinkan kami untuk memperluas rekomendasi kami ke apa pun dan bukan hanya film perjalanan waktu.

![gambar](Images/9-15.png)

**Gambar 9.15** Pemberi rekomendasi, dengan variasi dalam alur dan input yang diperluas

Input baru Subjek, Genre, Format, dan Kustom memungkinkan kita untuk mendefinisikan profil yang dapat dengan mudah disesuaikan dengan rekomendasi apa pun. Ini juga berarti bahwa kita harus menyiapkan input berdasarkan kasus penggunaan rekomendasi. Ada beberapa cara untuk menyiapkan input ini; dua contoh penyiapan input ditunjukkan pada gambar 9.16. Gambar tersebut menunjukkan dua opsi, opsi A dan B, untuk penyiapan input. Opsi A mewakili UI klasik; mungkin ada objek bagi pengguna untuk memilih subjek atau genre, misalnya. Opsi B menempatkan agen proksi/obrolan untuk berinteraksi dengan pengguna dengan lebih baik untuk memahami subjek, genre, dan sebagainya yang diinginkan.

![gambar](Images/9-16.png)

**Gambar 9.16** Opsi interaksi pengguna untuk berinteraksi dengan profil agen untuk menyiapkan input ke profil agen

Bahkan dengan mempertimbangkan kekuatan LLM, Anda mungkin masih ingin atau perlu menggunakan opsi A. Manfaat opsi A adalah Anda dapat membatasi dan memvalidasi input seperti yang Anda lakukan dengan UI modern mana pun. Atau, kelemahan opsi A adalah perilaku yang dibatasi dapat membatasi dan membatasi kasus penggunaan di masa mendatang.

Opsi B mewakili cara yang lebih cair dan alami tanpa UI tradisional. Ini jauh lebih kuat dan dapat diperluas daripada opsi A tetapi juga memperkenalkan lebih banyak hal yang tidak diketahui untuk evaluasi. Namun, jika agen proksi yang digunakan opsi B ditulis dengan baik, itu dapat sangat membantu dalam mengumpulkan informasi yang lebih baik dari pengguna.

Opsi yang Anda pilih akan menentukan bagaimana Anda perlu mengevaluasi profil Anda. Jika Anda baik-baik saja dengan UI yang dibatasi, maka kemungkinan input juga akan dibatasi pada satu set nilai diskrit. Untuk saat ini, kami akan mengasumsikan opsi B untuk penyiapan input, yang berarti nilai input akan ditentukan oleh namanya.

Untuk kembali ke VS Code dan tampilan visual alur pemberi rekomendasi dengan varian, klik ikon yang ditunjukkan sebelumnya pada gambar 9.15 untuk membuka varian dan mengizinkan pengeditan. Kemudian, klik tautan `recommend.jinja2` dan `recommender_variant_1.jinja2` untuk membuka file secara berdampingan, seperti yang ditunjukkan pada gambar 9.17.

![gambar](Images/9-17.png)

**Gambar 9.17** Perbandingan berdampingan dari templat profil varian untuk pemberi rekomendasi

Gambar 9.17 menunjukkan perbedaan antara profil varian. Satu profil menyuntikkan input ke dalam prompt pengguna, dan yang lainnya menyuntikkannya ke dalam prompt sistem. Namun, penting untuk dipahami bahwa variasi dapat mencakup lebih dari sekadar desain profil, seperti yang diidentifikasi dalam tabel 9.1.

**Tabel 9.1** Opsi variasi LLM dalam alur prompt

| Opsi | Contoh opsi evaluasi | Catatan | 
|---|---|---|
| Templat prompt Jinja2 | Bandingkan variasi prompt sistem, variasi prompt pengguna, atau variasi prompt campuran. | Beberapa kombinasi dan teknik tak berujung dapat diterapkan di sini. Rekayasa prompt berkembang setiap saat. |
| LLM | Bandingkan GPT-9.5 dengan GPT-4. <br/> Bandingkan GPT-4 dengan GPT-4 Turbo. <br/> Bandingkan model sumber terbuka dengan model komersial. | Ini adalah cara yang berguna untuk mengevaluasi dan mendasarkan kinerja model terhadap sebuah prompt. Ini juga dapat membantu Anda menyetel profil Anda agar berfungsi dengan model sumber terbuka dan/atau yang lebih murah. |
| Suhu | Bandingkan suhu 0 (tanpa keacakan) dengan 1 (keacakan maksimum). | Perubahan suhu dapat secara signifikan mengubah respons beberapa prompt, yang dapat meningkatkan atau menurunkan kinerja. |
| Token maks | Bandingkan token terbatas dengan ukuran token yang lebih besar. | Ini dapat memungkinkan Anda untuk mengurangi dan memaksimalkan penggunaan token. |
| Parameter lanjutan | Bandingkan perbedaan dengan opsi seperti `top_p`, `presence_penalty`, `frequency_penalty`, dan `logit_bias`. | Kami akan membahas penggunaan parameter lanjutan ini di bab-bab selanjutnya. |
| Panggilan fungsi | Bandingkan panggilan fungsi alternatif. | Panggilan fungsi akan dibahas nanti di bab ini. |

Untuk contoh sederhana ini, kita hanya akan menggunakan variasi prompt dengan memvariasikan input untuk dicerminkan baik dalam sistem atau prompt pengguna. Lihat gambar 9.17 untuk melihat seperti apa tampilannya. Kita kemudian dapat dengan cepat menjalankan kedua variasi dengan mengklik tombol Putar (Jalankan Semua) di bagian atas dan memilih keduanya, seperti yang ditunjukkan pada gambar 9.18.

![gambar](Images/9-18.png)

**Gambar 9.18** Menjalankan kedua variasi prompt secara bersamaan

Di jendela terminal, Anda akan melihat hasil dari kedua proses. Hasilnya kemungkinan akan terlihat serupa, jadi sekarang kita harus melanjutkan ke cara kita mengevaluasi perbedaan antara variasi di bagian berikutnya.

## 9.5 Memahami rubrik dan landasan

Evaluasi kinerja prompt/profil bukanlah sesuatu yang biasanya dapat kita lakukan dengan menggunakan ukuran akurasi atau persentase yang benar. Mengukur kinerja profil bergantung pada kasus penggunaan dan hasil yang diinginkan. Jika sesederhana menentukan apakah responsnya benar atau salah, itu lebih baik. Namun, dalam kebanyakan kasus, evaluasi tidak akan sesederhana itu.

Dalam pendidikan, konsep *rubrik* mendefinisikan seperangkat kriteria dan standar terstruktur yang harus ditetapkan siswa untuk menerima nilai tertentu. Rubrik juga dapat digunakan untuk mendefinisikan panduan untuk kinerja profil atau prompt. Kita dapat mengikuti langkah-langkah ini untuk mendefinisikan rubrik yang dapat kita gunakan untuk mengevaluasi kinerja profil atau prompt:

1. *Identifikasi tujuan dan sasaran.* Tentukan tujuan yang ingin dicapai oleh profil atau agen. Misalnya, apakah Anda ingin mengevaluasi kualitas rekomendasi untuk audiens tertentu atau kualitas keseluruhan untuk subjek, format, atau input lain yang diberikan?
2. *Tentukan kriteria.* Kembangkan seperangkat kriteria atau dimensi yang akan Anda gunakan untuk mengevaluasi profil. Kriteria ini harus selaras dengan tujuan Anda dan memberikan pedoman yang jelas untuk penilaian. Setiap kriteria harus spesifik dan terukur. Misalnya, Anda mungkin ingin mengukur rekomendasi berdasarkan seberapa baik kesesuaiannya dengan genre, lalu berdasarkan subjek dan format.
3. *Buat skala*. Tetapkan skala peringkat yang menjelaskan tingkat kinerja untuk setiap kriteria. Skala standar mencakup skala numerik (misalnya, 1–5) atau skala deskriptif (misalnya, Sangat Baik, Baik, Cukup, Buruk).
4. *Berikan deskripsi.* Untuk setiap level pada skala, berikan deskripsi yang jelas dan ringkas yang menunjukkan apa yang merupakan kinerja yang kuat dan apa yang mewakili kinerja yang lebih lemah untuk setiap kriteria.
5. *Terapkan rubrik.* Saat menilai prompt atau profil, gunakan rubrik untuk mengevaluasi kinerja prompt berdasarkan kriteria yang telah ditetapkan. Tetapkan skor atau peringkat untuk setiap kriteria, dengan mempertimbangkan deskripsi untuk setiap level.
6. *Hitung skor total.* Tergantung pada rubrik Anda, Anda dapat menghitung skor total dengan menjumlahkan skor untuk setiap kriteria atau menggunakan rata-rata tertimbang jika beberapa kriteria lebih penting daripada yang lain.
7. *Pastikan konsistensi evaluasi.* Jika beberapa evaluator menilai profil, sangat penting untuk memastikan konsistensi dalam penilaian.
8. *Tinjau, revisi, dan ulangi.* Tinjau dan revisi rubrik secara berkala untuk memastikannya selaras dengan tujuan dan sasaran penilaian Anda. Sesuaikan seperlunya untuk meningkatkan efektivitasnya.

*Landasan* adalah konsep yang dapat diterapkan pada evaluasi profil dan prompt—ini mendefinisikan seberapa baik respons selaras dengan kriteria dan standar spesifik rubrik yang diberikan. Anda juga dapat menganggap landasan sebagai ekspektasi dasar dari output prompt atau profil.

Daftar ini merangkum beberapa pertimbangan penting lainnya saat menggunakan landasan dengan evaluasi profil:

- Landasan mengacu pada penyelarasan respons dengan kriteria, tujuan, dan konteks yang ditentukan oleh rubrik dan prompt.
- Landasan melibatkan penilaian apakah respons secara langsung membahas kriteria rubrik, tetap pada topik, dan mematuhi instruksi yang diberikan.
- Evaluator dan evaluasi mengukur akurasi, relevansi, dan kepatuhan terhadap standar saat menilai landasan.
- Landasan memastikan bahwa output respons berakar kuat dalam konteks yang ditentukan, membuat proses penilaian lebih objektif dan bermakna.

Respons yang memiliki landasan yang baik selaras dengan semua kriteria rubrik dalam konteks dan tujuan yang diberikan. Respons yang memiliki landasan yang buruk akan gagal atau melewatkan seluruh kriteria, konteks, dan tujuan.

Karena konsep rubrik dan landasan mungkin masih abstrak, mari kita lihat penerapannya pada contoh pemberi rekomendasi kita saat ini. Berikut adalah daftar yang mengikuti proses untuk mendefinisikan rubrik seperti yang diterapkan pada contoh pemberi rekomendasi kita:

1. *Identifikasi tujuan dan sasaran.* Tujuan dari profil/prompt kami adalah untuk merekomendasikan tiga item teratas dengan subjek, format, genre, dan input khusus.
2. *Tentukan kriteria.* Untuk kesederhanaan, kami akan mengevaluasi bagaimana rekomendasi tertentu selaras dengan kriteria input yang diberikan, subjek, format, dan genre. Misalnya, jika sebuah profil merekomendasikan sebuah buku ketika diminta format film, kami mengharapkan skor rendah dalam kriteria format.
3. *Buat skala.* Sekali lagi, untuk menjaga agar tetap sederhana, kami akan menggunakan skala 1–5 (1 buruk, dan 5 sangat baik).
4. *Berikan deskripsi.* Lihat deskripsi umum untuk skala peringkat yang ditunjukkan pada tabel 9.2.
5. *Terapkan rubrik.* Dengan rubrik yang ditetapkan pada tahap ini, ini adalah latihan yang sangat baik untuk mengevaluasi rubrik terhadap rekomendasi secara manual.
6. *Hitung skor total.* Untuk rubrik kami, kami akan merata-ratakan skor untuk semua kriteria untuk memberikan skor total.
7. *Pastikan konsistensi evaluasi.* Teknik yang akan kami gunakan untuk evaluasi akan memberikan hasil yang sangat konsisten.
8. *Tinjau, revisi, dan ulangi.* Kami akan meninjau, membandingkan, dan mengulangi profil, rubrik, dan evaluasi kami sendiri.

**Tabel 9.2** Peringkat rubrik

| Peringkat | Deskripsi | 
|---|---|
| 1 | Penyelarasan yang buruk: ini adalah kebalikan dari apa yang diharapkan mengingat kriteria. |
| 2 | Penyelarasan yang buruk: ini bukan pilihan yang baik untuk kriteria yang diberikan. |
| 3 | Penyelarasan yang biasa-biasa saja: mungkin cocok atau tidak cocok dengan kriteria yang diberikan. |
| 4 | Penyelarasan yang baik: mungkin tidak selaras 100% dengan kriteria tetapi merupakan pilihan yang baik. |
| 5 | Penyelarasan yang sangat baik: ini adalah rekomendasi yang baik untuk kriteria yang diberikan. |

Rubrik dasar ini sekarang dapat diterapkan untuk mengevaluasi respons untuk profil kami. Anda dapat melakukan ini secara manual, atau seperti yang akan Anda lihat di bagian berikutnya, menggunakan profil LLM kedua.

## 9.6 Landasan evaluasi dengan profil LLM

Bagian ini akan menggunakan prompt/profil LLM lain untuk evaluasi dan landasan. Prompt LLM kedua ini akan menambahkan blok lain setelah rekomendasi dibuat. Ini akan memproses rekomendasi yang dihasilkan dan mengevaluasi masing-masing, dengan rubrik sebelumnya.

Sebelum GPT-4 dan LLM canggih lainnya muncul, kami tidak akan pernah mempertimbangkan untuk menggunakan prompt LLM lain untuk mengevaluasi atau mendasarkan profil. Anda sering ingin menggunakan model yang berbeda saat menggunakan LLM untuk mendasarkan profil. Namun, jika Anda membandingkan profil satu sama lain, menggunakan LLM yang sama untuk evaluasi dan landasan adalah tepat.

Buka file `recommender_with_LLM_evaluation\flow.dag.yaml` di editor visual alur prompt, gulir ke bawah ke blok `evaluate_recommendation`, dan klik tautan `evaluate_recommendation.jinja2` untuk membuka file, seperti yang ditunjukkan pada gambar 9.19. Setiap bagian dari rubrik diidentifikasi dalam gambar.

![gambar](Images/9-19.png)

**Gambar 9.19** Prompt evaluasi, dengan setiap bagian dari rubrik diuraikan

Kami memiliki rubrik yang tidak hanya didefinisikan dengan baik tetapi juga dalam bentuk prompt yang dapat digunakan untuk mengevaluasi rekomendasi. Ini memungkinkan kami untuk mengevaluasi keefektifan rekomendasi untuk profil tertentu—secara otomatis. Tentu saja, Anda juga dapat menggunakan rubrik untuk menilai dan mengevaluasi rekomendasi secara manual untuk landasan yang lebih baik.

> **Catatan** —Menggunakan LLM untuk mengevaluasi prompt dan profil memberikan landasan yang kuat untuk membandingkan kinerja profil. Ini juga dapat melakukannya tanpa bias manusia secara terkontrol dan dapat diulang. Ini memberikan mekanisme yang sangat baik untuk menetapkan landasan dasar untuk setiap profil atau prompt.

Kembali ke editor visual alur `recommender_with_LLM_evaluation`, kita dapat menjalankan alur dengan mengklik tombol Putar dan mengamati output. Anda dapat menjalankan satu rekomendasi atau menjalankan kedua variasi saat diminta. Output dari satu evaluasi menggunakan input default ditunjukkan dalam daftar berikut.

**Daftar 9.1** Output evaluasi rubrik LLM

```
{
    "rekomendasi": "Judul: The Butterfly Effect
Subjek: 5
Format: 5
Genre: 4

Judul: Primer
Subjek: 5
Format: 5
Genre: 4

Judul: Time Bandits
Subjek: 5
Format: 5
Genre: 5"
}
```

Kami sekarang memiliki rubrik untuk mendasarkan pemberi rekomendasi kami, dan evaluasi dijalankan secara otomatis menggunakan prompt LLM kedua. Di bagian selanjutnya, kita akan melihat cara melakukan beberapa evaluasi secara bersamaan dan kemudian pada skor total untuk semuanya.

## 9.7 Membandingkan profil: Mendapatkan profil yang sempurna

Dengan pemahaman kita tentang rubrik dan landasan, kita sekarang dapat melanjutkan untuk mengevaluasi dan mengulangi profil yang sempurna. Namun, sebelum kita melakukannya, kita perlu membersihkan output dari blok evaluasi LLM. Ini akan mengharuskan kita untuk mengurai rekomendasi menjadi sesuatu yang lebih Pythonic, yang akan kita tangani di bagian berikutnya.

### 9.7.1 Mengurai output evaluasi LLM

Karena output mentah dari blok evaluasi adalah teks, kami sekarang ingin mengurainya menjadi sesuatu yang lebih dapat digunakan. Tentu saja, menulis fungsi penguraian itu sederhana, tetapi ada cara yang lebih baik untuk mentransmisikan respons secara otomatis. Kami membahas metode yang lebih baik untuk mengembalikan respons di bab 5, tentang tindakan agen.

Buka `chapter_09\prompt_flow\recommender_with_parsing\flow.dag.yaml` di VS Code, dan lihat alur di editor visual. Temukan blok `parsing_results`, dan klik tautan untuk membuka file Python di editor, seperti yang ditunjukkan pada gambar 9.20.

![gambar](Images/9-20.png)

**Gambar 9.20** Membuka file `parsing_results.py` di VS Code

Kode untuk file `parsing_results.py` ditunjukkan dalam daftar 9.2.

**Daftar 9.2** `parsing_results.py`

```python
from promptflow import tool

@tool     #1
def parse(input: str) -> str:
    # Memisahkan rekomendasi menjadi blok film individual
    rblocks = input.strip().split("\n\n")     #2

    # Fungsi untuk mengurai blok rekomendasi individual menjadi kamus
    def parse_block(block):
        lines = block.split('\n')
        rdict = {}
        for line in lines:
            kvs = line.split(': ')
            key, value = kvs[0], kvs[1]
            rdict[key.lower()] = value    #3
        return rdict

    parsed = [parse_block(block) for block in rblocks]   #4

    return parsed
```

1. Dekorator khusus untuk menunjukkan blok alat
2. Memisahkan input dan baris baru ganda
3. Membuat entri kamus dan mengatur nilainya
4. Melakukan loop melalui setiap blok dan mengurai menjadi kamus kunci/nilai

Kami mengubah output rekomendasi dari daftar 9.1, yang hanya berupa string, menjadi kamus. Jadi kode ini akan mengubah string ini menjadi blok JSON yang ditunjukkan berikutnya:

*Sebelum penguraian:*
```
"Judul: The Butterfly Effect
Subjek: 5
Format: 5
Genre: 4

Judul: Primer
Subjek: 5
Format: 5
Genre: 4

Judul: Time Bandits
Subjek: 5
Format: 5
Genre: 5"
```

*Setelah penguraian:*
```
       {
            "judul": " The Butterfly Effect
            "subjek": "5",
            "format": "5",
            "genre": "4"
        },
        {
            "judul": " Primer",
            "subjek": "5",
            "format": "5",
            "genre": "4"
        },
        {
            "judul": " Time Bandits",
            "subjek": "5",
            "format": "5",
            "genre": "5"
        }
```

Output dari blok `parsing_results` ini sekarang diteruskan ke output dan dibungkus dalam daftar rekomendasi. Kita bisa melihat seperti apa semua ini dengan menjalankan alur.

Buka `flow.dag.yaml` untuk alur di editor visual, dan klik tombol Putar (Jalankan Semua). Pastikan untuk memilih untuk menggunakan kedua varian pemberi rekomendasi. Anda akan melihat kedua variasi berjalan dan output ke terminal.

Pada titik ini, kami memiliki rekomendasi kerja penuh dan alur evaluasi LLM yang menghasilkan skor untuk setiap kriteria pada setiap output. Namun, untuk melakukan evaluasi komprehensif dari profil tertentu, kami ingin menghasilkan beberapa rekomendasi dengan berbagai kriteria. Kita akan melihat cara melakukan pemrosesan batch alur di bagian berikutnya.

### 9.7.2 Menjalankan pemrosesan batch di alur prompt

Dalam profil rekomendasi generik kami, kami ingin mengevaluasi bagaimana berbagai kriteria input dapat memengaruhi rekomendasi yang dihasilkan. Untungnya, alur prompt dapat memproses batch variasi apa pun yang ingin kami uji. Batasannya hanya waktu dan uang yang ingin kami habiskan.

Untuk melakukan pemrosesan batch, pertama-tama kita harus membuat dokumen JSON Lines (JSONL) atau daftar JSON dari kriteria input kita. Jika Anda ingat, kriteria input kami terlihat seperti berikut dalam format JSON:

```json
{
    "**subjek**": "perjalanan waktu",
    "**format**": "buku",
    "**genre**": "fantasi",
    "**kustom**": "jangan sertakan konten berperingkat R"
}
```

Kami ingin membuat daftar objek JSON seperti yang baru saja ditunjukkan, lebih disukai secara acak. Tentu saja, cara sederhana untuk melakukan ini adalah dengan meminta ChatGPT untuk membuat dokumen JSONL menggunakan prompt berikut:

```
Saya sedang mengembangkan agen rekomendasi. Agen akan merekomendasikan apa pun dengan kriteria berikut:
```

```
1. subjek - contoh: perjalanan waktu, memasak, liburan
```

```
2. format - contoh: buku, film, game
```

```
3. genre: dokumenter, aksi, romansa
```

```
4. kustom: jangan sertakan konten berperingkat R
```

```
Bisakah Anda membuat daftar acak dari kriteria ini dan menampilkannya dalam format file JSON Lines, JSONL. Harap sertakan 10 item dalam daftar.
```

Cobalah ini dengan membuka ChatGPT dan memasukkan prompt sebelumnya. File yang dibuat sebelumnya dapat ditemukan di folder alur, yang disebut `\bulk_recommend.jsonl`. Isi file ini telah ditampilkan di sini untuk referensi:

```
{
  "subjek": "perjalanan waktu",
  "format": "buku",
  "genre": "fantasi",
  "kustom": "jangan sertakan konten berperingkat R"
}
{
  "subjek": "eksplorasi ruang angkasa",
  "format": "podcast",
  "genre": "sci-fi",
  "kustom": "sertakan hanya konten yang ramah keluarga"
}
{
  "subjek": "misteri",
  "format": "podcast",
  "genre": "fantasi",
  "kustom": "jangan sertakan konten berperingkat R"
}
{
  "subjek": "eksplorasi ruang angkasa",
  "format": "podcast",
  "genre": "aksi",
  "kustom": "sertakan hanya konten yang ramah keluarga"
}
{
  "subjek": "liburan",
  "format": "buku",
  "genre": "thriller",
  "kustom": "jangan sertakan konten berperingkat R"
}
{
  "subjek": "misteri",
  "format": "buku",
  "genre": "sci-fi",
  "kustom": "jangan sertakan konten berperingkat R"
}
{
  "subjek": "misteri",
  "format": "buku",
  "genre": "romansa",
  "kustom": "jangan sertakan konten berperingkat R"
}
{
  "subjek": "liburan",
  "format": "film",
  "genre": "fantasi",
  "kustom": "jangan sertakan konten berperingkat R"
}
{
  "subjek": "memasak",
  "format": "Acara TV",
  "genre": "thriller",
  "kustom": "sertakan hanya konten yang ramah keluarga"
}
{
  "subjek": "misteri",
  "format": "film",
  "genre": "romansa",
  "kustom": "sertakan hanya konten yang ramah keluarga"
}
```

Dengan file massal ini, kita dapat menjalankan kedua varian menggunakan berbagai kriteria input dalam file JSONL massal. Buka file `flow.dag.yaml` di editor visual, klik Batch (ikon gelas kimia) untuk memulai proses pemuatan data massal, dan pilih file seperti yang ditunjukkan pada gambar 9.21. Untuk beberapa sistem operasi, ini mungkin muncul sebagai `File` `Data` `Lokal`.

![gambar](Images/9-21.png)

**Gambar 9.21** Memuat file JSONL massal untuk menjalankan alur pada beberapa variasi input

Setelah file massal dipilih, dokumen YAML baru akan terbuka dengan tautan Jalankan ditambahkan di bagian bawah file, seperti yang ditunjukkan pada gambar 9.22. Klik tautan untuk melakukan proses batch input.

![gambar](Images/9-22.png)

**Gambar 9.22** Menjalankan proses batch input

Pada titik ini, beberapa hal akan terjadi. Editor visual alur akan muncul, dan di sampingnya file log akan terbuka, menunjukkan kemajuan proses. Di jendela terminal, Anda akan melihat berbagai proses pekerja muncul dan berjalan.

Bersabarlah. Proses batch, bahkan untuk 10 item, mungkin memakan waktu beberapa menit atau detik, tergantung pada berbagai faktor seperti perangkat keras, panggilan sebelumnya, dan sebagainya. Tunggu hingga proses selesai, dan Anda akan melihat ringkasan hasil di terminal.

Anda juga dapat melihat hasil proses dengan membuka ekstensi alur prompt dan memilih proses terakhir, seperti yang ditunjukkan pada gambar 9.23. Kemudian, Anda dapat menelusuri setiap proses dengan mengklik sel tabel. Banyak informasi yang diekspos dalam dialog ini, yang dapat membantu Anda memecahkan masalah alur dan profil.

![gambar](Images/9-23.png)

**Gambar 9.23** Membuka visualisasi proses dan memeriksa proses batch

Banyak informasi yang ditangkap selama proses batch, dan Anda dapat menjelajahi sebagian besarnya melalui visualizer. Informasi lebih lanjut dapat ditemukan dengan mengklik tautan folder output dari jendela terminal. Ini akan membuka sesi VS Code lain dengan folder output yang memungkinkan Anda meninjau log proses dan detail lainnya.

Sekarang setelah kami menyelesaikan proses batch untuk setiap varian, kami dapat menerapkan landasan dan mengevaluasi hasil dari kedua prompt. Bagian selanjutnya akan menggunakan alur baru untuk melakukan evaluasi profil/prompt.

### 9.7.3 Membuat alur evaluasi untuk landasan

Buka `chapter_3\prompt_flow\evaluate_groundings\flow.dag.yaml` di editor visual, seperti yang ditunjukkan pada gambar 9.24. Tidak ada blok LLM dalam alur evaluasi—hanya blok kode Python yang akan menjalankan penilaian dan kemudian menggabungkan skor.

![gambar](Images/9-24.png)

**Gambar 9.24** Melihat alur `evaluate_groundings` yang digunakan untuk mendasarkan proses rekomendasi

Sekarang kita dapat melihat kode untuk blok `penilaian` dan `agregat`, dimulai dengan kode penilaian dalam daftar 9.3. Kode penilaian ini merata-ratakan skor untuk setiap kriteria menjadi skor rata-rata. Output dari fungsi ini adalah daftar rekomendasi yang diproses.

**Daftar 9.3** `line_process.py`

```python
@tool
def line_process(recommendations: str):
    inputs = recommendations
    output = []
    for data_dict in inputs:                     #1
        total_score = 0
        score_count = 0

        for key, value in data_dict.items():     #2
                if key != "title":    #3
                    try:
                        total_score += float(value)
                        score_count += 1
                        data_dict[key] = float(value)    #4
                    except:
                        pass

        avg_score = total_score / score_count if score_count > 0 else 0

        data_dict["avg_score"] = round(avg_score, 2)   #5
        output.append(data_dict)

    return output
```

1. Satu set tiga rekomendasi dimasukkan ke dalam fungsi.
2. Melakukan loop pada setiap rekomendasi dan kriteria
3. Judul bukan kriteria, jadi abaikan.
4. Menjumlahkan skor untuk semua kriteria dan mengatur nilai float ke kunci
5. Menambahkan skor rata-rata sebagai skor landasan dari rekomendasi

Dari rekomendasi yang didasarkan, kita dapat melanjutkan ke agregasi skor dengan blok `agregat`—kode untuk blok `agregat` ditunjukkan dalam daftar berikut.

**Daftar 9.4** `aggregate.py`

```python
@tool
def aggregate(processed_results: List[str]):
    items = [item for sublist in processed_results 
              for item in sublist]    #1

    aggregated = {}

    for item in items:
        for key, value in item.items():
            if key == 'title':
                continue

            if isinstance(value, (float, int)):     #2
                if key in aggregated:
                    aggregated[key] += value
                else:
                    aggregated[key] = value

    for key, value in aggregated.items():     #3
        value = value / len(items)
        log_metric(key=key, value=value)    #4
        aggregated[key] = value

    return aggregated
```

1. Inputnya adalah daftar daftar; ratakan menjadi daftar item.
2. Memeriksa untuk melihat apakah nilainya numerik dan mengakumulasi skor untuk setiap kunci kriteria
3. Melakukan loop pada skor kriteria yang diagregasi
4. Mencatat kriteria sebagai metrik

Hasil dari agregasi akan menjadi skor ringkasan untuk setiap kriteria dan skor rata-rata. Karena alur evaluasi/landasan terpisah, alur ini dapat dijalankan pada setiap proses rekomendasi yang kami lakukan. Ini akan memungkinkan kami untuk menggunakan hasil proses batch untuk variasi apa pun untuk membandingkan hasil.

Kita dapat menjalankan alur landasan dengan membuka `flow.dag.yaml` di editor visual dan mengklik Batch (ikon gelas kimia). Kemudian, saat diminta, kami memilih proses yang ada dan kemudian memilih proses yang ingin kami evaluasi, seperti yang ditunjukkan pada gambar 9.25. Ini akan membuka file YAML dengan tautan Jalankan di bagian bawah, seperti yang telah kita lihat sebelumnya. Klik tautan Jalankan untuk menjalankan evaluasi.

![gambar](Images/9-25.png)

**Gambar 9.25** Memuat proses sebelumnya untuk didasarkan dan dievaluasi

Setelah proses selesai, Anda akan melihat ringkasan hasil di jendela terminal. Anda dapat mengklik tautan output untuk membuka folder di VS Code dan menganalisis hasilnya, tetapi ada cara yang lebih baik untuk membandingkannya.

Buka ekstensi alur prompt, fokus pada jendela Riwayat Proses Batch, dan gulir ke bawah ke bagian Jalankan terhadap Jalankan, seperti yang ditunjukkan pada gambar 9.26. Pilih proses yang ingin Anda bandingkan—kemungkinan yang berada di dekat bagian atas—sehingga tanda centang muncul. Kemudian, klik kanan proses, dan pilih opsi Visualisasikan Proses. Jendela Visualisasi Proses Batch terbuka, dan Anda akan melihat metrik untuk setiap proses di bagian atas.

![gambar](Images/9-26.png)

**Gambar 9.26** Memvisualisasikan metrik untuk beberapa proses dan membandingkannya

Kita sekarang dapat melihat perbedaan yang signifikan antara variasi profil/prompt 0, prompt pengguna, dan variasi 1, prompt sistem. Lihat gambar 9.15 jika Anda memerlukan penyegaran tentang seperti apa tampilan prompt/profil. Pada titik ini, harus jelas bahwa menyuntikkan parameter input ke dalam prompt sistem memberikan rekomendasi yang lebih baik.

Anda sekarang dapat kembali dan mencoba profil lain atau opsi varian lain untuk melihat pengaruhnya terhadap rekomendasi Anda. Kemungkinannya hampir tak terbatas, tetapi semoga Anda dapat melihat betapa hebatnya alat alur prompt untuk membangun profil dan prompt agen.

### 9.7.4 Latihan

Gunakan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- *Latihan 1* —Buat Varian Prompt Baru untuk Alur Pemberi Rekomendasi (Menengah)

    *Tujuan* —Meningkatkan hasil rekomendasi dengan membuat dan menguji varian prompt baru di alur prompt.

    *Tugas:*

    - Buat varian prompt baru untuk alur pemberi rekomendasi di alur prompt.
    - Jalankan alur dalam mode batch.
    - Evaluasi hasilnya untuk menentukan apakah lebih baik atau lebih buruk dibandingkan dengan prompt asli.

- *Latihan 2* —Tambahkan Bidang Kustom ke Rubrik dan Evaluasi (Menengah)

    *Tujuan* —Meningkatkan kriteria evaluasi dengan memasukkan bidang kustom ke dalam rubrik dan memperbarui alur evaluasi.

    *Tugas:*

    - Tambahkan bidang kustom sebagai kriteria baru ke rubrik.
    - Perbarui alur evaluasi untuk menilai kriteria baru.
    - Evaluasi hasilnya, dan analisis pengaruh kriteria baru pada evaluasi.

- *Latihan 3* —Kembangkan Kasus Penggunaan Baru dan Rubrik Evaluasi (Lanjutan)

    *Tujuan* —Memperluas penerapan rekayasa prompt dengan mengembangkan kasus penggunaan baru dan membuat rubrik evaluasi.

    *Tugas:*

    - Kembangkan kasus penggunaan baru selain dari rekomendasi.
    - Bangun prompt untuk kasus penggunaan baru.
    - Buat rubrik untuk mengevaluasi prompt baru.
    - Perbarui atau ubah alur evaluasi untuk menggabungkan dan membandingkan hasil kasus penggunaan baru dengan yang sudah ada.

- *Latihan 4* —Evaluasi LLM Lain Menggunakan LM Studio (Menengah)

    *Tujuan* —Menilai kinerja LLM sumber terbuka yang berbeda dengan menghosting server lokal dengan LM Studio.

    *Tugas:*

    - Gunakan LM Studio untuk menghosting server lokal untuk mengevaluasi LLM.
    - Evaluasi LLM sumber terbuka lainnya.
    - Konsultasikan bab 2 jika bantuan diperlukan untuk menyiapkan server dan melakukan evaluasi.

- *Latihan 5* —Bangun dan Evaluasi Prompt Menggunakan Alur Prompt (Menengah)

    *Tujuan* —Menerapkan strategi rekayasa prompt untuk membangun dan mengevaluasi prompt atau profil baru menggunakan alur prompt.

    *Tugas:*

    - Bangun prompt atau profil baru untuk evaluasi menggunakan alur prompt.
    - Terapkan strategi rekayasa prompt Tulis Instruksi yang Jelas dari bab 2.
    - Evaluasi prompt dan profil menggunakan alur prompt.
    - Lihat bab 2 untuk taktik dan detail implementasi jika diperlukan penyegaran.

## Ringkasan

- Profil agen terdiri dari beberapa prompt komponen lain yang dapat mendorong fungsi seperti tindakan/alat, pengetahuan, memori, evaluasi, penalaran, umpan balik, dan perencanaan.
- Alur prompt dapat digunakan untuk mengevaluasi prompt komponen agen.
- Rekayasa prompt sistemik adalah proses berulang yang mengevaluasi profil prompt dan agen.
- Strategi Uji Perubahan Secara Sistematis menjelaskan iterasi dan evaluasi prompt, dan rekayasa prompt sistem mengimplementasikan strategi ini.
- Profil agen dan rekayasa prompt memiliki banyak kesamaan. Kami mendefinisikan profil agen sebagai kombinasi elemen rekayasa prompt yang memandu dan membantu agen melalui tugasnya.
- Alur prompt adalah alat sumber terbuka dari Microsoft yang menyediakan beberapa fitur untuk mengembangkan dan mengevaluasi profil dan prompt.
- Koneksi LLM dalam alur prompt mendukung parameter tambahan, termasuk suhu, token berhenti, token maks, dan parameter lanjutan lainnya.
- Blok LLM mendukung varian prompt dan profil, yang memungkinkan untuk mengevaluasi perubahan pada prompt/profil atau parameter koneksi lainnya.
- Rubrik yang diterapkan pada prompt LLM adalah kriteria dan standar yang harus dipenuhi oleh prompt/profil agar dapat didasarkan. Landasan adalah penilaian dan evaluasi rubrik.
- Alur prompt mendukung menjalankan beberapa variasi sebagai proses tunggal atau proses batch.
- Dalam alur prompt, alur evaluasi dijalankan setelah alur generatif untuk menilai dan menggabungkan hasilnya. Opsi Visualisasikan Proses dapat membandingkan kriteria gabungan dari penilaian rubrik di beberapa proses.
