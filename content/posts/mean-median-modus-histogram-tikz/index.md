---
title: "Tiga Garis di Atas Histogram: Mean, Median, dan Modus Digambar dengan TikZ"
date: 2026-10-24T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman seri statistika TikZ: menghitung rata-rata, median, dan modus dari data nilai yang sama, lalu menggambar ketiganya sebagai garis tegak di atas histogram — dan membaca apa kata gambarnya."
featuredImage: "featured-image.png"

tags: ["TikZ", "Statistika", "Mean", "Median", "Modus", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Histogram kemarin sudah menunjukkan bentuk sebaran nilai kelas 8C: puncaknya di interval 70–79, ekornya tipis di dua ujung. Kemarin sore, seusai bel pulang, seorang anak menghampiri meja saya. "Pak, kalau ditanya nilai tengah kelas kita berapa, jawabnya yang mana?" Saya tersenyum — pertanyaan satu kalimat, jawabannya tiga angka.

Tiga ukuran pemusatan itu — rata-rata, median, modus — biasanya saya ajarkan sebagai tiga rumus di papan tulis. Hari ini saya memutuskan menggambarnya: tiga garis tegak di atas histogram yang sama, supaya anak-anak melihat sendiri di mana ketiganya berdiri. Datanya tetap yang kemarin, 32 nilai yang dikelompokkan menjadi enam interval, supaya serinya nyambung.

<!--more-->

## Menghitung dulu: tiga angka dari data yang sama

| Interval | Titik tengah ($x_i$) | $f_i$ | $f_i \cdot x_i$ |
|---|---|---|---|
| 40–49 | 44,5 | 2 | 89 |
| 50–59 | 54,5 | 4 | 218 |
| 60–69 | 64,5 | 7 | 451,5 |
| 70–79 | 74,5 | 9 | 670,5 |
| 80–89 | 84,5 | 7 | 591,5 |
| 90–100 | 95 | 3 | 285 |
| **Jumlah** | | **32** | **2305,5** |

Rata-ratanya: $\bar{x} = \dfrac{2305{,}5}{32} = 72{,}0$.

Mediannya jatuh di interval 70–79, karena frekuensi kumulatifnya 2, 6, 13, 22 — data ke-16 dan ke-17 ada di sana:

$$Me = L + \left(\frac{\frac{n}{2} - F}{f}\right)\cdot p = 69{,}5 + \left(\frac{16 - 13}{9}\right)\cdot 10 = 72{,}8$$

Modusnya juga di interval 70–79, dengan $d_1 = 9-7 = 2$ dan $d_2 = 9-7 = 2$:

$$Mo = L + \left(\frac{d_1}{d_1 + d_2}\right)\cdot p = 69{,}5 + \left(\frac{2}{2+2}\right)\cdot 10 = 74{,}5$$

Tiga angka sudah di tangan: 72,0 — 72,8 — 74,5. Sekarang bagian yang menyenangkan: menggambarnya.

## Tiga garis di atas gambar kemarin

Ada satu perubahan penting dari kode kemarin: sumbu $x$-nya bukan lagi nomor interval, melainkan nilai itu sendiri. Interval 40–50 saya gambar dari $x = 0$ sampai $x = 1{,}8$ (skala 0,18 cm per satu nilai), supaya garis rata-rata 72,0 benar-benar jatuh di posisi nilai 72 — bukan sekadar di tengah batang. Batangnya sendiri sama persis seperti kemarin, hanya koordinatnya yang digeser ke skala nilai.

```latex
\begin{tikzpicture}
  % sumbu x: 0,18 cm per 1 nilai (40 -> 0 ; 100 -> 10,8)
  % sumbu y: 1 cm = 4 anak, mulai dari NOL
  \draw[->] (-0.3,0) -- (11.5,0);
  \draw[->] (0,0) -- (0,4);
  \foreach \v in {40,50,60,70,80,90,100}
    { \pgfmathsetmacro{\x}{(\v-40)*0.18}
      \draw (\x,0) -- (\x,-0.08);
      \node[below, font=\small] at (\x,-0.15) {\v}; }
  \foreach \y/\label in {0/0, 1/4, 2/8}
    \node[left] at (0,\y) {\label};
  % histogram kemarin, digambar ulang pada skala nilai; tinggi = f/4
  \fill[teal!40]   (0,0) rectangle (1.8,0.5);    % 40-49: 2
  \fill[teal!40]   (1.8,0) rectangle (3.6,1);    % 50-59: 4
  \fill[orange!40] (3.6,0) rectangle (5.4,1.75); % 60-69: 7
  \fill[blue!40]   (5.4,0) rectangle (7.2,2.25); % 70-79: 9
  \fill[orange!40] (7.2,0) rectangle (9,1.75);   % 80-89: 7
  \fill[teal!40]   (9,0) rectangle (10.8,0.75);  % 90-100: 3
  % tiga garis tegak putus-putus; label disusun bertingkat
  \draw[red, thick, dashed] (5.77,0) -- (5.77,2.9)
    node[above, font=\small, red] {rata-rata 72,0};
  \draw[blue, thick, dashed] (5.91,0) -- (5.91,3.3)
    node[above, font=\small, blue] {median 72,8};
  \draw[green!50!black, thick, dashed] (6.21,0) -- (6.21,3.7)
    node[above, font=\small, green!50!black] {modus 74,5};
\end{tikzpicture}
```

Trik kecil yang saya pelajari saat membuatnya: ketiga garisnya berdekatan sekali, jadi labelnya saya susun bertingkat — rata-rata di ketinggian 2,9, median 3,3, modus 3,7. Kalau ketiganya diberi label sejajar, tulisannya bertumpuk dan tidak terbaca.

## Yang dikatakan gambarnya

Begitu tiga garis itu saya proyeksikan, kelas hening sebentar. Ketiganya berkumpul dalam rentang kurang dari tiga nilai: 72,0 — 72,8 — 74,5. Tidak ada yang menyangka, termasuk saya waktu pertama menghitungnya.

Inilah hadiah dari menggambar: tiga rumus hafalan berubah menjadi satu cerita. Ketika rata-rata, median, dan modus berkumpul sedekat ini, sebarannya nyaris simetris — nilai-nilai menumpuk di tengah, ekornya tipis di dua sisi. Anak yang kemarin bertanya langsung paham: "Berarti kelas kita kebanyakan dapat tujuh puluhan ya, Pak?" Tepat sekali. Itulah jawaban satu kalimat untuk pertanyaan satu kalimatnya.

## Kesalahan yang hampir selalu muncul

Dua jebakan setiap tahun. Pertama: anak menjawab modus = 9. Itu frekuensinya, bukan modusnya — modus adalah nilai 74,5, nilai yang diperkirakan paling sering muncul. Saya selalu mengulang: modus itu nilai, bukan banyaknya.

Kedua: mengira 72,0 adalah rata-rata yang persis. Bukan — ini perkiraan dari data yang sudah dikelompokkan, karena kita memakai titik tengah sebagai wakil tiap interval. Saya jujur soal ini di kelas: kalau dihitung dari 32 nilai mentahnya, hasilnya bisa bergeser sedikit. Kejujuran kecil seperti ini penting; anak-anak perlu tahu bahwa statistika data berkelompok itu seni memperkirakan, bukan sulap.

## Satu berkas untuk dipakai ulang

Seperti biasa, berkas `.tex` di bawah ini dokumen utuh: histogram plus tiga garisnya, berkomentar baris per baris, siap kompilasi. Untuk memakainya di kelas sendiri, yang perlu diganti hanya tiga hal: frekuensinya, batas intervalnya, dan posisi ketiga garisnya — hitung dulu seperti di atas, baru gambar. Skala 0,18 cm per nilai bisa dipertahankan selama rentang nilainya mirip.

Seri statistika ini masih berlanjut — data 8C masih punya cerita yang belum selesai digambar. Gambar hari ini mengajari saya satu hal: kadang cara terbaik menjelaskan rumus adalah berhenti menulis rumus, dan mulai menggambarnya.

---

> 📎 **Berkas TikZ lengkap:** [mean-median-modus-histogram.tex](tex/mean-median-modus-histogram.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
