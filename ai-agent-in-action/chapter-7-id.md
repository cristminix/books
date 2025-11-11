# Bab 7: Merakit dan menggunakan platform agen

## Bab ini mencakup

- Antarmuka obrolan dan dasbor Nexus untuk agen AI
- Kerangka kerja Streamlit untuk membangun dasbor cerdas, prototipe, dan aplikasi obrolan AI
- Mengembangkan, menguji, dan melibatkan profil dan persona agen di Nexus
- Mengembangkan agen Nexus dasar
- Mengembangkan, menguji, dan melibatkan tindakan dan alat agen sendiri atau di dalam Nexus

Setelah kita menjelajahi beberapa konsep dasar tentang agen dan melihat penggunaan tindakan dengan alat untuk membangun prompt dan persona menggunakan kerangka kerja seperti Semantic Kernel (SK), kita mengambil langkah pertama menuju pembangunan fondasi untuk buku ini. Fondasi itu disebut Nexus, sebuah platform agen yang dirancang agar mudah dipelajari, mudah dijelajahi, dan cukup kuat untuk membangun sistem agen Anda sendiri.

## 7.1 Memperkenalkan Nexus, bukan sekadar platform agen biasa

Ada lebih dari 100 platform dan perangkat AI untuk mengonsumsi dan mengembangkan aplikasi model bahasa besar (LLM), mulai dari perangkat seperti SK atau LangChain hingga platform lengkap seperti AutoGen dan CrewAI. Hal ini menyulitkan untuk memutuskan platform mana yang cocok untuk membangun agen AI Anda sendiri.

Nexus adalah platform sumber terbuka yang dikembangkan bersama buku ini untuk mengajarkan konsep inti dalam membangun agen AI berfitur lengkap. Dalam bab ini, kita akan mengkaji bagaimana Nexus dibangun dan memperkenalkan dua komponen agen utama: profil/persona dan tindakan/alat.

Gambar 7.1 menunjukkan antarmuka utama Nexus, sebuah aplikasi obrolan Streamlit yang memungkinkan Anda memilih dan menjelajahi berbagai fitur agentik. Antarmukanya mirip dengan ChatGPT, Gemini, dan aplikasi LLM komersial lainnya.

![gambar](Images/7-1.png)

**Gambar 7.1** Antarmuka dan fitur Nexus

Selain fitur standar aplikasi obrolan LLM, Nexus memungkinkan pengguna untuk mengonfigurasi agen agar menggunakan API/model tertentu, persona, dan tindakan yang memungkinkan. Di sisa buku ini, opsi agen yang tersedia akan mencakup yang berikut:

- **Persona/profil**—Persona dan profil utama yang akan digunakan agen. Persona adalah kepribadian dan motivator utama, dan agen melibatkan persona untuk menjawab permintaan. Kita akan melihat dalam bab ini bagaimana persona/profil dapat dikembangkan dan digunakan.
- **Tindakan/alat**—Mewakili tindakan yang dapat diambil agen menggunakan alat, baik itu fungsi semantik/prompt atau fungsi asli/kode. Dalam bab ini, kita akan melihat cara membangun fungsi semantik dan asli di dalam Nexus.
- **Pengetahuan/memori**—Mewakili informasi tambahan yang mungkin dapat diakses oleh agen. Pada saat yang sama, memori agen dapat mewakili berbagai aspek, dari memori jangka pendek hingga memori semantik.
- **Perencanaan/umpan balik**—Mewakili bagaimana agen merencanakan dan menerima umpan balik atas rencana atau pelaksanaan rencana. Nexus akan memungkinkan pengguna untuk memilih opsi untuk jenis perencanaan dan umpan balik yang digunakan agen.

Seiring kemajuan kita dalam buku ini, Nexus akan ditambahkan untuk mendukung fitur-fitur agen baru. Namun, pada saat yang sama, tujuannya adalah untuk menjaga agar semuanya tetap relatif sederhana untuk mengajarkan banyak konsep inti yang penting ini. Di bagian selanjutnya, kita akan melihat cara cepat menggunakan Nexus sebelum masuk ke balik layar untuk menjelajahi fitur-fiturnya secara mendetail.

### 7.1.1 Menjalankan Nexus

Nexus terutama dimaksudkan sebagai platform pengajaran untuk semua tingkat pengembang. Dengan demikian, ia akan mendukung berbagai opsi penerapan dan penggunaan. Dalam latihan berikutnya, kita akan memperkenalkan cara untuk memulai dan menjalankan Nexus dengan cepat.

Buka terminal ke lingkungan virtual Python baru (versi 3.10). Jika Anda memerlukan bantuan untuk membuatnya, lihat apendiks B. Kemudian, jalankan perintah yang ditunjukkan pada daftar 7.1 di dalam lingkungan baru ini. Anda dapat mengatur variabel lingkungan di baris perintah atau membuat file `.env` baru dan menambahkan pengaturannya.

**Daftar 7.1** Baris perintah terminal

```
pip install git+https://github.com/cxbxmxcx/Nexus.git    #1

#atur Kunci API OpenAI Anda
export OPENAI_API_KEY="< kunci API Anda>"         #2
atau
$env: OPENAI_API_KEY = ="< kunci API Anda>"       #2
atau
echo 'OPENAI_API_KEY="<kunci API Anda>"' > .env   #2

nexus run     #3
```

1. Menginstal paket langsung dari repositori dan cabang; pastikan untuk menyertakan cabang.
2. Membuat kunci sebagai variabel lingkungan atau membuat file .env baru dengan pengaturan tersebut
3. Menjalankan aplikasi

Setelah memasukkan perintah terakhir, sebuah situs web akan diluncurkan dengan halaman login, seperti yang ditunjukkan pada gambar 7.2. Silakan buat pengguna baru. Versi Nexus di masa mendatang akan memungkinkan banyak pengguna untuk terlibat dalam utas obrolan.

![gambar](Images/7-2.png)

**Gambar 7.2** Masuk atau membuat pengguna Nexus baru

Setelah Anda masuk, Anda akan melihat halaman seperti gambar 7.1. Buat obrolan baru dan mulailah bercakap-cakap dengan agen. Jika Anda mengalami masalah, pastikan Anda telah mengatur kunci API dengan benar. Seperti yang dijelaskan di bagian selanjutnya, Anda dapat menjalankan Nexus menggunakan metode ini atau dari alur kerja pengembangan.

### 7.1.2 Mengembangkan Nexus

Saat mengerjakan latihan-latihan dalam buku ini, Anda akan ingin menyiapkan Nexus dalam mode pengembangan. Itu berarti mengunduh repositori langsung dari GitHub dan bekerja dengan kodenya.

Buka terminal baru, dan atur direktori kerja Anda ke folder kode sumber `chapter_7`. Kemudian, siapkan lingkungan virtual Python baru (versi 3.10) dan masukkan perintah yang ditunjukkan pada daftar 7.2. Sekali lagi, lihat apendiks B jika Anda memerlukan bantuan dengan penyiapan sebelumnya.

**Daftar 7.2** Menginstal Nexus untuk pengembangan

```
git clone https://github.com/cxbxmxcx/Nexus.git     #1

pip install -e Nexus    #2

#atur Kunci API OpenAI Anda (disarankan file .env)
export OPENAI_API_KEY="< kunci API Anda>"  #bash           #3
atau
$env: OPENAI_API_KEY = ="< kunci API Anda>"  #powershell   #3
atau
echo 'OPENAI_API_KEY="<kunci API Anda>"' > .env       #3


nexus run     #4
```

1. Mengunduh dan menginstal cabang spesifik dari repositori
2. Menginstal repositori yang diunduh sebagai paket yang dapat diedit
3. Mengatur kunci OpenAI Anda sebagai variabel lingkungan atau menambahkannya ke file .env
4. Memulai aplikasi

Gambar 7.3 menunjukkan layar Login atau Buat Pengguna Baru. Buat pengguna baru, dan aplikasi akan membuat Anda masuk. Aplikasi ini menggunakan cookie untuk mengingat pengguna, jadi Anda tidak perlu masuk lagi saat memulai aplikasi berikutnya. Jika Anda menonaktifkan cookie di browser Anda, Anda harus masuk setiap saat.

![gambar](Images/7-3.png)

**Gambar 7.3** Halaman Login atau Buat Pengguna Baru

Buka folder repositori Nexus dan lihat-lihat. Gambar 7.4 menunjukkan diagram arsitektur elemen utama aplikasi. Di bagian atas, antarmuka yang dikembangkan dengan Streamlit menghubungkan seluruh sistem melalui sistem obrolan. Sistem obrolan mengelola basis data, manajer agen, manajer tindakan, dan manajer profil.

![gambar](Images/7-4.png)

**Gambar 7.4** Diagram arsitektur tingkat tinggi dari elemen utama aplikasi

Platform agen ini ditulis sepenuhnya dengan Python, dan antarmuka webnya menggunakan Streamlit. Di bagian selanjutnya, kita akan melihat cara membangun aplikasi obrolan OpenAI LLM.

## 7.2 Memperkenalkan Streamlit untuk pengembangan aplikasi obrolan

Streamlit adalah alat prototipe antarmuka web yang cepat dan kuat yang dirancang untuk digunakan dalam membangun dasbor dan konsep pembelajaran mesin. Ini memungkinkan aplikasi ditulis sepenuhnya dengan Python dan menghasilkan antarmuka web modern yang didukung React. Anda bahkan dapat dengan cepat menerapkan aplikasi yang sudah selesai ke cloud atau sebagai aplikasi mandiri.

### 7.2.1 Membangun aplikasi obrolan Streamlit

Mulailah dengan membuka Visual Studio Code (VS Code) ke folder sumber `chapter_07`. Jika Anda telah menyelesaikan latihan sebelumnya, Anda seharusnya sudah siap. Seperti biasa, jika Anda memerlukan bantuan untuk menyiapkan lingkungan dan alat Anda, lihat apendiks B.

Kita akan mulai dengan membuka file `chatgpt_clone_response.py` di VS Code. Bagian atas kode ditunjukkan pada daftar 7.3. Kode ini menggunakan status Streamlit untuk memuat model utama dan pesan. Streamlit menyediakan mekanisme untuk menyimpan status sesi untuk objek Python apa pun. Status ini hanya status sesi dan akan kedaluwarsa saat pengguna menutup browser.

**Daftar 7.3** `chatgpt_clone_response.py` (bagian atas)

```python
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()     #1

st.title("Klon seperti ChatGPT")

client = OpenAI()     #2

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] 
             = "gpt-4-1106-preview"    #3

if "messages" not in st.session_state:
    st.session_state["messages"] = []  #4

for message in st.session_state["messages"]:     #5
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

1. Memuat variabel lingkungan dari file .env
2. Mengonfigurasi klien OpenAI
3. Memeriksa status sesi internal untuk pengaturan, dan menambahkannya jika tidak ada
4. Memeriksa keberadaan status pesan; jika tidak ada, tambahkan daftar kosong
5. Melakukan loop melalui pesan dalam status dan menampilkannya

Aplikasi Streamlit itu sendiri tidak memiliki status. Ini berarti seluruh skrip Python akan mengeksekusi ulang semua komponen antarmuka saat halaman web disegarkan atau pengguna memilih suatu tindakan. Status Streamlit memungkinkan mekanisme penyimpanan sementara. Tentu saja, basis data diperlukan untuk mendukung penyimpanan jangka panjang.

Kontrol dan komponen UI ditambahkan dengan menggunakan awalan `st.` dan kemudian nama elemen. Streamlit mendukung beberapa kontrol UI standar dan mendukung gambar, video, suara, dan, tentu saja, obrolan.

Menggulir lebih jauh ke bawah akan menghasilkan daftar 7.4, yang memiliki tata letak komponen yang sedikit lebih kompleks. Pernyataan `if` utama mengontrol jalannya kode yang tersisa. Dengan menggunakan operator Walrus (:=), prompt diatur ke apa pun yang dimasukkan pengguna. Jika pengguna tidak memasukkan teks apa pun, kode di bawah pernyataan `if` tidak akan dieksekusi.

**Daftar 7.4** `chatgpt_clone_response.py` (bagian bawah)

```python
if prompt := st.chat_input("Apa yang Anda butuhkan?"):    #1
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):    #2
        st.markdown(prompt)

    with st.spinner(text="Asisten sedang berpikir..."):   #3
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],     #4
            )
            response_content = response.choices[0].message.content
            response = st.markdown(response_content,
             unsafe_allow_html=True)     #5
    st.session_state.messages.append(
{"role": "assistant", "content": response_content})     #6
```

1. Kontrol input obrolan dirender, dan konten diatur.
2. Mengatur kontrol pesan obrolan untuk ditampilkan sebagai pengguna
3. Menampilkan spinner untuk mewakili panggilan API yang berjalan lama
4. Memanggil API OpenAI dan mengatur riwayat pesan
5. Menulis respons pesan sebagai markdown ke antarmuka
6. Menambahkan respons asisten ke status pesan

Saat pengguna memasukkan teks di prompt dan menekan Enter, teks tersebut ditambahkan ke status pesan, dan permintaan dibuat ke API. Saat respons sedang diproses, kontrol `st.spinner` ditampilkan untuk mengingatkan pengguna tentang proses yang berjalan lama. Kemudian, saat respons kembali, pesan ditampilkan dan ditambahkan ke riwayat status pesan.

Aplikasi Streamlit dijalankan menggunakan modul, dan untuk men-debug aplikasi, Anda perlu melampirkan debugger ke modul dengan mengikuti langkah-langkah berikut:

1. Tekan Ctrl-Shift-D untuk membuka debugger VS Code.
2. Klik tautan untuk membuat konfigurasi peluncuran baru, atau klik ikon roda gigi untuk menampilkan yang sekarang.
3. Edit atau gunakan alat konfigurasi debugger untuk mengedit file `.vscode/launch.json`, seperti yang ditunjukkan pada daftar berikutnya. Banyak alat IntelliSense dan opsi konfigurasi yang dapat memandu Anda dalam mengatur opsi untuk file ini.

**Daftar 7.5** `.vscode/launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Module",    #1
      "type": "debugpy",
      "request": "launch",
      "module": "streamlit",    #2
      "args": ["run", "${file}"]   #3
    }
  ]
}
```

1. Pastikan debugger diatur ke Modul.
2. Pastikan modulnya adalah streamlit.
3. ${file} adalah file saat ini, atau Anda dapat melakukan hardcode ini ke jalur file.

Setelah Anda mengatur konfigurasi file `launch.json`, simpan, dan buka file `chatgpt_ clone_response.py` di VS Code. Anda sekarang dapat menjalankan aplikasi dalam mode debug dengan menekan F5. Ini akan meluncurkan aplikasi dari terminal, dan dalam beberapa detik, aplikasi akan ditampilkan.

Gambar 7.5 menunjukkan aplikasi berjalan dan menunggu untuk mengembalikan respons. Antarmukanya bersih, modern, dan sudah terorganisir tanpa pekerjaan tambahan. Anda dapat terus mengobrol dengan LLM menggunakan antarmuka dan kemudian menyegarkan halaman untuk melihat apa yang terjadi.

![gambar](Images/7-5.png)

**Gambar 7.5** Antarmuka sederhana dan spinner yang menunggu

Yang paling mengesankan dari demonstrasi ini adalah betapa mudahnya membuat aplikasi satu halaman. Di bagian selanjutnya, kita akan terus melihat aplikasi ini tetapi dengan beberapa penyempurnaan.

### 7.2.2 Membuat aplikasi obrolan streaming

Aplikasi obrolan modern, seperti ChatGPT dan Gemini, menutupi kelambatan model mereka dengan menggunakan streaming. Streaming memungkinkan panggilan API untuk segera mulai melihat token saat token tersebut diproduksi dari LLM. Pengalaman streaming ini juga lebih baik melibatkan pengguna dalam cara konten dihasilkan.

Menambahkan dukungan untuk streaming ke UI aplikasi apa pun umumnya bukan tugas yang sepele, tetapi untungnya, Streamlit memiliki kontrol yang dapat bekerja dengan mulus. Dalam latihan berikutnya, kita akan melihat cara memperbarui aplikasi untuk mendukung streaming.

Buka `chapter_7/chatgpt_clone_streaming.py` di VS Code. Pembaruan yang relevan pada kode ditunjukkan pada daftar 7.6. Menggunakan kontrol `st.write_stream` memungkinkan UI untuk melakukan streaming konten. Ini juga berarti skrip Python diblokir menunggu kontrol ini selesai.

**Daftar 7.6** `chatgpt_clone_streaming.py` (bagian yang relevan)

```python
with st.chat_message("assistant"):
    stream = client.chat.completions.create(
        model=st.session_state["openai_model"],
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,    #1
    )
    response = st.write_stream(stream)    #2
st.session_state.messages.append(
{"role": "assistant", "content": response})     #3
```

1. Mengatur stream ke True untuk memulai streaming pada API
2. Menggunakan kontrol stream untuk menulis stream ke antarmuka
3. Menambahkan respons ke riwayat status pesan setelah stream selesai

Debug halaman dengan menekan F5 dan tunggu hingga halaman dimuat. Masukkan kueri, dan Anda akan melihat bahwa responsnya di-streaming ke jendela secara real time, seperti yang ditunjukkan pada gambar 7.6. Dengan hilangnya spinner, pengalaman pengguna ditingkatkan dan tampak lebih responsif.

![gambar](Images/7-6.png)

**Gambar 7.6** Antarmuka yang diperbarui dengan streaming respons teks

Bagian ini menunjukkan betapa relatif sederhananya menggunakan Streamlit untuk membuat antarmuka web Python. Nexus menggunakan antarmuka Streamlit karena mudah digunakan dan dimodifikasi hanya dengan Python. Seperti yang akan Anda lihat di bagian selanjutnya, ini memungkinkan berbagai konfigurasi untuk mendukung aplikasi yang lebih kompleks.

## 7.3 Mengembangkan profil dan persona untuk agen

Nexus menggunakan profil agen untuk mendeskripsikan fungsi dan kemampuan agen. Gambar 7.7 mengingatkan kita pada komponen agen utama dan bagaimana komponen tersebut akan disusun di seluruh buku ini.

![gambar](Images/7-7.png)

**Gambar 7.7** Profil agen saat dipetakan ke definisi file YAML

Untuk saat ini, pada saat penulisan ini, Nexus hanya mendukung bagian persona dan tindakan dari profil. Gambar 7.7 menunjukkan profil bernama Fritz, beserta persona dan tindakannya. Tambahkan profil agen apa pun ke Nexus dengan menyalin file profil YAML agen ke dalam folder `Nexus/ nexus/nexus_base/nexus_profiles`.

Nexus menggunakan sistem plugin untuk secara dinamis menemukan berbagai komponen dan profil saat ditempatkan di folder masing-masing. Folder `nexus_profiles` menyimpan definisi YAML untuk agen.

Kita dapat dengan mudah mendefinisikan profil agen baru dengan membuat file YAML baru di folder `nexus_profiles`. Daftar 7.7 menunjukkan contoh profil baru dengan persona yang sedikit diperbarui. Untuk mengikuti, pastikan VS Code terbuka ke folder kode sumber `chapter_07` dan instal Nexus dalam mode pengembang (lihat daftar 7.7). Kemudian, buat file `fiona.yaml` di folder `Nexus/nexus/nexus_base/nexus_profiles`.

**Daftar 7.7** `fiona.yaml` (buat file ini)

```yaml
agentProfile:
  name: "Finona"
  avatar: "👹"    #1
  persona: "Anda adalah AI yang sangat banyak bicara yang
 tahu dan mengerti segalanya dalam hal
 Ogre. Anda selalu menjawab dalam bahasa Ogre yang samar."   #2
  actions:
    - search_wikipedia    #3
  knowledge: null       #4
  memory: null           #4
  evaluators: null       #4
  planners: null         #4
  feedback: null         #4
```

1. Avatar teks yang digunakan untuk mewakili persona
2. Persona mewakili prompt sistem dasar.
3. Fungsi tindakan yang dapat digunakan agen
4. Saat ini tidak didukung

Setelah menyimpan file, Anda dapat memulai Nexus dari baris perintah atau menjalankannya dalam mode debug dengan membuat konfigurasi peluncuran baru di folder `.vscode/launch.json`, seperti yang ditunjukkan pada daftar berikutnya. Kemudian, simpan file dan alihkan konfigurasi debug Anda untuk menggunakan konfigurasi web Nexus.

**Daftar 7.8** `.vscode/launch.json` (menambahkan peluncuran debug)

```json
{
      "name": "Python Debugger: Nexus Web",
      "type": "debugpy",
      "request": "launch",
      "module": "streamlit",
      "args": ["run", " Nexus/nexus/streamlit_ui.py"]     #1
    },
```

1. Anda mungkin harus menyesuaikan jalur ini jika lingkungan virtual Anda berbeda.

Saat Anda menekan F5 atau memilih Run > Start Debugging dari menu, antarmuka Streamlit Nexus akan diluncurkan. Silakan jalankan Nexus dalam mode debug. Setelah terbuka, buat utas baru, lalu pilih OpenAIAgent standar dan persona baru Anda, seperti yang ditunjukkan pada gambar 7.8.

![gambar](Images/7-8.png)

**Gambar 7.8** Memilih dan mengobrol dengan persona baru

Pada titik ini, profil bertanggung jawab untuk mendefinisikan prompt sistem agen. Anda dapat melihat ini di gambar 7.8, di mana kami meminta Finona untuk mengeja kata *clock*, dan dia merespons dalam semacam bahasa ogre. Dalam hal ini, kami menggunakan persona sebagai kepribadian, tetapi seperti yang telah kita lihat sebelumnya, prompt sistem juga dapat berisi aturan dan opsi lain.

Profil dan persona adalah definisi dasar tentang bagaimana agen berinteraksi dengan pengguna atau sistem lain. Untuk mendukung profil, diperlukan mesin agen. Di bagian selanjutnya, kita akan membahas implementasi dasar dari mesin agen.

## 7.4 Mendukung agen dan memahami mesin agen

Mesin agen mendukung agen di dalam Nexus. Mesin ini dapat diikat ke platform alat tertentu, seperti SK, dan/atau bahkan LLM yang berbeda, seperti Anthropic Claude atau Google Gemini. Dengan menyediakan abstraksi agen dasar, Nexus seharusnya dapat mendukung alat atau model apa pun sekarang dan di masa depan.

Saat ini, Nexus hanya mengimplementasikan agen yang didukung API OpenAI. Kita akan melihat bagaimana agen dasar didefinisikan dengan membuka file `agent_manager.py` dari folder `Nexus/nexus/nexus_base`.

Daftar 7.9 menunjukkan fungsi kelas `BaseAgent`. Saat membuat mesin agen baru, Anda perlu membuat subkelas dari kelas ini dan mengimplementasikan berbagai alat/tindakan dengan implementasi yang sesuai.

**Daftar 7.9** `agent_manager.py:BaseAgent`

```python
class BaseAgent:
    def __init__(self, chat_history=None):
        self._chat_history = chat_history or []
        self.last_message = ""
        self._actions = []
        self._profile = None

    async def get_response(self, 
                            user_input, 
                            thread_id=None):     #1
        raise NotImplementedError("Metode ini harus diimplementasikan...")

    async def get_semantic_response(self, 
                                     prompt, 
                                     thread_id=None):    #2
        raise NotImplementedError("Metode ini harus...")

    def get_response_stream(self, 
                             user_input, 
                             thread_id=None):     #3
        raise NotImplementedError("Metode ini harus...")

    def append_chat_history(self, 
                             thread_id, 
                             user_input, 
                             response):     #4
        self._chat_history.append(
            {"role": "user",
             "content": user_input,
             "thread_id": thread_id}
        )
        self._chat_history.append(
            {"role": "bot",
             "content": response, 
             "thread_id": thread_id}
        )

    def load_chat_history(self):      #5
        raise NotImplementedError(
                 "Metode ini harus diimplementasikan...")

    def load_actions(self):    #6
        raise NotImplementedError(
                 "Metode ini harus diimplementasikan...")

#... tidak ditampilkan – properti setter/getter
```

1. Memanggil LLM dan mengembalikan respons
2. Menjalankan fungsi semantik
3. Memanggil LLM dan mengembalikan respons
4. Menambahkan pesan ke riwayat obrolan internal agen
5. Memuat riwayat obrolan dan memungkinkan agen untuk memuat ulang berbagai riwayat
6. Memuat tindakan yang tersedia untuk digunakan agen

Buka file `nexus_agents/oai_agent.py` di VS Code. Daftar 7.10 menunjukkan implementasi mesin agen dari fungsi `get_response` yang secara langsung menggunakan API OpenAI. `self.client` adalah klien OpenAI yang dibuat sebelumnya selama inisialisasi kelas, dan sisa kode yang telah Anda lihat digunakan dalam contoh sebelumnya.

**Daftar 7.10** `oai_agent.py` (`get_response`)

```python
async def get_response(self, user_input, thread_id=None):
    self.messages += [{"role": "user",
                     "content": user_input}]     #1
    response = self.client.chat.completions.create(    #2
        model=self.model,
        messages=self.messages,
        temperature=0.7,     #3
    )
    self.last_message = str(response.choices[0].message.content)
    return self.last_message    #4
```

1. Menambahkan user_input ke tumpukan pesan
2. Klien dibuat sebelumnya dan sekarang digunakan untuk membuat penyelesaian obrolan.
3. Suhu di-hardcode tetapi dapat dikonfigurasi.
4. Mengembalikan respons dari panggilan penyelesaian obrolan

Seperti profil agen, Nexus menggunakan sistem plugin yang memungkinkan Anda menempatkan definisi mesin agen baru di folder `nexus_agents`. Jika Anda membuat agen Anda sendiri, itu hanya perlu ditempatkan di folder ini agar Nexus dapat menemukannya.

Kita tidak perlu menjalankan contoh karena kita sudah melihat bagaimana OpenAIAgent bekerja. Di bagian selanjutnya, kita akan melihat fungsi agen yang dapat dikembangkan, ditambahkan, dan digunakan oleh agen.

## 7.5 Memberi agen tindakan dan alat

Seperti SK, Nexus mendukung fungsi asli (kode) dan semantik (prompt). Namun, tidak seperti SK, mendefinisikan dan menggunakan fungsi di dalam Nexus lebih mudah. Yang perlu Anda lakukan hanyalah menulis fungsi ke dalam file Python dan menempatkannya di folder `nexus_actions`.

Untuk melihat betapa mudahnya mendefinisikan fungsi, buka folder `Nexus/nexus/nexus_base/nexus_actions`, dan buka file `test_actions.py`. Daftar 7.11 menunjukkan dua definisi fungsi. Fungsi pertama adalah contoh sederhana dari fungsi kode/asli, dan yang kedua adalah fungsi prompt/semantik.

**Daftar 7.11** `test_actions.py` (definisi fungsi asli/semantik)

```python
from nexus.nexus_base.action_manager import agent_action


@agent_action                                             #1
def get_current_weather(location, unit="fahrenheit"):     #1
    """Dapatkan cuaca saat ini di lokasi tertentu"""     #2
    return f"""
Cuaca saat ini di {location} adalah 0 {unit}.
"""     #3


@agent_action     #4
def recommend(topic):
    """
    Sistem:                                                  #5
        Berikan rekomendasi untuk {topic} tertentu.
        Gunakan penilaian terbaik Anda untuk memberikan rekomendasi.
    Pengguna:
        tolong gunakan penilaian terbaik Anda
        untuk memberikan rekomendasi untuk {topic}.           #5
    """
    pass     #6
```

1. Menerapkan dekorator agent_action untuk membuat fungsi menjadi tindakan
2. Menetapkan komentar deskriptif untuk fungsi tersebut
3. Kodenya bisa sesederhana atau sekompleks yang dibutuhkan.
4. Menerapkan dekorator agent_action untuk membuat fungsi menjadi tindakan
5. Komentar fungsi menjadi prompt dan dapat menyertakan placeholder.
6. Fungsi semantik tidak mengimplementasikan kode apa pun.

Tempatkan kedua fungsi di folder `nexus_actions`, dan fungsi tersebut akan ditemukan secara otomatis. Menambahkan dekorator `agent_action` memungkinkan fungsi untuk diperiksa dan secara otomatis menghasilkan spesifikasi alat standar OpenAI. LLM kemudian dapat menggunakan spesifikasi alat ini untuk penggunaan alat dan pemanggilan fungsi.

Daftar 7.12 menunjukkan spesifikasi alat OpenAI yang dihasilkan untuk kedua fungsi, seperti yang ditunjukkan sebelumnya pada daftar 7.11. Fungsi semantik, yang menggunakan prompt, juga berlaku untuk deskripsi alat. Deskripsi alat ini dikirim ke LLM untuk menentukan fungsi mana yang akan dipanggil.

**Daftar 7.12** `test_actions`: Spesifikasi alat yang dihasilkan OpenAI

```json
{
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": 
        "Dapatkan cuaca saat ini di lokasi tertentu",   #1
        "parameters": {
            "type": "object",
            "properties": {     #2
                "location": {
                    "type": "string",
                    "description": "location"
                },
                "unit": {
                    "type": "string",
                    "enum": [
                        "celsius",
                        "fahrenheit"
                    ]
                }
            },
            "required": [
                "location"
            ]
        }
    }
}
{
    "type": "function",
    "function": {
        "name": "recommend",
        "description": """
    Sistem:
    Berikan rekomendasi untuk {topic} tertentu.
Gunakan penilaian terbaik Anda untuk memberikan rekomendasi.
Pengguna:
tolong gunakan penilaian terbaik Anda
untuk memberikan rekomendasi untuk {topic}.""",     #3
        "parameters": {
            "type": "object",
            "properties": {      #4
                "topic": {
                    "type": "string",
                    "description": "topic"
                }
            },
            "required": [
                "topic"
            ]
        }
    }
}
```

1. Komentar fungsi menjadi deskripsi alat fungsi.
2. Parameter input fungsi diekstraksi dan ditambahkan ke spesifikasi.
3. Komentar fungsi menjadi deskripsi alat fungsi.
4. Parameter input fungsi diekstraksi dan ditambahkan ke spesifikasi.

Mesin agen juga perlu mengimplementasikan kemampuan itu untuk mengimplementasikan fungsi dan komponen lainnya. Agen OpenAI telah diimplementasikan untuk mendukung pemanggilan fungsi paralel. Implementasi mesin agen lain akan diperlukan untuk mendukung versi penggunaan tindakan masing-masing. Untungnya, definisi alat OpenAI menjadi standar, dan banyak platform mematuhi standar ini.

Sebelum kita masuk ke demo tentang penggunaan alat, mari kita amati bagaimana agen OpenAI mengimplementasikan tindakan dengan membuka file `oai_agent.py` di VS Code. Daftar berikut menunjukkan bagian atas fungsi `get_response_stream` agen dan implementasi pemanggilan fungsinya.

**Daftar 7.13** Memanggil API di `get_response_stream`

```python
def get_response_stream(self, user_input, thread_id=None):
    self.last_message = ""
    self.messages += [{"role": "user", "content": user_input}]
    if self.tools and len(self.tools) > 0:   #1
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=self.tools,     #2
            tool_choice="auto",     #3
        )
    else:    #4
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
        )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls    #5
```

1. Mendeteksi apakah agen memiliki alat yang tersedia yang dihidupkan
2. Mengatur alat dalam panggilan penyelesaian obrolan
3. Memastikan bahwa LLM tahu itu dapat memilih alat apa pun
4. Jika tidak ada alat, panggil LLM dengan cara standar
5. Mendeteksi apakah ada alat yang digunakan oleh LLM

Eksekusi fungsi mengikuti, seperti yang ditunjukkan pada daftar 7.14. Kode ini menunjukkan bagaimana agen mendukung panggilan fungsi/alat paralel. Panggilan ini paralel karena agen mengeksekusi masing-masing secara bersamaan dan tanpa urutan. Di bab 11, kita akan melihat perencana yang memungkinkan tindakan dipanggil dalam urutan yang teratur.

**Daftar 7.14** `oai_agent.py` (`get_response_stream`: jalankan panggilan alat)

```python
if tool_calls:    #1
    available_functions = {
        action["name"]: action["pointer"] for action in self.actions
    }    #2
    self.messages.append(
        response_message
    )
    for tool_call in tool_calls:    #3
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(
            **function_args, _caller_agent=self
        )

        self.messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": str(function_response),
            }
        )
    second_response = self.client.chat.completions.create(
        model=self.model,
        messages=self.messages,
    )     #4
    response_message = second_response.choices[0].message
```

1. Lanjutkan jika panggilan alat terdeteksi dalam respons LLM
2. Memuat pointer ke implementasi fungsi aktual untuk eksekusi kode
3. Melakukan loop melalui semua panggilan yang ingin dipanggil LLM; bisa ada beberapa.
4. Melakukan panggilan LLM kedua dengan hasil panggilan alat

Untuk mendemonstrasikan ini, jalankan Nexus di debugger dengan menekan F5. Kemudian, pilih dua tindakan pengujian—`recommend` dan `get_current_weather`—dan persona/profil singkat Olly. Gambar 7.9 menunjukkan hasil memasukkan kueri dan agen merespons dengan menggunakan kedua alat dalam responsnya.

![gambar](Images/7-9.png)

**Gambar 7.9** Bagaimana agen dapat menggunakan alat secara paralel dan merespons dengan satu respons

Jika Anda perlu meninjau cara kerja tindakan agen ini secara lebih rinci, lihat bab 5. Kode yang mendasarinya lebih kompleks dan di luar cakupan ulasan di sini. Namun, Anda dapat meninjau kode Nexus untuk mendapatkan pemahaman yang lebih baik tentang bagaimana semuanya terhubung.

Sekarang, Anda dapat terus melatih berbagai opsi agen di dalam Nexus. Coba pilih profil/persona yang berbeda dengan fungsi lain, misalnya. Di bab berikutnya, kami mengungkap bagaimana agen dapat menggunakan memori dan pengetahuan eksternal menggunakan pola seperti Retrieval Augmented Generation (RAG).

## 7.6 Latihan

Gunakan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- **Latihan 1**—Jelajahi Dasar-Dasar Streamlit (Mudah)

Tujuan —Mendapatkan keakraban dengan Streamlit dengan membuat aplikasi web sederhana yang menampilkan teks yang dimasukkan oleh pengguna.

Tugas:

- Ikuti dokumentasi Streamlit untuk menyiapkan aplikasi dasar.
- Tambahkan input teks dan tombol. Saat tombol diklik, tampilkan teks yang dimasukkan oleh pengguna di layar.

- **Latihan 2**—Buat Profil Agen Dasar

Tujuan —Memahami proses pembuatan dan penerapan profil agen di Nexus.

Tugas:

- Buat profil agen baru dengan persona unik. Persona ini harus memiliki tema atau karakteristik tertentu (misalnya, seorang sejarawan).
- Tentukan serangkaian respons dasar yang selaras dengan persona ini.
- Uji persona dengan berinteraksi dengannya melalui antarmuka Nexus.

- **Latihan 3**—Kembangkan Tindakan Kustom

Tujuan —Belajar memperluas fungsionalitas Nexus dengan mengembangkan tindakan kustom.

Tugas:

- Kembangkan tindakan baru (misalnya, `fetch_current_news`) yang terintegrasi dengan API tiruan untuk mengambil berita utama terbaru.
- Terapkan tindakan ini sebagai fungsi asli (kode) dan fungsi semantik (berbasis prompt).
- Uji tindakan di lingkungan Nexus untuk memastikan tindakan tersebut berfungsi seperti yang diharapkan.

- **Latihan 4**—Integrasikan API Pihak Ketiga

Tujuan —Meningkatkan kemampuan agen Nexus dengan mengintegrasikan API pihak ketiga yang sebenarnya.

Tugas:

- Pilih API publik (misalnya, API cuaca atau berita), dan buat tindakan baru yang mengambil data dari API ini.
- Gabungkan penanganan kesalahan dan pastikan agen dapat dengan anggun menangani kegagalan API atau respons yang tidak terduga.
- Uji integrasi secara menyeluruh di dalam Nexus.

## Ringkasan

- Nexus adalah platform pengembangan agen sumber terbuka yang digunakan bersama dengan buku ini. Ini dirancang untuk mengembangkan, menguji, dan menghosting agen AI dan dibangun di atas Streamlit untuk membuat dasbor interaktif dan antarmuka obrolan.
- Streamlit, kerangka kerja aplikasi web Python, memungkinkan pengembangan cepat dasbor dan aplikasi obrolan yang ramah pengguna. Kerangka kerja ini memfasilitasi eksplorasi dan interaksi dengan berbagai fitur agen secara efisien.
- Nexus mendukung pembuatan dan penyesuaian profil dan persona agen, memungkinkan pengguna untuk menentukan kepribadian dan perilaku agen mereka. Profil ini menentukan bagaimana agen berinteraksi dan merespons masukan pengguna.
- Platform Nexus memungkinkan pengembangan dan integrasi tindakan dan alat semantik (berbasis prompt) dan asli (berbasis kode) di dalam agen. Ini memungkinkan pembuatan agen yang sangat fungsional dan responsif.
- Sebagai platform sumber terbuka, Nexus dirancang untuk dapat diperluas, mendorong kontribusi dan penambahan fitur, alat, dan kemampuan agen baru oleh komunitas.
- Nexus fleksibel, mendukung berbagai opsi penerapan, termasuk antarmuka web, API, dan bot Discord di iterasi mendatang, mengakomodasi berbagai kebutuhan pengembangan dan pengujian.
