# Penalaran dan evaluasi agen

## Bab ini mencakup
- Menggunakan berbagai teknik rekayasa prompt untuk memperluas fungsi model bahasa besar
- Melibatkan model bahasa besar dengan teknik rekayasa prompt yang melibatkan penalaran
- Menggunakan prompt evaluasi untuk mempersempit dan mengidentifikasi solusi untuk masalah yang tidak diketahui

Sekarang setelah kita memeriksa pola memori dan pengambilan yang mendefinisikan komponen memori semantik dalam agen, kita dapat melihat komponen terakhir dan paling instrumental dalam agen: perencanaan. Perencanaan mencakup banyak aspek, mulai dari penalaran, pemahaman, dan evaluasi hingga umpan balik.

Untuk mengeksplorasi bagaimana LLM dapat diminta untuk bernalar, memahami, dan merencanakan, kami akan mendemonstrasikan cara melibatkan penalaran melalui rekayasa prompt dan kemudian mengembangkannya ke perencanaan. Solusi perencanaan yang disediakan oleh Semantic Kernel (SK) mencakup berbagai bentuk perencanaan. Kami akan menyelesaikan bab ini dengan memasukkan umpan balik adaptif ke dalam perencana baru.

Gambar 10.1 menunjukkan strategi rekayasa prompt tingkat tinggi yang akan kita bahas dalam bab ini dan bagaimana kaitannya dengan berbagai teknik yang akan kita bahas. Setiap metode yang ditampilkan dalam gambar akan dieksplorasi dalam bab ini, dari dasar-dasar solusi/prompting langsung, yang ditunjukkan di sudut kiri atas, hingga konsistensi diri dan tree of thought (ToT), di kanan bawah.

![Gambar 10.1](Images/10-1.png)

**Gambar 10.1** Bagaimana dua strategi rekayasa prompt perencanaan selaras dengan berbagai teknik

## Memahami prompting solusi langsung

*Prompting solusi langsung* umumnya merupakan bentuk pertama dari rekayasa prompt yang digunakan pengguna saat mengajukan pertanyaan kepada LLM atau memecahkan masalah tertentu. Mengingat penggunaan LLM apa pun, teknik-teknik ini mungkin tampak jelas, tetapi ada baiknya ditinjau untuk membangun fondasi pemikiran dan perencanaan. Di bagian selanjutnya, kita akan mulai dari awal, mengajukan pertanyaan dan mengharapkan jawaban.

### Prompting tanya jawab

Untuk latihan di bab ini, kita akan menggunakan alur prompt untuk membangun dan mengevaluasi berbagai teknik. (Kami telah membahas alat ini secara ekstensif di bab 9, jadi lihat bab itu jika Anda memerlukan ulasan.) Alur prompt adalah alat yang sangat baik untuk memahami cara kerja teknik ini dan menjelajahi alur proses perencanaan dan penalaran.

Buka Visual Studio Code (VS Code) ke folder sumber `bab` `10`. Buat lingkungan virtual baru untuk folder tersebut, dan instal file `requirements.txt`. Jika Anda memerlukan bantuan untuk menyiapkan lingkungan Python suatu bab, lihat apendiks B.

Kita akan melihat alur pertama di folder `prompt_flow/question-answering-prompting`. Buka file `flow.dag.yaml` di editor visual, seperti yang ditunjukkan pada gambar 10.2. Di sisi kanan, Anda akan melihat alur komponen. Di bagian atas adalah prompt LLM `question_answer`, diikuti oleh dua komponen `Embedding` dan prompt LLM terakhir untuk melakukan evaluasi yang disebut `evaluate`.

![Gambar 10.2](Images/10-2.png)

**Gambar 10.2** File `flow.dag.yaml`, terbuka di editor visual, menyoroti berbagai komponen alur

Rincian dalam daftar 10.1 menunjukkan struktur dan komponen alur secara lebih rinci menggunakan semacam pseudocode yang dipersingkat YAML. Anda juga dapat melihat input dan output ke berbagai komponen dan contoh output dari menjalankan alur.

**Daftar 10.1** alur `question-answer-prompting`

```
   Input:
       konteks  : konten untuk ditanyakan pertanyaannya
       pertanyaan : pertanyaan yang diajukan khusus untuk konten tersebut
       diharapkan : jawaban yang diharapkan

   LLM: Tanya-Jawab (prompt yang digunakan untuk mengajukan pertanyaan)
       input:
              konteks dan pertanyaan
       output: 
              prediksi/jawaban atas pertanyaan

   Embedding: menggunakan model embedding LLM untuk membuat representasi
 embedding dari teks

      Embedding_predicted: menyematkan output dari LLM Tanya-Jawab
      Embedding_expected: menyematkan output dari jawaban yang diharapkan

   Python: Evaluasi (kode Python untuk mengukur kesamaan embedding)
      Input:
             Output Embedding_predicted
             Output Embedding_expected
      Output: 
             skor kesamaan antara yang diprediksi dan yang diharapkan

   Output:
       konteks: -> input.konteks
       pertanyaan: -> input.pertanyaan
    diharapkan: -> input.diharapkan
    diprediksi: -> output.tanya_jawab
    skor_evaluasi: output.evaluasi

### Contoh Output
{
    "konteks": "Back to the Future (1985)…",
    "skor_evaluasi": 0.9567478002354606,
    "diharapkan": "Marty melakukan perjalanan kembali ke masa lalu selama 30 tahun.",
    "diprediksi": "Marty melakukan perjalanan kembali ke masa lalu selama 30 tahun dari tahun 1985 hingga 1955 
 dalam film "Back to the Future."",
    "pertanyaan": "Seberapa jauh Marty melakukan perjalanan kembali ke masa lalu dalam film 
 Back to the Future (1985)"
}
```

Sebelum menjalankan alur ini, pastikan blok LLM Anda dikonfigurasi dengan benar. Ini mungkin mengharuskan Anda untuk mengatur koneksi ke LLM pilihan Anda. Sekali lagi, lihat bab 9 jika Anda memerlukan ulasan tentang cara menyelesaikan ini. Anda harus mengonfigurasi blok LLM dan `Embedding` dengan koneksi Anda jika Anda tidak menggunakan OpenAI.

Setelah mengonfigurasi koneksi LLM Anda, jalankan alur dengan mengeklik tombol Putar dari editor visual atau menggunakan tautan Uji (Shift-F5) di jendela editor YAML. Jika semuanya terhubung dan dikonfigurasi dengan benar, Anda akan melihat output seperti pada daftar 10.1.

Buka file `question_answer.jinja2` di VS Code, seperti yang ditunjukkan pada daftar 10.2. Daftar ini menunjukkan prompt gaya tanya jawab dasar. Dalam gaya prompt ini, pesan sistem menjelaskan aturan dasar dan menyediakan konteks untuk menjawab pertanyaan. Di bab 4, kita menjelajahi pola retrieval augmented generation (RAG), dan prompt ini mengikuti pola yang serupa.

**Daftar 10.2** `question_answer.jinja2`

```
sistem:
Jawab pertanyaan pengguna berdasarkan konteks di bawah ini. Jaga agar jawabannya 
 singkat dan padat. Tanggapi "Tidak yakin tentang jawaban" jika tidak yakin dengan 
 jawabannya.

Konteks: {{konteks}}    #1

pengguna:
Pertanyaan: {{pertanyaan}}    #2

#1 Ganti dengan konten yang harus dijawab LLM tentang pertanyaan tersebut.
#2 Ganti dengan pertanyaan.
```

Latihan ini menunjukkan metode sederhana menggunakan LLM untuk mengajukan pertanyaan tentang sepotong konten. Kemudian, respons pertanyaan dievaluasi menggunakan skor pencocokan kesamaan. Kita dapat melihat dari output pada daftar 10.1 bahwa LLM melakukan pekerjaan yang baik dalam menjawab pertanyaan tentang konteks. Di bagian selanjutnya, kita akan menjelajahi teknik serupa yang menggunakan prompting langsung.

### Menerapkan few-shot prompting

*Few-shot prompting* seperti prompting tanya jawab, tetapi susunan prompt lebih tentang memberikan beberapa contoh daripada tentang fakta atau konteks. Hal ini memungkinkan LLM untuk membengkokkan pola atau konten yang belum pernah dilihat sebelumnya. Meskipun pendekatan ini terdengar seperti tanya jawab, implementasinya sangat berbeda, dan hasilnya bisa sangat kuat.

> **Zero-shot, one-shot, dan few-shot learning**
>
> Salah satu cawan suci dari pembelajaran mesin dan AI adalah kemampuan untuk melatih model pada item sesedikit mungkin. Misalnya, dalam model visi tradisional, jutaan gambar dimasukkan ke dalam model untuk membantu mengidentifikasi perbedaan antara kucing dan anjing.
>
> Model *one-shot* adalah model yang hanya memerlukan satu gambar untuk melatihnya. Misalnya, gambar kucing dapat ditampilkan, dan kemudian model dapat mengidentifikasi gambar kucing apa pun. Model *few-shot* hanya memerlukan beberapa hal untuk melatih model. Dan, tentu saja, *zero-shot* menunjukkan kemampuan untuk mengidentifikasi sesuatu tanpa contoh sebelumnya. LLM adalah pembelajar yang efisien dan dapat melakukan ketiga jenis pembelajaran tersebut.

Buka `prompt_flow/few-shot-prompting/flow.dag.yaml` di VS Code dan editor visual. Sebagian besar alur terlihat seperti yang digambarkan sebelumnya pada gambar 10.2, dan perbedaannya disorot dalam daftar 10.3, yang menunjukkan representasi pseudocode YAML. Perbedaan utama antara ini dan alur sebelumnya adalah input dan prompt LLM.

**Daftar 10.3** alur `few-shot-prompting`

```
   Input:
      pernyataan  : memperkenalkan konteks dan kemudian meminta output
      diharapkan : jawaban yang diharapkan untuk pernyataan tersebut
   LLM: few_shot (prompt yang digunakan untuk mengajukan pertanyaan)
      input:pernyataan
      output: prediksi/jawaban atas pernyataan tersebut

   Embedding: menggunakan model embedding LLM untuk membuat representasi
 embedding dari teks

      Embedding_predicted: menyematkan output dari LLM few_shot
      Embedding_expected: menyematkan output dari jawaban yang diharapkan

   Python: Evaluasi (kode Python untuk mengukur kesamaan embedding)
      Input:
             Output Embedding_predicted
             Output Embedding_expected
      Output: skor kesamaan antara yang diprediksi dan yang diharapkan

Output:
      pernyataan: -> input.pernyataan
      diharapkan: -> input.diharapkan
      diprediksi: -> output.few_shot
      skor_evaluasi: output.evaluasi

### Contoh Output
{
    "skor_evaluasi": 0.906647282920417,    #1
    "diharapkan": "Kami makan sunner dan menyaksikan matahari terbenam.",
    "diprediksi": "Setelah pendakian yang panjang, kami duduk di tepi danau 
 dan menikmati sunner yang damai saat langit berubah menjadi 
 warna oranye dan merah muda yang cemerlang.",    #2
    "pernyataan": "Sunner adalah makanan yang kami makan di Cananda 
 saat matahari terbenam, silakan gunakan kata itu dalam sebuah kalimat"    #3
}

#1 Skor evaluasi mewakili kesamaan antara yang diharapkan dan yang diprediksi.
#2 Menggunakan sunner dalam sebuah kalimat
#3 Ini adalah pernyataan yang salah tetapi tujuannya adalah untuk membuat LLM menggunakan kata tersebut seolah-olah itu nyata.
```

Jalankan alur dengan menekan Shift-F5 atau mengeklik tombol Putar/Uji dari editor visual. Anda akan melihat output seperti daftar 10.3 di mana LLM telah menggunakan kata *sunner* (istilah yang dibuat-buat) dengan benar dalam sebuah kalimat berdasarkan pernyataan awal.

Latihan ini menunjukkan kemampuan untuk menggunakan prompt untuk mengubah perilaku LLM agar bertentangan dengan apa yang telah dipelajarinya. Kami mengubah apa yang dipahami LLM sebagai akurat. Selanjutnya, kami kemudian menggunakan perspektif yang dimodifikasi itu untuk memunculkan penggunaan kata yang dibuat-buat.

Buka prompt `few_shot.jinja2` di VS Code, yang ditunjukkan pada daftar 10.4. Daftar ini menunjukkan pengaturan persona sederhana, yaitu pembuat kamus eksentrik, dan kemudian memberikan contoh kata-kata yang telah didefinisikan dan digunakan sebelumnya. Dasar dari prompt memungkinkan LLM untuk memperluas contoh dan menghasilkan hasil yang serupa menggunakan kata-kata lain.

**Daftar 10.4** `few_shot.jinja2`

```
sistem:
Anda adalah pembuat kamus kata yang eksentrik. Anda akan diminta untuk 

membangun sebuah kalimat menggunakan kata tersebut.
Berikut ini adalah contoh-contoh yang menunjukkan cara membuat kalimat menggunakan 
 kata tersebut.
"whatpu" adalah hewan kecil berbulu yang berasal dari Tanzania. 
Contoh kalimat yang menggunakan kata whatpu adalah:    #1
Kami sedang bepergian di Afrika dan kami melihat whatpus yang sangat lucu ini.
Melakukan "farduddle" berarti melompat-lompat dengan sangat cepat. Contoh 
 kalimat yang menggunakan kata farduddle adalah:
Saya sangat bersemangat sehingga saya mulai farduddle.    #2

Harap hanya kembalikan kalimat yang diminta oleh pengguna.  #3

pengguna:
{{pernyataan}}   #4

#1 Menunjukkan contoh yang mendefinisikan kata yang dibuat-buat dan menggunakannya dalam sebuah kalimat
#2 Menunjukkan contoh lain
#3 Aturan untuk mencegah LLM mengeluarkan informasi tambahan
#4 Pernyataan input mendefinisikan kata baru dan meminta penggunaannya.
```

Anda mungkin mengatakan kami memaksa LLM untuk berhalusinasi di sini, tetapi teknik ini adalah dasar untuk memodifikasi perilaku. Ini memungkinkan prompt untuk dibangun untuk memandu LLM untuk melakukan segala sesuatu yang bertentangan dengan apa yang dipelajarinya. Fondasi prompting ini juga menetapkan teknik untuk bentuk perilaku lain yang diubah. Dari kemampuan untuk mengubah persepsi dan latar belakang LLM, kita akan beralih untuk mendemonstrasikan contoh terakhir dari solusi langsung di bagian selanjutnya.

### Mengekstrak generalitas dengan zero-shot prompting

*Zero-shot prompting atau learning* adalah kemampuan untuk menghasilkan prompt sedemikian rupa sehingga memungkinkan LLM untuk menggeneralisasi. Generalisasi ini tertanam dalam LLM dan ditunjukkan melalui zero-shot prompting, di mana tidak ada contoh yang diberikan, tetapi sebaliknya seperangkat pedoman atau aturan diberikan untuk memandu LLM.

Menggunakan teknik ini sederhana dan bekerja dengan baik untuk memandu LLM untuk menghasilkan balasan berdasarkan pengetahuan internalnya dan tidak ada konteks lain. Ini adalah teknik yang halus namun kuat yang menerapkan pengetahuan LLM ke aplikasi lain. Teknik ini, dikombinasikan dengan strategi prompting lainnya, terbukti efektif dalam menggantikan model klasifikasi bahasa lain—model yang mengidentifikasi emosi atau sentimen dalam teks, misalnya.

Buka `prompt_flow/zero-shot-prompting/flow.dag.yaml` di editor visual alur prompt VS Code. Alur ini lagi-lagi hampir identik dengan yang ditunjukkan sebelumnya pada gambar 10.1 tetapi sedikit berbeda dalam implementasi, seperti yang ditunjukkan pada daftar 10.5.

**Daftar 10.5** alur `zero-shot-prompting`

```
   Input:
       pernyataan  : pernyataan yang akan diklasifikasikan
       diharapkan : klasifikasi yang diharapkan dari pernyataan tersebut

   LLM: zero_shot (prompt yang digunakan untuk mengklasifikasikan)
       input: pernyataan
       output: kelas yang diprediksi berdasarkan pernyataan

   Embedding: menggunakan model embedding LLM untuk membuat representasi
 embedding dari teks

   Embedding_predicted: menyematkan output dari LLM zero_shot
   Embedding_expected: menyematkan output dari jawaban yang diharapkan

   Python: Evaluasi (kode Python untuk mengukur kesamaan embedding)
       Input:
              Output Embedding_predicted
            Output Embedding_expected
         Output: skor kesamaan antara yang diprediksi dan yang diharapkan

   Output:
       pernyataan: -> input.pernyataan
       diharapkan: -> input.diharapkan
       diprediksi: -> output.few_shot
       skor_evaluasi: output.evaluasi

   ### Contoh Output
{
       "skor_evaluasi": 1,    #1
       "diharapkan": "netral",
       "diprediksi": "netral",
       "pernyataan": "Saya pikir liburannya baik-baik saja. "    #2
   }

#1 Menunjukkan skor evaluasi sempurna 1.0
#2 Pernyataan yang kami minta untuk diklasifikasikan oleh LLM
```

Jalankan alur dengan menekan Shift-F5 di dalam editor visual alur prompt VS Code. Anda akan melihat output yang mirip dengan yang ditunjukkan pada daftar 10.5.

Sekarang buka prompt `zero_shot.jinja2` seperti yang ditunjukkan pada daftar 10.6. Promptnya sederhana dan tidak menggunakan contoh untuk mengekstrak sentimen dari teks. Yang menarik untuk dicatat adalah bahwa prompt tersebut bahkan tidak menyebutkan frasa sentimen, dan LLM tampaknya memahami maksudnya.

**Daftar 10.6** `zero_shot.jinja2`

```
sistem:
Klasifikasikan teks menjadi netral, negatif, atau positif. 
Hanya kembalikan hasilnya dan tidak ada yang lain.    #1

pengguna:
{{pernyataan}}    #2

#1 Memberikan panduan penting tentang cara melakukan klasifikasi
#2 Pernyataan teks yang akan diklasifikasikan
```

Rekayasa prompt zero-shot adalah tentang menggunakan kemampuan LLM untuk menggeneralisasi secara luas berdasarkan materi pelatihannya. Latihan ini menunjukkan bagaimana pengetahuan dalam LLM dapat digunakan untuk tugas-tugas lain. Kemampuan LLM untuk mengontekstualisasikan diri dan menerapkan pengetahuan dapat melampaui pelatihannya. Di bagian selanjutnya, kita memperluas konsep ini lebih jauh dengan melihat bagaimana LLM dapat bernalar.

## Penalaran dalam rekayasa prompt

LLM seperti ChatGPT dikembangkan untuk berfungsi sebagai model penyelesaian obrolan, di mana konten teks dimasukkan ke dalam model, yang responsnya selaras dengan menyelesaikan permintaan itu. LLM tidak pernah dilatih untuk bernalar, merencanakan, berpikir, atau memiliki pemikiran.

Namun, seperti yang kami tunjukkan dengan contoh-contoh di bagian sebelumnya, LLM dapat diminta untuk mengekstrak generalitasnya dan diperluas di luar desain awalnya. Meskipun LLM tidak dirancang untuk bernalar, materi pelatihan yang dimasukkan ke dalam model memberikan pemahaman tentang penalaran, perencanaan, dan pemikiran. Oleh karena itu, secara ekstensi, LLM memahami apa itu penalaran dan dapat menggunakan konsep penalaran.

> **Penalaran dan perencanaan**
>
> *Penalaran* adalah kemampuan intelek, buatan atau tidak, untuk memahami proses berpikir atau memikirkan suatu masalah. Sebuah intelek dapat memahami bahwa tindakan memiliki hasil, dan dapat menggunakan kemampuan ini untuk menalar tindakan mana dari serangkaian tindakan yang dapat diterapkan untuk menyelesaikan tugas tertentu.
>
> *Perencanaan* adalah kemampuan intelek untuk menalar urutan tindakan atau tugas dan menerapkan parameter yang benar untuk mencapai tujuan atau hasil—sejauh mana rencana intelektual bergantung pada ruang lingkup masalah. Sebuah intelek dapat menggabungkan beberapa tingkat perencanaan, dari strategis dan taktis hingga operasional dan kontingen.

Kita akan melihat serangkaian teknik rekayasa prompt lain yang memungkinkan atau meniru perilaku penalaran untuk menunjukkan kemampuan penalaran ini. Biasanya, ketika mengevaluasi penerapan penalaran, kita melihat agar LLM memecahkan masalah-masalah menantang yang tidak dirancang untuk dipecahkannya. Sumber yang baik untuk itu didasarkan pada logika, matematika, dan soal cerita.

Menggunakan tema perjalanan waktu, kelas masalah unik apa yang bisa lebih baik untuk dipecahkan daripada memahami perjalanan waktu? Gambar 10.3 menggambarkan salah satu contoh masalah perjalanan waktu yang unik dan menantang. Tujuan kami adalah untuk memperoleh kemampuan untuk mendorong LLM dengan cara yang memungkinkannya untuk memecahkan masalah dengan benar.

![Gambar 10.3](Images/10-3.png)

**Gambar 10.3** Kompleksitas masalah perjalanan waktu yang ingin kami selesaikan menggunakan LLM dengan penalaran dan perencanaan

Masalah perjalanan waktu adalah latihan berpikir yang bisa jadi sangat sulit untuk dipecahkan. Contoh pada gambar 10.3 rumit untuk dipecahkan oleh LLM, tetapi bagian yang salah mungkin akan mengejutkan Anda. Bagian selanjutnya akan menggunakan penalaran dalam prompt untuk memecahkan masalah unik ini.

### Chain of thought prompting

*Chain of thought* (CoT) prompting adalah teknik rekayasa prompt yang menggunakan contoh one-shot atau few-shot yang menjelaskan penalaran dan langkah-langkah untuk mencapai tujuan yang diinginkan. Melalui demonstrasi penalaran, LLM dapat menggeneralisasi prinsip ini dan menalar melalui masalah dan tujuan yang serupa. Meskipun LLM tidak dilatih dengan tujuan penalaran, kita dapat memunculkan model untuk bernalar, menggunakan rekayasa prompt.

Buka `prompt_flow/chain-of-thought-prompting/flow.dag.yaml` di editor visual alur prompt VS Code. Elemen-elemen alur ini sederhana, seperti yang ditunjukkan pada gambar 10.4. Dengan hanya dua blok LLM, alur pertama menggunakan prompt CoT untuk menyelesaikan pertanyaan yang kompleks; kemudian, prompt LLM kedua mengevaluasi jawabannya.

![Gambar 10.4](Images/10-4.png)

**Gambar 10.4** Alur CoT

Daftar 10.7 menunjukkan pseudocode YAML yang menjelaskan blok dan input/output alur secara lebih rinci. Pernyataan masalah default dalam contoh ini tidak sama dengan pada gambar 10.3.

**Daftar 10.7** alur `chain-of-thought-prompting`

```
   Input:
       pernyataan  : masalah pernyataan yang harus dipecahkan
       diharapkan : solusi yang diharapkan untuk masalah tersebut

   LLM: cot (prompt yang digunakan untuk memecahkan masalah)
       input: pernyataan
       output: jawaban yang diprediksi berdasarkan pernyataan masalah

   LLM: evaluate_answer (prompt yang digunakan untuk mengevaluasi solusi)
       input:
              pernyataan: -> input.pernyataan
              diharapkan: -> input.diharapkan
              diprediksi: -> output.cot

       output: skor seberapa baik masalah itu dijawab


   Output:
       pernyataan: -> input.pernyataan
       diharapkan: -> input.diharapkan
       diprediksi: -> output.cot
       skor_evaluasi: output.evaluate_answer

   ### Contoh Output
{
    "skor_evaluasi": "0.5",    #1
    "diharapkan": "Setelah lompatan terakhir, Max menemukan dirinya 
 di tahun 1980 dan dia berusia 75 tahun.",    #2
    "diprediksi": " Max mulai pada tahun 2300 dan 
 melakukan perjalanan mundur dalam peningkatan 40 tahun, menghabiskan 5 tahun 
 di setiap periode. Perjalanannya akan sebagai berikut:


- Dari 2300 hingga 2260: Max berusia 25 + 5 = 30 tahun.

- Dari 2260 hingga 2220: Max berusia 30 + 5 = 35 tahun.

- Dari 2220 hingga 2180: Max berusia 35 + 5 = 40 tahun.

- Dari 2180 hingga 2140: Max berusia 40 + 5 = 45 tahun.

- Dari 2140 hingga 2100: Max berusia 45 + 5 = 50 tahun.

- Dari 2100 hingga 2060: Max berusia 50 + 5 = 55 tahun.

- Dari 2060 hingga 2020: Max berusia 55 + 5 = 60 tahun.

- Dari 2020 hingga 1980: Max berusia 60 + 5 = 65 tahun.

- Dari 1980 hingga 1940: Max berusia 65 + 5 = 70 tahun.

- Dari 1940 hingga 1900: Max berusia 70 + 5"    #3
}

#1 Skor yang dievaluasi untuk solusi yang diberikan
#2 Jawaban yang diharapkan untuk masalah tersebut
#3 Jawaban yang diprediksi menunjukkan langkah-langkah penalaran dan output.
```

Gali input dan periksa pernyataan masalah; coba evaluasi masalahnya sendiri. Kemudian, jalankan alur dengan menekan Shift-F5. Anda akan melihat output yang mirip dengan yang ditunjukkan pada daftar 10.7.

Buka file prompt `cot.jinja2` seperti yang ditunjukkan pada daftar 10.8. Prompt ini memberikan beberapa contoh masalah perjalanan waktu dan kemudian solusi yang dipikirkan dan dinalar. Proses menunjukkan kepada LLM langkah-langkah untuk menyelesaikan masalah memberikan mekanisme penalaran.

**Daftar 10.8** `cot.jinja2` 

```
sistem:
"Dalam sebuah film perjalanan waktu, Sarah melakukan perjalanan kembali ke masa lalu untuk 
 mencegah peristiwa bersejarah terjadi. Dia tiba 
 2 hari sebelum acara tersebut. Setelah menghabiskan satu hari untuk persiapan, 
 dia mencoba untuk mengubah acara tersebut tetapi menyadari bahwa dia sebenarnya 
 telah tiba 2 tahun lebih awal, bukan 2 hari. Dia kemudian 
 memutuskan untuk menunggu dan tinggal di masa lalu sampai tanggal 
 asli acara tersebut. Berapa hari yang dihabiskan Sarah di masa lalu 
 sebelum hari acara tersebut?"    #1

Rantai Pemikiran:    #2

    Asumsi Awal: Sarah mengira dia telah tiba 2 hari sebelum acara.
    Waktu yang Dihabiskan untuk Persiapan: 1 hari dihabiskan untuk persiapan.
    Realisasi Kesalahan: Sarah menyadari bahwa dia sebenarnya 2 tahun lebih awal.
    Konversi Tahun ke Hari: 
2 tahun = 2 × 365 = 730 hari (dengan asumsi bukan tahun kabisat).
    Sesuaikan dengan Hari yang Dihabiskan untuk Persiapan: 730 - 1 = 729 hari.
    Kesimpulan: Sarah menghabiskan 729 hari di masa lalu sebelum hari acara tersebut.

"Dalam sebuah film fiksi ilmiah, Alex adalah seorang penjelajah waktu yang memutuskan 
 untuk kembali ke masa lalu untuk menyaksikan pertempuran bersejarah yang terkenal 
 yang terjadi 100 tahun yang lalu, yang berlangsung selama 10 hari. 
 Dia tiba tiga hari sebelum pertempuran dimulai. Namun, 
 setelah menghabiskan enam hari di masa lalu, dia melompat maju dalam 
 waktu 50 tahun dan tinggal di sana selama 20 hari. Kemudian, dia 
 melakukan perjalanan kembali untuk menyaksikan akhir pertempuran. Berapa 
 hari yang dihabiskan Alex di masa lalu sebelum dia melihat akhir 
  pertempuran?"    #3

Rantai Pemikiran:    #4

    Perjalanan Awal: Alex tiba tiga hari sebelum pertempuran dimulai.
    Waktu yang Dihabiskan Sebelum Lompatan Waktu: Alex menghabiskan enam hari di masa lalu. 
Pertempuran telah dimulai dan telah berlangsung selama 3 hari (karena dia 
 tiba 3 hari lebih awal dan sekarang telah menghabiskan 6 hari, 3 + 3 = 6).
    Lompatan Waktu Pertama: Alex melompat 50 tahun ke depan dan tinggal selama 20 hari.
 Ini menambahkan 20 hari ke 6 hari yang telah dia habiskan di masa lalu 
 (6 + 20 = 26).
    Kembali ke Pertempuran: Ketika Alex kembali, dia tiba kembali pada hari yang sama 
dia pergi (sesuai logika perjalanan waktu). Pertempuran telah berlangsung selama 
 3 hari sekarang.
    Menunggu Pertempuran Berakhir: Pertempuran berlangsung 10 hari. Karena dia 
sudah menyaksikan 3 hari, dia perlu menunggu 7 hari lagi.
    Kesimpulan: Alex menghabiskan total 3 (penantian awal) + 3 (sebelum 
lompatan pertama) + 20 (50 tahun yang lalu) + 7 (setelah kembali) = 33 hari di 
 masa lalu sebelum dia melihat akhir pertempuran.
Pikirkan langkah demi langkah tetapi hanya tunjukkan jawaban akhir untuk pernyataan tersebut.

pengguna:
{{pernyataan}}    #5

#1 Beberapa contoh pernyataan masalah
#2 Solusi untuk pernyataan masalah, output sebagai urutan langkah-langkah penalaran
#3 Beberapa contoh pernyataan masalah
#4 Solusi untuk pernyataan masalah, output sebagai urutan langkah-langkah penalaran
#5 Pernyataan masalah yang harus diselesaikan oleh LLM
```

Anda mungkin memperhatikan bahwa solusi untuk gambar 10.3 juga disediakan sebagai contoh dalam daftar 10.8. Juga membantu untuk kembali dan meninjau daftar 10.7 untuk balasan dari LLM tentang masalah tersebut. Dari sini, Anda dapat melihat langkah-langkah penalaran yang diterapkan LLM untuk mendapatkan jawaban akhirnya.

Sekarang, kita dapat melihat prompt yang mengevaluasi seberapa baik solusi tersebut memecahkan masalah. Buka `evaluate_answer.jinja2`, yang ditunjukkan pada daftar 10.9, untuk meninjau prompt yang digunakan. Promptnya sederhana, menggunakan zero-shot prompting, dan memungkinkan LLM untuk menggeneralisasi bagaimana ia harus menilai yang diharapkan dan yang diprediksi. Kita dapat memberikan contoh dan skor, sehingga mengubah ini menjadi contoh klasifikasi few-shot.

**Daftar 10.9** `evaluate_answer.jinja2`

```
sistem:

Harap konfirmasikan bahwa hasil yang diharapkan dan yang diprediksi adalah 
 sama untuk masalah yang diberikan.    #1
Kembalikan skor dari 0 hingga 1 di mana 1 adalah kecocokan sempurna dan 0 tidak ada kecocokan.
Harap kembalikan hanya skornya dan bukan penjelasannya.    #2

pengguna:
Masalah: {{masalah}}    #3

Hasil yang diharapkan: {{diharapkan}}    #4

Hasil yang diprediksi: {{diprediksi}}    #5

#1 Aturan untuk mengevaluasi solusi
#2 Arahan untuk hanya mengembalikan skor dan tidak ada yang lain
#3 Pernyataan masalah awal
#4 Jawaban yang diharapkan atau beralasan
#5 Output dari prompt CoT sebelumnya
```

Melihat output LLM yang ditunjukkan sebelumnya pada daftar 10.7, Anda dapat melihat mengapa langkah evaluasi bisa membingungkan. Mungkin perbaikan untuk ini bisa dengan menyarankan kepada LLM untuk memberikan jawaban akhir dalam satu pernyataan. Di bagian selanjutnya, kita beralih ke contoh lain dari penalaran prompt.

### Zero-shot CoT prompting

Seperti yang ditunjukkan oleh perjalanan waktu kita, CoT prompting bisa mahal dalam hal pembuatan prompt untuk kelas masalah tertentu. Meskipun tidak seefektif itu, ada teknik yang mirip dengan CoT yang tidak menggunakan contoh dan bisa lebih umum. Bagian ini akan membahas frasa sederhana yang digunakan untuk memunculkan penalaran dalam LLM.

Buka `prompt_flow/zero-shot-cot-prompting/flow.dag.yaml` di editor visual alur prompt VS Code. Alur ini sangat mirip dengan CoT sebelumnya, seperti yang ditunjukkan pada gambar 10.4. Daftar berikutnya menunjukkan pseudocode YAML yang menjelaskan alur.

**Daftar 10.10** alur `zero-shot-CoT-prompting`

```
   Input:
       pernyataan  : masalah pernyataan yang harus dipecahkan
       diharapkan : solusi yang diharapkan untuk masalah tersebut

   LLM: cot (prompt yang digunakan untuk memecahkan masalah)
       input: pernyataan
       output: jawaban yang diprediksi berdasarkan pernyataan masalah

   LLM: evaluate_answer (prompt yang digunakan untuk mengevaluasi solusi)
       input:
              pernyataan: -> input.pernyataan
              diharapkan: -> input.diharapkan
              diprediksi: -> output.cot

        output: skor seberapa baik masalah itu dijawab


    Output:
        pernyataan: -> input.pernyataan
        diharapkan: -> input.diharapkan
        diprediksi: -> output.cot
        skor_evaluasi: output.evaluate_answer

    ### Contoh Output
   {
       "skor_evaluasi": "1",    #1
       "diharapkan": "Setelah lompatan terakhir, 
          Max menemukan dirinya di tahun 1980 dan 
   dia berusia 75 tahun.",    #2
       "diprediksi": "Max mulai di… 
          Oleh karena itu, setelah lompatan terakhir, 
          Max berusia 75 tahun dan berada di tahun 1980.",    #3
       "pernyataan": "Dalam perjalanan waktu yang kompleks …"    #4
   }

#1 Skor evaluasi akhir
#2 Jawaban yang diharapkan
#3 Jawaban yang diprediksi (langkah-langkahnya telah dihilangkan untuk menunjukkan jawaban akhir)
#4 Pernyataan masalah awal
```

Jalankan/uji alur di VS Code dengan menekan Shift-F5 saat berada di editor visual. Alur akan berjalan, dan Anda akan melihat output yang mirip dengan yang ditunjukkan pada daftar 10.10. Contoh latihan ini berkinerja lebih baik daripada contoh sebelumnya pada masalah yang sama.

Buka prompt `cot.jinja2` di VS Code, seperti yang ditunjukkan pada daftar 10.11. Ini adalah prompt yang jauh lebih sederhana daripada contoh sebelumnya karena hanya menggunakan zero-shot. Namun, satu frasa kunci mengubah prompt sederhana ini menjadi mesin penalaran yang kuat. Baris dalam prompt `Mari` `berpikir` `langkah` `demi` `langkah` memicu LLM untuk mempertimbangkan konteks internal yang menunjukkan penalaran. Ini, pada gilirannya, mengarahkan LLM untuk menalar masalah dalam langkah-langkah.

**Daftar 10.11** `cot.jinja2`

```
sistem:
Anda adalah seorang ahli dalam memecahkan masalah perjalanan waktu.
Anda diberi masalah perjalanan waktu dan Anda harus menyelesaikannya.
Mari kita berpikir langkah demi langkah.    #1
Harap selesaikan jawaban Anda dalam satu pernyataan.    #2

pengguna:
{{pernyataan}}    #3

#1 Baris ajaib yang merumuskan penalaran dari LLM
#2 Meminta LLM untuk memberikan pernyataan akhir dari jawaban
#3 Pernyataan masalah yang diminta untuk diselesaikan oleh LLM
```

Frasa serupa yang meminta LLM untuk memikirkan langkah-langkah atau memintanya untuk merespons dalam langkah-langkah juga mengekstrak penalaran. Kami akan mendemonstrasikan teknik serupa tetapi lebih rumit di bagian selanjutnya.

### Langkah demi langkah dengan perantaian prompt

Kita dapat memperluas perilaku meminta LLM untuk berpikir langkah demi langkah menjadi rantai prompt yang memaksa LLM untuk menyelesaikan masalah dalam langkah-langkah. Di bagian ini, kita melihat teknik yang disebut *perantaian prompt* yang memaksa LLM untuk memproses masalah dalam langkah-langkah.

Buka file `prompt_flow/prompt-chaining/flow.dag.yaml` di editor visual, seperti yang ditunjukkan pada gambar 10.5. Perantaian prompt memecah metode penalaran yang digunakan untuk menyelesaikan masalah menjadi rantai prompt. Teknik ini memaksa LLM untuk menjawab masalah dalam hal langkah-langkah.

![Gambar 10.5](Images/10-5.png)

**Gambar 10.5** Alur perantaian prompt

Daftar 10.12 menunjukkan pseudocode YAML yang menjelaskan alur dalam beberapa detail lagi. Alur ini merangkai output dari blok LLM pertama ke yang kedua dan kemudian dari yang kedua ke yang ketiga. Memaksa LLM untuk memproses masalah dengan cara ini mengungkap pola penalaran, tetapi juga bisa terlalu bertele-tele.

**Daftar 10.12** alur `prompt-chaining`

```
   Input:
       pernyataan  : masalah pernyataan yang harus dipecahkan

   LLM: decompose_steps (prompt yang digunakan untuk menguraikan masalah)
        input: 
               pernyataan: -> input.pernyataan    #1

        output: rincian langkah-langkah untuk menyelesaikan masalah

   LLM: calculate_steps (prompt yang digunakan untuk menghitung langkah-langkah)
        input:
               pernyataan: -> input.pernyataan
               decompose_steps: -> output.decompose_steps    #2

               output: perhitungan untuk setiap langkah
   LLM: calculate_solution (mencoba menyelesaikan masalah)
        input:
               pernyataan: -> input.pernyataan
               decompose_steps: -> output.decompose_steps
               calculate_steps: -> output.calculate_steps    #3

         output: pernyataan solusi akhir

   Output:
        pernyataan: -> input.pernyataan
        decompose_steps: -> output.decompose_steps
        calculate_steps: -> output.calculate_steps
        calculate_solution: -> output.calculate_solution

   ### Contoh Output
{
    "calculate_steps": "1. Hari-hari yang dihabiskan oleh Alex",
    "decompose_steps": "Untuk mengetahui …",
    "solution": "Alex menghabiskan 13 hari di 
           masa lalu sebelum akhir pertempuran.",    #4
    "pernyataan": "Dalam sebuah film fiksi ilmiah, Alex …"
}

#1 Awal dari rantai prompt
#2 Output dari langkah sebelumnya disuntikkan ke langkah ini
#3 Output dari dua langkah sebelumnya disuntikkan ke langkah ini
#4 Pernyataan solusi akhir, meskipun salah, lebih dekat.
```

Jalankan alur dengan menekan Shift-F5 dari editor visual, dan Anda akan melihat output seperti yang ditunjukkan pada daftar 10.12. Jawabannya masih belum benar untuk masalah Alex, tetapi kita dapat melihat semua pekerjaan yang dilakukan LLM untuk menalar masalah tersebut.

Buka ketiga prompt: `decompose_steps.jinja2`, `calculate_steps.jinja2`, dan `calculate_solution.jinja2` (lihat daftar 10.13, 10.14, dan 10.15, masing-masing). Ketiga prompt yang ditunjukkan dalam daftar dapat dibandingkan untuk menunjukkan bagaimana output saling berantai.

**Daftar 10.13** `decompose_steps.jinja2`

```
sistem:
Anda adalah asisten AI pemecah masalah.
Tugas Anda adalah memecah masalah pengguna menjadi langkah-langkah yang lebih kecil dan membuat daftar 
 langkah-langkah dalam urutan yang akan Anda selesaikan.
Pikirkan langkah demi langkah, bukan secara umum.
Jangan mencoba menyelesaikan masalah, cukup daftar langkah-langkahnya.#1

pengguna:
{{pernyataan}}    #2

#1 Memaksa LLM untuk hanya membuat daftar langkah-langkah dan tidak ada yang lain
#2 Pernyataan masalah awal
```

**Daftar 10.14** `calculate_steps.jinja2`

```
sistem:
Anda adalah asisten AI pemecah masalah.
Anda akan diberikan daftar langkah-langkah yang menyelesaikan masalah.
Tugas Anda adalah menghitung output untuk setiap langkah secara berurutan.
Jangan mencoba menyelesaikan seluruh masalah,
cukup daftar output untuk setiap langkah.    #1
Pikirkan langkah demi langkah.    #2

pengguna:
{{pernyataan}}

{{langkah}}    #3

#1 Meminta agar LLM tidak menyelesaikan seluruh masalah, hanya langkah-langkahnya
#2 Menggunakan pernyataan ajaib untuk mengekstrak penalaran
#3 Menyuntikkan langkah-langkah yang dihasilkan oleh langkah decompose_steps
```

**Daftar 10.15** `calculate_solution.jinja2`

```
sistem:
Anda adalah asisten AI pemecah masalah.
Anda akan diberikan daftar langkah-langkah dan output yang dihitung untuk setiap langkah.
Gunakan output yang dihitung dari setiap langkah untuk menentukan 
solusi akhir untuk masalah tersebut.
Berikan hanya solusi akhir untuk masalah dalam 
kalimat singkat tunggal. Jangan sertakan langkah apa pun 
dalam jawaban Anda.    #1

pengguna:
{{pernyataan}}

{{langkah}}    #2

{{dihitung}}    #3

#1 Meminta agar LLM mengeluarkan jawaban akhir dan bukan langkah apa pun
#2 Langkah-langkah yang diuraikan
#3 Langkah-langkah yang dihitung
```

Dalam contoh latihan ini, kami tidak melakukan evaluasi dan penilaian apa pun. Tanpa evaluasi, kita dapat melihat bahwa urutan prompt ini masih memiliki masalah dalam menyelesaikan masalah perjalanan waktu kita yang lebih menantang yang ditunjukkan sebelumnya pada gambar 10.3. Namun, itu tidak berarti teknik ini tidak memiliki nilai, dan format prompting ini memecahkan beberapa masalah kompleks dengan baik.

Namun, yang ingin kami temukan adalah metodologi penalaran dan perencanaan yang dapat menyelesaikan masalah kompleks seperti itu secara konsisten. Bagian berikut beralih dari penalaran ke mengevaluasi solusi terbaik.

## Menggunakan evaluasi untuk solusi yang konsisten

Di bagian sebelumnya, kita belajar bahwa bahkan rencana yang paling beralasan pun mungkin tidak selalu menghasilkan solusi yang benar. Selain itu, kita mungkin tidak selalu memiliki jawaban untuk mengonfirmasi apakah solusi itu benar. Kenyataannya adalah bahwa kita sering ingin menggunakan beberapa bentuk evaluasi untuk menentukan kemanjuran suatu solusi.

Gambar 10.6 menunjukkan perbandingan strategi rekayasa prompt yang telah dirancang sebagai sarana untuk membuat LLM bernalar dan merencanakan. Kami telah membahas dua di sebelah kiri: zero-shot direct prompting dan CoT prompting. Latihan contoh berikut di bagian ini akan melihat konsistensi diri dengan teknik CoT dan ToT.

![Gambar 10.6](Images/10-6.png)

**Gambar 10.6** Membandingkan berbagai strategi rekayasa prompt untuk memungkinkan penalaran dan perencanaan dari LLM

Kami akan terus fokus pada masalah perjalanan waktu yang kompleks untuk membandingkan metode yang lebih canggih ini yang memperluas penalaran dan perencanaan dengan evaluasi. Di bagian selanjutnya, kita akan mengevaluasi konsistensi diri.

### Mengevaluasi prompting konsistensi diri

Konsistensi dalam prompting lebih dari sekadar menurunkan parameter suhu yang kami kirim ke LLM. Seringkali, kami ingin menghasilkan rencana atau solusi yang konsisten dan masih menggunakan suhu tinggi untuk mengevaluasi semua variasi rencana dengan lebih baik. Dengan mengevaluasi beberapa rencana yang berbeda, kita bisa mendapatkan pemahaman yang lebih baik tentang nilai keseluruhan dari suatu solusi.

*Prompting konsisten diri* adalah teknik menghasilkan beberapa rencana/solusi untuk masalah tertentu. Kemudian, rencana-rencana tersebut dievaluasi, dan rencana yang lebih sering atau konsisten diterima. Bayangkan tiga rencana yang dihasilkan, di mana dua serupa, tetapi yang ketiga berbeda. Menggunakan konsistensi diri, kami mengevaluasi dua rencana pertama sebagai jawaban yang lebih konsisten.

Buka `prompt_flow/self-consistency-prompting/flow.dag.yaml` di editor visual alur prompt VS Code. Diagram alur menunjukkan kesederhanaan alur pembuatan prompt pada gambar 10.7. Di sebelahnya dalam diagram adalah alur evaluasi konsistensi diri.

![Gambar 10.7](Images/10-7.png)

**Gambar 10.7** Pembuatan prompt konsistensi diri di samping alur evaluasi

Alur prompt menggunakan format grafik asiklik langsung (DAG) untuk menjalankan logika alur. DAG adalah cara yang sangat baik untuk mendemonstrasikan dan menjalankan logika alur, tetapi karena bersifat *asiklik,* yang berarti tidak dapat diulang, mereka tidak dapat menjalankan loop. Namun, karena alur prompt menyediakan mekanisme pemrosesan batch, kita dapat menggunakannya untuk mensimulasikan loop atau pengulangan dalam alur.

Mengacu pada gambar 10.6, kita dapat melihat bahwa konsistensi diri memproses input tiga kali sebelum mengumpulkan hasil dan menentukan rencana/balasan terbaik. Kita dapat menerapkan pola yang sama ini tetapi menggunakan pemrosesan batch untuk menghasilkan output. Kemudian, alur evaluasi akan menggabungkan hasil dan menentukan jawaban terbaik.

Buka templat prompt `self-consistency-prompting/cot.jinja2` di VS Code (lihat daftar 10.16). Daftar tersebut dipersingkat, karena kita telah melihat bagian-bagiannya sebelumnya. Prompt ini menggunakan dua contoh (prompt few-shot) dari CoT untuk mendemonstrasikan penalaran pemikiran kepada LLM.

**Daftar 10.16** `self-consistency-prompting/cot.jinja2`

```
sistem:

"Dalam sebuah film perjalanan waktu, Sarah melakukan perjalanan kembali… "    #1

Rantai Pemikiran:

    Asumsi Awal: …    #2
    Kesimpulan: Sarah menghabiskan 729 hari di masa lalu sebelum hari acara tersebut.

"Dalam plot film perjalanan waktu yang kompleks, Max, seorang berusia 25 tahun…"    #3

Rantai Pemikiran:
    Titik Awal: Max mulai …    #4
    Kesimpulan: Setelah lompatan terakhir, 
Max menemukan dirinya di tahun 1980 dan dia berusia 75 tahun.
Pikirkan langkah demi langkah,
 tetapi hanya tunjukkan jawaban akhir untuk pernyataan tersebut.    #5

pengguna:
{{pernyataan}}

#1 Masalah perjalanan waktu Sarah
#2 Contoh CoT, dipotong untuk keringkasan
#3 Masalah perjalanan waktu Max
#4 Contoh CoT, dipotong untuk keringkasan
#5 Panduan dan pernyataan akhir untuk membatasi output
```

Buka file `self-consistency-prompting/flow.dag.yaml` di VS Code. Jalankan contoh dalam mode batch dengan mengeklik Jalankan Batch (ikon gelas kimia) dari editor visual. Gambar 10.8 menunjukkan proses langkah demi langkah: 

1. Klik Jalankan Batch.
2. Pilih input JSON Lines (JSONL).
3. Pilih `statements.jsonl`.
4. Klik tautan Jalankan.

![Gambar 10.8](Images/10-8.png)

**Gambar 10.8** Proses langkah demi langkah meluncurkan proses batch

> **TIPS**  Jika Anda perlu meninjau prosesnya, lihat bab 9, yang membahas proses ini secara lebih rinci.

Daftar 10.17 menunjukkan output JSON dari menjalankan alur dalam mode batch. File `statements.jsonl` memiliki lima entri masalah perjalanan waktu Alex yang identik. Menggunakan entri yang identik memungkinkan kita untuk mensimulasikan prompt yang dieksekusi lima kali pada entri duplikat.

**Daftar 10.17** output eksekusi batch `self-consistency-prompting`

```
{
    "nama": "self-consistency-prompting_default_20240203_100322_912000",
    "dibuat_pada": "2024-02-03T10:22:30.028558",
    "status": "Selesai",
    "nama_tampilan": "self-consistency-prompting_variant_0_202402031022",
    "deskripsi": null,
    "tag": null,
    "properti": {
        "flow_path": "…prompt_flow/self-consistency-prompting",    #1
        "output_path": "…/.promptflow/.runs/self-
 consistency-prompting_default_20240203_100322_912000",    #2
        "system_metrics": {
            "total_tokens": 4649,
            "prompt_tokens": 3635,
            "completion_tokens": 1014,
            "duration": 30.033773
        }
    },
    "flow_name": "self-consistency-prompting",
    "data": "…/prompt_flow/self-consistency-prompting/
 statements.jsonl",    #3
    "output": "…/.promptflow/.runs/self-consistency-
 prompting_default_20240203_100322_912000/flow_outputs"
}

#1 Path tempat alur dieksekusi
#2 Folder yang berisi output alur (perhatikan path ini)
#3 Data yang digunakan untuk menjalankan alur dalam batch
```

Anda dapat melihat alur yang dihasilkan dengan menekan tombol Ctrl dan mengeklik tautan output, yang disorot dalam daftar 10.17. Ini akan membuka instance lain dari VS Code, yang menunjukkan folder dengan semua output dari proses tersebut. Sekarang kami ingin memeriksa jawaban yang paling konsisten. Untungnya, fitur evaluasi dalam alur prompt dapat membantu kami mengidentifikasi jawaban yang konsisten menggunakan pencocokan kesamaan.

Buka `self-consistency-evaluation/flow.dag.yaml` di VS Code (lihat gambar 10.7). Alur ini menyematkan jawaban yang diprediksi dan kemudian menggunakan agregasi untuk menentukan jawaban yang paling konsisten.

Dari alur, buka `consistency.py` di VS Code, seperti yang ditunjukkan pada daftar 10.18. Kode untuk fungsi alat ini menghitung kesamaan kosinus untuk semua pasangan jawaban. Kemudian, ia menemukan jawaban yang paling mirip, mencatatnya, dan mengeluarkannya sebagai jawaban.

**Daftar 10.18** `consistency.py`

```
from promptflow import tool
from typing import List
import numpy as np
from scipy.spatial.distance import cosine
@tool
def consistency(texts: List[str],
                embeddings: List[List[float]]) -> str:
    if len(embeddings) != len(texts):
        raise ValueError("Jumlah embedding 
       harus cocok dengan jumlah teks.")

    mean_embedding = np.mean(embeddings, axis=0)    #1
    similarities = [1 - cosine(embedding, mean_embedding) 
                for embedding in embeddings]    #2
    most_similar_index = np.argmax(similarities)    #3

    from promptflow import log_metric
    log_metric(key="highest_ranked_output", value=texts[most_similar_index])    #4

    return texts[most_similar_index]    #5

#1 Menghitung rata-rata dari semua embedding
#2 Menghitung kesamaan kosinus untuk setiap pasang embedding
#3 Menemukan indeks jawaban yang paling mirip
#4 Mencatat output sebagai metrik
#5 Mengembalikan teks untuk jawaban yang paling mirip
```

Kita perlu menjalankan alur evaluasi dalam mode batch juga. Buka `self-consistency-evaluation/flow.dag.yaml` di VS Code dan jalankan alur dalam mode batch (ikon gelas kimia). Kemudian, pilih Jalankan yang Ada sebagai input alur, dan ketika diminta, pilih proses teratas atau proses terakhir yang baru saja Anda jalankan sebagai input.

Sekali lagi, setelah alur selesai diproses, Anda akan melihat output seperti yang ditunjukkan pada daftar 10.17. Ctrl-klik pada tautan folder output untuk membuka instance baru VS Code yang menunjukkan hasilnya. Temukan dan buka file `metric.json` di VS Code, seperti yang ditunjukkan pada gambar 10.9.

![Gambar 10.9](Images/10-9.png)

**Gambar 10.9** VS Code terbuka ke folder output proses batch. Yang disorot adalah file `metrics.json` dan output yang menunjukkan jawaban yang paling mirip.

Jawaban yang ditunjukkan pada gambar 10.9 masih salah untuk proses ini. Anda dapat melanjutkan beberapa proses batch lagi dari prompt dan/atau meningkatkan jumlah proses dalam satu batch dan kemudian mengevaluasi alur untuk melihat apakah Anda mendapatkan jawaban yang lebih baik. Teknik ini umumnya lebih membantu untuk masalah yang lebih sederhana tetapi masih menunjukkan ketidakmampuan untuk menalar masalah yang kompleks.

Konsistensi diri menggunakan pendekatan reflektif untuk mengevaluasi pemikiran yang paling mungkin. Namun, hal yang paling mungkin tentu tidak selalu yang terbaik. Oleh karena itu, kita harus mempertimbangkan pendekatan yang lebih komprehensif di bagian selanjutnya.

### Mengevaluasi tree of thought prompting

Seperti yang disebutkan sebelumnya, ToT prompting, seperti yang ditunjukkan pada gambar 10.6, menggabungkan teknik evaluasi diri dan perantaian prompt. Dengan demikian, ia memecah urutan perencanaan menjadi rantai prompt, tetapi pada setiap langkah dalam rantai, ia menyediakan beberapa evaluasi. Ini menciptakan pohon yang dapat dieksekusi dan dievaluasi di setiap tingkat, breadth-first, atau dari atas ke bawah, depth-first.

Gambar 10.10 menunjukkan perbedaan antara mengeksekusi pohon menggunakan breadth-first atau depth-first. Sayangnya, karena pola eksekusi DAG dari alur prompt, kita tidak dapat dengan cepat mengimplementasikan metode depth-first, tetapi breadth-first bekerja dengan baik.

![Gambar 10.10](Images/10-10.png)

**Gambar 10.10** Eksekusi breadth-first vs. depth-first pada pola ToT

Buka `tree-of-thought-evaluation/flow.dag.yaml` di VS Code. Visual alur ditunjukkan pada gambar 10.11. Alur ini berfungsi seperti pola ToT breadth-first—alur merangkai serangkaian prompt yang meminta LLM untuk mengembalikan beberapa rencana di setiap langkah.

![Gambar 10.11](Images/10-11.png)

**Gambar 10.11** Pola ToT diekspresikan dan alur prompt

Karena alur dieksekusi dalam gaya breadth-first, setiap output tingkat dari node juga dievaluasi. Setiap node dalam alur menggunakan sepasang fungsi semantik—satu untuk menghasilkan jawaban dan yang lainnya untuk mengevaluasi jawaban. Fungsi semantik adalah blok alur Python kustom yang memproses beberapa input dan menghasilkan beberapa output.

Daftar 10.19 menunjukkan alat `semantic_function.py`. Alat umum ini digunakan kembali untuk beberapa blok dalam alur ini. Ini juga menunjukkan fungsionalitas penyematan dari SK untuk penggunaan langsung dalam alur prompt.

**Daftar 10.19** `semantic_function.py`

```
@tool
def my_python_tool(
    input: str,
    input_node: int,
    history: str,
    semantic_function: str,
    evaluation_function: str,
    function_name: str,
    skill_name: str,
    max_tokens: int,
    temperature: float,
    deployment_name: str,
    connection: Union[OpenAIConnection, 
                      AzureOpenAIConnection],    #1
) -> str:
    if input is None or input == "":    #2
        return ""

    kernel = sk.Kernel(log=sk.NullLogger())
    # kode untuk menyiapkan kernel dan koneksi LLM dihilangkan


    function = kernel.create_semantic_function(
                             semantic_function,                                               
                             function_name=function_name,
                             skill_name=skill_name,
                             max_tokens=max_tokens,
                             temperature=temperature,
                             top_p=0.5)    #3
    evaluation = kernel.create_semantic_function(
                             evaluation_function,        
                             function_name="Evaluation",
                             skill_name=skill_name,
                             max_tokens=max_tokens,
                             temperature=temperature,
                             top_p=0.5)    #4

    async def main():
        query = f"{history}
{input}"
        try:
            eval = int((await evaluation.invoke_async(query)).result)
            if eval > 25:    #5
                return await function.invoke_async(query)   #6
        except Exception as e:
            raise Exception("Evaluation failed", e)

       try:
        result = asyncio.run(main()).result
        return result
    except Exception as e:
        print(e)
        return ""

#1 Menggunakan union untuk memungkinkan berbagai jenis koneksi LLM
#2 Memeriksa untuk melihat apakah input kosong atau None; jika demikian, fungsi tidak boleh dieksekusi.
#3 Menyiapkan fungsi generasi yang membuat rencana
#4 Menyiapkan fungsi evaluasi
#5 Menjalankan fungsi evaluasi dan menentukan apakah input cukup baik untuk melanjutkan
#6 Jika skor evaluasi cukup tinggi, hasilkan langkah berikutnya
```

Alat fungsi semantik digunakan di blok ahli, node, dan jawaban pohon. Pada setiap langkah, fungsi menentukan apakah ada teks yang dimasukkan. Jika tidak ada teks, blok kembali tanpa eksekusi. Melewatkan teks ke blok berarti blok sebelumnya gagal evaluasi. Dengan mengevaluasi sebelum setiap langkah, ToT memotong eksekusi rencana yang dianggapnya tidak valid.

Ini mungkin pola yang rumit untuk dipahami pada awalnya, jadi lanjutkan dan jalankan alur di VS Code. Daftar 10.20 hanya menunjukkan output node jawaban dari suatu proses; hasil ini mungkin berbeda dari apa yang Anda lihat tetapi harus serupa. Node yang tidak mengembalikan teks berarti gagal evaluasi atau induknya gagal.

**Daftar 10.20** Output dari alur `tree-of-thought-evaluation`

```
{
    "answer_1_1": "",    #1
    "answer_1_2": "",
    "answer_1_3": "",
    "answer_2_1": "Alex menghabiskan total 29 hari di masa lalu sebelum dia 
melihat akhir pertempuran.",
    "answer_2_2": "",    #2
    "answer_2_3": "Alex menghabiskan total 29 hari di masa lalu sebelum dia 
melihat akhir pertempuran.",
    "answer_3_1": "",    #3
    "answer_3_2": "Alex menghabiskan total 29 hari di masa lalu sebelum dia 
melihat akhir pertempuran.",
    "answer_3_3": "Alex menghabiskan total 9 hari di masa lalu sebelum dia 
melihat akhir pertempuran.",
}

#1 Menunjukkan bahwa rencana node pertama tidak valid dan tidak dieksekusi
#2 Rencana untuk node 2 dan jawaban 2 gagal evaluasi dan tidak dijalankan.
#3 Rencana untuk node ini gagal dievaluasi dan tidak dijalankan.
```

Output pada daftar 10.20 menunjukkan bagaimana hanya sekumpulan node terpilih yang dievaluasi. Dalam kebanyakan kasus, node yang dievaluasi mengembalikan jawaban yang bisa jadi valid. Di mana tidak ada output yang dihasilkan, itu berarti bahwa node itu sendiri atau induknya tidak valid. Ketika semua node saudara kembali kosong, node induk gagal dievaluasi.

Seperti yang bisa kita lihat, ToT valid untuk masalah yang kompleks tetapi mungkin tidak terlalu praktis. Eksekusi alur ini dapat memakan waktu hingga 27 panggilan ke LLM untuk menghasilkan output. Dalam praktiknya, mungkin hanya melakukan setengah dari jumlah panggilan itu, tetapi itu masih selusin atau lebih panggilan untuk menjawab satu masalah.

## Latihan

Gunakan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- *Latihan 1*—Buat Prompting Langsung, Prompting Few-Shot, dan Prompting Zero-Shot
  - *Tujuan*—Buat tiga prompt berbeda untuk LLM untuk meringkas artikel ilmiah terbaru: satu menggunakan prompting langsung, satu dengan prompting few-shot, dan yang terakhir menggunakan prompting zero-shot.
  - *Tugas:*
    - Bandingkan efektivitas ringkasan yang dihasilkan oleh setiap pendekatan.
    - Bandingkan keakuratan ringkasan yang dihasilkan oleh setiap pendekatan.
  - *Latihan 2*—Buat Prompt Penalaran
    - *Tujuan*—Rancang serangkaian prompt yang mengharuskan LLM untuk memecahkan teka-teki logika atau teka-teki.
    - *Tugas:*
      - Fokus pada bagaimana struktur prompt Anda dapat memengaruhi proses penalaran LLM.
      - Fokus pada bagaimana hal yang sama dapat memengaruhi kebenaran jawabannya.
  - *Latihan 3*—Teknik Prompt Evaluasi
    - *Tujuan*—Kembangkan prompt evaluasi yang meminta LLM untuk memprediksi hasil dari eksperimen hipotetis.
    - *Tugas:*
      - Buat prompt tindak lanjut yang mengevaluasi prediksi LLM untuk akurasi dan memberikan umpan balik pada proses penalarannya.

## Ringkasan

- Prompting solusi langsung adalah metode dasar menggunakan prompt untuk mengarahkan LLM untuk memecahkan masalah atau tugas tertentu, yang menekankan pentingnya struktur tanya jawab yang jelas.
- Few-shot prompting memberikan LLM beberapa contoh untuk membimbing mereka dalam menangani konten baru atau yang belum pernah dilihat, menyoroti kekuatannya dalam memungkinkan model untuk beradaptasi dengan pola yang tidak dikenal.
- Zero-shot learning dan prompting menunjukkan bagaimana LLM dapat menggeneralisasi dari pelatihan mereka untuk memecahkan masalah tanpa memerlukan contoh eksplisit, menunjukkan kemampuan bawaan mereka untuk memahami dan menerapkan pengetahuan dalam konteks baru.
- Chain of thought prompting memandu LLM melalui proses penalaran langkah demi langkah untuk menyelesaikan masalah yang kompleks, yang menggambarkan cara memunculkan penalaran terperinci dari model.
- Perantaian prompt memecah masalah menjadi serangkaian prompt yang saling membangun, menunjukkan cara menyusun proses pemecahan masalah yang kompleks menjadi langkah-langkah yang dapat dikelola untuk LLM.
- Konsistensi diri adalah teknik prompt yang menghasilkan beberapa solusi untuk suatu masalah dan memilih jawaban yang paling konsisten melalui evaluasi, yang menekankan pentingnya konsistensi dalam mencapai hasil yang andal.
- Tree of thought prompting menggabungkan evaluasi diri dan perantaian prompt untuk menciptakan strategi komprehensif untuk menangani masalah yang kompleks, yang memungkinkan eksplorasi sistematis dari beberapa jalur solusi.
- Strategi rekayasa prompt tingkat lanjut memberikan wawasan tentang teknik-teknik canggih seperti konsistensi diri dengan CoT dan ToT, yang menawarkan metode untuk meningkatkan akurasi dan keandalan solusi yang dihasilkan LLM.
