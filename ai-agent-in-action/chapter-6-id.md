# Membangun asisten otonom

## Bab ini mencakup
- Pohon perilaku untuk aplikasi robotika dan AI
- GPT Assistants Playground dan membuat asisten dan tindakan
- Kontrol otonom dari pohon perilaku agentic
- Mensimulasikan sistem multi-agen percakapan melalui pohon perilaku agentic
- Menggunakan perantaian mundur untuk membuat pohon perilaku untuk sistem yang kompleks

Setelah kita membahas bagaimana tindakan memperluas kekuatan/kemampuan agen, kita dapat melihat bagaimana pohon perilaku dapat memandu sistem agentic. Kita akan mulai dengan memahami dasar-dasar pohon perilaku dan bagaimana mereka mengontrol robotika dan AI dalam game.

Kami akan kembali ke tindakan agentic dan memeriksa bagaimana tindakan dapat diimplementasikan pada platform Asisten OpenAI menggunakan proyek GPT Assistants Playground. Dari sana, kita akan melihat cara membangun pohon perilaku agentic otonom (ABT) menggunakan asisten OpenAI. Kemudian, kita akan beralih ke pemahaman kebutuhan akan kontrol dan pagar pembatas pada agen otonom dan menggunakan fungsi penghalang kontrol.

Di bagian akhir bab ini, kita akan membahas penggunaan platform AgentOps untuk memantau sistem agentic berbasis perilaku otonom kita. Ini akan menjadi bab yang menarik dengan beberapa tantangan. Mari kita mulai dengan melompat ke bagian berikutnya, yang memperkenalkan pohon perilaku.

## 6.1 Memperkenalkan pohon perilaku

Pohon perilaku adalah pola yang sudah lama ada yang digunakan untuk mengontrol robotika dan AI dalam game. Rodney A. Brooks pertama kali memperkenalkan konsep ini dalam makalahnya "A Robust Layered Control System for a Mobile Robot" pada tahun 1986. Ini meletakkan dasar untuk pola yang diperluas menggunakan struktur pohon dan simpul yang kita miliki saat ini.

Jika Anda pernah memainkan game komputer dengan karakter non-pemain (NPC) atau berinteraksi dengan sistem robot canggih, Anda telah menyaksikan pohon perilaku bekerja. Gambar 6.1 menunjukkan pohon perilaku sederhana. Pohon tersebut mewakili semua simpul utama: simpul pemilih atau fallback, simpul urutan, simpul tindakan, dan simpul kondisi.

![Gambar 6.1](Images/6-1.png "Pohon perilaku sederhana untuk memakan apel atau pir")

Tabel 6.1 menjelaskan fungsi dan tujuan dari simpul-simpul utama yang akan kita jelajahi dalam buku ini. Ada simpul dan tipe simpul lain, dan Anda bahkan dapat membuat simpul khusus, tetapi untuk saat ini, kita akan fokus pada yang ada di tabel.

**Tabel 6.1** Simpul utama yang digunakan dalam pohon perilaku

| Simpul | Tujuan | Fungsi | Tipe |
|------|---------|----------|------|
| Pemilih (fallback) | Simpul ini bekerja dengan memilih anak pertama yang berhasil diselesaikan. Ini sering disebut simpul fallback karena akan selalu kembali ke simpul terakhir yang berhasil dieksekusi. | Simpul memanggil anak-anaknya secara berurutan dan berhenti mengeksekusi ketika anak pertama berhasil. Ketika simpul anak berhasil, ia akan mengembalikan keberhasilan; jika tidak ada simpul yang berhasil, ia mengembalikan kegagalan. | Komposit |
| Urutan | Simpul ini mengeksekusi semua anaknya secara berurutan sampai satu simpul gagal atau semuanya berhasil diselesaikan. | Simpul memanggil setiap anaknya secara berurutan terlepas dari apakah mereka gagal atau berhasil. Jika semua anak berhasil, ia mengembalikan keberhasilan, dan kegagalan jika hanya satu anak yang gagal. | Komposit |
| Kondisi | Pohon perilaku tidak menggunakan logika Boolean melainkan keberhasilan atau kegagalan sebagai sarana kontrol. Kondisi mengembalikan keberhasilan jika kondisi benar dan salah jika sebaliknya. | Simpul mengembalikan keberhasilan atau kegagalan berdasarkan suatu kondisi. | Tugas |
| Tindakan | Di sinilah tindakan terjadi. | Simpul mengeksekusi dan mengembalikan keberhasilan jika berhasil atau mengembalikan kegagalan jika sebaliknya. | Tugas |
| Dekorator | Mereka bekerja dengan mengontrol eksekusi simpul anak. Mereka sering disebut sebagai kondisional karena mereka dapat menentukan apakah sebuah simpul layak dieksekusi atau aman untuk dieksekusi. | Simpul mengontrol eksekusi simpul anak. Dekorator dapat beroperasi sebagai fungsi penghalang kontrol untuk memblokir atau mencegah perilaku yang tidak diinginkan. | Dekorator |
| Paralel | Simpul ini mengeksekusi semua simpulnya secara paralel. Keberhasilan atau kegagalan dikendalikan oleh ambang batas jumlah anak yang diperlukan untuk berhasil mengembalikan keberhasilan. | Simpul mengeksekusi semua simpul anaknya secara berurutan terlepas dari status simpul. | Komposit |

Simpul utama dalam tabel 6.1 dapat menyediakan fungsionalitas yang cukup untuk menangani banyak kasus penggunaan. Namun, memahami pohon perilaku pada awalnya bisa jadi menakutkan. Anda tidak akan menghargai kompleksitas yang mendasarinya sampai Anda mulai menggunakannya. Sebelum kita membangun beberapa pohon sederhana, kita ingin melihat eksekusi secara lebih rinci di bagian selanjutnya.

### 6.1.1 Memahami eksekusi pohon perilaku

Memahami bagaimana pohon perilaku dieksekusi sangat penting untuk merancang dan mengimplementasikan pohon perilaku. Tidak seperti kebanyakan konsep dalam ilmu komputer, pohon perilaku beroperasi dalam hal keberhasilan dan kegagalan. Ketika sebuah simpul dalam pohon perilaku dieksekusi, ia akan mengembalikan keberhasilan atau kegagalan; ini bahkan berlaku untuk kondisi dan simpul pemilih.

Pohon perilaku dieksekusi dari atas ke bawah dan dari kiri ke kanan. Gambar 6.2 menunjukkan proses dan apa yang terjadi jika sebuah simpul gagal atau berhasil. Dalam contoh, AI yang dikendalikan pohon memiliki sebuah apel tetapi tidak memiliki buah pir. Di simpul urutan pertama, sebuah kondisi memeriksa apakah AI memiliki sebuah apel. Karena AI tidak memiliki apel, ia membatalkan urutan dan kembali ke pemilih. Pemilih kemudian memilih simpul anak berikutnya, urutan lain, yang memeriksa apakah AI memiliki buah pir, dan karena ia memilikinya, AI memakan apel.

![Gambar 6.2](Images/6-2.png "Proses eksekusi pohon perilaku sederhana")

Pohon perilaku memberikan kontrol atas bagaimana sistem AI akan dieksekusi pada tingkat makro atau mikro. Mengenai robotika, pohon perilaku biasanya akan dirancang untuk beroperasi pada tingkat mikro, di mana setiap tindakan atau kondisi adalah peristiwa kecil, seperti mendeteksi apel. Sebaliknya, pohon perilaku juga dapat mengontrol sistem yang lebih makro, seperti NPC dalam game, di mana setiap tindakan mungkin merupakan kombinasi dari beberapa peristiwa, seperti menyerang pemain.

Untuk sistem agentic, pohon perilaku mendukung pengendalian agen atau asisten pada tingkat yang Anda pilih. Kita akan menjelajahi pengendalian agen pada tingkat tugas dan, di bab-bab selanjutnya, tingkat perencanaan. Lagi pula, dengan kekuatan LLM, agen dapat membangun pohon perilaku mereka sendiri.

Tentu saja, beberapa bentuk kontrol AI lain dapat digunakan untuk mengontrol sistem agentic. Bagian selanjutnya akan membahas sistem-sistem yang berbeda tersebut dan membandingkannya dengan pohon perilaku.

### 6.1.2 Memutuskan pohon perilaku

Banyak sistem kontrol AI lain memiliki manfaat dan layak untuk dieksplorasi dalam mengendalikan sistem agentic. Mereka dapat menunjukkan manfaat pohon perilaku dan memberikan opsi lain untuk kasus penggunaan tertentu. Pohon perilaku adalah pola yang sangat baik, tetapi bukan satu-satunya, dan ada baiknya mempelajari yang lain.

**Tabel 6.2** Perbandingan sistem kontrol AI lainnya

| Nama Kontrol | Deskripsi | Kekurangan | Kontrol AI agentic? |
|--------------|-------------|--------------|---------------------|
| Mesin keadaan hingga <sup>a</sup> (FSM) | FSM memodelkan AI menggunakan serangkaian status dan transisi yang dipicu oleh peristiwa atau kondisi. | FSM bisa menjadi tidak praktis dengan meningkatnya kompleksitas. | FSM tidak praktis untuk agen karena tidak dapat diskalakan dengan baik. |
| Pohon keputusan <sup>b</sup> | Pohon keputusan menggunakan model keputusan seperti pohon dan kemungkinan konsekuensinya. | Pohon keputusan dapat mengalami overfitting dan kurang generalisasi dalam skenario yang kompleks. | Pohon keputusan dapat diadaptasi dan ditingkatkan dengan pohon perilaku. |
| Sistem berbasis utilitas <sup>b</sup> | Fungsi utilitas mengevaluasi dan memilih tindakan terbaik berdasarkan situasi saat ini. | Sistem ini memerlukan desain fungsi utilitas yang cermat untuk menyeimbangkan prioritas. | Pola ini dapat diadopsi dalam pohon perilaku. |
| Sistem berbasis aturan <sup>a</sup> | Kumpulan aturan if-then ini mendefinisikan perilaku AI. | Sistem ini bisa menjadi rumit dengan banyak aturan, yang mengarah pada potensi konflik. | Ini tidak terlalu praktis bila dipasangkan dengan sistem agentic yang didukung oleh LLM. |
| Sistem perencanaan <sup>c</sup> | Sistem perencanaan menghasilkan urutan tindakan untuk mencapai tujuan tertentu menggunakan algoritma perencanaan. | Sistem ini mahal secara komputasi dan memerlukan pengetahuan domain yang signifikan. | Agen sudah dapat mengimplementasikan pola seperti itu sendiri seperti yang akan kita lihat di bab-bab selanjutnya. |
| Kloning perilaku <sup>c</sup> | Kloning perilaku mengacu pada kebijakan pembelajaran dengan meniru demonstrasi ahli. | Sistem ini mungkin kesulitan dengan generalisasi ke situasi yang tidak terlihat. | Ini dapat dimasukkan ke dalam pohon perilaku atau ke dalam tugas tertentu. |
| Jaringan Tugas Hirarkis (HTN) <sup>d</sup> | HTN menguraikan tugas menjadi subtugas yang lebih kecil dan dapat dikelola yang diatur dalam hierarki. | Ini rumit untuk dikelola dan dirancang untuk tugas yang sangat besar. | HTN memungkinkan organisasi dan eksekusi tugas yang kompleks dengan lebih baik. Pola ini dapat digunakan untuk sistem agentic yang lebih besar. |
| Sistem papan tulis <sup>b</sup> | Sistem ini menampilkan pemecahan masalah kolaboratif menggunakan papan tulis bersama untuk subsistem yang berbeda. | Sistem ini sulit untuk diimplementasikan dan mengelola komunikasi antar subsistem. | Sistem agentic dapat mengimplementasikan pola serupa menggunakan percakapan atau obrolan/utas grup. |
| Algoritma genetika (GA) <sup>d</sup> | Teknik pengoptimalan ini terinspirasi oleh seleksi alam untuk mengembangkan solusi untuk memecahkan masalah. | GA intensif secara komputasi dan mungkin tidak selalu menemukan solusi optimal. | GA memiliki potensi dan bahkan dapat digunakan untuk mengoptimalkan pohon perilaku. |
| | <sup>a</sup> Tidak praktis bila mempertimbangkan sistem agentic yang kompleks<br/><sup>b</sup> Ada di pohon perilaku atau dapat dengan mudah digabungkan<br/><sup>c</sup> Biasanya diterapkan pada tingkat tugas atau tindakan/kondisi<br/><sup>d</sup> Sistem canggih yang akan membutuhkan kerja keras saat diterapkan pada agen | | |

Di bab-bab selanjutnya dari buku ini, kita akan menyelidiki beberapa pola yang dibahas dalam tabel 6.2. Secara keseluruhan, beberapa pola dapat ditingkatkan atau digabungkan menggunakan pohon perilaku sebagai dasarnya. Sementara pola lain, seperti FSM, mungkin berguna untuk eksperimen kecil, mereka kurang skalabilitas pohon perilaku.

Pohon perilaku dapat memberikan beberapa manfaat sebagai sistem kontrol AI, termasuk skalabilitas. Daftar berikut menyoroti manfaat penting lainnya dari penggunaan pohon perilaku:

- **Modularitas dan penggunaan kembali**—Pohon perilaku mempromosikan pendekatan modular untuk merancang perilaku, memungkinkan pengembang untuk membuat komponen yang dapat digunakan kembali. Simpul dalam pohon perilaku dapat dengan mudah digunakan kembali di berbagai bagian pohon atau bahkan di proyek yang berbeda, meningkatkan pemeliharaan dan mengurangi waktu pengembangan.
- **Skalabilitas**—Seiring pertumbuhan kompleksitas sistem, pohon perilaku menangani penambahan perilaku baru dengan lebih anggun daripada metode lain, seperti FSM. Pohon perilaku memungkinkan organisasi tugas secara hierarkis, membuatnya lebih mudah untuk mengelola dan memahami kumpulan perilaku yang besar.
- **Fleksibilitas dan ekstensibilitas**—Pohon perilaku menawarkan kerangka kerja yang fleksibel di mana simpul baru (tindakan, kondisi, dekorator) dapat ditambahkan tanpa mengubah struktur yang ada secara drastis. Ekstensibilitas ini membuatnya mudah untuk memperkenalkan perilaku baru atau memodifikasi yang sudah ada untuk beradaptasi dengan persyaratan baru.
- **Debugging dan visualisasi**—Pohon perilaku memberikan representasi visual perilaku yang jelas dan intuitif, yang bermanfaat untuk debugging dan memahami proses pengambilan keputusan. Alat yang mendukung pohon perilaku sering kali menyertakan editor grafis yang memungkinkan pengembang untuk memvisualisasikan dan men-debug struktur pohon, membuatnya lebih mudah untuk mengidentifikasi dan memperbaiki masalah.
- **Pemisahan logika keputusan**—Pohon perilaku memisahkan logika pengambilan keputusan dan eksekusi, mempromosikan perbedaan yang jelas antara strategi tingkat tinggi dan tindakan tingkat rendah. Pemisahan ini menyederhanakan desain dan memungkinkan modifikasi dan pengujian bagian perilaku tertentu yang lebih mudah tanpa memengaruhi seluruh sistem.

Setelah membuat argumen yang kuat untuk pohon perilaku, kita sekarang harus mempertimbangkan bagaimana mengimplementasikannya dalam kode. Di bagian selanjutnya, kita melihat cara membangun pohon perilaku sederhana, menggunakan kode Python.

### 6.1.3 Menjalankan pohon perilaku dengan Python dan py_trees

Karena pohon perilaku telah ada begitu lama dan telah dimasukkan ke dalam banyak teknologi, membuat demonstrasi sampel sangat sederhana. Tentu saja, cara termudah adalah dengan bertanya kepada ChatGPT atau alat obrolan AI favorit Anda. Daftar 6.1 menunjukkan hasil penggunaan prompt untuk menghasilkan sampel kode dan mengirimkan gambar 6.1 sebagai pohon contoh. Kode akhir harus diperbaiki untuk kesalahan penamaan dan parameter sederhana.

> **Catatan**  Semua kode untuk bab ini dapat ditemukan dengan mengunduh proyek GPT Assistants Playground di https://mng.bz/Ea0q.

**Daftar 6.1** `first_btree.py`

```python
import py_trees

class HasApple(py_trees.behaviour.Behaviour):     #1
    def __init__(self, name):
        super(HasApple, self).__init__(name)

    def update(self):       
        if True: 
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE
# Kelas lain dihilangkan…

has_apple = HasApple(name="Has apple")     #2
eat_apple = EatApple(name="Eat apple")      #2
sequence_1 = py_trees.composites.Sequence(name="Sequence 1", memory=True)
sequence_1.add_children([has_apple, eat_apple])                             #3

has_pear = HasPear(name="Has pear")        #4
eat_pear = EatPear(name="Eat pear")         #4
sequence_2 = py_trees.composites.Sequence(name="Sequence 2", memory=True)
sequence_2.add_children([has_pear, eat_pear])               #3                

root = py_trees.composites.Selector(name="Selector", memory=True)
root.add_children([sequence_1, sequence_2])          #3                       

behavior_tree = py_trees.trees.BehaviourTree(root)    #5

py_trees.logging.level = py_trees.logging.Level.DEBUG   
for i in range(1, 4):                                                     #6
    print("
------------------ Tick {0} ------------------".format(i))
    behavior_tree.tick()                                                  #6

### Awal dari output
------------------ Tick 1 ------------------
[DEBUG] Selector             : Selector.tick()
[DEBUG] Selector             : Selector.tick() [!RUNNING->reset current_child]
[DEBUG] Sequence 1           : Sequence.tick()
[DEBUG] Has apple            : HasApple.tick()
[DEBUG] Has apple            : HasApple.stop(Status.INVALID->Status.SUCCESS)
[DEBUG] Eat apple            : EatApple.tick()
Eating apple
[DEBUG] Eat apple            : EatApple.stop(Status.INVALID->Status.SUCCESS)
[DEBUG] Sequence 1           : Sequence.stop()[Status.INVALID->Status.SUCCESS]
```

- #1 Membuat kelas untuk mengimplementasikan tindakan atau kondisi
- #2 Membuat simpul tindakan dan kondisi
- #3 Menambahkan simpul ke induknya masing-masing
- #4 Membuat simpul tindakan dan kondisi
- #5 Membuat seluruh pohon perilaku
- #6 Mengeksekusi satu langkah/tick pada pohon perilaku

Kode dalam daftar 6.1 mewakili pohon perilaku pada gambar 6.1. Anda dapat menjalankan kode ini apa adanya atau mengubah apa yang dikembalikan oleh kondisi dan kemudian menjalankan pohon lagi. Anda juga dapat mengubah pohon perilaku dengan menghapus salah satu simpul urutan dari pemilih akar.

Sekarang setelah kita memiliki pemahaman dasar tentang pohon perilaku, kita dapat melanjutkan untuk bekerja dengan agen/asisten. Sebelum melakukan itu, kita akan melihat alat untuk membantu kita bekerja dengan Asisten OpenAI. Alat ini akan membantu kita membungkus ABT pertama kita di sekitar Asisten OpenAI.

## 6.2 Menjelajahi GPT Assistants Playground

Untuk pengembangan buku ini, beberapa proyek GitHub dibuat untuk mengatasi berbagai aspek pembangunan agen dan asisten. Salah satu proyek tersebut, GPT Assistants Playground, dibangun menggunakan Gradio untuk antarmuka yang meniru OpenAI Assistants Playground tetapi dengan beberapa tambahan.

Proyek Playground dikembangkan sebagai bantuan pengajaran dan demonstrasi. Di dalam proyek, kode Python menggunakan API Asisten OpenAI untuk membuat antarmuka obrolan dan sistem agentic untuk membangun dan memberdayakan asisten. Ada juga koleksi tindakan komprehensif yang dapat Anda gunakan, dan Anda dapat dengan mudah menambahkan tindakan Anda sendiri.

### 6.2.1 Menginstal dan menjalankan Playground

Daftar berikut menunjukkan cara menginstal dan menjalankan proyek Playground dari terminal. Saat ini tidak ada paket PyPI untuk diinstal.

**Daftar 6.2** Menginstal GPT Assistants Playground

```bash
# ubah ke folder kerja dan buat lingkungan virtual Python baru
git clone https://github.com/cxbxmxcx/GPTAssistantsPlayground    #1
cd GPTAssistantsPlayground     #2
pip install -r requirements.txt     #3
```

- #1 Menarik kode sumber dari GitHub
- #2 Mengubah direktori ke folder kode sumber proyek
- #3 Menginstal persyaratan

Anda dapat menjalankan aplikasi dari terminal atau menggunakan Visual Studio Code (VS Code), yang terakhir memberi Anda lebih banyak kontrol. Sebelum menjalankan aplikasi, Anda perlu mengatur kunci API OpenAI Anda melalui baris perintah atau dengan membuat file `.env`, seperti yang telah kita lakukan beberapa kali. Daftar 6.3 menunjukkan contoh pengaturan variabel lingkungan di Linux/Mac atau shell Git Bash (disarankan Windows) dan menjalankan aplikasi.

**Daftar 6.3** Menjalankan GPT Assistants Playground

```bash
export OPENAI_API_KEY="kunci-api-anda"     #1
python main.py    #2
```

- #1 Mengatur kunci API Anda sebagai variabel lingkungan
- #2 Menjalankan aplikasi dari terminal atau melalui VS Code

Buka browser Anda ke URL yang ditampilkan (biasanya `http://127.0.0.1:7860`) atau apa yang disebutkan di terminal. Anda akan melihat antarmuka yang mirip dengan yang ditunjukkan pada gambar 6.3. Jika Anda sudah mendefinisikan Asisten OpenAI, Anda akan melihatnya di dropdown Pilih Asisten.

![Gambar 6.3](Images/6-3.png "Antarmuka GPT Assistants Playground yang digunakan untuk belajar matematika")

Jika Anda belum pernah mendefinisikan asisten, Anda dapat membuatnya dan memilih berbagai opsi dan instruksi yang Anda butuhkan. Jika Anda pernah mengunjungi OpenAI Playground, Anda sudah mengalami antarmuka yang serupa.

> **GPT vs. asisten**
>
> OpenAI mendefinisikan GPT sebagai asisten yang dapat Anda jalankan dan gunakan dalam antarmuka ChatGPT. Seorang asisten hanya dapat dikonsumsi melalui API dan memerlukan kode khusus dalam banyak kasus. Saat Anda menjalankan asisten, Anda dikenai biaya sesuai dengan penggunaan token model dan alat khusus apa pun, termasuk Code Interpreter dan file, sedangkan GPT berjalan dalam ChatGPT dan ditanggung oleh biaya akun.
>
> Alasan untuk membuat versi lokal dari Playground adalah latihan untuk mendemonstrasikan struktur kode tetapi juga menyediakan fitur tambahan yang tercantum di sini:
>
> - **Tindakan (tindakan khusus)**—Membuat tindakan Anda sendiri memungkinkan Anda untuk menambahkan fungsionalitas apa pun yang Anda inginkan ke asisten. Seperti yang akan kita lihat, Playground membuatnya sangat mudah untuk membuat tindakan Anda sendiri dengan cepat.
> - **Penjalankode**—API memang dilengkapi dengan Code Interpreter, tetapi relatif mahal ($.03 per proses), tidak memungkinkan Anda menginstal modul Anda, tidak dapat menjalankan kode secara interaktif, dan berjalan lambat. Playground akan memungkinkan Anda untuk menjalankan kode Python secara lokal di lingkungan virtual yang terisolasi. Meskipun tidak seaman mendorong kode ke gambar Docker, ia mengeksekusi kode berjendela dan di luar proses lebih baik daripada platform lain.
> - **Transparansi dan pencatatan**—Playground menyediakan pencatatan log yang komprehensif dan bahkan akan menunjukkan bagaimana asisten menggunakan alat/tindakan internal dan eksternal. Ini bisa menjadi cara yang bagus untuk melihat apa yang dilakukan asisten di belakang layar.

Masing-masing fitur ini dibahas lebih rinci di beberapa bagian berikutnya. Kita akan mulai dengan melihat penggunaan dan penggunaan tindakan di bagian selanjutnya.

### 6.2.2 Menggunakan dan membangun tindakan khusus

Tindakan dan alat adalah blok bangunan yang memberdayakan agen dan asisten. Tanpa akses ke alat, agen adalah chatbot yang tidak berfungsi. Platform OpenAI adalah pemimpin dalam menetapkan banyak pola untuk alat, seperti yang kita lihat di bab 3.

Playground menyediakan beberapa tindakan khusus yang dapat dilampirkan ke asisten melalui antarmuka. Dalam latihan berikutnya, kita akan membangun asisten sederhana dan melampirkan beberapa tindakan khusus untuk melihat apa yang mungkin.

Gambar 6.4 menunjukkan akordeon Tindakan yang diperluas, yang menampilkan banyak tindakan khusus yang tersedia. Jalankan Playground dari terminal atau debugger, dan buat asisten baru. Kemudian, pilih tindakan yang ditunjukkan pada gambar. Setelah Anda selesai memilih tindakan, gulir ke bawah, dan klik Tambah Asisten untuk menambahkan asisten. Asisten perlu dibuat sebelum dapat digunakan.

![Gambar 6.4](Images/6-4.png "Memilih dan menggunakan tindakan khusus di antarmuka")

Setelah Anda membuat asisten, Anda dapat memintanya untuk mendaftar semua asisten yang tersedia. Mendaftar asisten juga memberi Anda ID yang diperlukan untuk memanggil asisten. Anda juga dapat memanggil asisten lain dan meminta mereka untuk menyelesaikan tugas di bidang spesialisasi mereka.

Menambahkan tindakan khusus Anda sesederhana menambahkan kode ke file dan meletakkannya di folder yang tepat. Buka folder `playground/assistant_actions` dari folder proyek utama, dan Anda akan melihat beberapa file yang mendefinisikan berbagai tindakan. Buka file `file_actions.py` di VS Code, seperti yang ditunjukkan pada daftar 6.4.

**Daftar 6.4** `playground/assistant_actions/file_actions.py`

```python
import os

from playground.actions_manager import agent_action

OUTPUT_FOLDER = "assistant_outputs"


@agent_action    #1
def save_file(filename, content):     #2
    """
    Simpan konten ke file.     #3

    :param filename: Nama file termasuk ekstensi.
    :param content: Konten yang akan disimpan dalam file.
    """
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"File '{filename}' berhasil disimpan.")     #4
```

- #1 Dekorator ini secara otomatis menambahkan fungsi sebagai tindakan.
- #2 Beri nama fungsi Anda yang jelas yang selaras dengan tujuannya.
- #3 Deskripsi adalah apa yang digunakan asisten untuk menentukan fungsi, jadi dokumentasikan dengan baik.
- #4 Umumnya mengembalikan pesan yang menyatakan keberhasilan atau kegagalan

Anda dapat menambahkan tindakan khusus apa pun yang Anda inginkan dengan menempatkan file di folder `assistant_actions` dan mendekorasinya dengan dekorator `agent_action`. Pastikan untuk memberikan nama yang baik pada fungsi dan memasukkan dokumentasi berkualitas tentang bagaimana fungsi tersebut harus digunakan. Saat Playground dimulai, ia memuat semua tindakan di folder yang didekorasi dengan benar dan memiliki deskripsi/dokumentasi.

Sesederhana itu. Anda dapat menambahkan beberapa tindakan khusus sesuai kebutuhan. Di bagian selanjutnya, kita akan melihat tindakan khusus khusus yang memungkinkan asisten menjalankan kode secara lokal.

### 6.2.3 Menginstal basis data asisten

Untuk menjalankan beberapa contoh dalam bab ini, Anda perlu menginstal basis data asisten. Untungnya, ini dapat dengan mudah dilakukan melalui antarmuka dan hanya dengan bertanya kepada agen. Instruksi yang akan datang merinci proses untuk menginstal asisten dan diambil langsung dari README GPT Assistants Playground. Anda dapat menginstal beberapa asisten demo yang terletak di basis data SQLite `assistants.db`:

1. Buat asisten baru, atau gunakan asisten yang sudah ada.
2. Berikan asisten tindakan `create_manager_assistant` (ditemukan di bawah bagian Tindakan).
3. Minta asisten untuk membuat asisten manajer (yaitu, "tolong buat asisten manajer"), dan pastikan untuk menamai asisten "Asisten Manajer."
4. Segarkan browser Anda untuk memuat ulang pemilih asisten.
5. Pilih Asisten Manajer baru. Asisten ini memiliki instruksi dan tindakan yang akan memungkinkannya menginstal asisten dari basis data `assistants.db`.
6. Bicaralah dengan Asisten Manajer untuk memberi Anda daftar asisten yang akan diinstal, atau cukup minta Asisten Manajer untuk menginstal semua asisten yang tersedia.

### 6.2.4 Membuat asisten menjalankan kode secara lokal

Membuat agen dan asisten menghasilkan dan menjalankan kode yang dapat dieksekusi memiliki banyak kekuatan. Tidak seperti Code Interpreter, menjalankan kode secara lokal memberikan banyak peluang untuk melakukan iterasi dan penyetelan dengan cepat. Kami melihat ini sebelumnya dengan AutoGen, di mana agen dapat terus menjalankan kode sampai berfungsi seperti yang diharapkan.

Di Playground, ini adalah masalah sederhana untuk memilih tindakan khusus `run_code`, seperti yang ditunjukkan pada gambar 6.5. Anda juga ingin memilih tindakan `run_shell_command` karena memungkinkan asisten untuk `pip install` modul yang diperlukan.

![Gambar 6.5](Images/6-5.png "Memilih tindakan khusus untuk asisten menjalankan kode Python")

Anda sekarang dapat meminta asisten untuk menghasilkan dan menjalankan kode untuk memastikan kode tersebut berfungsi atas nama Anda. Coba ini dengan menambahkan tindakan khusus dan meminta asisten untuk menghasilkan dan menjalankan kode, seperti yang ditunjukkan pada gambar 6.6. Jika kode tidak berfungsi seperti yang diharapkan, beri tahu asisten masalah apa yang Anda temui.

![Gambar 6.6](Images/6-6.png "Membuat asisten menghasilkan dan menjalankan kode Python")

Sekali lagi, kode Python yang berjalan di Playground membuat lingkungan virtual baru di subfolder proyek. Sistem ini berfungsi dengan baik jika Anda tidak menjalankan kode tingkat sistem operasi atau kode tingkat rendah. Jika Anda membutuhkan sesuatu yang lebih kuat, opsi yang baik adalah AutoGen, yang menggunakan kontainer Docker untuk menjalankan kode yang terisolasi.

Menambahkan tindakan untuk menjalankan kode atau tugas lain dapat membuat asisten terasa seperti kotak hitam. Untungnya, API Asisten OpenAI memungkinkan Anda untuk menggunakan acara dan melihat apa yang dilakukan asisten di belakang layar. Di bagian selanjutnya, kita akan melihat seperti apa ini.

### 6.2.5 Menyelidiki proses asisten melalui log

OpenAI menambahkan fitur ke dalam API Asisten yang memungkinkan Anda untuk mendengarkan acara dan tindakan yang dirantai melalui penggunaan alat/tindakan. Fitur ini telah diintegrasikan ke dalam Playground, menangkap penggunaan tindakan dan alat saat asisten memanggil asisten lain.

Kita bisa mencoba ini dengan meminta asisten untuk menggunakan alat dan kemudian membuka log. Contoh bagus tentang bagaimana Anda dapat melakukan ini adalah dengan memberikan asisten alat Code Interpreter dan kemudian memintanya untuk memplot persamaan. Gambar 6.7 menunjukkan contoh latihan ini.

![Gambar 6.7](Images/6-7.png "Log asisten internal sedang ditangkap")

Biasanya, ketika alat Asisten Code Interpreter diaktifkan, Anda tidak melihat pembuatan atau eksekusi kode apa pun. Fitur ini memungkinkan Anda untuk melihat semua alat dan tindakan yang digunakan oleh asisten saat itu terjadi. Tidak hanya alat yang sangat baik untuk diagnostik, tetapi juga memberikan wawasan tambahan tentang fungsi LLM.

Kami belum meninjau kode untuk melakukan semua ini karena sangat luas dan kemungkinan akan mengalami beberapa perubahan. Meskipun demikian, jika Anda berencana untuk bekerja dengan API Asisten, proyek ini adalah tempat yang baik untuk memulai. Dengan diperkenalkannya Playground, kita dapat melanjutkan perjalanan kita ke ABT di bagian selanjutnya.

## 6.3 Memperkenalkan pohon perilaku agentic

Pohon perilaku agentic (ABT) mengimplementasikan pohon perilaku pada sistem asisten dan agen. Perbedaan utama antara pohon perilaku biasa dan ABT adalah bahwa mereka menggunakan prompt untuk mengarahkan tindakan dan kondisi. Karena prompt dapat mengembalikan kemunculan hasil acak yang tinggi, kita juga bisa menamai pohon ini pohon perilaku *stokastik*, yang memang ada. Untuk kesederhanaan, kita akan membedakan pohon perilaku yang digunakan untuk mengontrol agen, menyebutnya sebagai agentic.

Selanjutnya, kita akan melakukan latihan untuk membuat ABT. Pohon yang sudah jadi akan ditulis dengan Python tetapi akan memerlukan pengaturan dan konfigurasi berbagai asisten. Kita akan membahas cara mengelola asisten menggunakan asisten itu sendiri.

### 6.3.1 Mengelola asisten dengan asisten

Untungnya, Playground dapat membantu kita mengelola dan membuat asisten dengan cepat. Pertama-tama kita akan menginstal Asisten Manajer, diikuti dengan menginstal asisten yang telah ditentukan sebelumnya. mari kita mulai dengan menginstal Asisten Manajer menggunakan langkah-langkah berikut:

1. Buka Playground di browser Anda, dan buat asisten sederhana baru atau gunakan asisten yang sudah ada. Jika Anda memerlukan asisten baru, buatlah lalu pilih.
2. Dengan asisten yang dipilih, buka akordeon Tindakan, dan pilih tindakan `create_ manager_assistant`. Anda tidak perlu menyimpan; antarmuka akan memperbarui asisten secara otomatis.
3. Sekarang, di antarmuka obrolan, berikan prompt kepada asisten dengan yang berikut: "Silakan buat asisten manajer."
4. Setelah beberapa detik, asisten akan mengatakan sudah selesai. Segarkan browser Anda, dan konfirmasikan bahwa Asisten Manajer sekarang tersedia. Jika karena alasan tertentu, asisten baru tidak ditampilkan, coba mulai ulang aplikasi Gradio itu sendiri.

Asisten Manajer seperti admin yang memiliki akses ke semuanya. Saat melibatkan Asisten Manajer, pastikan untuk spesifik tentang permintaan Anda. Dengan Asisten Manajer aktif, Anda sekarang dapat menginstal asisten baru yang digunakan dalam buku menggunakan langkah-langkah berikut:

1. Pilih Asisten Manajer. Jika Anda telah memodifikasi Asisten Manajer, Anda dapat menghapusnya dan menginstalnya kembali kapan saja. Meskipun dimungkinkan untuk memiliki beberapa Asisten Manajer, itu tidak disarankan.
2. Tanyakan kepada Asisten Manajer asisten apa yang dapat diinstal dengan mengetikkan yang berikut di antarmuka obrolan:

```
Tolong daftarkan semua asisten yang dapat diinstal.
```

3. Identifikasi asisten mana yang ingin Anda instal saat Anda meminta Asisten Manajer untuk menginstalnya:

```
Silakan instal Asisten Pengodean Python.
```

Anda dapat mengelola dan menginstal asisten yang tersedia menggunakan Playground. Anda juga dapat meminta Asisten Manajer untuk menyimpan definisi semua asisten Anda sebagai JSON:

```
Harap simpan semua asisten sebagai JSON ke file bernama assistants.json.
```

Asisten Manajer dapat mengakses semua tindakan, yang harus dianggap unik dan digunakan dengan hemat. Saat membuat asisten, yang terbaik adalah menjaganya agar tetap spesifik tujuan dan membatasi tindakan hanya pada apa yang mereka butuhkan. Ini tidak hanya menghindari memberi AI terlalu banyak keputusan tetapi juga menghindari kecelakaan atau kesalahan yang disebabkan oleh halusinasi.

Saat kita membahas latihan yang tersisa di bab ini, Anda mungkin perlu menginstal asisten yang diperlukan. Atau, Anda dapat meminta Asisten Manajer untuk menginstal semua asisten yang tersedia. Bagaimanapun, kita melihat pembuatan ABT dengan asisten di bagian selanjutnya.

### 6.3.2 Membangun tantangan pengodean ABT

Tantangan pengodean memberikan dasar yang baik untuk menguji dan mengevaluasi sistem agen dan asisten. Tantangan dan tolok ukur dapat mengukur seberapa baik agen atau sistem agentic beroperasi. Kami telah menerapkan tantangan pengodean ke agen multi-platform di bab 4 dengan AutoGen dan CrewAI.

Untuk tantangan pengodean ini, kita akan melangkah lebih jauh dan melihat tantangan pengodean Python dari situs Edabit (https://edabit.com), yang berkisar dalam kompleksitas dari pemula hingga ahli. Kita akan tetap dengan tantangan kode ahli karena GPT-4o dan model lain adalah pembuat kode yang sangat baik. Lihat tantangan di daftar berikutnya, dan pikirkan tentang bagaimana Anda akan menyelesaikannya.

**Daftar 6.5** Tantangan Edabit: Tanam Rumput

```
Tanam Rumput oleh AniXDownLoe

Anda akan diberikan matriks yang mewakili bidang g
dan dua angka koordinat x, y.

Ada tiga jenis karakter yang mungkin ada di matriks:

    x mewakili batu.
    o mewakili ruang tanah.
    + mewakili ruang berumput.

Anda harus mensimulasikan rumput yang tumbuh dari posisi (x, y).
Rumput dapat tumbuh ke segala empat arah (atas, kiri, kanan, bawah).
Rumput hanya bisa tumbuh di ruang tanah dan tidak bisa melewati bebatuan.

Kembalikan matriks yang disimulasikan.
Contoh

simulate_grass([
"xxxxxxx",
"xooooox",
"xxxxoox"
"xoooxxx"
"xxxxxxx"
], 1, 1) → [
"xxxxxxx",
"x+++++x",
"xxxx++x"
"xoooxxx"
"xxxxxxx"
]

Catatan

Akan selalu ada bebatuan di perimeter
```

Anda dapat menggunakan tantangan atau latihan pengodean apa pun yang Anda inginkan, tetapi berikut adalah beberapa hal yang perlu dipertimbangkan:

- Tantangan harus dapat diuji dengan pernyataan yang dapat diukur (lulus/gagal).
- Hindari membuka jendela saat meminta game, membangun situs web, atau menggunakan antarmuka lain. Suatu saat, pengujian antarmuka penuh akan dimungkinkan, tetapi untuk saat ini, itu hanya output teks.
- Hindari tantangan yang berjalan lama, setidaknya pada awalnya. Mulailah dengan menjaga tantangan tetap ringkas dan berumur pendek.

Bersamaan dengan tantangan apa pun, Anda juga menginginkan serangkaian tes atau pernyataan untuk mengonfirmasi bahwa solusinya berfungsi. Di Edabit, sebuah tantangan biasanya menyediakan serangkaian tes yang komprehensif. Daftar berikut menunjukkan tes tambahan yang disediakan bersama tantangan.

**Daftar 6.6** Tes Tanam Rumput

```
Test.assert_equals(simulate_grass(
["xxxxxxx","xooooox","xxxxoox","xoooxxx","xxxxxxx"],
 1, 1), 
["xxxxxxx","x+++++x","xxxx++x","xoooxxx","xxxxxxx"])
    Test.assert_equals(simulate_grass(
["xxxxxxx","xoxooox","xxoooox","xooxxxx",
"xoxooox","xoxooox","xxxxxxx"],
 2, 3), ["xxxxxxx","xox+++x","xx++++x","x++xxxx",
"x+xooox","x+xooox","xxxxxxx"])
    Test.assert_equals(simulate_grass(
["xxxxxx","xoxoox","xxooox","xoooox","xoooox","xxxxxx"], 
1, 1), 
["xxxxxx","x+xoox","xxooox","xoooox","xoooox","xxxxxx"])
    Test.assert_equals(simulate_grass(
["xxxxx","xooox","xooox","xooox","xxxxx"], 
1, 1),
["xxxxx","x+++x","x+++x","x+++x","xxxxx"])
    Test.assert_equals(simulate_grass(
["xxxxxx","xxxxox","xxooox","xoooxx","xooxxx",
"xooxxx","xxooox","xxxoxx","xxxxxx"], 
4, 1),
["xxxxxx","xxxx+x","xx+++x","x+++xx","x++xxx",
"x++xxx","xx+++x","xxx+xx","xxxxxx"])
    Test.assert_equals(simulate_grass(
["xxxxxxxxxxx", "xoxooooooox", "xoxoxxxxxox", 
"xoxoxoooxox", "xoxoxoxoxox", "xoxoxoxoxox", 
"xoxoxxxoxox", "xoxoooooxox", "xoxxxxxxxox", 
"xooooooooox", "xxxxxxxxxxx"], 1, 1), 
["xxxxxxxxxxx", "x+x+++++++x", "x+x+xxxxx+x", 
"x+x+x+++x+x", "x+x+x+x+x+x", "x+x+x+x+x+x", 
"x+x+xxx+x+x", "x+x+++++x+x", "x+xxxxxxx+x", 
"x+++++++++x", "xxxxxxxxxxx"])
```

Tes akan dijalankan sebagai bagian dari verifikasi dua langkah untuk mengonfirmasi bahwa solusinya berfungsi. Kami juga akan menggunakan tes dan tantangan seperti yang tertulis, yang akan menguji AI lebih lanjut.

Gambar 6.8 menunjukkan susunan pohon perilaku sederhana yang akan digunakan untuk menyelesaikan berbagai tantangan pemrograman. Anda akan melihat bahwa ABT ini menggunakan asisten yang berbeda untuk tindakan dan kondisi. Untuk langkah pertama, asisten pengodean Python (disebut Peretas) menghasilkan solusi yang kemudian ditinjau oleh Juri tantangan pengodean (disebut Juri), yang menghasilkan solusi yang disempurnakan yang diverifikasi oleh asisten pengodean Python yang berbeda (disebut Verifikator).

![Gambar 6.8](Images/6-8.png "ABT untuk tantangan pengodean")

Gambar 6.8 juga menunjukkan bagaimana setiap agen berkomunikasi di utas mana. Asisten menggunakan utas pesan, mirip dengan saluran Slack atau Discord, di mana semua asisten yang berkomunikasi di utas akan melihat semua pesan. Untuk ABT ini, kami menyimpan satu utas percakapan utama untuk Peretas dan Juri untuk berbagi pesan, sementara Verifikator bekerja pada utas pesan terpisah. Menjaga Verifikator di utasnya sendiri mengisolasinya dari kebisingan upaya pemecahan solusi.

Sekarang, membangun ABT dalam kode adalah masalah menggabungkan paket `py_trees` dan fungsi API Playground. Daftar 6.7 menunjukkan kutipan kode yang membuat setiap simpul tindakan/kondisi dengan asisten dan memberi mereka instruksi.

**Daftar 6.7** `agentic_btree_coding_challenge.py`

```python
root = py_trees.composites.Sequence("RootSequence", memory=True)


thread = api.create_thread()    #1
challenge = textwrap.dedent("""
 #2
""")
judge_test_cases = textwrap.dedent("""
 #3
""")

hacker = create_assistant_action_on_thread(   
    thread=thread,     #4
    action_name="Hacker",
    assistant_name="Python Coding Assistant",
    assistant_instructions=textwrap.dedent(f"""
    Tujuan tantangan: 
    {challenge}     #5
    Selesaikan tantangan dan keluarkan 
solusi akhir ke file bernama solution.py        
    """),
)
root.add_child(hacker)

judge = create_assistant_action_on_thread(    
    thread=thread,     #6
    action_name="Judge solution",
    assistant_name="Coding Challenge Judge",
    assistant_instructions=textwrap.dedent(
        f"""
    Tujuan tantangan: 
    {challenge}     #7
    Muat solusi dari file solution.py.
    Kemudian konfirmasikan adalah solusi untuk tantangan 
dan uji dengan kasus uji berikut:
    {judge_test_cases}     #8
    Jalankan kode untuk solusi dan konfirmasikan itu melewati semua kasus uji.
    Jika solusi melewati semua tes, simpan solusi ke file bernama 
judged_solution.py
    """,
    ),
)
root.add_child(judge)

# verifikator beroperasi pada utas yang berbeda, pada dasarnya di ruang tertutup
verifier = create_assistant_condition(    #9
    condition_name="Verify solution",
    assistant_name="Python Coding Assistant",
    assistant_instructions=textwrap.dedent(
        f"""
    Tujuan tantangan: 
    {challenge}     #10
    Muat file bernama judged_solution.py dan 
verifikasi bahwa solusinya benar dengan menjalankan kode dan konfirmasikan itu melewati 
semua kasus uji:
    {judge_test_cases}     #11
    Jika solusinya benar, kembalikan hanya satu kata SUCCESS, jika tidak 
kembalikan satu kata FAILURE.
    """,
    ),
)
root.add_child(verifier)

tree = py_trees.trees.BehaviourTree(root)


while True:
    tree.tick()
    time.sleep(20)     #12
    if root.status == py_trees.common.Status.SUCCESS:   #13
        break
### Asisten yang dibutuhkan – 
### Asisten Pengodean Python dan Juri Tantangan Pengodean 
### instal asisten ini melalui Playground
```

- #1 Membuat utas pesan yang akan dibagikan oleh Peretas dan Juri
- #2 Tantangan seperti yang ditunjukkan pada contoh daftar 6.5
- #3 Tes seperti yang ditunjukkan pada contoh daftar 6.6
- #4 Membuat utas pesan yang akan dibagikan oleh Peretas dan Juri
- #5 Tantangan seperti yang ditunjukkan pada contoh daftar 6.5
- #6 Membuat utas pesan yang akan dibagikan oleh Peretas dan Juri
- #7 Tantangan seperti yang ditunjukkan pada contoh daftar 6.5
- #8 Tes seperti yang ditunjukkan pada contoh daftar 6.6
- #9 Panggilan membuat utas pesan baru
- #10 Tantangan seperti yang ditunjukkan pada contoh daftar 6.5
- #11 Tes seperti yang ditunjukkan pada contoh daftar 6.6
- #12 Waktu tidur dapat disesuaikan naik atau turun sesuai kebutuhan dan dapat digunakan untuk membatasi pesan yang dikirim ke LLM.
- #13 Proses akan berlanjut hingga verifikasi berhasil.

Jalankan ABT dengan memuat file di VS Code atau menggunakan baris perintah. Ikuti output di terminal, dan saksikan bagaimana asisten bekerja melalui setiap langkah di pohon.

Jika solusi gagal diverifikasi pada simpul kondisi, proses akan berlanjut sesuai pohon. Bahkan dengan solusi sederhana ini, Anda dapat dengan cepat membuat banyak variasi. Anda dapat memperluas pohon dengan lebih banyak simpul/langkah dan subpohon. Mungkin Anda ingin tim Peretas memecah dan menganalisis tantangan, misalnya.

Pekerjaan contoh ini dilakukan terutama dengan kode Playground, menggunakan fungsi pembantu `create_assistant_condition` dan `create_assistant_action_on_thread`. Kode ini menggunakan beberapa kelas untuk mengintegrasikan kode pohon perilaku `py_trees` dan kode Asisten OpenAI yang dibungkus di Playground. Tinjau kode dalam proyek jika Anda ingin memahami detail tingkat rendah.

### 6.3.3 Sistem AI percakapan vs. metode lain

Kita telah melihat sistem multi-agen percakapan di bab 4 ketika kita melihat AutoGen. ABT dapat bekerja menggunakan kombinasi percakapan (melalui utas) dan metode lain, seperti berbagi file. Meminta asisten/agen Anda saling memberikan file membantu mengurangi jumlah pemikiran/percakapan yang bising dan berulang. Sebaliknya, sistem percakapan mendapat manfaat dari potensi perilaku yang muncul. Jadi, menggunakan keduanya dapat membantu mengembangkan kontrol dan solusi yang lebih baik.

Solusi sederhana dalam daftar 6.7 dapat diperluas untuk menangani lebih banyak tantangan pengodean dunia nyata dan bahkan mungkin untuk bekerja sebagai ABT pengodean. Di bagian selanjutnya, kita membangun ABT yang berbeda untuk menangani masalah yang berbeda.

### 6.3.4 Memposting video YouTube ke X

Dalam latihan bagian ini, kita melihat ABT yang dapat melakukan hal berikut:

1. Cari video di YouTube untuk topik tertentu dan kembalikan video terbaru.
2. Unduh transkrip untuk semua video yang disediakan pencarian Anda.
3. Ringkas transkrip.
4. Tinjau transkrip yang diringkas dan pilih video untuk menulis postingan X (sebelumnya Twitter).
5. Tulis postingan yang menarik dan menarik tentang video tersebut, pastikan panjangnya kurang dari 280 karakter.
6. Tinjau postingan tersebut lalu posting di X.

Gambar 6.9 menunjukkan ABT yang dirakit dengan masing-masing asisten yang berbeda. Dalam latihan ini, kami menggunakan simpul urutan untuk akar, dan setiap asisten melakukan tindakan yang berbeda. Juga, untuk menjaga agar tetap sederhana, setiap interaksi asisten akan selalu terjadi di utas baru. Ini mengisolasi interaksi setiap asisten menjadi percakapan singkat yang lebih mudah di-debug jika terjadi kesalahan.

![Gambar 6.9](Images/6-9.png "ABT media sosial YouTube")

### 6.3.5 Pengaturan X yang Diperlukan

Jika Anda berencana untuk menjalankan kode dalam latihan ini, Anda harus menambahkan kredensial X Anda ke file `.env`. File `.env.default` menunjukkan contoh bagaimana kredensial harus, seperti yang ditunjukkan pada daftar 6.8. Anda tidak harus memasukkan kredensial Anda. Ini berarti langkah terakhir, memposting, akan gagal, tetapi Anda masih dapat melihat file (`youtube_twitter_post.txt`) untuk melihat apa yang dihasilkan.

**Daftar 6.8** Mengonfigurasi kredensial

```
X_EMAIL = "email twitter di sini"
X_USERNAME = "nama pengguna twitter di sini"
X_PASSWORD = "kata sandi twitter di sini"
```

> **Pencarian dan spam YouTube**
>
> Jika Anda berencana untuk menjalankan latihan ini secara nyata dan membiarkannya memposting ke akun X Anda, perlu diketahui bahwa YouTube memiliki sedikit masalah spam. Para asisten telah dikonfigurasi untuk mencoba menghindari spam video, tetapi beberapa di antaranya mungkin lolos. Membangun ABT yang berfungsi yang dapat menjelajahi video sambil menghindari spam memiliki beberapa aplikasi yang sesuai.

Daftar 6.9 hanya menunjukkan kode untuk membuat tindakan asisten. ABT ini menggunakan tiga asisten yang berbeda, masing-masing dengan instruksi tugasnya sendiri. Perhatikan bahwa setiap asisten memiliki serangkaian instruksi unik yang mendefinisikan perannya. Anda dapat meninjau instruksi untuk setiap asisten dengan menggunakan Playground.

**Daftar 6.9** `agentic_btree_video_poster_v1.py`

```python
root = py_trees.composites.Sequence("RootSequence", memory=True)

search_term = "GPT Agents"
search_youtube_action = create_assistant_action(
    action_name=f"Search YouTube({search_term})",
    assistant_name="YouTube Researcher v2",
    assistant_instructions=f"""
    Istilah Pencarian: {search_term}
    Gunakan kueri "{search_term}" untuk mencari video di YouTube.
    kemudian untuk setiap video unduh transkrip dan rangkum 
untuk relevansi dengan {search_term}
    pastikan untuk menyertakan tautan ke setiap video,
    dan kemudian simpan semua ringkasan ke file bernama youtube_transcripts.txt
    Jika Anda mengalami kesalahan, harap kembalikan hanya kata FAILURE.
    """,
)
root.add_child(search_youtube_action)

write_post_action = create_assistant_action(
    action_name="Write Post",
    assistant_name="Twitter Post Writer",
    assistant_instructions="""
    Muat file bernama youtube_transcripts.txt,
    analisis konten untuk referensi ke istilah pencarian di bagian atas dan 
kemudian pilih
    video yang paling menarik dan relevan terkait dengan: 
    pendidikan, hiburan, atau informatif, untuk diposting di Twitter.
    Kemudian tulis postingan Twitter yang relevan dengan video tersebut,
    dan sertakan tautan ke video, bersama
    dengan sorotan atau sebutan yang menarik, 
    dan simpan ke file bernama youtube_twitter_post.txt.
    Jika Anda mengalami kesalahan, harap kembalikan hanya kata FAILURE.
    """,
)
root.add_child(write_post_action)

post_action = create_assistant_action(
    action_name="Post",
    assistant_name="Social Media Assistant",
    assistant_instructions="""
    Muat file bernama youtube_twitter_post.txt dan posting kontennya 
ke Twitter.
    Jika kontennya kosong, jangan posting apa pun.
    Jika Anda mengalami kesalahan, harap kembalikan hanya kata FAILURE.
    """,
)
root.add_child(post_action)
### Asisten yang dibutuhkan – Peneliti YouTube v2, Penulis Postingan Twitter, 
dan Asisten Media Sosial – instal asisten ini melalui Playground
```

Jalankan kode seperti biasa, dan setelah beberapa menit, postingan baru akan muncul di folder `assistants_output`. Gambar 6.10 menunjukkan contoh postingan yang dibuat menggunakan ABT ini. Menjalankan ABT ini untuk menghasilkan lebih dari beberapa postingan sehari dapat, dan kemungkinan besar akan, membuat akun X Anda diblokir. Jika Anda telah mengonfigurasi kredensial X, Anda akan melihat postingan tersebut muncul di feed Anda.

![Gambar 6.10](Images/6-10.png "Contoh postingan X dari ABT")

ABT ini ditampilkan untuk tujuan demonstrasi dan bukan untuk penggunaan produksi atau jangka panjang. Fitur utama dari demonstrasi ini adalah untuk menunjukkan pencarian dan pemuatan data, peringkasan dan pemfilteran, kemudian menghasilkan konten baru, dan akhirnya menyoroti beberapa tindakan khusus dan integrasi dengan API.

## 6.4 Membangun agen-multi otonom percakapan

Aspek percakapan dari sistem multi-agen dapat mendorong mekanisme seperti umpan balik, penalaran, dan perilaku yang muncul. Mendorong agen dengan ABT yang menyekat asisten/agen dapat efektif untuk mengendalikan proses terstruktur, seperti yang kita lihat dalam contoh posting YouTube. Namun, kami juga tidak ingin melewatkan manfaat percakapan di seluruh agen/asisten.

Untungnya, Playground menyediakan metode untuk menyekat atau menggabungkan asisten ke utas percakapan. Gambar 6.11 menunjukkan bagaimana asisten dapat disekat atau dicampur dalam berbagai kombinasi ke utas. Menggabungkan silo dengan percakapan memberikan yang terbaik dari kedua pola.

![Gambar 6.11](Images/6-11.png "Berbagai tata letak asisten yang disekat dan percakapan")

Kami akan memeriksa latihan sederhana namun praktis untuk menunjukkan keefektifan pola percakapan. Untuk latihan berikutnya, kami akan menggunakan dua asisten dalam ABT yang bercakap-cakap melalui utas yang sama. Daftar berikutnya menunjukkan konstruksi pohon dalam kode dengan asisten masing-masing.

**Daftar 6.10** `agentic_conversation_btree.py`

```python
root = py_trees.composites.Sequence("RootSequence", memory=True)
bug_file = """
# kode tidak ditampilkan
"""

thread = api.create_thread()    #1

debug_code = create_assistant_action_on_thread(    #2
    thread=thread,
    action_name="Debug code",
    assistant_name="Python Debugger",
    assistant_instructions=textwrap.dedent(f"""    
    Berikut adalah kode dengan bug di dalamnya:
    {bug_file}
    Jalankan kode untuk mengidentifikasi bug dan memperbaikinya. 
    Pastikan untuk menguji kode untuk memastikan kode berjalan tanpa kesalahan atau melempar 
pengecualian apa pun.
    """),
)
root.add_child(debug_code)

verify = create_assistant_condition_on_thread(    #3
    thread=thread,
    condition_name="Verify",
    assistant_name="Python Coding Assistant",
    assistant_instructions=textwrap.dedent(
        """
    Verifikasi solusi memperbaiki bug dan tidak ada lagi masalah.
    Verifikasi bahwa tidak ada pengecualian yang dilemparkan saat kode dijalankan.
    Balas dengan SUCCESS jika solusinya benar, jika tidak kembalikan FAILURE.
    Jika Anda puas dengan solusinya, simpan kode ke file bernama 
fixed_bug.py.
    """,
    ),
)
root.add_child(verify)
tree = py_trees.trees.BehaviourTree(root)
while True:
    tree.tick()   
    if root.status == py_trees.common.Status.SUCCESS:
        break   #4
    time.sleep(20)
```

- #1 Membuat utas pesan untuk dibagikan dan dibicarakan oleh para asisten
- #2 Membuat tindakan kode debug dengan asisten khusus
- #3 Membuat kondisi verifikasi untuk menguji apakah kode sudah diperbaiki atau tidak
- #4 Pohon akan terus berjalan sampai urutan akar selesai dengan sukses.

Tiga simpul terdiri dari pohon: urutan akar, tindakan kode debug, dan kondisi verifikasi perbaikan. Karena akar pohon adalah urutan, kedua asisten akan terus bekerja satu demi satu sampai keduanya kembali dengan sukses. Kedua asisten bercakap-cakap di utas yang sama namun dikendalikan dengan cara yang memberikan umpan balik konstan.

Jalankan latihan dengan memuat file di VS Code, atau jalankan langsung dari baris perintah. Kode contoh memiliki beberapa bug dan masalah kecil yang akan diperbaiki oleh para asisten. Setelah ABT selesai berjalan dengan sukses, Anda dapat membuka file `assistants_output/fixed_bug.py` dan memverifikasi hasilnya semuanya baik.

Kami sekarang telah melihat beberapa ABT beraksi dan memahami nuansa menggunakan silo atau percakapan. Bagian berikut akan mengajari Anda beberapa teknik untuk membangun ABT Anda sendiri.

## 6.5 Membangun ABT dengan perantaian mundur

Perantaian mundur adalah metode yang berasal dari logika dan penalaran yang digunakan untuk membantu membangun pohon perilaku dengan bekerja mundur dari tujuan. Bagian ini akan menggunakan proses perantaian mundur untuk membangun ABT yang bekerja untuk mencapai tujuan. Daftar berikut memberikan deskripsi proses secara lebih rinci:

1. **Identifikasi perilaku tujuan**. Mulailah dengan perilaku yang Anda ingin agen lakukan.
2. **Tentukan tindakan yang diperlukan**. Identifikasi tindakan yang mengarah pada perilaku tujuan.
3. **Identifikasi kondisi**. Tentukan kondisi yang harus dipenuhi agar setiap tindakan berhasil.
4. **Tentukan mode komunikasi**. Tentukan bagaimana para asisten akan menyampaikan informasi. Akankah para asisten disekat atau bercakap-cakap melalui utas, atau apakah kombinasi pola lebih baik?
5. **Bangun pohon.** Mulailah dengan membangun pohon perilaku dari perilaku tujuan, menambahkan simpul untuk tindakan dan kondisi secara rekursif sampai semua kondisi yang diperlukan terhubung ke status atau fakta yang diketahui.

Pohon perilaku biasanya menggunakan pola yang disebut *papan tulis* untuk berkomunikasi di seluruh simpul. Papan tulis, seperti yang ada di `py_trees`, menggunakan penyimpanan kunci/nilai untuk menyimpan informasi dan membuatnya dapat diakses di seluruh simpul. Ini juga menyediakan beberapa kontrol, seperti membatasi akses ke simpul tertentu.

Kami menunda penggunaan file untuk komunikasi karena kesederhanaan dan transparansinya. Suatu saat, sistem agentic diharapkan untuk mengonsumsi lebih banyak informasi dan dalam format yang berbeda dari yang dirancang untuk papan tulis. Papan tulis harus menjadi lebih canggih atau diintegrasikan dengan solusi penyimpanan file.

Mari kita bangun ABT menggunakan perantaian mundur. Kita bisa mengatasi berbagai tujuan, tetapi satu tujuan yang menarik dan mungkin meta adalah membangun ABT yang membantu membangun asisten. Jadi mari kita pertama-tama sajikan tujuan kita sebagai pernyataan "Buat asisten yang dapat membantu saya melakukan {tugas}":

- **Tindakan yang diperlukan**: (bekerja mundur)
  - Buat asisten.
  - Verifikasi asisten.
  - Uji asisten.
  - Beri nama asisten.
  - Berikan instruksi yang relevan kepada asisten.
- **Kondisi yang teridentifikasi**:
  - Verifikasi asisten.
- **Tentukan pola komunikasi**: Agar tetap menarik, kami akan menjalankan semua asisten di utas pesan yang sama.
- **Bangun pohon**: Untuk membangun pohon, mari kita balik urutan tindakan dan tandai setiap elemen tindakan dan kondisi yang sesuai:
  - (tindakan) Berikan instruksi yang relevan kepada asisten untuk membantu pengguna dengan tugas tertentu.
  - (tindakan) Beri nama asisten.
  - (tindakan) Uji asisten.
  - (kondisi) Verifikasi asisten.
  - (tindakan) Buat asisten.

Tentu saja, solusi sederhana untuk membangun pohon sekarang adalah dengan bertanya kepada ChatGPT atau model lain yang mampu. Hasil dari meminta ChatGPT untuk membuat pohon ditunjukkan pada daftar berikutnya. Anda juga bisa mengerjakan pohon secara mandiri dan mungkin memperkenalkan elemen lain.

**Daftar 6.11** ABT untuk membangun asisten

```
Akar
│
├── Urutan
│    ├── Tindakan: Berikan instruksi yang relevan kepada asisten untuk membantu pengguna 
dengan tugas tertentu
│    ├── Tindakan: Beri nama asisten
│    ├── Tindakan: Uji asisten
│    ├── Kondisi: Verifikasi asisten
│    └── Tindakan: Buat asisten
```

Dari titik ini, kita dapat mulai membangun pohon dengan melakukan iterasi pada setiap simpul tindakan dan kondisi dan menentukan instruksi apa yang dibutuhkan asisten. Ini juga dapat mencakup alat dan tindakan khusus apa pun, termasuk yang mungkin perlu Anda kembangkan. Pada percobaan pertama Anda, jaga agar instruksi tetap generik. Idealnya, kami ingin membuat sesedikit mungkin asisten.

Setelah menentukan asisten, alat, dan tindakan untuk setiap asisten dan untuk tugas mana, Anda dapat mencoba untuk menggeneralisasi lebih lanjut. Pikirkan di mana dimungkinkan untuk menggabungkan tindakan dan mengurangi jumlah asisten. Lebih baik mulai mengevaluasi dengan asisten yang tidak mencukupi daripada dengan terlalu banyak. Namun, pastikan untuk mempertahankan pembagian kerja yang tepat sebagai tugas: misalnya, pengujian dan verifikasi paling baik dilakukan dengan asisten yang berbeda.

## 6.6 Latihan

Selesaikan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- **Latihan 1**—Membuat ABT Perencana Perjalanan

  **Tujuan**—Membangun pohon perilaku agentic (ABT) untuk merencanakan rencana perjalanan menggunakan asisten.

  **Tugas**:
  
  - Siapkan GPT Assistants Playground di mesin lokal Anda.
  - Buat ABT untuk merencanakan rencana perjalanan. Pohon harus memiliki struktur berikut:
    - Tindakan: Gunakan asisten Perjalanan untuk mengumpulkan informasi tentang tujuan potensial.
    - Tindakan: Gunakan Perencana Rencana Perjalanan untuk membuat rencana perjalanan harian.
    - Kondisi: Verifikasi kelengkapan dan kelayakan rencana perjalanan menggunakan Asisten Perjalanan lain.
  - Implementasikan dan run the ABT untuk membuat rencana perjalanan yang lengkap.

- **Latihan 2**—Membangun ABT untuk Otomatisasi Dukungan Pelanggan

  **Tujuan**—Membuat ABT yang mengotomatiskan respons dukungan pelanggan menggunakan asisten.

  **Tugas**:
  
  - Siapkan GPT Assistants Playground di mesin lokal Anda.
  - Buat ABT dengan struktur berikut:
    - Tindakan: Gunakan asisten Penganalisis Kueri Pelanggan untuk mengkategorikan kueri pelanggan.
    - Tindakan: Gunakan asisten Penghasil Respons untuk menyusun respons berdasarkan kategori kueri.
    - Tindakan: Gunakan asisten Dukungan Pelanggan untuk mengirim respons ke pelanggan.
  - Implementasikan dan jalankan ABT untuk mengotomatiskan proses analisis dan respons terhadap kueri pelanggan.

- **Latihan 3**—Mengelola Inventaris dengan ABT

  **Tujuan**—Pelajari cara membuat dan mengelola tingkat inventaris menggunakan ABT.

  **Tugas**:
  
  - Siapkan GPT Assistants Playground di mesin lokal Anda.
  - Buat ABT yang mengelola inventaris untuk bisnis ritel:
    - Tindakan: Gunakan asisten Pemeriksa Inventaris untuk meninjau tingkat stok saat ini.
    - Tindakan: Gunakan asisten Pesanan untuk memesan barang dengan stok rendah.
    - Kondisi: Verifikasi bahwa pesanan telah dilakukan dengan benar dan perbarui catatan inventaris.
  - Implementasikan dan jalankan ABT untuk mengelola inventaris secara dinamis.

- **Latihan 4**—Membuat ABT Pelatih Kebugaran Pribadi

  **Tujuan**—Membuat ABT yang menyediakan rencana pelatihan kebugaran yang dipersonalisasi menggunakan asisten.

  **Tugas**:
  
  - Siapkan GPT Assistants Playground di mesin lokal Anda.
  - Buat ABT untuk mengembangkan rencana kebugaran yang dipersonalisasi:
    - Tindakan: Gunakan asisten Penilaian Kebugaran untuk mengevaluasi tingkat kebugaran pengguna saat ini.
    - Tindakan: Gunakan Penghasil Rencana Pelatihan untuk membuat rencana kebugaran khusus berdasarkan penilaian.
    - Kondisi: Verifikasi kesesuaian dan keamanan rencana menggunakan asisten Kebugaran lain.
  - Implementasikan dan jalankan ABT untuk menghasilkan dan memvalidasi rencana pelatihan kebugaran yang dipersonalisasi.

- **Latihan 5**—Menggunakan Perantaian Mundur untuk Membangun ABT Penasihat Keuangan

  **Tujuan**—Menerapkan perantaian mundur untuk membangun ABT yang memberikan nasihat keuangan dan strategi investasi.

  **Tugas**:
  
  - Siapkan GPT Assistants Playground di mesin lokal Anda.
  - Tentukan tujuan berikut: "Buat asisten yang dapat memberikan nasihat keuangan dan strategi investasi."
  - Dengan menggunakan perantaian mundur, tentukan tindakan dan kondisi yang diperlukan untuk mencapai tujuan ini.
  - Implementasikan dan jalankan ABT untuk menghasilkan layanan penasihat keuangan yang komprehensif dengan merantai mundur konstruksi tindakan dan kondisi dasar untuk pohon.

## Ringkasan

- Pohon perilaku adalah pola kontrol AI yang kuat dan dapat diskalakan, pertama kali diperkenalkan dalam robotika oleh Rodney A. Brooks. Mereka banyak digunakan dalam game dan robotika karena modularitas dan dapat digunakan kembali.
- Simpul utama dalam pohon perilaku adalah pemilih, urutan, kondisi, tindakan, dekorator, dan simpul paralel. Pemilih seperti blok "atau": urutan mengeksekusi simpul secara berurutan, kondisi menguji status, tindakan melakukan pekerjaan, dekorator adalah pembungkus, dan simpul paralel memungkinkan eksekusi ganda.
- Memahami alur eksekusi pohon perilaku dapat menjadi sangat penting untuk merancang, membangun, dan mengoperasikannya untuk memberikan kontrol untuk membuat jalur pengambilan keputusan yang jelas.
- Keuntungan pohon perilaku termasuk modularitas, skalabilitas, fleksibilitas, kemudahan debugging, dan pemisahan logika keputusan, membuat pohon perilaku cocok untuk sistem AI yang kompleks.
- Menyiapkan dan menjalankan pohon perilaku sederhana di Python memerlukan penamaan dan pendokumentasian simpul khusus dengan benar.
- Proyek GPT Assistants Playground adalah antarmuka berbasis Gradio yang meniru OpenAI Assistants Playground dengan fitur tambahan untuk mengajar dan mendemonstrasikan ABT.
- GPT Assistants Playground memungkinkan pembuatan dan pengelolaan tindakan khusus, yang penting untuk membangun asisten serbaguna.
- ABT mengontrol agen dan asisten dengan menggunakan prompt untuk mengarahkan tindakan dan kondisi untuk asisten. ABT menggunakan kekuatan LLM untuk menciptakan sistem yang dinamis dan otonom.
- Perantaian mundur adalah metode untuk membangun pohon perilaku dengan bekerja mundur dari perilaku tujuan. Proses ini melibatkan identifikasi tindakan, kondisi, dan pola komunikasi yang diperlukan, dan kemudian membangun pohon langkah demi langkah.
- Sistem agentic mendapat manfaat dari pola silo dan percakapan untuk berkomunikasi antar entitas. ABT dapat mengambil manfaat dari penggabungan asisten silo dan percakapan untuk menggunakan proses terstruktur dan perilaku yang muncul.
