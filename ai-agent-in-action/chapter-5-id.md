# 5 Memberdayakan agen dengan tindakan

## Bab ini mencakup

- Bagaimana agen bertindak di luar dirinya menggunakan tindakan
- Mendefinisikan dan menggunakan fungsi OpenAI
- Kernel Semantik dan cara menggunakan fungsi semantik
- Mensinergikan fungsi semantik dan asli
- Membuat antarmuka GPT dengan Kernel Semantik

Dalam bab ini, kita menjelajahi tindakan melalui penggunaan fungsi dan bagaimana agen juga dapat menggunakannya. Kita akan mulai dengan melihat pemanggilan fungsi OpenAI dan kemudian dengan cepat beralih ke proyek lain dari Microsoft yang disebut Semantic Kernel (SK), yang akan kita gunakan untuk membangun dan mengelola keterampilan dan fungsi untuk agen atau sebagai agen.

Kita akan menyelesaikan bab ini menggunakan SK untuk menghosting sistem agen pertama kita. Ini akan menjadi bab yang lengkap dengan banyak contoh kode beranotasi.

## 5.1 Mendefinisikan tindakan agen

Plugin ChatGPT pertama kali diperkenalkan untuk menyediakan sesi dengan kemampuan, keterampilan, atau alat. Dengan plugin, Anda dapat mencari di web atau membuat spreadsheet atau grafik. Plugin menyediakan ChatGPT sarana untuk memperluas platform.

Gambar 5.1 menunjukkan cara kerja plugin ChatGPT. Dalam contoh ini, plugin pemberi rekomendasi film baru telah diinstal di ChatGPT. Ketika pengguna meminta ChatGPT untuk merekomendasikan film baru, model bahasa besar (LLM) mengenali bahwa ia memiliki plugin untuk mengelola tindakan itu. Kemudian ia memecah permintaan pengguna menjadi parameter yang dapat ditindaklanjuti, yang diteruskannya ke pemberi rekomendasi film baru.

![gambar](Images/5-1.png)

**Gambar 5.1** Bagaimana plugin ChatGPT beroperasi dan bagaimana plugin dan alat eksternal lainnya (misalnya, API) selaras dengan strategi rekayasa prompt Gunakan Alat Eksternal

Pemberi rekomendasi kemudian mengikis situs web yang menampilkan film-film baru dan menambahkan informasi itu ke permintaan prompt baru ke LLM. Dengan informasi ini, LLM merespons pemberi rekomendasi, yang meneruskannya kembali ke ChatGPT. ChatGPT kemudian merespons pengguna dengan permintaan yang direkomendasikan.

Kita dapat menganggap plugin sebagai proksi untuk tindakan. Plugin umumnya merangkum satu atau lebih kemampuan, seperti memanggil API atau mengikis situs web. Oleh karena itu, tindakan adalah ekstensi dari plugin—mereka memberikan kemampuan pada plugin.

Agen AI dapat dianggap sebagai plugin dan konsumen plugin, alat, keterampilan, dan agen lain. Menambahkan keterampilan, fungsi, dan alat ke agen/plugin memungkinkannya untuk menjalankan tindakan yang terdefinisi dengan baik—gambar 5.2 menyoroti di mana tindakan agen terjadi dan interaksinya dengan LLM dan sistem lain.

![gambar](Images/5-2.png)

**Gambar 5.2** Bagaimana agen menggunakan tindakan untuk melakukan tugas eksternal

Tindakan agen adalah kemampuan yang memungkinkannya menggunakan fungsi, keterampilan, atau alat. Yang membingungkan adalah kerangka kerja yang berbeda menggunakan terminologi yang berbeda. Kami akan mendefinisikan tindakan sebagai apa pun yang dapat dilakukan agen untuk menetapkan beberapa definisi dasar.

Plugin dan fungsi ChatGPT mewakili kemampuan yang dapat ditindaklanjuti yang dapat digunakan oleh ChatGPT atau sistem agen untuk melakukan tindakan tambahan. Sekarang mari kita periksa dasar untuk plugin OpenAI dan definisi fungsi.

## 5.2 Menjalankan fungsi OpenAI

OpenAI, dengan pengaktifan plugin, memperkenalkan spesifikasi struktur untuk mendefinisikan antarmuka antara fungsi/plugin yang dapat ditindaklanjuti oleh LLM. Spesifikasi ini menjadi standar yang dapat diikuti oleh sistem LLM untuk menyediakan sistem yang dapat ditindaklanjuti.

Definisi fungsi yang sama ini sekarang juga digunakan untuk mendefinisikan plugin untuk ChatGPT dan sistem lain. Selanjutnya, kita akan menjelajahi cara menggunakan fungsi secara langsung dengan panggilan LLM.

### 5.2.1 Menambahkan fungsi ke panggilan API LLM

Gambar 5.3 menunjukkan bagaimana LLM mengenali dan menggunakan definisi fungsi untuk mentransmisikan responsnya sebagai panggilan fungsi.

![gambar](Images/5-3.png)

**Gambar 5.3** Bagaimana satu permintaan LLM, termasuk alat, ditafsirkan oleh LLM

Daftar 5.1 menunjukkan detail panggilan API LLM menggunakan alat dan definisi fungsi. Menambahkan definisi fungsi memungkinkan LLM untuk membalas mengenai parameter input fungsi. Ini berarti LLM akan mengidentifikasi fungsi yang benar dan mengurai parameter yang relevan untuk permintaan pengguna.

**Daftar 5.1** `first_function.py` (panggilan API)

```python
response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[{"role": "system",
               "content": "You are a helpful assistant."},
              {"role": "user", "content": user_message}],
    temperature=0.7,
    tools=[
        {
            "type": "function",
            "function": {
                "name": "recommend",
                "description": "Provide a … topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {
                            "type": "string",
                            "description": 
                               "The topic,… for.",
                        },
                        "rating": {
                            "type": "string",
                            "description": 
                      "The rating … given.",
                            "enum": ["good",
                                     "bad", 
                                     "terrible"]
                            },
                    },
                    "required": ["topic"],
                },
            },
            }
        ]
    )
```

#1 Parameter baru bernama tools
#2 Mengatur jenis alat ke fungsi
#3 Memberikan deskripsi yang sangat baik tentang apa yang dilakukan fungsi
#4 Mendefinisikan jenis parameter untuk input; objek mewakili dokumen JSON.
#5 Deskripsi yang sangat baik untuk setiap parameter input
#6 Anda bahkan dapat mendeskripsikan dalam hal enumerasi.


Untuk melihat cara kerjanya, buka Visual Studio Code (VS Code) ke folder kode sumber buku: `chapter_4/first_function.py`. Merupakan praktik yang baik untuk membuka folder bab yang relevan di VS Code untuk membuat lingkungan Python baru dan menginstal file `requirements.txt`. Jika Anda memerlukan bantuan untuk ini, lihat apendiks B.

Sebelum memulai, siapkan file `.env` dengan benar di folder `chapter_4` dengan kredensial API Anda. Pemanggilan fungsi adalah kemampuan tambahan yang disediakan oleh layanan komersial LLM. Pada saat penulisan, fitur ini bukan pilihan untuk penerapan LLM sumber terbuka.

Selanjutnya, kita akan melihat bagian bawah kode di `first_function.py,` seperti yang ditunjukkan pada daftar 5.2. Berikut adalah dua contoh panggilan yang dibuat ke LLM menggunakan permintaan yang ditentukan sebelumnya di daftar 5.1. Di sini, setiap permintaan menunjukkan output yang dihasilkan dari menjalankan contoh.

**Daftar 5.2** `first_function.py` (melatih API)

```python
pengguna = "Bisakah Anda merekomendasikan saya film perjalanan waktu?"
respons = ask_chatgpt(pengguna)    #1
print(respons)

###Keluaran
Fungsi(argumen='{"topik":"film perjalanan waktu"}', 
                       nama='rekomendasikan')    #2

pengguna = "Bisakah Anda merekomendasikan saya film perjalanan waktu yang bagus?"
respons = ask_chatgpt(pengguna)    #3
print(respons)

###Keluaran
Fungsi(argumen='{"topik":"film perjalanan waktu",
                     "peringkat":"bagus"}',
 nama='rekomendasikan')    #4
```

#1 Fungsi yang ditentukan sebelumnya
#2 Dikembalikan atas nama fungsi yang akan dipanggil dan parameter input yang diekstraksi
#3 Fungsi yang ditentukan sebelumnya
#4 Dikembalikan atas nama fungsi yang akan dipanggil dan parameter input yang diekstraksi


Jalankan skrip Python `first_function.py` di VS Code menggunakan debugger (F5) atau terminal untuk melihat hasil yang sama. Di sini, LLM mengurai permintaan input untuk mencocokkan alat terdaftar apa pun. Dalam hal ini, alatnya adalah definisi fungsi tunggal, yaitu fungsi yang direkomendasikan. LLM mengekstrak parameter input dari fungsi ini dan mengurainya dari permintaan. Kemudian, ia membalas dengan fungsi bernama dan parameter input yang ditunjuk.

> **CATATAN** Fungsi sebenarnya tidak dipanggil. LLM hanya mengembalikan fungsi yang disarankan dan parameter input yang relevan. Nama dan parameter harus diekstraksi dan diteruskan ke fungsi yang cocok dengan tanda tangan untuk menindaklanjuti fungsi tersebut. Kita akan melihat contohnya di bagian selanjutnya.

### 5.2.2 Menindaklanjuti panggilan fungsi

Sekarang setelah kita memahami bahwa LLM tidak menjalankan fungsi atau plugin secara langsung, kita dapat melihat contoh yang menjalankan alat. Tetap dengan tema pemberi rekomendasi, kita akan melihat contoh lain yang menambahkan fungsi Python untuk rekomendasi sederhana.

Gambar 5.4 menunjukkan bagaimana contoh sederhana ini akan bekerja. Kami akan mengirimkan satu permintaan yang menyertakan definisi fungsi alat, meminta tiga rekomendasi. LLM, pada gilirannya, akan membalas dengan tiga panggilan fungsi dengan parameter input (perjalanan waktu, resep, dan hadiah). Hasil dari eksekusi fungsi kemudian diteruskan kembali ke LLM, yang mengubahnya kembali menjadi bahasa alami dan mengembalikan balasan.

![gambar](Images/5-4.png)

**Gambar 5.4** Permintaan sampel mengembalikan tiga panggilan fungsi alat dan kemudian mengirimkan hasilnya kembali ke LLM untuk mengembalikan respons bahasa alami.

Sekarang setelah kita memahami contohnya, buka `parallel_functions.py` di VS Code. Daftar 5.3 menunjukkan fungsi Python yang ingin Anda panggil untuk memberikan rekomendasi.

**Daftar 5.3** `parallel_functions.py` (fungsi rekomendasi)

```python
def recommend(topic, rating="good"):
    if "time travel" in topic.lower():    #1
        return json.dumps({"topic": "time travel",
                           "recommendation": "Back to the Future",
                           "rating": rating})
    elif "recipe" in topic.lower():    #1
        return json.dumps({"topic": "recipe",
                           "recommendation": "The best thing … ate.",
                           "rating": rating})
    elif "gift" in topic.lower():      #1
        return json.dumps({"topic": "gift",
                           "recommendation": "A glorious new...",
                           "rating": rating})
    else:    #2
        return json.dumps({"topic": topic,
                           "recommendation": "unknown"})    #3
```

#1 Memeriksa apakah string terkandung dalam input topik
#2 Jika tidak ada topik yang terdeteksi, kembalikan default
#3 Mengembalikan objek JSON


Selanjutnya, kita akan melihat fungsi yang disebut `run_conversation`, di mana semua pekerjaan dimulai dengan konstruksi permintaan.

**Daftar 5.4** `parallel_functions.py` (`run_conversation`, `request`)

```python
pengguna = """Bisakah Anda memberikan rekomendasi untuk hal-hal berikut:
1. Film perjalanan waktu
2. Resep
3. Hadiah"""    #1
pesan = [{"role": "user", "content": user}]    #2
alat = [    #3
    {
        "type": "function",
        "function": {
            "name": "recommend",
            "description": 
                "Berikan rekomendasi untuk topik apa pun.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": 
                              "Topik, … rekomendasi untuk.",
                        },
                        "rating": {
                            "type": "string",
                            "description": "Peringkat … diberikan.",
                            "enum": ["baik", "buruk", "mengerikan"]
                            },
                        },
                "required": ["topic"],
                },
            },
        }
    ]
```

#1 Pesan pengguna meminta tiga rekomendasi.
#2 Perhatikan bahwa tidak ada pesan sistem.
#3 Menambahkan definisi fungsi ke bagian alat dari permintaan


Daftar 5.5 menunjukkan permintaan yang dibuat, yang telah kita bahas sebelumnya, tetapi ada beberapa hal yang perlu diperhatikan. Panggilan ini menggunakan model yang lebih rendah seperti GPT-3.5 karena mendelegasikan fungsi adalah tugas yang lebih mudah dan dapat dilakukan menggunakan model bahasa yang lebih tua, lebih murah, dan kurang canggih.

**Daftar 5.5** `parallel_functions.py` (`run_conversation`, panggilan API)

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",    #1
    messages=messages,    #2
    tools=tools,     #2
    tool_choice="auto",  #3
)
response_message = response.choices[0].message    #4
```

#1 LLM yang mendelegasikan ke fungsi dapat menjadi model yang lebih sederhana.
#2 Menambahkan pesan dan definisi alat
#3 otomatis adalah default.
#4 Pesan yang dikembalikan dari LLM


Pada titik ini, setelah panggilan API, respons harus menyimpan informasi untuk panggilan fungsi yang diperlukan. Ingat, kami meminta LLM untuk memberi kami tiga rekomendasi, yang berarti ia juga harus memberi kami tiga output panggilan fungsi, seperti yang ditunjukkan pada daftar berikut.

**Daftar 5.6** `parallel_functions.py` (`run_conversation`, `tool_calls`)

```python
tool_calls = response_message.tool_calls    #1
if tool_calls:    #1
    available_functions = {
        "recommend": recommend,
    }
    # Langkah 4: kirim info untuk setiap panggilan fungsi dan respons fungsi ke 
# model
    for tool_call in tool_calls:    #3
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(
            topic=function_args.get("topic"),    #4
            rating=function_args.get("rating"),
        )
        messages.append(    #5
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            }
        )  # perluas percakapan dengan respons fungsi
    second_response = client.chat.completions.create(    #6
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    return second_response.choices[0].message.content  #6
```

#1 Jika respons berisi panggilan alat, jalankan.
#2 Hanya satu fungsi tetapi bisa berisi beberapa
#3 Melakukan loop melalui panggilan dan memutar ulang konten kembali ke LLM
#4 Menjalankan fungsi rekomendasi dari parameter yang diekstraksi
#5 Menambahkan hasil dari setiap panggilan fungsi ke kumpulan pesan
#6 Mengirim permintaan lain ke LLM dengan informasi yang diperbarui dan mengembalikan balasan pesan


Output panggilan alat dan panggilan ke hasil fungsi pemberi rekomendasi ditambahkan ke pesan. Perhatikan bagaimana pesan sekarang juga berisi riwayat panggilan pertama. Ini kemudian diteruskan kembali ke LLM untuk membuat balasan dalam bahasa alami.

Debug contoh ini di VS Code dengan menekan tombol F5 dengan file terbuka. Daftar berikut menunjukkan output dari menjalankan `parallel_functions.py`.

**Daftar 5.7** `parallel_functions.py` (output)

```python
Berikut adalah beberapa rekomendasi untuk Anda:

1. Film perjalanan waktu: "Back to the Future"
2. Resep: "Hal terbaik yang pernah Anda makan."
3. Hadiah: "Sesuatu yang baru yang mulia..." (rekomendasi terpotong, jadi saya 
tidak dapat memberikan rekomendasi lengkap)

Saya harap Anda menemukan rekomendasi ini bermanfaat! Beri tahu saya jika Anda membutuhkan 
informasi lebih lanjut.
```


Ini melengkapi demonstrasi sederhana ini. Untuk aplikasi yang lebih canggih, fungsi dapat melakukan sejumlah hal, mulai dari mengikis situs web hingga memanggil mesin pencari untuk menyelesaikan tugas yang jauh lebih kompleks.

Fungsi adalah cara terbaik untuk mentransmisikan output untuk tugas tertentu. Namun, pekerjaan menangani fungsi atau alat dan melakukan panggilan sekunder dapat dilakukan dengan cara yang lebih bersih dan lebih efisien. Bagian berikut akan mengungkap sistem yang lebih kuat untuk menambahkan tindakan ke agen.

## 5.3 Memperkenalkan Kernel Semantik

Semantic Kernel (SK) adalah proyek sumber terbuka lain dari Microsoft yang dimaksudkan untuk membantu membangun aplikasi AI, yang kami sebut agen. Pada intinya, proyek ini paling baik digunakan untuk mendefinisikan tindakan, atau apa yang disebut platform sebagai *plugin semantik*, yang merupakan pembungkus untuk keterampilan dan fungsi.

Gambar 5.5 menunjukkan bagaimana SK dapat digunakan sebagai plugin dan konsumen plugin OpenAI. SK mengandalkan definisi plugin OpenAI untuk mendefinisikan plugin. Dengan begitu, ia dapat mengonsumsi dan menerbitkan dirinya sendiri atau plugin lain ke sistem lain.

![gambar](Images/5-5.png)

**Gambar 5.5** Bagaimana Kernel Semantik terintegrasi sebagai plugin dan juga dapat mengonsumsi plugin

Definisi plugin OpenAI memetakan secara tepat ke definisi fungsi di daftar 5.4. Ini berarti bahwa SK adalah orkestrator panggilan alat API, alias plugin. Itu juga berarti bahwa SK dapat membantu mengatur beberapa plugin dengan antarmuka obrolan atau agen.

> Tim di SK awalnya melabeli modul fungsional sebagai *keterampilan.* Namun, agar lebih konsisten dengan OpenAI, mereka telah mengganti nama *keterampilan* menjadi *plugin.* Yang lebih membingungkan adalah kode tersebut masih menggunakan istilah *keterampilan.* Oleh karena itu, di seluruh bab ini, kita akan menggunakan *keterampilan* dan *plugin* untuk mengartikan hal yang sama.

SK adalah alat yang berguna untuk mengelola beberapa plugin (tindakan untuk agen) dan, seperti yang akan kita lihat nanti, juga dapat membantu dengan alat memori dan perencanaan. Untuk bab ini, kita akan fokus pada tindakan/plugin. Di bagian selanjutnya, kita akan melihat cara memulai menggunakan SK.

### 5.3.1 Memulai dengan fungsi semantik SK

SK mudah dipasang dan berfungsi di Python, Java, dan C#. Ini adalah berita bagus karena juga memungkinkan plugin yang dikembangkan dalam satu bahasa untuk dikonsumsi dalam bahasa yang berbeda. Namun, Anda belum dapat mengembangkan fungsi asli dalam satu bahasa dan menggunakannya di bahasa lain.

Kami akan melanjutkan dari tempat kami tinggalkan untuk lingkungan Python menggunakan ruang kerja `chapter_4` di VS Code. Pastikan Anda memiliki ruang kerja yang dikonfigurasi jika Anda ingin menjelajahi dan menjalankan contoh apa pun.

Daftar 5.8 menunjukkan cara menginstal SK dari terminal di dalam VS Code. Anda juga dapat menginstal ekstensi SK untuk VS Code. Ekstensi dapat menjadi alat yang membantu untuk membuat plugin/keterampilan, tetapi tidak diperlukan.

**Daftar 5.8** Menginstal Kernel Semantik 

```bash
pip uninstall semantic-kernel    #1

git clone https://github.com/microsoft/semantic-kernel.git    #2

cd semantic-kernel/python    #3

pip install -e .    #4
```

#1 Menghapus instalasi SK sebelumnya
#2 Mengkloning repositori ke folder lokal
#3 Berubah ke folder sumber
#4 Menginstal paket yang dapat diedit dari folder sumber


Setelah Anda menyelesaikan instalasi, buka `SK_connecting.py` di VS Code. Daftar 5.9 menunjukkan demo menjalankan contoh dengan cepat melalui SK. Contoh membuat layanan penyelesaian obrolan menggunakan OpenAI atau Azure OpenAI.

**Daftar 5.9** `SK_connecting.py`

```python
import semantic_kernel as sk

selected_service = "OpenAI"    #1
kernel = sk.Kernel()    #2

service_id = None
if selected_service == "OpenAI":
    from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

    api_key, org_id = sk.openai_settings_from_dot_env()    #3
    service_id = "oai_chat_gpt"
    kernel.add_service(
        OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id="gpt-3.5-turbo-1106",
            api_key=api_key,
            org_id=org_id,
        ),
    )
elif selected_service == "AzureOpenAI":
    from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

    deployment, api_key, endpoint = 
 ↪ sk.azure_openai_settings_from_dot_env()  #4
    service_id = "aoai_chat_completion"
    kernel.add_service(
        AzureChatCompletion(
            service_id=service_id,
            deployment_name=deployment,
            endpoint=endpoint,
            api_key=api_key,
        ),
    )

#Fungsi ini saat ini rusak
async def run_prompt():
    result = await kernel.invoke_prompt( 
              ↪ prompt="rekomendasikan film tentang 
 ↪ perjalanan waktu")    #5
    print(result)

# Gunakan asyncio.run untuk menjalankan fungsi async
asyncio.run(run_prompt())    #6

###Keluaran
Salah satu film perjalanan waktu yang sangat direkomendasikan adalah "Back to the Future" (1985) 
disutradarai oleh Robert Zemeckis. Film klasik ini mengikuti petualangan 
remaja Marty McFly (Michael J. Fox)…
```

#1 Mengatur layanan yang Anda gunakan (OpenAI atau Azure OpenAI)
#2 Membuat kernel
#3 Memuat rahasia dari file .env dan mengaturnya di layanan obrolan
#4 Memuat rahasia dari file .env dan mengaturnya di layanan obrolan
#5 Memanggil prompt
#6 Memanggil fungsi secara asinkron


Jalankan contoh dengan menekan F5 (debugging), dan Anda akan melihat output yang mirip dengan daftar 5.9. Contoh ini menunjukkan bagaimana fungsi semantik dapat dibuat dengan SK dan dieksekusi. Fungsi semantik setara dengan templat prompt di alur prompt, alat Microsoft lainnya. Dalam contoh ini, kami mendefinisikan prompt sederhana sebagai fungsi.

Penting untuk dicatat bahwa fungsi semantik ini tidak didefinisikan sebagai plugin. Namun, kernel dapat membuat fungsi sebagai elemen semantik mandiri yang dapat dieksekusi terhadap LLM. Fungsi semantik dapat digunakan sendiri atau didaftarkan sebagai plugin, seperti yang akan Anda lihat nanti. Mari kita lanjutkan ke bagian berikutnya, di mana kita memperkenalkan variabel kontekstual.

### 5.3.2 Fungsi semantik dan variabel konteks

Memperluas contoh sebelumnya, kita dapat melihat penambahan variabel kontekstual ke fungsi semantik. Pola penambahan placeholder ke templat prompt ini adalah salah satu yang akan kita ulas berulang kali. Dalam contoh ini, kita melihat templat prompt yang memiliki placeholder untuk subjek, genre, format, dan kustom.

Buka `SK_context_variables.py` di VS Code, seperti yang ditunjukkan pada daftar berikutnya. Prompt setara dengan menyisihkan bagian `sistem` dan `pengguna` dari prompt.

**Daftar 5.10** `SK_context_variables.py`

```python
#bagian atas dihilangkan…
prompt = """    #1
sistem:

Anda memiliki pengetahuan luas tentang segalanya dan dapat merekomendasikan apa pun asalkan 
Anda diberi kriteria berikut, subjek, genre, format, dan 
informasi khusus lainnya.

pengguna:
Harap rekomendasikan {{$format}} dengan subjek {{$subject}} dan {{$genre}}.
Sertakan informasi khusus berikut: {{$custom}}
"""

prompt_template_config = sk.PromptTemplateConfig(    #2
    template=prompt,
    name="tldr",
    template_format="semantic-kernel",
    input_variables=[
        InputVariable(
            name="format", 
            description="Format yang akan direkomendasikan", 
            is_required=True
        ),
        InputVariable(
            name="suject", 
            description="Subjek yang akan direkomendasikan", 
            is_required=True
        ),
        InputVariable(
            name="genre", 
            description="Genre yang akan direkomendasikan", 
            is_required=True
        ),
        InputVariable(
            name="custom",
            description="Informasi khusus apa pun [CA]
                       untuk meningkatkan rekomendasi",
            is_required=True,
        ),
    ],
    execution_settings=execution_settings,
)

recommend_function = kernel.create_function_from_prompt(    #3
    prompt_template_config=prompt_template_config,
    function_name="Recommend_Movies",
    plugin_name="Recommendation",
)

async def run_recommendation(
    subject="perjalanan waktu",
    format="film", 
    genre="abad pertengahan", 
           custom="harus komedi"
):
    recommendation = await kernel.invoke(
        recommend_function,
        sk.KernelArguments(subject=subject,
                      format=format, 
                      genre=genre, 
                      custom=custom),    #5
    )
    print(recommendation)


# Gunakan asyncio.run untuk menjalankan fungsi async
asyncio.run(run_recommendation())    #5

###Keluaran
Satu film yang sesuai dengan kriteria tentang perjalanan waktu, berlatar 
periode abad pertengahan, dan merupakan komedi adalah "The Visitors" (Les Visiteurs) 
dari tahun 1993. Film Prancis ini, disutradarai oleh Jean-Marie Poiré, mengikuti seorang 
ksatria dan pengawalnya yang diangkut ke era modern oleh 
antra penyihir yang salah…
```

#1 Mendefinisikan prompt dengan placeholder
#2 Mengonfigurasi templat prompt dan definisi variabel input
#3 Membuat fungsi kernel dari prompt
#4 Membuat fungsi asinkron untuk membungkus panggilan fungsi
#5 Mengatur argumen fungsi kernel


Silakan debug contoh ini (F5), dan tunggu outputnya dibuat. Itulah dasar untuk menyiapkan SK dan membuat serta melatih fungsi semantik. Di bagian berikutnya, kita akan beralih untuk melihat bagaimana fungsi semantik dapat didaftarkan sebagai keterampilan/plugin.

## 5.4 Mensinergikan fungsi semantik dan asli

Fungsi semantik merangkum prompt/profil dan dieksekusi melalui interaksi dengan LLM. Fungsi asli adalah enkapsulasi kode yang dapat melakukan apa saja mulai dari mengikis situs web hingga mencari di web. Baik fungsi semantik maupun asli dapat mendaftar sebagai plugin/keterampilan di kernel SK.

Fungsi, semantik atau asli, dapat didaftarkan sebagai plugin dan digunakan dengan cara yang sama seperti kita mendaftarkan fungsi sebelumnya secara langsung dengan panggilan API kita. Ketika sebuah fungsi didaftarkan sebagai plugin, ia menjadi dapat diakses oleh obrolan atau antarmuka agen, tergantung pada kasus penggunaan. Bagian selanjutnya melihat bagaimana fungsi semantik dibuat dan didaftarkan dengan kernel.

### 5.4.1 Membuat dan mendaftarkan keterampilan/plugin semantik

Ekstensi VS Code untuk SK menyediakan alat yang membantu untuk membuat plugin/keterampilan. Di bagian ini, kita akan menggunakan ekstensi SK untuk membuat plugin/keterampilan dan kemudian mengedit komponen ekstensi itu. Setelah itu, kita akan mendaftarkan dan menjalankan plugin di SK.

Gambar 5.6 menunjukkan proses pembuatan keterampilan baru di dalam VS Code menggunakan ekstensi SK. (Lihat apendiks B untuk petunjuk jika Anda perlu menginstal ekstensi ini.) Anda kemudian akan diberi opsi untuk folder keterampilan/plugin untuk menempatkan fungsi. Selalu kelompokkan fungsi yang serupa bersama-sama. Setelah membuat keterampilan, masukkan nama dan deskripsi fungsi yang ingin Anda kembangkan. Pastikan untuk mendeskripsikan fungsi seolah-olah LLM akan menggunakannya.

![gambar](Images/5-6.png)

**Gambar 5.6** Proses pembuatan keterampilan/plugin baru

Anda dapat melihat keterampilan dan fungsi yang telah selesai dengan membuka folder `keterampilan/plugin` dan meninjau file-filenya. Kami akan mengikuti contoh yang dibuat sebelumnya, jadi buka folder `keterampilan/Pemberi Rekomendasi/Rekomendasikan_Film`, seperti yang ditunjukkan pada gambar 5.7. Di dalam folder ini terdapat file `config.json`, deskripsi fungsi, dan fungsi/prompt semantik dalam file bernama `skprompt.txt`.

![gambar](Images/5-7.png)

**Gambar 5.7** Struktur file dan folder dari keterampilan/plugin fungsi semantik

Daftar 5.11 menunjukkan konten definisi fungsi semantik, juga dikenal sebagai definisi plugin. Perhatikan bahwa jenisnya ditandai sebagai `penyelesaian` dan bukan jenis `fungsi` karena ini adalah fungsi semantik. Kami akan mendefinisikan fungsi asli sebagai fungsi jenis.

**Daftar 5.11** `Rekomendasikan_Film/config.json`

```json
{
    "schema": 1,
    "type": "completion",    #1
    "description": "Fungsi untuk merekomendasikan film berdasarkan daftar film yang 
sebelumnya pernah ditonton pengguna.",
    "completion": {    #2
        "max_tokens": 256,
        "temperature": 0,
        "top_p": 0,
        "presence_penalty": 0,
        "frequency_penalty": 0
    },
    "input": {
        "parameters": [
            {
                "name": "input",    #3
                "description": "Daftar film yang sebelumnya pernah ditonton pengguna.",
                "defaultValue": ""
            }
        ]
    },
    "default_backends": []
}
```

#1 Fungsi semantik adalah fungsi jenis penyelesaian.
#2 Kita juga dapat mengatur parameter penyelesaian untuk bagaimana fungsi dipanggil.
#3 Mendefinisikan parameter yang dimasukkan ke dalam fungsi semantik


Selanjutnya, kita dapat melihat definisi dari prompt fungsi semantik, seperti yang ditunjukkan pada daftar 5.12. Formatnya sedikit berbeda, tetapi apa yang kita lihat di sini cocok dengan contoh sebelumnya yang menggunakan templat. Prompt ini merekomendasikan film berdasarkan daftar film yang pernah ditonton pengguna sebelumnya.

**Daftar 5.12** `Rekomendasikan_Film/skprompt.txt`

```
Anda adalah pemberi rekomendasi film yang bijaksana dan Anda telah diminta untuk merekomendasikan 
film kepada pengguna.
Anda diberikan daftar film yang pernah ditonton pengguna sebelumnya.
Anda ingin merekomendasikan film yang belum pernah ditonton pengguna sebelumnya.
[INPUT]
{{$input}}
[END INPUT]
```


Sekarang, kita akan menyelami kode yang memuat keterampilan/plugin dan menjalankannya dalam contoh sederhana. Buka file `SK_first_skill.py` di VS Code. Daftar berikut menunjukkan versi ringkas yang menyoroti bagian-bagian baru.

**Daftar 5.13** SK_first_skill.py (daftar ringkas)

```python
kernel = sk.Kernel()

plugins_directory = "plugins"

recommender = kernel.import_plugin_from_prompt_directory(
    plugins_directory,
    "Recommender",
)    #1

recommend = recommender["Recommend_Movies"]

seen_movie_list = [
    "Back to the Future",
    "The Terminator",
    "12 Monkeys",
    "Looper",
    "Groundhog Day",
    "Primer",
    "Donnie Darko",
    "Interstellar",
    "Time Bandits",
    "Doctor Strange",
]    #2


async def run():
    result = await kernel.invoke(
        recommend,
        sk.KernelArguments(    #3
                settings=execution_settings, input=", ".join(seen_movie_list)
        ),
    )
    print(result)


asyncio.run(run())    #4

###Keluaran
Berdasarkan daftar film yang telah Anda berikan, tampaknya Anda memiliki 
minat pada fiksi ilmiah, perjalanan waktu, dan narasi yang membingungkan. 
Mengingat bahwa Anda telah menonton campuran film klasik dan modern dalam 
genre ini, saya akan merekomendasikan film berikut yang belum pernah Anda tonton 
sebelumnya:

"Edge of Tomorrow" (juga dikenal sebagai "Live Die Repeat: Edge of Tomorrow")…
```

#1 Memuat prompt dari folder plugin
#2 Daftar film yang pernah ditonton pengguna sebelumnya
#3 Input diatur ke daftar gabungan film yang pernah ditonton.
#4 Fungsi dieksekusi secara asinkron.


Kode memuat keterampilan/plugin dari direktori `keterampilan` dan folder `plugin`. Ketika sebuah keterampilan dimuat ke dalam kernel dan tidak hanya dibuat, itu menjadi plugin terdaftar. Itu berarti ia dapat dieksekusi secara langsung seperti yang dilakukan di sini atau melalui percakapan obrolan LLM melalui antarmuka plugin.

Jalankan kode (F5), dan Anda akan melihat output seperti daftar 5.13. Kami sekarang memiliki fungsi semantik sederhana yang dapat dihosting sebagai plugin. Namun, fungsi ini mengharuskan pengguna untuk memasukkan daftar lengkap film yang telah mereka tonton. Kami akan mencari cara untuk memperbaikinya dengan memperkenalkan fungsi asli di bagian selanjutnya.

### 5.4.2 Menerapkan fungsi asli

Seperti yang dinyatakan, fungsi asli adalah kode yang dapat melakukan apa saja. Dalam contoh berikut, kita akan memperkenalkan fungsi asli untuk membantu fungsi semantik yang kita buat sebelumnya.

Fungsi asli ini akan memuat daftar film yang pernah ditonton pengguna sebelumnya, dari sebuah file. Meskipun fungsi ini memperkenalkan konsep memori, kita akan menunda diskusi itu hingga bab 8. Anggap fungsi asli baru ini sebagai kode apa pun yang secara virtual dapat melakukan apa saja.

Fungsi asli dapat dibuat dan didaftarkan menggunakan ekstensi SK. Untuk contoh ini, kita akan membuat fungsi asli langsung dalam kode agar contoh lebih mudah diikuti.

Buka `SK_native_functions.py` di VS Code. Kita akan mulai dengan melihat bagaimana fungsi asli didefinisikan. Fungsi asli biasanya didefinisikan di dalam kelas, yang menyederhanakan pengelolaan dan pembuatan instance fungsi asli.

**Daftar 5.14** `SK_native_functions.py` (`MySeenMovieDatabase`)

```python
kelas MySeenMoviesDatabase:
    """
    Deskripsi: Mengelola daftar film yang pernah ditonton pengguna.    #1
    """
    @kernel_function(    #2
        description="Memuat daftar film … yang pernah dilihat pengguna",
        name="LoadSeenMovies",
    )
    def load_seen_movies(self) -> str:    #3
        try:
            with open("seen_movies.txt", 'r') as file:    #4
                lines = [line.strip() for line in file.readlines()]
                comma_separated_string = ', '.join(lines)
            return comma_separated_string
        except Exception as e:
            print(f"Kesalahan membaca file: {e}")
            return None
```

#1 Memberikan deskripsi untuk kelas penampung
#2 Menggunakan dekorator untuk memberikan deskripsi dan nama fungsi
#3 Fungsi sebenarnya mengembalikan daftar film dalam string yang dipisahkan koma.
#4 Memuat film yang pernah ditonton dari file teks


Dengan fungsi asli yang telah ditentukan, kita dapat melihat bagaimana ia digunakan dengan menggulir ke bawah dalam file, seperti yang ditunjukkan pada daftar berikut.

**Daftar 5.15** `SK_native_functions` (kode yang tersisa)

```python
plugins_directory = "plugins"

recommender = kernel.import_plugin_from_prompt_directory(
    plugins_directory,
    "Recommender",
)    #1

recommend = recommender["Recommend_Movies"]

seen_movies_plugin = kernel.import_plugin_from_object(
    MySeenMoviesDatabase(), "SeenMoviesPlugin"
)    #2

load_seen_movies = seen_movies_plugin["LoadSeenMovies"]    #3

async def show_seen_movies():
    seen_movie_list = await load_seen_movies(kernel)
    return seen_movie_list

seen_movie_list = asyncio.run(show_seen_movies())    #4
print(seen_movie_list)

async def run():     #5
    result = await kernel.invoke(
        recommend,
        sk.KernelArguments(
                settings=execution_settings,
                input=seen_movie_list),
    )
    print(result)


asyncio.run(run())    #5

###Keluaran
The Matrix, The Matrix Reloaded, The Matrix Revolutions, The Matrix 
Resurrections – *keluaran dari pernyataan cetak*
Berdasarkan minat Anda pada seri "The Matrix", tampaknya Anda menikmati 
film fiksi ilmiah dengan nada filosofis yang kuat dan elemen 
Aksi. Mengingat Anda telah menonton keempatnya
```

#1 Memuat fungsi semantik seperti yang ditunjukkan sebelumnya
#2 Mengimpor keterampilan ke dalam kernel dan mendaftarkan fungsi sebagai plugin
#3 Memuat fungsi asli
#4 Menjalankan fungsi dan mengembalikan daftar sebagai string
#5 Membungkus panggilan plugin dalam fungsi asinkron dan menjalankannya


Satu aspek penting yang perlu diperhatikan adalah bagaimana fungsi asli diimpor ke dalam kernel. Tindakan mengimpor ke kernel mendaftarkan fungsi itu sebagai plugin/keterampilan. Ini berarti fungsi tersebut dapat digunakan sebagai keterampilan dari kernel melalui percakapan atau interaksi lain. Kita akan melihat cara menyematkan fungsi asli di dalam fungsi semantik di bagian selanjutnya.

### 5.4.3 Menyematkan fungsi asli di dalam fungsi semantik

Ada banyak fitur canggih di dalam SK, tetapi salah satu fitur yang bermanfaat adalah kemampuan untuk menyematkan fungsi asli atau semantik di dalam fungsi semantik lainnya. Daftar berikut menunjukkan bagaimana fungsi asli dapat disematkan di dalam fungsi semantik.

**Daftar 5.16** `SK_semantic_native_functions.py` (`skprompt`)

```python
sk_prompt = """
Anda adalah pemberi rekomendasi film yang bijaksana dan Anda telah diminta untuk merekomendasikan 
film kepada pengguna.
Anda memiliki daftar film yang pernah ditonton pengguna sebelumnya.
Anda ingin merekomendasikan film yang 
pengguna belum pernah menonton sebelumnya.    #1
Daftar Film: {{MySeenMoviesDatabase.LoadSeenMovies}}.    #2
"""
```

#1 Teks instruksi yang sama persis seperti sebelumnya
#2 Fungsi asli direferensikan dan diidentifikasi berdasarkan nama kelas dan nama fungsi.


Contoh berikutnya, `SK_semantic_native_functions.py`, menggunakan fungsi asli dan semantik sebaris. Buka file di VS Code, dan daftar berikut menunjukkan kode untuk membuat, mendaftarkan, dan menjalankan fungsi.

**Daftar 5.17** `SK_semantic_native_functions.py` (diringkas)

```python
prompt_template_config = sk.PromptTemplateConfig(
    template=sk_prompt,
    name="tldr",
    template_format="semantic-kernel",
    execution_settings=execution_settings,
)    #1

recommend_function = kernel.create_function_from_prompt(
    prompt_template_config=prompt_template_config,
    function_name="Recommend_Movies",
    plugin_name="Recommendation",
)    #2


async def run_recommendation():    #3
    recommendation = await kernel.invoke(
        recommend_function,
        sk.KernelArguments(),
    )
    print(recommendation)


# Gunakan asyncio.run untuk menjalankan fungsi async
asyncio.run(run_recommendation())
###Keluaran
Berdasarkan daftar yang diberikan, tampaknya pengguna adalah penggemar 
waralaba Matrix. Karena mereka telah menonton keempat film Matrix yang ada, saya 
Akan merekomendasikan…
```

#1 Membuat konfigurasi templat prompt untuk prompt
#2 Membuat fungsi semantik sebaris dari prompt
#3 Menjalankan fungsi semantik secara asinkron


Jalankan kode, dan Anda akan melihat output seperti daftar 5.17. Satu aspek penting yang perlu diperhatikan adalah bahwa fungsi asli terdaftar di kernel, tetapi fungsi semantik tidak. Ini penting karena pembuatan fungsi tidak mendaftarkan fungsi.

Agar contoh ini berfungsi dengan benar, fungsi asli harus didaftarkan dengan kernel, yang menggunakan panggilan fungsi `import_plugin`—baris pertama dalam daftar 5.17. Namun, fungsi semantik itu sendiri tidak terdaftar. Cara mudah untuk mendaftarkan fungsi adalah dengan menjadikannya plugin dan mengimpornya.

Latihan sederhana ini menunjukkan cara mengintegrasikan plugin dan keterampilan ke dalam obrolan atau antarmuka agen. Di bagian selanjutnya, kita akan melihat contoh lengkap yang menunjukkan penambahan plugin yang mewakili layanan atau antarmuka GPT ke fungsi obrolan.

## 5.5 Kernel Semantik sebagai agen layanan interaktif

Di bab 1, kami memperkenalkan konsep antarmuka GPT—paradigma baru dalam menghubungkan layanan dan komponen lain ke LLM melalui plugin dan lapisan semantik. SK menyediakan abstraksi yang sangat baik untuk mengubah layanan apa pun menjadi antarmuka GPT.

Gambar 5.8 menunjukkan antarmuka GPT yang dibangun di sekitar layanan API yang disebut The Movie Database (TMDB; www.themoviedb.org). Situs TMDB menyediakan API gratis yang mengekspos informasi tentang film dan acara TV.

![gambar](Images/5-8.png)

**Gambar 5.8** Diagram arsitektur lapisan ini menunjukkan peran antarmuka GPT dan Kernel Semantik yang diekspos ke antarmuka obrolan atau agen.

Untuk mengikuti latihan di bagian ini, Anda harus mendaftar untuk mendapatkan akun gratis dari TMDB dan membuat kunci API. Petunjuk untuk mendapatkan kunci API dapat ditemukan di situs web TMDB (www.themoviedb.org) atau dengan menanyakan GPT-4 turbo atau LLM yang lebih baru.

Selama beberapa subbagian berikutnya, kita akan membuat antarmuka GPT menggunakan seperangkat fungsi asli SK. Kemudian, kita akan menggunakan kernel SK untuk menguji antarmuka dan, nanti di bab ini, mengimplementasikannya sebagai plugin ke dalam fungsi obrolan. Di bagian selanjutnya, kita akan melihat membangun antarmuka GPT terhadap API TMDB.

### 5.5.1 Membangun antarmuka GPT semantik

TMDB adalah layanan yang sangat baik, tetapi tidak menyediakan layanan semantik atau layanan yang dapat dicolokkan ke ChatGPT atau agen. Untuk melakukannya, kita harus membungkus panggilan API yang diekspos TMDB dalam lapisan layanan semantik.

Lapisan layanan semantik adalah antarmuka GPT yang mengekspos fungsi melalui bahasa alami. Seperti yang telah dibahas, untuk mengekspos fungsi ke ChatGPT atau antarmuka lain seperti agen, mereka harus didefinisikan sebagai plugin. Untungnya, SK dapat membuat plugin untuk kita secara otomatis, asalkan kita menulis lapisan layanan semantik kita dengan benar.

Plugin asli atau seperangkat keterampilan dapat bertindak sebagai lapisan semantik. Untuk membuat plugin asli, buat folder plugin baru, dan letakkan file Python yang berisi kelas yang berisi seperangkat fungsi asli di dalam folder itu. Ekstensi SK saat ini tidak melakukan ini dengan baik, jadi membuat modul secara manual berfungsi paling baik.

Gambar 5.9 menunjukkan struktur plugin baru yang disebut `Film` dan lapisan layanan semantik yang disebut `tmdb.py`. Untuk fungsi asli, nama folder induk (`Film`) digunakan dalam impor.

![gambar](Images/5-9.png)

**Gambar 5.9** Struktur folder dan file dari plugin TMDB

Buka file `tmdb.py` di VS Code, dan lihat bagian atas file, seperti yang ditunjukkan pada daftar 5.18. File ini berisi kelas bernama `TMDbService`, yang mengekspos beberapa fungsi yang memetakan ke panggilan titik akhir API. Idenya adalah untuk memetakan berbagai panggilan fungsi API yang relevan dalam lapisan layanan semantik ini. Ini akan mengekspos fungsi sebagai plugin untuk antarmuka obrolan atau agen.

**Daftar 5.18** `tmdb.py` (atas file)

```python
dari semantic_kernel.functions impor kernel_funct
import requests
import inspect


def print_function_call():    #1
    #dihilangkan…


kelas TMDbService:    #2
    def __init__(self):
        # masukkan kunci API TMDb Anda di sini
        self.api_key = "kunci-api-TMDb-Anda"


    @kernel_function(     #2
        description="Mendapatkan ID genre film untuk nama genre tertentu",
        name="get_movie_genre_id",
        input_description="Nama genre film dari genre_id yang akan didapatkan",
        )
    def get_movie_genre_id(self, genre_name: str) -> str:    #3
        print_function_call()
        base_url = "https://api.themoviedb.org/3"
        endpoint = f"{base_url}/genre/movie/list
                     ↪ ?api_key={self.api_key}&language=en-US"

        response = requests.get(endpoint)    #4
        if response.status_code == 200:    #4
            genres = response.json()['genres']
            for genre in genres:
                if genre_name.lower() in genre['name'].lower():
                    return str(genre['id'])    #5
        return None
```

#1 Mencetak panggilan ke fungsi untuk debugging
#2 Layanan tingkat atas dan dekorator yang digunakan untuk mendeskripsikan fungsi (deskripsi yang baik itu penting)
#3 Fungsi yang dibungkus dalam pembungkus semantik; harus mengembalikan str
#4 Memanggil titik akhir API, dan, jika bagus (kode 200), memeriksa genre yang cocok
#5 Menemukan genre, mengembalikan id


Sebagian besar kode untuk `TMDbService` dan fungsi untuk memanggil titik akhir TMDB ditulis dengan bantuan GPT-4 Turbo. Kemudian, setiap fungsi dibungkus dengan dekorator `sk_function` untuk mengeksposnya secara semantik.

Beberapa panggilan API TMDB telah dipetakan secara semantik. Daftar 5.19 menunjukkan contoh lain dari fungsi yang diekspos ke lapisan layanan semantik. Fungsi ini menarik daftar 10 film teratas yang sedang diputar untuk genre tertentu.

**Daftar 5.19** `tmdb.py` (`get_top_movies_by_genre`)

```python
@kernel_function(    #1
    description="””
Mendapatkan daftar film yang sedang diputar untuk genre tertentu””",
    name="get_top_movies_by_genre",
    input_description="Genre film yang akan didapatkan",
    )
    def get_top_movies_by_genre(self, genre: str) -> str:
        print_function_call()
        genre_id = self.get_movie_genre_id(genre)    #2
        if genre_id:
            base_url = "https://api.themoviedb.org/3
            playing_movies_endpoint = f"{base_url}/movie/now_playing?"
↪ api_key={self.api_key}&language=en-US"
            response = requests.get(
                          playing_movies_endpoint)    #3
            if response.status_code != 200:
                return ""

            playing_movies = response.json()['results'
            for movie in playing_movies:    #4
                movie['genre_ids'] = [str(genre_id) 
                      ↪ for genre_id in movie['genre_ids']]
            filtered_movies = [movie for movie ↪
↪ in playing_movies if genre_id ↪
↪ in movie['genre_ids']][:10]    #5
            results = ", ".join([movie['title'] for movie in filtered_movies])
            return results
        else:
            return ""
```

#1 Menghias fungsi dengan deskripsi
#2 Menemukan id genre untuk nama genre yang diberikan
#3 Mendapatkan daftar film yang sedang diputar
#4 Mengonversi genre_id menjadi string
#5 Memeriksa apakah id genre cocok dengan genre film


Lihat melalui berbagai panggilan API lain yang dipetakan secara semantik. Seperti yang Anda lihat, ada pola yang terdefinisi dengan baik untuk mengubah panggilan API menjadi layanan semantik. Sebelum kita menjalankan layanan lengkap, kita akan menguji setiap fungsi di bagian selanjutnya.

### 5.5.2 Menguji layanan semantik

Dalam aplikasi dunia nyata, Anda mungkin ingin menulis serangkaian pengujian unit atau integrasi lengkap untuk setiap fungsi layanan semantik. Kami tidak akan melakukannya di sini; sebaliknya, kami akan menulis skrip pembantu cepat untuk menguji berbagai fungsi.

Buka `test_tmdb_service.py` di VS Code, dan tinjau kodenya, seperti yang ditunjukkan pada daftar 5.20. Anda dapat mengomentari dan menghapus komentar fungsi apa pun untuk mengujinya secara terpisah. Pastikan hanya ada satu fungsi yang tidak dikomentari pada satu waktu.

**Daftar 5.20** `test_tmdb_service.py`

```python
import semantic_kernel as sk
dari plugins.Movies.tmdb import TMDbService

async def main():
    kernel = sk.Kernel()    #1

    tmdb_service = kernel.import_plugin_from_object 
 ↪ (TMDbService(), "TMDBService")    #2

    print(
        await tmdb_service["get_movie_genre_id"](
            kernel, sk.KernelArguments(
                            genre_name="action")    #3
        )
    )    #4
    print(
        await tmdb_service["get_tv_show_genre_id"](
            kernel, sk.KernelArguments(
                            genre_name="action")    #5
        )
    )    #6
    print(
        await tmdb_service["get_top_movies_by_genre"](
            kernel, sk.KernelArguments(
                            genre_name="action")    #7
        )
    )    #8
    print(
        await tmdb_service["get_top_tv_shows_by_genre"](
            kernel, sk.KernelArguments(
                            genre_name="action")    #7
        )
    )
    print(await tmdb_service["get_movie_genres"](
kernel, sk.KernelArguments()))                       #9
    print(await tmdb_service["get_tv_show_genres"](
kernel, sk.KernelArguments()))                       #9


# Jalankan fungsi utama
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())    #10

###Keluaran
Nama fungsi: get_top_tv_shows_by_genre    #11
Argumen:
  self = <skills.Movies.tmdb.TMDbService object at 0x00000159F52090C0>
  genre = action
Nama fungsi: get_tv_show_genre_id    #11
Argumen:
  self = <skills.Movies.tmdb.TMDbService object at 0x00000159F52090C0>
  genre_name = action
Arcane, One Piece, Rick and Morty, Avatar: The Last Airbender, Fullmetal 
Alchemist: Brotherhood, Demon Slayer: Kimetsu no Yaiba, Invincible, 
Attack on Titan, My Hero Academia, Fighting Spirit, The Owl House
```

#1 Membuat instance kernel
#2 Mengimpor layanan plugin
#3 Memasukkan parameter ke fungsi, bila diperlukan
#4 Menjalankan dan menguji berbagai fungsi
#5 Memasukkan parameter ke fungsi, bila diperlukan
#6 Menjalankan dan menguji berbagai fungsi
#7 Memasukkan parameter ke fungsi, bila diperlukan
#8 Menjalankan dan menguji berbagai fungsi
#9 Menjalankan dan menguji berbagai fungsi
#10 Menjalankan utama secara asinkron
#11 Memanggil detail fungsi cetak untuk memberi tahu saat fungsi sedang dipanggil


Kekuatan sebenarnya dari SK ditunjukkan dalam pengujian ini. Perhatikan bagaimana kelas `TMDbService` diimpor sebagai plugin, tetapi kita tidak perlu mendefinisikan konfigurasi plugin apa pun selain yang sudah kita lakukan? Hanya dengan menulis satu kelas yang membungkus beberapa fungsi API, kita telah mengekspos bagian dari API TMDB secara semantik. Sekarang, dengan fungsi yang diekspos, kita dapat melihat bagaimana mereka dapat digunakan sebagai plugin untuk antarmuka obrolan di bagian selanjutnya.

### 5.5.3 Obrolan interaktif dengan lapisan layanan semantik

Dengan fungsi TMDB yang diekspos secara semantik, kita dapat melanjutkan untuk mengintegrasikannya ke dalam antarmuka obrolan. Ini akan memungkinkan kita untuk berkomunikasi secara alami di antarmuka ini untuk mendapatkan berbagai informasi, seperti film teratas saat ini.

Buka `SK_service_chat.py` di VS Code. Gulir ke bawah ke awal bagian baru kode yang membuat fungsi, seperti yang ditunjukkan pada daftar 5.21. Fungsi yang dibuat di sini sekarang diekspos sebagai plugin, kecuali kita memfilter fungsi obrolan, yang tidak ingin kita ekspos sebagai plugin. Fungsi obrolan di sini memungkinkan pengguna untuk berkomunikasi langsung dengan LLM dan tidak boleh menjadi plugin.

**Daftar 5.21** `SK_service_chat.py` (penyiapan fungsi)

```python
system_message = "Anda adalah asisten AI yang membantu."

tmdb_service = kernel.import_plugin_from_object(
TMDbService(), "TMDBService")    #1

# bagian kode yang diekstraksi
execution_settings = sk_oai.OpenAIChatPromptExecutionSettings(
        service_id=service_id,
        ai_model_id=model_id,
        max_tokens=2000,
        temperature=0.7,
        top_p=0.8,
        tool_choice="auto",
        tools=get_tool_call_object(
            kernel, {"exclude_plugin": ["ChatBot"]}),    #2
    )

prompt_config = sk.PromptTemplateConfig.from_completion_parameters(
    max_tokens=2000,
    temperature=0.7,
    top_p=0.8,
    function_call="auto",
    chat_system_prompt=system_message,
)    #3
prompt_template = OpenAIChatPromptTemplate(
    "{{$user_input}}", kernel.prompt_template_engine, prompt_config
)    #4

history = ChatHistory()

history.add_system_message("Anda merekomendasikan film dan Acara TV.")
history.add_user_message("Hai, siapa Anda?")
history.add_assistant_message(
    "Saya Rudy, bot obrolan pemberi rekomendasi. Saya mencoba mencari tahu apa yang 
dibutuhkan orang."
)    #5

chat_function = kernel.create_function_from_prompt(
    prompt_template_config=prompt_template,
    plugin_name="ChatBot",
    function_name="Chat",
)    #6
```

#1 Mengimpor TMDbService sebagai plugin
#2 Mengonfigurasi pengaturan eksekusi dan menambahkan alat yang difilter
#3 Mengonfigurasi konfigurasi prompt
#4 Mendefinisikan templat input dan mengambil string lengkap sebagai input pengguna
#5 Menambahkan objek riwayat obrolan dan mengisi beberapa riwayat
#6 Membuat fungsi obrolan


Selanjutnya, kita dapat melanjutkan dengan menggulir di file yang sama untuk meninjau fungsi obrolan, seperti yang ditunjukkan pada daftar berikut.

**Daftar 5.22** `SK_service_chat.py` (fungsi obrolan)

```python
async def chat() -> bool:
    try:
        user_input = input("Pengguna:>")    #1
    except KeyboardInterrupt:
        print("\n\nKeluar dari obrolan...")
        return False
    except EOFError:
        print("\n\nKeluar dari obrolan...")
        return False

    if user_input == "exit":    #2
        print("\n\nKeluar dari obrolan...")
        return False
    arguments = sk.KernelArguments(    #3
        user_input=user_input,
        history=("\n").join(
           [f"{msg.role}: {msg.content}" for msg in history]),
    )
    result = await chat_completion_with_tool_call(    #4
        kernel=kernel,
        arguments=arguments,
        chat_plugin_name="ChatBot",
        chat_function_name="Chat",
        chat_history=history,
    )
    print(f"Agen AI:> {result}")
    return True
```

#1 Input diambil langsung dari terminal/konsol.
#2 Jika pengguna mengetik keluar, maka keluar dari obrolan.
#3 Membuat argumen untuk diteruskan ke fungsi
#4 Menggunakan fungsi utilitas untuk memanggil fungsi dan menjalankan alat


Terakhir, gulir ke bawah ke bagian bawah file, dan tinjau fungsi utama. Ini adalah kode yang memanggil fungsi obrolan dalam satu lingkaran.

**Daftar 5.23** `SK_service_chat.py` (fungsi utama)

```python
async def main() -> None:
    chatting = True
    context = kernel.create_new_context()

    print("Selamat datang di Agen AI pertama Anda\    #1
  Ketik 'keluar' untuk keluar.
  Minta untuk mendapatkan daftar film yang sedang diputar berdasarkan genre."
    )
    while chatting:    #2
        chatting, context = await chat(context)    #3


if __name__ == "__main__":
    asyncio.run(main())
```

#1 Pengantar untuk pengguna
#2 Berlanjut hingga obrolan adalah Salah
#3 Memanggil fungsi obrolan secara asinkron


Jalankan antarmuka obrolan, jalankan file (F5), lalu tanyakan tentang film atau acara televisi dari genre tertentu. Contoh sesi percakapan ditunjukkan pada daftar 5.24. Output ini menunjukkan bagaimana permintaan untuk mendaftar film dari dua genre membuat antarmuka obrolan melakukan beberapa panggilan ke fungsi `get_top_movie_by_genre`.

**Daftar 5.24** `SK_service_chat.py` (contoh percakapan) 

```python
Selamat datang di Agen AI pertama Anda
  Ketik 'keluar' untuk keluar.
  Minta untuk mendapatkan daftar film yang sedang diputar berdasarkan genre.
Pengguna:> Input: bisakah Anda memberi saya daftar film teratas yang sedang diputar untuk 
genre aksi dan komedi?

Nama fungsi: get_top_movies_by_genre    #1
Argumen:
  genre = aksi
Nama fungsi: get_movie_genre_id    #2
Argumen:
  genre_name = aksi
Nama fungsi: get_top_movies_by_genre    #1
Argumen:
  genre = komedi
Nama fungsi: get_movie_genre_id    #2
Argumen:
  genre_name = komedi
Agen:> Berikut adalah film teratas yang sedang diputar 
untuk genre aksi dan komedi:

**Aksi:**    #3
1. The Hunger Games: The Ballad of Songbirds & Snakes
2. Rebel Moon - Part One: A Child of Fire
3. Aquaman and the Lost Kingdom
4. Silent Night
5. The Family Plan
6. Freelance
7. Migration
8. Sound of Freedom
9. Godzilla Minus One

**Komedi:**    #4
1. The Family Plan
2. Wonka
3. Freelance
4. Saltburn
5. Chicken Run: Dawn of the Nugget
6. Trolls Band Together
7. There's Something in the Barn
8. Migration

Harap dicatat bahwa beberapa film mungkin tumpang tindih di kedua genre, seperti 
"The Family Plan" dan "Freelance ."
```

#1 LLM melakukan dua panggilan ke get_top_movies_by_genre.
#2 Panggilan internal untuk mendapatkan id genre
#3 Daftar film aksi teratas saat ini
#4 Daftar film komedi teratas saat ini


Pastikan untuk menjelajahi batas-batas antarmuka obrolan dan apa yang dapat Anda minta dari layanan TMDB. Misalnya, coba minta daftar genre untuk film atau acara televisi. Layanan ini adalah percobaan pertama yang baik, tetapi mungkin kita bisa melakukan yang lebih baik, seperti yang akan kita lihat di bagian selanjutnya.

## 5.6 Berpikir secara semantik saat menulis layanan semantik

Sekarang kita telah melihat demonstrasi yang sangat baik tentang mengubah API menjadi antarmuka layanan semantik. Sebagaimana adanya, fungsi mengembalikan judul film dan acara televisi teratas yang sedang diputar. Namun, dengan hanya mengembalikan judul, kita membatasi kemampuan LLM untuk mengurai hasilnya sendiri.

Oleh karena itu, kita akan membuat versi v2 dari `TMDbService` untuk memperbaiki ini dan mengembalikan hasilnya sebagai string JSON. Buka file `tmdb_v2.py` di VS Code, dan gulir ke bawah ke fungsi `get_top_movies_by_genre`.

**Daftar 5.25** `tmdb_v2.py` (`get_top_movies_by_genre`)

```python
def get_top_movies_by_genre(self, genre: str) -> str:
    print_function_call()
    genre_id = self.get_movie_genre_id(genre)
    if genre_id:
        #kode yang sama…

        return json.dumps(filtered_movies)    #1
    else:
        return ""
```

#1 Sekarang mengembalikan daftar yang difilter sebagai string JSON


Sekarang buka `SK_service_chat.py` di VS Code, dan komentari dan hapus komentar pada baris yang ditunjukkan pada daftar 5.26. Ini kemudian akan menggunakan versi 2 dari `TMDbService` yang mengeluarkan hasil sebagai dokumen JSON lengkap dalam satu string.

**Daftar 5.26** `SK_service_chat.py` (memodifikasi impor)

```python
#dari skills.Movies.tmdb impor TMDbService    #1
 dari skills.Movies.tmdb_v2 impor TMDbService    #2
```

#1 Komentari baris ini.
#2 Hapus komentar pada baris ini untuk menggunakan versi 2 dari layanan.


Jalankan kembali file `SK_service_chat.py` di VS Code, dan ubah sedikit kueri Anda, seperti yang ditunjukkan oleh output pada daftar berikut.

**Daftar 5.27** `SK_service_chat.py` (output layanan `TMDb_v2`)

```python
Pengguna:> dapatkan daftar film yang sedang diputar untuk 
genre aksi dan hanya kembalikan film tentang luar angkasa    #1
Agen:> Untuk menemukan film aksi yang sedang diputar yang secara spesifik 
 tentativo tentang luar angkasa, saya perlu memfilter secara manual daftar yang diberikan untuk film-film 
yang memiliki tema terkait luar angkasa dalam ikhtisarnya. Inilah yang sesuai dengan 
kriteria itu dari daftar:

1. **Rebel Moon - Part One: A Child of Fire**    #2
   - Tanggal Rilis: 2023-12-15
   - Ikhtisar: Ketika sebuah koloni yang damai di tepi galaksi menemukan 
 dirinya terancam oleh pasukan Tiran Regent Balisarius, 
 mereka mengirim Kora, seorang wanita muda dengan masa lalu yang misterius, untuk mencari 
 prajurit dari planet tetangga untuk membantu mereka bertahan.

Ini adalah satu-satunya film dari daftar yang diberikan yang dengan jelas menyebutkan 
tema terkait luar angkasa dalam ikhtisarnya. …
```

#1 Kueri baru meminta untuk menyertakan filter tambahan untuk luar angkasa
#2 LLM memanggil layanan dan kemudian meninjau hasil yang dikembalikan yang cocok dengan filter.


Karena fungsi layanan semantik sekarang mengembalikan daftar film lengkap dalam JSON, LLM dapat menerapkan pemfilteran tambahan. Inilah kekuatan sebenarnya dari layanan semantik, memungkinkan Anda memproses data melalui LLM. Kita tidak akan melihat kekuatan ini dengan hanya mengembalikan daftar judul.

Latihan terakhir ini menunjukkan perubahan mentalitas yang perlu Anda lakukan saat menulis lapisan layanan semantik. Umumnya, Anda biasanya ingin mengembalikan informasi sebanyak mungkin. Mengembalikan lebih banyak informasi memanfaatkan kemampuan LLM untuk memfilter, mengurutkan, dan mengubah data secara mandiri. Di bab selanjutnya, kita akan menjelajahi membangun agen otonom menggunakan pohon perilaku.

## 5.7 Latihan

Selesaikan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- *Latihan 1*—Membuat Plugin Dasar untuk Konversi Suhu  
- *Tujuan*—Membiasakan diri dengan membuat plugin sederhana untuk API penyelesaian obrolan OpenAI. 
- *Tugas:*
  - Kembangkan plugin yang mengubah suhu antara Celsius dan Fahrenheit. 
  - Uji plugin dengan mengintegrasikannya ke dalam sesi obrolan OpenAI sederhana di mana pengguna dapat meminta konversi suhu. 
- *Latihan 2*—Mengembangkan Plugin Informasi Cuaca  
- *Tujuan*—Belajar membuat plugin yang melakukan tugas unik. 
- *Tugas:*
  - Buat plugin untuk API penyelesaian obrolan OpenAI yang mengambil informasi cuaca dari API publik. 
  - Pastikan plugin dapat menangani permintaan pengguna untuk kondisi cuaca saat ini di berbagai kota. 
- *Latihan 3*—Membuat Fungsi Semantik Kreatif  
- *Tujuan*—Menjelajahi pembuatan fungsi semantik. 
- *Tugas:*
  - Kembangkan fungsi semantik yang menulis puisi atau menceritakan dongeng anak-anak berdasarkan masukan pengguna. 
  - Uji fungsi dalam sesi obrolan untuk memastikan fungsi tersebut menghasilkan keluaran yang kreatif dan koheren. 
- *Latihan 4*—Meningkatkan Fungsi Semantik dengan Fungsi Asli  
- *Tujuan*—Memahami cara menggabungkan fungsi semantik dan asli. 
- *Tugas:*
  - Buat fungsi semantik yang menggunakan fungsi asli untuk meningkatkan kemampuannya. 
  - Misalnya, kembangkan fungsi semantik yang menghasilkan rencana makan dan menggunakan fungsi asli untuk mengambil informasi nutrisi untuk bahan-bahannya. 
- *Latihan 5*—Membungkus API Web yang Ada dengan Kernel Semantik 
- *Tujuan*—Belajar membungkus API web yang ada sebagai plugin layanan semantik. 
- *Tugas:*
  - Gunakan SK untuk membungkus API berita dan mengeksposnya sebagai plugin layanan semantik di agen obrolan. 
  - Pastikan plugin dapat menangani permintaan pengguna untuk artikel berita terbaru tentang berbagai topik. 

## Ringkasan

- Tindakan agen memperluas kemampuan sistem agen, seperti ChatGPT. Ini termasuk kemampuan untuk menambahkan plugin ke ChatGPT dan LLM agar berfungsi sebagai proksi untuk tindakan. 
- OpenAI mendukung definisi fungsi dan plugin dalam sesi API OpenAI. Ini termasuk menambahkan definisi fungsi ke panggilan API LLM dan memahami bagaimana fungsi-fungsi ini memungkinkan LLM untuk melakukan tindakan tambahan. 
- Semantic Kernel (SK) adalah proyek sumber terbuka dari Microsoft yang dapat digunakan untuk membangun aplikasi AI dan sistem agen. Ini termasuk peran plugin semantik dalam mendefinisikan fungsi asli dan semantik. 
- Fungsi semantik merangkum templat prompt/profil yang digunakan untuk melibatkan LLM. 
- Fungsi asli merangkum kode yang melakukan atau menjalankan tindakan menggunakan API atau antarmuka lain. 
- Fungsi semantik dapat digabungkan dengan fungsi semantik atau asli lainnya dan dilapisi satu sama lain sebagai tahap eksekusi. 
- SK dapat digunakan untuk membuat antarmuka GPT di atas panggilan API dalam lapisan layanan semantik dan mengeksposnya sebagai plugin antarmuka obrolan atau agen. 
- Layanan semantik mewakili interaksi antara LLM dan plugin, serta implementasi praktis dari konsep-konsep ini dalam menciptakan agen AI yang efisien.
