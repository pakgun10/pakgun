---
weight: 1
title: "Mengapa 1 + 2 + 3 + … + n Sama dengan n(n + 1)/2? Pendalaman dari Cerita Gauss Kecil"
date: 2026-11-14T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman rumus jumlah bilangan asli 1 + 2 + … + n untuk murid yang penasaran: dari cerita Gauss kecil yang menjumlah 1 sampai 100 dalam sekejap, menuju rumus n(n + 1)/2 lewat pasangan ujung."
featuredImage: "featured-image.png"

tags: ["Pola Bilangan", "Pendalaman", "Barisan", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Ada cerita lama yang saya ceritakan hampir setiap tahun di kelas VIII, sebelum kami masuk ke pola bilangan. Konon, ketika Carl Friedrich Gauss masih anak sekolah dasar, gurunya memberi tugas yang dimaksudkan supaya kelas diam lama: jumlahkan semua bilangan dari $1$ sampai $100$. Anak-anak lain mulai menulis deretan panjang di papan tulis kecil mereka. Gauss selesai dalam waktu kurang dari satu menit, dan jawabannya benar: $5050$. Guru itu tidak memberi tugas yang terlalu mudah — ia hanya tidak tahu bahwa anak di hadapannya melihat sesuatu yang anak lain belum lihat. Cerita ini mungkin sudah dibumbui dari mulut ke mulut, tetapi trik di baliknya nyata dan bisa dipakai siapa pun. Hari ini saya ingin membongkar trik itu sampai ke akarnya.

<!--more-->

## Triknya: pasangkan ujung dengan ujung

Coba tulis deretan $1$ sampai $10$, lalu pasangkan bilangan pertama dengan bilangan terakhir, kedua dengan kedua dari belakang, dan seterusnya:

$$1 + 10 = 11, \quad 2 + 9 = 11, \quad 3 + 8 = 11, \quad 4 + 7 = 11, \quad 5 + 6 = 11$$

Lima pasangan, masing-masing berjumlah $11$. Maka jumlah seluruhnya adalah $5 \times 11 = 55$. Tidak ada yang dijumlah satu per satu.

Sekarang terapkan pada $1$ sampai $100$. Pasangan pertama $1 + 100 = 101$, pasangan kedua $2 + 99 = 101$, pasangan ketiga $3 + 98 = 101$. Setiap pasangan selalu $101$, karena setiap kali bilangan kiri naik satu, bilangan kanan turun satu. Ada berapa pasangan? Seratus bilangan dibagi dua, jadi $50$ pasangan. Maka jumlahnya:

$$50 \times 101 = 5050$$

Itulah jawaban Gauss. Ia tidak menghitung lebih cepat dari teman-temannya — ia menghitung dengan cara yang berbeda. Ia tidak menjumlah seratus bilangan; ia hanya menghitung satu pasangan lalu mengalikannya.

## Kalau bilangannya ganjil, bagaimana?

Trik pasangan tetap bekerja, hanya ada satu bilangan yang tidak punya pasangan: bilangan yang di tengah. Ambil $1$ sampai $9$. Pasangannya: $1 + 9 = 10$, $2 + 8 = 10$, $3 + 7 = 10$, $4 + 6 = 10$. Tersisa $5$ sendirian di tengah. Jumlahnya $4 \times 10 + 5 = 45$.

Perhatikan bahwa $5$ itu sendiri adalah setengah dari $10$. Jadi rumusnya tetap sama: setengah dari banyak bilangan dikali jumlah pasangan. Untuk $1$ sampai $9$, setengah dari $9$ adalah $4{,}5$, dan $4{,}5 \times 10 = 45$. Bilangan di tengah itu bukan pengecualian — ia adalah setengah pasangan.

## Dari trik menjadi rumus

Sekarang tulis rumusnya secara umum. Misalkan $S_n$ adalah jumlah bilangan dari $1$ sampai $n$:

$$S_n = 1 + 2 + 3 + \cdots + n$$

Tulis penjumlahan itu dua kali, sekali dari depan dan sekali dari belakang, lalu jumlahkan tegak lurus:

$$\begin{aligned}
S_n &= 1 + 2 + 3 + \cdots + n \\
S_n &= n + (n-1) + (n-2) + \cdots + 1
\end{aligned}$$

Setiap kolom berjumlah $n + 1$: kolom pertama $1 + n$, kolom kedua $2 + (n-1) = n + 1$, dan begitu seterusnya sampai kolom terakhir $n + 1$. Ada $n$ kolom, jadi dua kali $S_n$ sama dengan $n(n + 1)$:

$$2S_n = n(n + 1) \quad\Longrightarrow\quad S_n = \frac{n(n + 1)}{2}$$

Inilah rumus yang dicari. Coba pakai untuk beberapa nilai: $n = 10$ memberi $\frac{10 \times 11}{2} = 55$, sama seperti hitungan pasangan tadi. Untuk $n = 20$, $\frac{20 \times 21}{2} = 210$. Untuk $n = 1000$, $\frac{1000 \times 1001}{2} = 500.500$ — setengah juta dari menjumlah seribu bilangan, tanpa menulis satu pun deretan panjang.

## Bonus: jumlah bilangan ganjil ternyata kuadrat sempurna

Selagi kami bermain dengan pasangan, ada pola kedua yang selalu membuat kelas terkejut. Jumlahkan bilangan ganjil dari awal:

$$1 = 1, \quad 1 + 3 = 4, \quad 1 + 3 + 5 = 9, \quad 1 + 3 + 5 + 7 = 16$$

Hasilnya $1$, $4$, $9$, $16$ — kuadrat sempurna $1^2$, $2^2$, $3^2$, $4^2$. Jumlah $n$ bilangan ganjil pertama selalu $n^2$. Sepuluh bilangan ganjil pertama, $1 + 3 + \cdots + 19$, jumlahnya $10^2 = 100$. Mengapa? Gambarlah titik-titik membentuk persegi: satu titik, lalu tambahkan tiga titik membentuk persegi $2 \times 2$, lalu lima titik membentuk persegi $3 \times 3$. Setiap lapis baru berbentuk huruf L dan menambah tepat satu bilangan ganjil. Jadi bilangan ganjil adalah cara lain untuk membangun persegi — dan itulah mengapa jumlahnya selalu kuadrat.

## Dua jebakan yang sering saya lihat

Pertama, lupa membagi dua. Rumusnya $n(n+1)$ saja tanpa dibagi dua adalah kesalahan paling sering. Saya selalu mengingatkan: kita menjumlah penjumlahan itu dua kali — sekali maju, sekali mundur — jadi hasilnya harus dibagi dua. Kalau jawabannya tampak terlalu besar, periksa dulu: sudah dibagi dua atau belum?

Kedua, memakai rumus untuk barisan yang tidak mulai dari $1$. Rumus $\frac{n(n+1)}{2}$ hanya berlaku bila deretnya mulai dari $1$ dan naik satu demi satu. Kalau soalnya meminta jumlah $5 + 6 + 7 + \cdots + 20$, jangan langsung memasukkan $n = 20$. Hitung dulu jumlah $1$ sampai $20$, yaitu $\frac{20 \times 21}{2} = 210$, lalu kurangi jumlah $1$ sampai $4$, yaitu $\frac{4 \times 5}{2} = 10$. Jawabannya $210 - 10 = 200$. Rumus yang sama, dipakai dua kali, dengan potongan di depan.

## Penutup: yang ditemukan sendiri lebih lama tinggalnya

Senin depan saya akan menulis di papan tulis: "Jumlahkan $1$ sampai $40$ — siapa yang selesai duluan?" Saya sudah tahu sebagian murid akan mulai menulis $1 + 2 + 3 + \cdots$ dengan tekun, dan sebagian akan tersenyum karena ingat cerita Gauss. Jawabannya $\frac{40 \times 41}{2} = 820$, tetapi jawaban itu bukan intinya. Intinya adalah momen ketika seorang murid berhenti menghitung satu per satu dan mulai melihat pasangan. Matematika, bagi saya, sering kali bukan soal menghitung lebih cepat — melainkan soal melihat pola yang membuat hitungan panjang menjadi tidak perlu. Dan pola itu, begitu terlihat sekali, sulit untuk tidak terlihat lagi.
