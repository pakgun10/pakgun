---
weight: 1
title: "Dari 180° ke (n − 2) × 180°: Pendalaman Jumlah Sudut Segi Banyak"
date: 2026-11-14T16:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman jumlah sudut segi banyak untuk murid yang penasaran: dari segitiga 180° menuju rumus (n − 2) × 180° lewat satu trik sederhana — memotong segi banyak menjadi segitiga-segitiga."
featuredImage: "featured-image.png"

tags: ["Segi Banyak", "Pendalaman", "Geometri", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Pagi tadi di kelas VIII kami membuktikan jumlah sudut segitiga selalu $180^\circ$ dengan lipatan kertas. Sebelum bel berbunyi, Dimas mengangkat tangan. "Pak, kalau segitiga $180^\circ$, segi empat berapa? Segi lima berapa? Segi seratus berapa?" Kelas tertawa, tetapi pertanyaan itu bagus sekali — dan jawabannya ternyata hanya butuh satu trik: potong segi banyak menjadi segitiga-segitiga, lalu hitung berapa segitiga yang terbentuk.

<!--more-->

## Segi empat: dua segitiga dalam satu bangun

Gambar sebuah segi empat sembarang di papan tulis. Sekarang tarik satu diagonal, garis dari satu titik sudut ke titik sudut yang berseberangan dengannya. Segi empat itu terbelah menjadi dua segitiga, dan jumlah sudut kedua segitiga itu persis sama dengan jumlah sudut segi empatnya.

Karena satu segitiga jumlah sudutnya $180^\circ$, maka segi empat jumlah sudutnya:

$$2 \times 180^\circ = 360^\circ$$

Cocok dengan yang sudah kita kenal: persegi panjang punya empat sudut siku-siku, dan $4 \times 90^\circ = 360^\circ$. Tidak ada yang aneh di sini — hanya dua segitiga yang menempel menjadi satu bangun.

## Segi lima: tiga segitiga dari satu titik sudut

Lanjut ke segi lima. Pilih satu titik sudut, lalu tarik diagonal ke dua titik sudut yang tidak bersebelahan dengannya. Berapa segitiga yang terbentuk? Tiga. Maka jumlah sudut segi lima adalah:

$$3 \times 180^\circ = 540^\circ$$

Perhatikan polanya. Segitiga butuh satu segitiga, segi empat butuh dua, segi lima butuh tiga. Banyak segitiga yang terbentuk selalu dua kurang dari banyak sisi. Inilah kuncinya: dari satu titik sudut, kita bisa membagi segi-$n$ menjadi $n - 2$ segitiga.

## Polanya: $(n - 2) \times 180^\circ$

Kalau polanya ditulis dalam tabel, semuanya jadi jelas:

| Banyak sisi ($n$) | Banyak segitiga | Jumlah sudut dalam |
| --- | --- | --- |
| 3 | 1 | $180^\circ$ |
| 4 | 2 | $360^\circ$ |
| 5 | 3 | $540^\circ$ |
| 6 | 4 | $720^\circ$ |
| 7 | 5 | $900^\circ$ |
| 8 | 6 | $1080^\circ$ |

Maka rumus umumnya:

$$\text{Jumlah sudut dalam segi-}n = (n - 2) \times 180^\circ$$

Sekarang pertanyaan Dimas yang paling jauh bisa dijawab. Segi seratus? $(100 - 2) \times 180^\circ = 17.640^\circ$. Tidak perlu menggambar seratus sisi untuk mengetahuinya — polanya yang bekerja.

Ada bonusnya. Kalau segi banyak itu beraturan, semua sudutnya sama besar, sehingga besar satu sudutnya tinggal membagi jumlah total dengan banyak sisi:

$$\text{Satu sudut segi-}n\text{ beraturan} = \frac{(n - 2) \times 180^\circ}{n}$$

Segi lima beraturan: $540^\circ \div 5 = 108^\circ$ per sudut. Segi enam beraturan: $720^\circ \div 6 = 120^\circ$ per sudut. Jadi kalau ada yang menggambar "segi lima beraturan" lalu mengukur sudutnya $90^\circ$, gambarnya pasti belum beraturan — rumus ini bisa dipakai untuk memeriksa.

## Dua jebakan yang sering saya lihat

Pertama, menarik diagonal dari semua titik sudut sekaligus, lalu menjumlahkan semua segitiga yang terlihat. Segitiga yang sama terhitung berkali-kali dan hasilnya membengkak. Kuncinya: pilih satu titik sudut sebagai pangkal, tarik diagonal hanya dari titik itu.

Kedua, mengira rumus ini hanya berlaku untuk segi beraturan. Tidak. Segi empat yang miring, segi lima yang salah satu sisinya panjang sekali — semuanya tunduk pada rumus yang sama, selama bangunnya bisa dipotong menjadi $n - 2$ segitiga. Untuk segi cekung, diagonalnya harus tetap berada di dalam bangun, tetapi jumlah sudutnya tetap $(n - 2) \times 180^\circ$.

## Penutup: rumus yang ditemukan, bukan dihafal

Senin depan saya akan meminta murid menggambar segi tujuh sendiri, menarik diagonal dari satu titik sudut, lalu menghitung jumlah sudutnya sebelum melihat tabel. Mereka akan menemukan $900^\circ$ dengan tangan mereka sendiri. Rumus yang dihafal bisa hilang setelah ulangan selesai; rumus yang ditemukan dari pola biasanya tinggal lebih lama. Dan kalau ada murid yang bertanya tentang segi seratus lagi, saya sudah punya jawabannya: $17.640^\circ$ — tanpa menggambar satu garis pun.
