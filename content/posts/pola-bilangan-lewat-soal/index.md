---
weight: 1
title: "Belajar Pola Bilangan Lewat Soal: Bahan Ajar dan Latihan untuk Kelas VIII"
date: 2026-10-23T04:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Bahan ajar singkat pola bilangan untuk kelas VIII lengkap dengan empat contoh soal berjenjang beserta pembahasannya — dari pola ganjil hingga menentukan rumus suku ke-n."
featuredImage: "featured-image.png"

tags: ["Pola Bilangan", "Latihan Soal", "Bahan Ajar"]
categories: ["Bahan Ajar"]

math:
  enable: true
---

Di kelas VIII saya, ada momen yang selalu saya tunggu: ketika anak-anak mulai menebak pola angka di papan. "5, 9, 13, 17... selanjutnya 21, Pak!" Betul. Tetapi ketika saya tanya, "kenapa 21?" — jawabannya sering hanya, "kan kelihatan, Pak." Nah, di situlah masalahnya. Menebak itu mudah, tetapi matematika menuntut alasan: pola apa yang dipakai, dan apakah alasan itu juga berlaku untuk suku ke-100?

<!--more-->

## Jangan mulai dari rumus

Kesalahan yang pernah saya lakukan: langsung mengenalkan rumus $U_n = a + (n-1)b$. Anak-anak bisa menghafal, tetapi begitu soalnya sedikit diputar — misalnya polanya menurun, atau bedanya berubah — mereka tenggelam. Sekarang saya selalu mulai dari mengamati: tulis tiga-empat suku pertama, hitung selisihnya, dan tanya, "apa yang berubah setiap langkah?"

Empat contoh berikut saya pakai berurutan di kelas. Setiap soal saya bacakan dulu, saya beri waktu anak mencoba sendiri, baru saya bahas. Pembahasannya sengaja saya tulis langkah demi langkah — bukan supaya anak mencontek, melainkan supaya mereka punya contoh cara menuliskan alasan yang rapi.

## Contoh 1 — Pola paling bersahabat

> Tentukan tiga suku berikutnya dari barisan $2, 6, 12, 20, \dots$

**Pembahasan.** Saya suruh anak menghitung selisih antarsuku yang berurutan:
$$6-2=4,\quad 12-6=6,\quad 20-12=8$$
Selisihnya bertambah 2 setiap langkah: $4, 6, 8, \dots$ Maka selisih berikutnya adalah $10, 12, 14$, sehingga:
$$20+10=30,\quad 30+12=42,\quad 42+14=56$$
Tiga suku berikutnya: **30, 42, 56**. Saya suka membuka dengan soal ini karena ia mengajarkan pelajaran penting: selisihnya pun punya pola.

## Contoh 2 — Ketika pola dibungkus cerita

> Harga sebuah kue bertingkat: tingkat pertama Rp5.000. Setiap tingkat berikutnya harganya bertambah Rp2.000 dari tingkat sebelumnya. Berapa harga kue lima tingkat?

**Pembahasan.** Ini hanya barisan bilangan yang dibungkus cerita: $5000, 7000, 9000, 11000, 13000$. Anak yang langsung melihat polanya menjawab tanpa ragu. Yang menarik justru kebalikannya: saya membalik pertanyaan — "kalau harga kue lima tingkat itu Rp65.000, berapa harga tingkat pertamanya?" — dan kelas mendadak sunyi. Cerita yang sama, arah yang berbeda, sudah cukup membuat mereka berpikir ulang. Pola tetap memandu: misalkan tingkat pertama $a$, maka:
$$a + (a+2000) + (a+4000) + (a+6000) + (a+8000) = 65000$$
$$5a + 20000 = 65000$$
$$a = 9000$$
Harga tingkat pertama **Rp9.000**.

## Contoh 3 — Pola konfigurasi: titik segitiga

> Perhatikan susunan titik berikut: suku pertama 1 titik, suku kedua 3 titik, suku ketiga 6 titik, suku keempat 10 titik. Berapa banyak titik pada suku kedelapan?

**Pembahasan.** Saya menggambar susunan segitiga di papan: baris pertama 1 titik, baris kedua 2 titik, dan seterusnya. Jumlah titik pada suku ke-$n$ adalah $1+2+3+\dots+n$. Ini momen terbaik untuk mengenalkan rumus jumlah $n$ bilangan asli pertama:
$$S_n = \frac{n(n+1)}{2}$$
Untuk suku kedelapan:
$$S_8 = \frac{8 \times 9}{2} = 36$$
Jadi ada **36 titik** pada suku kedelapan. Anak-anak biasanya kagum ketika tahu deretan sederhana ini punya rumus singkat — rumus yang "ditemukan" dari pola, bukan dihafal mentah-mentah.

## Contoh 4 — Menentukan suku ke-n

> Sebuah pola lantai berbentuk susunan ubin: lantai pertama memakai 5 ubin, dan setiap lantai berikutnya memakai 4 ubin lebih banyak dari lantai sebelumnya. Berapa banyak ubin pada lantai ke-20?

**Pembahasan.** Barisannya $5, 9, 13, 17, \dots$ dengan beda tetap $b = 4$. Suku ke-$n$:
$$U_n = 5 + (n-1) \times 4$$
Untuk lantai ke-20:
$$U_{20} = 5 + 19 \times 4 = 5 + 76 = 81$$
Jadi diperlukan **81 ubin** pada lantai ke-20. Barulah di akhir saya perkenalkan bentuk umumnya, $U_n = a + (n-1)b$ — rumus yang kini terasa seperti ringkasan dari empat soal yang sudah mereka kerjakan, bukan mantra asing.

## Penutup

Empat soal ini memakan waktu sekitar 40 menit di kelas saya. Ada tiga kebiasaan kecil yang membuat pelajaran ini bekerja: pertama, minta anak selalu menuliskan selisih atau aturan pola sebelum menjawab; kedua, mulai dari cerita sebelum rumus; ketiga, tunjukkan bahwa rumus adalah hasil peringkasan dari pola yang mereka temukan sendiri.

Pola bilangan adalah materi yang murah — tidak butuh alat peraga mahal — tetapi mahal maknanya: di sinilah anak belajar bahwa matematika bukan tentang menebak, melainkan tentang beralasan. Kalau empat contoh ini terasa membantu, silakan pakai di kelas Bapak/Ibu. Dan kalau ada variasi soal yang lebih dekat dengan keseharian murid, saya justru ingin mendengarnya.
