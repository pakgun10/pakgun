---
title: "Lima Angka dalam Satu Kotak: Menggambar Diagram Kotak-Garis dengan TikZ"
date: 2026-10-24T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman seri statistika TikZ: dari 32 nilai mentah kelas 8C dihitung kuartil Q1, Q2, Q3 lalu kelima angka ringkasan digambar sebagai diagram kotak-garis — cara tercepat membaca sebaran data tanpa melihat satu per satu."
featuredImage: "featured-image.png"

tags: ["TikZ", "Statistika", "Kuartil", "Box Plot", "Diagram Kotak-Garis", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Seri statistika ini berawal dari satu tabel frekuensi nilai ulangan harian kelas 8C: 32 anak, nilai 40 sampai 98. Dari tabel itu kita sudah menggambar diagram batang, histogram, poligon frekuensi, lalu tiga garis pemusatan. Hari ini saya ingin menunjukkan satu gambar lagi — yang menurut saya paling jujur untuk dibaca anak-anak: diagram kotak-garis, atau yang di buku-buku disebut *box plot*.

Bedanya dengan gambar-gambar sebelumnya: kali ini saya tidak memakai data yang sudah dikelompokkan. Saya memakai 32 nilai mentahnya, diurutkan dari kecil ke besar, lalu diringkas menjadi lima angka: nilai terendah, kuartil pertama, kuartil kedua (median), kuartil ketiga, dan nilai tertinggi. Lima angka itu, digambar sebagai satu kotak berkumis, bercerita lebih banyak daripada yang kita kira.

<!--more-->

## Lima angka dari 32 nilai mentah

Inilah 32 nilai 8C setelah diurutkan — saya tulis apa adanya supaya anak bisa ikut menghitung:

| Urutan | 1–8 | 9–16 | 17–24 | 25–32 |
|---|---|---|---|---|
| Nilai | 45, 48, 52, 55, 57, 59, 61, 63 | 65, 66, 67, 68, 69, 70, 71, 73 | 74, 75, 76, 77, 78, 79, 80, 82 | 84, 85, 86, 88, 89, 91, 94, 98 |

Kuartil membagi data terurut menjadi empat bagian yang sama banyak. Dengan 32 data, caranya mengikuti buku pegangan: mediannya dulu, lalu median dari separuh bawah, lalu median dari separuh atas.

- Nilai terendah = 45, nilai tertinggi = 98.
- Median ($Q_2$) = rata-rata data ke-16 dan ke-17: $Q_2 = \dfrac{73 + 74}{2} = 73{,}5$.
- Separuh bawah adalah data ke-1 sampai ke-16; mediannya rata-rata data ke-8 dan ke-9: $Q_1 = \dfrac{63 + 65}{2} = 64$.
- Separuh atas adalah data ke-17 sampai ke-32; mediannya rata-rata data ke-8 dan ke-9 dari kelompok itu: $Q_3 = \dfrac{82 + 84}{2} = 83$.

Perhatikan: median data mentah ini 73,5, sedangkan perkiraan median dari data berkelompok kemarin 72,8. Bergeser sedikit, persis seperti dugaan saya kemarin — bahan diskusi yang bagus: mengelompokkan data mempermudah, tapi harganya ketelitian. Jangkauan antar-kuartilnya: $IQR = Q_3 - Q_1 = 83 - 64 = 19$. Pagar pencilan bawahnya $64 - 1{,}5 \times 19 = 35{,}5$ dan pagar atasnya $111{,}5$ — keduanya jauh dari data kita, jadi tidak ada pencilan; kumisnya berhenti di 45 dan 98.

## Menggambarnya: kotak untuk separuh tengah, kumis untuk ujung

Kode TikZ-nya ternyata paling sederhana dari seluruh seri ini. Skalanya saya pertahankan sama seperti artikel-artikel sebelumnya — 0,18 cm untuk tiap 1 nilai, patokan 40 — supaya gambarnya bisa dibandingkan antar-artikel.

```latex
\begin{tikzpicture}
  \draw[->] (-0.3,0) -- (11.5,0);          % sumbu bilangan
  \foreach \v in {40,50,60,70,80,90,100}
    { \pgfmathsetmacro{\x}{(\v-40)*0.18}
      \draw (\x,0) -- (\x,-0.08);
      \node[below, font=\small] at (\x,-0.15) {\v}; }
  % kumis: dari nilai terendah ke Q1, dan dari Q3 ke nilai tertinggi
  \draw[thick] (0.9,1.3) -- (4.32,1.3);    % 45 -> 64
  \draw[thick] (7.74,1.3) -- (10.44,1.3);  % 83 -> 98
  \draw[thick] (0.9,1.0) -- (0.9,1.6);     % tutup kumis kiri
  \draw[thick] (10.44,1.0) -- (10.44,1.6); % tutup kumis kanan
  % kotak: separuh tengah data, Q1 s.d. Q3
  \draw[thick, fill=blue!25] (4.32,0.8) rectangle (7.74,1.8);
  \draw[ultra thick, red] (6.03,0.8) -- (6.03,1.8); % median 73,5
\end{tikzpicture}
```

Anak yang kemarin sudah menggambar histogram tidak akan kesulitan membaca kode ini — dan justru di situlah seninya: gambar yang terlihat "mahal" ternyata kodenya paling murah.

## Yang langsung terlihat dari gambarnya

Begitu gambarnya jadi, tiga hal terbaca tanpa menghitung apa-apa. Pertama, kotaknya simetris terhadap garis median: $Q_2 - Q_1 = 9{,}5$ dan $Q_3 - Q_2 = 9{,}5$. Artinya separuh tengah data 8C tersebar merata di kiri-kanan nilai tengah — tidak miring ke mana-mana. Kedua, kumis kirinya lebih panjang (dari 45 ke 64, sepanjang 19) daripada kumis kanannya (dari 83 ke 98, sepanjang 15). Artinya seperempat data terbawah meregang lebih jauh daripada seperempat data teratas — ada dua-tiga anak di ujung bawah yang nilainya jauh tertinggal dari gerombolan tengahnya.

Ketiga — dan ini yang membuat saya tersenyum — seluruh kotak, separuh tengah data, duduk di rentang 64 sampai 83: separuh anak 8C nilainya berada di rentang 19 angka itu. Satu kalimat yang butuh setengah papan tulis kalau dijelaskan dengan tabel, terbaca dalam satu kedipan dari gambar ini. Inilah alasan saya jatuh cinta pada diagram kotak-garis: ia memaksa kita berhenti menghafal rumus dan mulai membaca.

## Dua jebakan yang saya temukan di kelas

Setiap tahun, dua kesalahan yang sama. Pertama: anak menghitung $Q_1$ sebagai "data ke-8". Padahal kuartil pertama adalah *median dari separuh bawah*, bukan data ke seperempat. Dengan 32 data, separuh bawahnya 16 data, mediannya jatuh di antara data ke-8 dan ke-9 — dirata-ratakan. Saya selalu menyuruh anak menuliskan dulu "separuh bawah = data 1–16" sebelum menyentuh kalkulator; satu baris itu mencegah separuh kesalahan.

Kedua: mengira kotak berisi "setengah nilai". Bukan — kotak berisi *setengah data*, yaitu separuh tengah dari 32 anak. Lebar kotak 19 angka bukan berarti "rentang nilai separuh anak", melainkan "jarak antara kuartil bawah dan kuartil atas". Kedengarannya sama, tapi beda: yang satu bicara tentang anak, yang satu tentang angka. Saya meminta anak mengucapkan kalimat lengkapnya: "Separuh anak 8C nilainya antara 64 dan 83." Kalimat itu tidak bisa dihafal tanpa paham.

## Satu berkas untuk dipakai ulang

Berkas `.tex` di bawah ini dokumen utuh: diagram kotak-garis lengkap dengan label kelima angkanya, berkomentar baris per baris, siap kompilasi. Yang perlu diganti untuk data kelas sendiri hanya lima angka: terendah, $Q_1$, median, $Q_3$, tertinggi — hitung dulu seperti di atas, baru gambar. Skala 0,18 cm per nilai bisa dipertahankan selama rentang nilainya mirip dengan 40–100.

Seri statistika 8C hampir selesai — dari tabel ke batang, ke histogram, ke tiga garis, dan kini ke kotak berkumis. Data yang sama, lima gambar, lima cara membaca. Gambar hari ini mengajari saya satu hal: kadang ringkasan terbaik bukanlah angka yang paling teliti, melainkan gambar yang paling jujur dibaca.

---

> 📎 **Berkas TikZ lengkap:** [kuartil-boxplot.tex](tex/kuartil-boxplot.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
