# 2 Memanfaatkan kekuatan model bahasa besar

### Bab ini mencakup
- Memahami dasar-dasar LLM
- Menghubungkan dan menggunakan OpenAI API
- Menjelajahi dan menggunakan LLM sumber terbuka dengan LM Studio
- Mendorong LLM dengan rekayasa prompt
- Memilih LLM yang optimal untuk kebutuhan spesifik Anda

Istilah *model bahasa besar* (LLM) kini telah menjadi deskriptor di mana-mana dari suatu bentuk AI. LLM ini telah dikembangkan menggunakan transformer pretrained generatif (GPT). Meskipun arsitektur lain juga mendukung LLM, bentuk GPT saat ini adalah yang paling berhasil.

LLM dan GPT adalah model *generatif*, yang berarti mereka dilatih untuk *menghasilkan* daripada memprediksi atau mengklasifikasikan konten. Untuk mengilustrasikan ini lebih lanjut, pertimbangkan gambar 2.1, yang menunjukkan perbedaan antara model generatif dan prediktif/klasifikasi. Model generatif membuat sesuatu dari input, sedangkan model prediktif dan klasifikasi mengklasifikasikannya.

![Gambar 2.1](Images/2-1.png "Perbedaan antara model generatif dan prediktif")

Kita dapat mendefinisikan LLM lebih lanjut berdasarkan bagian-bagian penyusunnya, seperti yang ditunjukkan pada gambar 2.2. Dalam diagram ini, *data* mewakili konten yang digunakan untuk melatih model, dan *arsitektur* adalah atribut dari model itu sendiri, seperti jumlah parameter atau ukuran model. Model selanjutnya dilatih secara khusus untuk kasus penggunaan yang diinginkan, termasuk obrolan, penyelesaian, atau instruksi. Terakhir, *fine-tuning* adalah fitur yang ditambahkan ke model yang menyempurnakan data input dan pelatihan model agar lebih cocok dengan kasus penggunaan atau domain tertentu.

![Gambar 2.2](Images/2-2.png "Elemen utama yang menggambarkan LLM")

Arsitektur transformer GPT, yang merupakan arsitektur spesifik LLM, memungkinkan model untuk diskalakan hingga miliaran parameter dalam ukuran. Ini mengharuskan model-model besar ini dilatih pada terabyte dokumen untuk membangun fondasi. Dari sana, model-model ini akan dilatih secara berturut-turut menggunakan berbagai metode untuk kasus penggunaan model yang diinginkan.

ChatGPT, misalnya, dilatih secara efektif di internet publik dan kemudian disesuaikan dengan baik باستخدام beberapa strategi pelatihan. Pelatihan penyesuaian akhir diselesaikan menggunakan bentuk lanjutan yang disebut *pembelajaran penguatan dengan umpan balik manusia* (RLHF). Ini menghasilkan kasus penggunaan model yang disebut penyelesaian obrolan.

*Penyelesaian obrolan* LLM dirancang untuk meningkat melalui iterasi dan penyempurnaan—dengan kata lain, mengobrol. Model-model ini juga telah diukur sebagai yang terbaik dalam penyelesaian tugas, penalaran, dan perencanaan, yang menjadikannya ideal untuk membangun agen dan asisten. Model penyelesaian dilatih/dirancang hanya untuk menyediakan konten yang dihasilkan pada teks input, sehingga tidak mendapat manfaat dari iterasi.

Untuk perjalanan kita membangun agen yang kuat dalam buku ini, kita fokus pada kelas LLM yang disebut model penyelesaian obrolan. Tentu saja, itu tidak menghalangi Anda untuk mencoba bentuk model lain untuk agen Anda. Namun, Anda mungkin harus mengubah sampel kode yang disediakan secara signifikan untuk mendukung bentuk model lain.

Kita akan mengungkap lebih banyak detail tentang LLM dan GPT nanti di bab ini ketika kita melihat menjalankan LLM sumber terbuka secara lokal. Di bagian selanjutnya, kita akan melihat cara terhubung ke LLM menggunakan standar yang berkembang dari OpenAI.

## 2.1 Menguasai OpenAI API

Banyak proyek agen dan asisten AI menggunakan OpenAI API SDK untuk terhubung ke LLM. Meskipun bukan standar, konsep dasar yang menggambarkan koneksi sekarang mengikuti pola OpenAI. Oleh karena itu, kita harus memahami konsep inti koneksi LLM menggunakan OpenAI SDK.

Bab ini akan membahas tentang menghubungkan ke model LLM menggunakan OpenAI Python SDK/paket. Kita akan membahas menghubungkan ke model GPT-4, respons model, menghitung token, dan cara mendefinisikan pesan yang konsisten. Mulai dari sub-bagian berikut, kita akan memeriksa cara menggunakan OpenAI.

### 2.1.1 Menghubungkan ke model penyelesaian obrolan

Untuk menyelesaikan latihan di bagian ini dan bagian selanjutnya, Anda harus menyiapkan lingkungan pengembang Python dan mendapatkan akses ke LLM. Apendiks A memandu Anda melalui penyiapan akun OpenAI dan mengakses GPT-4 atau model lain. Apendiks B menunjukkan penyiapan lingkungan pengembangan Python dengan Visual Studio Code (VS Code), termasuk menginstal ekstensi yang diperlukan. Tinjau bagian ini jika Anda ingin mengikuti skenario.

Mulai dengan membuka folder kode sumber `chapter_2` di VS Code dan membuat lingkungan virtual Python baru. Sekali lagi, lihat apendiks B jika Anda memerlukan bantuan.

Kemudian, instal paket OpenAI dan Python dot environment menggunakan perintah di daftar berikut. Ini akan menginstal paket yang diperlukan ke dalam lingkungan virtual.

**Daftar 2.1** `pip` installs 
```
pip install openai python-dotenv
```

Selanjutnya, buka file `connecting.py` di VS Code, dan periksa kode yang ditunjukkan pada daftar 2.2. Pastikan untuk mengatur nama model ke nama yang sesuai—misalnya, gpt-4. Pada saat penulisan, `gpt-4-1106-preview` digunakan untuk mewakili GPT-4 Turbo.

**Daftar 2.2** `connecting.py` 
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()                          #1
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:                            #2
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key)                       #3

def ask_chatgpt(user_message):
    response = client.chat.completions.create(     #4
        model="gpt-4-1106-preview",
        messages=[{"role": "system",
 "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}],
        temperature=0.7,
        )
    return response.choices[0].message.content    #5

user = "What is the capital of France?"
response = ask_chatgpt(user)               #6
print(response)
```
* #1 Memuat rahasia yang disimpan di file .env
* #2 Memeriksa untuk melihat apakah kunci disetel
* #3 Membuat klien dengan kunci
* #4 Menggunakan fungsi buat untuk menghasilkan respons
* #5 Mengembalikan hanya konten respons
* #6 Menjalankan permintaan dan mengembalikan respons

Banyak yang terjadi di sini, jadi mari kita pecah berdasarkan bagian, dimulai dengan awal dan memuat variabel lingkungan. Di folder `chapter_2` ada file lain yang disebut `.env`, yang menyimpan variabel lingkungan. Variabel-variabel ini diatur secara otomatis dengan memanggil fungsi `load_dotenv`.

Anda harus menyetel kunci OpenAI API Anda di file `.env`, seperti yang ditunjukkan pada daftar berikutnya. Sekali lagi, lihat apendiks A untuk mengetahui cara mendapatkan kunci dan menemukan nama model.

**Daftar 2.3** `.env` 
```
OPENAI_API_KEY='kunci-api-openai-anda'
```

Setelah menyetel kunci, Anda dapat men-debug file dengan menekan tombol F5 atau memilih Run > Start Debugging dari menu VS Code. Ini akan menjalankan kode, dan Anda akan melihat sesuatu seperti "Ibukota Prancis adalah Paris."

Ingatlah bahwa respons dari model generatif bergantung pada probabilitas. Model kemungkinan besar akan memberi kita jawaban yang benar dan konsisten dalam kasus ini.

Anda dapat bermain dengan probabilitas ini dengan menyesuaikan suhu permintaan. Jika Anda ingin model lebih konsisten, turunkan suhu ke 0, tetapi jika Anda ingin model menghasilkan lebih banyak variasi, naikkan suhu. Kita akan menjelajahi pengaturan suhu lebih lanjut di bagian selanjutnya.

### 2.1.2 Memahami permintaan dan respons

Mendalami fitur permintaan dan respons penyelesaian obrolan bisa sangat membantu. Kita akan fokus pada permintaan terlebih dahulu, seperti yang ditunjukkan berikutnya. Permintaan merangkum model yang dimaksud, pesan, dan suhu.

**Daftar 2.4** Permintaan penyelesaian obrolan
```python
response = client.chat.completions.create(
    model="gpt-4-1106-preview",                #1
    messages=[{"role": "system", 
"content": "You are a helpful assistant."},                    #2
              {"role": "user", "content": user_message}],     #3
    temperature=0.7,    #4
    )
```
* #1 Model atau penerapan yang digunakan untuk menanggapi permintaan
* #2 Pesan peran sistem
* #3 Pesan peran pengguna
* #4 Suhu atau variabilitas permintaan

Di dalam permintaan, blok `messages` menjelaskan sekumpulan pesan dan peran yang digunakan dalam permintaan. Pesan untuk model penyelesaian obrolan dapat didefinisikan dalam tiga peran:

- *Peran sistem* —Pesan yang menjelaskan aturan dan pedoman permintaan. Ini sering dapat digunakan untuk menggambarkan peran LLM dalam membuat permintaan.
- *Peran pengguna* —Mewakili dan berisi pesan dari pengguna.
- *Peran asisten* —Dapat digunakan untuk menangkap riwayat pesan dari respons sebelumnya dari LLM. Ini juga dapat menyuntikkan riwayat pesan ketika mungkin tidak ada.

Pesan yang dikirim dalam satu permintaan dapat merangkum seluruh percakapan, seperti yang ditunjukkan dalam JSON di daftar berikut.

**Daftar 2.5** Pesan dengan riwayat
```json
[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What is the capital of France?"
    },
    {
        "role": "assistant",
        "content": "The capital of France is Paris."
    },
    {
        "role": "user",
        "content": "What is an interesting fact of Paris."
    }
],
```

Anda dapat melihat bagaimana ini dapat diterapkan dengan membuka `message_history.py` di VS Code dan men-debugnya dengan menekan F5. Setelah file berjalan, pastikan untuk memeriksa output. Kemudian, coba jalankan sampel beberapa kali lagi untuk melihat bagaimana hasilnya berubah.

Hasilnya akan berubah dari setiap proses ke proses berikutnya karena suhu `.7` yang tinggi. Silakan kurangi suhu menjadi `.0`, dan jalankan sampel `message_history.py` beberapa kali lagi. Menjaga suhu di `0` akan menunjukkan hasil yang sama atau serupa setiap saat.

Menyetel suhu permintaan akan sering bergantung pada kasus penggunaan khusus Anda. Terkadang, Anda mungkin ingin membatasi sifat stokastik (keacakan) respons. Mengurangi suhu ke `0` akan memberikan hasil yang konsisten. Demikian juga, nilai `1.0` akan memberikan variabilitas paling besar dalam respons.

Selanjutnya, kita juga ingin tahu informasi apa yang dikembalikan untuk setiap permintaan. Daftar berikutnya menunjukkan format output untuk respons. Anda dapat melihat output ini dengan menjalankan file `message_history.py` di VS Code.

**Daftar 2.6** Respons penyelesaian obrolan
```json
{
    "id": "chatcmpl-8WWL23up3IRfK1nrDFQ3EHQfhx0U6",
    "choices": [                                     #1
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "… omitted",
                "role": "assistant",      #2
                "function_call": null,
                "tool_calls": null
            },
            "logprobs": null
        }
    ],
    "created": 1702761496,
    "model": "gpt-4-1106-preview",    #3
    "object": "chat.completion",
    "system_fingerprint": "fp_3905aa4f79",
    "usage": {
        "completion_tokens": 78,    #4
        "prompt_tokens": 48,         #4
        "total_tokens": 126          #4
    }
}
```
* #1 Sebuah model dapat mengembalikan lebih dari satu respons.
* #2 Respons dikembalikan dalam peran asisten
* #3 Menunjukkan model yang digunakan
* #4 Menghitung jumlah token input (prompt) dan output (penyelesaian) yang digunakan

Sangat membantu untuk melacak jumlah *token input* (yang digunakan dalam prompt) dan *token output* (jumlah yang dikembalikan melalui penyelesaian). Terkadang, meminimalkan dan mengurangi jumlah token bisa menjadi penting. Memiliki lebih sedikit token biasanya berarti interaksi LLM akan lebih murah, merespons lebih cepat, dan menghasilkan hasil yang lebih baik dan lebih konsisten.

Itu mencakup dasar-dasar menghubungkan ke LLM dan mengembalikan respons. Sepanjang buku ini, kita akan meninjau dan memperluas cara berinteraksi dengan LLM. Sampai saat itu, kita akan menjelajahi di bagian selanjutnya cara memuat dan menggunakan LLM sumber terbuka.

## 2.2 Menjelajahi LLM sumber terbuka dengan LM Studio

LLM komersial, seperti GPT-4 dari OpenAI, adalah tempat yang sangat baik untuk memulai untuk mempelajari cara menggunakan AI modern dan membangun agen. Namun, agen komersial adalah sumber daya eksternal yang menimbulkan biaya, mengurangi privasi dan keamanan data, serta menimbulkan ketergantungan. Pengaruh eksternal lainnya dapat semakin mempersulit faktor-faktor ini.

Tidak mengherankan jika perlombaan untuk membangun LLM sumber terbuka yang sebanding semakin kompetitif setiap hari. Akibatnya, sekarang ada LLM sumber terbuka yang mungkin memadai untuk banyak tugas dan sistem agen. Bahkan ada begitu banyak kemajuan dalam peralatan hanya dalam setahun sehingga hosting LLM secara lokal sekarang sangat mudah, seperti yang akan kita lihat di bagian selanjutnya.

### 2.2.1 Menginstal dan menjalankan LM Studio

LM Studio adalah unduhan gratis yang mendukung pengunduhan dan hosting LLM dan model lain secara lokal untuk Windows, Mac, dan Linux. Perangkat lunak ini mudah digunakan dan menawarkan beberapa fitur bermanfaat untuk membantu Anda memulai dengan cepat. Berikut adalah ringkasan singkat langkah-langkah untuk mengunduh dan menyiapkan LM Studio:

1. Unduh LM Studio dari https://lmstudio.ai/.
2. Setelah mengunduh, instal perangkat lunak sesuai sistem operasi Anda. Perlu diketahui bahwa beberapa versi LM Studio mungkin masih dalam versi beta dan memerlukan penginstalan alat atau pustaka tambahan.
3. Luncurkan perangkat lunak.

Gambar 2.3 menunjukkan jendela LM Studio sedang berjalan. Dari sana, Anda dapat meninjau daftar model populer saat ini, mencari model lain, dan bahkan mengunduh. Konten halaman beranda dapat sangat berguna untuk memahami detail dan spesifikasi model teratas.

![Gambar 2.3](Images/2-3.png "Perangkat lunak LM Studio yang menampilkan halaman beranda utama")

Fitur menarik dari LM Studio adalah kemampuannya untuk menganalisis perangkat keras Anda dan menyelaraskannya dengan persyaratan model tertentu. Perangkat lunak akan memberi tahu Anda seberapa baik Anda dapat menjalankan model tertentu. Ini bisa menjadi penghemat waktu yang hebat dalam memandu model apa yang Anda eksperimenkan.

Masukkan beberapa teks untuk mencari model, dan klik Go. Anda akan dibawa ke antarmuka halaman pencarian, seperti yang ditunjukkan pada gambar 2.4. Dari halaman ini, Anda dapat melihat semua variasi model dan spesifikasi lainnya, seperti ukuran token konteks. Setelah Anda mengklik tombol Compatibility Guess, perangkat lunak bahkan akan memberi tahu Anda apakah model tersebut akan berjalan di sistem Anda.

![Gambar 2.4](Images/2-4.png "Halaman pencarian LM Studio")

Klik untuk mengunduh model apa pun yang akan berjalan di sistem Anda. Anda mungkin ingin tetap menggunakan model yang dirancang untuk penyelesaian obrolan, tetapi jika sistem Anda terbatas, bekerjalah dengan apa yang Anda miliki. Selain itu, jika Anda tidak yakin model mana yang akan digunakan, silakan unduh untuk mencobanya. LM Studio adalah cara yang bagus untuk menjelajahi dan bereksperimen dengan banyak model.

Setelah model diunduh, Anda kemudian dapat memuat dan menjalankan model di halaman obrolan atau sebagai server di halaman server. Gambar 2.5 menunjukkan pemuatan dan menjalankan model di halaman obrolan. Ini juga menunjukkan opsi untuk mengaktifkan dan menggunakan GPU jika Anda memilikinya.

![Gambar 2.5](Images/2-5.png "Halaman obrolan LM Studio dengan LLM yang dimuat dan berjalan secara lokal")

Untuk memuat dan menjalankan model, buka menu tarik-turun di bagian tengah atas halaman, dan pilih model yang diunduh. Bilah kemajuan akan muncul menunjukkan pemuatan model, dan ketika sudah siap, Anda dapat mulai mengetik ke UI.

Perangkat lunak bahkan memungkinkan Anda untuk menggunakan sebagian atau semua GPU Anda, jika terdeteksi, untuk inferensi model. GPU umumnya akan mempercepat waktu respons model dalam beberapa kapasitas. Anda dapat melihat bagaimana penambahan GPU dapat memengaruhi kinerja model dengan melihat status kinerja di bagian bawah halaman, seperti yang ditunjukkan pada gambar 2.5.

Mengobrol dengan model dan menggunakan atau bermain dengan berbagai prompt dapat membantu Anda menentukan seberapa baik model akan bekerja untuk kasus penggunaan Anda. Pendekatan yang lebih sistematis adalah menggunakan alat alur prompt untuk mengevaluasi prompt dan LLM. Kita akan menjelaskan cara menggunakan alur prompt di bab 9.

LM Studio juga memungkinkan model dijalankan di server dan diakses menggunakan paket OpenAI. Kita akan melihat cara menggunakan fitur server dan menyajikan model di bagian selanjutnya.

### 2.2.2 Menyajikan LLM secara lokal dengan LM Studio

Menjalankan LLM secara lokal sebagai server mudah dengan LM Studio. Cukup buka halaman server, muat model, lalu klik tombol Mulai Server, seperti yang ditunjukkan pada gambar 2.6. Dari sana, Anda dapat menyalin dan menempel salah satu contoh untuk terhubung dengan model Anda.

![Gambar 2.6](Images/2-6.png "Halaman server LM Studio dan server yang menjalankan LLM")

Anda dapat meninjau contoh kode Python dengan membuka `chapter_2/lmstudio_ server.py` di VS Code. Kode ini juga ditunjukkan di sini pada daftar 2.7. Kemudian, jalankan kode di debugger VS Code (tekan F5).

**Daftar 2.7** `lmstudio_server.py` 
```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model",                          #1
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}      #2
  ],
  temperature=0.7,
)

print(completion.choices[0].message)     #3
```
* #1 Saat ini tidak digunakan; bisa apa saja
* #2 Jangan ragu untuk mengubah pesan sesuka Anda.
* #3 Kode default mengeluarkan seluruh pesan.

Jika Anda mengalami masalah saat menyambung ke server atau mengalami masalah lain, pastikan konfigurasi Anda untuk Pengaturan Model Server cocok dengan jenis model. Misalnya, pada gambar 2.6, yang ditampilkan sebelumnya, model yang dimuat berbeda dari pengaturan server. Pengaturan yang diperbaiki ditunjukkan pada gambar 2.7.

![Gambar 2.7](Images/2-7.png "Memilih Pengaturan Model Server yang benar untuk model yang dimuat")

Sekarang, Anda dapat menggunakan LLM yang dihosting secara lokal atau model komersial untuk membangun, menguji, dan bahkan mungkin menjalankan agen Anda. Bagian berikut akan membahas cara membangun prompt dengan lebih efektif menggunakan rekayasa prompt.

## 2.3 Mendorong LLM dengan rekayasa prompt

Prompt yang didefinisikan untuk LLM adalah konten pesan yang digunakan dalam permintaan untuk output respons yang lebih baik. *Rekayasa prompt* adalah bidang baru dan berkembang yang mencoba menyusun metodologi untuk membangun prompt. Sayangnya, pembuatan prompt bukanlah ilmu yang mapan, dan ada serangkaian metode yang berkembang dan beragam yang didefinisikan sebagai rekayasa prompt.

Untungnya, organisasi seperti OpenAI telah mulai mendokumentasikan serangkaian strategi universal, seperti yang ditunjukkan pada gambar 2.8. Strategi-strategi ini mencakup berbagai taktik, beberapa di antaranya memerlukan infrastruktur dan pertimbangan tambahan. Dengan demikian, strategi rekayasa prompt yang berkaitan dengan konsep yang lebih maju akan dibahas dalam bab-bab yang ditunjukkan.

![Gambar 2.8](Images/2-8.png "Strategi rekayasa prompt OpenAI yang ditinjau dalam buku ini, berdasarkan lokasi bab")

Setiap strategi pada gambar 2.8 diuraikan menjadi taktik-taktik yang dapat lebih jauh menyempurnakan metode spesifik rekayasa prompt. Bab ini akan membahas strategi dasar Tulis Instruksi yang Jelas. Gambar 2.9 menunjukkan taktik-taktik untuk strategi ini secara lebih rinci, beserta contoh untuk setiap taktik. Kita akan melihat cara menjalankan contoh-contoh ini menggunakan demo kode di bagian berikut.

![Gambar 2.9](Images/2-9.png "Taktik-taktik untuk strategi Tulis Instruksi yang Jelas")

Strategi Tulis Instruksi yang Jelas adalah tentang berhati-hati dan spesifik tentang apa yang Anda minta. Meminta LLM untuk melakukan tugas tidak berbeda dengan meminta seseorang untuk menyelesaikan tugas yang sama. Umumnya, semakin banyak informasi dan konteks yang relevan dengan tugas yang dapat Anda tentukan dalam permintaan, semakin baik responsnya.

Strategi ini telah dipecah menjadi taktik-taktik spesifik yang dapat Anda terapkan pada prompt. Untuk memahami cara menggunakannya, demo kode (`prompt_engineering.py`) dengan berbagai contoh prompt ada di folder kode sumber `bab 2`.

Buka file `prompt_engineering.py` di VS Code, seperti yang ditunjukkan pada daftar 2.8. Kode ini dimulai dengan memuat semua file JSON Lines di folder `prompts`. Kemudian, ia menampilkan daftar file sebagai pilihan dan memungkinkan pengguna untuk memilih opsi prompt. Setelah memilih opsi, prompt dikirimkan ke LLM, dan respons dicetak.

**Daftar 2.8** `prompt_engineering.py` `(main())`
```python
def main():
    directory = "prompts"
    text_files = list_text_files_in_directory(directory)   #1

    if not text_files:
        print("No text files found in the directory.")
        return

    def print_available():                                    #2
        print("Available prompt tactics:")
        for i, filename in enumerate(text_files, start=1):
            print(f"{i}. {filename}")

    while True:
        try:
            print_available()                   #2              
            choice = int(input("Enter … 0 to exit): "))          #3
            if choice == 0:
                break
            elif 1 <= choice <= len(text_files):
                selected_file = text_files[choice - 1]
                file_path = os.path.join(directory,
      selected_file)
                prompts = 
 ↪ load_and_parse_json_file(file_path)                         #4
                print(f"Running prompts for {selected_file}")
                for i, prompt in enumerate(prompts):
                    print(f"PROMPT {i+1} --------------------")
                    print(prompt)
                    print(f"REPLY ---------------------------")
                    print(prompt_llm(prompt))                      #5
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
```
* #1 Mengumpulkan semua file untuk folder yang diberikan
* #2 Mencetak daftar file sebagai pilihan
* #3 Memasukkan pilihan pengguna
* #4 Memuat prompt dan mengurainya menjadi pesan
* #5 Mengirimkan prompt ke OpenAI LLM

Bagian yang dikomentari dari daftar menunjukkan cara terhubung ke LLM lokal. Ini akan memungkinkan Anda untuk menjelajahi taktik rekayasa prompt yang sama yang diterapkan pada LLM sumber terbuka yang berjalan secara lokal. Secara default, contoh ini menggunakan model OpenAI yang telah kita konfigurasikan sebelumnya di bagian 2.1.1. Jika Anda belum menyelesaikannya sebelumnya, silakan kembali dan lakukan sebelum menjalankan yang ini.

Gambar 2.10 menunjukkan output dari menjalankan penguji taktik rekayasa prompt, file `prompt_engineering.py` di VS Code. Saat Anda menjalankan penguji, Anda dapat memasukkan nilai untuk taktik yang ingin Anda uji dan menontonnya berjalan.

![Gambar 2.10](Images/2-10.png "Output dari penguji taktik rekayasa prompt")

Di bagian berikut, kita akan membahas setiap taktik prompt secara lebih rinci. Kita juga akan memeriksa berbagai contoh.

### 2.3.1 Membuat kueri terperinci

Premis dasar dari taktik ini adalah memberikan detail sebanyak mungkin tetapi juga berhati-hati untuk tidak memberikan detail yang tidak relevan. Daftar berikut menunjukkan contoh file JSON Lines untuk menjelajahi taktik ini.

**Daftar 2.9** `detailed_queries.jsonl` 
```json
[                       #1
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What is an agent?"     #2
    }
]
[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": """
What is a GPT Agent? 
Please give me 3 examples of a GPT agent
"""                                       #3
    }
]
```
* #1 Contoh pertama tidak menggunakan kueri terperinci.
* #2 Pertama ajukan pertanyaan yang sangat umum kepada LLM.
* #3 Ajukan pertanyaan yang lebih spesifik, dan minta contoh.

Contoh ini menunjukkan perbedaan antara menggunakan kueri terperinci dan tidak. Ini juga melangkah lebih jauh dengan meminta contoh. Ingat, semakin banyak relevansi dan konteks yang dapat Anda berikan dalam prompt Anda, semakin baik respons keseluruhannya. Meminta contoh adalah cara lain untuk memperkuat hubungan antara pertanyaan dan output yang diharapkan.

### 2.3.2 Mengadopsi persona

Mengadopsi persona memberikan kemampuan untuk mendefinisikan konteks atau seperangkat aturan yang menyeluruh untuk LLM. LLM kemudian dapat menggunakan konteks dan/atau aturan tersebut untuk membingkai semua respons output selanjutnya. Ini adalah taktik yang menarik dan akan sering kita gunakan di sepanjang buku ini.

Daftar 2.10 menunjukkan contoh penggunaan dua persona untuk menjawab pertanyaan yang sama. Ini bisa menjadi teknik yang menyenangkan untuk menjelajahi berbagai aplikasi baru, mulai dari mendapatkan umpan balik demografis hingga berspesialisasi dalam tugas tertentu atau bahkan *rubber ducking*.

> **GPT rubber ducking**
> 
> *Rubber ducking* adalah teknik pemecahan masalah di mana seseorang menjelaskan masalah kepada benda mati, seperti bebek karet, untuk memahami atau menemukan solusi. Metode ini lazim dalam pemrograman dan debugging, karena mengartikulasikan masalah dengan keras sering kali membantu memperjelas masalah dan dapat menghasilkan wawasan atau solusi baru.
> 
> GPT rubber ducking menggunakan teknik yang sama, tetapi alih-alih benda mati, kita menggunakan LLM. Strategi ini dapat diperluas lebih lanjut dengan memberikan persona LLM yang spesifik untuk domain solusi yang diinginkan.

**Daftar 2.10** `adopting_personas.jsonl` 
```json
[
    {
        "role": "system",
        "content": """
You are a 20 year old female who attends college 
in computer science. Answer all your replies as 
a junior programmer.
"""                        #1
    },
    {
        "role": "user",
        "content": "What is the best subject to study."
    }
]
[
    {
        "role": "system",
        "content": """
You are a 38 year old male registered nurse. 
Answer all replies as a medical professional.
"""                                            #2
    },
    {
        "role": "user",
        "content": "What is the best subject to study."
    }
]
```
* #1 Persona pertama
* #2 Persona kedua

Elemen inti dari profil agen adalah persona. Kita akan menggunakan berbagai persona untuk membantu agen dalam menyelesaikan tugas mereka. Saat Anda menjalankan taktik ini, perhatikan secara khusus cara LLM mengeluarkan respons.

### 2.3.3 Menggunakan pembatas

Pembatas adalah cara yang berguna untuk mengisolasi dan membuat LLM fokus pada beberapa bagian dari sebuah pesan. Taktik ini sering digabungkan dengan taktik lain tetapi dapat bekerja dengan baik secara independen. Daftar berikut menunjukkan dua contoh, tetapi ada beberapa cara lain untuk menggambarkan pembatas, dari tag XML hingga menggunakan markdown.

**Daftar 2.11** `using_delimiters.jsonl` 
```json
[
    {
        "role": "system",
        "content": """
Summarize the text delimited by triple quotes 
with a haiku.
"""              #1
    },
    {
        "role": "user",
        "content": "A gold chain is cool '''but a silver chain is better'''"
    }
]
[
    {
        "role": "system",
        "content": """
You will be provided with a pair of statements 
(delimited with XML tags) about the same topic. 
First summarize the arguments of each statement. 
Then indicate which of them makes a better statement
 and explain why.
"""                       #2
    },
    {
        "role": "user",
        "content": """
<statement>gold chains are cool</statement>
<statement>silver chains are better</statement>
"""
    }
]
```
* #1 Pembatas didefinisikan oleh jenis karakter dan pengulangan.
* #2 Pembatas didefinisikan oleh standar XML.

Saat Anda menjalankan taktik ini, perhatikan bagian-bagian teks yang menjadi fokus LLM saat mengeluarkan respons. Taktik ini dapat bermanfaat untuk menggambarkan informasi dalam hierarki atau pola hubungan lainnya.

### 2.3.4 Menentukan langkah-langkah

Menentukan langkah-langkah adalah taktik kuat lainnya yang dapat memiliki banyak kegunaan, termasuk pada agen, seperti yang ditunjukkan pada daftar 2.12. Ini sangat kuat saat mengembangkan prompt atau profil agen untuk tugas multi-langkah yang kompleks. Anda dapat menentukan langkah-langkah untuk memecah prompt kompleks ini menjadi proses langkah demi langkah yang dapat diikuti oleh LLM. Pada gilirannya, langkah-langkah ini dapat memandu LLM melalui berbagai interaksi selama percakapan yang lebih panjang dan banyak iterasi.

**Daftar 2.12** `specifying_steps.jsonl` 
```json
[
    {
        "role": "system",
        "content": """
Use the following step-by-step instructions to respond to user inputs.
Step 1 - The user will provide you with text in triple single quotes. 
Summarize this text in one sentence with a prefix that says 'Summary: '.
Step 2 - Translate the summary from Step 1 into Spanish, 
with a prefix that says 'Translation: '.
"""                                         #1
    },
    {
        "role": "user",
        "content": "'''I am hungry and would like to order an appetizer.'''"
    }
]
[
    {
        "role": "system",
        "content": """
Use the following step-by-step instructions to respond to user inputs.
Step 1 - The user will provide you with text. Answer any questions in 
the text in one sentence with a prefix that says 'Answer: '.

Step 2 - Translate the Answer from Step 1 into a dad joke,
 with a prefix that says 'Dad Joke: '."""                     #2
    },
    {
        "role": "user",
        "content": "What is the tallest structure in Paris?"
    }
]
```
* #1 Perhatikan taktik menggunakan pembatas.
* #2 Langkah-langkah dapat berupa operasi yang sama sekali berbeda.

### 2.3.5 Memberikan contoh

Memberikan contoh adalah cara terbaik untuk memandu output yang diinginkan dari LLM. Ada banyak cara untuk menunjukkan contoh kepada LLM. Pesan/prompt sistem dapat menjadi cara yang membantu untuk menekankan output umum. Dalam daftar berikut, contoh ditambahkan sebagai balasan asisten LLM terakhir, dengan prompt "Ajari saya tentang Python."

**Daftar 2.13** `providing_examples.jsonl` 
```json
[
    {
        "role": "system",
        "content": """
Answer all replies in a consistent style that follows the format, 
length and style of your previous responses.
Example:
  user:
       Teach me about Python.
  assistant:                                               #1
       Python is a programming language developed in 1989
 by Guido van Rossum.

   Future replies:
       The response was only a sentence so limit
 all future replies to a single sentence.
"""                                          #2
    },
    {
        "role": "user",
        "content": "Teach me about Java."
    }
]
```
* #1 Menyuntikkan output sampel sebagai balasan asisten "sebelumnya"
* #2 Menambahkan taktik batas output untuk membatasi ukuran output dan mencocokkan contoh

Memberikan contoh juga dapat digunakan untuk meminta format output tertentu dari serangkaian tugas kompleks yang menghasilkan output. Misalnya, meminta LLM untuk menghasilkan kode yang cocok dengan output sampel adalah penggunaan contoh yang sangat baik. Kami akan menggunakan taktik ini di seluruh buku, tetapi ada metode lain untuk memandu output.

### 2.3.6 Menentukan panjang output

Taktik menentukan panjang output dapat membantu tidak hanya dalam membatasi token tetapi juga dalam memandu output ke format yang diinginkan. Daftar 2.14 menunjukkan contoh penggunaan dua teknik berbeda untuk taktik ini. Yang pertama membatasi output hingga kurang dari 10 kata. Ini dapat memiliki manfaat tambahan untuk membuat respons lebih ringkas dan terarah, yang dapat diinginkan untuk beberapa kasus penggunaan. Contoh kedua menunjukkan pembatasan output ke satu set poin-poin yang ringkas. Metode ini dapat membantu mempersempit output dan menjaga jawaban tetap singkat. Jawaban yang lebih ringkas umumnya berarti output lebih terfokus dan mengandung lebih sedikit pengisi.

**Daftar 2.14** `specifying_output_length.jsonl` 
```json
[
    {
        "role": "system",
        "content": """
Summarize all replies into 10 or fewer words.
"""                                              #1
    },
    {
        "role": "user",
        "content": "Please tell me an exciting fact about Paris?"
    }
]
[
    {
        "role": "system",
        "content": """
Summarize all replies into 3 bullet points.
"""                                          #2
    },
    {
        "role": "user",
        "content": "Please tell me an exciting fact about Paris?"
    }
]
```
* #1 Membatasi output membuat jawaban lebih ringkas.
* #2 Membatasi jawaban menjadi satu set poin singkat

Menjaga jawaban tetap singkat dapat memiliki manfaat tambahan saat mengembangkan sistem multi-agen. Setiap sistem agen yang bercakap-cakap dengan agen lain dapat memperoleh manfaat dari balasan yang lebih ringkas dan terfokus. Ini cenderung menjaga LLM lebih fokus dan mengurangi komunikasi yang bising.

Pastikan untuk menjalankan semua contoh taktik prompt untuk strategi ini. Seperti yang disebutkan, kita akan membahas strategi dan taktik rekayasa prompt lainnya di bab-bab mendatang. Kita akan menyelesaikan bab ini dengan melihat cara memilih LLM terbaik untuk kasus penggunaan Anda.

## 2.4 Memilih LLM yang optimal untuk kebutuhan spesifik Anda

Meskipun menjadi perajin agen AI yang sukses tidak memerlukan pemahaman mendalam tentang LLM, ada baiknya untuk dapat mengevaluasi spesifikasinya. Seperti pengguna komputer, Anda tidak perlu tahu cara membuat prosesor untuk memahami perbedaan model prosesor. Analogi ini berlaku baik untuk LLM, dan meskipun kriterianya mungkin berbeda, itu masih tergantung pada beberapa pertimbangan utama.

Dari diskusi kita sebelumnya dan melihat LM Studio, kita dapat mengekstrak beberapa kriteria mendasar yang akan penting bagi kita saat mempertimbangkan LLM. Gambar 2.11 menjelaskan kriteria penting untuk menentukan apa yang membuat LLM layak dipertimbangkan untuk membuat agen GPT atau tugas LLM apa pun.

![Gambar 2.11](Images/2-11.png "Kriteria penting untuk dipertimbangkan saat menggunakan LLM")

Untuk tujuan kita membangun agen AI, kita perlu melihat setiap kriteria ini dalam kaitannya dengan tugas. Ukuran dan kecepatan konteks model dapat dianggap sebagai kriteria keenam dan ketujuh, tetapi biasanya dianggap sebagai variasi dari arsitektur dan infrastruktur penerapan model. Kriteria kedelapan yang perlu dipertimbangkan untuk LLM adalah biaya, tetapi ini tergantung pada banyak faktor lain. Berikut adalah ringkasan bagaimana kriteria ini berkaitan dengan pembangunan agen AI:

- *Kinerja model* —Anda biasanya ingin memahami kinerja LLM untuk serangkaian tugas tertentu. Misalnya, jika Anda membangun agen khusus untuk pengkodean, maka LLM yang berkinerja baik pada kode akan menjadi penting.
- *Parameter model (ukuran)* —Ukuran model sering kali merupakan indikasi yang sangat baik tentang kinerja inferensi dan seberapa baik model merespons. Namun, ukuran model juga akan menentukan persyaratan perangkat keras Anda. Jika Anda berencana menggunakan model yang dihosting secara lokal, ukuran model juga akan menentukan komputer dan GPU yang Anda butuhkan. Untungnya, kita melihat model sumber terbuka kecil yang sangat mampu dirilis secara teratur.
- *Kasus penggunaan (jenis model)* —Jenis model memiliki beberapa variasi. Model penyelesaian obrolan seperti ChatGPT efektif untuk melakukan iterasi dan penalaran melalui masalah, sedangkan model seperti penyelesaian, tanya jawab, dan instruksi lebih terkait dengan tugas-tugas tertentu. Model penyelesaian obrolan sangat penting untuk aplikasi agen, terutama yang berulang.
- *Input pelatihan* —Memahami konten yang digunakan untuk melatih model akan sering menentukan domain model. Meskipun model umum dapat efektif di berbagai tugas, model yang lebih spesifik atau disesuaikan dapat lebih relevan dengan suatu domain. Ini mungkin menjadi pertimbangan untuk agen khusus domain di mana model yang lebih kecil dan lebih disesuaikan dapat berkinerja sebaik atau lebih baik daripada model yang lebih besar seperti GPT-4.
- *Metode pelatihan* —Ini mungkin kurang menjadi perhatian, tetapi ada baiknya untuk memahami metode apa yang digunakan untuk melatih model. Bagaimana model dilatih dapat memengaruhi kemampuannya untuk menggeneralisasi, bernalar, dan merencanakan. Ini bisa menjadi penting untuk agen perencanaan tetapi mungkin kurang signifikan untuk agen daripada untuk asisten yang lebih spesifik tugas.
- *Ukuran token konteks* —Ukuran konteks model lebih spesifik untuk arsitektur dan jenis model. Ini menentukan ukuran konteks atau memori yang mungkin dipegang oleh model. Jendela konteks yang lebih kecil kurang dari 4.000 token biasanya lebih dari cukup untuk tugas-tugas sederhana. Namun, jendela konteks yang besar bisa menjadi penting saat menggunakan banyak agen—semuanya bercakap-cakap tentang suatu tugas. Model-model tersebut biasanya akan digunakan dengan variasi pada ukuran jendela konteks.
- *Kecepatan model (penerapan model)* —Kecepatan model ditentukan oleh *kecepatan inferensi* (atau seberapa cepat model membalas permintaan), yang pada gilirannya ditentukan oleh infrastruktur tempat ia berjalan. Jika agen Anda tidak berinteraksi langsung dengan pengguna, kecepatan waktu nyata mentah mungkin tidak diperlukan. Di sisi lain, agen LLM yang berinteraksi dalam waktu nyata harus secepat mungkin. Untuk model komersial, kecepatan akan ditentukan dan didukung oleh penyedia. Infrastruktur Anda akan menentukan kecepatan bagi mereka yang ingin menjalankan LLM mereka sendiri.
- *Biaya model (anggaran proyek)* —Biaya sering kali ditentukan oleh proyek. Baik belajar membangun agen atau mengimplementasikan perangkat lunak perusahaan, biaya selalu menjadi pertimbangan. Ada tradeoff signifikan antara menjalankan LLM Anda sendiri versus menggunakan API komersial.

Ada banyak hal yang perlu dipertimbangkan saat memilih model mana yang ingin Anda gunakan untuk membangun sistem agen produksi. Namun, memilih dan bekerja dengan satu model biasanya merupakan yang terbaik untuk tujuan penelitian dan pembelajaran. Jika Anda baru mengenal LLM dan agen, Anda mungkin ingin memilih opsi komersial seperti GPT-4 Turbo. Kecuali dinyatakan lain, pekerjaan dalam buku ini akan bergantung pada GPT-4 Turbo.

Seiring waktu, model niscaya akan digantikan oleh model yang lebih baik. Jadi Anda mungkin perlu memutakhirkan atau menukar model. Namun, untuk melakukan ini, Anda harus memahami metrik kinerja LLM dan agen Anda. Untungnya, di bab 9, kita akan membahas evaluasi LLM, prompt, dan profil agen dengan alur prompt.

## 2.5 Latihan

Gunakan latihan berikut untuk membantu Anda terlibat dengan materi di bab ini:

- *Latihan 1*—Mengonsumsi LLM yang Berbeda
  - *Tujuan* —Gunakan contoh kode `connecting.py` untuk menggunakan LLM yang berbeda dari OpenAI atau penyedia lain.
  - *Tugas*:
    - Ubah `connecting.py` untuk terhubung ke LLM yang berbeda.
    - Pilih LLM dari OpenAI atau penyedia lain.
    - Perbarui kunci API dan titik akhir dalam kode.
    - Jalankan kode yang dimodifikasi dan validasi responsnya.
- *Latihan 2*—Menjelajahi Taktik Rekayasa Prompt
  - *Tujuan* —Jelajahi berbagai taktik rekayasa prompt, dan buat variasi untuk masing-masing.
  - *Tugas*:
    - Tinjau taktik rekayasa prompt yang dibahas dalam bab ini.
    - Tulis variasi untuk setiap taktik, bereksperimen dengan frase dan struktur yang berbeda.
    - Uji variasi dengan LLM untuk mengamati hasil yang berbeda.
    - Dokumentasikan hasilnya, dan analisis keefektifan setiap variasi.
- *Latihan 3*—Mengunduh dan Menjalankan LLM dengan LM Studio
  - *Tujuan* —Unduh LLM menggunakan LM Studio, dan hubungkan ke taktik rekayasa prompt.
  - *Tugas*:
    - Instal LM Studio di mesin Anda.
    - Unduh LLM menggunakan LM Studio.
    - Sajikan model menggunakan LM Studio.
    - Tulis kode Python untuk terhubung ke model yang disajikan.
    - Integrasikan contoh taktik reayasa prompt dengan model yang disajikan.
- *Latihan 4*—Membandingkan LLM Komersial dan Sumber Terbuka
  - *Tujuan* —Bandingkan kinerja LLM komersial seperti GPT-4 Turbo dengan model sumber terbuka menggunakan contoh rekayasa prompt.
  - *Tugas*:
    - Terapkan contoh rekayasa prompt menggunakan GPT-4 Turbo.
    - Ulangi implementasi menggunakan LLM sumber terbuka.
    - Evaluasi model berdasarkan kriteria seperti akurasi respons, koherensi, dan kecepatan.
    - Dokumentasikan proses evaluasi, dan rangkum temuannya.
- *Latohan 5*—Alternatif Hosting untuk LLM
  - *Tujuan* —Kontraskan dan bandingkan alternatif untuk hosting LLM versus menggunakan model komersial.
  - *Tugas*:
    - Teliti opsi hosting yang berbeda untuk LLM (mis., server lokal, layanan cloud).
    - Evaluasi keuntungan dan kerugian dari setiap opsi hosting.
    - Bandingkan opsi-opsi ini dengan menggunakan model komersial dalam hal biaya, kinerja, dan kemudahan penggunaan.
    - Tulis laporan yang merangkum perbandingan dan merekomendasikan pendekatan terbaik berdasarkan kasus penggunaan tertentu.

## Ringkasan

- LLM menggunakan jenis arsitektur yang disebut generative pretrained transformers (GPT).
- Model generatif (mis., LLM dan GPT) berbeda dari model prediktif/klasifikasi dengan mempelajari cara merepresentasikan data dan tidak hanya mengklasifikasikannya.
- LLM adalah kumpulan data, arsitektur, dan pelatihan untuk kasus penggunaan tertentu, yang disebut *fine-tuning.*
- OpenAI API SDK dapat digunakan untuk terhubung ke LLM dari model, seperti GPT-4, dan juga digunakan untuk mengonsumsi LLM sumber terbuka.
- Anda dapat dengan cepat menyiapkan lingkungan Python dan menginstal paket yang diperlukan untuk integrasi LLM.
- LLM dapat menangani berbagai permintaan dan menghasilkan respons unik yang dapat digunakan для meningkatkan keterampilan pemrograman terkait integrasi LLM.
- LLM sumber terbuka adalah alternatif untuk model komersial dan dapat dihosting secara lokal menggunakan alat seperti LM Studio.
- Rekayasa prompt adalah kumpulan teknik yang membantu menyusun prompt yang lebih efektif untuk meningkatkan respons LLM.
- LLM dapat digunakan untuk mendukung agen dan asisten, dari chatbot sederhana hingga pekerja otonom yang sepenuhnya mampu.
- Memilih LLM yang paling sesuai untuk kebutuhan spesifik bergantung pada kinerja, parameter, kasus penggunaan, masukan pelatihan, dan kriteria lainnya.
- Menjalankan LLM secara lokal memerlukan berbagai keterampilan, mulai dari menyiapkan GPU hingga memahami berbagai opsi konfigurasi.
