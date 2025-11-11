# 10 Entri CLAUDE.md Pengubah Permainan yang Mengubah Sesi Kode Claude Saya menjadi Kekuatan Super Pengkodean

**TL;DR:** Lelah bergelut dengan AI yang menulis kode spageti? Kenali [CLAUDE.md](https://www.anthropic.com/engineering/claude-code-best-practices) – otak persisten proyek Anda yang mengajari Claude cara membuat kode seperti seorang profesional. Di bawah ini adalah 10 prompt CLAUDE.md yang mematikan (dengan contoh) yang mengubah alur kerja pengkodean AI agentik saya dari begadang menjadi autopilot.

## Mimpi Buruk di Node (dan Pencerahan CLAUDE.md)

Saat itu pukul 2:13 pagi pada hari Selasa. Saya membungkuk di atas keyboard, mata merah, men-debug API Node.js yang mengeluarkan kesalahan 500 yang samar.

![10 Entri CLAUDE.md Pengubah Permainan](https://miro.medium.com/v2/resize:fit:720/format:webp/1*BQvfq_gj5CB7mGFcdwkm6g@2x.jpeg)

[Claude Code](https://docs.claude.com/en/docs/claude-code/overview) sedang bekerja. Diambil oleh [Google Nano Banana](https://aistudio.google.com/models/gemini-2-5-flash-image)

Saya punya pernyataan console.log di mana-mana, Postman terbuka di satu layar, Stack Overflow di layar lain – menjalani hari groundhog terburuk setiap pengembang yang dipicu oleh insomnia.

Semakin saya utak-atik, semakin banyak kepala baru yang tumbuh pada bug hydra. Menjelang fajar, saya mempertanyakan pilihan karier saya (dan menenggak kopi ke-5 saya). Terdengar akrab? Inilah saya sebelum saya menemukan [CLAUDE.md](https://www.anthropic.com/engineering/claude-code-best-practices).

Maju cepat seminggu: Saya memulai proyek sampingan baru (SaaS React + Express kecil). Kali ini, saya mulai dengan membuat file [CLAUDE.md](https://www.anthropic.com/engineering/claude-code-best-practices) – senjata rahasia Anthropic untuk pengkodean AI agentik. Perbedaannya? Siang dan malam.

Proyek saya berikutnya tidak lepas kendali; proyek itu di-deploy dengan sempurna dalam waktu kurang dari 4 jam. Saya merasa seperti telah membuka mode dewa untuk pengkodean – seolah-olah Claude-magang yang kacau dan berkafein telah berubah menjadi arsitek perangkat lunak berpengalaman dalam semalam.

Saus rahasianya adalah memberi Claude seperangkat aturan dan konteks yang persisten sebelum kode apa pun dibuat. Itulah tepatnya yang dilakukan [CLAUDE.md](https://www.anthropic.com/engineering/claude-code-best-practices): ini adalah *"otak persisten"* proyek Anda, file Markdown yang secara otomatis menyuntikkan pengetahuan penting dan aturan pengkodean ke dalam setiap prompt Claude.

Dengan kata lain, CLAUDE.md berfungsi sebagai [memori jangka panjang Claude](https://github.com/anthropics/claude-cookbooks.git) – dimuat di awal setiap sesi – mencakup semuanya mulai dari tumpukan teknologi dan panduan gaya Anda hingga keanehan spesifik proyek tersebut.

**Mengapa ini penting?** *Karena AI agentik berkembang dalam konteks.* **Claude Code** berubah menjadi pemrogram pasangan yang tak kenal lelah. Faktanya, pengembang Anthropic sendiri menemukan bahwa tim dengan file CLAUDE.md yang disetel dengan baik mencapai eksekusi 2 – 3× lebih cepat pada tugas.

*Tidak perlu lagi menjelaskan kembali dasar-dasar proyek Anda setiap sesi;* CLAUDE.md membuat Claude selalu tahu. Ini seperti mempekerjakan pengembang baru yang membaca seluruh wiki dan basis kode sebelum menulis sebaris kode. *(Tidak heran 80% insinyur Anthropic menggunakan Claude Code setiap hari sekarang – mereka pada dasarnya memberinya transplantasi otak!)* Dan bagian terbaiknya?

Claude bahkan akan membuat draf CLAUDE.md awal untuk Anda dengan satu perintah – jalankan */init* dan saksikan ia menyusun ikhtisar proyek singkat yang dapat Anda sempurnakan.

**Jadi, apa sebenarnya yang harus dimasukkan ke dalam file ajaib ini?** Menurut panduan Anthropic *(dan pengalaman pribadi yang diperoleh dengan susah payah)*, CLAUDE.md sangat ideal untuk mendokumentasikan *"perintah umum, pola inti, panduan gaya, protokol pengujian, konvensi repo"* yang harus diingat oleh teman AI Anda.

Tujuannya adalah untuk menanamkan wawasan *"satu trik aneh"* yang mengubah bantuan kode biasa-biasa saja menjadi sahabat karib utama Anda. Di bawah ini, saya telah menyusun 10 entri CLAUDE.md pengubah permainan yang menaikkan level sesi Claude Code saya.

Setiap entri dilengkapi dengan skenario dunia nyata, cuplikan Markdown yang siap disalin-tempel, dan kiat pro untuk menyesuaikannya dengan kebutuhan Anda. Curi cuplikan ini *(saya tidak akan memberi tahu)*, letakkan di CLAUDE.md Anda, dan saksikan Claude berubah dari baik menjadi sangat tak terhentikan dalam pengkodean AI agentik. Mari kita selami!

## 1. Cetak Biru Arsitektur

Berikan Claude pandangan 10.000 kaki tentang struktur dan tumpukan teknologi aplikasi Anda di muka. Ketika saya pertama kali menjalankan */init* di [Claude Code](https://claude.com/product/claude-code), itu secara otomatis menghasilkan bagian Arsitektur yang terbaca seperti contekan arsitek.

Entri ini menjadi landasan CLAUDE.md saya. Dengan menguraikan desain tingkat tinggi – kerangka kerja, lapisan, dan bagaimana semuanya terhubung – saya memastikan Claude selalu membuat kode dengan mempertimbangkan rencana besar. Tidak ada lagi pencampuran pola MVC secara acak atau salah menempatkan file; Cetak Biru Arsitektur membuat Claude sadar akan "gambaran besar" sejak awal.

Contoh dunia nyata: Saya sedang membangun pelacak keuangan pribadi. Awalnya, Claude terus mencampurkan logika frontend dengan kode backend (ya ampun).

Setelah saya mendefinisikan arsitektur di CLAUDE.md – mis. Frontend React SPA, backend Express API, database SQLite – Claude secara ketat mengikuti pemisahan itu. Ia bahkan tahu di mana menempatkan modul baru tanpa saya beri tahu. Berikut adalah cuplikan ringkas yang terinspirasi oleh CLAUDE.md proyek itu:

### Arsitektur Inti

Proyek ini adalah Pelacak Keuangan Pribadi tumpukan penuh dengan frontend React dan backend [Node.js](https://nodejs.org/en)/[Express](https://expressjs.com/):

- **Frontend:** [Aplikasi satu halaman React 19 (Vite)](https://dev.to/a1guy/setting-up-your-react-19-development-environment-with-vite-4b7k) dengan UI berbasis komponen.
- **Backend:** Express.js REST API dengan database SQLite.
- **Database:** SQLite3 dengan tabel untuk `transactions`, `categories`, `savings_goals`.
- **Komunikasi:** Frontend memanggil backend di `http://localhost:3001/api/`.
- **Pola Desain:** Backend mengikuti MVC – rute untuk titik akhir API, model untuk operasi DB.

Entri *"cetak biru"* ini memberi tahu Claude persis bagaimana sistem kami ditata dan memberlakukan pola-pola utama (seperti MVC).

Seketika, pemrogram pasangan AI saya berhenti mengusulkan kode yang tidak sesuai dengan cetakan. Claude sekarang melihat hutan, bukan hanya pepohonan.

**Gambar:** File CLAUDE.md hierarkis memungkinkan Anda mengatur pengetahuan proyek di berbagai tingkatan – dari aturan global dan seluruh tim hingga pedoman spesifik proyek dan bahkan spesifik folder.

Claude secara otomatis menarik semua konteks CLAUDE.md yang berlaku, memprioritaskan panduan paling spesifik untuk setiap tugas.

**Kiat Pro:** Jika proyek Anda memiliki subsistem yang berbeda *(mis. frontend vs backend)*, pertimbangkan untuk menggunakan file CLAUDE.md bersarang di direktori tersebut untuk panduan yang lebih bertarget.

Claude akan menarik CLAUDE.md dari root dan yang ada di frontend/ saat mengerjakan kode UI, misalnya. Hierarki ini menjaga konteks tetap relevan dan ketat.

Juga, setiap kali Anda menyelesaikan refactor besar, minta Claude memperbarui bagian arsitektur *(Anda benar-benar dapat memberitahunya "perbarui bagian Arsitektur di CLAUDE.md untuk mencerminkan struktur modul baru kami")*. Menjaga cetak biru ini tetap terkini akan membuahkan hasil dalam kualitas kode!

## 2. Pusat Komando

Jangan biarkan Claude lupa cara membangun, menjalankan, atau menguji aplikasi Anda. Salah satu poin masalah pertama yang saya perbaiki adalah Claude tidak mengetahui skrip dev proyek saya. *(Terkadang ia bertanya "Bagaimana cara menjalankan aplikasi?")*.

Entri Pusat Komando adalah daftar sederhana dari perintah umum dan fungsinya. Ini menghindarkan Claude dari memindai package.json atau Makefile Anda berulang kali dan mempercepat iterasinya.

Anggap saja sebagai contekan untuk semua tugas CLI di proyek Anda.

**Contoh dunia nyata:** Di API Node saya, saya menambahkan bagian *"Perintah Bash"* yang mencantumkan npm run dev, npm run test, npm run lint dengan deskripsi. Tiba-tiba, Claude berhenti menebak-nebak dan mulai menjalankan perintah yang benar secara otomatis. Ketika saya memintanya untuk menjalankan tes, ia sudah tahu untuk menggunakan npm run test *(dan bahkan pustaka pengujian apa yang digunakan)*.

**Berikut tampilan cuplikan Pusat Komando:**

**Perintah Bash**

- `npm run dev` – Memulai server pengembangan (memuat ulang secara otomatis saat ada perubahan kode).
- `npm run build` – Membangun proyek untuk produksi (output ke folder `dist/`).
- `npm run test` – Menjalankan rangkaian pengujian (menggunakan Jest dengan cakupan).
- `npm run lint` – Melakukan lint pada semua file menggunakan ESLint (menegakkan standar pengkodean).

Dengan mendokumentasikan ini, Anda memastikan Claude selalu menggunakan mantra yang benar. Tidak ada lagi momen *"berfungsi di mesin saya"* karena AI menjalankan perintah yang salah.

**Seperti yang disarankan oleh para insinyur Anthropic:** dokumentasikan alat dan skrip yang sering Anda gunakan di CLAUDE.md sehingga Claude dapat menggunakannya tanpa ragu-ragu.

**Kiat Pro:** Sertakan versi alat atau keanehan lingkungan jika relevan. Misalnya, tentukan *"Gunakan Node 18"* atau *"Membutuhkan Python 3.11 venv"* di bagian ini jika penyiapan Anda rumit. Claude kemudian akan secara proaktif menangani penyiapan lingkungan saat menulis kode.

Juga, jika Anda menemukan Claude meminta izin atau konfirmasi untuk tugas-tugas rutin *(seperti menjalankan tes)*, Anda dapat mendahuluinya dengan memasukkan perintah aman ke dalam daftar putih. *(Saya pribadi menjalankan Claude Code dengan flag –dangerously-skip-permissions di dev, tetapi lakukan ini hanya jika Anda mempercayai CLAUDE.md dan tes Anda!)*.

Kuncinya adalah merampingkan akses Claude ke alur kerja Anda – berikan kunci ke Pusat Komando Anda dan saksikan ia bekerja.

## 3. Sheriff Panduan Gaya

Jaga agar gaya kode Anda tetap konsisten, tidak peduli siapa (atau apa) yang menulis kode. Tidak ada yang lebih buruk daripada asisten AI yang mengubah gaya pengkodean di tengah proyek – satu menit menggunakan snake_case, menit berikutnya camelCase; atau mencampur tab dan spasi (gasp!).

Untuk mencegah kekacauan seperti itu, saya menunjuk Sheriff Panduan Gaya di CLAUDE.md saya. Entri ini menetapkan hukum tentang gaya dan konvensi kode: *dari preferensi sintaks hingga pola penamaan.*

**Contoh dunia nyata:** Proyek React saya memiliki aturan ESLint yang ketat *(kutipan tunggal, inden 2 spasi, titik koma, dll.)*. Awalnya, Claude akan menghasilkan kode yang melanggar beberapa aturan lint, yang berarti pekerjaan perbaikan tambahan.

Saya menambahkan poin-poin seperti *"Gunakan sintaks ES6+ (tidak ada panggilan require CommonJS)"* dan *"Ikuti aturan ESLint kami (inden 2 spasi, kutipan tunggal, tanpa titik koma)"* ke CLAUDE.md. Ajaibnya, output Claude mulai sesuai dengan standar ini tanpa pengingat.

Sepertinya ia menginternalisasi konfigurasi prettier kami. Berikut adalah contoh cuplikannya:

### Pedoman Gaya Kode

- **Sintaks:** Gunakan Modul ES (`import`/`export`) daripada CommonJS. Gunakan fitur ES6+ modern (fungsi panah, dll.) jika sesuai.
- **Pemformatan:** Gunakan 2 spasi untuk indentasi. Gunakan kutipan tunggal untuk string. **Tidak ada** titik koma di akhir *(kami menjalankan Prettier)* – kecuali jika diperlukan dalam TypeScript *(enum, antarmuka)*.
- **Penamaan:** Gunakan `camelCase` untuk variabel/fungsi, `PascalCase` untuk komponen dan kelas React. Konstanta dalam `UPPER_SNAKE_CASE`.
- **Pola:** Lebih suka komponen fungsional dengan kait daripada komponen kelas di React. Hindari penggunaan API yang sudah usang.

Ini memberi Claude kompas gaya. Setelah menambahkan bagian gaya, saya melihat lebih sedikit cerewet selama peninjauan kode – permintaan tarik Claude mulai lolos dari linter dan terlihat seragam.

[Praktik terbaik resmi Claude Code](https://www.anthropic.com/engineering/claude-code-best-practices) secara eksplisit merekomendasikan untuk menempatkan aturan gaya kode Anda di CLAUDE.md karena alasan ini. Konsistensi adalah ratu dalam kode yang dapat dipelihara, dan sekarang Claude mengawasinya untuk saya.

**Kiat Pro:** Terapkan nada dalam komentar dan pesan komit juga. Jika Anda memiliki standar untuk komentar kode atau deskripsi PR (mis. format JSDoc, atau "harus menyertakan ID tiket Jira dalam pesan komit"), catat itu.

[Claude](https://claude.com/product/claude-code) kemudian akan menyertakan komentar yang terbentuk dengan baik dan bahkan memformat komit git-nya sesuai. Salah satu entri saya mengatakan *"Awali semua pesan komit dengan ID tiket dan cakupan singkat (mis. '[PAY-123] feat: …')".* Lihatlah, Claude mulai membuat pesan komit seperti pengembang berpengalaman. Sheriff Panduan Gaya bukan hanya tentang titik koma dan kurung – Anda dapat memperluasnya ke konvensi apa pun yang Anda pedulikan.

## 4. Pelatih Meja Uji

Jadikan pengujian sebagai warga negara kelas satu dengan mendorong Claude untuk berpikir test-first. Jika Anda seperti saya, menulis tes bisa luput dari perhatian saat Anda sedang fokus.

[Claude Code](https://claude.com/product/claude-code) suka membuat tes – terutama jika Anda secara eksplisit meminta atau mengingatkannya. Saya menambahkan bagian Instruksi Pengujian di CLAUDE.md untuk memastikan bahwa untuk setiap fitur atau perbaikan bug, Claude menulis atau memperbarui tes sebagai bagian dari alur kerjanya.

**Skenario dunia nyata:** Saat melakukan pemrograman berpasangan pada modul manajemen status Redux, saya ingin memastikan bahwa reducer baru memiliki tes unit. Saya menempatkan panduan di CLAUDE.md seperti *"Selalu sertakan tes untuk fitur baru"* dan spesifik seperti *"Gunakan Jest dan React Testing Library untuk tes UI."*

**Efeknya:** setelah mengimplementasikan komponen React, Claude akan segera menyarankan untuk membuat file tes yang sesuai, seringkali tanpa saya minta. Ini pada dasarnya adalah dorongan lembut yang tertanam dalam setiap prompt.

**Berikut tampilan entri Pelatih Meja Uji:**

### Instruksi Pengujian

- Selalu ikuti **pola pikir TDD**: untuk setiap perbaikan bug atau fitur baru, pertimbangkan untuk menulis tes terlebih dahulu atau segera setelah pengkodean.
- Gunakan **Jest** untuk tes unit. Untuk komponen React, gunakan @testing-library/react untuk rendering dan pernyataan.
- Bertujuan untuk cakupan tinggi pada logika inti (layanan, reducer, dll.). Sertakan kasus tepi (input tidak valid, status kesalahan) dalam tes.
- **Penamaan Tes:** gunakan blok `describe` untuk modul dan `it('should …')` untuk perilaku. Jaga agar tes tetap jelas dan terfokus.
- Jalankan tes dengan `npm run test` dan pastikan semua lolos sebelum menganggap tugas selesai.

Entri ini mengubah [Claude](https://claude.com/product/claude-code) menjadi sersan bor yang sopan: Saya akan melihatnya secara otomatis menyarankan *"Saya sekarang akan menulis tes untuk X"* setelah menyelesaikan sebuah fungsi.

Perlu dicatat bahwa Anthropic menyarankan untuk mendokumentasikan kerangka kerja dan praktik pengujian di CLAUDE.md, karena ini mengarahkan rantai pemikiran Claude ke arah kualitas. Anda secara efektif melatih AI untuk mengadopsi budaya pengujian.

**Kiat Pro:** Manfaatkan sifat tak kenal lelah Claude untuk pengujian yang mendalam. Tambahkan baris seperti *"Jika waktu memungkinkan, buat tes tambahan untuk kasus tepi dan regresi potensial."*

Claude kemudian akan sering melampaui batas, menulis tes tambahan yang bahkan mungkin saya lupakan *(pernah menguji fungsi pada jam 2 pagi? Claude akan melakukannya!)*. Beberapa pengembang bahkan menyertakan prompt di CLAUDE.md untuk tes berbasis properti atau tes fuzz untuk bagian-bagian penting.

Ingat, Claude dapat memikirkan dan menjalankan tes dengan cepat, jadi doronglah. Diri Anda di masa depan *(dan tim QA Anda)* akan berterima kasih.

## 5. Mantra Penanganan Kesalahan

Ajari Claude untuk men-debug dan menangani kesalahan seperti insinyur berpengalaman. Entri ini adalah pengubah permainan pribadi. Saya menyebutnya Mantra Penanganan Kesalahan – seperangkat pedoman yang mendorong Claude untuk mendekati bug dan pengecualian secara metodis, daripada menempelkan perbaikan sementara.

Mantra ini biasanya masuk ke CLAUDE.md sebagai daftar periksa singkat atau filosofi, mengingatkan AI untuk berpikir langkah demi langkah saat menghadapi kesalahan.

**Contoh dunia nyata:** Saya pernah meminta Claude merefaktor panggilan API, dan itu memperkenalkan bug halus. Alih-alih menjelaskan seluruh konteks aplikasi lagi, saya mengandalkan mantra CLAUDE.md saya: *"Ketika terjadi kesalahan, analisis akar penyebabnya langkah demi langkah sebelum mengusulkan perbaikan."*

Hasilnya? Claude menghasilkan penjelasan rantai pemikiran tentang kemungkinan penyebabnya *(tipe argumen yang salah)*, kemudian menyarankan perbaikan, lengkap dengan peringatan konsol yang bijaksana. Saya pada dasarnya mendapatkan debugger bebek karet bawaan.

**Cuplikan Mantra Penanganan Kesalahan saya terlihat seperti ini:**

Penanganan & Debugging Kesalahan

- **Diagnosis, Jangan Menebak:** Saat menemukan bug atau tes yang gagal, pertama-tama jelaskan kemungkinan penyebabnya langkah demi langkah: [docs.claude.com](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought%23:~:text=,where%20prompts%20may%20be%20unclear). Periksa asumsi, input, dan jalur kode yang relevan.
- **Penanganan yang Anggun:** Kode harus menangani kesalahan dengan anggun. Misalnya, gunakan try/catch di sekitar panggilan asinkron, dan kembalikan pesan kesalahan yang ramah pengguna atau nilai fallback jika sesuai.
- **Pencatatan:** Sertakan log konsol atau log kesalahan yang bermanfaat untuk kegagalan kritis (tetapi hindari spam log dalam kode produksi).
- **Tidak Ada Kegagalan Senyap:** Jangan menelan pengecualian secara diam-diam. Selalu munculkan kesalahan baik dengan melemparkannya atau mencatatnya.

Entri ini menyetel perilaku Claude dalam kondisi kegagalan. Setelah menambahkannya, saya melihat Claude lebih sering menangkap kesalahannya sendiri.

Ia akan mengatakan *"Saya perhatikan ini bisa menimbulkan kesalahan yang tidak terdefinisi, saya akan menambahkan pemeriksaan"* tanpa dorongan saya. Intinya, AI mulai berpikir seperti pengembang yang sedang berburu bug, dan itulah yang kami inginkan.

**Di atas:** Perbedaan sebelum/sesudah dari kode saya di mana Claude menerapkan penanganan kesalahan yang lebih baik. *"Setelah"* (hijau) menunjukkan Claude menambahkan validasi input *(if (!name) throw…)* dan menggunakan string template untuk output, mengikuti Mantra Penanganan Kesalahan untuk tidak melanjutkan dengan nama yang hilang.

**Kiat Pro:** Pinjam teknik dari debugger berpengalaman. Misalnya, tambahkan aturan seperti *"Selalu gunakan React Error Boundaries di sekitar komponen yang melakukan panggilan API"* jika Anda berada dalam konteks React – ini berasal dari CLAUDE.md saya setelah kegagalan produksi, dan itu terinspirasi oleh kiat pro yang saya lihat online.

Claude kemudian secara otomatis membungkus komponen berisiko dalam komponen <ErrorBoundary> di salah satu proyek saya!

Juga, jangan malu-malu mengajari Claude strategi debugging: mis., *"Pada bug kritis, pertimbangkan pencarian biner melalui riwayat git atau tambahkan pernyataan console.debug sementara untuk mengisolasi masalah."*

Kedengarannya gila untuk memberi tahu AI ini, tetapi saya pernah meminta Claude menyarankan untuk membagi dua kode setelah membaca pedoman itu. Mantra ini menanamkan pendekatan yang hati-hati dan sistematis yang akan menyelamatkan Anda saat terjadi kesalahan.

## 6. Perintah Kode Bersih

Kodekan prinsip-prinsip *"kode bersih"* Anda sehingga Claude menulis kode yang dapat dipelihara dan ramah manusia secara default. Anggap ini seperti mengatur hati nurani pemrogram pasangan Anda. Kita semua memiliki kekesalan dalam peninjauan kode – fungsi yang terlalu panjang, variabel bernama data atau foo, logika yang sangat bersarang, dll.

Saya mengubah aturan tak tertulis itu menjadi entri CLAUDE.md yang eksplisit, dan efeknya langsung terasa: kode Claude menjadi terasa lebih bersih dan lebih modular. Bukan lelucon, churn diff saya turun karena saya tidak terus-menerus merefaktor kode yang ditulis AI untuk kejelasan.

**Contoh dunia nyata:** Pada satu titik, Claude menghasilkan fungsi 150 baris.

Aturan saya adalah *"tidak ada fungsi yang boleh lebih dari ~40 baris"*. Jadi saya menambahkan pedoman Kode Bersih: *"Batasi panjang fungsi; refactor fungsi besar menjadi pembantu yang lebih kecil dengan nama yang jelas."* Lain kali, Claude secara otomatis membagi rutin yang panjang menjadi beberapa fungsi dengan nama yang baik tanpa saya minta.

Saya juga menambahkan perintah penamaan (*"Beri nama fungsi dengan jelas, mis. calculateInvoiceTotal, bukan handleData"*). Kode itu mulai terbaca seperti buku yang ditulis oleh Paman Bob sendiri.

### **Cuplikan Perintah Kode Bersih saya:**

### Pedoman Kode Bersih

- **Ukuran Fungsi:** Bertujuan untuk fungsi ≤ 50 baris. Jika sebuah fungsi melakukan terlalu banyak, pecah menjadi fungsi pembantu yang lebih kecil.
- **Tanggung Jawab Tunggal:** Setiap fungsi/modul harus memiliki satu tujuan yang jelas. Jangan menggabungkan logika yang tidak terkait.
- **Penamaan:** Gunakan nama deskriptif. Hindari nama generik seperti `tmp`, `data`, `handleStuff`. Misalnya, lebih suka `calculateInvoiceTotal` daripada `doCalc`.
- **Prinsip DRY:** Jangan duplikat kode. Jika logika serupa ada di dua tempat, refactor menjadi fungsi bersama (atau klarifikasi mengapa keduanya membutuhkan implementasi sendiri).
- **Komentar:** Jelaskan logika yang tidak jelas, tetapi jangan terlalu banyak mengomentari kode yang sudah jelas. Hapus semua sisa debug atau kode yang dikomentari.

Setelah ini, saya melihat Claude mengoreksi sendiri hal-hal seperti: *"Saya perhatikan fungsi ini menjadi besar, saya akan merefaktor sebagian menjadi formatAddress() pembantu baru.*

Dalam satu kasus, ia menemukan kode duplikat di dua layanan mikro dan menyarankan untuk mengabstraksikannya – semua karena prinsip DRY secara eksplisit ada dalam konteksnya. Intinya, Anda menanamkan kebijaksanaan insinyur senior Anda ke dalam kesadaran semu Claude.

**Kiat Pro:** Sertakan "gotchas" atau bau kode spesifik apa pun yang unik untuk proyek Anda. Misalnya, di satu basis kode kami memiliki aturan yang melarang penggunaan moment.js *(kami menggunakan Day.js sebagai gantinya).*

Saya menambahkan: *"Jangan gunakan pustaka moment (gunakan Day.js untuk penanganan tanggal)."*

Benar saja, Claude berhenti menyarankan moment sama sekali. Jika ada anti-pola yang tidak pernah ingin Anda lihat (seperti menggunakan any di [TypeScript](https://www.typescriptlang.org/), atau variabel global, atau menyalin kode dari [StackOverflow](https://stackoverflow.com/questions) tanpa atribusi), tulislah.

Claude umumnya akan mematuhinya. Anggap ini sebagai tes unit untuk output Claude – jika melanggar Perintah, Anda punya alasan untuk mengatakan *"Claude nakal, coba lagi!"* Tetapi menurut pengalaman saya, jarang sekali terjadi setelah melihat pedoman ini.

## 7. Penjaga Keamanan

Tunjuk Claude sebagai penjaga keamanan Anda dengan mencantumkan praktik terbaik keamanan yang penting. Entri CLAUDE.md ini memastikan bahwa teman AI Anda membuat kode dengan memperhatikan kerentanan dan praktik yang aman – area di mana model gaya GPT sering kekurangan konteks.

Dengan bersikap eksplisit tentang keamanan (validasi input, enkripsi, dll.), saya membuat Claude menangkap masalah keamanan yang mungkin saya lewatkan dengan tergesa-gesa.

**Skenario dunia nyata:** Saat mengerjakan alur otentikasi pengguna, saya menulis pedoman tentang penanganan kata sandi: *"Selalu hash kata sandi dengan bcrypt, jangan pernah menyimpan teks biasa; validasi format email; terapkan pembatasan laju pada upaya login,"* dll.

Saya tidak bercanda – Claude kemudian memasukkan validasi input untuk email dan bahkan mengingatkan saya untuk menggunakan kueri SQL berparameter di salah satu output, tanpa diminta. Ini seperti memiliki alat OWASP ZAP yang tertanam di asisten pengkodean Anda.

Di lain waktu, di aplikasi React, saya menambahkan catatan: *"Sanitasi konten HTML apa pun untuk mencegah XSS (gunakan DOMPurify)."* Setelah itu, setiap kali kami berurusan dengan dangerouslySetInnerHTML, Claude secara otomatis menyarankan penggunaan DOMPurify. Pikiran saya meledak.

**Berikut adalah contoh entri Penjaga Keamanan:**

### Pedoman Keamanan

- **Validasi Input:** Validasi semua input (terutama dari pengguna atau API eksternal). Jangan pernah mempercayai input pengguna – mis., periksa format email yang valid, batas panjang string, dll.
- **Otentikasi:** Jangan pernah menyimpan kata sandi dalam teks biasa. Gunakan bcrypt dengan salt untuk hashing kata sandi. Terapkan penguncian akun atau pembatasan laju pada upaya login yang gagal berulang kali.
- **Keamanan Database:** Gunakan kueri berparameter atau ORM untuk mencegah injeksi SQL. Jangan menggabungkan input pengguna dalam kueri SQL secara langsung.
- **XSS & CSRF:** Sanitasi konten HTML atau buatan pengguna apa pun sebelum rendering (pertimbangkan untuk menggunakan pustaka seperti DOMPurify). Gunakan token CSRF untuk pengiriman formulir yang mengubah status.
- **Dependensi:** Hati-hati dengan eval atau menjalankan kode dinamis. Hindari memperkenalkan paket dengan kerentanan yang diketahui (Claude harus lebih memilih solusi bawaan jika pustaka eksternal berisiko).

Ini mungkin tampak berat, tetapi Claude dapat menanganinya – dan itu akan menegakkan aturan ini dengan tekun. Tim internal Anthropic sendiri mencatat bahwa Claude sering menemukan bug dan potensi kerentanan yang diabaikan manusia, jadi memberinya buku aturan keamanan membuatnya semakin efektif.

Saya telah melihat Claude menolak untuk mengimplementasikan sesuatu dengan cara yang tidak aman karena "Pedoman Keamanan mengatakannya." Misalnya, ia tidak akan menggunakan localStorage untuk JWT tanpa saya izinkan secara eksplisit, dengan alasan masalah keamanan (saya kesal dan terkesan pada saat yang sama!).

**Kiat Pro:** Perbarui bagian ini saat ancaman baru muncul atau saat menggunakan teknologi baru. Jika Anda beralih menggunakan AWS S3, tambahkan baris seperti *"Pastikan bucket S3 diakses dengan hak istimewa paling rendah dan tidak ada ACL publik."* Claude kemudian akan memperhatikan hal itu saat membuat kode IaC atau backend. Penjaga Keamanan memberi Anda ketenangan pikiran – seolah-olah Anda telah menyewa konsultan keamanan yang meninjau setiap baris saat ditulis. Pada tahun 2025, di mana pengkodean AI agentik sedang meningkat, entri ini adalah jaring pengaman Anda terhadap penyebaran kerentanan secara tidak sengaja.

## 8. Protokol Kerja Tim

Jaga agar Claude selaras dengan konvensi kolaborasi tim Anda – dari etiket Git hingga dokumentasi. Entri ini membahas aspek *"lunak"* dari pengkodean yang tetap penting untuk pengalaman pengembang yang lancar. Lagi pula, pengkodean bukan hanya menulis fungsi – ini juga menulis pesan komit, melakukan peninjauan kode, dan memperbarui dokumen. Dengan mengajari Claude alur kerja tim Anda, Anda mendapatkan AI yang tidak hanya membuat kode dalam ruang hampa tetapi benar-benar bertindak sebagai anggota tim.

**Contoh dunia nyata:** Tim kami memiliki konvensi seperti membuat cabang dari dev untuk fitur, mengawali pesan komit dengan ID tiket, dan memperbarui CHANGELOG.md untuk perubahan penting. Saya mengkodekan ini di CLAUDE.md.

Hasilnya? Ketika Claude menyelesaikan implementasi fitur, ia secara otomatis memformat pesan komit dengan sempurna *(mis., "feat(login): add Google OAuth support (RES-102)")* dan bahkan menambahkan poin ke changelog kami sekaligus. Saya duduk di sana dengan mulut ternganga. Demikian pula, saya menambahkan: *"Dokumentasikan titik akhir baru di dokumen API markdown."* Benar saja, setelah membuat rute API baru, Claude menambahkan cuplikan rapi di docs/api.md yang menjelaskan titik akhir.

**Templat untuk Protokol Kerja Tim mungkin:**

### Kolaborasi & Alur Kerja

- **Cabang Git:** Ikuti GitFlow lite – buat cabang fitur dari `dev` (mis., `feature/login-form`), gabungkan melalui Pull Request. **Jangan** melakukan komit langsung ke `main`.
- **Pesan Komit:** Gunakan komit konvensional (mis., awalan `feat: `, `fix: `, `docs: `). Sertakan ID tiket JIRA dalam komit jika tersedia. Jaga agar pesan tetap ringkas (ringkasan satu baris, detail opsional setelahnya).
- **Pull Request:** Ketika tugas selesai, minta Claude membuka PR dengan deskripsi singkat tentang perubahan dan menandai peninjau yang relevan (mis., `@frontend-team` untuk perubahan UI).
- **Dokumentasi:** Jika perubahan kode memengaruhi perilaku yang dihadapi pengguna atau API, perbarui dokumen Markdown yang relevan di folder `docs/` sebagai bagian dari PR yang sama.
- **Peninjauan Kode:** Claude harus membantu dalam peninjauan kode jika diminta (mis., analisis statis untuk bug, memastikan kepatuhan panduan gaya) dan hanya menyetujui ketika semua pemeriksaan lolos.

Dengan menjelaskan ekspektasi ini, saya secara efektif membuat Claude menangani hal-hal membosankan yang sering luput dari perhatian. Ia mulai menulis catatan rilis untuk saya *("Menambahkan fitur X, memperbaiki bug Y")* saat mendorong PR, karena saya telah menyebutkan pembaruan dokumen dan changelog.

Praktik terbaik Anthropic mengisyaratkan untuk menyertakan etiket repositori dan catatan alur kerja di CLAUDE.md – yang persis seperti ini. Ini mengubah Claude dari sekadar generator kode menjadi asisten pengembang yang lebih holistik.

**Kiat Pro:** Gunakan Claude untuk orientasi anggota tim baru. Dengan Protokol Kerja Tim yang terperinci, pengembang baru (manusia) dapat benar-benar membaca CLAUDE.md untuk mendapatkan pengantar singkat tentang "cara kami bekerja di sini." Saya telah membagikan CLAUDE.md kami dengan para magang, dan mereka merasa itu lebih membantu daripada wiki perusahaan.

Juga, pertimbangkan untuk menambahkan baris yang menyenangkan seperti *"Tim kami menghargai kode bersih dan membantu orang lain – Claude harus memberi semangat dalam nada selama penjelasan."* Percaya atau tidak, AI akan mengadopsi nada ramah dalam komentar dan outputnya, yang membuat pengalaman pengembang lebih menyenangkan.

Bagian protokol ini menjadikan Claude kolaborator sejati, bukan hanya monyet kode.

## 9. Orakel Kasus Tepi

Pastikan tidak ada kasus sudut yang tidak dipertimbangkan dengan menginstruksikan Claude untuk selalu memikirkan kondisi tepi. Entri ini mendorong Claude untuk melampaui "jalur bahagia" dan mengantisipasi skenario yang mungkin dilewatkan oleh pengembang junior. Ini seperti memiliki insinyur senior yang tanpa henti bertanya *"Tapi bagaimana jika…?"* untuk setiap perubahan, yang secara dramatis meningkatkan ketahanan.

**Skenario dunia nyata:** Saya menambahkan catatan di CLAUDE.md: *"Untuk setiap fitur non-sepele, daftarkan kasus tepi potensial dan tangani."* Saat membangun pemilih rentang tanggal, Claude menemukan kasus tepi seperti "Bagaimana jika tanggal akhir sebelum tanggal mulai?" dan mengimplementasikan pemeriksaan untuk menukarnya.

Saya bahkan belum memikirkannya! Pada kesempatan lain, untuk modul kalkulasi keuangan, ia bertanya *"Bagaimana jika inputnya bisa diabaikan pada awalnya.*

Tim internal Anthropic melaporkan manfaat serupa: menangkap kasus tepi dalam desain daripada dalam produksi. Jadi mari kita masukkan kebijaksanaan itu ke dalam entri Orakel kita.

**Contoh cuplikan:**

### Pertimbangan Kasus Tepi

- Selalu pertimbangkan kasus tepi dan sudut untuk logika apa pun:
- Input kosong atau nol (mis., daftar kosong, bidang yang hilang, nilai nol).
- Nilai maks/min dan luapan (mis., angka yang sangat besar, teks yang sangat panjang).
- Status tidak valid (mis., tanggal akhir sebelum tanggal mulai, kuantitas negatif).
- Masalah konkurensi (mis., dua pengguna mengedit data yang sama secara bersamaan).
- Jika kasus tepi diidentifikasi, tangani dalam kode atau setidaknya tandai dengan komentar/TODO.
- Lebih suka gagal cepat pada input buruk (lemparkan kesalahan atau kembalikan default yang aman) daripada melanjutkan dengan asumsi yang salah.

**Kiat Pro:** Dorong Claude untuk mengartikulasikan kasus tepi dalam mode perencanaan. Jika Anda menggunakan kemampuan *"berpikir"* atau merencanakan Claude, memiliki entri Orakel ini akan mendorongnya untuk menyebutkan kasus tepi selama langkah perencanaan. Ini berarti Anda akan mendapatkan daftar periksa skenario untuk diuji atau diperhitungkan sebelum menulis kode. Anda bahkan dapat memformalkannya: tambahkan

**"Langkah 2: Brainstorming kasus tepi"** dalam cetak biru tentang cara mendekati masalah *(lihat bagian berikutnya tentang pagar pembatas alur kerja)*. Kemudian Claude akan secara sistematis menghasilkan daftar itu. Lebih baik menangkap hal-hal aneh di muka daripada jam 3 pagi di malam peluncuran, bukan?

## 10. Pagar Pembatas Alur Kerja Agentik

Pandu Claude dalam mengatur tugas-tugas kompleks dan multi-langkah dengan memecahnya dan memverifikasi setiap langkah. Entri terakhir ini seperti peretasan meta yang menyatukan semuanya.

[Claude Code](https://claude.com/product/claude-code) adalah alat pengkodean AI agentik – artinya ia tidak hanya dapat menulis kode tetapi juga merencanakan, melaksanakan, dan menyesuaikan dalam alur kerja multi-langkah. Entri Pagar Pembatas Alur Kerja memberi tahu Claude bagaimana cara memecahkan masalah besar daripada langsung terjun.

Ini pada dasarnya adalah nasihat proses: rencanakan, laksanakan sebagian, tinjau, sesuaikan – cara yang sama seperti pengembang senior akan menangani proyek besar.

**Contoh dunia nyata:** Saya menugaskan Claude untuk menambahkan fitur utama (alur login OAuth2 penuh). Alih-alih membiarkannya mencoba semuanya sekaligus (yang bisa gagal secara spektakuler), saya memanfaatkan Pagar Pembatas.

**Di CLAUDE.md, saya punya sesuatu seperti:** *"Untuk tugas besar, ikuti pendekatan 3 langkah – Analisis → Rencana → Implementasi. Selalu usulkan rencana terlebih dahulu untuk persetujuan."* Jadi ketika saya meminta Claude untuk fitur OAuth, pertama-tama ia merespons dengan rencana terstruktur *(daftar langkah: buat klien OAuth, tambahkan titik akhir panggilan balik, tangani token, dll.)*. Kami mengulangi rencana itu *(saya menambahkan langkah untuk token penyegaran)*.

Baru kemudian Claude menulis kode, dan melakukannya secara modular *(secara harfiah dikatakan, "Saya akan mengimplementasikan langkah 1 sekarang…" dan seterusnya).* Hasilnya bersih dan berfungsi pada proses pertama. Tanpa pagar pembatas, saya curiga itu akan menjadi tumpukan kode monolitik dan kemungkinan besar kesalahan.

Berikut adalah versi ringkas dari entri Pagar Pembatas Alur Kerja Agentik:

### Pedoman Alur Kerja & Perencanaan

- Untuk tugas yang kompleks atau multi-langkah, Claude harus terlebih dahulu mengeluarkan rencana atau garis besar pendekatan yang jelas [anthropic.com](https://www.anthropic.com/engineering/claude-code-best-practices%23:~:text=early%20on%20in%20a%20conversation,reset%20to%20this%20spot%20if). *(Mis., daftar langkah atau modul yang dibutuhkan)*.
- **Pengembangan Inkremental:** Implementasikan dalam potongan-potongan logis. Setelah setiap potongan, verifikasi keselarasan dengan rencana dan lolos tes sebelum melanjutkan.
- Berpikir Keras: Gunakan penalaran yang diperluas *("berpikir lebih keras atau ultrathink")* untuk keputusan yang kompleks. Tidak apa-apa menghabiskan lebih banyak token untuk memastikan pendekatan yang solid daripada terburu-buru membuat kode.
- **Persetujuan Pengguna:** Jeda untuk konfirmasi setelah memberikan rencana atau keputusan desain utama. Lanjutkan hanya setelah pengguna/pengembang mengonfirmasi.
- **Pemulihan Kesalahan:** Jika solusi tidak berhasil, Claude harus mundur dan berpikir ulang daripada bertahan dengan keras kepala. Pertimbangkan pendekatan alternatif jika tes gagal atau batasan tercapai.

Pagar pembatas ini secara dramatis meningkatkan tingkat keberhasilan Claude pada tugas-tugas besar.

Ini pada dasarnya mengikuti siklus tangkas mini sekarang: *usulkan -> dapatkan umpan balik -> implementasikan -> tinjau.*

Ini didukung oleh rekomendasi Anthropic sendiri – mereka mengamati bahwa memaksa Claude untuk meneliti dan merencanakan sebelum membuat kode *"secara signifikan meningkatkan kinerja untuk tugas yang lebih dalam"*.

Saya dapat mendukung itu: kode yang saya dapatkan dengan pendekatan ini tidak hanya lebih benar, tetapi seringkali direkayasa dengan lebih baik *(Claude sebenarnya akan mengatakan "Saya akan membuat kelas pembantu untuk konfigurasi OAuth" karena punya waktu untuk memikirkan desain).*

**Kiat Pro:** Tentukan kata pemicu khusus untuk mode. Misalnya, saya menambahkan: *"Jika saya mengatakan 'Mari kita brainstorming', masuk ke Mode Rencana."* Dengan cara ini Claude tahu kapan saya secara eksplisit meminta rencana vs. kode.

Anda juga dapat mengintegrasikan strategi sub-agen Anda di sini (jika Anda menggunakannya) – mis., instruksikan Claude untuk memunculkan sub-agen *"Pelari Tes"* bila diperlukan, dll.

Kiat lain yang berguna: minta Claude merangkum rencana dalam file (seperti PLAN.md) yang dapat Anda rujuk kembali atau bahkan sertakan melalui referensi @filename. Ini menjaga ukuran konteks tetap kecil.

Pada akhirnya, Pagar Pembatas Alur Kerja memastikan Claude berperilaku lebih seperti mitra proyek daripada pengembang junior yang terlalu bersemangat. Ia akan mengatur kecepatan, memeriksa ulang, dan membuat Anda tetap terhubung di setiap tahap. Dengan kata lain, ia membuat kode seperti seorang insinyur, bukan hanya generator kode.

---

Siap untuk meningkatkan sesi Claude Code Anda sendiri? Curi templat dan tweak CLAUDE.md saya ([tautan di bio](https://github.com/alirezarezvani/agentx)), sesuaikan dengan tumpukan Anda, dan letakkan di repo Anda.

Sejak saat itu, setiap prompt yang Anda berikan kepada Claude akan membawa bobot pengetahuan dan standar kolektif proyek Anda. Hasilnya, Anda akan menghasilkan kode siap produksi dengan kecepatan kilat – saya berbicara tentang pengiriman dalam hitungan jam yang dulu memakan waktu berminggu-minggu.

Pada tahun 2026, saya memperkirakan setiap repo pengembang akan memiliki CLAUDE.md – atau tertinggal. Ini adalah saus rahasia baru bagi mereka yang tahu. Jika Anda telah membaca sejauh ini, Anda sekarang termasuk di antara mereka.

Pergilah dan bangun hal-hal luar biasa dengan sahabat AI Anda! Dan setelah Anda mencoba peretasan ini, kembalilah dan pamer: apa entri CLAUDE.md andalan Anda? Tulis di komentar – saya benar-benar bersemangat untuk mempelajari trik baru dari komunitas yang luar biasa ini.

Selamat membuat kode!

---

**Atau lihat Panduan Utama baru saya untuk Pengembangan Berbasis Spesifikasi:**

👉 **Langkah 1:** Baca Panduan Utama ini — pusat sumber daya abadi Anda untuk Pengembangan Berbasis Spesifikasi.
👉 **Langkah 2:** [Baca Bagian 1: Fondasi untuk menyiapkan sistem memori, konstitusi, dan alur kerja spesifikasi Anda.](https://alirezarezvani.medium.com/7-steps-how-to-stop-claude-code-from-building-the-wrong-thing-part-1-the-foundation-of-2d2c9c1a99f1)
👉 **Langkah 3:** [Lanjutkan dengan Bagian 2: Eksekusi dan Penskalaan untuk mengubah spesifikasi menjadi rencana, tugas, dan fitur yang diuji.](https://alirezarezvani.medium.com/7-steps-how-to-stop-claude-code-from-building-the-wrong-thing-part-2-execution-results-and-d990ef7d92db)

### Panduan pengkodean agentik baru saya:

👉 [BUKU PEDOMAN PEMBUAT SDK AGEN CLAUDE — Bagian 1](https://alirezarezvani.medium.com/the-claude-agent-sdk-builders-playbook-build-your-first-autonomous-agent-in-30-minutes-88a1952f637e)

*Atau baca tentang pengalaman saya menggunakan prompt yang telah saya bagikan dengan Anda di artikel ini:* [Saya Memberi Claude Code 2.0 Refactor 3 Minggu Kami pada Jam 11 Malam. Pada Jam 7 Pagi, Selesai](https://medium.com/@alirezarezvani/i-gave-claude-code-2-0-our-3-week-refactor-at-11-pm-at-7-am-it-was-done-34decd54e441)

### Tentang Penulis

**Alireza Rezvani** adalah Chief Technology Officer, Arsitek Full-stack Senior, dan Insinyur Perangkat Lunak, serta Spesialis Teknologi AI, dengan keahlian dalam kerangka kerja pengembangan modern, aplikasi cloud-native, dan sistem AI berbasis agen. Dengan fokus pada [ReactJS](https://react.dev/), [NextJS](https://nextjs.org/), [Node.js](https://nodejs.org/en), dan teknologi AI mutakhir serta konsep rekayasa AI, Alireza membantu tim teknik memanfaatkan alat seperti [Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/), dan [Claude Code](https://www.anthropic.com/claude-code) atau [Codex dari OpenAI](https://openai.com/en-EN/codex/) untuk mengubah alur kerja pengembangan mereka.

Terhubung dengan Alireza di [alirezarezvani.com](https://alirezarezvani.com/) untuk wawasan lebih lanjut tentang pengembangan bertenaga AI, pola arsitektur, dan masa depan rekayasa perangkat lunak.

Berharap dapat terhubung dan melihat kontribusi Anda — lihat [proyek sumber terbuka saya di GitHub](https://github.com/alirezarezvani)!

✨ Terima kasih telah membaca! Jika Anda ingin lebih banyak wawasan praktis tentang AI dan teknologi, tekan **berlangganan** untuk tetap mendapatkan informasi terbaru.

Saya juga ingin mendengar pendapat Anda — berikan komentar dengan ide, pertanyaan, atau bahkan jenis topik yang ingin Anda lihat di sini selanjutnya. Masukan Anda sangat membantu membentuk arah saluran ini.
