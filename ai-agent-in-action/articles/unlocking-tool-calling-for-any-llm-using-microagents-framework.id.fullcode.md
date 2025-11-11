# Membuka Panggilan Alat untuk LLM Apa Pun: Menggunakan Kerangka MicroAgents

Dalam pengembangan AI modern, mengoordinasikan beberapa agen model bahasa secara efisien menghadirkan tantangan yang signifikan. Untuk mengatasi hal ini, kerangka MicroAgents menghadirkan lapisan orkestrasi yang ringan dan fleksibel yang mendukung panggilan alat universal dengan ketergantungan minimal.

## Keterbatasan Kerangka Kerja yang Ada

Banyak solusi orkestrasi memperkenalkan kompleksitas yang tidak diinginkan — dan masih belum dapat mengaktifkan panggilan alat untuk berbagai model:

- **Panggilan alat terbatas**: Kerangka kerja seperti CrewAI, LangGraph, AutoGen, dan LangChain tidak dapat memanggil alat pada banyak model sumber terbuka atau on-prem (misalnya, Llama, DeepSeek, Phi-3, Gemma).
- **Ketergantungan yang membengkak**: Pustaka populer seringkali membutuhkan ratusan megabyte paket vendor dan integrasi.
- **Pengaturan yang kompleks**: Kode boilerplate yang ekstensif diperlukan sebelum satu agen dapat berjalan.
- **Keterikatan model**: Keterikatan yang erat dengan penyedia LLM tertentu dapat membatasi eksperimen.

Meskipun proyek-proyek ini menawarkan fitur-fitur canggih, mereka biasanya mencakup puluhan atau ratusan ribu baris kode dan membutuhkan puluhan megabyte pustaka tambahan — tetapi masih membuat LLM utama tidak dapat memanggil fungsi.

## MicroAgents: Alternatif yang Benar-benar Ringan

**MicroAgents** mengadopsi desain yang sangat minimalis:

- **~1K LOC**, **<1 MB** jejak instalasi
- Hanya **requests** dan **urllib3** sebagai ketergantungan
- Integrasi fungsi Python langsung — tanpa kelas pembungkus
- Kompatibel dengan **endpoint API gaya OpenAI apa pun**

## Fitur Utama yang Membedakan microAgents

### Dukungan Panggilan Alat Universal

Fitur menonjol dari microAgents adalah dukungan panggilan alat universalnya:

- Bekerja dengan **API LLM APA PUN** yang mengikuti format yang kompatibel dengan OpenAI
- Mengaktifkan panggilan fungsi/alat **bahkan dengan model yang tidak mendukungnya secara native**
- Menggunakan format panggilan alat berbasis XML yang intuitif dan mudah dibaca manusia

### Desain Ultra-Ringan

Dibandingkan dengan kerangka kerja lain:

- **LangGraph** — 37K LOC; +51 MB;
- **CrewAI** — 18K LOC; +173 MB;
- **AutoGen** — 7K LOC; +26 MB;
- **MicroAgents** — ~1K LOC; <1 MB;

### Integrasi Sederhana

MicroAgents menekankan kesederhanaan dan fleksibilitas:

- Integrasi fungsi langsung tanpa kelas pembungkus
- Bekerja dengan LLM apa pun yang mengikuti format API OpenAI
- Ketergantungan minimal, hanya pustaka HTTP inti yang diperlukan

## Memecahkan Hambatan Panggilan Alat

Karena panggilan fungsi secara historis terbatas pada model yang dihosting tingkat atas, pengembang menghadapi tiga pertukaran umum:

1. **Biaya**: Bergantung pada panggilan API yang mahal.
2. **Privasi**: Menerapkan on-premise dengan mengorbankan dukungan fitur.
3. **Spesialisasi**: Menggunakan LLM sumber terbuka khusus domain tanpa panggilan alat native.

MicroAgents menghilangkan batasan ini: **model** yang kompatibel dengan OpenAI dapat memanggil alat melalui protokol XML-nya. Ini berhasil mengaktifkan panggilan alat di beberapa LLM yang tidak mendukungnya secara native seperti:

- **GPT-4** — native ✓; microAgents ✓; CrewAI ✓; LangGraph ✓; AutoGen ✓
- **Claude 3** — native ✓; microAgents ✓; CrewAI ✓; LangGraph ✓; AutoGen ✓
- **Llama 3** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen✗
- **Mistral** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen ✗
- **Qwen** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen ✗
- **Phi-3** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen ✗
- **Gemma** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen✗

## Keunggulan Format XML

Ketika model tidak mendukung panggilan fungsi secara native, microAgents memandunya untuk menggunakan format XML terstruktur seperti:

```xml
<tool>
  <name>search_database</name>
  <parameters>
    <query>quantum computing</query>
  </parameters>
</tool>
```

Format XML ini:

- **Intuitif untuk LLM**: Bahkan model tanpa pelatihan panggilan fungsi khusus dapat memahami dan menghasilkan format ini
- **Mudah dibaca manusia**: Membuat debugging dan pengembangan jauh lebih mudah
- **Terstruktur dan dapat diurai**: Memungkinkan eksekusi yang andal terlepas dari model yang mendasarinya

## Instalasi Cepat

Memulai microAgents sangat sederhana:

```bash
# Instal langsung dari PyPI
pip install microAgents
```

Atau instal dari sumber untuk pengembangan:

```bash
git clone https://github.com/prabhjots664/MicroAgents.git
cd MicroAgents
pip install -e .
```

## Contoh Dasar: Membuat Agen Matematika

Berikut adalah contoh lengkap yang menunjukkan cara membuat agen matematika:

```python
from microAgents.llm import LLM
from microAgents.core import MicroAgent, Tool, BaseMessageStore

# Inisialisasi LLM dengan API Anda
llm = LLM(
    base_url="https://api.example.com/v1",  # Ganti dengan endpoint API Anda
    api_key="your-api-key",
    model="your-preferred-model",
    max_tokens=4000,
    temperature=0.8,
    top_p=0.9
)
# Definisikan alat untuk operasi matematika dasar
def add_numbers(a: float, b: float) -> float:
    return a + b
def multiply_numbers(a: float, b: float) -> float:
    return a * b
# Buat agen matematika
math_agent = MicroAgent(
    llm=llm,
    prompt="Anda adalah asisten matematika. Tangani operasi aritmatika dasar.",
    toolsList=[
        Tool(description="Tambahkan dua angka", func=add_numbers),
        Tool(description="Kalikan dua angka", func=multiply_numbers)
    ]
)
# Buat penyimpanan pesan untuk riwayat percakapan
message_store = BaseMessageStore()
# Gunakan agen
response = math_agent.execute_agent(
    "Pertama tambahkan 3 dan 5, lalu kalikan hasilnya dengan 2",
    message_store
)
print(response)
```

## Membangun Sistem Multi-Agen dengan Orkestrasi

Di sinilah microAgents benar-benar bersinar dalam kemampuannya untuk membuat dan mengoordinasikan beberapa agen khusus:

```python
"""Demo end-to-end sederhana dengan agen matematika dan orkestrator."""

from microAgents.llm import LLM
from microAgents.core import MicroAgent, Tool, BaseMessageStore

# Inisialisasi LLM
math_llm = LLM(
    base_url="https://api.hyperbolic.xyz/v1",
    api_key="YOUR_API_KEY",
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    max_tokens=4000,
    temperature=0.8,
    top_p=0.9
)

# Definisikan alat
def add_numbers(a: float, b: float) -> float:
    """Menambahkan dua angka."""
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """Mengalikan dua angka."""
    return a * b

def factorial(n: int) -> int:
    """Menghitung faktorial suatu angka."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Buat agen
simple_math_agent = MicroAgent(
    llm=math_llm,
    prompt="""Anda adalah asisten matematika sederhana. Tangani operasi aritmatika dasar.""",
    toolsList=[
        Tool(description="Menambahkan dua angka", func=add_numbers),
        Tool(description="Mengalikan dua angka", func=multiply_numbers)
    ]
)

advanced_math_agent = MicroAgent(
    llm=math_llm,
    prompt="""Anda adalah asisten matematika tingkat lanjut. Tangani operasi matematika kompleks.""",
    toolsList=[
        Tool(description="Menghitung faktorial", func=factorial)
    ]
)

class Orchestrator(MicroAgent):
    def __init__(self):
        super().__init__(
            llm=math_llm,
            prompt="""Anda adalah penganalisis kueri matematika. Untuk setiap kueri:
1. Jika berisi aritmatika dasar (penjumlahan, pengurangan, perkalian, pembagian), keluarkan persis: SIMPLE_MATHS NEEDED
2. Jika berisi matematika tingkat lanjut (faktorial, eksponen, logaritma, turunan, integral), keluarkan persis: ADVANCED_MATHS NEEDED
3. Jika tidak yakin, keluarkan persis: UNKNOWN_MATH_TYPE

Contoh:
- "Berapa 5 ditambah 3?" → SIMPLE_MATHS NEEDED
- "Hitung 10 faktorial" → ADVANCED_MATHS NEEDED
- "Selesaikan x^2 + 2x + 1 = 0" → UNKNOWN_MATH_TYPE

Selalu keluarkan persis salah satu dari tiga opsi ini, tidak ada yang lain.""",
            toolsList=[]
        )
        self.simple_math_agent = simple_math_agent
        self.advanced_math_agent = advanced_math_agent

    def execute_agent(self, query: str, message_store: BaseMessageStore) -> str:
        """Tangani alur kueri penuh melalui orkestrator."""
        print(f"\nDebug: Orkestrator menganalisis kueri: {query}")
        
        # Dapatkan analisis awal dari orkestrator
        analysis = super().execute_agent(query, message_store)
        print(f"Debug: Hasil analisis orkestrator: {analysis}")
        
        if "SIMPLE_MATHS NEEDED" in analysis:
            print("Debug: Merutekan ke Agen Matematika Sederhana")
            result = self.simple_math_agent.execute_agent(query, message_store)
            print(f"Debug: Hasil Agen Matematika Sederhana: {result}")
            return self._format_result("Agen Matematika Sederhana", result)
        elif "ADVANCED_MATHS NEEDED" in analysis:
            print("Debug: Merutekan ke Agen Matematika Tingkat Lanjut")
            result = self.advanced_math_agent.execute_agent(query, message_store)
            print(f"Debug: Hasil Agen Matematika Tingkat Lanjut: {result}")
            return self._format_result("Agen Matematika Tingkat Lanjut", result)
        else:
            return "Orkestrator: Tidak dapat menentukan agen yang sesuai untuk kueri ini."

    def _format_result(self, agent_name: str, result: str) -> str:
        """Format hasil akhir dari agen."""
        return f"Orkestrator: Hasil dari {agent_name}:\n{result}"

def main():
    message_store = BaseMessageStore()
    orchestrator = Orchestrator()
    
    # Contoh kueri yang menunjukkan panggilan alat gaya XML
    queries = [
        "Berapa 15 ditambah 27?",
        "Hitung 5 faktorial",
        "Kalikan 8 dengan 9",
        "Pertama tambahkan 3 dan 5, lalu kalikan hasilnya dengan 2"
    ]
    
    for query in queries:
        print(f"\nPengguna: {query}")
        response = orchestrator.execute_agent(query, message_store)
        print(f"{response}")

if __name__ == "__main__":
    main()
```

## Contoh Praktis: Asisten Basis Data dengan Llama 3

Berikut adalah contoh yang menunjukkan bagaimana microAgents mengaktifkan panggilan alat dengan Llama 3, yang tidak mendukung panggilan fungsi secara native:

```python
from microAgents.llm import LLM
from microAgents.core import MicroAgent, Tool, BaseMessageStore

# Inisialisasi dengan Llama 3 (yang tidak mendukung panggilan fungsi secara native)
llm = LLM(
    base_url="https://api.together.xyz/v1",
    api_key="your-api-key",
    model="meta-llama/Llama-3-8b-instruct",
    max_tokens=2000
)
# Definisikan alat basis data
def query_database(table: str, filter_condition: str = None) -> list:
    # Kueri basis data simulasi
    if table == "customers":
        return ["Customer1", "Customer2", "Customer3"]
    return ["Tidak ada data yang ditemukan"]
def insert_record(table: str, data: dict) -> str:
    # Operasi penyisipan simulasi
    return f"Catatan dimasukkan ke dalam {table}"
# Buat agen basis data
db_agent = MicroAgent(
    llm=llm,  # Llama 3 tidak memiliki panggilan fungsi native!
    prompt="Anda adalah asisten basis data. Bantu pengguna berinteraksi dengan basis data.",
    toolsList=[
        Tool(description="Kueri tabel basis data dengan filter opsional", func=query_database),
        Tool(description="Sisipkan catatan ke dalam tabel basis data", func=insert_record)
    ]
)
# Jalankan kueri - dengan dukungan panggilan alat penuh!
result = db_agent.execute_agent("Tampilkan semua pelanggan di basis data", BaseMessageStore())
print(result)
```

## Kasus Penggunaan Dunia Nyata

- **Prototyping**: Bukti konsep multi-agen yang cepat
- **Produksi**: Penerapan ringan dalam layanan mikro
- **Edge/IoT**: Beroperasi dalam batasan sumber daya
- **LLM Kustom**: Endpoint API yang kompatibel dengan OpenAI

## Jalan ke Depan

Sebagai proyek sumber terbuka, MicroAgents menyambut kontribusi untuk:

- Memperluas ekosistem alatnya
- Memberikan lebih banyak templat dan contoh
- Meningkatkan orkestrasi (streaming, async)
- UI Tanpa Kode/Kode Rendah yang mudah untuk membangun sistem multi-agen.