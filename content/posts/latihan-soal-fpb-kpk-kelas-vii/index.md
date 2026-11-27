---
weight: 1
title: "Bagi Rata atau Bertemu Lagi: Latihan Soal FPB dan KPK untuk Kelas VII"
date: 2026-11-27T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lembar latihan FPB dan KPK untuk kelas VII: empat soal faktorisasi prima dan soal cerita dengan pembahasan langkah demi langkah, plus dua latihan mandiri beserta kuncinya."
featuredImage: "featured-image.png"

tags: ["FPB", "KPK", "Faktorisasi Prima", "Kelas VII"]
categories: ["Matematika"]

math:
  enable: true
---

Awal semester ini saya menulis dua bilangan di papan tulis, 36 dan 48, lalu bertanya, "Berapa bilangan terbesar yang bisa membagi habis keduanya?" Separuh kelas menjawab 12 dengan cepat. Lalu saya bertanya pertanyaan kedua: "Berapa bilangan terkecil yang habis dibagi keduanya?" Kelas mendadak hening, lalu seorang anak menjawab ragu-ragu, "144, Pak?" Betul. Dua pertanyaan itu hanya berbeda satu kata — terbesar dan terkecil — tetapi jawabannya datang dari dua cara berpikir yang berlawanan. Di situlah FPB dan KPK selalu membingungkan anak: namanya mirip, caranya mirip, tetapi yang dicari justru kebalikannya.

Saya sendiri selalu memulai dengan satu kalimat yang saya tulis besar-besar di papan: FPB itu **bagi rata**, KPK itu **bertemu lagi**. Kalau soalnya tentang membagi sesuatu sama banyak tanpa sisa, pikirkan FPB. Kalau soalnya tentang dua hal yang terjadi berulang lalu bertemu pada waktu yang sama, pikirkan KPK. Lembar latihan di bawah ini saya susun mengikuti kalimat itu: empat soal dengan pembahasan, lalu dua latihan mandiri.

<!--more-->

## Satu alat untuk keduanya: faktorisasi prima

Sebelum mengerjakan soal, saya selalu mengingatkan anak tentang satu alat yang sama untuk FPB dan KPK, yaitu faktorisasi prima dengan pohon faktor. Setiap bilangan kita uraikan menjadi perkalian bilangan-bilangan prima, lalu kita bandingkan pangkatnya.

Aturannya sederhana dan saya minta anak menghafalnya sebagai sepasang: FPB mengambil pangkat **terkecil** dari faktor prima yang **sama-sama dimiliki** kedua bilangan, sedangkan KPK mengambil pangkat **terbesar** dari **semua** faktor prima yang muncul. FPB mengecilkan, KPK membesarkan. Kalau hasil FPB Anda lebih besar dari bilangan yang dicari, atau hasil KPK lebih kecil dari bilangan yang dicari, pasti ada yang terbalik.

## Soal 1: FPB dari 36 dan 48

Tentukan FPB dari 36 dan 48.

Kita uraikan dulu keduanya. $36 = 2^2 \times 3^2$ dan $48 = 2^4 \times 3$. Faktor prima yang sama-sama dimiliki adalah 2 dan 3. Untuk FPB kita ambil pangkat terkecil dari masing-masing: pangkat terkecil dari 2 adalah $2^2$, dan pangkat terkecil dari 3 adalah $3^1$.

$$\text{FPB}(36, 48) = 2^2 \times 3 = 4 \times 3 = 12$$

Untuk memeriksa, saya selalu meminta anak membagi: $36 \div 12 = 3$ dan $48 \div 12 = 4$, keduanya habis dan hasilnya 3 dan 4 sudah tidak punya faktor bersama lagi. Kalau hasil pembagiannya masih punya faktor bersama, berarti FPB-nya belum maksimal.

## Soal 2: KPK dari 12 dan 18

Tentukan KPK dari 12 dan 18.

Faktorisasinya: $12 = 2^2 \times 3$ dan $18 = 2 \times 3^2$. Kali ini, untuk KPK, kita mengambil pangkat terbesar dari semua faktor prima yang muncul, yaitu $2^2$ dan $3^2$.

$$\text{KPK}(12, 18) = 2^2 \times 3^2 = 4 \times 9 = 36$$

Kesalahan paling sering di soal seperti ini adalah anak hanya mengalikan semua faktor yang muncul tanpa memilih pangkat terbesar, sehingga mendapat $2 \times 3 = 6$ atau $2^2 \times 3 = 12$ — padahal 12 tidak habis dibagi 18. Saya selalu meminta mereka memeriksa balik: 36 habis dibagi 12 dan habis dibagi 18, dan tidak ada bilangan lebih kecil dari 36 yang bisa begitu. Pemeriksaan balik ini memakan waktu sepuluh detik, tetapi menyelamatkan banyak jawaban.

## Soal 3: membagi permen sama rata (soal cerita FPB)

Ibu mempunyai 24 permen cokelat dan 36 permen stroberi. Permen itu akan dimasukkan ke dalam kotak-kotak dengan isi yang sama banyak, tanpa sisa. Berapa kotak terbanyak yang bisa dibuat, dan berapa isi tiap kotak?

Kata kuncinya ada di soal: "kotak terbanyak" dan "tanpa sisa". Kita membagi dua jenis permen ke dalam kotak yang sama, jadi yang dicari adalah FPB. Faktorisasinya: $24 = 2^3 \times 3$ dan $36 = 2^2 \times 3^2$. Ambil pangkat terkecil dari faktor yang sama: $2^2 \times 3 = 12$.

$$\text{FPB}(24, 36) = 12$$

Jadi kotak terbanyak adalah 12 kotak. Isi tiap kotak: $24 \div 12 = 2$ permen cokelat dan $36 \div 12 = 3$ permen stroberi. Setiap kotak berisi 2 cokelat dan 3 stroberi, dan tidak ada permen yang tersisa.

Yang saya tekankan di sini adalah soal cerita FPB selalu punya dua pertanyaan: berapa kelompoknya, lalu berapa isi tiap kelompok. Anak yang hanya menjawab 12 kotak baru menyelesaikan separuh soal. Biasakan menulis kedua jawabannya.

## Soal 4: dua lampu yang berkedip bersama (soal cerita KPK)

Lampu A berkedip setiap 6 detik dan lampu B berkedip setiap 8 detik. Kedua lampu berkedip bersama pada detik ke-0. Setelah berapa detik keduanya berkedip bersama lagi?

Kata kuncinya adalah "berkedip bersama lagi": dua kejadian berulang yang bertemu pada waktu yang sama. Itu KPK. Faktorisasinya: $6 = 2 \times 3$ dan $8 = 2^3$. Ambil pangkat terbesar dari semua faktor: $2^3 \times 3 = 24$.

$$\text{KPK}(6, 8) = 24$$

Jadi kedua lampu berkedip bersama lagi setelah 24 detik. Kalau pertanyaannya dilanjutkan — berapa kali keduanya berkedip bersama dalam 2 menit? — jawabannya tinggal membagi: $120 \div 24 = 5$ kali setelah detik ke-0, yaitu pada detik ke-24, 48, 72, 96, dan 120.

Jebakan di soal seperti ini adalah anak yang menghitung $6 + 8 = 14$ atau $6 \times 8 = 48$. Yang pertama tidak punya arti, yang kedua memang kelipatan bersama, tetapi bukan yang terkecil: 48 habis dibagi 6 dan 8, tetapi 24 sudah lebih dulu memenuhi dan lebih kecil. Kalimat "bertemu lagi" selalu berarti yang pertama kali bertemu, jadi jawabannya KPK, bukan sekadar perkalian.

## Latihan mandiri

Kerjakan dua soal berikut di buku latihanmu, lalu cocokkan dengan kunci di bawah.

1. Tentukan FPB dari 42 dan 56.
2. Tentukan KPK dari 15 dan 20.

**Kunci jawaban:** 1) 14 — karena $42 = 2 \times 3 \times 7$ dan $56 = 2^3 \times 7$, sehingga FPB-nya $2 \times 7 = 14$. 2) 60 — karena $15 = 3 \times 5$ dan $20 = 2^2 \times 5$, sehingga KPK-nya $2^2 \times 3 \times 5 = 60$.

## Penutup

Kalau saya harus merangkum satu pertemuan FPB dan KPK dalam satu kalimat, kalimatnya adalah kalimat di awal tadi: FPB itu bagi rata, KPK itu bertemu lagi. Anak yang sudah memegang kalimat itu jarang tertukar, karena sebelum menghitung mereka sudah tahu apa yang sedang dicari. Faktorisasi prima hanyalah alat hitungnya; arah berpikirnya ditentukan oleh cerita soalnya.

Untuk pertemuan berikutnya, saya akan meminta anak membuat sendiri satu soal cerita FPB dan satu soal cerita KPK dari kehidupan di sekolah — jadwal piket, lampu kelas, atau kue untuk teman sebangku. Soal yang mereka buat sendiri biasanya lebih mereka ingat daripada soal yang saya berikan.
