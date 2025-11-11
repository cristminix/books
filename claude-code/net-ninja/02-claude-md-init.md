# Menginisialisasi Proyek Anda dengan `claude.md`

Setelah Claude Code siap dan berjalan di proyek Anda, langkah awal yang sangat disarankan adalah menginisialisasi file `claude.md` menggunakan perintah `init`.

## Apa itu `claude.md`?

Perintah `init` akan memindai seluruh basis kode Anda. Claude Code akan melihat struktur folder, cara aplikasi dijalankan, manajemen state yang digunakan, dan semua detail lainnya untuk mendapatkan pemahaman mendalam tentang proyek Anda.

Informasi ini kemudian dirangkum dan disimpan dalam file `claude.md` dalam format yang terstruktur dan mudah dibaca manusia. File ini berfungsi sebagai dokumentasi mini dari kode Anda yang akan digunakan Claude sebagai konteks dan panduan setiap kali Anda berinteraksi dengannya, baik untuk bertanya tentang kode maupun untuk membuat perubahan.

## Proses Inisialisasi

Saat Anda menjalankan `init`, Claude Code akan membuat daftar tugas untuk dirinya sendiri:
- Menjelajahi repositori.
- Menganalisis `package.json` dan kode sumber.
- Memeriksa file dokumentasi yang ada.
- Membuat file `claude.md`.

Setelah pemindaian selesai, Claude akan menampilkan rencananya dan meminta konfirmasi untuk membuat file `claude.md`.

## Isi `claude.md`

File `claude.md` berisi panduan untuk Claude Code saat bekerja dengan kode di repositori Anda. Contoh isinya antara lain:
- **Perintah Pengembangan:** Ditemukan dari `package.json`.
- **Gambaran Arsitektur:** Penjelasan singkat tentang proyek (misalnya, aplikasi blog Next.js 15, React 19, Tailwind V4).
- **Struktur Proyek:** Membantu Claude mengetahui di mana harus meletakkan file baru.
- **Arsitektur Data:** Informasi tentang sumber data (misalnya, Hygraph untuk konten).
- **Styling:** Panduan tentang gaya penulisan kode.
- **Pengaturan Pengujian:** Konfigurasi untuk testing.
- **Catatan Pengembangan Tambahan.**

Dengan panduan komprehensif ini, Claude Code dapat membuat perubahan yang selaras dengan proyek Anda.

## Menjaga `claude.md` Tetap Terkini

Penting untuk menjaga file `claude.md` tetap *up-to-date*. Jika Anda mengubah struktur file, paket yang digunakan, atau apa pun yang diuraikan dalam file ini, Anda harus memperbaruinya. Jika tidak, Claude Code mungkin tidak secara otomatis mengetahui perubahan tersebut dan bisa menghasilkan kode yang tidak sesuai.

Anda bisa mengedit file ini secara manual. Misalnya, jika Anda berencana menambahkan folder `hooks`, Anda bisa menambahkannya ke bagian struktur proyek di `claude.md` bahkan sebelum folder itu dibuat. Claude Code akan membaca pembaruan ini dan menempatkan hook baru di folder yang benar saat diminta.

## Menambah "Memori" dari Sesi Chat

Anda dapat menambahkan instruksi ke `claude.md` langsung dari sesi chat menggunakan simbol tagar (`#`).

Contoh:
`# saat membuat komponen halaman baru, selalu tambahkan tautan ke halaman itu di header.`

Claude akan mengenali ini sebagai instruksi untuk diingat dan akan menyimpannya di file `claude.md` untuk referensi di masa mendatang.

### Jenis-jenis Memori

Saat menyimpan memori baru, Anda akan diberi beberapa pilihan:
1.  **Project Memory (`claude.md`):** Disimpan di file `claude.md` utama di root proyek. File ini dimaksudkan untuk dilacak oleh *version control* dan dibagikan dengan pengembang lain di tim. Berisi panduan spesifik proyek seperti struktur folder, konvensi penamaan, dll.
2.  **Local Project Memory (`claude.local.md`):** File untuk preferensi pribadi Anda dalam proyek ini. Tidak akan didorong ke repositori remote. *Catatan: Dokumentasi Claude Code menyebutkan bahwa memori lokal akan usang dan digantikan dengan mengimpor file yang tidak dilacak.*
3.  **User Memory (Global):** Panduan pribadi Anda untuk *semua* proyek. Disimpan di folder `claude` global di komputer Anda. Berisi preferensi gaya kode pribadi atau alat yang Anda gunakan di banyak proyek.

## Mengakses File Memori

Anda dapat dengan mudah membuka dan mengedit file memori menggunakan perintah `/memory`. Claude akan menanyakan file memori mana yang ingin Anda buka (proyek, lokal, atau global) dan membukanya di editor Anda.

## Ringkasan

- Selalu gunakan perintah `init` saat memulai Claude Code di sebuah proyek.
- Jaga file `claude.md` tetap terbarui saat proyek Anda berkembang.
- Gunakan file ini untuk memberikan konteks dan panduan kepada Claude, sehingga menghasilkan kode yang lebih baik dan lebih konsisten.
- Bagikan `claude.md` dengan tim Anda untuk memastikan semua orang memiliki panduan yang sama.

Dengan mempraktikkan hal ini, Anda akan menemukan bahwa pekerjaan Claude Code jauh lebih selaras dengan kode dan struktur proyek Anda saat ini.
