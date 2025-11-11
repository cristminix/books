
# Panduan Memulai Claude Code: Alat Pengkodean AI Agentik Anda

Selamat datang! Dalam panduan ini, kita akan menyelami **Claude Code**, sebuah alat pengkodean agentik bertenaga AI dari Anthropic yang dapat Anda manfaatkan untuk menganalisis, merencanakan, menulis, dan mengedit kode dalam proyek Anda.

## Apa itu Claude Code?

Claude Code mirip dengan alat pengkodean agentik lainnya seperti GitHub Copilot atau Cursor. Namun, ada beberapa hal yang membuatnya menonjol:

- **Berbasis Terminal**: Tidak seperti alat lain yang memiliki antarmuka pengguna di dalam editor kode, Claude Code hidup langsung di terminal. Ini memungkinkannya berintegrasi secara mulus dengan alur kerja pengembangan Anda yang sudah ada tanpa memaksa Anda mengganti IDE favorit.
- **Integrasi GitHub**: Anda dapat menggunakan Claude Code dalam alur kerja GitHub untuk mengotomatiskan tinjauan kode pada *pull requests* dan bahkan membuatnya bekerja secara independen pada *open issues* di repositori Anda.
- **Pemahaman Konteks Mendalam**: Claude Code memiliki kemampuan luar biasa untuk memahami basis kode dari proyek yang sedang dikerjakan, menghasilkan kode yang lebih sesuai dan relevan dari satu proyek ke proyek lainnya.

Dalam seri ini, kita akan membahas cara mengatur Claude Code, memberinya konteks, membuatnya menghasilkan kode, dan mengaturnya untuk bekerja secara otonom di repositori GitHub.

> **Catatan**: Pendekatan kita adalah **mengkode bersama Claude**, bukan membiarkannya bekerja sepenuhnya sendiri. Ini adalah alur kerja yang lebih produktif untuk menjaga kode tetap bersih, mengurangi bug, dan memastikan Anda tetap memegang kendali penuh.

---

## Instalasi dan Pengaturan Awal

Sebelum memulai, Anda perlu menginstal Claude Code dan mendaftar untuk sebuah paket.

### 1. Pilih Paket Berlangganan

Kunjungi halaman harga Claude. Anda memerlukan paket **Pro** atau **Max** untuk menggunakan Claude Code. Paket gratis hanya memberikan akses ke model Claude di web, bukan alat Claude Code itu sendiri.

- **Paket Pro**: Pilihan yang baik dengan batas penggunaan yang wajar dan akses ke model seperti `Sonnet` dan `Opus`.
- **Paket Max**: Lebih mahal, tetapi memberikan batas penggunaan yang jauh lebih tinggi dan akses ke fitur-fitur terbaru.

### 2. Instalasi melalui NPM

Setelah mendaftar, buka terminal Anda dan jalankan perintah berikut untuk menginstal Claude Code secara global:

```bash
npm install -g @anthropic-ai/claude-code
```

Perintah ini berfungsi baik di Windows, macOS, maupun Linux (termasuk WSL).

### 3. Menjalankan Claude untuk Pertama Kali

1.  Navigasikan ke direktori proyek yang ingin Anda kerjakan.
2.  Jalankan perintah `claude` di terminal Anda:

    ```bash
    claude
    ```

3.  Saat pertama kali menjalankannya, Claude akan menanyakan beberapa hal:
    - **Mode Tampilan**: Pilih mode terang atau gelap.
    - **Login**: Pilih untuk masuk dengan langganan Anda. Ini akan membuka browser untuk otorisasi.
    - **Kepercayaan Proyek**: Claude akan bertanya apakah Anda mempercayai file di folder saat ini. Pilih "Yes".

Setelah selesai, Anda siap untuk mulai berinteraksi dengan Claude. Anda bisa langsung mencoba bertanya, "Bisakah Anda memberi saya ringkasan tentang proyek ini?" untuk melihat kemampuannya menganalisis basis kode Anda.

---

## Integrasi dengan VS Code

Untuk pengalaman terbaik, disarankan menjalankan Claude Code di terminal terintegrasi VS Code. Saat Anda melakukannya, Claude akan secara otomatis menginstal ekstensi **Claude Code untuk VS Code**.

Ekstensi ini menyediakan beberapa fitur tambahan yang sangat berguna:
- **Tampilan Perbedaan (Diff View)**: Memudahkan Anda melihat perubahan yang dibuat.
- **Konteks dari Pilihan**: Anda dapat dengan mudah menambahkan teks yang dipilih sebagai konteks untuk Claude.
- **Pintasan Keyboard**: Mempercepat alur kerja Anda.
- **Kesadaran Tab Aktif**: Claude tahu file mana yang sedang Anda buka dan kerjakan.

---

## Konfigurasi Awal di Sesi Claude

Setelah Claude berjalan, ada beberapa pengaturan yang bisa Anda lakukan untuk kenyamanan.

### Pengaturan Terminal

Jalankan perintah berikut untuk mengatur agar `Shift + Enter` dapat digunakan untuk membuat baris baru di jendela obrolan:

```
/terminal-settings
```

### Bekerja dengan Git

Claude memiliki pengetahuan tentang repositori Git lokal Anda dan dapat menjalankan perintah `bash` untuk Anda. Anda bisa memintanya untuk:
- Melakukan staging dan commit perubahan.
- Beralih atau membuat cabang baru.
- Menggabungkan cabang dan bahkan menyelesaikan konflik.

Sebagai contoh, untuk memastikan proyek awal tetap aman, Anda bisa meminta Claude untuk membuat cabang baru:

> "Tolong alihkan saya ke cabang baru bernama `claude-edits`."

Claude akan menampilkan perintah `git checkout -b claude-edits` dan meminta izin Anda untuk menjalankannya.

---

## Langkah Selanjutnya

Sekarang Anda telah berhasil menginstal dan mengkonfigurasi Claude Code. Di bagian selanjutnya, kita akan mulai membuat editan kode nyata dan membahas cara menambahkan "memori" jangka panjang ke Claude menggunakan file `claude.md`.

Selamat mengkode bersama Claude!
