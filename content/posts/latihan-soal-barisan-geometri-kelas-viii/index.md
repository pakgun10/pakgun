---
weight: 1
title: "Dari 2 ke 6 ke 18: Latihan Soal Barisan Geometri untuk Kelas VIII"
date: 2026-11-27T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lembar latihan barisan geometri untuk kelas VIII: empat soal suku ke-n, rasio, dan jumlah suku dengan pembahasan langkah demi langkah, plus dua latihan mandiri beserta kuncinya."
featuredImage: "featured-image.png"

tags: ["Barisan Geometri", "Pola Bilangan", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Minggu lalu kelas VIII saya sudah nyaman dengan barisan aritmetika. Mereka hafal polanya: setiap langkah menambah bilangan yang sama. Lalu pada pertemuan berikutnya saya menulis empat bilangan di papan tulis: $2, 6, 18, 54, \dots$ Saya bertanya, berapa suku berikutnya? Separuh kelas menjawab 72, karena mereka menambahkan 18 seperti biasa. Sebagian lagi menjawab 90, karena selisihnya dianggap bertambah 36. Hanya tiga anak yang berkata 162, dan ketika saya tanya alasannya, jawabannya sederhana: "Setiap bilangan dikali tiga, Pak."

Di situlah letak perbedaan barisan geometri dan aritmetika. Kalau aritmetika berjalan dengan menambah, geometri berjalan dengan mengalikan. Bilangan pengalinya disebut rasio, dan selama satu pertemuan penuh saya melihat sendiri betapa kebiasaan lama — selalu mencari selisih — menjadi penghalang terbesar anak-anak memahami materi ini. Lembar latihan di bawah ini saya susun untuk melatih kebiasaan baru itu: empat soal dengan pembahasan, lalu dua latihan mandiri.

<!--more-->

## Dua rumus yang harus benar-benar dipahami

Sebelum mengerjakan soal, saya selalu menulis dua rumus ini di papan tulis dan meminta anak membacanya dengan kata-kata mereka sendiri. Rumus suku ke-$n$ adalah $U_n = a \cdot r^{n-1}$, dengan $a$ suku pertama dan $r$ rasio, yaitu hasil bagi dua suku yang berurutan. Rumus jumlah $n$ suku pertama adalah $S_n = \frac{a(r^n - 1)}{r - 1}$, untuk $r \neq 1$.

Kalimat yang saya ulang setiap kali adalah: rasio itu pembagian, bukan pengurangan, dan $(n-1)$ itu banyaknya perkalian dari suku pertama ke suku yang dicari. Kalau anak paham bahwa suku ke-8 berarti 7 kali perkalian dari suku pertama, sebagian besar kesalahan sudah hilang sebelum terjadi.

## Soal 1: suku ke-8 dari barisan yang sudah jelas

Tentukan suku ke-8 dari barisan $3, 6, 12, 24, \dots$

Soal ini adalah pemanasan, dan saya memakainya untuk memeriksa apakah anak membaca barisan dengan cara yang baru. Suku pertama $a = 3$, dan rasionya $r = \frac{6}{3} = 2$. Suku ke-8 berarti kita mengalikan 7 kali dari suku pertama, masing-masing perkalian sebesar 2.

$$U_8 = 3 \times 2^{7} = 3 \times 128 = 384$$

Jawaban yang paling sering muncul di sini bukan 384, melainkan 768, dari anak yang memakai $2^8$ tanpa mengurangi satu. Begitu saya tanyakan "suku pertama itu perkalian ke berapa?", biasanya mereka langsung menemukan sendiri letak salahnya.

## Soal 2: suku pertama dan rasio yang disembunyikan

Diketahui suku ke-3 suatu barisan geometri adalah 12 dan suku ke-6 adalah 96. Tentukan suku ke-10 barisan itu.

Soal ini sengaja tidak memberi suku pertama maupun rasio, karena di sinilah pemahaman diuji. Dari suku ke-3 ke suku ke-6 ada 3 kali perkalian, dan selama 3 kali perkalian itu nilainya naik dari 12 menjadi 96. Maka $r^3 = \frac{96}{12} = 8$, sehingga $r = 2$.

Setelah rasio diketahui, kita mundur 2 kali perkalian dari suku ke-3 untuk menemukan suku pertama: $a = \frac{12}{2^2} = \frac{12}{4} = 3$. Barisannya ternyata $3, 6, 12, 24, 48, 96, \dots$, dan suku ke-3 memang 12 serta suku ke-6 memang 96, jadi langkah kita sudah terkonfirmasi. Suku ke-10 adalah $U_{10} = 3 \times 2^9 = 3 \times 512 = 1536$.

Saya selalu meminta anak memeriksa kembali: masukkan jawaban ke dalam soal dan lihat apakah cocok. Suku pertama 3 dan rasio 2 memang menghasilkan suku ke-3 sama dengan 12.

## Soal 3: bakteri yang membelah diri

Sejumlah bakteri membelah diri menjadi dua setiap 20 menit. Pada awal pengamatan terdapat 4 bakteri. Berapa banyak bakteri setelah 2 jam?

Soal cerita seperti ini adalah yang paling sering membuat anak berhenti sebelum menghitung, karena mereka harus menerjemahkan cerita menjadi barisan dulu. "Membelah menjadi dua" berarti rasionya $r = 2$, dan banyaknya bakteri mula-mula $a = 4$. Dalam 2 jam ada 6 kali pembelahan, karena $\frac{120}{20} = 6$, jadi yang ditanyakan adalah suku ke-7: suku pertama ditambah 6 kali perkalian.

$$U_7 = 4 \times 2^6 = 4 \times 64 = 256$$

Yang saya tekankan di sini adalah urutan kerjanya: terjemahkan dulu, hitung kemudian. Anak yang langsung mengalikan 4 dengan 6 tanpa menulis $a$ dan $r$ hampir selalu salah, sedangkan anak yang menulis $a = 4$ dan $r = 2$ di kertasnya jarang sekali tersesat.

## Soal 4: rasio pecahan yang membuat barisan mengecil

Tentukan suku ke-7 dan jumlah 6 suku pertama dari barisan $81, 27, 9, 3, \dots$

Soal ini sengaja saya letakkan terakhir, karena rasionya pecahan: $r = \frac{27}{81} = \frac{1}{3}$. Banyak anak menganggap rasio pecahan itu jawaban yang salah, padahal barisan yang mengecil justru wajar bila dikali bilangan yang lebih kecil dari satu. Suku ke-7 adalah $U_7 = 81 \times \left(\frac{1}{3}\right)^6 = 81 \times \frac{1}{729} = \frac{1}{9}$.

Jumlah 6 suku pertama memakai rumus jumlah: $S_6 = \frac{81\left(\left(\frac{1}{3}\right)^6 - 1\right)}{\frac{1}{3} - 1} = \frac{364}{3} = 121\frac{1}{3}$. Satu anak menjumlahkan langsung di papan tulis, $81 + 27 + 9 + 3 + 1 + \frac{1}{3}$, dan hasilnya sama: $121\frac{1}{3}$. Kelas melihat sendiri bahwa rumus jumlah itu jalan pintas yang terbukti sama hasilnya.

## Tiga jebakan yang paling sering muncul

Pertama, rasio dikira selisih. Anak yang terbiasa dengan barisan aritmetika melihat $2, 6, 18$ lalu menghitung $6 - 2 = 4$ dan mengira itulah polanya. Saya selalu meminta mereka memeriksa dua langkah sekaligus: kalau polanya tambah 4, suku ketiganya harus 10, bukan 18.

Kedua, pangkat yang dipakai $n$, bukan $n-1$. Ini kesalahan yang sama seperti di barisan aritmetika, hanya pindah ke perkalian. Suku pertama sudah ada tanpa perkalian apa pun, jadi suku ke-$n$ hanya mengalami $n-1$ kali perkalian.

Ketiga, rasio pecahan dianggap mustahil. Begitu hasil bagi dua suku berurutan menghasilkan pecahan, banyak anak mengulang hitungannya karena mengira mereka salah. Padahal $\frac{1}{3}$ adalah rasio yang sah, dan barisan yang mengecil adalah hal yang biasa — seperti harga barang yang didiskon berulang kali.

## Latihan mandiri

Kerjakan dua soal berikut di buku latihan, lalu cocokkan dengan kunci di bawah.

1. Tentukan suku ke-7 dari barisan $2, 10, 50, 250, \dots$
2. Selembar kertas setebal $0{,}1$ mm dilipat sehingga ketebalannya menjadi dua kali lipat setiap lipatan. Berapa tebal kertas itu setelah 10 kali lipatan? Nyatakan dalam cm.

**Kunci jawaban:** 1) $U_7 = 2 \times 5^6 = 31.250$; 2) $0{,}1 \times 2^{10} = 102{,}4$ mm $= 10{,}24$ cm.

## Penutup

Barisan geometri mengajarkan satu kebiasaan yang berguna jauh di luar matematika: sebelum menghitung, pastikan dulu operasi apa yang sedang bekerja — menambah atau mengalikan. Empat soal di atas sengaja saya susun dari yang paling mudah ditebak sampai yang rasionya pecahan, supaya anak merasakan sendiri bahwa rumusnya tidak pernah berubah. Kalau kebiasaan membaca dulu itu sudah terbentuk, soal barisan apa pun tinggal soal menghitung.
