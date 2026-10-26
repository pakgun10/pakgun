---
title: "Satu Lingkaran, Dua Sudut: Menggambar Sudut Pusat dan Sudut Keliling dengan TikZ"
date: 2026-10-27T10:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya sering menganggap sudut pusat dan sudut keliling sebagai dua rumus terpisah. Dengan menggambar keduanya dalam satu lingkaran TikZ yang jujur pada busurnya, hubungan 'dua kali lebih besar' itu akhirnya terlihat mata, bukan sekadar dihafal."
featuredImage: "featured-image.png"

tags: ["TikZ", "Lingkaran", "Sudut Pusat", "Sudut Keliling", "Geometri", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Ada satu soal yang hampir setiap tahun muncul di kelas VIII saya: sebuah lingkaran dengan titik $A$, $B$, $C$ pada kelilingnya dan titik $O$ di pusat, diketahui sudut keliling $ACB$ besarnya $40^\circ$, berapakah sudut pusat $AOB$? Jawaban yang ditunggu tentu $80^\circ$. Tetapi tahun lalu, ketika saya memeriksa lembar jawaban, saya menemukan sesuatu yang mengganggu: banyak siswa yang menulis $80^\circ$ dengan benar, tetapi ketika saya minta mereka menunjuk sudut pusat dan sudut keliling pada gambar di soal, jari mereka ragu. Mereka tahu rumusnya. Mereka tidak tahu mengapa rumus itu jalan.

<!--more-->

## Sudut yang "menghadap" busur yang sama

Cara saya menjelaskannya di papan tulis sekarang berhenti pada satu kalimat: sudut pusat dan sudut keliling itu seperti dua orang yang menonton panggung yang sama dari tempat duduk berbeda. Panggungnya adalah busur $AB$. Sudut pusat duduk di tengah lapangan, tepat di pusat lingkaran. Sudut keliling duduk di pinggir, tepat pada kelilingnya. Keduanya menghadap busur yang sama, dan selisih tempat duduk itulah yang membuat sudutnya berbeda: yang di pusat selalu dua kali yang di keliling.

Kalimat itu membuat suasana kelas lebih hidup daripada membacakan teorema. Tetapi saya sadar ada batasnya: begitu siswa pulang dan buka LKS, gambar yang mereka temui sering tidak mendukung kalimat itu. Busurnya terlalu kecil, sudutnya digambar "kira-kira", dan kadang sudut kelilingnya bahkan tidak benar-benar berada di keliling lingkaran. Gambar yang tidak jujur seperti itu justru meruntuhkan intuisi yang sudah dibangun. Jika sudut pusat di gambar tidak benar-benar terlihat dua kali sudut keliling, siswa tidak punya alasan untuk percaya pada teorema; mereka hanya menghafalnya karena disuruh.

## Menghitung koordinat dulu, menggambar kemudian

Maka saya menggambar ulang dengan TikZ, dan seperti biasa, aturan saya sendiri berlaku: ukuran di gambar harus benar-benar sesuai angka di soal. Saya pilih lingkaran berpusat di $(0,0)$ berjari-jari $3$. Titik $A$ saya letakkan di sudut $200^\circ$ dan titik $B$ di sudut $340^\circ$, sehingga busur kecil $AB$ menghadap sudut pusat $140^\circ$. Otomatis, sudut kelilingnya harus $70^\circ$. Titik $C$ saya taruh di sudut $80^\circ$, jauh di sisi lain lingkaran, supaya posisinya jelas "di pinggir" sementara $O$ jelas "di tengah".

Angka $140^\circ$ memang bukan angka yang biasa muncul di soal, tetapi justru itu kelebihannya: gambar tidak bisa lagi ditebak dengan "sudut pusat pasti $90^\circ$ kan, Pak?" Siswa dipaksa membaca busurnya, bukan menebak dari kenangan soal-soal sebelumnya.

Menariknya, proses menentukan titik $C$ ini sendiri menjadi bahan diskusi. Ketika saya memutar titik $C$ mengelilingi lingkaran di berkas TikZ, siswa melihat busur hijau tidak berubah besar sama sekali selama $C$ tetap berada di busur besar $AB$. Posisi sudut keliling boleh pindah ke mana saja di sepanjang busur itu; besar sudutnya tetap $70^\circ$. Properti ini kelihatan sepele, tetapi inilah yang membuat teorema kuat: ia tidak bergantung pada letak $C$, hanya pada busur yang dihadapinya. Dalam gambar statis, kebebasan memindahkan $C$ itu tidak pernah terlihat; siswa menganggap posisi $C$ di soal adalah satu-satunya posisi yang mungkin.

```latex
\begin{tikzpicture}[scale=1.0, line width=1.4pt]
  % Lingkaran dan titik-titiknya
  \draw (0,0) circle (3);
  \coordinate (O) at (0,0);
  \coordinate (A) at (200:3);
  \coordinate (B) at (340:3);
  \coordinate (C) at (80:3);
  \fill (O) circle (2pt) node[below=4pt] {$O$};
  \fill (A) circle (2pt) node[anchor=95, inner sep=6pt] {$A$};
  \fill (B) circle (2pt) node[anchor=35, inner sep=6pt] {$B$};
  \fill (C) circle (2pt) node[above=3pt] {$C$};
  % Jari-jari ke A dan B: sudut pusat 140 derajat
  \draw[gold] (O) -- (A) -- (B) -- cycle;
  % Tali ke A dan B dari C: sudut keliling 70 derajat
  \draw[teal] (C) -- (A) -- (B) -- cycle;
  % Busur sudut pusat
  \draw[gold, line width=2pt] (200:0.9) arc[start angle=200, end angle=340, radius=0.9];
  \node[gold] at (270:1.45) {$140^\circ$};
  % Busur sudut keliling di C
  \draw[teal, line width=2pt] ($(C)+(230:0.85)$) arc[start angle=230, end angle=300, radius=0.85];
  \node[teal] at ($(C)+(265:1.65)$) {$70^\circ$};
\end{tikzpicture}
```

Dua warna di gambar itu sengaja: emas untuk segitiga sudut pusat, hijau untuk segitiga sudut keliling. Ketika siswa melihat dua busur, satu di $O$ dan satu di $C$, keduanya menganga menghadap busur $AB$ yang sama, hubungan "dua kali" itu langsung terbaca dari proporsi gambarnya. Busur emas memang terlihat jauh lebih lebar daripada busur hijau, dan ukurannya memang tepat $140^\circ$ melawan $70^\circ$.

## Kesalahan yang muncul di lembar jawaban

Saya juga belajar membaca kesalahan dari gambar ini. Dua kesalahan yang paling sering saya temui pertama-tama bukan kesalahan hitung, melainkan kesalahan membaca gambar. Pertama, siswa membagi dua sudut yang sebenarnya bukan sudut pusat: mereka melihat sudut yang "besar" di gambar lalu langsung membaginya, tanpa memeriksa apakah kakinya dari pusat. Kedua, siswa memakai hubungan dua-kali pada sudut keliling dan sudut keliling lain yang tidak menghadap busur yang sama. Keduanya adalah kesalahan yang tidak akan muncul kalau kebiasaan pertama siswa adalah menunjuk busurnya dulu.

Karena itu, di lembar kerja saya sekarang ada satu pertanyaan wajib sebelum angka: "sudut ini menghadap busur yang mana?" Siswa menuliskan jawabannya, misalnya "busur $AB$", baru menghitung. Tampak menambah langkah, tetapi justru mempercepat: kesalahan yang dulu baru ketahuan setelah koreksi, sekarang berhenti di langkah pertama. Gambar berwarna yang sama membantu di sini, karena busur yang dihadapi dua sudut itu memang terlihat: kedua sudut, emas dan hijau, sama-sama membuka mulutnya ke arah busur $AB$.

## Ketika sudut kelilingnya yang ditanya

Gambar yang sama juga saya pakai untuk soal terbalik: diketahui sudut pusat $140^\circ$, tentukan sudut keliling yang menghadap busur yang sama. Ini terdengar mudah, dibagi dua saja, tetapi di kelas soal terbalik selalu menampakkan siapa yang paham dan siapa yang menghafal. Siswa yang paham akan bilang, "busurnya sama, jadi dibagi dua, $70^\circ$." Siswa yang menghafal akan ragu, karena di soal mereka biasa diberi sudut kelilingnya, bukan sudut pusatnya.

Ada satu jebakan yang juga saya bahas dengan gambar ini: sudut keliling yang menghadap busur besar $AB$, bukan busur kecil. Kalau titik $C$ saya pindah ke busur kecil $AB$ itu sendiri, sudut kelilingnya tidak lagi $70^\circ$, melainkan menghadap busur besar yang besarnya $360^\circ - 140^\circ = 220^\circ$, sehingga sudut kelilingnya $110^\circ$. Dengan menggeser satu titik di berkas TikZ, siswa bisa melihat busur hijau yang tadinya ramping berubah menjadi lebar. Hubungan dua-kali itu tetap berlaku, hanya busurnya yang berganti. Perubahan satu koordinat yang membuat teorema terlihat tetap berdiri di situasi yang berbeda; itu demonstrasi yang tidak bisa diberikan gambar statis di buku cetak.

> $$
> \angle AOB = 2 \cdot \angle ACB
> \qquad\text{selama } A,\, B,\, C \text{ pada keliling dan } O \text{ di pusat.}
> $$

## Penutup: dari rumus yang dihafal ke hubungan yang dilihat

Malam itu, setelah kelas VIII dan lembar jawaban yang ragu-ragu itu, saya tidak mengubah cara mengajar teorema sudut pusat dan sudut keliling. Saya mengubah gambarnya. Sejak gambar berwarna ini dipakai, saya jarang lagi mendengar jawaban $80^\circ$ yang disertai jari yang tidak yakin. Siswa menunjuk busur dulu, baru membagi atau menggandakan.

Bagi saya, ini persis pekerjaan gambar soal yang baik: ia tidak menambah materi baru, ia hanya membuat hubungan yang sudah ada di materi itu terlihat. TikZ memberi saya jaminan bahwa yang terlihat memang benar, karena setiap sudut di gambar saya hitung dari koordinatnya, bukan dari perasaan. Gambar yang jujur membuat teorema tidak perlu dibela dengan kata-kata; ia membuktikan dirinya sendiri di depan mata siswa.

> 📎 **Berkas TikZ lengkap:** [sudut-pusat-keliling.tex](tex/sudut-pusat-keliling.tex) — dokumen siap kompilasi (butuh paket `tikz` dan `calc`). Silakan geser titik $A$, $B$, atau $C$ untuk membuat variasi soal Anda sendiri.
