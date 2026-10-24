---
title: "Batang yang Menyatu: Menggambar Histogram dan Poligon Frekuensi dengan TikZ"
date: 2026-10-24T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lanjutan seri statistika TikZ: mengubah data nilai berkelompok menjadi histogram dan poligon frekuensi — tanpa celah antar batang, tanpa skala yang menipu."
featuredImage: "featured-image.png"

tags: ["TikZ", "Statistika", "Histogram", "Poligon Frekuensi", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Seri statistika ini saya mulai dari satu kekesalan: diagram yang bohong. Kemarin saya menulis tentang diagram batang dan diagram garis, lengkap dengan pengakuan memalukan saya tentang sumbu yang tidak mulai dari nol. Hari ini serinya berlanjut ke diagram yang paling sering bikin siswa salah paham: histogram. Bukan karena histogram sulit — melainkan karena ia terlihat persis seperti diagram batang, padahal bukan.

Data yang saya pakai tetap nyata: 32 nilai ulangan harian Matematika kelas 8C, yang kali ini saya kelompokkan karena nilainya menyebar dari 40 sampai 100. Inilah tabelnya:

| Interval nilai | Frekuensi |
|---|---|
| 40–49 | 2 |
| 50–59 | 4 |
| 60–69 | 7 |
| 70–79 | 9 |
| 80–89 | 7 |
| 90–100 | 3 |

<!--more-->

## Histogram: ketika batangnya tidak boleh bercelah

Perbedaan histogram dan diagram batang sederhana tetapi fundamental. Diagram batang menggambar kategori yang terpisah — "sepeda" dan "diantar" adalah dua hal yang berbeda, maka batangnya diberi jarak. Histogram menggambar interval nilai yang bersambungan: interval 50–59 berakhir tepat di titik interval 60–69 bermula. Memberi celah di antara batangnya sama saja mengatakan ada nilai yang hilang di antara 59 dan 60 — padahal tidak ada.

Maka aturan pertama saya di kelas: **batang histogram harus menempel, tanpa celah**. Aturan keduanya melanjutkan artikel kemarin: sumbu frekuensi tetap mulai dari nol. Dua aturan, dua kejujuran — yang satu menjaga kesinambungan data, yang lain menjaga kejujuran skala.

Kode TikZ-nya mirip diagram batang kemarin, hanya batangnya saya buat menempel. Interval saya beri lebar 1,5 cm, dan skala sumbu saya pakai 1 cm = 4 anak — sama seperti kemarin, supaya konsisten. Tinggi batang dihitung dengan rumus yang sama: $h = \dfrac{f}{4}$ cm. Batang interval 70–79 yang frekuensinya 9 menjadi 2,25 cm, batang interval 40–49 yang frekuensinya 2 menjadi 0,5 cm.

```latex
\begin{tikzpicture}
  % sumbu: x = interval nilai, y = frekuensi (1 cm = 4 anak, mulai dari nol)
  \draw[->] (0,0) -- (9.5,0);
  \draw[->] (0,0) -- (0,3.5);
  \foreach \y/\label in {0/0, 1/4, 2/8}
    \node[left] at (0,\y) {\label};
  % batang MENEMPEL, tanpa celah: lebar 1,5 cm, tinggi = f/4
  \fill[teal!60]   (0,0) rectangle (1.5,0.5);   % 40-49: 2
  \fill[teal!60]   (1.5,0) rectangle (3,1);     % 50-59: 4
  \fill[orange!70] (3,0) rectangle (4.5,1.75);  % 60-69: 7
  \fill[blue!50]   (4.5,0) rectangle (6,2.25);  % 70-79: 9
  \fill[orange!70] (6,0) rectangle (7.5,1.75);  % 80-89: 7
  \fill[teal!60]   (7.5,0) rectangle (9,0.75);  % 90-100: 3
  % label interval di tengah tiap batang
  \foreach \x/\t in {0.75/40-49, 2.25/50-59, 3.75/60-69,
                      5.25/70-79, 6.75/80-89, 8.25/90-100}
    \node[below, font=\small] at (\x,-0.15) {\t};
\end{tikzpicture}
```

Perhatikan angka frekuensinya tetap saya tulis — kebiasaan dari kemarin saya pertahankan. Histogram yang baik tidak memaksa pembacanya memperkirakan tinggi batang.

## Poligon frekuensi: menghubungkan titik tengah

Histogram menunjukkan bentuk sebaran, tetapi kadang saya ingin melihat "puncak" dan "kemiringan" datanya dengan lebih tegas — misalnya ketika membandingkan sebaran dua kelas dalam satu gambar. Di sinilah poligon frekuensi berguna: ia menghubungkan titik tengah tiap interval dengan garis.

Titik tengah interval 40–49 adalah 44,5, yang dalam gambar terletak tepat di tengah batang pertama — koordinat $(0{,}75;\,0{,}5)$ pada skala di atas. Poligonnya saya gambar dengan cara baku: mulai dari sumbu di setengah interval sebelum batang pertama, hubungkan semua titik tengah, lalu turunkan kembali ke sumbu di setengah interval sesudah batang terakhir. Bentuknya seperti tenda — dan bentuk tenda inilah yang membuat sebaran data mudah dibaca.

```latex
\begin{tikzpicture}
  % sumbu sama seperti histogram di atas
  \draw[->] (0,0) -- (9.5,0);
  \draw[->] (0,0) -- (0,3.5);
  \foreach \y/\label in {0/0, 1/4, 2/8}
    \node[left] at (0,\y) {\label};
  % poligon frekuensi: dari (0,0), lewat titik tengah tiap interval, ke (9,0)
  \draw[thick, blue] (0,0) -- (0.75,0.5) -- (2.25,1) -- (3.75,1.75)
    -- (5.25,2.25) -- (6.75,1.75) -- (8.25,0.75) -- (9,0);
  \foreach \x/\y/\t in {0.75/0.5/2, 2.25/1/4, 3.75/1.75/7,
                         5.25/2.25/9, 6.75/1.75/7, 8.25/0.75/3}
    { \fill[blue] (\x,\y) circle (2.5pt);
      \node[above, font=\small] at (\x,\y) {\t}; }
  % garis bantu tipis supaya posisi interval tetap terbaca
  \foreach \x/\t in {0.75/40-49, 2.25/50-59, 3.75/60-69,
                      5.25/70-79, 6.75/80-89, 8.25/90-100}
    \node[below, font=\small] at (\x,-0.15) {\t};
\end{tikzpicture}
```

Cerita di balik gambar ini nyata di kelas saya: puncaknya ada di interval 70–79. Begitu poligon ini saya proyeksikan, seorang anak langsung bertanya: "Pak, berarti nilai saya yang 75 itu termasuk yang paling banyak ya?" Dia benar — dan pertanyaan itu tidak akan lahir dari sekadar melihat tabel angka.

## Kesalahan yang hampir selalu muncul

Setiap tahun, setidaknya ada tiga anak di kelas saya yang menggambar histogram dengan celah antar batang — mereka mencontek pola diagram batang kemarin. Saya tidak menyalahkan mereka; gambarnya memang mirip. Cara saya memperbaikinya pun sederhana: saya tanya, "di antara 59 dan 60, ada nilai berapa yang hilang?" Begitu mereka menjawab tidak ada, mereka sendiri yang menghapus celahnya.

Kesalahan kedua: menggambar poligon frekuensi dari titik sudut batang, bukan dari titik tengahnya. Padahal titik tengah itulah yang mewakili interval — 44,5 mewakili 40–49, bukan 40 atau 49. Saya selalu minta mereka menulis dulu titik tengahnya di tabel sebelum menggambar. Lima menit tambahan di awal, menghemat tiga puluh menit salah gambar.

## Satu pola untuk dipakai ulang

Kedua gambar di atas sudah saya satukan dalam satu berkas `.tex` yang terlampir di akhir artikel, seperti biasa: dokumen LaTeX utuh, siap kompilasi, berkomentar baris per baris. Untuk memakainya di kelas sendiri, yang perlu diganti hanya tiga hal: frekuensinya, batas intervalnya, dan skalanya bila datanya jauh lebih besar. Batangnya harus tetap menempel, sumbunya harus tetap mulai dari nol — dua aturan yang tidak boleh ditawar.

Sama seperti artikel-artikel sebelumnya di seri ini, saya tidak mengajarkan kode ini ke siswa. Ini perkakas guru. Yang sampai ke tangan siswa adalah gambarnya: di soal ulangan, di bahan ajar, di slide pembahasan. Seri statistika ini masih berlanjut — data saya masih punya cerita yang belum selesai digambar.

---

> 📎 **Berkas TikZ lengkap:** [histogram-poligon-frekuensi.tex](tex/histogram-poligon-frekuensi.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
