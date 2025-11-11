# Meningkatkan Produktivitas dengan Custom Commands di Claude Code

## Pendahuluan

Dalam pengembangan aplikasi modern, efisiensi dan konsistensi adalah kunci kesuksesan. Claude Code menyediakan fitur **slash commands** yang memungkinkan developer untuk mengotomatisasi tugas-tugas berulang dan memastikan konsistensi kode di seluruh proyek. Artikel ini akan membahas secara mendalam tentang cara menggunakan dan membuat custom commands di Claude Code.

## Mengenal Slash Commands

Slash commands adalah perintah bawaan yang disediakan Claude Code untuk mempermudah berbagai tugas development. Untuk mengakses daftar perintah yang tersedia, cukup ketik garis miring (`/`) di interface Claude Code.

### Beberapa Built-in Commands yang Berguna:

- **`/clear`** - Membersihkan context percakapan
- **`/initialize`** - Menginisialisasi file claude.md
- **`/add dir`** - Memberikan akses Claude ke direktori kerja tambahan, memungkinkan pengembangan multi-repository
- **`/agents`** - Mengelola sub-agents
- **`/compact`** - Mengompres context
- **`/model`** - Memilih model AI yang akan digunakan (misalnya Sonic 4)
- **`/permissions`** - Mengatur permissions untuk berbagai tools dalam proyek

## Mengapa Membuat Custom Commands?

Custom commands sangat berguna untuk tugas-tugas yang sering dilakukan dalam proyek. Sebagai contoh, jika Anda sering membuat komponen UI, Anda bisa membuat command khusus yang mencakup:

- Prompt terperinci
- Context yang diperlukan
- Detail spesifik untuk AI model
- Konvensi penamaan
- Struktur folder yang konsisten
- Konfigurasi testing otomatis

## Cara Membuat Custom Command

### Langkah 1: Persiapan Struktur Folder

Pertama, buat struktur folder berikut di dalam proyek Anda:

```
.claw/
  └── commands/
      └── ui-component.md
```

### Langkah 2: Menulis Instruksi Command

Buat file markdown dengan nama command yang diinginkan. Contoh untuk membuat UI component:

```markdown
---
description: "Create a UI component in this directory"
argumentHint: "component-name | brief description"
---

## Context

[name]: Extract the component name from $arguments
[summary]: Extract the brief description from $arguments

## Task

Create a new UI component with the following specifications:

- Location: components/ui folder
- Component type: Functional component
- Naming: Use Pascal case for the component name
- Variants: Add variants based on theme variables from @styles.css
- Testing: Create test file and run until all tests pass
- Preview: Add component to preview page only

Component name: [name]
Component purpose: [summary]
```

### Langkah 3: Restart Claude Session

Setelah membuat custom command, Anda perlu me-restart sesi Claude agar perubahan dapat terdeteksi.

## Menggunakan Command Arguments

Command arguments memungkinkan Anda untuk membuat commands yang lebih fleksibel dan dinamis.

### Syntax Dasar:

```
/ui-component icon | an icon component for showing icons with circular background
```

### Cara Kerja Arguments:

1. **`$arguments`** - Menangkap semua argumen yang diberikan
2. **Square brackets `[name]`** - Membuat variabel untuk menyimpan nilai tertentu
3. **Pipe `|`** - Memisahkan multiple arguments

### Contoh Implementasi:

```markdown
[name]: Extract the component name from $arguments
[summary]: Extract the brief description from $arguments
```

Variabel ini kemudian dapat digunakan dalam instruksi:

```markdown
Create a component named [name] with the following description: [summary]
```

## Studi Kasus: Membuat Card Component

Mari kita lihat contoh praktis pembuatan card component menggunakan custom command.

### Command Execution:

```
/ui-component
```

Tanpa argumen, Claude akan memutuskan sendiri komponen apa yang akan dibuat.

### Hasil yang Dihasilkan:

1. **Card Component** dengan struktur:

   - 5 variants (primary, secondary, success, warning, danger)
   - 3 ukuran berbeda
   - Hover effects
   - Dark mode support

2. **Test File** dengan:

   - Unit tests lengkap
   - Semua tests passing

3. **Preview Integration** di halaman preview

### Dengan Arguments:

```
/ui-component icon | an icon component for showing icons with circular background
```

Menghasilkan icon component dengan spesifikasi yang lebih tepat sesuai kebutuhan.

## Best Practices

### 1. **Selalu Review Kode yang Dihasilkan**

Jangan menerima semua yang dihasilkan AI secara default. Periksa:

- Struktur kode
- Konvensi penamaan
- Best practices
- Performance implications

### 2. **Iterative Improvement**

Jika hasil tidak sesuai harapan, berikan feedback kepada Claude Code untuk perbaikan. Contoh:

```
"Update the icon component to use an icon library instead of emojis"
```

### 3. **Gunakan Context Files**

Manfaatkan `@` syntax untuk memasukkan file sebagai context:

```markdown
Reference the colors from @styles.css
```

### 4. **Definisikan Scope dengan Jelas**

Batasi dimana komponen akan ditambahkan:

```markdown
Add the component to the preview page only, not anywhere else in the project
```

## Tips dan Trik

### 1. **Front Matter untuk Metadata**

Gunakan front matter untuk memberikan informasi tentang command:

```markdown
---
description: "Create a UI component"
argumentHint: "name | description"
---
```

### 2. **Structured Instructions**

Bagi instruksi menjadi sections yang jelas:

- Context
- Task
- Variants
- Testing Requirements
- Integration Points

### 3. **Multiple Repository Development**

Gunakan `/add dir` untuk bekerja dengan multiple repositories:

- Backend dan frontend terpisah
- Shared components
- Related microservices

## Keuntungan Menggunakan Custom Commands

### 1. **Konsistensi Kode**

- Struktur folder yang seragam
- Konvensi penamaan yang konsisten
- Testing pattern yang sama

### 2. **Efisiensi Waktu**

- Automasi tugas berulang
- Reduce boilerplate code
- Faster component creation

### 3. **Dokumentasi Implisit**

- Commands mendokumentasikan best practices tim
- Onboarding lebih mudah untuk developer baru
- Knowledge transfer yang lebih baik

### 4. **Quality Assurance**

- Automated testing
- Consistent code quality
- Reduced human error

## Troubleshooting

### Command Tidak Muncul

**Solusi**: Restart Claude session setelah membuat atau mengubah command file.

### Arguments Tidak Terparsing

**Solusi**:

- Periksa syntax square brackets
- Gunakan pipe `|` untuk memisahkan arguments
- Pastikan `$arguments` variable digunakan dengan benar

### Component Tidak Sesuai Ekspektasi

**Solusi**:

- Berikan instruksi yang lebih detail
- Tambahkan lebih banyak context files
- Lakukan iterative refinement dengan feedback

## Kesimpulan

Custom commands di Claude Code adalah tool yang powerful untuk meningkatkan produktivitas development. Dengan mendefinisikan commands untuk tugas-tugas yang sering dilakukan, Anda dapat:

- Mengotomatisasi proses repetitif
- Memastikan konsistensi di seluruh proyek
- Mengurangi cognitive load
- Mempercepat development cycle

Kuncinya adalah **staying in the loop** - selalu review dan refine hasil yang dihasilkan AI untuk memastikan kualitas kode yang optimal.

## Langkah Selanjutnya

Setelah menguasai custom commands, langkah berikutnya adalah mempelajari **MCP servers** untuk mengintegrasikan layanan eksternal dan memperluas kemampuan Claude Code lebih jauh lagi.

---

**Pro Tip**: Mulailah dengan membuat commands sederhana untuk tugas yang paling sering Anda lakukan, kemudian secara bertahap tingkatkan kompleksitas seiring dengan pemahaman Anda tentang fitur ini.
