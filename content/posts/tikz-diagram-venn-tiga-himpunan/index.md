---
title: "Tiga Lingkaran, Tujuh Daerah: Menggambar Diagram Venn Tiga Himpunan dengan TikZ"
date: 2026-11-09T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Dua lingkaran hanya memberi empat daerah, padahal survei tiga ekstrakurikuler butuh tujuh. Di tulisan ini saya menggambar diagram Venn tiga himpunan dengan TikZ — tiga lingkaran yang pusatnya membentuk segitiga, irisan bertingkat, dan angka yang jatuh di daerah yang benar."
featuredImage: "featured-image.png"

tags: ["TikZ", "Himpunan", "Diagram Venn", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu saya menyurvei 40 siswa kelas VII tentang ekstrakurikuler yang mereka ikuti: sepak bola, basket, dan voli. Datanya sudah saya rekap, tinggal digambar. Saya buka berkas diagram Venn dua himpunan yang pernah saya buat, lalu sadar: dua lingkaran hanya memberi empat daerah, padahal tiga ekstrakurikuler butuh tujuh daerah — tiga yang hanya satu, tiga irisan dua, dan satu irisan tiga. Saya coba menggambar tiga lingkaran di papan tulis, dan hasilnya berantakan: lingkaran ketiga menutupi angka yang sudah saya tulis, dan seorang siswa bertanya, "Pak, angka 4 itu di irisan yang mana?" Saya tidak bisa menjawab dengan yakin. Malam harinya saya menggambar ulang dengan TikZ, dan tulisan ini adalah catatan caranya.

<!--more-->

## Kenapa tiga himpunan butuh tujuh daerah

Satu lingkaran membagi persegi panjang semesta menjadi dua daerah: di dalam dan di luar. Lingkaran kedua memotong lingkaran pertama dan menambah dua daerah baru, sehingga totalnya empat. Lingkaran ketiga memotong kedua lingkaran yang sudah ada sekaligus, dan setiap potongannya menambah satu daerah lagi — totalnya tujuh daerah di dalam, ditambah satu daerah di luar ketiga lingkaran untuk siswa yang tidak mengikuti apa pun. Polanya jelas: satu himpunan dua daerah, dua himpunan empat daerah, tiga himpunan delapan daerah. Kalau ada yang menggambar tiga lingkaran tetapi hanya menemukan enam daerah, hampir pasti satu lingkarannya tidak benar-benar memotong kedua lingkaran lain — ia hanya menempel di pinggir.

Karena itu, sebelum menulis satu baris kode pun, saya menulis dulu tujuh angka dari survei saya di selembar kertas, lalu memeriksa jumlahnya. Hanya sepak bola ada $8$ siswa, hanya basket $6$, hanya voli $5$. Yang ikut sepak bola dan basket saja ada $4$, sepak bola dan voli saja $3$, basket dan voli saja $2$. Yang ikut ketiganya hanya $1$ siswa, dan yang tidak ikut satu pun ada $11$ siswa. Jumlahnya: $8 + 6 + 5 + 4 + 3 + 2 + 1 + 11 = 40$, sama dengan jumlah siswa yang disurvei. Pemeriksaan sederhana ini penting, karena kesalahan paling mahal dalam menggambar diagram Venn bukan garisnya yang miring, melainkan angkanya yang salah tempat.

## Pusat tiga lingkaran membentuk segitiga

Kunci diagram Venn tiga himpunan adalah posisi pusat ketiganya. Kalau ketiga pusat diletakkan segaris, yang terjadi bukan diagram Venn melainkan tiga lingkaran yang saling menumpuk seperti rantai — daerah irisan tiga tidak akan pernah muncul. Pusatnya harus membentuk segitiga: satu di atas, dua di bawah, dengan jarak yang sama antarpusat. Saya memakai segitiga dengan sisi $2{,}3$ cm dan jari-jari lingkaran $1{,}9$ cm, sehingga setiap pasang lingkaran saling memotong di dua titik dan ketiga lingkaran bertemu di satu daerah kecil di tengah.

```latex
\begin{tikzpicture}[scale=1.0, font=\large]
  % Tiga pusat membentuk segitiga sama sisi (kira-kira)
  \coordinate (A) at (0, 1.15);
  \coordinate (B) at (-1.15, -0.75);
  \coordinate (C) at (1.15, -0.75);
  % Ketiga lingkaran: sepak bola, basket, voli
  \draw[thick, fill=blue!15]   (A) circle (1.9);
  \draw[thick, fill=red!15]    (B) circle (1.9);
  \draw[thick, fill=green!15]  (C) circle (1.9);
  \node at (0, 3.1) {$S$};
  \node at (-2.6, -1.9) {$B$};
  \node at (2.6, -1.9) {$V$};
\end{tikzpicture}
```

Tiga hal yang saya jaga di potongan kode ini. Pertama, saya memberi nama pada ketiga pusat dengan `\coordinate` sebelum menggambar lingkarannya, supaya kalau jaraknya perlu diubah, saya hanya mengubah tiga baris itu. Kedua, saya memakai warna isi yang berbeda untuk tiap himpunan dengan transparansi yang sama, supaya daerah irisan terlihat sebagai campuran warna. Ketiga, label himpunan saya letakkan di luar lingkaran, jauh dari angka — label di dalam lingkaran akan berebut tempat dengan angka daerah.

## Mewarnai irisan tiga dengan trik clip

Bagian yang paling saya sukai dari gambar ini adalah irisan ketiganya: daerah kecil di tengah tempat satu siswa itu berada. Kalau digambar biasa, daerah itu hanya terlihat sebagai campuran tiga warna isi, dan mata sulit membedakannya dari irisan dua. Saya ingin daerah itu punya warna sendiri yang tegas, supaya ketika saya bertanya "di mana siswa yang ikut ketiganya?" seluruh kelas menunjuk ke tempat yang sama. Caranya adalah trik `clip` yang sama seperti pada diagram Venn dua himpunan, hanya dipakai dua kali: potong dulu dengan lingkaran pertama, lalu potong hasilnya dengan lingkaran kedua, dan warnai lingkaran ketiga di dalam potongan itu.

```latex
% Irisan tiga: hanya daerah yang ada di ketiga lingkaran
\begin{scope}
  \clip (A) circle (1.9);
  \clip (B) circle (1.9);
  \fill[orange, fill opacity=0.45] (C) circle (1.9);
\end{scope}
% Gambar ulang garis lingkarannya supaya tetap tegas
\draw[thick] (A) circle (1.9);
\draw[thick] (B) circle (1.9);
\draw[thick] (C) circle (1.9);
```

Perintah `clip` di TikZ bekerja seperti memotong kertas: semua yang digambar setelahnya hanya muncul di dalam daerah potongan. Dua `clip` berurutan berarti daerah yang tersisa hanyalah irisan pertama dan kedua. Di dalam daerah itu saya mengisi lingkaran ketiga dengan warna oranye, sehingga hanya bagian yang sekaligus berada di ketiga lingkaran yang berwarna. Setelah itu saya menggambar ulang ketiga garis lingkarannya, karena perintah `fill` di dalam `scope` ikut menimpa garis tepi di daerah irisan. Tanpa tiga baris `\draw` terakhir itu, garis lingkaran di sekitar irisan tiga akan terlihat pudar.

## Menaruh angka di daerah yang benar

Langkah terakhir adalah menaruh tujuh angka di tujuh daerah, ditambah angka $11$ di luar ketiga lingkaran. Inilah bagian yang paling mudah salah: angka irisan dua yang ditulis di irisan tiga, atau sebaliknya. Saya punya satu patokan sederhana: angka irisan dua diletakkan di dekat titik potong dua lingkaran yang bersangkutan, tetapi jauh dari lingkaran ketiga; angka irisan tiga diletakkan di titik berat segitiga pusat, yaitu kira-kira di $(0, 0{,}15)$ untuk ukuran gambar saya. Angka "hanya satu himpunan" diletakkan di dekat tepi lingkaran yang bersangkutan, di sisi yang berlawanan dengan pusat gambar.

```latex
% Angka: hanya satu himpunan
\node at (0, 2.35) {$8$};
\node at (-2.15, -1.35) {$6$};
\node at (2.15, -1.35) {$5$};
% Angka: irisan dua himpunan
\node at (-0.85, 0.55) {$4$};
\node at (0.85, 0.55) {$3$};
\node at (0, -1.15) {$2$};
% Angka: irisan tiga himpunan
\node at (0, 0.15) {$1$};
```

Setelah semua angka terpasang, saya memeriksa gambar dengan satu cara yang sama seperti memeriksa jawaban siswa: saya membaca tiap daerah dan membandingkannya dengan tabel survei. Hanya sepak bola $8$ — cocok. Sepak bola dan basket saja $4$ — cocok. Ketiganya $1$ — cocok. Lalu saya menjumlahkan semua angka di dalam persegi panjang semesta: $29$ siswa mengikuti sedikitnya satu ekstrakurikuler, ditambah $11$ yang tidak mengikuti apa pun, sama dengan $40$. Kalau jumlahnya tidak cocok, saya tidak memperbaiki gambarnya dulu — saya memeriksa tabelnya, karena hampir selalu tabelnyalah yang salah ketik.

Tiga lingkaran, tujuh daerah, satu pemeriksaan jumlah di akhir. Itu resepnya. Dan sejak gambar ini saya pakai di kelas, tidak ada lagi siswa yang bertanya angka 4 itu di irisan yang mana — karena sekarang jawabannya terlihat, bukan ditebak.

> 📎 **Berkas TikZ lengkap:** [venn-tiga-himpunan.tex](tex/venn-tiga-himpunan.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
