# Perencanaan dan umpan balik agen

## Bab ini mencakup
- Merencanakan LLM dan mengimplementasikannya dalam agen dan asisten
- Menggunakan platform Asisten OpenAI melalui tindakan khusus
- Menerapkan/menguji perencana generik pada LLM
- Menggunakan mekanisme umpan balik pada model-model canggih
- Perencanaan, penalaran, evaluasi, dan umpan balik dalam membangun sistem agentic

Setelah kita mempelajari bagaimana model bahasa besar (LLM) dapat bernalar dan merencanakan, bab ini membawa konsep ini selangkah lebih maju dengan menerapkan perencanaan dalam kerangka kerja agen. Perencanaan harus menjadi inti dari setiap platform atau perangkat agen/asisten. Kita akan mulai dengan melihat dasar-dasar perencanaan dan cara mengimplementasikan perencana melalui *prompting*. Kemudian, kita akan melihat bagaimana perencanaan beroperasi menggunakan platform Asisten OpenAI, yang secara otomatis menggabungkan perencanaan. Dari sana, kita akan membangun dan mengimplementasikan perencana umum untuk LLM.

Perencanaan hanya bisa berjalan sejauh ini, dan elemen yang sering tidak dikenali adalah umpan balik. Oleh karena itu, di bagian terakhir bab ini, kita akan menjelajahi umpan balik dan mengimplementasikannya dalam sebuah perencana. Anda harus terbiasa dengan konten bab 10, jadi silakan tinjau jika perlu, dan jika Anda siap, mari kita mulai merencanakan.

## 11.1 Perencanaan: Alat penting untuk semua agen/asisten

Agen dan asisten yang tidak dapat merencanakan dan hanya mengikuti interaksi sederhana tidak lebih dari *chatbot*. Seperti yang telah kita lihat di seluruh buku ini, tujuan kita bukanlah untuk membangun *bot*, melainkan untuk membangun agen pemikir otonom—agen yang dapat mengambil tujuan, mencari cara untuk menyelesaikannya, dan kemudian kembali dengan hasilnya.

Gambar 11.1 menjelaskan proses perencanaan keseluruhan yang akan dilakukan oleh agen/asisten. Gambar ini juga disajikan di bab 1, tetapi mari kita tinjau sekarang secara lebih rinci. Di bagian atas gambar, pengguna mengirimkan tujuan. Dalam sistem *agentic*, agen mengambil tujuan, menyusun rencana, melaksanakannya, dan kemudian mengembalikan hasilnya.

![Proses perencanaan agen](Images/11-1.png)

Tergantung pada interaksi Anda dengan platform seperti ChatGPT dan GPT, Claude, dan lainnya, Anda mungkin sudah pernah bertemu dengan asisten perencanaan dan bahkan tidak menyadarinya. Perencanaan menjadi ada di mana-mana dan sekarang dibangun di sebagian besar platform komersial untuk membuat model tampak lebih cerdas dan mampu. Oleh karena itu, dalam latihan berikutnya, kita akan melihat contoh untuk menetapkan garis dasar dan membedakan antara LLM yang tidak dapat merencanakan dan agen yang bisa.

Untuk latihan berikutnya, kita akan menggunakan Nexus untuk menunjukkan bagaimana LLM mentah tidak dapat merencanakan secara mandiri. Jika Anda memerlukan bantuan untuk menginstal, mengatur, dan menjalankan Nexus, lihat bab 7. Setelah Anda menginstal dan menyiapkan Nexus, kita dapat mulai menjalankannya dengan antarmuka Gradio, menggunakan perintah yang ditunjukkan berikutnya.

**Daftar 11.1** Menjalankan Nexus dengan antarmuka Gradio
```
nexus run gradio
```

Gradio adalah alat antarmuka web yang sangat baik yang dibuat untuk mendemonstrasikan proyek pembelajaran mesin Python. Gambar 11.2 menunjukkan antarmuka Gradio Nexus dan proses untuk membuat agen dan menggunakan mesin agen (OpenAI, Azure, dan Groq) pilihan Anda. Anda tidak dapat menggunakan LM Studio kecuali model/server mendukung penggunaan alat/tindakan. Claude dari Anthropic mendukung perencanaan internal, jadi untuk tujuan latihan ini, hindari menggunakan model ini.

![Membuat agen baru di Nexus](Images/11-2.png)

Setelah membuat agen, kami ingin memberinya tindakan (alat) spesifik untuk dilakukan atau menyelesaikan tujuan. Umumnya, memberikan hanya tindakan yang dibutuhkan agen untuk menyelesaikan tujuannya adalah yang terbaik karena beberapa alasan:

- Lebih banyak tindakan dapat membingungkan agen dalam memutuskan mana yang akan digunakan atau bahkan bagaimana menyelesaikan tujuan.
- API memiliki batasan jumlah alat yang dapat dikirimkan; pada saat penulisan, mencapai batas ini relatif mudah.
- Agen dapat menggunakan tindakan Anda dengan cara yang tidak Anda inginkan kecuali itu tujuan Anda. Namun, berhati-hatilah, bahwa tindakan dapat memiliki konsekuensi.
- Keamanan dan keselamatan perlu dipertimbangkan. LLM tidak akan mengambil alih dunia, tetapi mereka membuat kesalahan dan dengan cepat keluar jalur. Ingat, agen-agen ini akan beroperasi secara independen dan dapat melakukan tindakan apa pun.

> **PERINGATAN** Saat menulis buku ini dan bekerja dengan dan membangun agen selama berjam-jam, saya telah mengalami beberapa contoh agen yang menjadi liar dengan tindakan, mulai dari mengunduh file hingga menulis dan mengeksekusi kode saat tidak dimaksudkan, terus-menerus berulang dari alat ke alat, dan bahkan menghapus file yang seharusnya tidak mereka hapus. Menyaksikan agen memunculkan perilaku baru menggunakan tindakan bisa menyenangkan, tetapi segalanya bisa dengan cepat menjadi kacau.

Untuk latihan ini, kita akan mendefinisikan tujuan yang dijelaskan dalam daftar berikut.

**Daftar 11.2** Mendemonstrasikan perencanaan: Tujuannya
```
Cari halaman Wikipedia tentang {topik} dan unduh setiap halaman dan simpan
ke file bernama Wikipedia_{topik}.txt
```

Tujuan ini akan menunjukkan tindakan-tindakan berikut:

- `search_wikipedia(topic)`—Mencari Wikipedia dan mengembalikan ID halaman untuk istilah pencarian yang diberikan.
- `get_wikipedia_page(page_id)`—Mengunduh konten halaman berdasarkan ID halaman.
- `save_file`—Menyimpan konten ke file.

Atur tindakan pada agen, seperti yang ditunjukkan pada gambar 11.3. Anda juga ingin memastikan Perencana diatur ke Tidak Ada. Kita akan membahas pengaturan dan penggunaan perencana segera. Anda tidak perlu mengklik Simpan; antarmuka secara otomatis menyimpan perubahan agen.

![Memilih tindakan untuk agen dan menonaktifkan perencana](Images/11-3.png)

Setelah Anda memilih tindakan dan perencana, masukkan tujuan di daftar 11.2. Kemudian klik Buat Utas Baru untuk membuat percakapan baru. Ganti topik yang ingin Anda cari di input obrolan, dan tunggu agen merespons. Berikut adalah contoh tujuan yang diisi dengan topik, tetapi sekali lagi, gunakan topik apa pun yang Anda suka:

```
Cari halaman Wikipedia tentang Calgary dan unduh setiap halaman dan simpan ke
file bernama Wikipedia_Calgary.txt.
```

Gambar 11.4 menunjukkan hasil pengiriman tujuan ke agen biasa. Kita melihat agen mengeksekusi alat/tindakan untuk mencari topik tetapi tidak dapat mengeksekusi langkah apa pun di luar itu. Jika Anda ingat dari diskusi dan contoh kode tindakan kita di bab 5, OpenAI, Groq, dan Azure OpenAI semuanya mendukung tindakan paralel tetapi bukan tindakan berurutan atau terencana.

![Hasil dari mencoba membuat agen/LLM menyelesaikan tujuan](Images/11-4.png)

LLM dapat menjawab dengan cukup baik jika Anda mengirimkan tujuan dengan beberapa tugas/tindakan paralel. Namun, jika tindakannya berurutan, yang mengharuskan satu langkah bergantung pada langkah lain, itu akan gagal. Ingat, tindakan paralel adalah tindakan mandiri yang dapat dijalankan bersama yang lain.

Claude dari Anthropic dan Asisten OpenAI mendukung perencanaan tindakan berurutan. Ini berarti kedua model dapat dipanggil dengan rencana berurutan, dan model akan melaksanakannya dan mengembalikan hasilnya. Di bagian selanjutnya, kita akan menjelajahi perencanaan berurutan dan kemudian mendemonstrasikannya dalam tindakan.

## 11.2 Memahami proses perencanaan berurutan

Dalam latihan berikutnya, kita akan meminta asisten OpenAI untuk menyelesaikan tujuan yang sama. Jika Anda memiliki kredensial Anthropic/Claude dan telah mengonfigurasi mesin, Anda juga dapat mencoba latihan ini dengan model tersebut.

Gambar 11.5 menunjukkan perbedaan antara mengeksekusi tugas secara berurutan (perencanaan) dan menggunakan iterasi. Jika Anda pernah menggunakan GPT, asisten, atau Claude Sonnet 3.5, Anda mungkin sudah mengalami perbedaan ini. Alat-alat canggih ini sudah menggabungkan perencanaan dengan anotasi *prompt*, pelatihan lanjutan, atau kombinasi keduanya.

![Perbedaan antara eksekusi berulang dan terencana](Images/11-5.png)

Seiring berkembangnya layanan LLM dan obrolan, sebagian besar model kemungkinan akan secara native mendukung beberapa bentuk perencanaan dan penggunaan alat. Namun, sebagian besar model, termasuk GPT-4o, hanya mendukung penggunaan tindakan/alat saat ini.

Mari kita buka GPT Assistants Playground untuk mendemonstrasikan perencanaan berurutan dalam tindakan. Jika Anda memerlukan bantuan, lihat panduan penyiapan di bab 6. Kita akan menggunakan tujuan yang sama tetapi, kali ini, menjalankannya pada asisten (yang memiliki perencanaan bawaan).

Setelah Anda meluncurkan Playground, buat asisten baru, dan berikan tindakan `search_wikipedia`, `get_wikipedia_page`, dan `save_file`. Gambar 11.6 menunjukkan hasil memasukkan tujuan ke asisten. Seperti yang Anda lihat, asisten menyelesaikan semua tugas di belakang layar dan merespons dengan output akhir yang diminta pengguna, mencapai tujuan.

![Asisten memproses tujuan dan mengeluarkan hasil](Images/11-6.png)

Untuk menunjukkan keefektifan perencana Asisten OpenAI, kami menambahkan tugas lain, yaitu merangkum setiap halaman, ke tujuan. Tugas yang disisipkan tidak memiliki fungsi/alat, tetapi asisten cukup cerdas untuk menggunakan kemampuannya untuk merangkum konten. Anda dapat melihat output dari apa yang dihasilkan asisten dengan membuka file `[root folder]assistants_working_folder/Wikipedia_{topic}.txt` dan meninjau isinya. Sekarang setelah kita memahami bagaimana LLM berfungsi tanpa perencana dan perencanaan, kita dapat melanjutkan ke pembuatan perencana kita sendiri di bagian selanjutnya.

## 11.3 Membangun perencana berurutan

Alat LLM seperti LangChain dan Semantic Kernel (SK) memiliki banyak perencana yang menggunakan berbagai strategi. Namun, menulis perencana kita sendiri relatif mudah, dan Nexus juga mendukung antarmuka gaya *plugin* yang memungkinkan Anda menambahkan perencana lain dari alat seperti LangChain dan SK, atau turunan Anda sendiri.

Perencana mungkin terdengar rumit, tetapi mereka mudah diimplementasikan melalui strategi rekayasa *prompt* yang menggabungkan perencanaan dan penalaran. Di bab 10, kita membahas dasar-dasar penalaran dan menurunkan rencana, dan sekarang kita dapat memanfaatkan keterampilan tersebut dengan baik.

Daftar 11.3 menunjukkan perencana berurutan yang diturunkan dari SK, yang diperluas untuk memasukkan iterasi. Perencana anotasi *prompt* seperti yang ditunjukkan dalam daftar dapat disesuaikan agar sesuai dengan kebutuhan spesifik atau menjadi lebih umum seperti yang ditunjukkan. Perencana ini menggunakan JSON, tetapi perencana dapat menggunakan format apa pun yang dipahami LLM, termasuk kode.

**Daftar 11.3** `basic_nexus_planner.py`
```
Anda adalah perencana untuk Nexus. #1
Tugas Anda adalah membuat rencana JSON yang diformat dengan benar langkah demi langkah, untuk
memenuhi tujuan yang diberikan.
Buat daftar subtugas berdasarkan [TUJUAN] yang diberikan.
Setiap subtugas harus berasal dari dalam daftar [FUNGSI YANG TERSEDIA]. Jangan
gunakan fungsi apa pun yang tidak ada dalam daftar.
Dasarkan keputusan Anda tentang fungsi mana yang akan digunakan dari deskripsi dan
nama fungsi.
Terkadang, sebuah fungsi mungkin memerlukan argumen. Berikan jika perlu.
Rencananya harus sesingkat mungkin.
Anda juga akan diberikan daftar umpan balik korektif, sugestif, dan epistemik
dari rencana sebelumnya untuk membantu Anda membuat keputusan.
Sebagai contoh:

[FUNGSI KHUSUS] #2
awalan for-each-
deskripsi: jalankan fungsi untuk setiap item dalam daftar
argumen:
- fungsi: fungsi yang akan dieksekusi
- daftar: daftar item yang akan diulang
- indeks: nama argumen untuk item saat ini dalam daftar

[FUNGSI YANG TERSEDIA]
GetJokeTopics
deskripsi: Dapatkan daftar ([str]) topik lelucon

EmailTo
deskripsi: kirim email teks masukan ke penerima
argumen:
- teks: teks yang akan dikirim melalui email
- penerima: alamat email penerima. Beberapa alamat dapat
disertakan jika dipisahkan oleh ';'.

Summarize
deskripsi: rangkum teks masukan
argumen:
- teks: teks yang akan dirangkum

Joke
deskripsi: Hasilkan lelucon lucu
argumen:
- topik: topik untuk menghasilkan lelucon

[TUJUAN]
"Dapatkan daftar topik lelucon dan hasilkan lelucon yang berbeda untuk setiap topik.
Kirim lelucon melalui email ke seorang teman."

[KELUARAN]
     {
         "subtugas": [
             {"fungsi": "GetJokeTopics"},
             {"fungsi": "for-each",
              "args": {
                        "list": "output_GetJokeTopics",
                        "index": "topic",
                        "function":
                                   {
                                    "function": "Joke",
                                    "args": {"topic": "topic"}}}},
             {
              "function": "EmailTo",
               "args": {
                         "text": "for-each_output_GetJokeTopics"
                        "penerima": "teman"}}
         ]
     }
# 2 contoh lagi diberikan tetapi dihilangkan dari daftar ini

[FUNGSI KHUSUS] #3
for-each
deskripsi: jalankan fungsi untuk setiap item dalam daftar
argumen:
- fungsi: fungsi yang akan dieksekusi
- iterator: daftar item yang akan diulang
- indeks: nama argumen untuk item saat ini dalam daftar

[FUNGSI YANG TERSEDIA] #4
{{$available_functions}}

[TUJUAN]
{{$goal}} #5

Pastikan untuk hanya menggunakan fungsi dari daftar fungsi yang tersedia.
Rencananya harus sesingkat mungkin.
Dan hanya kembalikan rencana dalam format JSON.
[KELUARAN] #6
```
#1 Instruksi pembukaan yang memberitahu agen cara memproses contoh
#2 Awal dari tiga contoh (sedikit-tembakan)
#3 Menambahkan fungsi iteratif khusus for-each
#4 Fungsi yang tersedia diisi secara otomatis dari daftar fungsi yang tersedia agen.
#5 Tujuan disisipkan di sini.
#6 Di mana agen diharapkan menempatkan output

Gambar 11.7 menunjukkan proses membangun dan menjalankan *prompt* perencanaan, dari membangun hingga eksekusi hingga akhirnya mengembalikan hasil kepada pengguna. Perencana bekerja dengan membangun *prompt* perencanaan, mengirimkannya ke LLM untuk menyusun rencana, mengurai dan mengeksekusi rencana secara lokal, mengembalikan hasil ke LLM untuk mengevaluasi dan merangkum, dan akhirnya mengembalikan output akhir kembali ke pengguna.

![Proses perencanaan untuk membuat dan melaksanakan rencana](Images/11-7.png)

Penting untuk memperhatikan beberapa detail halus tentang proses perencanaan. Biasanya, rencana dibangun secara terpisah dengan tidak menambahkan riwayat konteks. Ini dilakukan untuk fokus pada tujuan karena sebagian besar *prompt* perencanaan menggunakan banyak token. Mengeksekusi fungsi di dalam eksekutor biasanya dilakukan di lingkungan lokal dan mungkin termasuk memanggil API, mengeksekusi kode, atau bahkan menjalankan model pembelajaran mesin.

Daftar 11.4 menunjukkan kode untuk fungsi `create_plan` dari kelas `BasicNexusPlanner`; alat seperti LangChain dan SK menggunakan pola serupa. Proses ini memuat tindakan agen sebagai string. Daftar tujuan dan fungsi yang tersedia kemudian dimasukkan ke dalam templat *prompt* perencana menggunakan `PromptTemplateManager`, yang hanya merupakan pembungkus untuk kode penanganan templat. Penanganan templat dilakukan dengan regex sederhana tetapi juga bisa lebih canggih menggunakan alat seperti Jinja2, Handlebars, atau Mustache.

**Daftar 11.4** `basic_nexus_planner.py` (`create_plan`)
```
def create_plan(self, nexus, agent, goal: str, prompt: str = PROMPT) -> Plan:
    selected_actions = nexus.get_actions(agent.actions)
    available_functions_string = "

".join(
        format_action(action) for action in selected_actions
    )    #1

    context = {}    #2
    context["goal"] = goal
    context["available_functions"] = available_functions_string

    ptm = PromptTemplateManager()    #3
    prompt = ptm.render_prompt(prompt, context)

    plan_text = nexus.execute_prompt(agent, prompt)    #4
    return Plan(prompt=prompt,
                goal=goal,
                plan_text=plan_text)    #5
```
#1 Memuat tindakan yang tersedia agen dan memformat string hasil untuk perencana
#2 Konteks akan disuntikkan ke dalam templat *prompt* perencana.
#3 Manajer templat sederhana, mirip konsepnya dengan Jinja2, Handlebars, atau Mustache
#4 Mengirimkan *prompt* perencana yang telah diisi ke LLM
#5 Hasil (rencana) dibungkus dalam kelas Plan dan dikembalikan untuk dieksekusi.

Kode untuk mengeksekusi rencana, yang ditunjukkan pada daftar 11.5, mengurai string JSON dan mengeksekusi fungsi-fungsi tersebut. Saat mengeksekusi rencana, kode mendeteksi fungsi `for-each` tertentu, yang melakukan iterasi melalui daftar dan mengeksekusi setiap elemen dalam suatu fungsi. Hasil dari setiap eksekusi fungsi ditambahkan ke konteks. Konteks ini diteruskan ke setiap panggilan fungsi dan dikembalikan sebagai output akhir.

**Daftar 11.5** `basic_nexus_planner.py` (`execute_plan`)
```
def execute_plan(self, nexus, agent, plan: Plan) -> str:
    context = {}
    plan = plan.generated_plan
    for task in plan["subtasks"]:    #1
        if task["function"] == "for-each":    #2
            list_name = task["args"]["list"]
            index_name = task["args"]["index"]
            inner_task = task["args"]["function"]

            list_value = context.get(list_name, [])
            for item in list_value:
                context[index_name] = item
                result = nexus.execute_task(agent, inner_task, context)
                context[f"for-each_{list_name}_{item}"] = result

            for_each_output = [     #2
                context[f"for-each_{list_name}_{item}"]
                  for item in list_value
            ]
            context[f"for-each_{list_name}"] = for_each_output

            for item in list_value:    #3
                del context[f"for-each_{list_name}_{item}"]

        else:
            result = nexus.execute_task(agent,
                                        task,
                                        context)    #4
            context[f"output_{task['function']}"] = result

    return context    #5
```
#1 Melakukan iterasi melalui setiap subtugas dalam rencana
#2 Menangani fungsi yang harus diulang dan menambahkan daftar hasil lengkap ke konteks
#3 Menghapus entri konteks for-each individual
#4 Eksekusi tugas umum
#5 Mengembalikan konteks lengkap, yang mencakup hasil dari setiap panggilan fungsi

Konteks yang dikembalikan dari seluruh eksekusi dikirim dalam panggilan terakhir ke LLM, yang merangkum hasil dan mengembalikan respons. Jika semuanya berjalan sesuai rencana, LLM akan merespons dengan ringkasan hasil. Jika ada kesalahan atau ada yang kurang, LLM dapat mencoba memperbaiki masalah atau memberi tahu pengguna tentang kesalahan tersebut.

Sekarang mari kita buka Nexus lagi dan uji perencana dalam operasi. Muat agen yang sama yang Anda gunakan terakhir kali, tetapi kali ini pilih perencana di bawah opsi Lanjutan, seperti yang ditunjukkan pada gambar 11.8. Kemudian, masukkan *prompt* tujuan seperti yang Anda lakukan sebelumnya, dan biarkan agen mengambil alih.

![Hasil dari permintaan untuk menyelesaikan tujuan di Nexus menggunakan perencana dasar](Images/11-8.png)

Setelah beberapa menit, agen kembali dengan file yang disimpan, dan dalam beberapa kasus, agen mungkin memberikan informasi tambahan, seperti langkah selanjutnya dan apa yang harus dilakukan dengan output. Ini karena agen diberi gambaran umum tingkat tinggi tentang apa yang telah dicapainya. Namun, ingatlah bahwa eksekusi rencana dilakukan di tingkat lokal, dan hanya konteks, rencana, dan tujuan yang dikirim ke LLM.

Ini berarti bahwa eksekusi rencana dapat diselesaikan oleh proses apa pun, tidak harus oleh agen. Mengeksekusi rencana di luar LLM mengurangi token dan penggunaan alat yang perlu dilakukan agen. Ini juga berarti bahwa LLM tidak perlu mendukung penggunaan alat untuk menggunakan perencana.

Secara internal, ketika perencana diaktifkan di dalam Nexus, alat mesin agen dilewati. Sebaliknya, perencana menyelesaikan eksekusi tindakan, dan agen hanya mengetahui tindakan melalui pengiriman konteks output. Ini bisa baik untuk model yang mendukung penggunaan alat tetapi tidak dapat merencanakan. Namun, perencana dapat membatasi fungsionalitas untuk model yang mendukung penggunaan alat dan perencanaan, seperti Claude.

Secara umum, Anda akan ingin memahami kemampuan LLM yang Anda gunakan. Jika Anda tidak yakin dengan detail tersebut, maka sedikit coba-coba juga bisa berhasil. Minta agen untuk menyelesaikan tujuan multi-langkah dengan dan tanpa perencanaan diaktifkan, lalu lihat hasilnya.

Perencanaan memungkinkan agen untuk menyelesaikan beberapa tugas berurutan untuk mencapai tujuan yang lebih kompleks. Masalah dengan perencanaan eksternal atau *prompt* adalah ia melewati putaran iterasi umpan balik, yang dapat membantu memperbaiki masalah dengan cepat. Karena itu, OpenAI dan lainnya sekarang secara langsung mengintegrasikan penalaran dan perencanaan di tingkat LLM, seperti yang akan kita lihat di bagian selanjutnya.

## 11.4 Meninjau perencana bertahap: OpenAI Strawberry

Rilis model o1-preview, dengan nama kode Strawberry, memperkenalkan pergeseran dramatis dalam jenis LLM yang tersedia untuk sistem *agentic*. Strawberry tidak hanya dinyatakan lebih efisien dalam tugas matematika, sains, dan perhitungan umum, tetapi juga mampu terlibat dalam penalaran, perencanaan, evaluasi, dan umpan balik secara langsung di LLM.

Pertimbangkan masalah perjalanan waktu kita dari bab 10 dan ditunjukkan lagi pada gambar 11.9. Jika Anda ingat, masalah ini sulit dipecahkan menggunakan GPT-4 dan LLM serupa lainnya. Namun, dengan penerapan penalaran dan umpan balik, kami dapat menghasilkan output yang terkadang benar.

![Masalah perjalanan waktu, ditinjau kembali](Images/11-9.png)

Sebagai percobaan, masukkan masalah ini ke ChatGPT menggunakan model o1-preview, seperti yang ditunjukkan pada daftar 11.6. Duduk santai selama beberapa detik dan tunggu jawabannya. Ya, modelnya masih salah.

**Daftar 11.6** Masalah penalaran/perencanaan perjalanan waktu
```
Dalam sebuah film fiksi ilmiah, Alex adalah seorang penjelajah waktu yang memutuskan untuk kembali ke masa lalu
untuk menyaksikan pertempuran bersejarah terkenal yang terjadi 100 tahun yang lalu,
yang berlangsung selama 10 hari. Dia tiba tiga hari sebelum pertempuran dimulai.
Namun, setelah menghabiskan enam hari di masa lalu, dia melompat maju dalam waktu
sebanyak 50 tahun dan tinggal di sana selama 20 hari. Kemudian, dia melakukan perjalanan kembali ke
menyaksikan akhir pertempuran. Berapa hari yang dihabiskan Alex di masa lalu
sebelum dia melihat akhir pertempuran?
```

Meskipun mungkin agak mengecewakan melihat model mendapatkan jawaban yang salah, namun, ia melakukan pekerjaan yang jauh lebih baik dalam memecah masalah dan menunjukkan jawabannya. Daftar 11.7 menunjukkan contoh output dari mengajukan masalah dalam daftar 11.6 ke model Strawberry. Perhatikan, Anda mungkin mendapatkan jawaban yang berbeda karena sifat stokastik dari LLM.

**Daftar 11.7** Respons o1-preview terhadap masalah perjalanan waktu
```
Untuk menentukan berapa hari yang dihabiskan Alex di masa lalu sebelum menyaksikan
akhir pertempuran, mari kita rekonstruksi garis waktu langkah demi langkah:
Kedatangan di Masa Lalu:
Alex tiba 3 hari sebelum pertempuran dimulai.
Dia menghabiskan 3 hari ini menunggu pertempuran dimulai.
Selama Pertempuran:
Pertempuran dimulai, dan Alex mengalami 3 hari pertama pertempuran itu.
Pada titik ini, dia telah menghabiskan total 6 hari di masa lalu (3 hari sebelum
pertempuran dan 3 hari selama pertempuran).
Lompatan Waktu ke Depan: #1
Setelah 6 hari ini, Alex melompat 50 tahun ke depan dalam waktu.
Dia menghabiskan 20 hari di waktu mendatang ini.
Kembali ke Masa Lalu:
Alex kemudian kembali ke masa lalu untuk menyaksikan akhir pertempuran.
Karena pertempuran berlangsung 10 hari dan dia pergi setelah hari ke-3 pertempuran,
ada 7 hari tersisa dalam pertempuran.
Namun, karena dia pergi selama 20 hari, yang lebih lama dari
sisa 7 hari pertempuran, dia harus kembali ke suatu titik waktu sebelum
pertempuran berakhir untuk menyaksikan kesimpulannya.
Untuk melihat akhir pertempuran, dia kembali ke masa lalu pada hari terakhir
pertempuran.
Hari Terakhir yang Dihabiskan Sebelum Pertempuran Berakhir:
Setelah kembali, dia menghabiskan 1 hari lagi di masa lalu untuk menyaksikan pertempuran
berakhir.
Total Hari yang Dihabiskan di Masa Lalu Sebelum Melihat Akhir:
6 hari sebelum melompat maju dalam waktu.
1 hari setelah kembali ke masa lalu.
Total: 6 + 1 = 7 hari.
Jawaban: 7
```
#1 Menjadi jelas di mana model membuat kesalahan.

Karena kita tahu jawaban yang benar adalah 27, kita tahu LLM salah, tetapi jika kita tidak tahu, kita bisa dengan mudah berasumsi bahwa pekerjaan dan penalarannya semuanya benar. Masalah seperti ini dapat terjadi ketika kita menghapus umpan balik dalam interaksi LLM dan sistem *agentic*. Umpan balik dapat memandu model untuk mengoreksi dirinya sendiri.

Namun, bagaimana jika kita tidak tahu jawaban yang benar adalah 27 (26, jika Anda berasumsi dia tidak menghabiskan hari itu untuk menyaksikan pertempuran) dan berasumsi bahwa LLM atau agen itu benar? Nah, ini adalah masalah yang dapat kita perbaiki dengan beberapa *prompt* sederhana yang dapat melibatkan LLM dalam penalaran dan umpan balik perencanaan. Namun, teknik ini lebih efektif dengan LLM atau pembungkus seperti Asisten OpenAI, yang menyediakan penalaran dan perencanaan di dalam model.

Yang ingin kita lakukan adalah memberikan umpan balik kepada LLM, tetapi memahami umpan balik itu kemungkinan akan sulit bagi kita. Untungnya, kita dapat memperoleh umpan balik langsung dari LLM, asalkan kita memberikan jawaban yang benar. Daftar 11.8 menunjukkan cara menghasilkan umpan balik yang membangun dari LLM mengenai masalah perjalanan waktu kita.

**Daftar 11.8** Menghasilkan umpan balik
```
jawaban yang benar adalah 27, silakan tinjau apa yang Anda lakukan salah dan sarankan
umpan balik yang bisa Anda berikan pada diri sendiri saat mencoba menyelesaikan masalah serupa di masa depan
```

Memasukkan ini setelah model menjawab pertanyaan salah akan menghasilkan umpan balik yang dapat Anda gunakan untuk memandu model melalui *prompting* atau sebagai bagian dari instruksi sistem. Daftar 11.9 menunjukkan contoh umpan balik yang diberikan oleh o1-preview. Anda kemudian dapat mengekstrak umpan balik ini dan menambah instruksi pada saat berikutnya Anda ingin mengatasi masalah perjalanan waktu yang kompleks.

**Daftar 11.9** Umpan balik yang dihasilkan
```
Umpan Balik untuk Masalah di Masa Depan
Memahami Kerangka Waktu dalam Perjalanan Waktu:
Kerangka Waktu Relatif: Selalu pertimbangkan periode waktu relatif terhadap
titik acuan asli. Dalam masalah ini, meskipun Alex melompat
maju 50 tahun, dia masih di masa lalu relatif terhadap aslinya
waktu sekarang.
Termasuk Semua Periode yang Relevan:
Pastikan bahwa semua periode waktu yang dihabiskan di masa lalu (atau masa depan) disertakan
dalam perhitungan total, bahkan jika itu melibatkan perpindahan ke yang berbeda
titik waktu.
Kontinuitas Waktu:
Ingatlah bahwa saat penjelajah bergerak melalui waktu, peristiwa di lain waktu
periode terus berlanjut kecuali ditentukan lain.
Aplikasi:
Membaca dengan Cermat:
Perhatikan baik-baik detail yang diberikan, seperti durasi dan
urutan lompatan waktu.
Visualisasi:
Mungkin membantu untuk menggambar garis waktu untuk memvisualisasikan urutan peristiwa dan
periode waktu yang terlibat.
Memeriksa Ulang Perhitungan:
Setelah menyelesaikan, kunjungi kembali setiap langkah untuk memastikan semua periode waktu adalah
diperhitungkan dengan benar.
```

Teknik umpan balik ini akan secara konsisten bekerja pada model seperti o1-preview, tetapi model lain mungkin masih kesulitan untuk menjawab dengan benar, bahkan dengan umpan balik ini. Seiring waktu, seiring model menjadi lebih pintar, teknik ini kemungkinan akan berhasil secara umum pada sebagian besar model. Namun, mekanisme umpan balik ini kemungkinan akan menjadi penting bahkan ketika model menjadi semakin cerdas. karena bahasa itu bernuansa, dan tidak setiap masalah yang kita tantang pada LLM mungkin memiliki jawaban absolut yang jelas. Ambil contoh masalah kita, misalnya. Masalah ini adalah contoh yang sangat baik yang mengharuskan pemecah masalah untuk membuat asumsi dan menarik korelasi dari pertanyaan. Masih banyak bidang dalam sains, dari geologi hingga ilmu perilaku, di mana menjawab masalah yang sama dapat menghasilkan berbagai jawaban. Mari kita lihat selanjutnya beberapa teknik tentang bagaimana penerapan penalaran, perencanaan, evaluasi, dan umpan balik dapat diterapkan pada sistem *agentic*.

## 11.5 Menerapkan perencanaan, penalaran, evaluasi, dan umpan balik pada sistem asisten dan *agentic*

Dalam bab-bab terakhir, kita telah memeriksa bagaimana komponen *agentic* dari perencanaan, penalaran, umpan balik, dan evaluasi dapat diimplementasikan. Sekarang kita melihat bagaimana, kapan, dan di mana komponen-komponen tersebut dapat diintegrasikan ke dalam sistem asisten dan *agentic* untuk produksi, penelitian, atau pengembangan waktu nyata.

Meskipun tidak semua komponen ini mungkin cocok sama untuk setiap aplikasi, ada baiknya untuk memahami di mana dan kapan harus menerapkan komponen mana. Di bagian selanjutnya, kita melihat bagaimana perencanaan dapat diintegrasikan ke dalam sistem asisten/*agentic*.

### 11.5.1 Penerapan perencanaan asisten/*agentic*

Perencanaan adalah komponen di mana asisten atau agen dapat merencanakan untuk melakukan serangkaian tugas, baik secara seri, paralel, atau kombinasi lainnya. Kami biasanya mengaitkan perencanaan dengan penggunaan alat, dan, memang benar, sistem apa pun yang menggunakan alat kemungkinan besar akan menginginkan perencana yang mumpuni. Namun, tidak semua sistem dibuat sama, jadi pada tabel 11.1, kita akan meninjau di mana, kapan, dan bagaimana mengimplementasikan perencana.

**Tabel 11.1** Kapan dan di mana perencanaan digunakan dan digunakan dalam berbagai aplikasi

| Aplikasi | Diimplementasikan | Lingkungan | Tujuan | Waktu | Konfigurasi |
|---|---|---|---|---|---|
| Asisten pribadi | Pada atau di dalam LLM | Perangkat pribadi | Memfasilitasi penggunaan alat | Selama respons | Sebagai bagian dari *prompt* atau LLM |
| Bot layanan pelanggan | Tidak umum; lingkungan terbatas | Lingkungan terbatas, tidak ada penggunaan alat | | | |
| Agen otonom | Sebagai bagian dari *prompt* agen dan di dalam LLM | Server atau layanan | Memfasilitasi penggunaan alat yang kompleks dan perencanaan tugas | Sebagai bagian dari membangun agen dan/atau selama respons | Di dalam agen atau LLM |
| Alur kerja kolaboratif | Sebagai bagian dari LLM | Kanvas atau pengkodean bersama | Memfasilitasi penggunaan alat yang kompleks | Selama respons | Di dalam LLM |
| AI Game | Sebagai bagian dari LLM | Server atau aplikasi | Penggunaan dan perencanaan alat yang kompleks | Sebelum atau selama respons | Di dalam LLM |
| Penelitian | Di mana saja | Server | Memfasilitasi penggunaan alat dan terlibat dalam alur kerja tugas yang kompleks | Sebelum, selama, dan setelah pembuatan respons | Di mana saja |

Tabel 11.1 menunjukkan beberapa skenario aplikasi yang bervariasi di mana kita mungkin menemukan asisten atau agen yang digunakan untuk membantu dalam beberapa kapasitas. Untuk memberikan informasi dan panduan lebih lanjut, daftar ini memberikan detail lebih lanjut tentang bagaimana perencanaan dapat digunakan di setiap aplikasi:

- *Asisten pribadi*—Meskipun aplikasi ini lambat diluncurkan, asisten pribadi LLM berjanji untuk melampaui Alexa dan Siri di masa depan. Perencanaan akan menjadi penting bagi asisten/agen baru ini untuk mengoordinasikan banyak tugas kompleks dan mengeksekusi alat (tindakan) secara seri atau paralel.
- *Bot layanan pelanggan*—Karena sifat lingkungan yang terkontrol ini, tidak mungkin asisten yang terlibat langsung dengan pelanggan akan memiliki penggunaan alat yang terkontrol dan sangat spesifik. Ini berarti bahwa jenis asisten ini kemungkinan tidak akan memerlukan perencanaan yang ekstensif.
- *Agen otonom*—Seperti yang telah kita lihat di bab-bab sebelumnya, agen dengan kemampuan merencanakan dapat menyelesaikan serangkaian tugas kompleks untuk berbagai tujuan. Perencanaan akan menjadi elemen penting dari setiap sistem *agentic* otonom.
- *Alur kerja kolaboratif*—Anggap ini sebagai agen atau asisten yang duduk di samping pembuat kode atau penulis. Meskipun alur kerja ini masih dalam pengembangan awal, pikirkan alur kerja di mana agen secara otomatis ditugaskan untuk menulis dan mengeksekusi kode pengujian bersama pengembang. Perencanaan akan menjadi bagian penting dalam melaksanakan alur kerja masa depan yang kompleks ini.
- *AI Game*—Meskipun penerapan LLM pada game masih dalam tahap awal, tidak sulit membayangkan agen atau asisten dalam game yang dapat membantu atau menantang pemain. Memberi agen ini kemampuan untuk merencanakan dan melaksanakan alur kerja yang kompleks dapat mengganggu cara dan dengan siapa kita bermain game.
- *Penelitian*—Mirip dengan alur kerja kolaboratif, agen-agen ini akan bertanggung jawab untuk mendapatkan ide-ide baru dari sumber informasi yang ada. Menemukan informasi itu kemungkinan akan difasilitasi melalui penggunaan alat yang ekstensif, yang akan mendapat manfaat dari koordinasi perencanaan.

Seperti yang Anda lihat, perencanaan adalah bagian penting dari banyak aplikasi LLM, baik melalui koordinasi penggunaan alat atau lainnya. Di bagian selanjutnya, kita melihat komponen penalaran berikutnya dan bagaimana hal itu dapat diterapkan pada tumpukan aplikasi yang sama.

### 11.5.2 Penerapan penalaran asisten/*agentic*

Penalaran, meskipun sering sangat terkait dengan perencanaan dan penyelesaian tugas, adalah komponen yang juga dapat berdiri sendiri. Seiring LLM menjadi dewasa dan lebih pintar, penalaran sering kali disertakan di dalam LLM itu sendiri. Namun, tidak semua aplikasi dapat memperoleh manfaat dari penalaran yang ekstensif, karena sering kali memperkenalkan siklus berpikir dalam respons LLM. Tabel 11.2 menjelaskan secara umum bagaimana komponen penalaran dapat diintegrasikan dengan berbagai jenis aplikasi LLM.

**Tabel 11.2** Kapan dan di mana penalaran digunakan dan digunakan dalam berbagai aplikasi

| Aplikasi | Diimplementasikan | Lingkungan | Tujuan | Waktu | Konfigurasi |
|---|---|---|---|---|---|
| Asisten pribadi | Di dalam LLM | Perangkat pribadi | Memecah pekerjaan menjadi beberapa langkah | Selama respons | Sebagai bagian dari *prompt* atau LLM |
| Bot layanan pelanggan | Tidak umum; biasanya hanya informasional | Penggunaan alat terbatas dan kebutuhan akan penggunaan alat komposit | | | |
| Agen otonom | Sebagai bagian dari *prompt* agen dan di dalam LLM | Server atau layanan | Memfasilitasi penggunaan alat yang kompleks dan perencanaan tugas | Sebagai bagian dari LLM, penalaran eksternal tidak cocok | Di dalam agen atau LLM |
| Alur kerja kolaboratif | Sebagai bagian dari LLM | Kanvas atau pengkodean bersama | Membantu dalam memecah pekerjaan | Selama respons | Di dalam LLM |
| AI Game | Sebagai bagian dari LLM | Server atau aplikasi | Penting untuk melakukan tindakan kompleks | Sebelum atau selama respons | Di dalam LLM |
| Penelitian | Di mana saja | Server | Memahami cara menyelesaikan masalah kompleks dan terlibat dalam alur kerja tugas yang kompleks | Sebelum, selama, dan setelah pembuatan respons | Di mana saja |

Tabel 11.2 menunjukkan beberapa skenario aplikasi yang bervariasi di mana kita mungkin menemukan asisten atau agen yang digunakan untuk membantu dalam beberapa kapasitas. Untuk memberikan informasi dan panduan lebih lanjut, daftar ini memberikan detail lebih lanjut tentang bagaimana penalaran dapat digunakan di setiap aplikasi:

- *Asisten pribadi*—Tergantung pada aplikasinya, jumlah penalaran yang digunakan agen mungkin terbatas. Penalaran adalah proses yang mengharuskan LLM untuk memikirkan suatu masalah, dan ini sering kali membutuhkan waktu respons yang lebih lama tergantung pada kompleksitas masalah dan luasnya *prompt*. Dalam banyak situasi, respons yang dimaksudkan untuk mendekati penalaran waktu nyata dapat dinonaktifkan atau diturunkan. Meskipun ini dapat membatasi kompleksitas interaksi agen, penalaran yang terbatas atau tidak ada dapat meningkatkan waktu respons dan meningkatkan kenikmatan pengguna.
- *Bot layanan pelanggan*—Sekali lagi, karena sifat lingkungan yang terkontrol ini, tidak mungkin asisten yang terlibat langsung dengan pelanggan perlu melakukan penalaran yang kompleks atau dalam bentuk apa pun.
- *Agen otonom*—Meskipun penalaran adalah komponen kuat dari agen otonom, kita masih belum tahu seberapa banyak penalaran yang terlalu banyak. Seiring model seperti Strawberry tersedia untuk alur kerja *agentic*, kita dapat mengukur pada titik mana penalaran yang ekstensif mungkin tidak diperlukan. Ini pasti akan menjadi kasus untuk alur kerja agen otonom yang terdefinisi dengan baik.
- *Alur kerja kolaboratif*—Sekali lagi, menerapkan penalaran menciptakan overhead dalam interaksi LLM. Penalaran yang ekstensif dapat memberikan manfaat untuk beberapa alur kerja, sementara alur kerja lain yang terdefinisi dengan baik mungkin menderita. Ini mungkin berarti bahwa jenis alur kerja ini akan mendapat manfaat dari beberapa agen—yang memiliki penalaran dan yang tidak.
- *AI Game*—Mirip dengan aplikasi lain, aplikasi dengan penalaran berat mungkin tidak sesuai untuk sebagian besar AI game. Game terutama akan membutuhkan waktu respons LLM yang cepat, dan ini pasti akan menjadi penerapan penalaran untuk agen taktis umum. Tentu saja, itu tidak menghalangi penggunaan agen penalaran lain yang mungkin memberikan kontrol yang lebih strategis.
- *Penelitian*—Penalaran kemungkinan akan menjadi penting untuk setiap tugas penelitian yang kompleks karena beberapa alasan. Contoh yang baik adalah penerapan model Strawberry, yang telah kita lihat dalam penelitian yang dilakukan di bidang matematika dan sains.

Meskipun kita sering mempertimbangkan penalaran bersamaan dengan perencanaan, mungkin ada kondisi di mana tingkat implementasi masing-masing mungkin berbeda. Di bagian selanjutnya kita mempertimbangkan pilar agen evaluasi dari berbagai aplikasi.

### 11.5.3 Penerapan evaluasi pada sistem *agentic*

Evaluasi adalah komponen sistem *agentic*/asisten yang dapat memandu seberapa baik kinerja sistem. Meskipun kami mendemonstrasikan penggabungan evaluasi dalam beberapa alur kerja *agentic*, evaluasi sering kali merupakan komponen eksternal dalam sistem *agentic*. Namun, ini juga merupakan komponen inti dari sebagian besar aplikasi LLM dan bukan sesuatu yang harus diabaikan dalam sebagian besar pengembangan. Tabel 11.3 menjelaskan secara umum bagaimana komponen evaluasi dapat diintegrasikan dengan berbagai jenis aplikasi LLM.

**Tabel 11.3** Kapan dan di mana evaluasi digunakan dan digunakan dalam berbagai aplikasi

| Aplikasi | Diimplementasikan | Lingkungan | Tujuan | Waktu | Konfigurasi |
|---|---|---|---|---|---|
| Asisten pribadi | Eksternal | Server | Menentukan seberapa baik kinerja sistem | Setelah interaksi | Sering dikembangkan secara eksternal |
| Bot layanan pelanggan | Monitor eksternal | Server | Mengevaluasi keberhasilan setiap interaksi | Setelah interaksi | Eksternal ke sistem agen |
| Agen otonom | Eksternal atau internal | Server atau layanan | Menentukan keberhasilan sistem setelah atau selama penyelesaian tugas | Setelah interaksi | Eksternal atau internal |
| Alur kerja kolaboratif | Eksternal | Kanvas atau pengkodean bersama | Mengevaluasi keberhasilan kolaborasi | Setelah interaksi | Layanan eksternal |
| AI Game | Eksternal atau internal | Server atau aplikasi | Mengevaluasi agen atau mengevaluasi keberhasilan strategi atau tindakan | Setelah interaksi | Eksternal atau sebagai bagian dari agen atau agen lain |
| Penelitian | Gabungan manual dan LLM | Server dan manusia | Mengevaluasi output dari penelitian yang dikembangkan | Setelah output yang dihasilkan | Tergantung pada kompleksitas masalah dan penelitian yang dilakukan |

Tabel 11.3 menunjukkan beberapa skenario aplikasi yang bervariasi di mana kita mungkin menemukan asisten atau agen yang digunakan untuk membantu dalam beberapa kapasitas. Untuk memberikan informasi dan panduan lebih lanjut, daftar ini memberikan detail lebih lanjut tentang bagaimana evaluasi dapat digunakan di setiap aplikasi:

- *Asisten pribadi*—Dalam kebanyakan kasus, komponen evaluasi akan digunakan untuk memproses dan memandu kinerja respons agen. Dalam sistem yang terutama menggunakan *retrieval augmented generation* (RAG) untuk eksplorasi dokumen, evaluasi menunjukkan seberapa baik asisten merespons permintaan informasi.
- *Bot layanan pelanggan*—Mengevaluasi bot layanan sangat penting untuk memahami seberapa baik bot merespons permintaan pelanggan. Dalam banyak kasus, elemen pengetahuan RAG yang kuat mungkin menjadi elemen sistem yang akan memerlukan evaluasi yang ekstensif dan berkelanjutan. Sekali lagi, dengan sebagian besar komponen evaluasi, elemen ini berada di luar sistem kerja utama dan sering dijalankan sebagai bagian dari pemantauan kinerja umum pada beberapa metrik.
- *Agen otonom*—Dalam kebanyakan kasus, tinjauan manual output agen akan menjadi panduan utama keberhasilan agen otonom. Namun, dalam beberapa kasus, evaluasi internal dapat membantu memandu agen saat melakukan tugas-tugas kompleks atau sebagai sarana untuk meningkatkan output akhir. Beberapa sistem agen, seperti CrewAI dan AutoGen, adalah contoh agen otonom yang menggunakan umpan balik internal untuk meningkatkan output yang dihasilkan.
- *Alur kerja kolaboratif*—Dalam sebagian besar kasus langsung, evaluasi manual sedang berlangsung dalam jenis alur kerja ini. Pengguna akan sering segera dan dalam waktu dekat mengoreksi asisten/agen dengan mengevaluasi output. Agen tambahan dapat ditambahkan serupa dengan agen otonom untuk alur kerja kolaboratif yang lebih luas.
- *AI Game*—Evaluasi akan sering dipecah menjadi evaluasi pengembangan—mengevaluasi bagaimana agen berinteraksi dengan game—dan evaluasi dalam game, mengevaluasi seberapa baik agen berhasil dalam suatu tugas. Menerapkan bentuk evaluasi yang terakhir mirip dengan agen otonom tetapi bertujuan untuk meningkatkan beberapa strategi atau eksekusi. Evaluasi dalam game seperti itu juga kemungkinan akan mendapat manfaat dari memori dan sarana umpan balik.
- *Penelitian*—Evaluasi pada tingkat ini umumnya terjadi sebagai upaya manual setelah menyelesaikan tugas penelitian. Agen dapat menggunakan beberapa bentuk evaluasi yang mirip dengan agen otonom untuk meningkatkan output yang dihasilkan, bahkan mungkin merenungkan secara internal bagaimana evaluasi output dapat diperluas atau diteliti lebih lanjut. Karena ini saat ini merupakan area baru untuk pengembangan *agentic*, seberapa baik ini akan dieksekusi masih harus dilihat.

Evaluasi adalah elemen penting untuk setiap sistem *agentic* atau asisten, terutama jika sistem tersebut memberikan informasi nyata dan mendasar kepada pengguna. Mengembangkan sistem evaluasi untuk agen dan asisten kemungkinan merupakan sesuatu yang bisa atau seharusnya memiliki bukunya sendiri. Di bagian terakhir bab ini, kita akan melihat implementasi umpan balik untuk berbagai aplikasi LLM.

### 11.5.4 Penerapan umpan balik pada aplikasi *agentic*/asisten

Umpan balik sebagai komponen sistem *agentic* sering kali, jika tidak selalu, diimplementasikan sebagai komponen eksternal—setidaknya untuk saat ini. Mungkin kepercayaan pada sistem evaluasi dapat meningkat ke titik di mana umpan balik secara teratur dimasukkan ke dalam sistem tersebut. Tabel 11.4 menunjukkan bagaimana umpan balik dapat diimplementasikan ke dalam berbagai aplikasi LLM.

**Tabel 11.4** Kapan dan di mana umpan balik digunakan dan digunakan dalam berbagai aplikasi

| Aplikasi | Diimplementasikan | Lingkungan | Tujuan | Waktu | Konfigurasi |
|---|---|---|---|---|---|
| Asisten pribadi | Eksternal atau oleh pengguna | Diagregasi ke server atau sebagai bagian dari sistem | Menyediakan sarana perbaikan sistem | Setelah atau selama interaksi | Internal dan eksternal |
| Bot layanan pelanggan | Monitor eksternal | Diagregasi ke server | Mengkualifikasi dan menyediakan sarana untuk perbaikan sistem | Setelah interaksi | Eksternal ke sistem agen |
| Agen otonom | Eksternal | Diagregasi di server | Menyediakan sarana untuk perbaikan sistem | Setelah interaksi | Eksternal |
| Alur kerja kolaboratif | Saat berinteraksi | Kanvas atau pengkodean bersama | Menyediakan mekanisme untuk umpan balik langsung | Selama interaksi | Layanan eksternal |
| AI Game | Eksternal atau internal | Server atau aplikasi | Sebagai bagian dari umpan balik evaluasi internal yang diberikan untuk peningkatan dinamis | Setelah atau selama interaksi | Eksternal atau sebagai bagian dari agen atau agen lain |
| Penelitian | Gabungan manual dan LLM | Server dan manusia | Mengevaluasi output dari penelitian yang dikembangkan | Setelah output yang dihasilkan | Tergantung pada kompleksitas masalah dan penelitian yang dilakukan |

Tabel 11.4 menunjukkan beberapa skenario aplikasi di mana kita mungkin menemukan asisten atau agen yang digunakan untuk membantu dalam beberapa kapasitas. Untuk memberikan informasi dan panduan lebih lanjut, daftar ini memberikan detail lebih lanjut tentang bagaimana umpan balik dapat digunakan di setiap aplikasi:

- *Asisten pribadi*—Jika asisten atau agen berinteraksi dengan pengguna dalam antarmuka gaya obrolan, umpan balik langsung dan segera dapat diterapkan oleh pengguna. Apakah umpan balik ini dipertahankan selama percakapan atau interaksi di masa depan, biasanya berkembang dalam memori *agentic*. Asisten seperti ChatGPT sekarang menggabungkan memori dan dapat memperoleh manfaat dari umpan balik pengguna yang eksplisit.
- *Bot layanan pelanggan*—Umpan balik pengguna atau sistem biasanya diberikan melalui survei setelah interaksi selesai. Ini biasanya berarti bahwa umpan balik diatur ke sistem eksternal yang mengagregasi umpan balik untuk perbaikan di kemudian hari.
- *Agen otonom*—Sama seperti bot, umpan balik dalam agen otonom biasanya diatur setelah agen menyelesaikan tugas yang kemudian ditinjau oleh pengguna. Mekanisme umpan balik mungkin lebih sulit ditangkap karena banyak hal bisa bersifat subjektif. Metode yang dieksplorasi dalam bab ini untuk menghasilkan umpan balik dapat digunakan dalam perbaikan rekayasa *prompt*.
- *Alur kerja kolaboratif*—Mirip dengan asisten pribadi, jenis aplikasi ini dapat memperoleh manfaat dari umpan balik langsung dan langsung dari pengguna. Sekali lagi, bagaimana informasi ini dipertahankan di seluruh sesi sering kali merupakan implementasi dari memori *agentic*.
- *AI Game*—Umpan balik dapat diimplementasikan bersama evaluasi melalui agen tambahan dan ganda. Bentuk umpan balik ini mungkin sekali lagi sekali pakai dan ada dalam interaksi saat ini atau mungkin bertahan sebagai memori. Bayangkan sebuah AI game yang dapat mengevaluasi tindakannya, memperbaikinya dengan umpan balik, dan mengingat perbaikan tersebut. Meskipun pola ini tidak ideal untuk game, ini pasti akan meningkatkan pengalaman bermain game.
- *Penelitian*—Mirip dengan evaluasi dalam konteks penelitian, umpan balik biasanya dilakukan secara offline setelah output dievaluasi. Meskipun beberapa pengembangan telah dilakukan menggunakan beberapa sistem agen yang menggabungkan agen untuk evaluasi dan umpan balik, sistem ini tidak selalu berkinerja baik, setidaknya tidak dengan model canggih saat ini. Sebaliknya, seringkali lebih baik untuk mengisolasi umpan balik dan evaluasi di akhir untuk menghindari masalah perulangan umpan balik yang umum.

Umpan balik adalah komponen kuat lain dari sistem *agentic* dan asisten, tetapi tidak selalu diperlukan pada rilis pertama. Namun, memasukkan mekanisme umpan balik dan evaluasi yang ketat dapat sangat bermanfaat bagi sistem *agentic* dalam jangka panjang terkait pemantauan berkelanjutan dan memberikan kepercayaan diri untuk meningkatkan berbagai aspek sistem.

Bagaimana Anda mengimplementasikan setiap komponen ini dalam sistem *agentic* Anda mungkin, sebagian, dipandu oleh arsitektur platform *agentic* pilihan Anda. Sekarang setelah Anda memahami nuansa setiap komponen, Anda juga memiliki pengetahuan untuk memandu Anda dalam memilih sistem agen yang tepat yang sesuai dengan aplikasi dan kasus penggunaan bisnis Anda. Terlepas dari aplikasi Anda, Anda akan ingin menggunakan beberapa komponen *agentic* di hampir semua kasus.

Seiring sistem *agentic* menjadi dewasa dan LLM itu sendiri menjadi lebih pintar, beberapa komponen yang saat ini kita anggap eksternal mungkin terintegrasi erat. Kita telah melihat penalaran dan perencanaan diintegrasikan ke dalam model seperti Strawberry. Tentu saja, saat kita mendekati tonggak kecerdasan umum buatan teoretis, kita mungkin melihat model yang mampu melakukan evaluasi diri dan umpan balik jangka panjang.

Bagaimanapun, saya harap Anda menikmati perjalanan ini bersama saya ke perbatasan luar biasa dari teknologi baru dan yang sedang berkembang ini yang pasti akan mengubah persepsi kita tentang pekerjaan dan bagaimana kita melakukannya melalui agen.

## 11.6 Latihan

Gunakan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- *Latihan 1*—Menerapkan Agen Perencanaan Sederhana (Pemula)

  *Tujuan*—Pelajari cara mengimplementasikan agen perencanaan dasar menggunakan *prompt* untuk menghasilkan urutan tindakan.

  *Tugas:*

  - Buat agen yang menerima tujuan, memecahnya menjadi beberapa langkah, dan melaksanakan langkah-langkah tersebut secara berurutan.
  - Tentukan tujuan sederhana, seperti mengambil informasi dari Wikipedia dan menyimpannya ke file.
  - Terapkan agen menggunakan *prompt* perencana dasar (lihat contoh perencana di bagian 11.3).
  - Jalankan agen, dan evaluasi seberapa baik ia merencanakan dan melaksanakan setiap langkah.

- *Latihan 2*—Uji Integrasi Umpan Balik dalam Agen Perencanaan (Menengah)

  *Tujuan*—Pahami bagaimana mekanisme umpan balik dapat meningkatkan kinerja sistem *agentic*.

  *Tugas:*

  - Ubah agen dari latihan 1 untuk menyertakan putaran umpan balik setelah setiap tugas.
  - Gunakan umpan balik untuk menyesuaikan atau mengoreksi tugas berikutnya dalam urutan.
  - Uji agen dengan memberinya tugas yang lebih kompleks, seperti mengumpulkan data dari berbagai sumber, dan amati bagaimana umpan balik meningkatkan kinerjanya.
  - Dokumentasikan dan bandingkan perilaku agen sebelum dan sesudah menambahkan umpan balik.

- *Latihan 3*—Eksperimen dengan Perencanaan Paralel dan Berurutan (Menengah)

  *Tujuan*—Pelajari perbedaan antara tindakan paralel dan berurutan dan bagaimana pengaruhnya terhadap perilaku agen.

  *Tugas:*

  - Siapkan dua agen menggunakan Nexus: satu yang mengeksekusi tugas secara paralel dan satu lagi yang melakukan tugas secara berurutan.
  - Tentukan tujuan multi-langkah di mana beberapa tindakan bergantung pada hasil tindakan sebelumnya (berurutan), dan beberapa dapat dilakukan secara bersamaan (paralel).
  - Bandingkan kinerja dan output kedua agen, catat setiap kesalahan atau inefisiensi dalam eksekusi paralel ketika langkah-langkah berurutan diperlukan.

- *Latihan 4*—Bangun dan Integrasikan Perencana Kustom ke dalam Nexus (Lanjutan)

  *Tujuan*—Pelajari cara membangun perencana kustom dan mengintegrasikannya ke dalam platform agen.

  *Tugas:*

  - Tulis perencana kustom menggunakan strategi rekayasa *prompt* dari bagian 11.3, pastikan ia mendukung eksekusi tugas berurutan.
  - Integrasikan perencana ini ke dalam Nexus, dan buat agen yang menggunakannya.
  - Uji perencana dengan tujuan kompleks yang melibatkan beberapa langkah dan alat (misalnya, pengambilan, pemrosesan, dan penyimpanan data).
  - Evaluasi bagaimana kinerja perencana kustom dibandingkan dengan perencana bawaan di Nexus atau platform lain.

- *Latihan 5*—Menerapkan Penanganan Kesalahan dan Umpan Balik dalam Perencanaan Berurutan (Lanjutan)

  *Tujuan*—Pelajari cara menerapkan penanganan kesalahan dan umpan balik untuk menyempurnakan perencanaan berurutan dalam sistem *agentic*.

  *Tugas:*

  - Dengan menggunakan perencana berurutan, siapkan agen untuk melakukan tujuan yang mungkin mengalami kesalahan umum (misalnya, panggilan API yang gagal, data yang hilang, atau input yang tidak valid).
  - Terapkan mekanisme penanganan kesalahan di perencana untuk mengenali dan menanggapi kesalahan ini.
  - Tambahkan putaran umpan balik untuk menyesuaikan rencana atau mencoba kembali tindakan berdasarkan kesalahan yang dihadapi.
  - Uji sistem dengan sengaja menyebabkan kesalahan selama eksekusi, dan amati bagaimana agen pulih atau menyesuaikan rencananya.

## Ringkasan

- Perencanaan adalah pusat bagi agen dan asisten, memungkinkan mereka untuk mengambil tujuan, memecahnya menjadi beberapa langkah, dan melaksanakannya. Tanpa perencanaan, agen direduksi menjadi interaksi seperti *chatbot* sederhana.
- Agen harus membedakan antara tindakan paralel dan berurutan. Banyak LLM dapat menangani tindakan paralel, tetapi hanya model canggih yang mendukung perencanaan berurutan, yang penting untuk penyelesaian tugas yang kompleks.
- Umpan balik sangat penting dalam memandu agen untuk mengoreksi arah mereka dan meningkatkan kinerja dari waktu ke waktu. Bab ini menunjukkan bagaimana mekanisme umpan balik dapat diintegrasikan dengan agen untuk menyempurnakan proses pengambilan keputusan mereka.
- Platform seperti Asisten OpenAI dan Claude dari Anthropic mendukung perencanaan internal dan dapat melaksanakan tugas multi-langkah yang kompleks. Agen yang menggunakan platform ini dapat menggunakan perencanaan tindakan berurutan untuk alur kerja yang canggih.
- Memilih dan membatasi tindakan agen dengan benar sangat penting untuk menghindari kebingungan dan perilaku yang tidak diinginkan. Terlalu banyak tindakan dapat membanjiri agen, sementara alat yang tidak perlu dapat disalahgunakan.
- Nexus memungkinkan pembuatan dan pengelolaan agen melalui antarmuka yang fleksibel, di mana pengguna dapat mengimplementasikan perencana kustom, menetapkan tujuan, dan menetapkan alat. Bab ini mencakup contoh-contoh praktis menggunakan Nexus untuk menyoroti perbedaan antara LLM mentah dan agen yang disempurnakan dengan perencana.
- Menulis perencana kustom itu mudah, menggunakan strategi rekayasa *prompt*. Alat seperti LangChain dan Semantic Kernel menawarkan berbagai perencana yang dapat diadaptasi atau diperluas agar sesuai dengan kebutuhan *agentic* tertentu.
- Model seperti OpenAI Strawberry mengintegrasikan penalaran, perencanaan, evaluasi, dan umpan balik secara langsung ke dalam LLM, menawarkan kemampuan pemecahan masalah yang lebih akurat.
- Evaluasi membantu menentukan seberapa baik kinerja sistem *agentic* dan dapat diimplementasikan secara internal atau eksternal, tergantung pada kasus penggunaan.
- Seiring berkembangnya LLM, mekanisme penalaran, perencanaan, dan umpan balik dapat menjadi sangat terintegrasi ke dalam model, membuka jalan bagi sistem agen yang lebih otonom dan cerdas.
