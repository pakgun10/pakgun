---
title: "Naik Setapak demi Setapak: Menggambar Ogive Frekuensi Kumulatif dengan TikZ"
date: 2026-10-24T16:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman seri statistika TikZ: dari tabel frekuensi nilai kelas 8C disusun frekuensi kumulatifnya, lalu digambar sebagai ogive — kurva yang menjawab berapa anak di bawah nilai tertentu dan di mana letak mediannya, tanpa rumus."
featuredImage: "featured-image.png"

tags: ["TikZ", "Statistika", "Ogive", "Frekuensi Kumulatif", "Median", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Seri statistika kelas 8C ini sudah melewati diagram batang, histogram, poligon frekuensi, dan tiga garis pemusatan. Pagi ini, sebelum bel pertama, seorang anak menghampiri saya dengan pertanyaan yang tampak sederhana: "Pak, kalau saya mau tahu ada berapa anak yang nilainya di bawah 70, saya harus menghitung satu per satu?" Tidak. Jawabannya sudah ada di tabel — hanya saja tersembunyi di balik kolom yang belum pernah kita buat: frekuensi kumulatif. Dan kalau kolom itu digambar, namanya ogive.

Ogive adalah kurva frekuensi kumulatif. Berbeda dengan histogram yang batangnya berdiri sendiri-sendiri, ogive menghubungkan titik-titik menjadi satu garis yang selalu naik — seperti anak tangga yang tidak pernah turun. Sekali anak paham logikanya, satu gambar ini menjawab banyak pertanyaan: berapa anak di bawah nilai tertentu, berapa anak di atasnya, dan di mana letak mediannya — tanpa satu rumus pun.

<!--more-->

## Dari tabel frekuensi ke tabel kumulatif

Mulainya tetap dari tabel kemarin: 32 nilai, enam interval. Bedanya, sekarang setiap baris saya tambahkan ke baris-baris sebelumnya. Dua anak di interval 40–49, ditambah empat anak di 50–59, menjadi enam anak di bawah 60. Begitu seterusnya sampai baris terakhir yang harus kembali ke 32 — kalau tidak, ada yang salah hitung.

| Interval | Tepi atas | $f$ | $f_k$ (kurang dari) |
|---|---|---|---|
| 40–49 | 49,5 | 2 | 2 |
| 50–59 | 59,5 | 4 | 6 |
| 60–69 | 69,5 | 7 | 13 |
| 70–79 | 79,5 | 9 | 22 |
| 80–89 | 89,5 | 7 | 29 |
| 90–100 | 100,5 | 3 | 32 |

Perhatikan kolom tepi atas, bukan titik tengah. Ogive kurang dari selalu dipasangkan dengan tepi atas kelas: 2 anak itu nilainya kurang dari 49,5 — bukan kurang dari 44,5. Ini detail kecil yang menentukan apakah gambarnya benar atau meleset setengah interval. Dan ada satu titik tambahan yang tidak boleh dilupakan: titik awal $(39{,}5; 0)$. Kurva harus mulai dari nol, di tepi bawah kelas pertama, karena belum ada satu anak pun yang nilainya di bawah itu.

## Menghubungkan titik-titiknya

Skalanya saya samakan dengan gambar kemarin supaya serinya nyambung: sumbu $x$ 0,13 cm per satu nilai, sumbu $y$ 1 cm untuk 8 anak. Titik-titiknya tinggal dihubungkan dengan garis lurus — ogive memang poligon, bukan kurva mulus, meskipun namanya terdengar seperti itu.

```latex
\begin{tikzpicture}
  % sumbu x: 0,13 cm per 1 nilai (35 -> 0 ; 105 -> 9,1)
  % sumbu y: 1 cm = 8 anak
  \draw[->] (-0.3,0) -- (9.6,0);
  \draw[->] (0,0) -- (0,4.8);
  \foreach \v in {40,50,60,70,80,90,100}
    { \pgfmathsetmacro{\x}{(\v-35)*0.13}
      \draw (\x,0) -- (\x,-0.08);
      \node[below, font=\small] at (\x,-0.15) {\v}; }
  \foreach \y/\label in {0/0, 1/8, 2/16, 3/24, 4/32}
    \node[left] at (0,\y) {\label};
  % ogive kurang dari: (tepi atas, fk) -> x = (v-35)*0,13 ; y = fk/8
  \draw[blue, thick] (0.59,0) -- (1.89,0.25) -- (3.19,0.75)
    -- (4.49,1.63) -- (5.79,2.75) -- (7.09,3.63) -- (8.52,4);
  \foreach \x/\y in {0.59/0, 1.89/0.25, 3.19/0.75, 4.49/1.63,
      5.79/2.75, 7.09/3.63, 8.52/4}
    \fill[blue] (\x,\y) circle (2pt);
\end{tikzpicture}
```

Setiap titik saya beri tanda bulat kecil. Tanpa tanda itu, pembaca tidak tahu di mana tepatnya data berada — garisnya bisa dikira kurva bebas, padahal setiap belokannya adalah satu angka dari tabel.

## Membaca median langsung dari kurva

Bagian yang paling saya suka: median bisa dibaca dari gambar, tanpa rumus. Median adalah data ke-16 dari 32 — setengah dari tinggi kurva. Saya tarik garis putus-putus mendatar dari angka 16 di sumbu $y$ sampai menyentuh kurva, lalu garis tegak ke bawah menuju sumbu $x$:

```latex
  % membaca median: n/2 = 16 -> y = 2 ; jatuh di x = 4,91 (nilai 72,8)
  \draw[red, thick, dashed] (0,2) -- (4.91,2) -- (4.91,0);
  \node[below, font=\small, red] at (4.91,-0.15) {72,8};
```

Garis itu jatuh di nilai 72,8 — persis sama dengan median yang kemarin kita hitung dengan rumus. Anak yang kemarin masih meraba-raba rumus median langsung berseru: "Oh, jadi median itu titik tengah kurvanya, Pak!" Tepat. Dan pertanyaan pembuka tadi pun terjawab dari gambar yang sama: tarik garis dari 70 ke atas, baca di sumbu $y$ — sekitar 13–14 anak yang nilainya di bawah 70, tanpa menghitung satu per satu.

## Kesalahan yang hampir selalu muncul

Dua jebakan setiap tahun. Pertama: titik digambar di titik tengah interval, bukan di tepi atas. Gambarnya jadi bergeser setengah interval dan median yang dibaca ikut meleset. Saya selalu mengulang: ogive kurang dari itu "kurang dari tepi atas", bukan "sekitar tengah".

Kedua: kurva dimulai dari titik pertama, bukan dari nol. Tanpa titik $(39{,}5; 0)$, kurva tampak melayang — padahal cerita yang ingin disampaikan justru "dari nol anak, naik setapak demi setapak sampai 32". Titik nol itu bukan hiasan; ia adalah awal cerita.

Terakhir, jangan tertukar dengan kembarannya: ogive lebih dari. Kurvanya menurun, bukan menaik, karena ia menghitung anak yang nilainya lebih dari tiap tepi bawah. Berkas `.tex` di bawah memuat keduanya — ogive kurang dari dan ogive lebih dari berdampingan — supaya perbedaannya terlihat sekali pandang.

Sejak hari itu, pertanyaan "ada berapa anak di bawah 70?" tidak lagi dijawab dengan menghitung ulang. Anak-anak menunjuk kurva, menarik garis, dan membaca jawabannya sendiri. Itulah gunanya menggambar statistika: bukan supaya bukunya penuh gambar, melainkan supaya datanya bisa ditanya dan menjawab sendiri.

Seri ini masih berlanjut — data 8C masih punya satu cerita lagi yang belum digambar.

---

> 📎 **Berkas TikZ lengkap:** [ogive-frekuensi-kumulatif.tex](tex/ogive-frekuensi-kumulatif.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
