
# Memahami Konteks dalam Claude Code

Dalam interaksi dengan model AI seperti Claude Code, memberikan **konteks** yang relevan adalah kunci untuk mendapatkan respons yang akurat dan sesuai. Sama seperti dalam percakapan manusia, informasi tambahan membantu AI memahami permintaan Anda dengan lebih baik.

## Apa itu Konteks?

Konteks adalah informasi tambahan yang Anda berikan pada *prompt* Anda. Bayangkan Anda hanya mengatakan kata "pisang" tanpa konteks apa pun; lawan bicara Anda pasti akan bingung. Namun, jika Anda mengatakan, "Buah favorit saya adalah pisang," Anda telah memberikan konteks, yang memungkinkan percakapan berlanjut.

Prinsip yang sama berlaku untuk Claude Code. Meminta untuk "memperbaiki tautan" tanpa referensi akan membingungkan. Namun, dengan menyebutkan file spesifik menggunakan simbol `@`, seperti `@/src/components/ui/Button.tsx`, Anda memberikan konteks yang jelas, memungkinkan Claude Code untuk langsung menemukan dan memperbaiki masalahnya.

## Cara Menambahkan Konteks

Ada beberapa cara untuk menambahkan konteks ke sesi Claude Code Anda:

### 1. Menggunakan Simbol `@`

Anda dapat secara manual menambahkan file sebagai konteks dengan mengetik simbol `@` diikuti dengan path file. Claude Code akan memberikan saran *autocomplete* untuk memudahkan Anda memilih file yang benar. Anda bisa menambahkan beberapa file dengan cara ini.

```
@/src/components/Button.tsx
@/src/styles/buttons.css

Tolong perbarui varian tombol di file pertama agar sesuai dengan gaya di file kedua.
```

### 2. Membuka File di Editor

Cukup dengan membuka file di editor Anda dan menempatkan kursor di dalamnya, file tersebut secara otomatis akan ditambahkan sebagai konteks. Nama file akan muncul di bawah jendela obrolan, menandakan bahwa file tersebut aktif dalam konteks.

### 3. Memilih Sebagian Kode

Anda juga dapat menyorot bagian kode tertentu dalam sebuah file. Ini akan memfokuskan konteks hanya pada baris-baris yang Anda pilih, yang sangat berguna untuk tugas-tugas yang sangat spesifik.

### 4. Menambahkan Gambar

Claude Code juga dapat menerima gambar sebagai konteks. Cukup seret dan lepas file gambar (misalnya, `button-design.png`) ke dalam jendela obrolan. Anda kemudian dapat meminta Claude untuk mereplikasi gaya atau desain dari gambar tersebut ke dalam kode Anda.

```
@/src/components/ui/Button.tsx

Bisakah Anda memperbarui desain tombol agar terlihat seperti pada gambar yang saya lampirkan, lengkap dengan efek 3D?
```

## Mengelola Konteks yang Berlebihan

Setiap pesan, file, dan respons AI dalam satu sesi disimpan dalam riwayat obrolan, yang semuanya menjadi bagian dari konteks. Meskipun ini berguna saat mengerjakan satu fitur, konteks bisa menjadi "kotor" jika Anda beralih ke tugas yang tidak terkait. Misalnya, setelah mengerjakan logika keranjang belanja, lalu beralih ke perbaikan UI pada komponen tombol, konteks tentang keranjang belanja menjadi tidak relevan dan dapat membingungkan AI.

Menjaga konteks tetap bersih dan terfokus sangat penting untuk hasil yang akurat.

## Teknik Membersihkan Konteks

Berikut adalah beberapa perintah untuk mengelola dan membersihkan konteks sesi Anda:

1.  **`/clear`**: Menghapus seluruh riwayat percakapan dan konteks yang ditambahkan secara manual. Ini seperti memulai sesi baru dari awal, tetapi tetap mempertahankan konteks dari file `claude.md`.
2.  **`/compact`**: Meringkas seluruh riwayat sesi menjadi sebuah ringkasan singkat. Sisa riwayat akan dihapus, sehingga mengurangi "kebisingan" dalam konteks tanpa kehilangan inti dari pekerjaan yang telah dilakukan.
3.  **Tekan `Escape` Dua Kali**: Memungkinkan Anda untuk "memundurkan" sesi ke titik sebelumnya, menghapus semua pesan dan file yang ditambahkan setelah titik tersebut dari konteks.
4.  **`/exit` dan `/resume`**: Anda dapat keluar dari sesi saat ini dengan `/exit` dan memulai yang baru. Jika Anda perlu kembali, gunakan `/resume` untuk melihat daftar semua sesi aktif dan melanjutkannya, lengkap dengan konteks historisnya.

## Jendela Konteks (Context Window)

Setiap model AI memiliki **jendela konteks**, yaitu jumlah maksimum informasi yang dapat diproses sekaligus, diukur dalam *token*. Claude Code memiliki jendela konteks yang besar (sekitar 200.000 token), tetapi sesi yang sangat panjang dapat mengisinya. Jika ini terjadi, Claude akan memberi tahu Anda, dan pada saat itu, akurasi model mungkin menurun. Inilah saatnya menggunakan salah satu teknik pembersihan konteks di atas.

Dengan mengelola konteks secara efektif, Anda memastikan bahwa Claude Code selalu memiliki informasi yang paling relevan untuk menyelesaikan tugas Anda dengan efisien dan akurat.
