---
weight: 1
title: "Menandai Pecahan di Garis Bilangan dengan TikZ: Supaya Letaknya Tidak Lagi Ditebak"
date: 2026-11-02T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya sering menandai pecahan di garis bilangan dengan kira-kira. Dengan TikZ, ruas 0 sampai 1 dibagi menjadi bagian-bagian yang persis sama, sehingga letak pecahan seperti 2/3 dan 4/3 bisa ditunjuk, bukan ditebak."
featuredImage: "featured-image.png"
tags: ["TikZ", "LaTeX", "Pecahan", "Garis Bilangan", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]
math:
  enable: true
---

Pekan lalu, di kelas VII, saya menggambar garis bilangan 0 sampai 2 di papan tulis, lalu bertanya, "Di mana letak $\frac{2}{3}$?" Seorang siswa maju dengan percaya diri dan menancapkan titik persis di tengah antara 0 dan 1. Siswa lain menaruhnya lebih dekat ke 1, dengan alasan "karena 2 itu hampir 3". Ada juga yang menaruhnya dekat angka 2, di luar ruas 0 sampai 1, karena ia membaca $\frac{2}{3}$ sebagai "dua, tiga".

Tiga jawaban, tiga letak, semuanya ditebak. Padahal garis bilangan adalah alat ukur, bukan tempat menebak. Masalahnya, garis yang biasa kami gambar hanya memberi rumah bagi bilangan bulat: 0, 1, dan 2 sudah punya tanda, sedangkan pecahan tidak, sehingga siswa memperlakukannya seperti tamu yang boleh berdiri di mana saja. Pekan ini saya memperbaiki garis itu dengan TikZ, dan perbaikannya hanya satu kalimat: bagi dulu ruasnya sama besar, baru tandai pecahannya.

<!--more-->

## Garis bilangan pecahan itu garis yang dibagi, bukan ditambah

Sebelum menggambar apa pun, saya mengajak siswa menyepakati dulu artinya. Pecahan $\frac{2}{3}$ bukan "angka 2 dan angka 3 yang ditulis bertumpuk". Ia adalah perintah: potong ruas dari 0 sampai 1 menjadi 3 bagian yang sama panjang, lalu melangkahlah 2 bagian dari 0. Penyebut memberi tahu banyaknya potongan, pembilang memberi tahu banyaknya langkah. Kalau potongannya tidak sama besar, perintah itu tidak bisa dijalankan, dan letak pecahannya pun tidak bisa dipercaya.

Kesepakatan ini mengubah pertanyaan di papan tulis: bukan lagi "di mana kira-kira $\frac{2}{3}$?", melainkan "ruas 0 sampai 1 ini dibagi berapa, dan kita melangkah berapa?". Begitu siswa menjawab "dibagi 3, melangkah 2", titiknya harus jatuh tepat pada ujung langkah kedua. Dan di sinilah TikZ menolong saya, karena TikZ tidak mengenal kata kira-kira: ruas yang diminta dibagi tiga, dibaginya persis tiga sama besar.

## Menggambarnya langkah demi langkah di TikZ

Gambar pertama hanya memuat ruas 0 sampai 2, dengan setiap satuan dibagi menjadi tiga. Saya memakai satu trik: satu satuan panjangnya 3 cm, sehingga setiap pertiga tepat 1 cm dan semua tanda jatuh pada bilangan bulat sentimeter.

```latex
\begin{tikzpicture}[x=1cm]
  % Sumbu dari 0 sampai 2 (6 pertiga)
  \draw[thick,-{Stealth}] (-0.3,0) -- (6.6,0);
  % Tanda untuk setiap pertiga, dari 0 sampai 2
  \foreach \i/\lab in {0/0, 1/\frac{1}{3}, 2/\frac{2}{3},
                        3/1, 4/\frac{4}{3}, 5/\frac{5}{3}, 6/2} {
    \draw[thick] (\i,-0.15) -- (\i,0.15);
    \node[below] at (\i,-0.25) {$\lab$};
  }
  % Ruas 0 sampai 2/3 ditebalkan dengan warna emas
  \draw[very thick, color=goldenrod] (0,0) -- (2,0);
  % Titik pecahan yang sedang dibahas
  \fill[red] (2,0) circle (0.09);
  \node[above, red] at (2,0.25) {$\frac{2}{3}$};
\end{tikzpicture}
```

Perhatikan tiga hal pada kode itu. Pertama, perulangan `\foreach` memasangkan posisi dan label sekaligus, sehingga tanda dan tulisannya tidak mungkin bergeser satu sama lain. Kedua, ruas dari 0 sampai $\frac{2}{3}$ saya tebalkan dengan warna emas: siswa melihat bukan hanya sebuah titik, melainkan dua langkah yang sudah ditempuh. Ketiga, pecahan yang lebih besar dari 1 tidak perlu takut: $\frac{4}{3}$ dan $\frac{5}{3}$ jatuh dengan sendirinya di antara 1 dan 2, karena langkahnya diteruskan melewati 1.

Ketika gambar ini tampil di kelas, siswa yang tadinya menaruh $\frac{2}{3}$ di tengah langsung berkata, "Oh, ternyata bukan di tengah, Pak, tapi di langkah kedua." Ia tidak merasa disalahkan, karena yang mengoreksinya adalah gambar itu sendiri: tengah ruas 0 sampai 1 adalah $\frac{1}{2}$, bukan $\frac{2}{3}$, dan keduanya kini punya rumah masing-masing.

## Satu ruas, dua pembagi: membandingkan $\frac{2}{3}$ dan $\frac{3}{4}$

Gambar kedua adalah gambar yang paling sering saya pakai ulang, karena ia menjawab pertanyaan berikutnya yang selalu muncul: "Lebih besar mana, $\frac{2}{3}$ atau $\frac{3}{4}$?" Di papan tulis, perbandingan itu hampir selalu berakhir pada hafalan menyamakan penyebut; di garis bilangan, ia bisa dilihat.

Caranya, saya menggambar dua garis sejajar sama panjang, satu untuk pertiga dan satu untuk perempat, keduanya dari 0 sampai 1. Pada garis pertiga, titik $\frac{2}{3}$ jatuh dua pertiga dari 0; pada garis perempat, titik $\frac{3}{4}$ jatuh tiga perempat dari 0. Karena kedua garis sama panjang dan sama-sama berangkat dari 0, titik yang lebih kanan adalah pecahan yang lebih besar. Siswa melihat sendiri $\frac{3}{4}$ terletak sedikit di kanan $\frac{2}{3}$, dan barulah saya menuliskan penguatnya: $\frac{2}{3} = \frac{8}{12}$ sedangkan $\frac{3}{4} = \frac{9}{12}$.

```latex
\begin{tikzpicture}[x=1cm]
  % Garis pertiga (atas) dan garis perempat (bawah), sama panjang 6 cm
  \draw[thick,-{Stealth}] (-0.3,0) -- (6.6,0);
  \draw[thick,-{Stealth}] (-0.3,-1.8) -- (6.6,-1.8);
  \foreach \i/\lab in {0/0, 1/\frac{1}{3}, 2/\frac{2}{3}, 3/1} {
    \draw[thick] (2*\i,-0.15) -- (2*\i,0.15);
    \node[below] at (2*\i,-0.25) {$\lab$};
  }
  \foreach \i/\lab in {0/0, 1/\frac{1}{4}, 2/\frac{1}{2}, 3/\frac{3}{4}, 4/1} {
    \draw[thick] (1.5*\i,-1.95) -- (1.5*\i,-1.65);
    \node[below] at (1.5*\i,-2.05) {$\lab$};
  }
  % Titik yang dibandingkan, dihubungkan garis putus-putus
  \fill[red] (4,0) circle (0.09);
  \fill[blue] (4.5,-1.8) circle (0.09);
  \draw[dashed] (4,0) -- (4.5,-1.8);
\end{tikzpicture}
```

Kunci gambar ini ada pada satu syarat: kedua garis harus sama panjang. Kalau garis perempat lebih pendek daripada garis pertiga, titik $\frac{3}{4}$ bisa jatuh di kiri $\frac{2}{3}$ dan kesimpulan siswa menjadi terbalik, padahal pecahannya tidak berubah. Gambar yang tidak jujur skalanya mengajarkan kesimpulan yang salah, serapi apa pun gambar itu.

## Tiga kesalahan yang langsung kelihatan di gambar

Sejak memakai gambar ini, tiga kesalahan siswa mudah dikenali, karena semuanya tampak sebagai gambar yang janggal, bukan sekadar jawaban yang salah. Pertama, membagi ruas tidak sama besar: siswa menggambar tiga potong yang satu panjang, satu pendek, satu sedang, lalu heran mengapa titiknya tidak cocok dengan jawaban temannya. Kedua, menghitung tanda, bukan langkah: siswa menghitung tanda 0 sebagai langkah pertama, sehingga $\frac{2}{3}$ jatuh pada tanda $\frac{1}{3}$. Ketiga, menahan pecahan lebih besar dari 1 di dalam ruas 0 sampai 1: $\frac{4}{3}$ ditulis di antara 0 dan 1 karena "kan pecahan itu kecil", padahal ia sudah melewati 1.

Ketiga kesalahan itu dulu saya koreksi dengan kata-kata, dan kata-kata mudah hilang begitu bel berbunyi. Sekarang saya mengoreksinya dengan gambar, dan gambar itu tinggal di buku siswa: ketika mengerjakan soal berikutnya, mereka mengingat garis yang ruasnya dibagi tiga, lalu melangkah dua.

## Penutup: gambar yang bisa diperiksa

Pada akhirnya, garis bilangan pecahan ini bukan gambar yang paling indah di lembar kerja saya: hanya garis lurus, beberapa tanda, dan dua titik berwarna. Tetapi ia punya satu sifat yang tidak dimiliki gambar kira-kira: ia bisa diperiksa. Siswa lain bisa menghitung potongannya dan memutuskan sendiri apakah titik itu benar di tempatnya.

Dan di situlah letak gunanya TikZ di kelas matematika bagi saya: bukan membuat lembar kerja yang terlihat canggih, melainkan gambar yang jujur — setiap tanda punya alasan, setiap jarak punya ukuran, dan setiap pecahan punya rumah yang bisa ditunjuk. Kalau siswa sudah bisa menunjuk rumah $\frac{2}{3}$ tanpa menebak, ia tidak hanya hafal pecahan; ia sudah mengerti apa itu pecahan.

> 📎 **Berkas TikZ lengkap:** [garis-bilangan-pecahan.tex](tex/garis-bilangan-pecahan.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
