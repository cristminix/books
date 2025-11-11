# 4 Menjelajahi sistem multi-agen

## Bab ini mencakup
* Membangun sistem multi-agen menggunakan AutoGen Studio 
* Membangun sistem multi-agen sederhana
* Membuat agen yang dapat bekerja secara kolaboratif melalui obrolan grup
* Membangun kru agen dan sistem multi-agen menggunakan CrewAI
* Memperluas jumlah agen dan menjelajahi pola pemrosesan dengan CrewAI 

Sekarang mari kita melakukan perjalanan dari AutoGen ke CrewAI, dua platform multi-agen yang sudah mapan. Kita akan mulai dengan AutoGen, sebuah proyek Microsoft yang mendukung banyak agen dan menyediakan studio untuk bekerja dengan mereka. Kita akan menjelajahi sebuah proyek dari Microsoft bernama AutoGen, yang mendukung banyak agen tetapi juga menyediakan studio untuk memudahkan Anda bekerja dengan agen. Dari sana, kita akan lebih banyak praktik langsung mengkodekan agen AutoGen untuk menyelesaikan tugas menggunakan percakapan dan kolaborasi obrolan grup. 

Kemudian, kita akan beralih ke CrewAI, sistem agen perusahaan yang diusulkan sendiri yang mengambil pendekatan berbeda. CrewAI menyeimbangkan agen berbasis peran dan otonom yang dapat menjadi sistem manajemen tugas yang fleksibel secara berurutan atau hierarkis. Kita akan menjelajahi bagaimana CrewAI dapat memecahkan masalah yang beragam dan kompleks.

Sistem multi-agen menggabungkan banyak alat yang sama yang digunakan sistem agen tunggal tetapi mendapat manfaat dari kemampuan untuk memberikan umpan balik dan evaluasi dari luar kepada agen lain. Kemampuan untuk mendukung dan mengkritik solusi agen secara internal memberikan kekuatan lebih pada sistem multi-agen. Kita akan menjelajahi pengantar sistem multi-agen, dimulai dengan AutoGen Studio di bagian selanjutnya.

## Memperkenalkan sistem multi-agen dengan AutoGen Studio

AutoGen Studio adalah alat yang ampuh yang menggunakan banyak agen di belakang layar untuk menyelesaikan tugas dan masalah yang diarahkan pengguna. Alat ini telah digunakan untuk mengembangkan beberapa kode yang lebih kompleks dalam buku ini. Untuk alasan itu dan lainnya, ini adalah pengantar yang sangat baik untuk sistem multi-agen praktis.

Gambar 4.1 menunjukkan diagram skematik dari pola koneksi/komunikasi agen yang digunakan AutoGen. AutoGen adalah platform multi-agen percakapan karena komunikasi dilakukan menggunakan bahasa alami. Percakapan bahasa alami tampaknya menjadi pola paling alami bagi agen untuk berkomunikasi, tetapi itu bukan satu-satunya metode, seperti yang akan Anda lihat nanti.

![Gambar 4.1](Images/4-1.png)

Gambar 4.1 Bagaimana agen AutoGen berkomunikasi melalui percakapan (Sumber: AutoGen)

AutoGen mendukung berbagai pola percakapan, dari grup dan hierarkis hingga komunikasi proksi yang lebih umum dan lebih sederhana. Dalam komunikasi proksi, satu agen bertindak sebagai proksi dan mengarahkan komunikasi ke agen yang relevan untuk menyelesaikan tugas. Proksi mirip dengan pelayan yang menerima pesanan dan mengirimkannya ke dapur, yang memasak makanan. Kemudian, pelayan menyajikan makanan yang sudah dimasak.

Pola dasar di AutoGen menggunakan `UserProxy` dan satu atau lebih agen asisten. Gambar 4.2 menunjukkan proksi pengguna menerima arahan dari manusia dan kemudian mengarahkan agen asisten yang diaktifkan untuk menulis kode untuk melakukan tugas. Setiap kali asisten menyelesaikan tugas, agen proksi meninjau, mengevaluasi, dan memberikan umpan balik kepada asisten. Loop iterasi ini berlanjut hingga proksi puas dengan hasilnya.

![Gambar 4.2](Images/4-2.png)

Gambar 4.2 Komunikasi agen proksi pengguna dan agen asisten (Sumber: AutoGen)

Manfaat proksi adalah ia bekerja untuk menggantikan umpan balik dan evaluasi manusia yang diperlukan, dan, dalam banyak kasus, ia melakukan pekerjaan dengan baik. Meskipun tidak menghilangkan kebutuhan akan umpan balik dan evaluasi manusia, ia menghasilkan hasil yang jauh lebih lengkap secara keseluruhan. Dan, meskipun loop iterasi memakan waktu, itu adalah waktu yang bisa Anda gunakan untuk minum kopi atau mengerjakan tugas lain.

AutoGen Studio adalah alat yang dikembangkan oleh tim AutoGen yang memberikan pengantar yang bermanfaat untuk agen yang dapat diajak bicara. Dalam latihan berikutnya, kita akan menginstal Studio dan menjalankan beberapa eksperimen untuk melihat seberapa baik kinerja platform. Alat-alat ini masih dalam siklus pengembangan yang cepat, jadi jika Anda mengalami masalah, lihat dokumentasi di repositori GitHub AutoGen.

### Menginstal dan menggunakan AutoGen Studio

Buka folder `chapter_04` di Visual Studio Code (VS Code), buat lingkungan virtual Python lokal, dan instal file `requirements.txt`. Jika Anda memerlukan bantuan untuk ini, lihat apendiks B untuk menginstal semua persyaratan latihan bab ini.

Buka terminal di VS Code (Ctrl-`, Cmd-`) yang menunjuk ke lingkungan virtual Anda, dan jalankan AutoGen Studio menggunakan perintah yang ditunjukkan pada daftar 4.1. Anda harus terlebih dahulu menentukan variabel lingkungan untuk kunci OpenAI Anda. Karena port 8080 dan 8081 populer, dan jika Anda memiliki layanan lain yang berjalan, ubah port ke 8082 atau sesuatu yang Anda pilih.

**Daftar 4.1** Meluncurkan AutoGen Studio 

```
# atur variabel lingkungan di Bash (Git Bash)
ekspor OPENAI_API_KEY="<kunci API Anda>"         #1

# variabel lingkungan yang dikirim dengan PowerShell
$env:VAR_NAME ="<kunci API Anda>"                #1

autogenstudio ui --port 8081    #2
```

1. Gunakan perintah yang sesuai untuk jenis terminal Anda.
2. Ubah port jika Anda mengharapkan atau mengalami konflik di mesin Anda.

Arahkan browser Anda ke antarmuka AutoGen Studio yang ditunjukkan pada gambar 4.3 (pada saat penulisan ini). Meskipun mungkin ada perbedaan, satu hal yang pasti: antarmuka utama akan tetap berupa obrolan. Masukkan tugas kompleks yang memerlukan pengkodean. Contoh yang digunakan di sini adalah `Buat` `plot` `yang menunjukkan` `popularitas` `istilah` `Agen` `GPT` `dalam` `pencarian` `Google.`

![Gambar 4.3](Images/4-3.png)

Gambar 4.3 Memasukkan tugas untuk dikerjakan agen di antarmuka AutoGen

Asisten agen menghasilkan cuplikan kode untuk melakukan atau menyelesaikan berbagai subtugas saat agen bekerja sama melalui tugas dalam contoh. Agen proksi pengguna kemudian mencoba menjalankan cuplikan kode tersebut dan menilai outputnya. Dalam banyak kasus, membuktikan bahwa kode berjalan dan menghasilkan output yang diperlukan sudah cukup bagi agen proksi pengguna untuk menyetujui penyelesaian tugas.

Jika Anda mengalami masalah dengan permintaan agen asisten, minta agen proksi untuk mencoba metode yang berbeda atau masalah lain. Ini menyoroti masalah yang lebih besar dengan sistem agen yang menggunakan paket atau pustaka yang telah kedaluwarsa dan tidak lagi berfungsi. Untuk alasan ini, umumnya lebih baik membuat agen menjalankan tindakan daripada membangun kode untuk melakukan tindakan sebagai alat.

> **Kiat** Menjalankan AutoGen dan AutoGen Studio menggunakan Docker disarankan, terutama saat bekerja dengan kode yang dapat memengaruhi sistem operasi. Docker dapat mengisolasi dan memvirtualisasikan lingkungan agen, sehingga mengisolasi kode yang berpotensi berbahaya. Menggunakan Docker dapat membantu meringankan jendela atau situs web sekunder apa pun yang dapat memblokir proses agen agar tidak berjalan. 

Gambar 4.4 menunjukkan penyelesaian tugas oleh agen. Agen proksi akan mengumpulkan setiap cuplikan kode, gambar, atau dokumen lain yang dihasilkan dan menambahkannya ke pesan. Anda juga dapat meninjau percakapan agen dengan membuka perluasan Pesan Agen. Dalam banyak kasus, jika Anda meminta agen untuk menghasilkan plot atau aplikasi, jendela sekunder akan terbuka yang menunjukkan hasil tersebut.

![Gambar 4.4](Images/4-4.png)

Gambar 4.4 Output setelah agen menyelesaikan tugas

Luar biasanya, para agen akan melakukan sebagian besar tugas dengan baik dan menyelesaikannya dengan baik. Tergantung pada kompleksitas tugas, Anda mungkin perlu melakukan iterasi lebih lanjut dengan proksi. Terkadang, agen mungkin hanya melangkah sejauh ini untuk menyelesaikan tugas karena tidak memiliki keterampilan yang diperlukan. Di bagian selanjutnya, kita akan melihat cara menambahkan keterampilan ke agen.

### Menambahkan keterampilan di AutoGen Studio

Keterampilan dan alat, atau *tindakan,* seperti yang kita sebut dalam buku ini, adalah sarana utama di mana agen dapat memperluas diri. Tindakan memberi agen kemampuan untuk menjalankan kode, memanggil API, atau bahkan mengevaluasi dan memeriksa lebih lanjut output yang dihasilkan. AutoGen Studio saat ini dimulai hanya dengan seperangkat alat dasar untuk mengambil konten web atau menghasilkan gambar.

> **Catatan** Banyak sistem agen menggunakan praktik mengizinkan agen untuk membuat kode untuk menyelesaikan tujuan. Namun, kami menemukan bahwa kode dapat dengan mudah rusak, perlu dipelihara, dan dapat berubah dengan cepat. Oleh karena itu, seperti yang akan kita bahas di bab-bab selanjutnya, lebih baik memberikan agen keterampilan/tindakan/alat untuk memecahkan masalah. 

Dalam skenario latihan berikut, kita akan menambahkan keterampilan/tindakan untuk memeriksa gambar menggunakan model visi OpenAI. Ini akan memungkinkan agen proksi untuk memberikan umpan balik jika kita meminta asisten untuk menghasilkan gambar dengan konten tertentu.

Dengan AutoGen Studio berjalan, buka tab Bangun dan klik Keterampilan, seperti yang ditunjukkan pada gambar 4.5. Kemudian, klik tombol Keterampilan Baru untuk membuka panel kode tempat Anda dapat menyalin-tempel kode. Dari tab ini, Anda juga dapat mengonfigurasi model, agen, dan alur kerja agen.

![Gambar 4.5](Images/4-5.png)

Gambar 4.5 Langkah-langkah untuk membuat keterampilan baru di tab Bangun

Masukkan kode yang ditunjukkan pada daftar 4.2 dan juga disediakan dalam kode sumber buku sebagai `describe_image.py`. Salin dan tempel kode ini ke jendela editor, lalu klik tombol Simpan di bagian bawah.

**Daftar 4.2** `describe_image.py` 

```
import base64
import requests
import os

def describe_image(image_path='animals.png') -> str:
    """
    Menggunakan GPT-4 Vision untuk memeriksa dan mendeskripsikan konten gambar.

    :param input_path: str, nama file PNG yang akan dideskripsikan.
    """
    api_key = os.environ['OPEN_API_KEY']

    # Fungsi untuk mengkodekan gambar
    def encode_image(image_path):     #1
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    # Mendapatkan string base64
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-turbo",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Ada apa di gambar ini?"
            },
            {
            "type": "image_url",
            "image_url": {
         "url": f"data:image/jpeg;base64,{base64_image}"     #2
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload)

    return response.json()["choices"][0]["message"] #3
["content"]                                          #3
```

1. Fungsi untuk memuat dan mengkodekan gambar sebagai string Base64
2. Termasuk string gambar bersama dengan muatan JSON
3. Membongkar respons dan mengembalikan konten balasan

Fungsi `describe_image` menggunakan model visi OpenAI GPT-4 untuk mendeskripsikan apa yang ada di dalam gambar. Keterampilan ini dapat dipasangkan dengan keterampilan generate_image yang ada sebagai penilaian kualitas. Agen dapat mengonfirmasi bahwa gambar yang dihasilkan cocok dengan persyaratan pengguna.

Setelah keterampilan ditambahkan, itu harus ditambahkan ke alur kerja agen dan agen tertentu untuk digunakan. Gambar 4.6 menunjukkan penambahan keterampilan baru ke agen asisten utama dalam alur kerja agen umum atau default. 

![Gambar 4.6](Images/4-6.png)

Gambar 4.6 Mengonfigurasi agen primary_assistant dengan keterampilan baru

Sekarang setelah keterampilan ditambahkan ke asisten utama, kita dapat menugaskan agen untuk membuat gambar tertentu dan memvalidasinya menggunakan keterampilan describe_image yang baru. Karena generator gambar terkenal kesulitan dengan teks yang benar, kita akan membuat tugas latihan untuk melakukan hal itu.

Masukkan teks yang ditunjukkan pada daftar 4.3 untuk meminta agen membuat gambar sampul buku untuk buku ini. Kami akan secara eksplisit mengatakan bahwa teks harus benar dan bersikeras agar agen menggunakan fungsi `describe_image` yang baru untuk memverifikasi gambar.

**Daftar 4.3** Meminta sampul buku

```
Harap buat sampul untuk buku GPT Agents In Action, gunakan 
keterampilan describe_image untuk memastikan judul buku dieja 
dengan benar di sampul
```

Setelah prompt dimasukkan, tunggu beberapa saat, dan Anda mungkin akan melihat beberapa dialog dipertukarkan tentang proses pembuatan dan verifikasi gambar. Namun, pada akhirnya, jika semuanya berfungsi dengan benar, agen akan kembali dengan hasil yang ditunjukkan pada gambar 4.7.

![Gambar 4.7](Images/4-7.png)

Gambar 4.7 Output file yang dihasilkan dari pekerjaan agen pada tugas pembuatan gambar

Luar biasanya, koordinasi agen menyelesaikan tugas hanya dalam beberapa iterasi. Seiring dengan gambar, Anda juga dapat melihat berbagai cuplikan kode pembantu yang dihasilkan untuk membantu penyelesaian tugas. AutoGen Studio sangat mengesankan dalam kemampuannya untuk mengintegrasikan keterampilan yang dapat diadaptasi lebih lanjut oleh agen untuk menyelesaikan beberapa tujuan. Bagian berikut akan menunjukkan bagaimana agen-agen kuat ini diimplementasikan dalam kode.

## Menjelajahi AutoGen

Meskipun AutoGen Studio adalah alat yang fantastis untuk memahami sistem multi-agen, kita harus melihat ke dalam kode. Untungnya, mengkodekan beberapa contoh agen dengan AutoGen sederhana dan mudah dijalankan. Kita akan membahas penyiapan dasar AutoGen di bagian selanjutnya.

### Menginstal dan menggunakan AutoGen

Latihan berikutnya ini akan melihat pengkodean sistem multi-agen dasar yang menggunakan proksi pengguna dan agen yang dapat diajak bicara. Namun, sebelum kita melakukannya, kita ingin memastikan AutoGen diinstal dan dikonfigurasi dengan benar.

Buka terminal di VS Code, dan jalankan seluruh petunjuk instalasi bab 4 per apendiks B, atau jalankan perintah `pip` di daftar 4.4. Jika Anda telah menginstal file `requirements.txt`, Anda juga akan siap untuk menjalankan AutoGen.

**Daftar 4.4** Menginstal AutoGen

```
pip install pyautogen
```

Selanjutnya, salin `chapter_04/OAI_CONFIG_LIST.example` ke `OAI_CONFIG_LIST`, hapus `.example` dari nama file. Kemudian, buka file baru di VS Code, dan masukkan konfigurasi OpenAI atau Azure Anda di file `OAI_CONFIG_LIST` di daftar 4.5. Isi kunci API, model, dan detail lainnya sesuai persyaratan layanan API Anda. AutoGen akan bekerja dengan model apa pun yang mematuhi klien OpenAI. Itu berarti Anda dapat menggunakan LLM lokal melalui LM Studio atau layanan lain seperti Groq, Hugging Face, dan banyak lagi.

**Daftar 4.5** `OAI_CONFIG_LIST` 

```
[
    {
        "model": "gpt-4",                    #1
        "api_key": "<kunci API OpenAI Anda di sini>",           #2
        "tags": ["gpt-4", "tool"]
    },
    {
        "model": "<nama penerapan Azure OpenAI Anda>",     #3
        "api_key": "<kunci API Azure OpenAI Anda di sini>",     #4
        "base_url": "<basis API Azure OpenAI Anda di sini>",    #5
        "api_type": "azure",
        "api_version": "2024-02-15-preview"
    }    
]
```

1. Pilih model; GPT-4 direkomendasikan.
2. Gunakan kunci layanan yang biasanya Anda gunakan.
3. Pilih model; GPT-4 direkomendasikan.
4. Gunakan kunci layanan yang biasanya Anda gunakan.
5. Mengubah URL dasar memungkinkan Anda menunjuk ke layanan lain, bukan hanya Azure OpenAI.

Sekarang, kita dapat melihat kode untuk obrolan multi-agen dasar menggunakan agen `UserProxy` dan `ConversableAgent` yang sudah jadi. Buka `autogen_start.py` di VS Code, yang ditunjukkan pada daftar berikut, dan tinjau bagian-bagiannya sebelum menjalankan file.

**Daftar 4.6** `autogen_start.py` 

```
import autogen
from autogen import ConversableAgent, UserProxyAgent, config_list_from_json


    config_list = config_list_from_json(
         env_or_file="OAI_CONFIG_LIST")     #1

    asisten = ConversableAgent(
         "agen", 
         llm_config={"config_list": config_list})

    user_proxy = UserProxyAgent(     #3
         "pengguna",
         code_execution_config={
             "work_dir": "working",
             "use_docker": False,
         },
         human_input_mode="ALWAYS",
         is_termination_msg=lambda x: x.get("content", "")
         .rstrip()
         .endswith("TERMINATE"),     #4
     )
     user_proxy.initiate_chat(asisten, message="tulis solusi 
untuk fizz buzz dalam satu baris?")    #5
```

1. Memuat konfigurasi LLM Anda dari file JSON OAI_CONFIG_LIST
2. Agen ini berbicara langsung dengan LLM.
3. Agen ini menjadi perantara percakapan dari pengguna ke asisten.
4. Mengatur pesan penghentian memungkinkan agen untuk berulang.
5. Obrolan dimulai dengan asisten melalui user_proxy untuk menyelesaikan tugas.

Jalankan kode dengan menjalankan file di VS Code di debugger (F5). Kode di daftar 4.6 menggunakan tugas sederhana untuk mendemonstrasikan penulisan kode. Daftar 4.7 menunjukkan beberapa contoh untuk dipilih. Tugas pengkodean ini juga merupakan beberapa tolok ukur reguler penulis untuk menilai kekuatan LLM dalam pengkodean.

**Daftar 4.7** Contoh tugas pengkodean sederhana

```
tulis fungsi Python untuk memeriksa apakah suatu bilangan prima
kodekan permainan sname klasik menggunakan Pygame                  #1
kodekan permainan asteroid klasik dalam Python menggunakan Pygame  #1
```

1. Untuk menikmati iterasi tugas-tugas ini, gunakan Windows Subsystem for Linux (WSL) di Windows, atau gunakan Docker.

Setelah kode dimulai dalam beberapa detik, asisten akan merespons proksi dengan solusi. Pada saat ini, proksi akan meminta umpan balik dari Anda. Tekan Enter, yang pada dasarnya tidak memberikan umpan balik, dan ini akan meminta proksi untuk menjalankan kode untuk memverifikasi bahwa kode tersebut beroperasi seperti yang diharapkan. 

Luar biasanya, agen proksi bahkan akan menerima isyarat untuk menginstal paket yang diperlukan seperti Pygame. Kemudian ia akan menjalankan kode, dan Anda akan melihat output di terminal atau sebagai jendela atau browser baru. Anda dapat memainkan game atau menggunakan antarmuka jika kode tersebut membuka jendela/browser baru.

Perhatikan bahwa jendela/browser yang muncul tidak akan ditutup di Windows dan akan memerlukan keluar dari seluruh program. Untuk menghindari masalah ini, jalankan kode melalui Windows Subsystem for Linux (WSL) atau Docker. AutoGen secara eksplisit merekomendasikan penggunaan Docker untuk agen eksekusi kode, dan jika Anda merasa nyaman dengan kontainer, ini adalah pilihan yang baik.

Bagaimanapun, setelah proksi menghasilkan dan menjalankan kode, folder `working_dir` yang diatur sebelumnya di daftar 4.6 sekarang harus memiliki file Python dengan kode tersebut. Ini akan memungkinkan Anda untuk menjalankan kode sesuka Anda, membuat perubahan, atau bahkan meminta perbaikan, seperti yang akan kita lihat. Di bagian selanjutnya, kita akan melihat cara meningkatkan kemampuan agen pengkodean.

### Meningkatkan output kode dengan kritik agen

Salah satu manfaat kuat dari sistem multi-agen adalah beberapa peran/persona yang dapat Anda tetapkan secara otomatis saat menyelesaikan tugas. Menghasilkan atau membantu menulis kode dapat menjadi keuntungan yang sangat baik bagi pengembang mana pun, tetapi bagaimana jika kode itu juga ditinjau dan diuji? Dalam latihan berikutnya, kita akan menambahkan kritik agen lain ke sistem agen kita untuk membantu tugas pengkodean. Buka `autogen_coding_critic.py`, seperti yang ditunjukkan pada daftar berikut.

**Daftar 4.8** `autogen_coding_critic.py` 

```
import autogen
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

user_proxy = UserProxyAgent(
    "pengguna",
    code_execution_config={
        "work_dir": "working",
        "use_docker": False,
        "last_n_messages": 1,
    },
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: 
x.get("content", "").rstrip().endswith("TERMINATE"),
)

insinyur = AssistantAgent(
    name="Insinyur",
    llm_config={"config_list": config_list},
    system_message="""
    Anda adalah seorang insinyur Python profesional, yang dikenal dengan keahlian Anda dalam 
pengembangan perangkat lunak.
    Anda menggunakan keahlian Anda untuk membuat aplikasi perangkat lunak, alat, dan 
permainan yang fungsional dan efisien.
    Preferensi Anda adalah menulis kode yang bersih dan terstruktur dengan baik yang mudah 
dibaca dan dipelihara.    
    "",     #1
)

kritikus = AssistantAgent(
    name="Peninjau",
    llm_config={"config_list": config_list},
    system_message="""
    Anda adalah seorang peninjau kode, yang dikenal dengan ketelitian dan komitmen Anda 
terhadap standar.
    Tugas Anda adalah meneliti konten kode untuk setiap elemen berbahaya atau di bawah standar
. 
    Anda memastikan bahwa kode tersebut aman, efisien, dan mematuhi praktik terbaik
. 
    Anda akan mengidentifikasi setiap masalah atau area untuk perbaikan dalam kode 
    dan menampilkannya sebagai daftar.
    "",     #2
)

def review_code(penerima, pesan, pengirim, config):     #3
    return f"""
            Tinjau dan kritik kode berikut.

            {penerima.chat_messages_for_summary(pengirim)[-1]['content']}
            """                       #3                    

user_proxy.register_nested_chats(     #4
    [
        {
            "penerima": kritikus,
            "pesan": review_code,
            "summary_method": "last_msg",
            "max_turns": 1,
        }
    ],
    trigger=insinyur,                 #4
)
tugas = """Tulis permainan ular menggunakan Pygame."""

res = user_proxy.initiate_chat(
    penerima=insinyur, 
    pesan=tugas, 
    max_turns=2, 
    summary_method="last_msg"     #5
)
```

1. Kali ini, asisten diberi pesan sistem/persona.
2. Agen kritik asisten kedua dibuat dengan latar belakang.
3. Fungsi khusus membantu mengekstrak kode untuk ditinjau oleh kritikus.
4. Obrolan bersarang dibuat antara kritikus dan insinyur.
5. Agen proksi memulai obrolan dengan penundaan maksimum dan metode ringkasan eksplisit.

Jalankan file `autogen_coding_critic.py` di VS Code dalam mode debug, dan saksikan dialog antar agen. Kali ini, setelah kode kembali, kritikus juga akan dipicu untuk merespons. Kemudian, kritikus akan menambahkan komentar dan saran untuk meningkatkan kode.

Obrolan bersarang berfungsi dengan baik untuk mendukung dan mengontrol interaksi agen, tetapi kita akan melihat pendekatan yang lebih baik di bagian berikut. Namun, sebelum itu, kita akan meninjau pentingnya cache AutoGen di bagian selanjutnya.

### Memahami Cache AutoGen

AutoGen dapat menggunakan banyak token selama iterasi obrolan sebagai platform multi-agen yang dapat diajak bicara. Jika Anda meminta AutoGen untuk mengerjakan masalah yang kompleks atau baru, Anda bahkan mungkin mengalami batas token pada LLM Anda; karena itu, AutoGen mendukung beberapa metode untuk mengurangi penggunaan token.

AutoGen menggunakan caching untuk menyimpan kemajuan dan mengurangi penggunaan token. Caching diaktifkan secara default, dan Anda mungkin sudah mengalaminya. Jika Anda memeriksa folder kerja Anda saat ini, Anda akan melihat folder `.cache`, seperti yang ditunjukkan pada gambar 4.8. Caching memungkinkan agen Anda untuk melanjutkan percakapan jika terganggu.

![Gambar 4.8](Images/4-8.png)

Gambar 4.8 Cache AutoGen dan folder kerja

Dalam kode, Anda dapat mengontrol folder cache untuk proses agen Anda, seperti yang ditunjukkan pada daftar 4.9. Dengan membungkus panggilan `initiate_chat` dengan pernyataan `with`, Anda dapat mengontrol lokasi dan seed untuk cache. Ini akan memungkinkan Anda untuk menyimpan dan kembali ke tugas AutoGen yang berjalan lama di masa mendatang hanya dengan menyetel `cache_seed` untuk cache sebelumnya.

**Daftar 4.9** Mengatur folder cache

```
with Cache.disk(cache_seed=42) as cache:    #1
    res = user_proxy.initiate_chat(
        penerima=insinyur,
        pesan=tugas,
        max_turns=2,
        summary_method="last_msg",
        cache=cache,     #2
    )
```

1. Mengatur seed_cache menunjukkan lokasi individu.
2. Mengatur cache sebagai parameter

Kemampuan caching ini memungkinkan Anda untuk melanjutkan operasi dari lokasi cache sebelumnya dan menangkap proses sebelumnya. Ini juga bisa menjadi cara yang bagus untuk mendemonstrasikan dan memeriksa bagaimana percakapan agen menghasilkan hasil. Di bagian selanjutnya, kita akan melihat pola percakapan lain di mana AutoGen mendukung obrolan grup.

## Obrolan grup dengan agen dan AutoGen

Satu masalah dengan delegasi obrolan dan obrolan atau percakapan bersarang adalah penyampaian informasi. Jika Anda pernah memainkan permainan telepon, Anda telah menyaksikan ini secara langsung dan mengalami seberapa cepat informasi dapat berubah selama iterasi. Dengan agen, ini tentu tidak berbeda, dan mengobrol melalui percakapan bersarang atau berurutan dapat mengubah tugas atau bahkan hasil yang diinginkan.

### Permainan telepon

Permainan telepon adalah permainan yang menyenangkan tetapi mendidik yang menunjukkan hilangnya informasi dan koherensi. Anak-anak membentuk barisan, dan anak pertama menerima pesan yang hanya bisa mereka dengar. Kemudian, secara bergantian, anak-anak secara lisan menyampaikan pesan kepada anak berikutnya, dan seterusnya. Pada akhirnya, anak terakhir mengumumkan pesan kepada seluruh kelompok, yang sering kali bahkan tidak mendekati pesan yang sama.

Untuk mengatasi ini, AutoGen menyediakan obrolan grup, sebuah mekanisme di mana agen berpartisipasi dalam percakapan bersama. Ini memungkinkan agen untuk meninjau semua percakapan sebelumnya dan berkolaborasi dengan lebih baik pada tugas-tugas yang berjalan lama dan kompleks.

Gambar 4.9 menunjukkan perbedaan antara obrolan grup bersarang dan kolaboratif. Kami menggunakan fitur obrolan bersarang di bagian sebelumnya untuk membangun obrolan agen bersarang. Di bagian ini, kami menggunakan obrolan grup untuk memberikan pengalaman yang lebih kolaboratif.

![Gambar 4.9](Images/4-9.png)

Gambar 4.9 Perbedaan antara obrolan bersarang dan obrolan grup untuk agen yang dapat diajak bicara

Buka `autogen_coding_group.py` dengan bagian yang relevan, seperti yang ditunjukkan pada daftar 4.10. Kodenya mirip dengan latihan sebelumnya tetapi sekarang memperkenalkan `GroupChat` dan `GroupChatManager`. Agen dan pesan disimpan dengan obrolan grup, mirip dengan saluran perpesanan di aplikasi seperti Slack atau Discord. Manajer obrolan mengoordinasikan respons pesan untuk mengurangi tumpang tindih percakapan.

**Daftar 4.10** `autoget_coding_group.py` (bagian yang relevan)

```
user_proxy = UserProxyAgent(
    "pengguna",
    code_execution_config={
        "work_dir": "working",
        "use_docker": False,
        "last_n_messages": 3,
    },
    human_input_mode="NEVER",    #1
)

llm_config = {"config_list": config_list}


insinyur = AssistantAgent(…     #2


kritikus = AssistantAgent(…       #2


obrolan grup = GroupChat(agen=[user_proxy, 
                              insinyur, 
                              kritikus], 
                              pesan=[], 
                              max_round=20)     #3
manajer = GroupChatManager(groupchat=obrolan grup, 
                           llm_config=llm_config)    #4

tugas = """Tulis permainan ular menggunakan Pygame."""

with Cache.disk(cache_seed=43) as cache:
    res = user_proxy.initiate_chat(
        penerima=manajer,
        pesan=tugas,
        cache=cache,
    )
```

1. Input manusia sekarang diatur ke tidak pernah, jadi tidak ada umpan balik manusia.
2. Kode dihilangkan, tetapi lihat perubahan pada persona dalam file
3. Objek ini menyimpan koneksi ke semua agen dan menyimpan pesan.
4. Manajer mengoordinasikan percakapan seperti yang dilakukan moderator.

Jalankan latihan ini, dan Anda akan melihat bagaimana para agen berkolaborasi. Insinyur sekarang akan menerima umpan balik dari kritikus dan melakukan operasi untuk mengatasi saran kritikus. Ini juga memungkinkan proksi untuk terlibat dalam semua percakapan.

Percakapan grup adalah cara yang sangat baik untuk memperkuat kemampuan agen Anda saat mereka berkolaborasi dalam tugas. Namun, mereka juga secara substansial lebih bertele-tele dan mahal token. Tentu saja, seiring dengan matangnya LLM, begitu pula ukuran jendela token konteks mereka dan harga pemrosesan token. Seiring dengan meningkatnya jendela token, kekhawatiran tentang konsumsi token pada akhirnya dapat hilang.

AutoGen adalah platform multi-agen yang kuat yang dapat dialami menggunakan antarmuka web atau kode. Apa pun preferensi Anda, alat kolaborasi agen ini adalah platform yang sangat baik untuk membangun kode atau tugas kompleks lainnya. Tentu saja, ini bukan satu-satunya platform, seperti yang akan Anda lihat di bagian selanjutnya, di mana kita menjelajahi pendatang baru bernama CrewAI.

## Membangun kru agen dengan CrewAI

CrewAI relatif baru di ranah sistem multi-agen. Di mana AutoGen pada awalnya dikembangkan dari penelitian dan kemudian diperluas, CrewAI dibangun dengan mempertimbangkan sistem perusahaan. Dengan demikian, platform ini lebih kuat, membuatnya kurang dapat diperluas di beberapa area.

Dengan CrewAI, Anda membangun kru agen untuk fokus pada area spesifik dari tujuan tugas. Tidak seperti AutoGen, CrewAI tidak memerlukan penggunaan agen proksi pengguna tetapi malah mengasumsikan agen hanya bekerja di antara mereka sendiri.

Gambar 4.10 menunjukkan elemen utama platform CrewAI, bagaimana mereka terhubung bersama, dan fungsi utamanya. Ini menunjukkan sistem agen pemrosesan berurutan dengan agen peneliti dan penulis generik. Agen diberi tugas yang mungkin juga mencakup alat atau memori untuk membantu mereka.

![Gambar 4.10](Images/4-10.png)

Gambar 4.10 Komposisi sistem CrewAI

CrewAI mendukung dua bentuk pemrosesan utama: berurutan dan hierarkis. Gambar 4.10 menunjukkan proses berurutan dengan melakukan iterasi di seluruh agen yang diberikan dan tugas terkait mereka. Di bagian selanjutnya, kita akan mempelajari beberapa kode untuk menyiapkan kru dan menggunakannya untuk menyelesaikan tujuan dan membuat lelucon yang bagus.

### Membuat kru pelawak dari agen CrewAI

CrewAI membutuhkan lebih banyak penyiapan daripada AutoGen, tetapi ini juga memungkinkan lebih banyak kontrol dan panduan tambahan, yang memberikan konteks yang lebih spesifik untuk memandu agen dalam menyelesaikan tugas yang diberikan. Ini bukan tanpa masalah, tetapi ia menawarkan lebih banyak kontrol daripada AutoGen di luar kotak.

Buka `crewai_introduction.py` di VS Code dan lihat bagian atas, seperti yang ditunjukkan pada daftar 4.11. Banyak pengaturan yang diperlukan untuk mengonfigurasi agen, termasuk peran, tujuan, verbositas, memori, latar belakang, delegasi, dan bahkan alat (tidak ditampilkan). Dalam contoh ini, kami menggunakan dua agen: seorang peneliti lelucon senior dan seorang penulis lelucon.

**Daftar 4.11** `crewai_introduction.py` (bagian agen)

```
from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv

load_dotenv()

joke_researcher = Agent(     #1
    role="Peneliti Lelucon Senior",
    goal="Teliti apa yang membuat hal-hal lucu tentang {topik} berikut",
    verbose=True,     #2
    memory=True,     #3
    backstory=(
        "Didorong oleh humor slapstick, Anda adalah seorang peneliti lelucon berpengalaman"
        "yang tahu apa yang membuat orang tertawa. Anda memiliki bakat untuk menemukan"
        "yang lucu dalam situasi sehari-hari dan dapat mengubah momen yang membosankan menjadi"
        "kerusuhan tawa."
    ),    #4
    allow_delegation=True,    #5
)

joke_writer = Agent(    #6
    role="Penulis Lelucon",
    goal="Tulis lelucon yang lucu dan jenaka tentang {topik} berikut",
    verbose=True,    #7
    memory=True,     #8
    backstory=(
        "Anda adalah seorang penulis lelucon dengan bakat humor. Anda dapat mengubah"
        "ide sederhana menjadi kerusuhan tawa. Anda memiliki cara dengan kata-kata dan"
        "dapat membuat orang tertawa hanya dengan beberapa baris."
    ),    #9
    allow_delegation=False,    #5
)
```

1. Membuat agen dan memberi mereka tujuan
2. verbose memungkinkan agen untuk mengeluarkan output ke terminal.
3. Mendukung penggunaan memori untuk agen
4. Latar belakang adalah latar belakang agen—personanya.
5. Agen dapat didelegasikan atau diizinkan untuk mendelegasikan; True berarti mereka dapat mendelegasikan.
6. Membuat agen dan memberi mereka tujuan
7. verbose memungkinkan agen untuk mengeluarkan output ke terminal.
8. Mendukung penggunaan memori untuk agen
9. Latar belakang adalah latar belakang agen—personanya.

Bergerak ke bawah kode, kita selanjutnya melihat tugas, seperti yang ditunjukkan pada daftar 4.12. Tugas menunjukkan proses agen untuk menyelesaikan tujuan sistem utama. Mereka juga menautkan agen untuk mengerjakan tugas tertentu, menentukan output dari tugas itu, dan mungkin menyertakan bagaimana itu dieksekusi.

**Daftar 4.12** `crewai_introduction.py` (bagian tugas)

```
research_task = Task(        #1
    description=(
        "Identifikasi apa yang membuat topik berikut:{topic} begitu lucu."
        "Pastikan untuk menyertakan elemen kunci yang membuatnya lucu."
        "Juga, berikan analisis tren sosial saat ini,"
        "dan bagaimana hal itu memengaruhi persepsi humor."
    ),
    expected_output="Laporan komprehensif sepanjang 3 paragraf 
dalam tentang lelucon terbaru.",              #2
    agent=joke_researcher,     #3
)

write_task = Task(  #4
    description=(
        "Tulis lelucon yang berwawasan, lucu, dan sadar sosial tentang {topic}."
        "Pastikan untuk menyertakan elemen kunci yang membuatnya lucu dan"
        "relevan dengan tren sosial saat ini."
    ),
    expected_output="Lelucon tentang {topic}.".  #5
    agent=joke_writer,        #3
    async_execution=False,         #6
    output_file="the_best_joke.md",     #7
)
```

1. Deskripsi Tugas mendefinisikan bagaimana agen akan menyelesaikan tugas.
2. Secara eksplisit mendefinisikan output yang diharapkan dari melakukan tugas
3. Agen yang ditugaskan untuk mengerjakan tugas
4. Deskripsi Tugas mendefinisikan bagaimana agen akan menyelesaikan tugas.
5. Secara eksplisit mendefinisikan output yang diharapkan dari melakukan tugas
6. Jika agen harus mengeksekusi secara asinkron
7. Setiap output yang akan dihasilkan agen

Sekarang, kita dapat melihat bagaimana semuanya bersatu sebagai `Kru` di bagian bawah file, seperti yang ditunjukkan pada daftar 4.13. Sekali lagi, banyak opsi yang dapat diatur saat membangun `Kru`, termasuk agen, tugas, jenis proses, memori, cache, permintaan maksimum per menit (`max_rpm`), dan apakah kru berbagi.

**Daftar 4.13** `crewai_introduction.py` (bagian kru)

```
kru = Crew(
    agen=[peneliti_lelucon, penulis_lelucon],   #1
    tugas=[tugas_penelitian, tugas_penulisan],    #2
    proses=Process.berurutan,     #3
    memori=True,     #4
    cache=True,    #5
    max_rpm=100,    #6
    share_crew=True,    #7
)

hasil = kru.kickoff(input={"topik": "lelucon insinyur AI"})
print(hasil)
```

1. Para agen berkumpul menjadi kru
2. Tugas yang dapat dikerjakan oleh para agen
3. Mendefinisikan bagaimana para agen akan berinteraksi
4. Apakah sistem harus menggunakan memori; perlu diatur jika agen/tugas mengaktifkannya
5. Apakah sistem harus menggunakan cache, mirip dengan AutoGen
6. Permintaan maksimum per menit yang harus dibatasi oleh sistem
7. Apakah kru harus berbagi informasi, mirip dengan obrolan grup

Setelah selesai meninjau, jalankan file di VS Code (F5), dan saksikan terminal untuk percakapan dan pesan dari kru. Seperti yang mungkin sudah Anda duga sekarang, tujuan dari sistem agen ini adalah untuk membuat lelucon yang berkaitan dengan rekayasa AI. Berikut adalah beberapa lelucon lucu yang dihasilkan selama beberapa kali menjalankan sistem agen:

* Mengapa komputer itu dingin? Ia membiarkan Windows terbuka. 
* Mengapa insinyur AI tidak bermain petak umpet dengan algoritme mereka? Karena di mana pun mereka bersembunyi, algoritme selalu menemukan mereka di ruang "overfitting"!
* Apa lagu favorit seorang insinyur AI? "Aku baru saja menelepon untuk mengatakan aku mencintaimu... . dan untuk mengumpulkan lebih banyak data untuk perangkat lunak pengenalan suaraku."
* Mengapa insinyur AI itu bangkrut? Karena dia menghabiskan semua uangnya untuk kue, tetapi perambannya terus memakannya. 

Sebelum Anda menjalankan lebih banyak iterasi kru lelucon, Anda harus membaca bagian selanjutnya. Bagian ini menunjukkan cara menambahkan observabilitas ke sistem multi-agen.

### Mengamati agen yang bekerja dengan AgentOps

Mengamati kumpulan yang kompleks seperti sistem multi-agen sangat penting untuk memahami berbagai masalah yang dapat terjadi. Observabilitas melalui penelusuran aplikasi adalah elemen kunci dari setiap sistem yang kompleks, terutama yang terlibat dalam penggunaan perusahaan.

CrewAI mendukung koneksi ke platform operasi agen khusus yang disebut AgentOps. Platform observabilitas ini bersifat generik dan dirancang untuk mendukung observabilitas dengan platform agen apa pun yang spesifik untuk penggunaan LLM. Saat ini, tidak ada detail harga atau komersialisasi yang tersedia.

Menghubungkan ke AgentOps semudah menginstal paket, mendapatkan kunci API, dan menambahkan sebaris kode ke penyiapan kru Anda. Latihan berikutnya ini akan membahas langkah-langkah untuk menghubungkan dan menjalankan AgentOps.

Daftar 4.14 menunjukkan penginstalan paket `agentops` menggunakan `pip`. Anda dapat menginstal paket itu sendiri atau sebagai komponen tambahan dari paket `crewai`. Ingatlah bahwa AgentOps juga dapat dihubungkan ke platform agen lain untuk observabilitas.

**Daftar 4.14** Menginstal AgentOps

```
pip install agentops

atau sebagai opsi dengan CrewAI

pip install crewai[agentops]
```

Sebelum menggunakan AgentOps, Anda perlu mendaftar untuk mendapatkan kunci API. Berikut adalah langkah-langkah umum untuk mendaftar kunci pada saat penulisan:

1. Kunjungi https://app.agentops.ai di browser Anda. 
2. Daftar untuk sebuah akun.
3. Buat proyek, atau gunakan yang default.
4. Buka Pengaturan > Proyek dan Kunci API.
5. Salin dan/atau buat kunci API baru; ini akan menyalin kunci ke browser Anda.
6. Tempel kunci ke file `.env` Anda di proyek Anda. 

Setelah kunci API disalin, itu akan menyerupai contoh yang ditunjukkan pada daftar berikut.

**Daftar 4.15** `env.`: Menambahkan kunci AgentOps

```
AGENTOPS_API_KEY="kunci API Anda"
```

Sekarang, kita perlu menambahkan beberapa baris kode ke skrip CrewAI. Daftar 4.16 menunjukkan penambahan saat ditambahkan ke file `crewai_agentops.py`. Saat membuat skrip Anda sendiri, yang perlu Anda lakukan hanyalah menambahkan paket `agentops` dan menginisialisasinya saat menggunakan CrewAI.

**Daftar 4.16** `crewai_agentops.py` (Penambahan AgentOps)

```
import agentops     #1
from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv

load_dotenv()
agentops.init()    #2
```

1. Penambahan paket yang diperlukan
2. Pastikan untuk menginisialisasi paket setelah variabel lingkungan dimuat.

Jalankan file `crewai_agentops.py` di VS Code (F5), dan saksikan para agen bekerja seperti sebelumnya. Namun, Anda sekarang dapat membuka dasbor AgentOps dan melihat interaksi agen di berbagai tingkatan.

Gambar 4.11 menunjukkan dasbor untuk menjalankan kru lelucon untuk membuat lelucon terbaik. Beberapa statistik termasuk durasi total, lingkungan proses, token prompt dan penyelesaian, waktu panggilan LLM, dan perkiraan biaya. Melihat biaya bisa menjadi hal yang menyadarkan dan menunjukkan betapa bertele-tele percakapan agen bisa menjadi. 

![Gambar 4.11](Images/4-11.png)

Gambar 4.11 Dasbor AgentOps untuk menjalankan kru lelucon

Platform AgentOps adalah tambahan yang sangat baik untuk platform agen apa pun. Meskipun dibangun ke dalam CrewAI, sangat membantu bahwa observabilitas dapat ditambahkan ke AutoGen atau kerangka kerja lainnya. Hal menarik lainnya tentang AgentOps adalah ia didedikasikan untuk mengamati interaksi agen dan tidak bertransformasi dari platform operasi pembelajaran mesin. Di masa depan, kita kemungkinan akan melihat munculnya lebih banyak pola observabilitas agen.

Satu manfaat yang tidak dapat dilebih-lebihkan adalah pengamatan biaya yang dapat diberikan oleh platform observabilitas. Apakah Anda memperhatikan pada gambar 4.11 bahwa membuat satu lelucon berharga sedikit di atas 50 sen? Agen bisa sangat kuat, tetapi mereka juga bisa menjadi sangat mahal, dan penting untuk mengamati berapa biaya tersebut dalam hal kepraktisan dan komersialisasi.

Di bagian terakhir bab ini, kita akan kembali ke CrewAI dan meninjau kembali pembangunan agen yang dapat membuat kode game. Ini akan memberikan perbandingan yang sangat baik antara kemampuan AutoGen dan CrewAI.

## Meninjau kembali agen pengkodean dengan CrewAI

Cara yang bagus untuk membandingkan kemampuan antara platform multi-agen adalah dengan mengimplementasikan tugas serupa di bot. Dalam rangkaian latihan berikutnya, kita akan menggunakan CrewAI sebagai tim pemrograman game. Tentu saja, ini juga dapat diadaptasi ke tugas pengkodean lainnya.

Buka `crewai_coding_crew.py` di VS Code, dan pertama-tama kita akan meninjau bagian agen di daftar 4.17. Di sini, kita membuat seorang insinyur senior, seorang insinyur QA, dan seorang kepala insinyur QA dengan peran, tujuan, dan latar belakang. 

**Daftar 4.17** `crewai_coding_crew.py` (bagian agen)

```
print("## Selamat datang di Kru Game")     #1
print("-------------------------------")
game = input("Game apa yang ingin Anda buat? 
Apa mekanismenya?\n")


senior_engineer_agent = Agent(
    role="Insinyur Perangkat Lunak Senior",
    goal="Buat perangkat lunak sesuai kebutuhan",
    backstory=dedent(
        """
        Anda adalah seorang Insinyur Perangkat Lunak Senior di sebuah lembaga pemikir teknologi terkemuka.
        Keahlian Anda dalam pemrograman dengan python. dan lakukan yang terbaik untuk
        menghasilkan kode yang sempurna
        """
    ),
    allow_delegation=False,
    verbose=True,
)

qa_engineer_agent = Agent(
    role="Insinyur Kontrol Kualitas Perangkat Lunak",
    goal="buat kode prefek, dengan menganalisis kode 
yang diberikan untuk kesalahan",
    backstory=dedent(
        """
        Anda adalah seorang insinyur perangkat lunak yang berspesialisasi dalam memeriksa kode
        untuk kesalahan. Anda memiliki mata untuk detail dan bakat untuk menemukan
        bug tersembunyi.
        Anda memeriksa impor yang hilang, deklarasi variabel, kurung yang tidak cocok
        dan kesalahan sintaks.
        Anda juga memeriksa kerentanan keamanan, dan kesalahan logika
        """
    ),
    allow_delegation=False,
    verbose=True,
)

chief_qa_engineer_agent = Agent(
    role="Kepala Insinyur Kontrol Kualitas Perangkat Lunak",
    goal="Pastikan kode melakukan pekerjaan yang seharusnya dilakukan",
    backstory=dedent(
        """
        Anda adalah seorang Kepala Insinyur Kontrol Kualitas Perangkat Lunak di sebuah lembaga
        pemikir teknologi terkemuka. Anda bertanggung jawab untuk memastikan bahwa kode
        yang ditulis melakukan pekerjaan yang seharusnya dilakukan.
        Anda bertanggung jawab untuk memeriksa kode untuk kesalahan dan memastikan
        bahwa itu adalah kualitas tertinggi.
        """
    ),
    allow_delegation=True,    #2
    verbose=True,
)
```

1. Memungkinkan pengguna untuk memasukkan instruksi untuk game mereka
2. Hanya kepala insinyur QA yang dapat mendelegasikan tugas. 

Bergulir ke bawah dalam file akan menampilkan tugas agen, seperti yang ditunjukkan pada daftar 4.18. Deskripsi tugas dan output yang diharapkan harus mudah diikuti. Sekali lagi, setiap agen memiliki tugas khusus untuk memberikan konteks yang lebih baik saat bekerja untuk menyelesaikan tugas.

**Daftar 4.18** `crewai_coding_crew.py` (bagian tugas)

```
code_task = Task(
    description=f"""
Anda akan membuat game menggunakan python, ini adalah instruksinya:
        Instruksi
        ------------
        {game}            #1
        Anda akan menulis kode untuk game menggunakan python.""",
    expected_output="Jawaban Akhir Anda harus berupa 
kode python lengkap, hanya kode python dan tidak ada yang lain.",
    agent=senior_engineer_agent,
)

qa_task = Task(
    description=f"""Anda membantu membuat game 
menggunakan python, ini adalah instruksinya:
        Instruksi
        ------------
        {game}            #1
        Menggunakan kode yang Anda dapatkan, periksa kesalahannya. Periksa kesalahan logika,
        kesalahan sintaks, impor yang hilang, deklarasi variabel, 
kurung yang tidak cocok,
        dan kerentanan keamanan.""",
    expected_output="Keluarkan daftar masalah yang Anda temukan dalam kode.",
    agent=qa_engineer_agent,
)

evaluate_task = Task(
    description=f"""Anda membantu membuat game 
menggunakan python, ini adalah instruksinya:
        Instruksi
        ------------
        {game}            #1
        Anda akan melihat kode untuk memastikan bahwa itu lengkap dan
        melakukan pekerjaan yang seharusnya dilakukan. """,
    expected_output="Jawaban Akhir Anda harus berupa 
kode python lengkap yang diperbaiki, hanya kode python dan tidak ada yang lain.",
    agent=chief_qa_engineer_agent,
)
```

1. Instruksi game diganti ke dalam prompt menggunakan pemformatan Python.

Akhirnya, kita dapat melihat bagaimana ini bersatu dengan membuka bagian bawah file, seperti yang ditunjukkan pada daftar 4.19. Konfigurasi kru ini sangat mirip dengan apa yang telah kita lihat sebelumnya. Setiap agen dan tugas ditambahkan, serta atribut verbose dan proses. Untuk contoh ini, kita akan terus menggunakan metode berurutan. 

**Daftar 4.19** `crewai_coding_crew.py` (bagian kru)

```
kru = Crew(
    agen=[insinyur_senior_agen, 
            qa_insinyur_agen, 
            kepala_qa_insinyur_agen],
    tugas=[tugas_kode, tugas_qa, tugas_evaluasi],
    verbose=2,  
    proses=Process.berurutan,     #1
)

# Buat kru Anda bekerja!
hasil = kru.kickoff()   #2

print("######################")
print(hasil)
```

1. Prosesnya berurutan.
2. Tidak ada konteks tambahan yang disediakan saat kickoff.

Saat Anda menjalankan file VS Code (F5), Anda akan diminta untuk memasukkan instruksi untuk menulis game. Masukkan beberapa instruksi, mungkin game ular atau game lain yang Anda pilih. Kemudian, biarkan para agen bekerja, dan amati apa yang mereka hasilkan.

Dengan penambahan kepala insinyur QA, hasilnya secara umum akan terlihat lebih baik daripada yang dihasilkan dengan AutoGen, setidaknya di luar kotak. Jika Anda meninjau kode, Anda akan melihat bahwa itu umumnya mengikuti pola yang baik dan, dalam beberapa kasus, bahkan mungkin menyertakan pengujian dan pengujian unit.

Sebelum kita menyelesaikan bab ini, kita akan membuat satu perubahan terakhir pada pola pemrosesan kru. Sebelumnya, kita menggunakan pemrosesan berurutan, seperti yang ditunjukkan pada gambar 4.10. Gambar 4.12 menunjukkan seperti apa pemrosesan hierarkis di CrewAI. 

![Gambar 4.12](Images/4-12.png)

Gambar 4.12 Pemrosesan hierarkis agen yang dikoordinasikan melalui manajer kru

Menambahkan manajer ini adalah proses yang relatif sederhana. Daftar 4.20 menunjukkan perubahan kode tambahan ke file baru yang menggunakan kru pengkodean dalam metode hierarkis. Selain mengimpor kelas untuk terhubung ke OpenAI dari LangChain, penambahan lainnya adalah menambahkan kelas ini sebagai manajer kru, `manager_llm`. 

**Daftar 4.20** `crewai_hierarchy.py` (bagian manajer kru)

```
from langchain_openai import ChatOpenAI     #1

kru = Crew(
    agen=[insinyur_senior_agen, 
            qa_insinyur_agen, 
            kepala_qa_insinyur_agen],
    tugas=[tugas_kode, tugas_qa, tugas_evaluasi],
    verbose=2,  
    proses=Process.hierarkis,    #2
    manager_llm=ChatOpenAI(    #3
        suhu=0, model="gpt-4"      #3
    ),   #4
)         #4
```

1. Mengimpor konektor LLM dari LangChain
2. Anda harus menyetel manajer kru saat memilih pemrosesan hierarkis.
3. Menyetel manajer kru menjadi konektor LLM
4. Anda harus menyetel manajer kru saat memilih pemrosesan hierarkis.

Jalankan file ini di VS Code (F5). Saat diminta, masukkan game yang ingin Anda buat. Coba gunakan game yang sama yang Anda coba dengan AutoGen; game ular juga merupakan contoh dasar yang baik. Amati para agen bekerja melalui kode dan meninjaunya berulang kali untuk masalah.

Setelah Anda menjalankan file, Anda juga dapat membuka AgentOps untuk meninjau biaya proses ini. Kemungkinan besar, biayanya akan lebih dari dua kali lipat dari biaya tanpa manajer agen. Outputnya juga kemungkinan tidak akan jauh lebih baik. Ini adalah jebakan membangun sistem agen tanpa memahami seberapa cepat hal-hal dapat berputar.

Contoh spiral ini yang sering terjadi ketika agen terus-menerus mengulangi tindakan yang sama adalah sering mengulangi tugas. Anda dapat melihat masalah ini di AgentOps, seperti yang ditunjukkan pada gambar 4.13, dengan melihat plot Ulangi Pikiran. 

![Gambar 4.13](Images/4-13.png)

Gambar 4.13 Pengulangan pikiran saat terjadi dalam proses agen

Plot Ulangi Pikiran dari AgentOps adalah cara yang sangat baik untuk mengukur pengulangan yang ditemui sistem agen Anda. Pola pikir yang terlalu berulang biasanya berarti agen tidak cukup tegas dan malah terus mencoba menghasilkan jawaban yang berbeda. Jika Anda mengalami masalah ini, Anda ingin mengubah pola pemrosesan, tugas, dan tujuan agen. Anda bahkan mungkin ingin mengubah jenis dan jumlah agen sistem.

Sistem multi-agen adalah cara yang sangat baik untuk memecah pekerjaan dalam hal pola kerja pekerjaan dan tugas. Umumnya, peran pekerjaan dialokasikan ke peran/persona agen, dan tugas yang perlu diselesaikan mungkin implisit, seperti di AutoGen, atau lebih eksplisit, seperti di CrewAI. 

Dalam bab ini, kami membahas banyak alat dan platform berguna yang dapat Anda gunakan segera untuk meningkatkan pekerjaan, kehidupan, dan banyak lagi. Itu melengkapi perjalanan kita melalui platform multi-agen, tetapi itu tidak mengakhiri eksplorasi dan penggunaan banyak agen kita, seperti yang akan kita temukan di bab-bab selanjutnya.

## Latihan

Gunakan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

* *Latihan 1* —Komunikasi Agen Dasar dengan AutoGen 
  * *Tujuan* —Membiasakan diri dengan komunikasi dan penyiapan agen dasar di AutoGen.
  * *Tugas*:
    * Siapkan AutoGen Studio di mesin lokal Anda, ikuti instruksi yang diberikan dalam bab ini. 
    * Buat sistem multi-agen sederhana dengan proksi pengguna dan dua agen asisten. 
    * Terapkan tugas dasar di mana proksi pengguna berkoordinasi antara agen asisten untuk menghasilkan output teks sederhana, seperti merangkum paragraf pendek. 
* *Latihan 2* —Menerapkan Keterampilan Agen Tingkat Lanjut di AutoGen Studio 
  * *Tujuan* —Meningkatkan kemampuan agen dengan menambahkan keterampilan tingkat lanjut.
  * *Tugas*:
    * Kembangkan dan integrasikan keterampilan baru ke dalam agen AutoGen yang memungkinkannya mengambil dan menampilkan data waktu nyata dari API publik (mis., informasi cuaca atau harga saham). 
    * Pastikan agen dapat meminta preferensi pengguna (mis., kota untuk cuaca, jenis saham) dan menampilkan data yang diambil sesuai.
* *Latihan 3* —Manajemen Tugas Berbasis Peran dengan CrewAI 
  * *Tujuan* —Menjelajahi manajemen tugas berbasis peran di CrewAI.
  * *Tugas*:
    * Rancang penyiapan CrewAI di mana banyak agen diberi peran spesifik (mis., pengambil data, penganalisis, penyaji).
    * Konfigurasikan urutan tugas di mana pengambil data mengumpulkan data, penganalisis memproses data, dan penyaji menghasilkan laporan. 
    * Jalankan urutan dan amati alur informasi dan delegasi tugas di antara agen. 
* *Latihan 4* —Kolaborasi Multi-Agen dalam Obrolan Grup Menggunakan AutoGen 
  * *Tujuan* —Memahami dan mengimplementasikan sistem obrolan grup di AutoGen untuk memfasilitasi kolaborasi agen.
  * *Tugas*:
    * Siapkan skenario di mana banyak agen perlu berkolaborasi untuk memecahkan masalah yang kompleks (mis., merencanakan rencana perjalanan untuk perjalanan bisnis).
    * Gunakan fitur obrolan grup untuk memungkinkan agen berbagi informasi, mengajukan pertanyaan, dan memberikan pembaruan satu sama lain. 
    * Pantau interaksi dan efektivitas agen dalam pemecahan masalah kolaboratif. 
* *Latihan 5* —Menambahkan dan Menguji Observabilitas dengan AgentOps di CrewAI 
  * *Tujuan* —Menerapkan dan mengevaluasi observabilitas agen menggunakan AgentOps di lingkungan CrewAI.
  * *Tugas*:
    * Integrasikan AgentOps ke dalam sistem multi-agen CrewAI. 
    * Rancang tugas untuk agen yang melibatkan komputasi atau pemrosesan data yang signifikan (mis., menganalisis ulasan pelanggan untuk menentukan tren sentimen).
    * Gunakan AgentOps untuk memantau kinerja, biaya, dan akurasi output agen. Identifikasi setiap potensi inefisiensi atau kesalahan dalam interaksi agen. 

## Ringkasan

* AutoGen, yang dikembangkan oleh Microsoft, adalah platform multi-agen percakapan yang menggunakan berbagai jenis agen, seperti proksi pengguna dan agen asisten, untuk memfasilitasi pelaksanaan tugas melalui interaksi bahasa alami. 
* AutoGen Studio bertindak sebagai lingkungan pengembangan yang memungkinkan pengguna untuk membuat, menguji, dan mengelola sistem multi-agen, meningkatkan kegunaan AutoGen. 
* AutoGen mendukung beberapa pola komunikasi, termasuk obrolan grup dan komunikasi hierarkis dan proksi. Komunikasi proksi melibatkan agen utama (proksi) yang menjadi antarmuka antara pengguna dan agen lain untuk merampingkan penyelesaian tugas. 
* CrewAI menawarkan pendekatan terstruktur untuk membangun sistem multi-agen dengan fokus pada aplikasi perusahaan. Ini menekankan fungsionalitas agen berbasis peran dan otonom, memungkinkan manajemen tugas yang fleksibel, berurutan, atau hierarkis. 
* Latihan praktis dalam bab ini menggambarkan cara menyiapkan dan menggunakan AutoGen Studio, termasuk menginstal komponen yang diperlukan dan menjalankan sistem multi-agen dasar. 
* Agen di AutoGen dapat dilengkapi dengan keterampilan khusus untuk melakukan tugas-tugas seperti pembuatan kode, analisis gambar, dan pengambilan data, sehingga memperluas cakupan aplikasi mereka. 
* CrewAI dibedakan oleh kemampuannya untuk menyusun interaksi agen lebih kaku daripada AutoGen, yang dapat menguntungkan dalam pengaturan yang memerlukan perilaku agen yang tepat dan terkontrol. 
* CrewAI mendukung integrasi memori dan alat untuk digunakan agen melalui penyelesaian tugas. 
* CrewAI mendukung integrasi dengan alat observabilitas seperti AgentOps, yang memberikan wawasan tentang kinerja agen, efisiensi interaksi, dan manajemen biaya. 
* AgentOps adalah platform observabilitas agen yang dapat membantu Anda dengan mudah memantau interaksi agen yang luas.
