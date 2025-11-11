# Memahami memori dan pengetahuan agen

## Bab ini mencakup
- Pengambilan dalam pengetahuan/memori dalam fungsi AI
- Membangun alur kerja pembuatan yang ditambah dengan pengambilan dengan LangChain
- Pembuatan yang ditambah dengan pengambilan untuk sistem pengetahuan agentik di Nexus
- Pola pengambilan untuk memori dalam agen
- Meningkatkan sistem pengambilan yang ditambah dengan kompresi memori dan pengetahuan

Sekarang setelah kita menjelajahi tindakan agen menggunakan alat eksternal, seperti plugin dalam bentuk fungsi asli atau semantik, kita dapat melihat peran memori dan pengetahuan menggunakan pengambilan di agen dan antarmuka obrolan. Kami akan menjelaskan memori dan pengetahuan dan bagaimana keduanya berhubungan dengan strategi rekayasa prompt, dan kemudian, untuk memahami pengetahuan memori, kami akan menyelidiki pengindeksan dokumen, membangun sistem pengambilan dengan LangChain, menggunakan memori dengan LangChain, dan membangun memori semantik menggunakan Nexus.

## 8.1 Memahami pengambilan dalam aplikasi AI

Pengambilan dalam aplikasi agen dan obrolan adalah mekanisme untuk memperoleh pengetahuan untuk disimpan dalam penyimpanan yang biasanya eksternal dan berumur panjang. Pengetahuan tidak terstruktur mencakup riwayat percakapan atau tugas, fakta, preferensi, atau item lain yang diperlukan untuk mengontekstualisasikan prompt. Pengetahuan terstruktur, yang biasanya disimpan dalam basis data atau file, diakses melalui fungsi atau plugin asli.

Memori dan pengetahuan, seperti yang ditunjukkan pada gambar 8.1, adalah elemen yang digunakan untuk menambahkan konteks dan informasi yang relevan lebih lanjut ke sebuah prompt. Prompt dapat ditambah dengan segala sesuatu mulai dari informasi tentang dokumen hingga tugas atau percakapan sebelumnya dan informasi referensi lainnya.

![figure](Images/8-1.png)

**Gambar 8.1** Memori, pengambilan, dan augmentasi prompt menggunakan strategi rekayasa prompt berikut: Gunakan Alat Eksternal dan Sediakan Teks Referensi.

Strategi rekayasa prompt yang ditunjukkan pada gambar 8.1 dapat diterapkan pada memori dan pengetahuan. Pengetahuan tidak dianggap sebagai memori melainkan augmentasi dari prompt dari dokumen yang ada. Baik pengetahuan maupun memori menggunakan pengambilan sebagai dasar bagaimana informasi tidak terstruktur dapat ditanyakan.

Mekanisme pengambilan, yang disebut retrieval augmented generation (RAG), telah menjadi standar untuk menyediakan konteks yang relevan dengan sebuah prompt. Mekanisme persis yang mendukung RAG juga mendukung memori/pengetahuan, dan penting untuk memahami cara kerjanya. Di bagian selanjutnya, kita akan memeriksa apa itu RAG.

## 8.2 Dasar-dasar retrieval augmented generation (RAG)

RAG telah menjadi mekanisme populer untuk mendukung obrolan dokumen atau obrolan tanya jawab. Sistem ini biasanya bekerja dengan pengguna yang menyediakan dokumen yang relevan, seperti PDF, dan kemudian menggunakan RAG dan model bahasa besar (LLM) untuk menanyakan dokumen tersebut.

Gambar 8.2 menunjukkan bagaimana RAG dapat memungkinkan sebuah dokumen untuk ditanyakan menggunakan LLM. Sebelum dokumen apa pun dapat ditanyakan, dokumen tersebut harus dimuat terlebih dahulu, diubah menjadi potongan-potongan konteks, disematkan ke dalam vektor, dan disimpan dalam basis data vektor.

![figure](Images/8-2.png)

**Gambar 8.2** Dua fase RAG: pertama, dokumen harus dimuat, diubah, disematkan, dan disimpan, dan, kedua, dokumen tersebut dapat ditanyakan menggunakan pembuatan yang ditambah.

Seorang pengguna dapat menanyakan dokumen yang diindeks sebelumnya dengan mengirimkan kueri. Kueri itu kemudian disematkan ke dalam representasi vektor untuk mencari potongan serupa di basis data vektor. Konten yang mirip dengan kueri kemudian digunakan sebagai konteks dan diisi ke dalam prompt sebagai augmentasi. Prompt didorong ke LLM, yang dapat menggunakan informasi konteks untuk membantu menjawab kueri.

Konsep memori/pengetahuan *tidak terstruktur* mengandalkan beberapa format pencarian kesamaan teks mengikuti pola pengambilan yang ditunjukkan pada gambar 8.2. Gambar 8.3 menunjukkan bagaimana memori menggunakan komponen penyematan dan basis data vektor yang sama. Alih-alih memuat dokumen terlebih dahulu, percakapan atau bagian dari percakapan disematkan dan disimpan ke basis data vektor.

![figure](Images/8-3.png)

**Gambar 8.3** Pengambilan memori untuk pembuatan yang ditambah menggunakan pola penyematan yang sama untuk mengindeks item ke basis data vektor.

Pola pengambilan dan pengindeksan dokumen memiliki nuansa dan memerlukan pertimbangan yang cermat untuk dapat digunakan dengan sukses. Ini memerlukan pemahaman tentang bagaimana data disimpan dan diambil, yang akan kita mulai buka di bagian selanjutnya.

## 8.3 Menyelidiki pencarian semantik dan pengindeksan dokumen

Pengindeksan dokumen mengubah informasi dokumen agar lebih mudah dipulihkan. Bagaimana indeks akan ditanyakan atau dicari juga memainkan faktor, apakah mencari sekumpulan kata tertentu atau ingin mencocokkan frasa demi frasa.

Pencarian *semantik* adalah pencarian konten yang cocok dengan frasa yang dicari berdasarkan kata dan makna. Kemampuan untuk mencari berdasarkan makna, secara semantik, sangat kuat dan layak untuk diselidiki secara rinci. Di bagian selanjutnya, kita melihat bagaimana pencarian kesamaan vektor dapat meletakkan kerangka kerja untuk pencarian semantik.

### 8.3.1 Menerapkan pencarian kesamaan vektor

Mari kita lihat sekarang bagaimana sebuah dokumen dapat diubah menjadi *vektor semantik,* atau representasi teks yang kemudian dapat digunakan untuk melakukan pencocokan jarak atau kesamaan. Ada banyak cara untuk mengubah teks menjadi vektor semantik, jadi kita akan melihat yang sederhana.

Buka folder `chapter_08` di ruang kerja Visual Studio Code (VS Code) yang baru. Buat lingkungan baru dan `pip` `install` file `requirements.txt` untuk semua dependensi bab. Jika Anda memerlukan bantuan untuk menyiapkan lingkungan Python baru, lihat apendiks B.

Sekarang buka file `document_vector_similarity.py` di VS Code, dan tinjau bagian atas di daftar 8.1. Contoh ini menggunakan Term Frequency–Inverse Document Frequency (TF–IDF). Statistik numerik ini mencerminkan seberapa penting sebuah kata bagi sebuah dokumen dalam koleksi atau kumpulan dokumen dengan meningkat secara proporsional dengan jumlah kemunculan kata dalam dokumen dan diimbangi oleh frekuensi kata dalam kumpulan dokumen. TF–IDF adalah ukuran klasik untuk memahami pentingnya satu dokumen dalam satu set dokumen.

**Daftar 8.1** `document_vector_similarity` (transformasi ke vektor)
```
import plotly.graph_objects as go
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [     #1
    "The sky is blue and beautiful.",
    "Love this blue and beautiful sky!",
    "The quick brown fox jumps over the lazy dog.",
    "A king's breakfast has sausages, ham, bacon, eggs, toast, and beans",
    "I love green eggs, ham, sausages and bacon!",
    "The brown fox is quick and the blue dog is lazy!",
    "The sky is very blue and the sky is very beautiful today",
    "The dog is lazy but the brown fox is quick!"
]

vectorizer = TfidfVectorizer()    #2
X = vectorizer.fit_transform(documents)     #3
```
*#1 Contoh dokumen*
*#2 Vektorisasi menggunakan TF–IDF*
*#3 Vektorisasi dokumen.*

Mari kita pecah TF–IDF menjadi dua komponennya menggunakan kalimat contoh, "Langit itu biru dan indah," dan berfokus pada kata *biru*.

#### Frekuensi Istilah (TF)

*Frekuensi Istilah* mengukur seberapa sering suatu istilah muncul dalam sebuah dokumen. Karena kita hanya mempertimbangkan satu dokumen (kalimat contoh kita), bentuk paling sederhana dari TF untuk *biru* dapat dihitung sebagai jumlah kemunculan *biru* dalam dokumen dibagi dengan jumlah total kata dalam dokumen. Mari kita hitung:

Jumlah kemunculan *biru* dalam dokumen: 1

Jumlah total kata dalam dokumen: 6

TF = 1 ÷ 6
TF = 0,16

#### Frekuensi Dokumen Terbalik (IDF)

*Frekuensi Dokumen Terbalik* mengukur seberapa penting suatu istilah dalam seluruh korpus. Ini dihitung dengan membagi jumlah total dokumen dengan jumlah dokumen yang mengandung istilah tersebut dan kemudian mengambil logaritma dari hasil bagi tersebut:

IDF = log(Jumlah total dokumen ÷ Jumlah dokumen yang mengandung kata tersebut)

Dalam contoh ini, korpus adalah kumpulan kecil dari delapan dokumen, dan *biru* muncul di empat dokumen ini.

IDF = log(8 ÷ 4)

#### Perhitungan TF–IDF

Akhirnya, skor TF–IDF untuk *biru* dalam kalimat contoh kita dihitung dengan mengalikan skor TF dan IDF:

TF–IDF = TF × IDF

Mari kita hitung nilai aktual untuk TF–IDF untuk kata *biru* menggunakan contoh yang diberikan; pertama, frekuensi istilah (seberapa sering kata itu muncul dalam dokumen) dihitung sebagai berikut:

TF = 1 ÷ 6

Dengan asumsi dasar logaritma adalah 10 (umumnya digunakan), frekuensi dokumen terbalik dihitung sebagai berikut:

IDF = log10 (8 ÷ 4)

Sekarang mari kita hitung nilai TF–IDF yang tepat untuk kata *biru* dalam kalimat, "Langit itu biru dan indah":

Frekuensi Istilah (TF) kira-kira 0,1670.

Frekuensi Dokumen Terbalik (IDF) kira-kira 0,301.

Jadi, skor TF–IDF (TF × IDF) untuk *biru* kira-kira 0,050.

Skor TF–IDF ini menunjukkan kepentingan relatif kata *biru* dalam dokumen yang diberikan (kalimat contoh) dalam konteks korpus yang ditentukan (delapan dokumen, dengan *biru* muncul di empat di antaranya). Skor TF–IDF yang lebih tinggi menyiratkan kepentingan yang lebih besar.

Kami menggunakan TF–IDF di sini karena mudah diterapkan dan dipahami. Sekarang setelah kita memiliki elemen yang direpresentasikan sebagai vektor, kita dapat mengukur kesamaan dokumen menggunakan kesamaan kosinus. Kesamaan kosinus adalah ukuran yang digunakan untuk menghitung kosinus sudut antara dua vektor bukan nol dalam ruang multidimensi, yang menunjukkan seberapa mirip keduanya, terlepas dari ukurannya.

Gambar 8.4 menunjukkan bagaimana jarak kosinus membandingkan representasi vektor dari dua potong atau dokumen teks. Kesamaan kosinus mengembalikan nilai dari –1 (tidak mirip) hingga 1 (identik). *Jarak kosinus* adalah nilai yang dinormalisasi mulai dari 0 hingga 2, yang diturunkan dengan mengambil 1 dikurangi kesamaan kosinus. Jarak kosinus 0 berarti item identik, dan 2 menunjukkan kebalikan total.

![figure](Images/8-4.png)

**Gambar 8.4** Bagaimana kesamaan kosinus diukur

Daftar 8.2 menunjukkan bagaimana kesamaan kosinus dihitung menggunakan fungsi `cosine_similarity` dari scikit-learn. Kesamaan dihitung untuk setiap dokumen terhadap semua dokumen lain dalam set. Matriks kesamaan yang dihitung untuk dokumen disimpan dalam variabel `cosine_similarities`. Kemudian, dalam loop input, pengguna dapat memilih dokumen untuk melihat kesamaannya dengan dokumen lain.

**Daftar 8.2** `document_vector_similarity` (kesamaan kosinus)
```
cosine_similarities = cosine_similarity(X)     #1

while True:     #2
    selected_document_index = input(f"Enter a document number (0-{len(documents)-1}) or 'exit' to quit: ").strip()

    if selected_document_index.lower() == 'exit':
        break

    if not selected_document_index.isdigit() or 
 not <= int(selected_document_index) < len(documents):
        print("Invalid input. Please enter a valid document number.")
        continue

    selected_document_index = int(selected_document_index)   #3

    selected_document_similarities = cosine_similarities[selected_document_index]    #4

# kode untuk memplot kesamaan dokumen dihilangkan
```
*#1 Menghitung kesamaan dokumen untuk semua pasangan vektor*
*#2 Loop input utama*
*#3 Mendapatkan indeks dokumen yang dipilih untuk dibandingkan*
*#4 Mengekstrak kesamaan yang dihitung terhadap semua dokumen*

Gambar 8.5 menunjukkan output dari menjalankan sampel di VS Code (F5 untuk mode debug). Setelah Anda memilih dokumen, Anda akan melihat kesamaan antara berbagai dokumen dalam set. Sebuah dokumen akan memiliki kesamaan kosinus 1 dengan dirinya sendiri. Perhatikan bahwa Anda tidak akan melihat kesamaan negatif karena vektorisasi TF–IDF. Kita akan melihat nanti cara lain yang lebih canggih untuk mengukur kesamaan semantik.

![figure](Images/8-5.png)

**Gambar 8.5** Kesamaan kosinus antara dokumen yang dipilih dan set dokumen

Metode vektorisasi akan menentukan ukuran kesamaan semantik antar dokumen. Sebelum kita beralih ke metode yang lebih baik untuk memvektorisasi dokumen, kita akan memeriksa penyimpanan vektor untuk melakukan pencarian kesamaan vektor.

### 8.3.2 Basis data vektor dan pencarian kesamaan

Setelah memvektorisasi dokumen, dokumen tersebut dapat disimpan dalam basis data vektor untuk pencarian kesamaan nanti. Untuk mendemonstrasikan cara kerjanya, kita dapat secara efisien mereplikasi basis data vektor sederhana dalam kode Python.

Buka `document_vector_database.py` di VS Code, seperti yang ditunjukkan pada daftar 8.3. Kode ini mendemonstrasikan pembuatan basis data vektor dalam memori dan kemudian memungkinkan pengguna memasukkan teks untuk mencari basis data dan mengembalikan hasil. Hasil yang dikembalikan menunjukkan teks dokumen dan skor kesamaan.

**Daftar 8.3** `document_vector_database.py`
```
# kode di atas dihilangkan
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
vector_database = X.toarray()    #1

def cosine_similarity_search(query,
                             database, 
                             vectorizer, 
                             top_n=5):    #2
    query_vec = vectorizer.transform([query]).toarray()
    similarities = cosine_similarity(query_vec, database)[0]
    top_indices = np.argsort(-similarities)[:top_n]  # Top n indices
    return [(idx, similarities[idx]) for idx in top_indices]

while True:     #3
    query = input("Enter a search query (or 'exit' to stop): ")
    if query.lower() == 'exit':
        break
    top_n = int(input("How many top matches do you want to see? "))
    search_results = cosine_similarity_search(query,
                                              vector_database, 
                                              vectorizer, 
                                              top_n)

    print("Top Matched Documents:")
    for idx, score in search_results:
        print(f"- {documents[idx]} (Score: {score:.4f})")  #4

    print("
")
###Keluaran
Enter a search query (or 'exit' to stop): blue
How many top matches do you want to see? 3
Top Matched Documents:
- The sky is blue and beautiful. (Score: 0.4080)
- Love this blue and beautiful sky! (Score: 0.3439)
- The brown fox is quick and the blue dog is lazy! (Score: 0.2560)
```
*#1 Menyimpan vektor dokumen ke dalam sebuah array*
*#2 Fungsi untuk melakukan pencocokan kesamaan pada pengembalian kueri, kecocokan, dan skor kesamaan*
*#3 Loop input utama*
*#4 Melakukan loop melalui hasil dan mengeluarkan teks dan skor kesamaan*

Jalankan latihan ini untuk melihat outputnya (F5 di VS Code). Masukkan teks apa pun yang Anda suka, dan lihat hasil dokumen yang dikembalikan. Bentuk pencarian ini berfungsi dengan baik untuk mencocokkan kata dan frasa dengan kata dan frasa yang serupa. Bentuk pencarian ini kehilangan konteks dan makna kata dari dokumen. Di bagian selanjutnya, kita akan melihat cara mengubah dokumen menjadi vektor yang lebih baik dalam mempertahankan makna semantiknya.

### 8.3.3 Mendemistifikasi penyematan dokumen

TF–IDF adalah bentuk sederhana yang mencoba menangkap makna semantik dalam dokumen. Namun, ini tidak dapat diandalkan karena hanya menghitung frekuensi kata dan tidak memahami hubungan antar kata. Metode yang lebih baik dan lebih modern menggunakan penyematan dokumen, suatu bentuk vektorisasi dokumen yang lebih baik dalam mempertahankan makna semantik dokumen.

Jaringan penyematan dibangun dengan melatih jaringan saraf pada kumpulan data besar untuk memetakan kata, kalimat, atau dokumen ke vektor berdimensi tinggi, menangkap hubungan semantik dan sintaksis berdasarkan konteks dan hubungan dalam data. Anda biasanya menggunakan model yang telah dilatih sebelumnya yang dilatih pada kumpulan data besar untuk menyematkan dokumen dan melakukan penyematan. Model tersedia dari banyak sumber, termasuk Hugging Face dan, tentu saja, OpenAI.

Dalam skenario kita berikutnya, kita akan menggunakan model penyematan OpenAI. Model-model ini biasanya sempurna untuk menangkap konteks semantik dari dokumen yang disematkan. Daftar 8.4 menunjukkan kode yang relevan yang menggunakan OpenAI untuk menyematkan dokumen ke dalam vektor yang kemudian direduksi menjadi tiga dimensi dan dirender menjadi plot.

**Daftar 8.4** `document_visualizing_embeddings.py` (bagian yang relevan)
```
load_dotenv()     #1
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key)     #1            

def get_embedding(text, model="text-embedding-ada-002"):    #2
    text = text.replace("
", " ")
    return client.embeddings.create(input=[text],
              model=model).data[0].embedding                #2

# Contoh dokumen (dihilangkan)

embeddings = [get_embedding(doc) for doc in documents]   #3
print(embeddings_array.shape)

embeddings_array = np.array(embeddings)   #4

pca = PCA(n_components=3)  #5
reduced_embeddings = pca.fit_transform(embeddings_array)
```
*#1 Gabungkan semua item pada string ', '.*
*#2 Menggunakan klien OpenAI untuk membuat penyematan*
*#3 Menghasilkan penyematan untuk setiap dokumen dengan ukuran 1536 dimensi*
*#4 Mengonversi penyematan ke array NumPy untuk PCA*
*#5 Menerapkan PCA untuk mengurangi dimensi menjadi 3 untuk plotting*

Ketika sebuah dokumen disematkan menggunakan model OpenAI, ia mengubah teks menjadi vektor dengan dimensi 1536. Kita tidak dapat memvisualisasikan jumlah dimensi ini, jadi kita menggunakan teknik reduksi dimensionalitas melalui analisis komponen utama (PCA) untuk mengubah vektor ukuran 1536 menjadi 3 dimensi.

Gambar 8.6 menunjukkan output yang dihasilkan dari menjalankan file di VS Code. Dengan mengurangi penyematan menjadi 3D, kita dapat memplot output untuk menunjukkan bagaimana dokumen yang mirip secara semantik sekarang dikelompokkan.

![figure](Images/8-6.png)

**Gambar 8.6** Penyematan dalam 3D, menunjukkan bagaimana dokumen semantik yang serupa dikelompokkan

Pilihan model atau layanan penyematan mana yang Anda gunakan terserah Anda. Model penyematan OpenAI dianggap yang terbaik untuk kesamaan semantik umum. Ini telah membuat model-model ini menjadi standar untuk sebagian besar aplikasi memori dan pengambilan. Dengan pemahaman kita tentang bagaimana teks dapat divektorisasi dengan penyematan dan disimpan dalam basis data vektor, kita dapat melanjutkan ke contoh yang lebih realistis di bagian selanjutnya.

### 8.3.4 Menanyakan penyematan dokumen dari Chroma

Kita dapat menggabungkan semua bagian dan melihat contoh lengkap menggunakan basis data vektor lokal bernama Chroma DB. Ada banyak pilihan basis data vektor, tetapi Chroma DB adalah penyimpanan vektor lokal yang sangat baik untuk pengembangan atau proyek skala kecil. Ada juga banyak pilihan yang lebih kuat yang dapat Anda pertimbangkan nanti.

Daftar 8.5 menunjukkan bagian kode baru dan relevan dari file `document_query_chromadb.py`. Perhatikan bahwa hasilnya dinilai berdasarkan jarak dan bukan berdasarkan kesamaan. Jarak kosinus ditentukan oleh persamaan ini:

Jarak Kosinus(A,B) = 1 – Kesamaan Kosinus(A,B)

Ini berarti bahwa jarak kosinus akan berkisar dari 0 untuk yang paling mirip hingga 2 untuk yang berlawanan secara semantik dalam makna.

**Daftar 8.5** `document_query_chromadb.py` (bagian kode yang relevan)
```
embeddings = [get_embedding(doc) for doc in documents]    #1
ids = [f"id{i}" for i in range(len(documents))]           #1

chroma_client = chromadb.Client()              #2
collection = chroma_client.create_collection(
                       name="documents")       #2
collection.add(    #3
    embeddings=embeddings,
    documents=documents,
    ids=ids
)

def query_chromadb(query, top_n=2):     #4
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_n
    )
    return [(id, score, text) for id, score, text in
            zip(results['ids'][0],
                results['distances'][0], 
                results['documents'][0])]

while True:    #5
    query = input("Enter a search query (or 'exit' to stop): ")
    if query.lower() == 'exit':
        break
    top_n = int(input("How many top matches do you want to see? "))
    search_results = query_chromadb(query, top_n)

    print("Top Matched Documents:")
    for id, score, text in search_results:
        print(f"""
ID:{id} TEXT: {text} SCORE: {round(score, 2)}
""")    #5

    print("
")
###Keluaran
Enter a search query (or 'exit' to stop): dogs are lazy
How many top matches do you want to see? 3
Top Matched Documents:
ID:id7 TEXT: The dog is lazy but the brown fox is quick! SCORE: 0.24
ID:id5 TEXT: The brown fox is quick and the blue dog is lazy! SCORE: 0.28
ID:id2 TEXT: The quick brown fox jumps over the lazy dog. SCORE: 0.29
```
*#1 Menghasilkan penyematan untuk setiap dokumen dan memberikan ID*
*#2 Membuat klien Chroma DB dan koleksi*
*#3 Menambahkan penyematan dokumen ke koleksi*
*#4 Menanyakan datastore dan mengembalikan n dokumen relevan teratas*
*#5 Loop input untuk input pengguna dan output dokumen/skor yang relevan*

Seperti yang ditunjukkan oleh skenario sebelumnya, Anda sekarang dapat menanyakan dokumen menggunakan makna semantik daripada hanya istilah atau frasa kunci. Skenario ini sekarang harus memberikan latar belakang untuk melihat bagaimana pola pengambilan bekerja pada tingkat rendah. Di bagian selanjutnya, kita akan melihat bagaimana pola pengambilan dapat digunakan menggunakan LangChain.

## 8.4 Membangun RAG dengan LangChain

LangChain dimulai sebagai proyek sumber terbuka yang berspesialisasi dalam mengabstraksi pola pengambilan di berbagai sumber data dan penyimpanan vektor. Sejak itu telah berubah menjadi lebih banyak, tetapi secara fundamental, ia masih menyediakan opsi yang sangat baik untuk mengimplementasikan pengambilan.

Gambar 8.7 menunjukkan diagram dari LangChain yang mengidentifikasi proses penyimpanan dokumen untuk pengambilan. Langkah-langkah yang sama ini dapat direplikasi secara keseluruhan atau sebagian untuk mengimplementasikan pengambilan memori. Perbedaan penting antara pengambilan dokumen dan memori adalah sumber dan bagaimana konten diubah.

![figure](Images/8-7.png)

**Gambar 8.7** Langkah-langkah memuat, mengubah, menyematkan, dan menyimpan dalam menyimpan dokumen untuk pengambilan nanti

Kita akan memeriksa cara mengimplementasikan setiap langkah ini menggunakan LangChain dan memahami nuansa dan detail yang menyertai implementasi ini. Di bagian selanjutnya, kita akan mulai dengan memisahkan dan memuat dokumen dengan LangChain.

### 8.4.1 Memisahkan dan memuat dokumen dengan LangChain

Mekanisme pengambilan menambah konteks dari prompt yang diberikan dengan informasi spesifik yang relevan dengan permintaan. Misalnya, Anda dapat meminta informasi terperinci tentang dokumen lokal. Dengan model bahasa sebelumnya, mengirimkan seluruh dokumen sebagai bagian dari prompt bukanlah pilihan karena keterbatasan token.

Saat ini, kita dapat mengirimkan seluruh dokumen untuk banyak LLM komersial, seperti GPT-4 Turbo, sebagai bagian dari permintaan prompt. Namun, hasilnya mungkin tidak lebih baik dan kemungkinan akan lebih mahal karena jumlah token yang meningkat. Oleh karena itu, pilihan yang lebih baik adalah membagi dokumen dan menggunakan bagian yang relevan untuk meminta konteks—persis seperti yang dilakukan RAG dan memori.

Memisahkan dokumen sangat penting dalam memecah konten menjadi bagian-bagian yang relevan secara semantik dan spesifik. Gambar 8.8 menunjukkan cara memecah dokumen HTML yang berisi sajak anak-anak Mother Goose. Seringkali, memisahkan dokumen menjadi potongan-potongan semantik kontekstual memerlukan pertimbangan yang cermat.

![figure](Images/8-8.png)

**Gambar 8.8** Bagaimana dokumen idealnya akan dibagi menjadi beberapa bagian untuk makna semantik dan kontekstual yang lebih baik

Idealnya, ketika kita membagi dokumen menjadi beberapa bagian, mereka dipecah berdasarkan relevansi dan makna semantik. Meskipun LLM atau agen dapat membantu kita dengan ini, kita akan melihat opsi perangkat saat ini dalam LangChain untuk memisahkan dokumen. Nanti di bab ini, kita akan melihat fungsi semantik yang dapat membantu kita dalam membagi konten secara semantik untuk penyematan.

Untuk latihan berikutnya, buka `langchain_load_splitting.py` di VS Code, seperti yang ditunjukkan pada daftar 8.6. Kode ini menunjukkan di mana kita tinggalkan dari daftar 8.5, di bagian sebelumnya. Alih-alih menggunakan dokumen sampel, kali ini kita memuat sajak anak-anak Mother Goose.

**Daftar 8.6** `langchain_load_splitting.py` (bagian dan output)
```
From langchain_community.document_loaders 
                       import UnstructuredHTMLLoader   #1
from langchain.text_splitter import RecursiveCharacterTextSplitter
#kode sebelumnya

loader = UnstructuredHTMLLoader(
                   "sample_documents/mother_goose.html")  #2
data = loader.load   #3

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=25,    #4
    length_function=len,
    add_start_index=True,
)
documents = text_splitter.split_documents(data)

documents = [doc.page_content 
                for doc in documents] [100:350]  #5

embeddings = [get_embedding(doc) for doc in documents]    #6
ids = [f"id{i}" for i in range(len(documents))]
###Keluaran
Enter a search query (or 'exit' to stop): **who kissed the girls and made **

**them cry?**

How many top matches do you want to see? 3
Top Matched Documents:
ID:id233 TEXT: And chid her daughter,
        And kissed my sister instead of me. SCORE: 0.4…
```
*#1 Impor LangChain baru*
*#2 Memuat dokumen sebagai HTML*
*#3 Memuat dokumen*
*#4 Memisahkan dokumen menjadi blok teks sepanjang 100 karakter dengan tumpang tindih 25 karakter*
*#5 Menyematkan hanya 250 potongan, yang lebih murah dan lebih cepat*
*#6 Mengembalikan penyematan untuk setiap dokumen*

Perhatikan dalam daftar 8.6 bahwa dokumen HTML dibagi menjadi potongan 100 karakter dengan tumpang tindih 25 karakter. Tumpang tindih memungkinkan bagian-bagian dokumen untuk tidak memotong pemikiran tertentu. Kami memilih pemisah untuk latihan ini karena mudah digunakan, diatur, dan dipahami.

Silakan jalankan file `langchain_load_splitting.py` di VS Code (F5). Masukkan kueri, dan lihat hasil apa yang Anda dapatkan. Output dalam daftar 8.6 menunjukkan hasil yang baik mengingat contoh spesifik. Ingatlah bahwa kami hanya menyematkan 250 potongan dokumen untuk mengurangi biaya dan menjaga latihan tetap singkat. Tentu saja, Anda selalu dapat mencoba menyematkan seluruh dokumen atau menggunakan contoh dokumen input yang lebih kecil.

Mungkin elemen paling penting untuk membangun pengambilan yang tepat adalah proses pemisahan dokumen. Anda dapat menggunakan banyak metode untuk membagi dokumen, termasuk beberapa metode bersamaan. Lebih dari satu metode melewati dan membagi dokumen untuk berbagai tampilan penyematan dari dokumen yang sama. Di bagian selanjutnya, kita akan memeriksa teknik yang lebih umum untuk memisahkan dokumen, menggunakan token dan tokenisasi.

### 8.4.2 Memisahkan dokumen berdasarkan token dengan LangChain

*Tokenisasi* adalah proses memecah teks menjadi token kata. Di mana token kata mewakili elemen ringkas dalam teks, token bisa berupa kata seperti *tahan* atau bahkan simbol seperti kurung kurawal kiri ({), tergantung pada apa yang relevan.

Memisahkan dokumen menggunakan tokenisasi memberikan dasar yang lebih baik tentang bagaimana teks akan ditafsirkan oleh model bahasa dan untuk kesamaan semantik. Tokenisasi juga memungkinkan penghapusan karakter yang tidak relevan, seperti spasi, membuat pencocokan kesamaan dokumen lebih relevan dan umumnya memberikan hasil yang lebih baik.

Untuk latihan kode berikutnya, buka file `langchain_token_splitting.py` di VS Code, seperti yang ditunjukkan pada daftar 8.7. Sekarang kita membagi dokumen menggunakan tokenisasi, yang memecah dokumen menjadi beberapa bagian dengan ukuran yang tidak sama. Ukuran yang tidak sama dihasilkan dari bagian spasi yang besar dari dokumen asli.

**Daftar 8.7** `langchain_token_splitting.py` (kode baru yang relevan)
```
loader = UnstructuredHTMLLoader("sample_documents/mother_goose.html")
data = loader.load()
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=50, chunk_overlap=10     #1
)

documents = text_splitter.split_documents(data)
documents = [doc for doc in documents][8:94]     #2

db = Chroma.from_documents(documents, OpenAIEmbeddings())

def query_documents(query, top_n=2):
    docs = db.similarity_search(query, top_n)     #3
    return docs
###Keluaran
Created a chunk of size 68, 
which is longer than the specified 50
Created a chunk of size 67, 
which is longer than the specified 50    #4
Enter a search query (or 'exit' to stop): 
                     who kissed the girls and made them cry?
How many top matches do you want to see? 3
Top Matched Documents:
Document 1: GEORGY PORGY

        Georgy Porgy, pudding and pie,
        Kissed the girls and made them cry.
```
*#1 Pembaruan menjadi 50 token dan tumpang tindih 10 token*
*#2 Memilih hanya dokumen yang berisi sajak*
*#3 Menggunakan pencarian kesamaan basis data*
*#4 Memecah menjadi potongan-potongan ukuran tidak teratur karena spasi*

Jalankan kode `langchain_token_splitting.py` di VS Code (F5). Anda dapat menggunakan kueri yang kami gunakan terakhir kali atau milik Anda sendiri. Perhatikan bagaimana hasilnya jauh lebih baik daripada latihan sebelumnya. Namun, hasilnya masih diragukan karena kueri menggunakan beberapa kata serupa dalam urutan yang sama.

Tes yang lebih baik adalah mencoba frasa yang mirip secara semantik tetapi menggunakan kata-kata yang berbeda dan memeriksa hasilnya. Dengan kode yang masih berjalan, masukkan frasa baru untuk ditanyakan: `Mengapa` `para` `gadis` `menangis?` Daftar 8.8 menunjukkan hasil dari menjalankan kueri itu. Jika Anda menjalankan contoh ini sendiri dan menggulir ke bawah output, Anda akan melihat Georgy Porgy muncul di dokumen kedua atau ketiga yang dikembalikan.

**Daftar 8.8** Kueri: Siapa yang membuat para gadis menangis?
```
Enter a search query (or 'exit' to stop): Who made the girls cry?
How many top matches do you want to see? 3
Top Matched Documents:
Document 1: WILLY, WILLY

        Willy, Willy Wilkin…
```

Latihan ini menunjukkan bagaimana berbagai metode pengambilan dapat digunakan untuk mengembalikan dokumen secara semantik. Dengan dasar ini, kita dapat melihat bagaimana RAG dapat diterapkan pada sistem pengetahuan dan memori. Bagian berikut akan membahas RAG karena berlaku untuk pengetahuan agen dan sistem agentik.

## 8.5 Menerapkan RAG untuk membangun pengetahuan agen

Pengetahuan dalam agen mencakup penggunaan RAG untuk mencari secara semantik di seluruh dokumen tidak terstruktur. Dokumen-dokumen ini bisa apa saja mulai dari PDF hingga dokumen Microsoft Word dan semua teks, termasuk kode. Pengetahuan agentik juga mencakup penggunaan dokumen tidak terstruktur untuk T&J, pencarian referensi, augmentasi informasi, dan pola masa depan lainnya.

Nexus, platform agen yang dikembangkan bersama dengan buku ini dan diperkenalkan di bab sebelumnya, menggunakan sistem pengetahuan dan memori lengkap untuk agen. Di bagian ini, kita akan mengungkap cara kerja sistem pengetahuan.

Untuk menginstal Nexus hanya untuk bab ini, lihat daftar 8.9. Buka terminal di dalam folder `chapter_08`, dan jalankan perintah dalam daftar untuk mengunduh, menginstal, dan menjalankan Nexus dalam mode normal atau pengembangan. Jika Anda ingin merujuk ke kode, Anda harus menginstal proyek dalam pengembangan dan mengonfigurasi debugger untuk menjalankan aplikasi Streamlit dari VS Code. Lihat bab 7 jika Anda memerlukan penyegaran pada salah satu langkah ini.

**Daftar 8.9** Menginstal Nexus
```
# untuk menginstal dan menjalankan
pip install git+https://github.com/cxbxmxcx/Nexus.git

nexus run
# instal dalam mode pengembangan
git clone https://github.com/cxbxmxcx/Nexus.git

# Instal repositori yang dikloning dalam mode yang dapat diedit
pip install -e Nexus
```

Terlepas dari metode mana yang Anda putuskan untuk menjalankan aplikasi setelah Anda masuk, navigasikan ke halaman Manajer Penyimpanan Pengetahuan, seperti yang ditunjukkan pada gambar 8.9. Buat Penyimpanan Pengetahuan baru, lalu unggah skrip film `sample_documents/back_to_the_future.txt`.

![figure](Images/8-9.png)

**Gambar 8.9** Menambahkan penyimpanan pengetahuan baru dan mengisinya dengan dokumen

Skripnya adalah dokumen besar, dan mungkin perlu beberapa saat untuk memuat, memotong, dan menyematkan bagian-bagiannya ke dalam basis data vektor Chroma DB. Tunggu hingga pengindeksan selesai, lalu Anda dapat memeriksa penyematan dan menjalankan kueri, seperti yang ditunjukkan pada gambar 8.10.

![figure](Images/8-10.png)

**Gambar 8.10** Tampilan penyematan dan kueri dokumen

Sekarang, kita dapat menghubungkan penyimpanan pengetahuan ke agen yang didukung dan mengajukan pertanyaan. Gunakan pemilih kiri atas untuk memilih halaman obrolan di dalam antarmuka Nexus. Kemudian, pilih agen dan penyimpanan pengetahuan `time_travel`, seperti yang ditunjukkan pada gambar 8.11. Anda juga perlu memilih mesin agen yang mendukung pengetahuan. Masing-masing dari beberapa mesin agen memerlukan konfigurasi yang tepat agar dapat diakses.

![figure](Images/8-11.png)

**Gambar 8.11** Mengaktifkan penyimpanan pengetahuan untuk penggunaan agen

Saat ini, pada bab ini, Nexus hanya mendukung akses ke satu penyimpanan pengetahuan pada satu waktu. Di versi mendatang, agen mungkin dapat memilih beberapa penyimpanan pengetahuan sekaligus. Ini mungkin termasuk opsi yang lebih canggih, dari pengetahuan semantik hingga menggunakan bentuk RAG lainnya.

Anda juga dapat mengonfigurasi pengaturan RAG di dalam tab Konfigurasi pada halaman Manajer Penyimpanan Pengetahuan, seperti yang ditunjukkan pada gambar 8.12. Sampai sekarang, Anda dapat memilih dari jenis pemisah (bidang Opsi Pemotongan) untuk memotong dokumen, bersama dengan bidang Ukuran Potongan dan bidang Tumpang Tindih.

![figure](Images/8-12.png)

**Gambar 8.12** Mengelola opsi pemisahan dan pemotongan penyimpanan pengetahuan

Opsi pemuatan, pemisahan, pemotongan, dan penyematan yang disediakan adalah satu-satunya opsi dasar yang didukung oleh LangChain untuk saat ini. Di versi Nexus mendatang, lebih banyak opsi dan pola akan ditawarkan. Kode untuk mendukung opsi lain dapat ditambahkan langsung ke Nexus.

Kami tidak akan membahas kode yang melakukan RAG karena sangat mirip dengan apa yang telah kami bahas. Jangan ragu untuk meninjau kode Nexus, khususnya kelas `KnowledgeManager` dalam file `knowledge_manager.py`.

Meskipun pola pengambilan untuk pengetahuan dan memori sangat mirip untuk augmentasi, kedua pola tersebut berbeda dalam hal mengisi penyimpanan. Di bagian selanjutnya, kita akan menjelajahi apa yang membuat memori dalam agen unik.

## 8.6 Mengimplementasikan memori dalam sistem agentik

Memori dalam agen dan aplikasi AI sering digambarkan dalam istilah yang sama dengan fungsi memori kognitif. Memori *kognitif* menggambarkan jenis memori yang kita gunakan untuk mengingat apa yang kita lakukan 30 detik yang lalu atau seberapa tinggi kita 30 tahun yang lalu. Memori komputer juga merupakan elemen penting dari memori agen, tetapi yang tidak akan kita pertimbangkan di bagian ini.

Gambar 8.13 menunjukkan bagaimana memori dipecah menjadi memori sensorik, jangka pendek, dan jangka panjang. Memori ini dapat diterapkan pada agen AI, dan daftar ini menjelaskan bagaimana setiap bentuk memori memetakan ke fungsi agen:

- *Memori sensorik dalam AI* —Fungsi seperti RAG tetapi dengan bentuk data gambar/audio/haptik. Secara singkat menahan data input (misalnya, teks dan gambar) untuk pemrosesan segera tetapi tidak untuk penyimpanan jangka panjang.
- *Memori jangka pendek/kerja dalam AI* —Bertindak sebagai buffer memori aktif dari riwayat percakapan. Kami menahan sejumlah input dan konteks terbaru yang terbatas untuk analisis dan pembuatan respons segera. Di dalam Nexus, memori percakapan jangka pendek dan jangka panjang juga disimpan dalam konteks utas.
- *Memori jangka panjang dalam AI* —Penyimpanan memori jangka panjang yang relevan dengan kehidupan agen atau pengguna. Memori semantik menyediakan kapasitas yang kuat untuk menyimpan dan mengambil fakta dan konsep global atau lokal yang relevan.

![figure](Images/8-13.png)

**Gambar 8.13** Bagaimana memori dipecah menjadi berbagai bentuk

Meskipun memori menggunakan mekanisme pengambilan dan augmentasi yang sama persis dengan pengetahuan, biasanya berbeda secara signifikan saat memperbarui atau menambahkan memori. Gambar 8.14 menyoroti proses menangkap dan menggunakan memori untuk menambah prompt. Karena memori seringkali berbeda dari ukuran dokumen lengkap, kita dapat menghindari penggunaan mekanisme pemisahan atau pemotongan apa pun.

![figure](Images/8-14.png)

**Gambar 8.14** Alur kerja pengambilan dan augmentasi memori dasar

Nexus menyediakan mekanisme seperti penyimpanan pengetahuan, yang memungkinkan pengguna membuat penyimpanan memori yang dapat dikonfigurasi untuk berbagai penggunaan dan aplikasi. Ini juga mendukung beberapa bentuk memori yang lebih canggih yang disorot pada gambar 8.13. Bagian berikut akan memeriksa cara kerja penyimpanan memori dasar di Nexus.

### 8.6.1 Mengkonsumsi penyimpanan memori di Nexus

Penyimpanan memori beroperasi dan dibangun seperti penyimpanan pengetahuan di Nexus. Keduanya sangat bergantung pada pola pengambilan. Yang berbeda adalah langkah-langkah ekstra yang diambil sistem memori untuk membangun memori baru.

Silakan mulai Nexus, dan lihat daftar 8.9 jika Anda perlu menginstalnya. Setelah masuk, pilih halaman Memori, dan buat penyimpanan memori baru, seperti yang ditunjukkan pada gambar 8.15. Pilih mesin agen, lalu tambahkan beberapa fakta dan preferensi pribadi tentang diri Anda.

![figure](Images/8-15.png)

**Gambar 8.15** Menambahkan memori ke penyimpanan memori yang baru dibuat

Alasan kita membutuhkan agen (LLM) ditunjukkan pada gambar 8.14 sebelumnya. Ketika informasi dimasukkan ke dalam penyimpanan memori, informasi tersebut umumnya diproses melalui LLM menggunakan fungsi memori, yang tujuannya adalah untuk memproses pernyataan/percakapan menjadi informasi yang relevan secara semantik terkait dengan jenis memori.

Daftar 8.10 menunjukkan fungsi memori percakapan yang digunakan untuk mengekstrak informasi dari percakapan menjadi memori. Ya, ini hanyalah bagian header dari prompt yang dikirim ke LLM, yang menginstruksikannya cara mengekstrak informasi dari percakapan.

**Daftar 8.10** Fungsi memori percakapan
```
Summarize the conversation and create a set of statements that summarize 
the conversation. Return a JSON object with the following keys: 'summary'. 
Each key should have a list of statements that are relevant to that 
category. Return only the JSON object and nothing else.
```

Setelah Anda menghasilkan beberapa memori yang relevan tentang diri Anda, kembali ke area Obrolan di Nexus, aktifkan penyimpanan memori `my_memory`, dan lihat seberapa baik agen mengenal Anda. Gambar 8.16 menunjukkan contoh percakapan menggunakan mesin agen yang berbeda.

![figure](Images/8-16.png)

**Gambar 8.16** Bercakap-cakap dengan agen yang berbeda di penyimpanan memori yang sama

Ini adalah contoh pola memori dasar yang mengekstrak fakta/preferensi dari percakapan dan menyimpannya dalam basis data vektor sebagai memori. Banyak implementasi memori lain mengikuti yang ditampilkan sebelumnya pada gambar 8.13. Kita akan mengimplementasikannya di bagian selanjutnya.

### 8.6.2 Memori semantik dan aplikasi pada memori semantik, episodik, dan prosedural

Psikolog mengkategorikan memori ke dalam berbagai bentuk, tergantung pada informasi apa yang diingat. Memori semantik, episodik, dan prosedural semuanya mewakili berbagai jenis informasi. Memori *episodik* adalah tentang peristiwa, memori *prosedural* adalah tentang proses atau langkah-langkah, dan *semantik* mewakili makna dan dapat mencakup perasaan atau emosi. Bentuk memori lain (geospasial adalah yang lain), tidak dijelaskan di sini tetapi bisa jadi.

Karena ingatan ini bergantung pada tingkat kategorisasi tambahan, mereka juga bergantung pada tingkat kategorisasi semantik lainnya. Beberapa platform, seperti Semantic Kernel (SK), menyebut ini sebagai *memori semantik*. Ini bisa membingungkan karena kategorisasi semantik juga diterapkan untuk mengekstrak ingatan episodik dan prosedural.

Gambar 8.17 menunjukkan proses kategorisasi memori semantik, juga terkadang disebut memori semantik. Perbedaan antara memori semantik dan memori biasa adalah langkah tambahan memproses masukan secara semantik dan mengekstrak pertanyaan relevan yang dapat digunakan untuk menanyakan basis data relevan memori.

![figure](Images/8-17.png)

**Gambar 8.17** Cara kerja augmentasi memori semantik

Manfaat menggunakan augmentasi semantik adalah peningkatan kemampuan untuk mengekstrak lebih banyak memori yang relevan. Kita dapat melihat ini beroperasi dengan melompat kembali ke Nexus dan membuat penyimpanan memori semantik baru.

Gambar 8.18 menunjukkan cara mengonfigurasi penyimpanan memori baru menggunakan memori semantik. Sampai sekarang, Anda belum dapat mengonfigurasi prompt fungsi spesifik untuk memori, augmentasi, dan peringkasan. Namun, akan berguna untuk membaca setiap prompt fungsi untuk mendapatkan gambaran tentang cara kerjanya.

![figure](Images/8-18.png)

**Gambar 8.18** Konfigurasi untuk mengubah jenis penyimpanan memori menjadi semantik

Sekarang, jika Anda kembali dan menambahkan fakta dan preferensi, mereka akan dikonversi ke semantik dari jenis memori yang relevan. Gambar 8.19 menunjukkan contoh memori yang diisi untuk kumpulan pernyataan yang sama ke dalam dua bentuk memori yang berbeda. Umumnya, pernyataan yang dimasukkan ke dalam memori akan lebih spesifik pada bentuk memori.

![figure](Images/8-19.png)

**Gambar 8.19** Membandingkan memori untuk informasi yang sama yang diberikan dua jenis memori yang berbeda

Memori dan pengetahuan dapat secara signifikan membantu agen dengan berbagai jenis aplikasi. Memang, satu penyimpanan memori/pengetahuan dapat memberi makan satu atau beberapa agen, memungkinkan interpretasi yang lebih khusus dari kedua jenis penyimpanan. Kita akan menyelesaikan bab ini dengan membahas kompresi memori/pengetahuan selanjutnya.

## 8.7 Memahami kompresi memori dan pengetahuan

Sama seperti ingatan kita sendiri, penyimpanan ingatan dapat menjadi berantakan dengan informasi yang berlebihan dan banyak detail yang tidak terkait dari waktu ke waktu. Secara internal, pikiran kita menangani kekacauan ingatan dengan mengompresi atau meringkas ingatan. Pikiran kita mengingat detail yang lebih signifikan daripada yang kurang penting, dan ingatan yang lebih sering diakses.

Kita dapat menerapkan prinsip-prinsip kompresi memori yang serupa pada memori agen dan sistem pengambilan lainnya untuk mengekstrak detail yang signifikan. Prinsip kompresi mirip dengan augmentasi semantik tetapi menambahkan lapisan lain ke kelompok pra-klaster dari memori terkait yang secara kolektif dapat diringkas.

Gambar 8.20 menunjukkan proses kompresi memori/pengetahuan. Memori atau pengetahuan pertama-tama dikelompokkan menggunakan algoritma seperti k-means. Kemudian, kelompok-kelompok memori dilewatkan melalui fungsi kompresi, yang meringkas dan mengumpulkan item-item tersebut ke dalam representasi yang lebih ringkas.

![figure](Images/8-20.png)

**Gambar 8.20** Proses kompresi memori dan pengetahuan

Nexus menyediakan kompresi penyimpanan pengetahuan dan memori menggunakan pengelompokan optimal k-means. Gambar 8.21 menunjukkan antarmuka kompresi untuk memori. Di dalam antarmuka kompresi, Anda akan melihat item ditampilkan dalam 3D dan dikelompokkan. Ukuran (jumlah item) dari cluster ditunjukkan di tabel kiri.

![figure](Images/8-21.png)

**Gambar 8.21** Antarmuka untuk mengompresi memori

Mengompresi memori dan bahkan pengetahuan umumnya direkomendasikan jika jumlah item dalam sebuah cluster besar atau tidak seimbang. Setiap kasus penggunaan untuk kompresi dapat bervariasi tergantung pada penggunaan dan aplikasi memori. Namun, secara umum, jika pemeriksaan item di toko berisi informasi yang berulang atau duplikat, ini adalah waktu yang tepat untuk kompresi. Berikut ini adalah ringkasan kasus penggunaan untuk aplikasi yang akan mendapat manfaat dari kompresi.

#### Kasus untuk kompresi pengetahuan

Pengambilan dan augmentasi pengetahuan juga telah terbukti mendapat manfaat signifikan dari kompresi. Hasil akan bervariasi berdasarkan kasus penggunaan, tetapi secara umum, semakin bertele-tele sumber pengetahuan, semakin besar manfaatnya dari kompresi. Dokumen yang menampilkan prosa sastra, seperti cerita dan novel, akan lebih diuntungkan daripada, katakanlah, basis kode. Namun, jika kode tersebut juga sangat berulang, kompresi juga dapat terbukti bermanfaat.

#### Kasus seberapa sering Anda menerapkan kompresi

Memori akan sering mendapat manfaat dari aplikasi kompresi berkala, sedangkan penyimpanan pengetahuan biasanya hanya membantu pada pemuatan pertama. Seberapa sering Anda menerapkan kompresi akan sangat bergantung pada penggunaan, frekuensi, and kuantitas memori.

#### Kasus untuk menerapkan kompresi lebih dari sekali

Beberapa lintasan kompresi pada saat yang sama telah terbukti meningkatkan kinerja pengambilan. Pola lain juga menyarankan penggunaan memori atau pengetahuan pada berbagai tingkat kompresi. Misalnya, penyimpanan pengetahuan dikompresi dua kali, menghasilkan tiga tingkat pengetahuan yang berbeda.

#### Kasus untuk memadukan kompresi pengetahuan dan memori

Jika suatu sistem dikhususkan untuk sumber pengetahuan tertentu dan sistem itu juga menggunakan memori, mungkin ada optimasi lebih lanjut untuk mengkonsolidasikan penyimpanan. Pendekatan lain adalah mengisi memori dengan pengetahuan awal dari sebuah dokumen secara langsung.

#### Kasus untuk beberapa penyimpanan memori atau pengetahuan

Dalam sistem yang lebih canggih, kita akan melihat agen yang menggunakan beberapa penyimpanan memori dan pengetahuan yang relevan dengan alur kerja mereka. Misalnya, seorang agen dapat menggunakan penyimpanan memori individual sebagai bagian dari percakapannya dengan pengguna individu, mungkin termasuk kemampuan untuk berbagi kelompok memori yang berbeda dengan kelompok individu yang berbeda. Pengambilan memori dan pengetahuan adalah landasan sistem agentik, dan sekarang kita dapat merangkum apa yang telah kita bahas dan meninjau beberapa latihan pembelajaran di bagian selanjutnya.

## 8.8 Latihan

Gunakan latihan berikut untuk meningkatkan pengetahuan Anda tentang materi:

- *Latihan 1* —Muat dan Pisahkan Dokumen yang Berbeda (Menengah)

*Tujuan* —Memahami pengaruh pemisahan dokumen terhadap efisiensi pengambilan dengan menggunakan LangChain.

*Tugas*:

  - Pilih dokumen yang berbeda (misalnya, artikel berita, makalah ilmiah, atau cerita pendek).
  - Gunakan LangChain untuk memuat dan membagi dokumen menjadi beberapa bagian.
  - Analisis bagaimana dokumen dibagi menjadi beberapa bagian dan bagaimana hal itu memengaruhi proses pengambilan.

- *Latihan 2* —Eksperimen dengan Pencarian Semantik (Menengah)

*Tujuan* —Bandingkan efektivitas berbagai teknik vektorisasi dengan melakukan pencarian semantik.

*Tugas*:

  - Pilih satu set dokumen untuk pencarian semantik.
  - Gunakan metode vektorisasi seperti Word2Vec atau penyematan BERT alih-alih TF–IDF.
  - Lakukan pencarian semantik, dan bandingkan hasilnya dengan yang diperoleh menggunakan TF–IDF untuk memahami perbedaan dan efektivitasnya.

- *Latihan 3* —Terapkan Alur Kerja RAG Kustom (Lanjutan)

*Tujuan* —Menerapkan pengetahuan teoretis RAG dalam konteks praktis menggunakan LangChain.

*Tugas*:

  - Pilih aplikasi tertentu (misalnya, pertanyaan layanan pelanggan atau pertanyaan penelitian akademis).
  - Rancang dan terapkan alur kerja RAG kustom menggunakan LangChain.
  - Sesuaikan alur kerja agar sesuai dengan aplikasi yang dipilih, dan uji efektivitasnya.

- *Latihan 4* —Bangun Penyimpanan Pengetahuan dan Eksperimen dengan Pola Pemisahan (Menengah)

*Tujuan* —Memahami bagaimana pola pemisahan dan kompresi yang berbeda memengaruhi pengambilan pengetahuan.

*Tugas*:

  - Bangun penyimpanan pengetahuan, dan isilah dengan beberapa dokumen.
  - Bereksperimenlah dengan berbagai bentuk pola pemisahan/pemotongan, dan analisis pengaruhnya terhadap pengambilan.
  - Kompres penyimpanan pengetahuan, dan amati pengaruhnya terhadap kinerja kueri.

- *Latihan 5* —Bangun dan Uji Berbagai Penyimpanan Memori (Lanjutan)

*Tujuan* —Memahami keunikan dan kasus penggunaan berbagai jenis penyimpanan memori.

*Tugas*:

  - Bangun berbagai bentuk penyimpanan memori (percakapan, semantik, episodik, dan prosedural).
  - Berinteraksi dengan agen menggunakan setiap jenis penyimpanan memori, dan amati perbedaannya.
  - Kompres penyimpanan memori, dan analisis pengaruhnya terhadap pengambilan memori.

## Ringkasan

- Memori dalam aplikasi AI membedakan antara memori tidak terstruktur dan terstruktur, menyoroti penggunaannya dalam mengontekstualisasikan prompt untuk interaksi yang lebih relevan.
- Retrieval augmented generation (RAG) adalah mekanisme untuk menyempurnakan prompt dengan konteks dari dokumen eksternal, menggunakan penyematan vektor dan pencarian kesamaan untuk mengambil konten yang relevan.
- Pencarian semantik dengan pengindeksan dokumen mengubah dokumen menjadi vektor semantik menggunakan TF–IDF dan kesamaan kosinus, meningkatkan kemampuan untuk melakukan pencarian semantik di seluruh dokumen yang diindeks.
- Basis data vektor dan pencarian kesamaan menyimpan vektor dokumen dalam basis data vektor, memfasilitasi pencarian kesamaan yang efisien dan meningkatkan akurasi pengambilan.
- Penyematan dokumen menangkap makna semantik, menggunakan model seperti model OpenAI untuk menghasilkan penyematan yang mempertahankan konteks dokumen dan memfasilitasi pencarian kesamaan semantik.
- LangChain menyediakan beberapa alat untuk melakukan RAG, dan ini mengabstraksi proses pengambilan, memungkinkan implementasi RAG dan sistem memori yang mudah di berbagai sumber data dan penyimpanan vektor.
- Memori jangka pendek dan jangka panjang di LangChain mengimplementasikan memori percakapan di dalam LangChain, membedakan antara pola buffering jangka pendek dan solusi penyimpanan jangka panjang.
- Menyimpan vektor dokumen dalam basis data untuk pencarian kesamaan yang efisien sangat penting untuk mengimplementasikan sistem pengambilan yang dapat diskalakan dalam aplikasi AI.
- Pengetahuan agen secara langsung berkaitan dengan pola RAG umum dalam melakukan tanya jawab pada dokumen atau informasi tekstual lainnya.
- Memori agen adalah pola yang terkait dengan RAG yang menangkap interaksi agentik dengan pengguna, dirinya sendiri, dan sistem lain.
- Nexus adalah platform yang mengimplementasikan sistem pengetahuan dan memori agentik, termasuk menyiapkan penyimpanan pengetahuan untuk pengambilan dokumen dan penyimpanan memori untuk berbagai bentuk memori.
- Augmentasi memori semantik (memori semantik) membedakan antara berbagai jenis memori (semantik, episodik, prosedural). Ini mengimplementasikannya melalui augmentasi semantik, meningkatkan kemampuan agen untuk mengingat dan menggunakan informasi yang relevan secara spesifik dengan sifat memori.
- Kompresi memori dan pengetahuan adalah teknik untuk memadatkan informasi yang disimpan dalam sistem memori dan pengetahuan, meningkatkan efisiensi dan relevansi pengambilan melalui pengelompokan dan peringkasan.
