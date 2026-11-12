---
weight: 1
title: "Dari Suku ke Suku: Latihan Soal Barisan Aritmetika untuk Kelas VIII"
date: 2026-11-13T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lembar latihan barisan aritmetika untuk kelas VIII: empat soal suku ke-n dan jumlah suku dengan pembahasan langkah demi langkah, plus dua latihan mandiri beserta kuncinya."
featuredImage: "featured-image.png"

tags: ["Barisan Aritmetika", "Pola Bilangan", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VIII saya, barisan aritmetika adalah materi yang tampak mudah di papan tulis dan tiba-tiba sulit di kertas ulangan. Anak-anak hafal rumusnya, tetapi begitu soalnya tidak lagi berbunyi "tentukan suku ke-20 dari barisan 3, 7, 11, 15, ...", mereka bingung harus mulai dari mana. Padahal yang berubah hanya bungkusnya, bukan idenya: setiap langkah selalu menambah bilangan yang sama.

Karena itu saya lebih suka melatih barisan aritmetika lewat soal-soal yang memaksa anak membaca dulu sebelum menghitung. Ada soal yang suku pertamanya disembunyikan, ada soal yang bedanya harus dicari dari dua suku yang berjauhan, ada soal cerita yang baris kursinya harus diterjemahkan dulu menjadi barisan. Lembar latihan di bawah ini saya susun dengan pola itu: empat soal dengan pembahasan, lalu dua latihan mandiri.

<!--more-->

## Dua rumus yang harus benar-benar dipahami

Sebelum mengerjakan soal, saya selalu menulis dua rumus ini di papan tulis dan meminta anak membacanya dengan kata-kata mereka sendiri. Rumus suku ke-$n$ adalah $U_n = a + (n-1)b$, dengan $a$ suku pertama dan $b$ beda antar suku. Rumus jumlah $n$ suku pertama adalah $S_n = \frac{n}{2}(2a + (n-1)b)$.

Kalimat yang saya ulang setiap kali adalah: beda itu selisih antara dua suku yang berurutan, dan $(n-1)$ itu banyaknya lompatan dari suku pertama ke suku yang dicari. Kalau anak paham bahwa suku ke-20 berarti 19 lompatan dari suku pertama, sebagian besar kesalahan sudah hilang sebelum terjadi.

## Soal 1: suku ke-20 dari barisan yang sudah jelas

Tentukan suku ke-20 dari barisan $3, 7, 11, 15, \dots$

Soal ini adalah pemanasan, dan saya memakainya untuk memeriksa apakah anak membaca barisan dengan benar. Suku pertama $a = 3$, dan bedanya $b = 7 - 3 = 4$. Suku ke-20 berarti kita melompat 19 kali dari suku pertama, masing-masing lompatan sebesar 4.

$$U_{20} = 3 + (20-1) \times 4 = 3 + 19 \times 4 = 3 + 76 = 79$$

Jawaban yang paling sering muncul di sini bukan 79, melainkan 83, dari anak yang memakai $20 \times 4$ tanpa mengurangi satu. Begitu saya tanyakan "suku pertama itu lompatan ke berapa?", biasanya mereka langsung menemukan sendiri letak salahnya.

## Soal 2: suku pertama yang disembunyikan

Diketahui suku ke-5 suatu barisan aritmetika adalah 23 dan suku ke-9 adalah 39. Tentukan suku ke-15 barisan itu.

Soal ini sengaja tidak memberi suku pertama maupun beda, karena di sinilah pemahaman diuji. Dari suku ke-5 ke suku ke-9 ada 4 lompatan, dan selama 4 lompatan itu nilainya naik dari 23 menjadi 39, selisihnya 16. Maka bedanya adalah $b = \frac{39 - 23}{9 - 5} = \frac{16}{4} = 4$.

Setelah beda diketahui, kita mundur 4 lompatan dari suku ke-5 untuk menemukan suku pertama: $a = 23 - 4 \times 4 = 23 - 16 = 7$. Barisannya ternyata $7, 11, 15, 19, 23, \dots$, dan suku ke-5 memang 23, jadi langkah kita sudah terkonfirmasi. Suku ke-15 adalah $U_{15} = 7 + 14 \times 4 = 7 + 56 = 63$.

Saya selalu meminta anak memeriksa kembali dengan cara ini: masukkan jawaban ke dalam soal dan lihat apakah cocok. Kalau suku pertama 7 dan beda 4 menghasilkan suku ke-5 sama dengan 23, perhitungannya sudah benar.

## Soal 3: menjumlahkan lima belas suku pertama

Tentukan jumlah 15 suku pertama dari barisan $2, 5, 8, 11, \dots$

Di sini anak harus berpindah dari rumus suku ke rumus jumlah, dan kesalahan yang paling sering terjadi adalah menjumlahkan satu per satu sampai suku ke-15. Cara itu memang benar, tetapi memakan waktu dan rawan salah hitung. Dengan $a = 2$ dan $b = 3$, rumus jumlah memberi jalan yang lebih pendek:

$$S_{15} = \frac{15}{2}\bigl(2 \times 2 + 14 \times 3\bigr) = \frac{15}{2} \times (4 + 42) = \frac{15}{2} \times 46 = 15 \times 23 = 345$$

Saya meminta satu anak menjumlahkan dengan cara panjang di papan tulis, satu per satu sampai suku ke-15, dan kami membandingkan hasilnya. Keduanya sampai di 345, dan kelas melihat sendiri bahwa rumus jumlah itu bukan hafalan kosong, melainkan jalan pintas yang terbukti sama hasilnya.

## Soal 4: kursi bioskop yang tersusun rapi

Di sebuah aula, kursi disusun per baris. Baris pertama berisi 20 kursi, dan setiap baris berikutnya berisi 3 kursi lebih banyak dari baris di depannya. Berapa banyak kursi pada baris ke-12, dan berapa jumlah kursi pada 10 baris pertama?

Soal cerita seperti ini adalah yang paling sering membuat anak berhenti sebelum menghitung, karena mereka harus menerjemahkan cerita menjadi barisan dulu. Baris pertama 20 kursi berarti $a = 20$, dan "3 kursi lebih banyak" berarti $b = 3$. Setelah diterjemahkan, soalnya menjadi soal barisan biasa.

Kursi pada baris ke-12 adalah $U_{12} = 20 + 11 \times 3 = 20 + 33 = 53$. Jumlah kursi pada 10 baris pertama adalah $S_{10} = \frac{10}{2}\bigl(2 \times 20 + 9 \times 3\bigr) = 5 \times (40 + 27) = 5 \times 67 = 335$.

Yang saya tekankan di sini adalah urutan kerjanya: terjemahkan dulu, hitung kemudian. Anak yang langsung mengalikan 20 dengan 3 tanpa menulis $a$ dan $b$ hampir selalu salah, sedangkan anak yang menulis $a = 20$ dan $b = 3$ di kertasnya jarang sekali tersesat.

## Latihan mandiri

Kerjakan dua soal berikut di buku latihan, lalu cocokkan dengan kunci di bawah.

1. Tentukan suku ke-25 dari barisan $5, 9, 13, 17, \dots$
2. Tentukan jumlah 12 suku pertama dari barisan $4, 7, 10, 13, \dots$

**Kunci jawaban:** 1) $U_{25} = 5 + 24 \times 4 = 101$; 2) $S_{12} = \frac{12}{2}(2 \times 4 + 11 \times 3) = 6 \times 41 = 246$.

## Penutup

Barisan aritmetika mengajarkan satu kebiasaan yang berguna jauh di luar matematika: sebelum menghitung, pastikan dulu apa yang diketahui dan apa yang ditanyakan. Empat soal di atas sengaja saya susun dari yang paling mudah ditebak sampai yang paling membutuhkan terjemahan, supaya anak merasakan sendiri bahwa rumusnya tidak pernah berubah, yang berubah hanya cara soalnya disajikan. Kalau kebiasaan membaca dulu itu sudah terbentuk, soal barisan apa pun tinggal soal menghitung.
