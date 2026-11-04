---
title: "Segitiga Pascal yang Tumbuh dari Angka Satu: Menggambar Pola Penjumlahan dengan TikZ"
date: 2026-11-03T19:40:00+07:00
draft: false
authors: ["Gunanto"]
description: "Mengajarkan koefisien binomial lewat Segitiga Pascal yang digambar jujur dengan TikZ — setiap angka benar-benar hasil penjumlahan dua angka di atasnya."
featuredImage: "featured-image.png"
tags: ["TikZ", "pola bilangan", "binomial"]
categories: ["Matematika"]
math:
  enable: true
---

Di kelas VIII, topik pola bilangan biasanya saya tutup dengan satu pertanyaan yang suka membuat kelas hening: "Kalau saya tuliskan angka satu di puncak, terus di bawahnya dua angka satu lagi, dan seterusnya — angka di dalam segitiga ini berasal dari mana?" Ada yang menjawab "pola, Bu", ada yang bilang "dikalikan dua", dan ada yang sengaja diam karena tidak yakin. Diamnya itu justru kesempatan. Karena segitiga Pascal memang bukan soal menghafal baris berikutnya, tapi soal melihat bahwa setiap angka adalah **hasil penjumlahan dua angka tepat di atasnya**.

<!--more-->

Masalahnya, gambar segitiga Pascal di papan tulis itu melelahkan. Barisnya makin panjang, angkanya makin besar, dan kalau saya salah menambah satu angka di baris kelima, siswa akan menemukannya — biasanya tepat saat saya sedang paling percaya diri. Pernah sekali saya menulis 15 di posisi yang seharusnya 10, dan satu anak dengan sopan berkata, "Bu, sepuluh plus lima itu lima belas, tapi yang di atasnya sepuluh dan lima posisinya geser." Dia benar, dan saya belajar: gambar soal semacam ini harus jujur secara aritmetika, bukan sekadar rapi.

Karena itu untuk bahan ajar dan lembar latihan, saya sekarang menggambar segitiga Pascal dengan TikZ. Selain bisa dipakai ulang, cara menggambarnya memaksa saya memikirkan struktur: baris ke-$n$ punya $n+1$ angka, dan setiap angka memang menempel di antara dua angka baris di atasnya.

## Struktur yang Sederhana Tapi Konsisten

Prinsipnya begini: baris ke-$n$ berisi koefisien binomial $\binom{n}{k}$ untuk $k = 0, 1, \dots, n$. Susunannya seperti ini:

$$\begin{array}{ccccccc}
 & & & 1 & & & \\
 & & 1 & & 1 & & \\
 & 1 & & 2 & & 1 & \\
 1 & & 3 & & 3 & & 1 \\
\end{array}$$

Dan aturannya hanya satu: angka = jumlah dua angka terdekat di baris atas. $2 = 1+1$, $3 = 1+2$, $6 = 3+3$. Dari aturan kecil ini lahirlah barisan yang muncul di mana-mana: jumlah baris ke-$n$ selalu $2^n$, dan barisnya sendiri adalah koefisien dari $(a+b)^n$:

$$(a+b)^4 = 1a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + 1b^4$$

Kalau siswa sudah menghitung baris keempat dengan penjumlahan, koefisien $1, 4, 6, 4, 1$ itu bukan hafalan lagi — mereka yang menambahkannya baris demi baris.

## Kode TikZ-nya

Bagian yang saya suka: dengan satu perulangan, semua posisi angka dihitung dari koordinat, bukan diketik manual.

```latex
\begin{tikzpicture}[
  angka/.style={font=\small, text=white},
  skala=1.1cm]
  \def\N{5}
  \foreach \n in {0,...,\N} {
    \foreach \k in {0,...,\n} {
      % hitung C(n,k) dengan rumus rekursif di LuaTeX, atau tulis manual:
      \node[angka] at ({(\k-\n/2)*\skala}, {-\n*0.9}) {\pasc{\n}{\k}};
    }
  }
\end{tikzpicture}
```

Untuk pekerjaan harian saya lebih memilih versi yang angkanya dituliskan eksplisit, karena bisa disunting per-baris dan tetap aman dikompilasi di mesin apa pun:

```latex
\begin{tikzpicture}[xscale=1.4, yscale=0.9]
  \node (a00) at (0,0)  {$1$};
  \node (a10) at (-1,-1) {$1$}; \node (a11) at (1,-1) {$1$};
  \node (a20) at (-2,-2) {$1$}; \node (a21) at (0,-2) {$2$};
  \node (a22) at (2,-2)  {$1$};
  \node (a30) at (-3,-3) {$1$}; \node (a31) at (-1,-3) {$3$};
  \node (a32) at (1,-3)  {$3$}; \node (a33) at (3,-3)  {$1$};
  % garis bantu: setiap angka "ditopang" dua angka di atasnya
  \draw[gray!50] (a00) -- (a10); \draw[gray!50] (a00) -- (a11);
  \draw[gray!50] (a10) -- (a20); \draw[gray!50] (a10) -- (a21);
  \draw[gray!50] (a11) -- (a21); \draw[gray!50] (a11) -- (a22);
\end{tikzpicture}
```

Garis bantu abu-abu itu detail kecil yang menurut saya penting. Tanpa garis, segitiga Pascal di lembar soal hanya tumpukan angka. Dengan garis, siswa melihat "siapa menopang siapa" — dan ketika saya minta mereka melanjutkan baris berikutnya, mereka melakukannya dengan menelusuri garis, bukan menebak.

> 📎 **Berkas TikZ lengkap:** [tikz-segitiga-pascal.tex](tex/tikz-segitiga-pascal.tex) — siap kompilasi (butuh paket `tikz`).

## Ada Apa Saja di Dalamnya

Kelas paling seru biasanya saat kita "membongkar" segitiga yang sudah jadi. Beberapa hal yang selalu ditemukan siswa sendiri:

1. **Bilangan segitiga** ($1, 3, 6, 10, \dots$) berjajar miring di salah satu sisi — dan itu persis baris yang kita bahas waktu pola bilangan.
2. **Baris ganjil-genap**: kalau angka diganti titik, baris tertentu punya semua titik pada posisi ganjil.
3. **Jumlah tiap baris** selalu pangkat dua: $1, 2, 4, 8, 16, \dots$
4. **Pola Fibonacci** muncul kalau angka dijumlah serong.

Yang ketiga favorit saya untuk diskusi penutup. Saya tanya, "Kenapa jumlah barisnya selalu dua pangkat $n$?" Kadang ada yang bisa menjelaskan dengan bahasanya sendiri: karena setiap angka di baris atas "diwariskan" ke dua anak di bawahnya, jadi tiap baris jumlahnya jadi dua kali baris sebelumnya. Penjelasan seperti itu tidak bisa lahir dari menghafal rumus — dia lahir dari melihat gambar yang jujur.

Yang tidak kalah penting: segitiga ini murah secara pikiran tapi kaya secara pertanyaan. Saya pernah memberi lembar berisi segitiga sampai baris kedelapan, kosong pada beberapa angka yang saya hilangkan sengaja, dan tugasnya cuma satu — "lengkapi yang hilang, dan katakan kenapa kamu yakin." Tidak ada satu pun siswa yang bertanya rumusnya apa. Mereka langsung bekerja dengan penjumlahan, dan justru dari situ muncul pertanyaan-pertanyaan yang lebih dalam: apakah pola ini berhenti? Apakah ada angka yang muncul dua kali? Pertanyaan seperti itu tidak muncul kalau yang saya berikan adalah daftar rumus.

## Menutup Refleksi

Kalau dipikir-pikir, segitiga Pascal ini contoh bagus kenapa saya peduli pada kualitas gambar bahan ajar. Gambar yang salah — satu angka tidak sesuai penjumlahan, satu jarak tidak konsisten — tidak hanya jelek, dia mengajarkan sesuatu yang keliru secara diam-diam. Siswa percaya gambar lebih cepat daripada percaya kata-kata guru.

Dengan TikZ, ketika saya mengubah satu angka di baris mana pun, sisanya tetap berdiri di koordinat yang benar, dan garis penopangnya tetap menghubungkan yang seharusnya. Gambar itu tidak berbohong. Dan di kelas yang penuh dengan siswa yang cepat curiga pada matematika, gambar yang tidak berbohong adalah aset yang tidak ternilai.
