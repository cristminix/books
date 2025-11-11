
# Memahami Tools dan Perizinan di Claude Code

Claude Code dilengkapi dengan serangkaian *tools* bawaan yang memungkinkannya untuk melakukan berbagai tindakan secara otonom. Selain itu, Claude Code memiliki sistem perizinan yang kuat untuk memastikan Anda tetap memegang kendali penuh atas proyek Anda. Mari kita telaah lebih dalam tentang *tools* yang tersedia dan cara kerja perizinan.

## Tools Bawaan Claude Code

Setiap kali Anda memberikan instruksi kepada Claude Code, ia akan menggunakan *tool* internal untuk melaksanakan tugas tersebut. Anda tidak perlu menyebutkan nama *tool* secara eksplisit; Claude Code secara cerdas akan memilih *tool* yang tepat berdasarkan permintaan Anda.

Beberapa *tools* utama yang sering digunakan antara lain:

- **`read`**: Digunakan untuk membaca konten dari sebuah *file*.
- **`edit`**: Digunakan untuk memodifikasi *file* yang ada.
- **`bash`**: Digunakan untuk menjalankan perintah *bash* di terminal.
- **`to-do`**: *Tool* internal yang digunakan Claude untuk membuat daftar tugas (checklist) agar tetap terorganisir saat mengerjakan task yang kompleks.

Meskipun Anda tidak perlu menghafal semua *tools* ini, mengetahui kapabilitas bawaan Claude Code akan membantu Anda memanfaatkannya secara lebih efektif.

## Sistem Perizinan

Tidak semua *tools* diciptakan sama. Beberapa *tools* yang berpotensi mengubah *file* atau sistem Anda, seperti `edit` dan `bash`, memerlukan izin eksplisit dari Anda sebelum dapat dieksekusi. Sebaliknya, *tools* yang bersifat *read-only* seperti `read` tidak memerlukan izin.

Ketika Claude Code hendak melakukan tindakan yang memerlukan izin, ia akan menampilkan sebuah *prompt* konfirmasi. Anda akan diberikan tiga pilihan:

1.  **Yes**: Memberikan izin untuk tindakan tersebut satu kali.
2.  **No**: Menolak izin untuk tindakan tersebut. Anda bisa memberikan instruksi lebih lanjut jika diperlukan.
3.  **Yes, and don't ask me again this session**: Memberikan izin dan mengizinkan Claude Code untuk melakukan tindakan spesifik tersebut tanpa bertanya lagi di masa mendatang untuk proyek ini.

### Mengelola Perizinan Secara Persisten

Jika Anda memilih opsi "Yes, and don't ask me again", Claude Code akan membuat sebuah *file* konfigurasi lokal di dalam proyek Anda pada path `.claude/settings.local.json`.

*File* ini berisi sebuah objek JSON yang mendefinisikan perizinan yang telah Anda berikan. Contohnya:

```json
{
  "permissions": {
    "allow": [
      "git add ."
    ]
  }
}
```

Dengan adanya konfigurasi ini, setiap kali Claude Code perlu menjalankan `git add .`, ia tidak akan lagi meminta izin dari Anda. Anda juga dapat menambahkan perintah lain secara manual ke dalam *array* `allow` untuk menyederhanakan alur kerja Anda. *File* `settings.local.json` ini dirancang untuk alur kerja lokal dan tidak seharusnya di-*commit* ke *repository* Anda.

### Menerima Edit Secara Otomatis (Session-wide)

Untuk sesi kerja di mana Anda akan banyak melakukan modifikasi *file*, Anda dapat mengaktifkan fitur "Accept Edits". Gunakan *shortcut* `Alt + M` (di Windows) atau `Control + M` (di Mac) untuk mengaktifkannya.

Saat fitur ini aktif, Claude Code tidak akan meminta izin setiap kali ia perlu mengedit *file* selama sesi *chat* tersebut masih berlangsung. Jika Anda memulai sesi baru, Anda perlu mengaktifkannya kembali.

Dengan memahami cara kerja *tools* dan sistem perizinan ini, Anda dapat bekerja sama dengan Claude Code secara lebih efisien dan aman, sambil tetap memegang kendali penuh atas setiap perubahan yang terjadi pada proyek Anda.
