---
weight: 1
title: "Dari Lidi ke Tabungan: Mengajar Barisan Aritmetika yang Tumbuh Tetap untuk Kelas VIII"
date: 2026-11-17T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Barisan aritmetika saya ajarkan dari segitiga lidi di meja murid dan tabungan mingguan — sampai mereka sendiri yang menemukan bahwa suku ke-n selalu memakai (n − 1), bukan n."
featuredImage: "featured-image.png"

tags: ["Barisan Aritmetika", "Kelas VIII", "Ide Mengajar"]
categories: ["Matematika"]

math:
  enable: true
---

Pelajaran hari itu saya buka bukan dengan definisi, melainkan dengan segenggam lidi. Saya bagikan beberapa batang lidi ke tiap kelompok dan meminta mereka menyusun satu segitiga di atas meja. "Tiga batang," kata mereka. Lalu saya minta mereka menempelkan segitiga kedua di samping segitiga pertama, berbagi satu sisi. "Berapa batang sekarang?" Mereka menghitung: lima. Segitiga ketiga ditempel lagi di sampingnya, dan jumlahnya menjadi tujuh. Di papan saya tulis deret angka yang baru saja mereka buat sendiri: $3, 5, 7, 9, 11, \ldots$ Seorang murid nyeletuk, "Naik dua terus, Pak." Tepat. Di situlah barisan aritmetika masuk ke kelas kami — bukan sebagai rumus yang jatuh dari langit, melainkan sebagai pola yang baru saja mereka susun dengan tangan mereka sendiri.

<!--more-->

## Pola yang tumbuh tetap

Saya tulis kalimat itu di papan dan kami sepakati bersama: barisan aritmetika adalah barisan bilangan yang selisih dua suku berurutannya selalu tetap. Selisih tetap itu kami sebut beda, disimbolkan $b$. Pada segitiga lidi tadi, bedanya $2$ — setiap segitiga baru selalu menambah dua batang, karena satu sisinya menumpang pada segitiga sebelumnya. Itulah alasan fisik di balik angka itu, dan murid yang memegang lidinya sendiri tidak perlu menghafal: mereka melihat mengapa tambahannya dua, bukan tiga.

Supaya polanya makin terasa, saya ajak kelas melihat ubin di lantai musala. Baris pertama ada $1$ ubin bermotif, baris kedua $4$, baris ketiga $7$, lalu $10$. Bedanya $3$, tetap dari baris ke baris. Saya tanya, "Baris ke-20 ada berapa ubin?" Tidak ada yang berlari menghitung satu per satu sampai dua puluh — mereka sudah mencium ada jalan pintas. Di sinilah rumus suku ke-$n$ saya perkenalkan, sebagai jalan pintas yang lahir dari pola, bukan dari hafalan.

## Rumus suku ke-n, dan jebakan yang paling sering muncul

Saya tunjukkan cara berpikirnya pelan-pelan. Suku pertama, $a$, kita pegang. Untuk sampai ke suku kedua, kita melangkah satu kali sebesar beda. Ke suku ketiga, dua langkah. Ke suku keempat, tiga langkah. Polanya jelas: suku ke-$n$ ditempuh dengan $n - 1$ langkah. Maka rumusnya:

$$U_n = a + (n-1)b$$

Untuk ubin musala tadi: $a = 1$, $b = 3$, maka suku ke-20 adalah $U_{20} = 1 + 19 \times 3 = 58$. Lima puluh delapan ubin bermotif pada baris kedua puluh — jawaban yang mustahil diperoleh dengan menghitung satu per satu di waktu yang tersisa.

Lalu saya tunjukkan jebakan yang hampir selalu muncul di ulangan: murid yang memakai $n$, bukan $n - 1$. Pada segitiga lidi, suku ke-15 yang benar adalah $U_{15} = 3 + 14 \times 2 = 31$ batang. Murid yang lupa mengurangi satu akan menulis $3 + 15 \times 2 = 33$ — lebih dua batang, persis sebesar satu segitiga. Saya minta mereka memeriksa dengan cara kecil: suku ke-2 harus memberi $3 + 1 \times 2 = 5$, dan memang lima batang yang mereka pegang tadi. Kalau rumusnya benar untuk suku ke-2, ia benar untuk suku ke-15. Cara memeriksa yang sederhana ini saya ulang berkali-kali, karena di matematika, satu soal kecil yang bisa dicek dengan tangan sering lebih meyakinkan daripada seratus kali hafalan.

## Menabung: barisan yang terasa di dompet

Setelah lidi dan ubin, saya pindah ke contoh yang menyentuh dompet mereka: menabung. Seorang murid bercerita ia menabung Rp10.000 pada minggu pertama, lalu menambah Rp5.000 setiap minggu. Maka tabungannya membentuk barisan $10.000, 15.000, 20.000, 25.000, \ldots$ dengan $a = 10.000$ dan $b = 5.000$. Saya tanya, "Minggu ke-8, berapa yang ia tabung minggu itu?" Kelas menghitung: $U_8 = 10.000 + 7 \times 5.000 = 45.000$. Lalu saya lanjutkan, "Kalau begitu, berapa total uangnya setelah delapan minggu?" Pertanyaan kedua ini berbeda — bukan satu suku, melainkan jumlah seluruh suku — dan justru di sinilah deret aritmetika masuk secara alami.

## Menjumlahkan semuanya: deret aritmetika

Untuk menjumlahkan delapan minggu tabungan itu, saya tunjukkan trik pasangan yang konon dipakai Gauss kecil: pasangkan suku pertama dengan suku terakhir, suku kedua dengan suku kedua terakhir, dan seterusnya. Setiap pasangan berjumlah sama: $10.000 + 45.000 = 55.000$, dan ada empat pasangan. Maka totalnya $4 \times 55.000 = 220.000$ rupiah. Rumus umumnya sama saja, ditulis rapi:

$$S_n = \frac{n}{2}\left(a + U_n\right)$$

Saya terapkan rumus yang sama pada ubin musala: berapa ubin bermotif seluruhnya dari baris pertama sampai baris kesepuluh? Suku kesepuluh adalah $U_{10} = 1 + 9 \times 3 = 28$, maka $S_{10} = \frac{10}{2} \times (1 + 28) = 145$ ubin. Seorang murid langsung mengecek dengan cara pasangan yang sama: baris pertama dan kesepuluh berjumlah $1 + 28 = 29$, dan ada lima pasangan seperti itu — $5 \times 29 = 145$. Dua jalan yang berbeda menuju jawaban yang sama selalu membuat kelas lebih percaya pada rumusnya.

## Kalau bedanya negatif

Sebelum menutup, saya balik arah polanya supaya murid tidak mengira beda selalu positif. Tandon air di sekolah berisi $100$ liter; setiap hari dipakai $5$ liter tanpa diisi. Isinya membentuk barisan $100, 95, 90, 85, \ldots$ dengan beda $-5$. Hari ke-12 isinya tinggal $U_{12} = 100 + 11 \times (-5) = 45$ liter. Rumusnya tidak berubah — hanya bedanya yang negatif — dan murid yang paham ini tidak akan panik saat bertemu soal cerita yang angkanya mengecil.

Pelajaran itu saya tutup dengan meminta tiap kelompok membuat satu barisan dari benda di sekitar mereka: anak tangga, nomor rumah di gang, atau jadwal piket. Syaratnya satu: bedanya harus tetap, dan mereka harus bisa menjawab suku ke-10 tanpa menghitung satu per satu. Esoknya, satu kelompok datang membawa barisan dari deretan kursi di aula, kelompok lain dari harga gorengan yang naik lima ratus rupiah setiap tahun. Polanya sudah pindah dari papan tulis ke kepala mereka — dan dari kepala mereka ke jalan di depan sekolah. Di situlah saya tahu barisan aritmetika hari itu sungguh mereka miliki, bukan sekadar mereka hafalkan.
