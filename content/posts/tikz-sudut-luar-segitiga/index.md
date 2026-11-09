---
title: "Satu Sisi Diperpanjang, Satu Sudut Baru: Menggambar Sudut Luar Segitiga dengan TikZ"
date: 2026-11-09T16:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Perpanjang satu sisi segitiga dan lahirlah sudut baru di luarnya: sudut luar sama dengan jumlah dua sudut dalam yang tidak bersisian. Di tulisan ini saya menggambarnya dengan TikZ — segitiga 50, 60, dan 70 derajat, plus perpanjangan putus-putus yang membuat sudut luar 110 derajat langsung terlihat."
featuredImage: "featured-image.png"

tags: ["TikZ", "Garis dan Sudut", "Sudut Luar Segitiga", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Di kelas VIII minggu lalu, saya menggambar segitiga $ABC$ di papan tulis, lalu saya memperpanjang sisi $BC$ melewati titik $C$ sampai ke titik $D$. Satu garis tambahan — dan tiba-tiba ada sudut baru yang lahir di luar segitiga: sudut $ACD$. Saya bertanya, "Berapa besar sudut ini, kalau sudut $A$ 50 derajat dan sudut $B$ 60 derajat?" Seorang murid menjawab 70 derajat, karena ia mengambil sudut $C$ yang ada di sebelahnya. Murid lain menjawab 180 derajat, karena ia menjumlahkan semua sudut yang ia lihat. Jawaban yang benar adalah 110 derajat, dan cara menemukannya tidak memerlukan busur derajat sama sekali. Malam harinya saya menggambar ulang gambar papan tulis itu dengan TikZ, supaya besok pagi murid saya bisa melihat sendiri mengapa 50 tambah 60 sama dengan 110.

<!--more-->

## Satu garis diperpanjang, satu sudut lahir

Sudut luar segitiga adalah sudut yang dibentuk oleh satu sisi segitiga dan perpanjangan sisi lain yang bersisian dengannya. Di gambar saya, sisi $BC$ diperpanjang melewati $C$ ke titik $D$, sehingga sudut $ACD$ adalah sudut luar di titik $C$. Tetangganya, sudut dalam $ACB$, berpelurus dengannya: $70^{\circ} + 110^{\circ} = 180^{\circ}$. Itu sudah menjadi cara pertama menemukan sudut luar: kurangkan sudut dalam yang bersisian dari 180 derajat.

Setiap segitiga sebenarnya punya enam sudut luar, dua di tiap titik, tetapi dua sudut luar di satu titik saling bertolak belakang sehingga besarnya sama. Cukup satu per titik, dan gambar tetap rapi.

## Sudut luar sama dengan jumlah dua sudut dalam yang tidak bersisian

Cara kedua — dan yang jauh lebih berguna — adalah teorema sudut luar: besar sudut luar sama dengan jumlah dua sudut dalam yang **tidak** bersisian dengannya. Di segitiga saya: $50^{\circ} + 60^{\circ} = 110^{\circ}$.

Buktinya hanya dua baris. Pertama, jumlah ketiga sudut dalam segitiga adalah 180 derajat: $\angle A + \angle B + \angle C = 180^{\circ}$. Kedua, sudut luar dan sudut dalam yang bersisian berpelurus, jadi jumlah keduanya juga 180 derajat. Kedua jumlah itu sama dan sama-sama memuat sudut $C$, maka sudut luar harus sama dengan $\angle A + \angle B$. Tidak ada yang perlu dihafal — teoremanya lahir dari dua fakta yang sudah murid kenal.

Supaya bukti itu tidak hanya tinggal di papan, saya menggambar gambar kedua: dua sudut dalam, 50 dan 60 derajat, saya pindahkan dan saya jajarkan pada satu garis lurus. Keduanya menempel persis dan berhenti tepat di 110 derajat.

## Menggambar sudut luar di TikZ

Kunci gambar pertama adalah posisi titik $C$. Saya meletakkan $A$ di $(0,0)$ dan $B$ di $(5,0)$, lalu $C$ saya tulis dengan koordinat polar TikZ: $(50:4{,}61)$ berarti jarak $4{,}61$ cm dari titik asal dengan arah $50^{\circ}$. Dengan begitu sudut di $A$ dijamin 50 derajat, dan sudut $B$ serta $C$ mengikuti: 60 dan 70 derajat.

Titik $D$ saya hitung dari arah sisi $BC$: garis $BC$ berjalan ke arah $120^{\circ}$, jadi $D$ saya letakkan $1{,}5$ cm dari $C$ ke arah itu, yaitu di $(2{,}21; 4{,}83)$. Perpanjangan saya gambar putus-putus supaya mata langsung membedakan sisi segitiga dari garis tambahan, dan busur sudut luar saya gambar lebih besar daripada busur sudut dalam — $1{,}1$ cm berbanding $0{,}8$ cm — supaya keduanya tidak bertumpuk di titik $C$.

```latex
\begin{tikzpicture}[scale=1.0, font=\large]
  % Titik-titik segitiga: C ditulis dengan koordinat polar
  \coordinate (A) at (0, 0);
  \coordinate (B) at (5, 0);
  \coordinate (C) at (50:4.61);
  % Titik D: perpanjangan BC melewati C (arah 120 derajat)
  \coordinate (D) at (2.21, 4.83);

  % Segitiga ABC
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  % Perpanjangan sisi BC, digambar putus-putus
  \draw[thick, dashed] (C) -- (D);

  % Busur sudut dalam: 50, 60, dan 70 derajat
  \draw (A) ++(0:0.8) arc (0:50:0.8);
  \draw (B) ++(120:0.8) arc (120:180:0.8);
  \draw (C) ++(230:0.8) arc (230:300:0.8);
  % Busur sudut luar: 110 derajat (jari-jari lebih besar)
  \draw (C) ++(120:1.1) arc (120:230:1.1);

  % Nama titik
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above] at (C) {$C$};
  \node[above left] at (D) {$D$};

  % Label sudut
  \node at (1.04, 0.49) {$50^{\circ}$};
  \node at (4.00, 0.58) {$60^{\circ}$};
  \node at (2.86, 2.38) {$70^{\circ}$};
  \node at (1.47, 3.66) {$110^{\circ}$};
\end{tikzpicture}
```

Perhatikan dua busur di titik $C$. Busur dalam saya tarik dari arah $230^{\circ}$ ke $300^{\circ}$ — arah sisi $CA$ dan $CB$ bila dilihat dari $C$. Busur luar saya tarik dari arah $120^{\circ}$ (arah $CD$) ke $230^{\circ}$ (arah $CA$). Keduanya bertemu di sisi $CA$: dari situlah murid melihat bahwa sudut dalam dan sudut luar di titik yang sama memang berpelurus.

## Tiga kesalahan yang sering saya lihat

Ketiga kesalahan ini berakar dari satu hal yang sama: murid belum yakin sudut mana yang boleh dijumlahkan.

**Pertama, menjumlahkan sudut yang bersisian.** Murid menulis $50^{\circ} + 70^{\circ} = 120^{\circ}$ karena ia menjumlahkan sudut $A$ dengan sudut $C$ yang ada di sebelah sudut luar. Padahal teorema ini hanya berlaku untuk dua sudut dalam yang *tidak* bersisian dengan sudut luar itu. Cara saya mengatasinya: sebelum menghitung, murid menunjuk dulu sudut luarnya, lalu menutup sudut dalam yang bersisian dengan telapak tangan. Dua sudut yang masih terlihat — itulah yang dijumlahkan.

**Kedua, mengira sudut luar sama dengan sudut dalam di sebelahnya.** Murid menjawab sudut luar di $C$ adalah 70 derajat, sama dengan sudut $ACB$ — biasanya karena gambarnya kurang tegas: perpanjangan digambar tipis dan menyatu dengan sisi segitiga. Begitu perpanjangan digambar putus-putus dan busur luar digambar lebih besar, murid jarang tertukar lagi.

**Ketiga, rumusnya terbalik.** Murid menulis sudut luar $= 180^{\circ} - (\angle A + \angle B)$, padahal itu justru menghasilkan sudut dalam $\angle C$. Yang benar adalah sebaliknya: sudut luar $= \angle A + \angle B$, sedangkan $\angle C = 180^{\circ} - (\angle A + \angle B)$. Saya membiasakan murid mengecek dengan akal sehat: sudut luar harus lebih besar daripada masing-masing sudut dalam yang tidak bersisian dengannya.

## Satu soal untuk dicoba

Segitiga $PQR$ memiliki sudut luar di titik $R$ sebesar $130^{\circ}$, dan sudut dalam di titik $P$ sebesar $75^{\circ}$. Berapa besar sudut dalam di titik $Q$, dan berapa besar sudut dalam di titik $R$?

Sudut di $Q$ tidak bersisian dengan sudut luar di $R$, jadi ia pasangan sudut $P$: $\angle Q = 130^{\circ} - 75^{\circ} = 55^{\circ}$. Sudut dalam di $R$ adalah tetangga yang bersisian dengan sudut luar itu, jadi $\angle R = 180^{\circ} - 130^{\circ} = 50^{\circ}$. Pemeriksaan akhir: $75^{\circ} + 55^{\circ} + 50^{\circ} = 180^{\circ}$ — pas. Satu soal ini melatih dua cara sekaligus.

Sudut luar tampak seperti tambahan kecil di luar segitiga, tetapi ia adalah pintu ke banyak teorema lain: jumlah sudut luar segitiga, sudut luar segibanyak, sampai sudut keliling di lingkaran. Minggu depan, ketika saya menggambar segiempat, saya akan memakai cara yang sama — memperpanjang satu sisi, lalu bertanya sudut apa yang lahir di luarnya.

> 📎 **Berkas TikZ lengkap:** [sudut-luar-segitiga.tex](tex/sudut-luar-segitiga.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
