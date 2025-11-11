
# Claude Code: Perencanaan dan Proses Berpikir

Claude Code menawarkan dua fitur canggih untuk membantunya menangani tugas-tugas kompleks: **Perencanaan** dan **Berpikir**. Keduanya adalah proses yang berbeda, tetapi dapat digunakan bersamaan untuk hasil yang optimal.

## Mode Perencanaan (Planning Mode)

Mode Perencanaan sangat ideal untuk tugas-tugas yang perubahannya berdampak luas di beberapa file, meskipun setiap perubahan individu mungkin tidak rumit. Dengan membuat rencana, Claude Code dapat tetap fokus dan menyelesaikan setiap langkah secara berurutan.

### Kapan Menggunakan Mode Perencanaan?

Gunakan mode ini ketika Anda memberikan tugas dengan cakupan yang luas, seperti:

- Membuat komponen baru dan mengintegrasikannya di seluruh proyek.
- Melakukan refaktorisasi yang memengaruhi banyak bagian dari basis kode.

### Cara Mengaktifkan

Anda dapat mengaktifkan Mode Perencanaan dengan menekan `Alt+M` (atau `Option+M`) dua kali hingga Anda melihat mode "planning" aktif di bilah status.

### Contoh Kasus: Membuat Komponen Avatar

Dalam contoh yang diberikan, Claude Code diminta untuk membuat komponen avatar kustom dan mengganti semua implementasi avatar yang ada di proyek.

1.  **Analisis**: Claude Code pertama-tama menganalisis basis kode untuk menemukan di mana komponen avatar dapat digunakan.
2.  **Rencana**: Selanjutnya, ia menyusun rencana yang mencakup:
    - Membuat komponen `Avatar.tsx` baru di dalam direktori `ui`.
    - Mengganti kode avatar yang ada di kartu postingan blog dan aktivitas terbaru.
    - Menambahkan avatar ke halaman detail postingan blog.
    - Membuat file pengujian untuk komponen baru.
    - Menambahkan pratinjau avatar di navigasi header.
3.  **Eksekusi**: Setelah rencana disetujui, Claude Code secara otomatis menjalankan setiap langkah, termasuk menjalankan pengujian dan melakukan *linting* pada file.

Meskipun hasilnya sebagian besar berhasil, contoh ini juga menyoroti pentingnya memberikan instruksi yang spesifik. Claude Code sedikit "terlalu bersemangat" dan membuat halaman penuh untuk pratinjau avatar, padahal niat awalnya adalah untuk menambahkannya ke halaman pratinjau yang sudah ada. Hal ini menunjukkan bahwa meskipun AI sangat membantu, pengawasan dan spesifisitas dari pengembang tetap penting.

## Mode Berpikir (Thinking Mode)

Mode Berpikir dirancang untuk tugas-tugas yang melibatkan logika kompleks, bahkan jika cakupannya sempit. Mode ini memungkinkan model untuk bernalar dan memikirkan solusi terbaik sebelum menulis kode apa pun.

### Kapan Menggunakan Mode Berpikir?

Gunakan mode ini untuk tugas-tugas seperti:

- Mengimplementasikan sistem yang kompleks dari awal (misalnya, sistem komentar).
- Memecahkan masalah yang memerlukan pertimbangan arsitektural (misalnya, memilih *database*, skema, layanan otentikasi).

### Cara Mengaktifkan

Mode Berpikir diaktifkan dengan menyertakan kata kunci `think` dalam *prompt* Anda. Proses "berpikir" Claude Code akan terlihat di editor dengan teks berwarna abu-abu, memberikan Anda wawasan tentang proses penalarannya.

### Tingkatan Berpikir

Claude Code memiliki beberapa tingkat pemikiran yang dapat Anda aktifkan:

- `think`: Memicu sejumlah kecil pemikiran dan penalaran.
- `think hard`: Meningkatkan intensitas proses berpikir.
- `think harder`: Lebih lanjut meningkatkan kemampuan berpikir.
- `ultra think`: Mengaktifkan mode berpikir paling kuat yang tersedia.

Penting untuk diingat bahwa mode berpikir mengonsumsi lebih banyak token. Semakin "keras" Anda meminta Claude Code untuk berpikir, semakin banyak token yang akan digunakannya.

### Contoh Kasus: Sistem Komentar

Saat diminta untuk mengimplementasikan sistem komentar, Claude Code (dengan mode berpikir dan perencanaan aktif) melakukan hal berikut:

1.  **Berpikir**: Claude Code melalui proses pemikiran yang ekstensif, mempertimbangkan *database*, skema, layanan otentikasi, moderasi, dan pembaruan *real-time*.
2.  **Rencana**: Berdasarkan pemikirannya, ia menghasilkan rencana yang sangat rinci yang mencakup semua langkah yang diperlukan untuk membangun sistem.

Dalam praktiknya, untuk tugas sebesar ini, disarankan untuk tidak membiarkan AI bekerja sepenuhnya sendiri. Sebaiknya, pecah tugas menjadi bagian-bagian yang lebih kecil dan bekerja sama dengan Claude Code untuk setiap langkah. Ini memungkinkan Anda untuk tetap memegang kendali, meninjau kode dalam iterasi kecil, dan memandu AI ke arah yang benar.

## Kesimpulan

Mode **Perencanaan** dan **Berpikir** adalah alat yang ampuh dalam alur kerja pengembangan Anda dengan Claude Code. **Perencanaan** membantu menjaga tugas-tugas berskala besar tetap pada jalurnya, sementara **Berpikir** memastikan bahwa solusi untuk masalah-masalah kompleks telah dipertimbangkan dengan matang. Dengan menggunakan kedua fitur ini secara bijak, Anda dapat secara signifikan meningkatkan efisiensi dan kualitas kode yang Anda hasilkan bersama AI.
