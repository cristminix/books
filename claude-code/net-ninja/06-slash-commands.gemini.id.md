Sesuai permintaan Anda, berikut adalah artikel mengenai _slash commands_ dan cara membuat _custom command_ di Claude Code, disajikan dalam format Markdown dan disesuaikan dengan instruksi bahasa Indonesia kasual yang tersimpan dalam memori saya.

---

# 💻 Mengenal _Slash Commands_ dan Cara Membuat _Custom Command_ di Claude Code

Halo teman-teman\! [cite\_start]Di pelajaran ini, kita akan ngobrol santai soal fitur keren di **Claude Code** yang namanya _slash commands_, atau biar lebih simpel, kita sebut aja **commands**[cite: 1]. [cite\_start]Selain itu, kita juga akan coba bikin _custom command_ sendiri, lho\! [cite: 2]

## 🛠️ Apa Itu _Commands_ (Perintah)?

[cite\_start]_Commands_ adalah perintah bawaan yang sudah disediakan oleh Claude Code yang bisa kita pakai langsung[cite: 2]. [cite\_start]Cara pakainya gampang banget: cukup ketik garis miring (**/**) diikuti dengan nama perintahnya[cite: 3].

Beberapa perintah yang mungkin sudah pernah kita gunakan, contohnya:

- [cite\_start]`/clear`: untuk menghapus konteks percakapan[cite: 3, 7].
- [cite\_start]`/initialize`: untuk membuat _file_ `a.md`[cite: 3].

Kalau kamu cuma ketik garis miring (**/**) doang, nanti akan muncul daftar semua _commands_ yang tersedia di Claude Code. [cite\_start]Kamu bisa geser ke atas dan bawah untuk melihat-lihat daftarnya[cite: 4].

### Contoh _Commands_ Bawaan Lainnya:

- `/add-dir`: buat kasih akses ke Claude ke direktori kerja lain. [cite\_start]Ini berguna banget kalau kamu punya proyek yang saling berhubungan, misalnya _backend_ dan _frontend_[cite: 5].
- [cite\_start]`/agents`: buat mengelola sub-_agents_ (akan kita bahas nanti)[cite: 6].
- [cite\_start]`/model`: buat memilih model AI mana yang ingin kamu gunakan[cite: 7].
- `/permissions`: buat menambahkan izin untuk _tools_ yang berbeda di Claude Code untuk proyek ini. [cite\_start]Izin ini akan ditambahkan ke _file_ pengaturan lokal[cite: 9, 10].

[cite\_start]Kamu bisa coba-coba sendiri semua _commands_ ini dan main-main dengannya[cite: 12].

---

## ✨ Membuat _Custom Command_ Sendiri

[cite\_start]Nah, yang seru adalah kita bisa bikin **custom command** yang bisa kita tambahkan ke dalam daftar _commands_ bawaan tadi[cite: 13]. [cite\_start]Kita biasanya bikin _custom command_ untuk tugas-tugas yang sering kita lakukan dalam proyek[cite: 14].

Misalnya, kalau kamu sering bikin komponen UI, kamu bisa bikin _command_ khusus untuk _generate_ komponen tersebut. [cite\_start]_Command_ ini bisa berisi _prompt_ yang detail, konteks yang diperlukan, dan spesifikasi lain yang akan diteruskan ke model AI[cite: 15, 16, 17]. [cite\_start]Jadi, kapanpun kamu butuh komponen baru, tinggal panggil _command_ itu aja[cite: 18].

### 1\. Persiapan Struktur Folder

[cite\_start]Langkah pertama yang perlu dilakukan adalah membuat struktur folder dan _file_[cite: 19]:

1.  [cite\_start]Buat folder bernama **`commands`** di dalam folder **`.claude`** (kalau folder `.claude` belum ada, buat juga)[cite: 19, 20].
2.  Di dalam folder `commands`, buat _file_ Markdown (`.md`) baru. Nama _file_ ini akan jadi nama _command_ kamu. [cite\_start]Contohnya: **`ui-component.md`**[cite: 21, 22].

### 2\. Isi _File_ _Command_

[cite\_start]_File_ Markdown ini pada dasarnya adalah **prompt yang sangat besar**[cite: 31]. [cite\_start]Ketika _custom command_ ini digunakan, Claude Code akan mengambil isi _file_ ini dan menggunakannya sebagai _prompt_[cite: 32].

[cite\_start]Di sini kamu bisa kasih instruksi ke Claude Code tentang apa yang harus dilakukan[cite: 23], contohnya:

- Di mana _file_ komponen harus diletakkan.
- [cite\_start]Konvensi penamaan (misalnya, _functional component_ dengan nama dalam _Pascal case_)[cite: 24].
- [cite\_start]Jenis varian dan ukuran komponen yang diinginkan[cite: 25].
- [cite\_start]Instruksi untuk membuat _file_ tes dan memastikan semua tes lolos[cite: 27, 28].
- [cite\_start]Instruksi untuk menambahkan komponen ke halaman _preview_ saja, dan tidak ke bagian lain proyek[cite: 29, 30].

> [cite\_start]💡 **Tips Keren:** Kamu bisa menggunakan tanda **`@`** untuk memuat _file_ lain sebagai konteks di dalam _custom command_ ini[cite: 26].

### 3\. Menggunakan _Command_

[cite\_start]Setelah _file_ _command_ dibuat, kamu perlu **keluar dan memulai ulang sesi Claude Code** agar _command_ baru ini bisa terbaca[cite: 33, 34, 83].

[cite\_start]Setelah _restart_, ketik **`/`** lagi, dan kamu akan melihat _command_ barumu, contohnya `/ui-component`[cite: 35, 36].

---

## 🚀 Menambahkan Argumen ke _Custom Command_

[cite\_start]Awalnya, _command_ kita akan membuat komponen secara misterius (_mystery component_) karena kita tidak menentukan jenis komponen apa yang harus dibuat[cite: 60, 61]. [cite\_start]Kita ingin bisa menentukan komponen apa yang kita mau, misalnya: `/ui-component card | brief description`[cite: 62, 63]. [cite\_start]Ini bisa kita lakukan dengan **Command Arguments**[cite: 64].

Untuk menambahkan argumen, buka kembali _file_ _command_ kamu dan tambahkan bagian-bagian ini:

### 1\. _Front Matter_

[cite\_start]Tambahkan bagian _front matter_ di bagian atas _file_ untuk memberikan _metadata_[cite: 65].

- [cite\_start]**`description`**: Penjelasan singkat tentang apa yang dilakukan _command_[cite: 66].
- [cite\_start]**`argument-hint`**: Petunjuk tentang argumen apa yang diharapkan saat _command_ dijalankan[cite: 67].

[cite\_start]Kedua properti ini akan muncul di _interface_ _chat_ saat kamu menggunakan _tool_[cite: 68].

### 2\. Memproses Argumen

[cite\_start]Gunakan variabel khusus **`$arguments`** untuk menangkap semua argumen yang kita masukkan saat memanggil _command_[cite: 69, 70, 71].

[cite\_start]Untuk memisahkan beberapa nilai argumen (misalnya **nama** dan **ringkasan** komponen), kamu bisa menggunakan sintaksis tautan referensi Markdown (`[variabel]`) untuk menyimpan nilai-nilai tersebut[cite: 74, 75, 76]:

```markdown
[nama-komponen]
[ringkasan-komponen]
```

[cite\_start]Ini memberi tahu Claude Code untuk mencoba memisahkan argumen yang dimasukkan untuk menemukan dan menyimpan nilai-nilai variabel tersebut[cite: 77].

### 3\. Menggunakan Argumen dalam Instruksi

[cite\_start]Setelah argumen ditangkap dan dipisahkan, kamu bisa menggunakannya di dalam instruksi[cite: 77]:

- [cite\_start]Ganti instruksi lama dengan instruksi baru yang **menggunakan nilai-nilai argumen**[cite: 78, 79].
- [cite\_start]Contohnya, gunakan variabel **nama** untuk nama folder/file dan nama komponen[cite: 80].
- [cite\_start]Gunakan variabel **ringkasan** saat Claude Code membuat komponen itu sendiri[cite: 80].

[cite\_start]Dengan cara ini, saat kamu memanggil _command_ seperti `/ui-component icon | an icon component for showing icons with a circular background`, argumennya akan digunakan oleh AI untuk membuat komponen sesuai keinginan[cite: 81, 87, 88].

[cite\_start]Ingat, setelah mengubah _file_ _command_, kamu harus **keluar dan memulai ulang sesi Claude Code** lagi[cite: 82, 83].

_Custom commands_ adalah cara yang sangat ampuh untuk mengotomatisasi tugas-tugas umum dan memastikan bahwa _prompt_ yang sangat detail selalu digunakan saat kamu membutuhkannya\! 👍

---

<br>
Mau saya carikan contoh proyek *open source* yang menggunakan *custom commands* di Claude Code?
