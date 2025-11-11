# 1 Pengantar agen dan dunianya

### Bab ini mencakup
- Mendefinisikan konsep agen
- Membedakan komponen-komponen agen
- Menganalisis kebangkitan era agen: Mengapa agen?
- Mengupas antarmuka AI
- Menavigasi lanskap agen

Agen bukanlah konsep baru dalam pembelajaran mesin dan kecerdasan buatan (AI). Dalam pembelajaran penguatan, misalnya, kata *agen* menunjukkan kecerdasan pembuat keputusan dan pembelajaran yang aktif. Di area lain, kata *agen* lebih selaras dengan aplikasi atau perangkat lunak otomatis yang melakukan sesuatu atas nama Anda.

## 1.1 Mendefinisikan agen

Anda dapat melihat kamus online mana pun untuk menemukan definisi agen. *Kamus Merriam-Webster* mendefinisikannya seperti ini (www.merriam-webster.com/dictionary/agent):

- Sesuatu yang bertindak atau menggunakan kekuatan
- Sesuatu yang menghasilkan atau dapat menghasilkan efek
- Sarana atau instrumen yang dengannya kecerdasan pemandu mencapai hasil

Kata *agen* dalam perjalanan kita membangun agen yang kuat di buku ini menggunakan definisi kamus ini. Itu juga berarti istilah *asisten* akan sinonim dengan *agen.* Alat seperti Asisten GPT OpenAI juga akan termasuk dalam selimut agen AI. OpenAI menghindari kata *agen* karena sejarah pembelajaran mesin, di mana agen bersifat memutuskan sendiri dan otonom.

Gambar 1.1 menunjukkan empat kasus di mana pengguna dapat berinteraksi dengan model bahasa besar (LLM) secara langsung atau melalui proksi agen/asisten, agen/asisten, atau agen otonom. Keempat kasus penggunaan ini disorot lebih detail dalam daftar ini:

- *Interaksi pengguna langsung*—Jika Anda menggunakan versi ChatGPT sebelumnya, Anda mengalami interaksi langsung dengan LLM. Tidak ada agen proksi atau asisten lain yang menyela atas nama Anda.
- *Proksi agen/asisten*—Jika Anda pernah menggunakan Dall-E 3 melalui ChatGPT, maka Anda pernah mengalami interaksi agen proksi. Dalam kasus penggunaan ini, LLM menyela permintaan Anda dan menyusunnya kembali dalam format yang dirancang lebih baik untuk tugas tersebut. Misalnya, untuk pembuatan gambar, ChatGPT menyusun prompt dengan lebih baik. Agen proksi adalah kasus penggunaan sehari-hari untuk membantu pengguna dengan tugas atau model yang tidak dikenal.
- *Agen/asisten*—Jika Anda pernah menggunakan plugin ChatGPT atau asisten GPT, maka Anda pernah mengalami kasus penggunaan ini. Dalam hal ini, LLM mengetahui fungsi plugin atau asisten dan bersiap untuk melakukan panggilan ke plugin/fungsi ini. Namun, sebelum melakukan panggilan, LLM memerlukan persetujuan pengguna. Jika disetujui, plugin atau fungsi dijalankan, dan hasilnya dikembalikan ke LLM. LLM kemudian membungkus respons ini dalam bahasa alami dan mengembalikannya kepada pengguna.
- *Agen otonom*—Dalam kasus penggunaan ini, agen menafsirkan permintaan pengguna, menyusun rencana, dan mengidentifikasi titik keputusan. Dari sini, ia menjalankan langkah-langkah dalam rencana dan membuat keputusan yang diperlukan secara mandiri. Agen dapat meminta umpan balik pengguna setelah tugas tonggak tertentu, tetapi sering kali diberi kebebasan untuk menjelajah dan belajar jika memungkinkan. Agen ini menimbulkan masalah etika dan keamanan yang paling besar, yang akan kita bahas nanti.

![Gambar 1.1](Images/1-1.png "Perbedaan antara interaksi LLM dari tindakan langsung dibandingkan dengan menggunakan agen proksi, agen, dan agen otonom")

Gambar 1.1 menunjukkan kasus penggunaan untuk satu alur tindakan pada LLM menggunakan satu agen. Untuk masalah yang lebih kompleks, kita sering memecah agen menjadi profil atau persona. Setiap profil agen diberi tugas tertentu dan menjalankan tugas itu dengan alat dan pengetahuan khusus.

*Sistem multi-agen* adalah profil agen yang bekerja sama dalam berbagai konfigurasi untuk memecahkan masalah. Gambar 1.2 menunjukkan contoh sistem multi-agen yang menggunakan tiga agen: pengontrol atau proksi dan dua agen profil sebagai pekerja yang dikendalikan oleh proksi. Profil pembuat kode di sebelah kiri menulis kode yang diminta pengguna; di sebelah kanan adalah profil penguji yang dirancang untuk menulis pengujian unit. Agen-agen ini bekerja dan berkomunikasi bersama sampai mereka puas dengan kode tersebut dan kemudian meneruskannya kepada pengguna.

Gambar 1.2 menunjukkan salah satu konfigurasi agen yang mungkin tak terbatas. (Dalam bab 4, kita akan menjelajahi platform sumber terbuka Microsoft, AutoGen, yang mendukung banyak konfigurasi untuk menggunakan sistem multi-agen.)

![Gambar 1.2](Images/1-2.png "Dalam contoh sistem multi-agen ini, pengontrol atau proksi agen berkomunikasi langsung dengan pengguna. Dua agen—pembuat kode dan penguji—bekerja di latar belakang untuk membuat kode dan menulis pengujian unit untuk menguji kode.")

Sistem multi-agen dapat bekerja secara otonom tetapi mungkin juga berfungsi dengan dipandu sepenuhnya oleh umpan balik manusia. Manfaat menggunakan banyak agen sama seperti agen tunggal tetapi sering kali diperbesar. Di mana agen tunggal biasanya berspesialisasi dalam satu tugas, sistem multi-agen dapat menangani banyak tugas secara paralel. Beberapa agen juga dapat memberikan umpan balik dan evaluasi, mengurangi kesalahan saat menyelesaikan tugas.

Seperti yang bisa kita lihat, agen AI atau sistem agen dapat dirakit dengan berbagai cara. Namun, agen itu sendiri juga dapat dirakit menggunakan banyak komponen. Di bagian selanjutnya, kita akan membahas topik mulai dari profil agen hingga tindakan yang mungkin dilakukannya, serta memori dan perencanaan.

## 1.2 Memahami sistem komponen agen

Agen dapat berupa unit kompleks yang terdiri dari beberapa sistem komponen. Komponen-komponen ini adalah alat yang digunakan agen untuk membantunya menyelesaikan tujuan atau tugas yang diberikan dan bahkan membuat yang baru. Komponen dapat berupa sistem sederhana atau kompleks, biasanya dibagi menjadi lima kategori.

Gambar 1.3 menjelaskan kategori utama komponen yang dapat digabungkan oleh sistem agen tunggal. Setiap elemen akan memiliki subtipe yang dapat menentukan jenis, struktur, dan penggunaan komponen. Inti dari semua agen adalah profil dan persona; yang memperluas dari itu adalah sistem dan fungsi yang menyempurnakan agen.

![Gambar 1.3](Images/1-3.png "Lima komponen utama sistem agen tunggal (gambar dihasilkan melalui DALL-E 3)")

Profil dan persona agen yang ditunjukkan pada gambar 1.4 mewakili deskripsi dasar agen. Persona—sering disebut *system prompt*—memandu agen untuk menyelesaikan tugas, mempelajari cara merespons, dan nuansa lainnya. Ini mencakup elemen-elemen seperti latar belakang (misalnya, pembuat kode, penulis) dan demografi, dan dapat dihasilkan melalui metode seperti kerajinan tangan, bantuan LLM, atau teknik berbasis data, termasuk algoritme evolusioner.

![Gambar 1.4](Images/1-4.png "Pandangan mendalam tentang bagaimana kita akan menjelajahi pembuatan profil agen")

Kita akan menjelajahi cara membuat profil/persona agen yang efektif dan spesifik melalui teknik seperti rubrik dan landasan. Selain itu, kita akan menjelaskan aspek profil yang dirumuskan manusia versus yang dirumuskan AI (LLM), termasuk teknik inovatif menggunakan data dan algoritme evolusioner untuk membangun profil.

> **Catatan** —Profil agen atau asisten terdiri dari elemen-elemen, termasuk persona. Mungkin akan membantu jika Anda menganggap profil sebagai deskripsi pekerjaan yang akan dilakukan agen/asisten dan alat yang dibutuhkannya.

Gambar 1.5 menunjukkan tindakan komponen dan penggunaan alat dalam konteks agen yang melibatkan aktivitas yang diarahkan pada penyelesaian tugas atau perolehan informasi. Tindakan-tindakan ini dapat dikategorikan ke dalam penyelesaian tugas, eksplorasi, dan komunikasi, dengan berbagai tingkat pengaruh pada lingkungan agen dan keadaan internalnya. Tindakan dapat dihasilkan secara manual, through memory recollection, or by following predefined plans, influencing the agent's behavior and enhancing learning.

![Gambar 1.5](Images/1-5.png "Aspek-aspek tindakan agen yang akan kita jelajahi dalam buku ini")

Memahami target tindakan membantu kita menentukan tujuan yang jelas untuk penyelesaian tugas, eksplorasi, atau komunikasi. Mengenali efek tindakan mengungkapkan bagaimana tindakan memengaruhi hasil tugas, lingkungan agen, dan keadaan internalnya, yang berkontribusi pada pengambilan keputusan yang efisien. Terakhir, memahami metode pembuatan tindakan membekali kita dengan pengetahuan untuk membuat tindakan secara manual, mengingatnya dari memori, atau mengikuti rencana yang telah ditentukan sebelumnya, yang meningkatkan kemampuan kita untuk secara efektif membentuk perilaku agen dan proses pembelajaran.

Gambar 1.6 menunjukkan komponen pengetahuan dan memori secara lebih rinci. Agen menggunakan pengetahuan dan memori untuk membubuhi keterangan konteks dengan informasi yang paling relevan sambil membatasi jumlah token yang digunakan. Struktur pengetahuan dan memori dapat disatukan, di mana kedua subset mengikuti struktur tunggal atau struktur hibrida yang melibatkan campuran berbagai bentuk pengambilan. Format pengetahuan dan memori dapat sangat bervariasi dari bahasa (misalnya, dokumen PDF) hingga basis data (relasional, objek, atau dokumen) dan penyematan, menyederhanakan pencarian kesamaan semantik melalui representasi vektor atau bahkan daftar sederhana yang berfungsi sebagai memori agen.

![Gambar 1.6](Images/1-6.png "Menjelajahi peran dan penggunaan memori dan pengetahuan agen")

Gambar 1.7 menunjukkan komponen penalaran dan evaluasi dari sistem agen. Penelitian dan aplikasi praktis telah menunjukkan bahwa LLM/agen dapat bernalar secara efektif. Sistem penalaran dan evaluasi membubuhi keterangan alur kerja agen dengan memberikan kemampuan untuk memikirkan masalah dan mengevaluasi solusi.

![Gambar 1.7](Images/1-7.png "Komponen penalaran dan evaluasi serta detailnya")

Gambar 1.8 menunjukkan komponen perencanaan/umpan balik agen dan perannya dalam mengatur tugas untuk mencapai tujuan tingkat yang lebih tinggi. Ini dapat dikategorikan ke dalam dua pendekatan ini:

- *Perencanaan tanpa umpan balik*—Agen otonom membuat keputusan secara mandiri.
- *Perencanaan dengan umpan balik*—Pemantauan dan modifikasi rencana didasarkan pada berbagai sumber masukan, termasuk perubahan lingkungan dan umpan balik manusia secara langsung.

![Gambar 1.8](Images/1-8.png "Menjelajahi peran perencanaan dan penalaran agen")

Dalam perencanaan, agen dapat menggunakan penalaran *jalur tunggal*,* penalaran berurutan* melalui setiap langkah tugas, atau penalaran *multipath* untuk menjelajahi banyak strategi dan menyimpan yang efisien untuk digunakan di masa mendatang. Perencana eksternal, yang dapat berupa kode atau sistem agen lain, mungkin juga memainkan peran dalam mengatur rencana.

Salah satu dari jenis agen kami sebelumnya—agen/asisten proksi, agen/asisten, atau agen otonom—dapat menggunakan sebagian atau semua komponen ini. Bahkan komponen perencanaan memiliki peran di luar agen otonom dan dapat secara efektif memberdayakan bahkan agen biasa.

## 1.3 Meneliti kebangkitan era agen: Mengapa agen?

Agen dan asisten AI dengan cepat beralih dari komoditas utama dalam penelitian AI ke pengembangan perangkat lunak arus utama. Daftar alat dan platform yang terus berkembang membantu dalam pembangunan dan pemberdayaan agen. Bagi orang luar, itu semua mungkin tampak seperti sensasi yang dimaksudkan untuk menggelembungkan nilai beberapa teknologi keren tapi berlebihan.

Selama beberapa bulan pertama setelah rilis awal ChatGPT, disiplin baru yang disebut *rekayasa prompt* terbentuk: pengguna menemukan bahwa menggunakan berbagai teknik dan pola dalam prompt mereka memungkinkan mereka untuk menghasilkan output yang lebih baik dan lebih konsisten. Namun, pengguna juga menyadari bahwa rekayasa prompt hanya bisa sampai sejauh ini.

Rekayasa prompt still an excellent way to interact directly with LLMs such as ChatGPT. Over time, many users discovered that effective prompting required iteration, reflection, and more iteration. The first agent systems, such as AutoGPT, emerged from these discoveries, capturing the community's attention.

Gambar 1.9 menunjukkan desain asli AutoGPT, salah satu sistem agen otonom pertama. Agen ini dirancang untuk mengulangi urutan tugas yang direncanakan yang ditetapkannya dengan melihat tujuan pengguna. Melalui setiap iterasi tugas dari langkah-langkah, agen mengevaluasi tujuan dan menentukan apakah tugas tersebut selesai. Jika tugas belum selesai, agen dapat merencanakan ulang langkah-langkah dan memperbarui rencana berdasarkan pengetahuan baru atau umpan balik manusia.

![Gambar 1.9](Images/1-9.png "Desain asli sistem agen AutoGPT")

AutoGPT menjadi contoh pertama yang menunjukkan kekuatan penggunaan perencanaan tugas dan iterasi dengan model LLM. Dari sini dan bersamaan, sistem dan kerangka kerja agen lain meledak ke dalam komunitas menggunakan sistem perencanaan dan iterasi tugas yang serupa. Secara umum diterima bahwa perencanaan, iterasi, dan pengulangan adalah proses terbaik untuk memecahkan tujuan yang kompleks dan multifaset untuk LLM.

Namun, sistem agen otonom memerlukan kepercayaan pada proses pengambilan keputusan agen, sistem pagar pengaman/evaluasi, dan definisi tujuan. Kepercayaan juga merupakan sesuatu yang diperoleh dari waktu ke waktu. Kurangnya kepercayaan kita berasal dari kurangnya pemahaman kita tentang kemampuan agen otonom.

> **Catatan** —Kecerdasan umum buatan (AGI) adalah bentuk kecerdasan yang dapat belajar untuk menyelesaikan tugas apa pun yang dapat dilakukan manusia. Banyak praktisi di dunia baru AI ini percaya bahwa AGI yang menggunakan sistem agen otonom adalah tujuan yang dapat dicapai.

Untuk alasan ini, banyak alat agen arus utama dan siap produksi tidak otonom. Namun, mereka masih memberikan manfaat yang signifikan dalam mengelola dan mengotomatiskan tugas menggunakan GPT (LLM). Oleh karena itu, karena tujuan kita dalam buku ini adalah untuk memahami semua bentuk agen, lebih banyak aplikasi praktis akan didorong oleh agen non-otonom.

Agen dan alat agen hanyalah lapisan teratas dari paradigma pengembangan aplikasi perangkat lunak baru. Kita akan melihat paradigma baru ini di bagian selanjutnya.

## 1.4 Mengupas antarmuka AI

Paradigma agen AI bukan only a shift in how we work with LLMs but is also perceived as a shift in how we develop software and handle data. Software and data will no longer be interfaced using user interfaces (UIs), application programming interfaces (APIs), and specialized query languages such as SQL. Instead, they will be designed to be interfaced using natural language.

Gambar 1.10 menunjukkan cuplikan tingkat tinggi tentang seperti apa arsitektur baru ini dan peran apa yang dimainkan oleh agen AI. Data, perangkat lunak, dan aplikasi beradaptasi untuk mendukung antarmuka bahasa alami yang semantik. Antarmuka AI ini memungkinkan agen untuk mengumpulkan data dan berinteraksi dengan aplikasi perangkat lunak, bahkan agen lain atau aplikasi agen. Ini merupakan pergeseran baru dalam cara kita berinteraksi dengan perangkat lunak dan aplikasi.

![Gambar 1.10](Images/1-10.png "Visi tentang bagaimana agen akan berinteraksi dengan sistem perangkat lunak")

*Antarmuka AI* adalah kumpulan fungsi, alat, dan lapisan data yang mengekspos data dan aplikasi dengan bahasa alami. Di masa lalu, kata *semantik* telah banyak digunakan untuk menggambarkan antarmuka ini, dan bahkan beberapa alat menggunakan nama tersebut; namun, "semantik" juga dapat memiliki berbagai arti dan kegunaan. Oleh karena aitu, dalam buku ini, kita akan menggunakan istilah *antarmuka AI.*

Pembangunan antarmuka AI akan memberdayakan agen yang perlu menggunakan layanan, alat, dan data. Dengan pemberdayaan ini akan datang peningkatan akurasi dalam menyelesaikan tugas dan aplikasi yang lebih dapat dipercaya dan otonom. Meskipun antarmuka AI mungkin tidak sesuai untuk semua perangkat lunak dan data, antarmuka ini akan mendominasi banyak kasus penggunaan.

## 1.5 Menavigasi lanskap agen

Agen GPT mewakili pergeseran keseluruhan dalam cara konsumen dan pengembang mendekati segalanya, mulai dari menemukan informasi hingga membangun perangkat lunak dan mengakses data. Hampir setiap hari, kerangka kerja, komponen, atau antarmuka agen baru muncul di GitHub atau di makalah penelitian. Ini bisa sangat banyak dan mengintimidasi bagi pengguna baru yang mencoba memahami apa itu sistem agen dan bagaimana menggunakannya.

## Ringkasan

- Agen adalah entitas yang bertindak atau menggunakan kekuatan, menghasilkan efek, atau berfungsi sebagai sarana untuk mencapai hasil. Agen mengotomatiskan interaksi dengan model bahasa besar (LLM) di AI.
- Asisten identik dengan agen. Kedua istilah tersebut mencakup alat-alat seperti Asisten GPT OpenAI.
- Agen otonom dapat membuat keputusan independen, dan perbedaan mereka dari agen non-otonom sangat penting.
- Empat jenis utama interaksi LLM termasuk interaksi pengguna langsung, proksi agen/asisten, agen/asisten, dan agen otonom.
- Sistem multi-agen melibatkan profil agen yang bekerja sama, sering kali dikendalikan oleh proksi, untuk menyelesaikan tugas-tugas kompleks.
- Komponen utama agen meliputi profil/persona, tindakan, pengetahuan/memori, penalaran/evaluasi, dan perencanaan/umpan balik.
- Profil dan persona agen memandu tugas, respons, dan nuansa lain dari agen, sering kali termasuk latar belakang dan demografi.
- Tindakan dan alat untuk agen dapat dibuat secara manual, dipanggil dari memori, atau mengikuti rencana yang telah ditentukan sebelumnya.
- Agen menggunakan struktur pengetahuan dan memori untuk mengoptimalkan konteks dan meminimalkan penggunaan token melalui berbagai format, dari dokumen hingga penyematan.
- Sistem penalaran dan evaluasi memungkinkan agen untuk memikirkan masalah dan menilai solusi menggunakan pola prompt seperti zero-shot, one-shot, and few-shot.
- Komponen perencanaan/umpan balik mengatur tugas untuk mencapai tujuan menggunakan penalaran jalur tunggal atau multipath dan mengintegrasikan umpan balik lingkungan dan manusia.
- Kebangkitan agen AI telah memperkenalkan paradigma pengembangan perangkat lunak baru, bergeser dari antarmuka tradisional ke antarmuka berbasis bahasa alami.
- Memahami perkembangan dan interaksi alat-alat ini membantu mengembangkan sistem agen, baik tunggal, ganda, atau otonom.
