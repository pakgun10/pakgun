---
weight: 1
title: "Tegak Lurus Tanpa Busur Derajat: Menggambar Garis Tegak Lurus dari Titik di Luar Garis dengan TikZ"
date: 2026-11-02T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Dari satu titik di luar garis, garis tegak lurus bisa ditemukan tanpa mengukur sudut sama sekali: satu busur dari titik itu memotong garis di dua tempat, lalu dua busur dari kedua tempat itu bertemu di titik yang menentukan garisnya."
featuredImage: "featured-image.png"
tags: ["TikZ", "LaTeX", "Garis Tegak Lurus", "Konstruksi", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]
math:
  enable: true
---

Pekan lalu, seorang siswa bertanya kepada saya sambil menunjuk gambar di buku: "Pak, kalau titiknya tidak menempel di garis, bagaimana cara menarik garis tegak lurusnya?" Pertanyaan itu bagus, karena selama ini sebagian besar siswa hanya pernah menarik garis tegak lurus dari titik yang sudah terletak pada garis itu sendiri. Begitu titiknya melayang di luar garis, mereka kebingungan: dari mana harus mulai, dan bagaimana memastikan garis yang ditarik benar-benar tegak lurus, bukan sekadar tampak tegak lurus.

Di kelas, saya menjawabnya bukan dengan busur derajat, melainkan dengan jangka: satu titik ditemukan oleh perpotongan dua busur, bukan oleh tebakan mata. Setelah siswa melihat sendiri mengapa cara itu bekerja, saya menuangkannya ke TikZ, supaya langkahnya bisa dicetak di lembar kerja dan dipakai lagi tahun depan.

<!--more-->

## Langkah pertama: gambar garis dan titiknya dulu

Segala konstruksi dimulai dari sesuatu yang sudah pasti: sebuah garis, sebut saja garis $l$, dan sebuah titik $P$ di luar garis itu. Saya meletakkan garis $l$ mendatar, dan titik $P$ tiga satuan di atas garis, tepatnya di $(3,4)$ kalau garisnya kita anggap sebagai sumbu $x$. Angka ini saya pilih sengaja: jarak $P$ ke garis adalah 4 satuan, sebuah angka yang nanti membuat perhitungannya jatuh rapi.

```latex
\begin{tikzpicture}
  \draw[thick] (-1,0) -- (7,0);
  \node[right] at (7,0) {$l$};
  \fill (3,4) circle (2pt);
  \node[above] at (3,4) {$P$};
\end{tikzpicture}
```

Satu kebiasaan yang saya tekankan: gambar garisnya cukup panjang ke kiri dan ke kanan, supaya busur berikutnya tidak keluar dari gambar.

## Langkah kedua: satu busur dari titik P memotong garis di dua tempat

Sekarang jangka mulai bekerja. Jarum jangka ditancapkan di $P$, lalu jangka dibuka selebar 5 satuan dan digoreskan memotong garis $l$. Karena jari-jarinya lebih besar daripada jarak $P$ ke garis, busur itu pasti memotong garis di dua tempat. Di TikZ, saya menggambar busur itu sebagai lingkaran yang dipotong tampilannya hanya pada bagian di bawah garis, supaya yang tampak hanyalah busur yang melintasi garis itu.

```latex
\begin{tikzpicture}
  \draw[thick] (-1,0) -- (7,0);
  \node[right] at (7,0) {$l$};
  \begin{scope}
    \clip (-1,-1.5) rectangle (7,0.5);
    \draw[dashed, blue] (3,4) circle (5);
  \end{scope}
  \fill (3,4) circle (2pt);
  \fill (0,0) circle (2pt);
  \fill (6,0) circle (2pt);
  \node[above] at (3,4) {$P$};
  \node[below] at (0,0) {$M$};
  \node[below] at (6,0) {$N$};
\end{tikzpicture}
```

Busur itu memotong garis di titik $M = (0,0)$ dan titik $N = (6,0)$. Dua titik inilah kunci seluruh konstruksi: jarak $P$ ke $M$ sama dengan jarak $P$ ke $N$, yaitu 5 satuan, karena keduanya terletak pada busur yang sama dengan pusat $P$. Titik tengah $MN$ memang $(3,0)$, tepat di bawah $P$, tetapi di atas kertas siswa belum boleh menganggap itu sudah diketahui — ia harus menemukannya lewat langkah berikutnya.

## Langkah ketiga: dua busur dari M dan N bertemu di bawah garis

Inilah langkah yang paling memuaskan untuk dilihat. Jangka dipindahkan ke $M$, dibuka selebar 5 satuan, lalu digoreskan ke bawah garis. Kemudian hal yang sama dilakukan dari $N$, dengan lebar jangka yang tidak diubah. Kedua goresan itu bertemu di satu titik di bawah garis, yang saya namai $Q$. Di TikZ, kedua busur itu saya gambar dengan perintah yang sama seperti sebelumnya: lingkaran penuh yang dipotong tampilannya hanya pada bagian di bawah garis.

```latex
\begin{tikzpicture}
  \draw[thick] (-1,0) -- (7,0);
  \node[right] at (7,0) {$l$};
  \begin{scope}
    \clip (-1,-4.5) rectangle (7,0);
    \draw[dashed, red] (0,0) circle (5);
    \draw[dashed, red] (6,0) circle (5);
  \end{scope}
  \fill (3,4) circle (2pt);
  \fill (0,0) circle (2pt);
  \fill (6,0) circle (2pt);
  \fill (3,-4) circle (2pt);
  \node[above] at (3,4) {$P$};
  \node[below] at (0,0) {$M$};
  \node[below] at (6,0) {$N$};
  \node[below] at (3,-4) {$Q$};
\end{tikzpicture}
```

Titik $Q$ berada di $(3,-4)$. Angka itu bukan tebakan: jarak $Q$ ke $M$ dan ke $N$ masing-masing tepat 5 satuan, karena kedua busur digambar dengan lebar jangka yang sama. Polanya adalah segitiga 3-4-5 yang muncul dua kali: dari $P$ ke garis, setengah jarak $MN$ adalah 3 satuan dan jarak tegaknya 4 satuan; dari $Q$ ke garis pun demikian, hanya arahnya ke bawah.

## Langkah keempat: tarik garisnya dari P melalui Q

Langkah terakhir adalah yang paling sederhana, tetapi paling sering dikerjakan tergesa-gesa: tarik garis dari $P$ melalui $Q$, dan tandai perpotongannya dengan garis $l$ sebagai titik $F$. Garis $PQ$ itulah garis tegak lurus yang dicari, dan saya menandainya dengan tanda siku-siku kecil di titik $F$, supaya tegak lurusnya terlihat tanpa harus mengukur lagi.

```latex
\begin{tikzpicture}
  \draw[thick] (-1,0) -- (7,0);
  \node[right] at (7,0) {$l$};
  \draw[thick, blue] (3,4) -- (3,-4);
  \draw (3,0) -- (3.4,0) -- (3.4,0.4) -- (3,0.4);
  \fill (3,4) circle (2pt);
  \fill (0,0) circle (2pt);
  \fill (6,0) circle (2pt);
  \fill (3,-4) circle (2pt);
  \fill (3,0) circle (2pt);
  \node[above] at (3,4) {$P$};
  \node[below] at (0,0) {$M$};
  \node[below] at (6,0) {$N$};
  \node[below] at (3,-4) {$Q$};
  \node[below] at (3,0) {$F$};
\end{tikzpicture}
```

Mengapa garis ini dijamin tegak lurus? Karena $P$ dan $Q$ sama-sama berjarak sama dari $M$ dan $N$: $PM = PN = 5$ satuan dan $QM = QN = 5$ satuan. Dua titik yang masing-masing berjarak sama dari ujung-ujung sebuah ruas garis pasti terletak pada sumbu ruas garis itu, yaitu garis yang tegak lurus ruas garis dan melalui titik tengahnya. Jadi garis $PQ$ adalah sumbu ruas garis $MN$: ia tegak lurus garis $l$ dan memotongnya tepat di titik tengah $MN$, yaitu $F = (3,0)$. Satu konstruksi menjelaskan dua hal sekaligus, tegak lurus dan titik tengah.

## Tiga kesalahan yang paling sering saya temui

Selama mengajar konstruksi ini, tiga kesalahan muncul berulang-ulang. Pertama, busur dari $P$ dibuka terlalu kecil, lebih kecil daripada jarak $P$ ke garis, sehingga busurnya tidak memotong garis sama sekali dan siswa kebingungan mencari $M$ dan $N$ yang tidak ada. Kedua, lebar jangka diubah antara busur dari $M$ dan busur dari $N$, sehingga $QM$ tidak lagi sama dengan $QN$ dan titik $Q$ meleset dari garis tegak yang benar. Ketiga, garis ditarik dari $P$ ke $M$ atau ke $N$, bukan dari $P$ melalui $Q$ — padahal garis tegak lurusnya harus melalui titik temu kedua busur itu, dan titik $F$ baru ditemukan sesudah garisnya ditarik, bukan sebelum.

Konstruksi ini adalah bekal untuk materi berikutnya: jarak titik ke garis, tinggi segitiga, dan garis sumbu segitiga. Polanya sama: satu titik ditemukan oleh perpotongan dua busur, bukan oleh tebakan mata. Begitu siswa merasakannya sendiri, ia mulai memandang jangka bukan lagi sebagai alat menggambar lingkaran, melainkan sebagai alat berpikir.

📎 **Berkas TikZ lengkap:** [garis-tegak-lurus-titik-luar.tex](tex/garis-tegak-lurus-titik-luar.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
