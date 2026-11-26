---
title: "Garis yang Berdiri Tegak di Alas: Menggambar Tinggi Segitiga dengan TikZ"
date: 2026-11-21T20:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Banyak siswa menggambar tinggi segitiga miring ke mana-mana. Dengan TikZ, garis tinggi yang tegak lurus alas bisa dibuat jujur dan terlihat sifatnya."
featuredImage: "featured-image.png"
tags: ["TikZ", "geometri", "segitiga", "tinggi segitiga"]
categories: ["Matematika"]
math:
  enable: true
---

Kalau saya tanya di kelas, "Gambarkan tinggi segitiga ini!", hampir selalu ada tangan yang bergerak percaya diri lalu menghasilkan garis miring yang entah berdiri di mana. Untuk segitiga lancip, siswa biasanya lancar. Tapi begitu segitiganya tumpul, atau begitu titik sudutnya miring ke satu sisi, garis yang mereka tarik sering jadi kuis terselubung: itu tinggi, median, atau garis bagi? Kadang bahkan hanya sekadar garis dari titik puncak ke arah alas "kira-kira di situ".

Dari semua garis istimewa segitiga, tinggi segitiga mungkin yang paling sering digambar salah. Dan masalahnya bukan ketelitian siswa, melainkan sesuatu yang lebih mendasar: mereka belum benar-benar melihat apa yang diminta dari garis itu. Di artikel sebelumnya saya sudah menulis tentang garis bagi sudut dan titik berat. Kali ini giliran garis tinggi — dan seperti biasa, saya mengandalkan TikZ supaya gambar di lembar kerja saya jujur pada apa yang seharusnya terjadi.

<!--more-->

## Sifat tunggal yang menentukan segalanya

Pengertian tinggi segitiga sebenarnya cuma satu kalimat: garis dari suatu titik sudut yang tegak lurus terhadap sisi di seberangnya (atau perpanjangannya). Satu kata kunci: **tegak lurus**. Median menghubungkan titik sudut ke titik tengah sisi, garis bagi membagi sudut jadi dua sama besar, garis tinggi tidak peduli di mana alas dibagi — yang dipedulikan hanya satu hal, garis itu berdiri tegak pada alas, membentuk sudut $90^\circ$.

Masalahnya, pengertian itu mudah dihafal tapi sulit dilihat. Di papan tulis, kalau garis yang saya gambar miring sedikit saja, siswa tidak punya cara mengecek. Tak ada busur derajat yang cukup teliti untuk melihat beda $85^\circ$ dan $90^\circ$ pada gambar asal-asalan. Di sinilah TikZ menang: dia tidak menebak tegak lurus dari tangan saya, dia menghitungnya.

## Menggambar tinggi segitiga lancip

Mulai dari kasus paling ramah. Segitiga $ABC$ dengan alas $BC$ di bawah. Titik $A$ saya letakkan sedikit ke kiri supaya kelak bisa membandingkan dengan kasus tumpul. Tinggi dari $A$ jatuh ke titik $D$ pada $BC$:

```tex
\begin{tikzpicture}[scale=1.2]
  \coordinate (B) at (0,0);
  \coordinate (C) at (6,0);
  \coordinate (A) at (2.2,3);
  % proyeksi A pada BC (y=0), hasilnya D=(2.2,0)
  \coordinate (D) at (2.2,0);
  \draw[thick] (B) -- (C) -- (A) -- cycle;
  \draw[dashed, thick, orange!80!black] (A) -- (D);
  % tanda siku di D, diberi label h
  \draw ($(D)+(0.25,0)$) -- ($(D)+(0.25,0.25)$) -- ($(D)+(0,0.25)$);
  \node[above right] at ($(A)!0.55!(D)$) {$h$};
  \foreach \p/\pos in {A/above, B/below left, C/below right, D/below}
    \node[\pos] at (\p) {$\p$};
\end{tikzpicture}
```

Kunci teknisnya ada di satu baris: koordinat $D$ saya tulis dengan **x yang sama** dengan $A$, y = 0. Karena $BC$ memang terletak pada $y=0$, garis $AD$ otomatis tegak lurus. Saya tidak perlu menaksir "kira-kira di bawah $A$" — saya memastikannya lewat koordinat. Inilah pelajaran penting yang sering saya sampaikan ke siswa ketika mereka mencoba TikZ: kalau sebuah sifat bisa dinyatakan dalam koordinat, gambarlah lewat koordinat itu, jangan lewat mata.

Ini versi lengkap yang siap kompilasi:

```tex
\documentclass[tikz]{standalone}
\usetikzlibrary{calc}
\begin{document}
\begin{tikzpicture}[scale=1.2]
  \coordinate (B) at (0,0);
  \coordinate (C) at (6,0);
  \coordinate (A) at (2.2,3);
  \coordinate (D) at (2.2,0);
  \draw[thick] (B) -- (C) -- (A) -- cycle;
  \draw[dashed, thick, orange!80!black] (A) -- (D);
  \draw ($(D)+(0.25,0)$) -- ($(D)+(0.25,0.25)$) -- ($(D)+(0,0.25)$);
  \node[above right] at ($(A)!0.55!(D)$) {$h$};
  \foreach \p/\pos in {A/above, B/below left, C/below right, D/below}
    \node[\pos] at (\p) {$\p$};
\end{tikzpicture}
\end{document}
```

Tanda siku kecil di $D$ adalah hal yang nyaris selalu lupa siswa buat, padahal dia justru bagian dari makna gambar. Tanpa kotak siku itu, garis putus-putus tinggal jadi garis putus-putus.

## Sisi yang tak mudah dijangkau: tinggi dari titik tumpul

Kasus yang menumbangkan siswa adalah segitiga tumpul. Ambil segitiga $ABC$ yang sama tapi geser $A$ ke kanan sampai dia "menggantung" di luar kaki $BC$. Tinggi dari $C$ terhadap perpanjangan $AB$ sekarang jatuh **di luar segitiga**:

```tex
\begin{tikzpicture}[scale=1.2]
  \coordinate (B) at (0,0);
  \coordinate (C) at (6,0);
  \coordinate (A) at (1.5,2.8);
  % perpanjangan BA cukup jauh, lalu proyeksikan C ke garis AB
  % arah BA = (-1.5,-2.8)/|..| ; proyeksi C di garis AB memberi titik D
  \coordinate (D) at (3.779,0.623);   % hasil perhitungan proyeksi
  \draw[dashed, gray] (A) -- (3.4,-0.36);   % perpanjangan BA
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \draw[dashed, thick, orange!80!black] (C) -- (D);
  \draw ($(D)!0.13!(A)$) -- ($($(D)!0.13!(A)$)!0.13!(D)$) -- (D);
  \node[right] at ($(C)!0.5!(D)$) {$h_c$};
  \foreach \p/\pos in {A/above, B/below left, C/below, D/above}
    \node[\pos] at (\p) {$\p$};
\end{tikzpicture}
```

Di sinilah diskusi kelas jadi seru. Hampir pasti ada yang bertanya, "Lho, kok tingginya di luar segitiga?" Ini pertanyaan emas, bukan gangguan. Saya biasanya balik bertanya: definisi tinggi apa yang kita pakai? Kalau definisinya cuma "garis dari titik sudut ke alas", siswa bingung, karena alasnya $AB$ dan garis itu tidak menyentuh ruas $AB$. Tapi kalau definisi lengkapnya dipakai — tegak lurus terhadap **sisi atau perpanjangannya** — masalahnya luruh. Tinggi segitiga tumpul memang berdiri di perpanjangan sisi, dan sebagian siswa baru sungguh-sungguh menyerap definisi itu ketika melihat gambarnya.

Tiga tinggi pada segitiga lancip bertemu di satu titik (ortosenter, di dalam segitiga). Pada segitiga tumpul, ortosenter kabur ke luar. Kalau digambar dengan TikZ — tiga garis tinggi yang masing-masing benar-benar tegak lurus karena dihitung, bukan ditaksir — siswa bisa melihat sendiri garis-garis itu bertemu di luar, dan tidak ada yang perlu saya perdebatkan soal ketelitian gambar. Angka di koordinat sudah bicara.

## Kenapa saya tetap repot dengan TikZ untuk garis sesederhana ini

Sebenarnya saya bisa menggambar tinggi segitiga di papan tulis dalam sepuluh detik. Tapi lembar kerja itu akan hidup lebih lama dari papan tulis: dia dipotofoto, dipraktikkan di rumah, dipakai tahun depan. Gambar yang $89^\circ$ di papan tulis hari ini akan menjadi miskonsepsi yang diwariskan besok. TikZ memaksa saya jujur: kalau garis tinggi saya miring, berarti koordinat saya salah, dan itu mudah diperbaiki sebelum lembar dicetak.

Sisipan kecil untuk rekan guru yang mau langsung pakai: gambar-gambar di atas bisa disalin ke `geogebra` untuk verifikasi ulang, tapi saya lebih suka langsung membiasakan diri membaca koordinat. Sekali terbiasa, "tegak lurus" tidak lagi jadi tuntutan keahlian tangan, melainkan pernyataan tentang angka — dan itulah cara matematika bekerja.

## Refleksi di akhir jam

Minggu lalu, setelah latihan menggambar tiga garis tinggi pada segitiga tumpul, seorang siswa berkomentar sambil menunjuk kotak siku di gambar, "Pak, tanda kotak kecil ini penting juga ya." Ya, penting. Tanda itu tidak mengubah garisnya sedikit pun, tapi dia menyatakan janji: garis ini bukan garis sembarangan, dia berdiri tegak. Begitu pula dengan TikZ bagi saya — alatnya tidak mengubah matematika yang saya ajarkan, tapi dia memaksa gambar-gambar saya menepati janji yang tertulis di definisi.

Garis tinggi hanya salah satu dari garis istimewa segitiga, dan mungkin bukan yang paling gempar. Tapi di garis inilah siswa belajar hal yang lebih besar: bahwa dalam matematika, kesesuaian gambar dan definisi bisa **dipastikan**, bukan sekadar diharapkan. Dan kalau pelajaran itu melekat, kerja menyiapkan koordinat malam tadi sudah lebih dari terbayar.

> 📎 **Berkas TikZ lengkap:** [tikz-tinggi-segitiga.tex](tex/tikz-tinggi-segitiga.tex) — siap kompilasi (butuh paket `tikz`).
