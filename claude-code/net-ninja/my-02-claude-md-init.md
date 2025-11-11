# Menggunakan File `claude.md` untuk Konteks Proyek

## Inisialisasi `claude.md`

Baiklah.
Jadi sekarang kita sudah menyiapkan dan menjalankan kode Claude di dalam proyek ini.
Saya ingin mulai menggunakannya untuk membuat beberapa perubahan pada kode dan mengerjakan komponen baru.
Namun sebelum itu, selalu merupakan ide yang baik ketika Anda mulai menggunakan perintah `/init` untuk menginisialisasi file `claude.md` di dalam root proyek.

Dan ketika kita melakukan ini, Claude memindai seluruh basis kode.
Ia menganalisis struktur folder, cara aplikasi dimulai, manajemen status yang digunakan, dan detail lainnya. Ini memberinya gambaran menyeluruh tentang proyek, lokasi komponen, dan cara terbaik untuk mengembangkan fitur baru di masa mendatang.

Kemudian ia meringkas semua itu dan membuang informasi tersebut ke dalam file `claude.md` dalam format yang terstruktur dan mudah dibaca manusia.
Setiap kali kita berinteraksi dengan Claude untuk bertanya atau mengubah kode proyek, ia menggunakan file `claude.md` sebagai konteks dan panduan.

File ini berfungsi sebagai dokumentasi mini kode Anda. Claude menggunakannya setiap kali ia perlu mengimplementasikan sesuatu atau memberikan umpan balik.
Jadi kemudian saya akan menekan enter sekarang untuk menjalankan perintah ini dan melihat apa yang dihasilkannya.

Saat proses ini berlangsung, Claude membuat daftar tugas. Ia menjelajahi repositori, menganalisis package.json dan kode sumber, serta memeriksa file dokumentasi yang ada. Setelah itu, ia akan membuat file `claude.md`. Anda dapat melihat ia menandai setiap langkah, menunjukkan kemajuan tugas ekstensif yang dilakukannya, seperti membaca dan mencari file.

Baiklah.
Kemudian, setelah ia melakukan semua itu, Anda dapat melihat ia telah membuat rencana ini.
Dan jika kita gulir ke bawah, ia bertanya kepada kita, apakah Anda ingin membuat file `claude.md` ini?
Dan saya akan memilih ya.
Ia kemudian membuat file tersebut, yang kini dapat kita lihat di root direktori proyek.

## Isi File `claude.md`

Jadi mari kita buka itu di sini dan lihat seperti apa.
Jadi Anda dapat melihat file ini memberikan panduan kepada kode Claude saat bekerja dengan kode di repositori ini.

File ini berisi beberapa perintah pengembangan yang ditemukan dari package.json. Ada juga gambaran umum arsitektur yang menjelaskan bahwa ini adalah aplikasi blog Next.js 15, menggunakan teknologi seperti React 19, Tailwind V4, Vest, dan lainnya.

Struktur proyek juga disertakan, sehingga Claude tahu di mana harus menempatkan file baru.
Terdapat arsitektur data yang menunjukkan penggunaan Higraph untuk konten, informasi gaya, pengaturan pengujian, dan catatan pengembangan tambahan.
Jadi, ini cukup komprehensif.

Ini memberikan Kode Claude panduan yang baik tentang apa yang kita lakukan.
Dan setiap kali kita membuat perubahan, ia dapat menggunakan panduan ini.

## Pentingnya Memperbarui `claude.md`

Karena proyek ini sudah dimulai sebelum Claude terlibat, ia dapat memindai basis kode yang ada dan membuat file `claude.md` yang terperinci.
Tetapi jika Anda memulai dengan proyek baru dengan hampir tidak ada file atau kode pengaturan, maka ia akan memiliki lebih sedikit untuk dikerjakan.

Dan file `claude.md` mungkin tidak akan banyak isinya.
Dalam kasus tersebut, Anda dapat mengedit file secara manual. Uraikan struktur proyek tingkat tinggi, alat, paket, atau kerangka kerja yang akan digunakan, preferensi gaya kode, dan ringkasan keseluruhan aplikasi.

Dan Anda dapat memperbaruinya seiring berjalannya waktu.
Pembaruan berkala sangat penting, baik untuk proyek baru maupun yang sudah ada.

Anda harus selalu memperbarui file ini jika ada perubahan pada struktur file, paket yang digunakan, atau detail lain yang diuraikan di dalamnya.

Jika tidak, maka kode Claude mungkin tidak secara otomatis mengambil perubahan itu, dan ia bisa pergi ke arah yang sama sekali berbeda ketika Anda memintanya untuk melakukan sesuatu.

## `claude.md` dalam Konteks Sesi

Bagaimanapun, file Claude MD ini sekarang secara otomatis ditambahkan ke konteks sesi sehingga Claude dapat merujuknya ketika ia membuat perubahan.
Dan Anda akan menemukan bahwa menjaga file Claude yang mutakhir seperti ini menghasilkan generasi kode yang jauh lebih baik.

## Contoh Penggunaan: Membuat Hook Baru

Jadi sekarang setelah kita memiliki file ini, mari kita minta kode Claude untuk melakukan sesuatu dan melihat apakah ia mematuhi panduan.
Saya ingin Claude membuat hook baru. Hook ini akan menyimpan preferensi tema pengguna, berdasarkan tema yang aktif saat mereka mengaktifkan ikon di sudut kanan atas.

Sekarang saya perhatikan bahwa di dalam file Claude di sini, kita tidak mereferensikan folder hooks.
Jadi ini akan menjadi kesempatan yang baik untuk memperbarui file ini sehingga kode Claude tahu di mana harus membuat hooks.

Saya akan menyimpannya di bagian struktur proyek, di mana disebutkan bahwa semua hook yang dapat digunakan kembali berada dalam folder 'hooks'.
Jadi sekarang jika saya meminta kode Claude untuk membuat hook, semoga ia akan menempatkannya di dalam folder itu.

Baiklah.
Jadi Anda dapat melihat kita sebenarnya tidak memiliki folder hooks saat ini tetapi semoga Kode Claude akan membuatnya juga.
Saya akan membuka terminal dan kemudian saya akan memintanya untuk membuat hook baru ini.

Saya akan meminta Claude untuk membuat hook yang menyimpan preferensi tema pengguna saat mereka mengaktifkan tema di situs, dan menyimpannya di penyimpanan lokal untuk penggunaan berikutnya.

Saya juga akan menekankan untuk tidak langsung menggunakan hook tersebut di mana pun. Ini karena Claude seringkali ingin langsung mengintegrasikan fitur, hook, atau komponen baru yang dibuatnya ke dalam proyek.

Jadi, seringkali saya menambahkan ini di akhir untuk memastikan ia tidak melakukannya.
Jadi, saya akan menekan enter.
Satu-satunya hal yang benar-benar saya khawatirkan saat ini adalah untuk menguji apakah kode Claude melihat file `claude.md` itu dan membuat hook di folder yang benar.

Oke, jadi sepertinya ia telah menghasilkan beberapa kode.
Jika kita perhatikan, ia ingin menempatkannya di dalam folder 'hooks'. Hook yang dibuatnya ada di sini. Biasanya, saya akan memeriksa kode secara detail, tetapi untuk tutorial ini, saya akan langsung menerima perubahan tersebut.

Dan Anda dapat melihat ia telah membuat folder hooks dan ia telah membuat file use theme di dalam folder itu.
Luar biasa.

## Menambahkan Memori ke `claude.md`

Anda juga dapat menambahkan memori ke file `claude.md` langsung dari sesi obrolan dengan menggunakan simbol hash.

Misalnya, saya bisa menambahkan hash lalu mengatakan sesuatu seperti ketika membuat komponen halaman baru, selalu tambahkan tautan ke halaman itu di header.

Dan Anda dapat melihat di sini saat saya mengetik itu, ia memberi tahu kita bahwa ia akan mengingat apa yang kita katakan karena kita menambahkan hash itu.

Intinya, instruksi ini akan ditempatkan di file `claude.md` sebagai referensi di masa mendatang. Jadi, setiap kali ia membuat komponen halaman, ia juga harus membuat tautan header untuknya.
Sekarang ketika kita menekan enter, kita akan melihat beberapa opsi.

Ada beberapa opsi penyimpanan:

- **Memori Proyek:** Disimpan ke file `claude.md` yang baru dibuat di root proyek.
- **Memori Proyek Lokal:** Disimpan di folder root yang sama, tetapi dengan penambahan 'lokal' pada nama file.
- **Memori Global:** Disimpan sebagai file claude global di folder root Claude di komputer Anda, yang ditambahkan saat instalasi.

### Memori Proyek

Memori proyek diatur saat kita menjalankan perintah forward/init untuk membuat file `claude.md` di root proyek.

File ini dimaksudkan untuk dilacak oleh kontrol versi dan didorong ke repositori jarak jauh. Tujuannya agar pengembang lain yang mengerjakan proyek memiliki file claude yang sama dengan panduan yang seragam untuk Claude.

Dan itu berarti setiap memori atau informasi dalam file ini harus spesifik untuk proyek.
Misalnya, struktur folder, konvensi penamaan, pengujian, kerangka kerja, dll.

### Memori Proyek Lokal

Memori proyek lokal adalah file untuk panduan dan preferensi pribadi Anda saat bekerja dengan Claude. Misalnya, ini dapat menguraikan alat pribadi yang Anda gunakan, yang mungkin tidak digunakan oleh pengembang lain dalam proyek yang sama.

Dan file ini tidak akan didorong ke repositori jarak jauh dan hanya akan bersifat lokal untuk Anda di dalam proyek ini.

### Memori Pengguna

Memori pengguna adalah panduan pribadi Anda untuk Claude di semua proyek yang Anda kerjakan. Alat global atau preferensi gaya kode pribadi Anda akan masuk ke file ini.

Dan lagi, ini hanya untuk Anda di komputer Anda, tetapi ini akan untuk setiap proyek tempat Kode Claude berjalan.

Untuk saat ini, kita hanya akan menambahkan ini ke memori proyek, yang berarti itu harus ditambahkan ke file `claude.md` yang sudah kita miliki.
Jadi, jika saya menutup ini dan membuka file ini, kita seharusnya dapat melihat di bagian bawah bahwa memori baru telah ditambahkan.

Dan Anda dapat melihat di sini, ketika membuat komponen halaman baru, selalu tambahkan tautan ke halaman itu di header.
Luar biasa.

## Contoh Penggunaan: Membuat Halaman Baru

Baiklah.
Jadi, sekarang kita akan menguji ini.
Jadi, saya akan membuka cadangan kode, dan saya akan menempelkan prompt, yang mengatakan, bisakah Anda menambahkan halaman tentang baru hanya dengan judul H2 dan satu baris Lauram sebagai kontak konten?
Jadi, tekan enter.

Semoga, ia akan membaca instruksi itu di file `claude.md` juga dan membuat tautan untuk kita.
Di daftar tugasnya, ia mencatat untuk menambahkan tautan halaman 'tentang' ke navigasi header, menunjukkan bahwa ia memahami instruksi tersebut.

Baiklah.
Jadi, saya hanya akan menerima perubahan ini.
Lagi, biasanya Anda harus memeriksa ini, tetapi demi tutorial ini, saya hanya akan menerima ini.
Dan lagi, ia meminta izin untuk mengedit file, file tata letak kali ini untuk menambahkan tautan baru.
Lagi, saya akan menekan ya.

Anda bisa melakukan ini.
Dan kemudian perubahan lain pada file tata letak, yang juga akan saya terima.

Oke.
Dan sekarang sudah selesai.
Jadi jika saya menutup ini, buka aplikasi dan kemudian kita dapat melihat halaman tentang ini dan di dalamnya kita memiliki judul H2 dan hanya satu baris Lauram Ipsum.
Luar biasa.

Jika kita melihat halaman tata letak yang telah dieditnya, ia seharusnya telah menambahkan tautan di navigasi, yaitu tautan 'tentang'.
Sekarang mari kita coba ini di browser.

Oke.
Jadi ya, ia telah melakukannya.
Anda dapat melihat tautan tentang di sini.
Dan jika kita mengklik itu, kita pergi ke halaman tentang.

Secara retrospektif, Claude juga menambahkan dua tautan lain yang tidak saya minta. Ini adalah salah satu hal yang saya perhatikan tentang Claude Code; terkadang ia melakukan hal-hal di luar cakupan permintaan.

Penting untuk secara spesifik menginstruksikan Claude tentang apa yang harus dilakukan dan tidak dilakukan. Anda bisa menambahkan instruksi ini ke file `claude.md` Anda.

## Mengakses File Memori

Perlu dicatat bahwa dokumentasi Claude Code menyatakan memori lokal tidak lagi digunakan. Sebagai gantinya, disarankan untuk mengimpor file yang tidak terlacak ke dalam memori tingkat proyek untuk memberikan konteks pribadi kepada Claude.

Dan saya akan menunjukkan kepada Anda cara mengimpor dan mereferensikan file nanti dalam kursus.
Tetapi pada saat merekam video ini, opsi lokal masih muncul di terminal ketika Anda menggunakan pintasan hashtag memori untuk menambahkan memori baru.

Anda juga dapat mengakses file memori (yaitu file `claude.md`, baik lokal maupun global) menggunakan perintah '/memory'.

Tetapi bagaimanapun, ketika Anda menggunakan perintah memori ini, kode claude akan menanyakan file memori mana yang ingin Anda buka dan edit.

Anda dapat memilih salah satu opsi dan menekan Enter untuk membuka file tersebut. Misalnya, memilih memori proyek akan membuka file `claude.md` di VS Code untuk diedit langsung.

## Ringkasan dan Praktik Terbaik

Sebagai ringkasan, selalu disarankan untuk menggunakan perintah '/init' saat memperkenalkan Claude Code ke proyek.

Ini memungkinkan Claude mempelajari basis kode dan menguraikan pola struktural, kerangka kerja, pustaka, konvensi penamaan, dan lainnya ke dalam file `claude.md`.

File ini secara otomatis digunakan oleh Claude sebagai konteks untuk keputusan proyek di masa mendatang.

File ini juga dapat ditambahkan ke repositori jarak jauh, sehingga pengembang lain memiliki akses untuk alur kerja mereka dengan Claude Code.

Akhirnya, itu bukan sesuatu yang harus Anda buat dan kemudian lupakan, tetapi lebih baik tetap di atas, edit, dan perbarui ketika ada perubahan dalam proyek Anda.

Dengan begitu, Anda selalu menjaga Claude tetap dalam lingkaran, dan Anda akan menemukan pekerjaannya jauh lebih sesuai dengan kode dan struktur proyek Anda yang ada saat ini.
