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
- Only **requests** and **urllib3** as dependencies
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

| Model      | native | microAgents | CrewAI | LangGraph | AutoGen |
| :--------- | :----- | :---------- | :----- | :-------- | :------ |
| **GPT-4**  | ✓      | ✓           | ✓      | ✓         | ✓       |
| **Claude 3** | ✓      | ✓           | ✓      | ✓         | ✓       |
| **Llama 3** | ✗      | ✓           | ✗      | ✗         | ✗       |
| **Mistral** | ✗      | ✓           | ✗      | ✗         | ✗       |
| **Qwen**   | ✗      | ✓           | ✗      | ✗         | ✗       |
| **Phi-3**  | ✗      | ✓           | ✗      | ✗         | ✗       |
| **Gemma**  | ✗      | ✓           | ✗      | ✗         | ✗       |

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
- **Terstruktur dan dapat diurai**: Memungkinkan eksekusi yang اندal terlepas dari model yang mendasarinya

## Instalasi Cepat

Memulai microAgents sangat sederhana:

```bash
# Install directly from PyPI
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

# Initialize LLM with your API
llm = LLM(
    base_url="https://api.example.com/v1",  # Replace with your API endpoint
    api_key="your-api-key",
    model="your-preferred-model",
    max_tokens=4000,
    temperature=0.8,
    top_p=0.9
)
# Define tools for basic math operations
def add_numbers(a: float, b: float) -> float:
    return a + b
def multiply_numbers(a: float, b: float) -> float:
    return a * b
# Create math agent
math_agent = MicroAgent(
    llm=llm,
    prompt="You are a math assistant. Handle basic arithmetic operations.",
    toolsList=[
        Tool(description="Add two numbers", func=add_numbers),
        Tool(description="Multiply two numbers", func=multiply_numbers)
    ]
)
# Create message store for conversation history
message_store = BaseMessageStore()
# Use the agent
response = math_agent.execute_agent(
    "First add 3 and 5, then multiply the result by 2",
    message_store
)
print(response)
```

## Membangun Sistem Multi-Agen dengan Orkestrasi

Di sinilah microAgents benar-benar bersinar dalam kemampuannya untuk membuat dan mengoordinasikan beberapa agen khusus:

```python
"""Simple end-to-end demo with math agents and orchestrator."""

from microAgents.llm import LLM
from microAgents.core import MicroAgent, Tool, BaseMessageStore

# Initialize LLM
math_llm = LLM(
    base_url="https://api.hyperbolic.xyz/v1",
    api_key="YOUR_API_KEY",
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    max_tokens=4000,
    temperature=0.8,
    top_p=0.9
)

# Define tools
def add_numbers(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

def factorial(n: int) -> int:
    """Calculates factorial of a number."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Create agents
simple_math_agent = MicroAgent(
    llm=math_llm,
    prompt="""You are a simple math assistant. Handle basic arithmetic operations.""",
    toolsList=[
        Tool(description="Adds two numbers", func=add_numbers),
        Tool(description="Multiplies two numbers", func=multiply_numbers)
    ]
)

advanced_math_agent = MicroAgent(
    llm=math_llm,
    prompt="""You are an advanced math assistant. Handle complex math operations.""",
    toolsList=[
        Tool(description="Calculates factorial", func=factorial)
    ]
)

class Orchestrator(MicroAgent):
    def __init__(self):
        super().__init__(
            llm=math_llm,
            prompt="""You are a math query analyzer. For each query:
1. If it contains basic arithmetic (addition, subtraction, multiplication, division), output exactly: SIMPLE_MATHS NEEDED
2. If it contains advanced math (factorials, exponents, logarithms, derivatives, integrals), output exactly: ADVANCED_MATHS NEEDED
3. If unsure, output exactly: UNKNOWN_MATH_TYPE

Examples:
- "What is 5 plus 3?" → SIMPLE_MATHS NEEDED
- "Calculate 10 factorial" → ADVANCED_MATHS NEEDED
- "Solve x^2 + 2x + 1 = 0" → UNKNOWN_MATH_TYPE

Always output exactly one of these three options, nothing else.""",
            toolsList=[]
        )
        self.simple_math_agent = simple_math_agent
        self.advanced_math_agent = advanced_math_agent

    def execute_agent(self, query: str, message_store: BaseMessageStore) -> str:
        """Handle full query flow through orchestrator."""
        print(f"\nDebug: Orchestrator analyzing query: {query}")
        
        # Get initial analysis from orchestrator
        analysis = super().execute_agent(query, message_store)
        print(f"Debug: Orchestrator analysis result: {analysis}")
        
        if "SIMPLE_MATHS NEEDED" in analysis:
            print("Debug: Routing to Simple Math Agent")
            result = self.simple_math_agent.execute_agent(query, message_store)
            print(f"Debug: Simple Math Agent result: {result}")
            return self._format_result("Simple Math Agent", result)
        elif "ADVANCED_MATHS NEEDED" in analysis:
            print("Debug: Routing to Advanced Math Agent")
            result = self.advanced_math_agent.execute_agent(query, message_store)
            print(f"Debug: Advanced Math Agent result: {result}")
            return self._format_result("Advanced Math Agent", result)
        else:
            return "Orchestrator: Unable to determine the appropriate agent for this query."

    def _format_result(self, agent_name: str, result: str) -> str:
        """Format the final result from an agent."""
        return f"Orchestrator: Result from {agent_name}:\n{result}"

def main():
    message_store = BaseMessageStore()
    orchestrator = Orchestrator()
    
    # Example queries that demonstrate XML-style tool calls
    queries = [
        "What is 15 plus 27?",
        "Calculate 5 factorial",
        "Multiply 8 by 9",
        "First add 3 and 5, then multiply the result by 2"
    ]
    
    for query in queries:
        print(f"\nUser: {query}")
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

# Initialize with Llama 3 (which doesn't natively support function calling)
llm = LLM(
    base_url="https://api.together.xyz/v1",
    api_key="your-api-key",
    model="meta-llama/Llama-3-8b-instruct",
    max_tokens=2000
)
# Define database tools
def query_database(table: str, filter_condition: str = None) -> list:
    # Simulated database query
    if table == "customers":
        return ["Customer1", "Customer2", "Customer3"]
    return ["No data found"]
def insert_record(table: str, data: dict) -> str:
    # Simulated insert operation
    return f"Record inserted into {table}"
# Create database agent
db_agent = MicroAgent(
    llm=llm,  # Llama 3 doesn't have native function calling!
    prompt="You are a database assistant. Help users interact with databases.",
    toolsList=[
        Tool(description="Query database table with optional filter", func=query_database),
        Tool(description="Insert record into database table", func=insert_record)
    ]
)
# Execute query - with full tool calling support!
result = db_agent.execute_agent("Show me all customers in the database", BaseMessageStore())
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