---
weight: 1
title: "Mengapa Bilangan Prima Tidak Pernah Habis? Bukti Euclid yang Berumur 2.300 Tahun"
date: 2026-11-28T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman bilangan prima untuk kelas VIII dan IX: bukti Euclid bahwa prima tidak pernah habis, dicoba langsung dengan perkalian prima pertama ditambah satu."
featuredImage: "featured-image.png"

tags: ["Bilangan Prima", "Pendalaman", "Teori Bilangan", "Kelas VIII", "Kelas IX"]
categories: ["Matematika"]

math:
  enable: true
---

Suatu hari di kelas VIII, setelah kami selesai menyaring bilangan prima sampai 100 dengan saringan Eratosthenes, seorang murid mengangkat tangan. "Pak, bilangan prima yang paling besar itu berapa?" Saya diam sejenak, lalu menjawab, "Tidak ada." Kelas riuh. "Masa tidak ada, Pak? Kan semua bilangan ada yang paling besar?" Saya tersenyum. Justru di situlah letak keindahannya: bilangan prima tidak pernah habis. Dan yang lebih menakjubkan, orang sudah membuktikan hal itu lebih dari 2.300 tahun yang lalu — dengan penalaran yang begitu sederhana sampai murid kelas VIII pun bisa mengikutinya. Namanya bukti Euclid, dan hari ini saya ingin mengajak Anda berjalan menyusuri bukti itu selangkah demi selangkah.

<!--more-->

## Daftar prima yang selalu bisa diperpanjang

Mari kita mulai dari yang kita tahu. Bilangan prima adalah bilangan yang lebih besar dari 1 dan hanya habis dibagi 1 dan dirinya sendiri. Daftarnya dimulai begini: $2,\ 3,\ 5,\ 7,\ 11,\ 13,\ 17,\ 19,\ 23,\ 29$, lalu berlanjut $31,\ 37,\ 41$, dan seterusnya. Sejauh ini tidak ada yang aneh. Tetapi perhatikan polanya: jarak antarprima makin tidak beraturan, dan kadang kita harus menunggu lama sebelum menemukan prima berikutnya. Di sinilah pertanyaan murid tadi menjadi masuk akal: bagaimana kalau suatu hari kita sampai di ujung, dan ternyata tidak ada prima lagi setelah itu?

Euclid, matematikawan Yunani yang hidup sekitar tahun 300 sebelum Masehi, menjawab pertanyaan itu dalam bukunya *Elements*, tepatnya pada Proposisi 20 Buku IX. Ia tidak menghitung prima satu demi satu sampai ke ujung — itu mustahil. Ia justru membuktikan bahwa ujung itu tidak ada. Caranya: andaikan seseorang mengklaim sudah menemukan semua bilangan prima. Euclid menunjukkan bahwa dari daftar yang diklaim lengkap itu, kita selalu bisa membuat sebuah bilangan prima baru yang tidak ada di daftar. Daftar itu tidak pernah bisa lengkap.

## Triknya: kalikan semuanya, lalu tambah satu

Inilah trik Euclid. Ambil beberapa prima pertama, kalikan semuanya, lalu tambahkan satu. Coba dengan tiga prima pertama:

$$2 \times 3 \times 5 + 1 = 31$$

Hasilnya 31, dan 31 adalah bilangan prima — prima baru yang tidak ada di daftar $2,\ 3,\ 5$. Coba dengan empat prima pertama:

$$2 \times 3 \times 5 \times 7 + 1 = 211$$

Hasilnya 211, dan 211 juga prima. Coba dengan lima prima pertama:

$$2 \times 3 \times 5 \times 7 \times 11 + 1 = 2311$$

Hasilnya 2311, dan 2311 pun prima. Tiga kali mencoba, tiga kali kita menemukan prima baru. Murid-murid saya biasanya langsung menebak: "Wah, Pak, berarti cara ini selalu menghasilkan bilangan prima?" Dan di sinilah pelajaran menjadi menarik, karena jawaban saya adalah: "Tidak selalu."

Coba dengan enam prima pertama:

$$2 \times 3 \times 5 \times 7 \times 11 \times 13 + 1 = 30031$$

Apakah 30031 prima? Bukan. Ia bisa difaktorkan menjadi $59 \times 509$. Tetapi perhatikan baik-baik: 59 dan 509 keduanya adalah bilangan prima, dan keduanya tidak ada di daftar $2,\ 3,\ 5,\ 7,\ 11,\ 13$. Jadi meskipun 30031 sendiri bukan prima, ia tetap melahirkan prima baru. Inilah inti bukti Euclid, dan inilah bagian yang sering terlewat: yang penting bukan hasil kalinya prima atau bukan, melainkan bahwa hasilnya selalu membawa prima baru yang belum terdaftar.

## Mengapa prima baru itu selalu muncul

Mengapa hal ini selalu terjadi? Pikirkan sifat bilangan hasil kalinya. Misalkan kita punya daftar prima $p_1, p_2, \dots, p_n$ dan kita bentuk bilangan $N = p_1 \times p_2 \times \cdots \times p_n + 1$. Bilangan $N$ ini bila dibagi $p_1$ akan bersisa 1, karena bagian $p_1 \times p_2 \times \cdots \times p_n$ habis dibagi $p_1$, sedangkan tambah satunya membuat sisanya 1. Hal yang sama berlaku untuk $p_2$, $p_3$, sampai $p_n$: $N$ tidak habis dibagi satu pun prima di daftar kita.

Sekarang ada dua kemungkinan. Pertama, $N$ sendiri prima — maka kita menemukan prima baru. Kedua, $N$ bukan prima — maka $N$ pasti punya faktor prima. Tetapi faktor prima itu tidak mungkin ada di daftar kita, karena sudah kita buktikan $N$ tidak habis dibagi satu pun dari mereka. Jadi faktor primanya adalah prima yang belum terdaftar. Dalam kedua kemungkinan, kita selalu menemukan bilangan prima yang tidak ada di daftar semula. Daftar prima tidak pernah bisa lengkap — dan karena itu prima tidak pernah habis.

Penalaran ini bekerja untuk daftar sepanjang apa pun. Ambil sejuta prima pertama, kalikan, tambah satu, dan Anda tetap akan menemukan prima baru. Itulah yang membuat bukti Euclid begitu memukau: ia tidak perlu menghitung sampai jauh. Dengan satu langkah penalaran, ia menutup kemungkinan adanya prima terbesar, untuk selama-lamanya.

## Kegiatan lima menit di kelas

Saya biasa mengajak murid mencoba trik ini sendiri, dengan kalkulator di tangan. Saya memberi setiap kelompok daftar prima yang berbeda — satu kelompok memakai $2,\ 3,\ 5$, kelompok lain $2,\ 3,\ 5,\ 7$, kelompok lain lagi $2,\ 3,\ 5,\ 7,\ 11,\ 13$ — lalu mereka menghitung $N$ dan memeriksa apakah $N$ prima atau harus difaktorkan. Kelompok yang mendapat 30031 biasanya paling ribut, karena mereka mengira triknya gagal — sampai mereka menemukan $59 \times 509$ dan sadar bahwa triknya justru bekerja dengan cara yang lebih dalam dari dugaan mereka.

Di akhir kegiatan saya bertanya: "Jadi, adakah bilangan prima yang paling besar?" Mereka menjawab serempak: "Tidak ada, Pak." Lalu saya menambahkan satu hal lagi: bilangan prima terbesar yang diketahui manusia hari ini punya puluhan juta digit, dan para matematikawan masih terus mencarinya — bukan karena ada ujungnya, melainkan karena Euclid sudah membuktikan tidak ada ujung. Pencarian itu tidak akan pernah selesai, dan justru itulah yang membuat prima tetap hidup sebagai misteri selama ribuan tahun.

Jadi, lain kali ada murid yang bertanya bilangan prima yang paling besar itu berapa, saya tidak akan menjawab dengan angka. Saya akan menjawab dengan sebuah pertanyaan balik: "Kalau kamu punya daftar semua prima, bisakah kamu membuat prima baru dari daftar itu?" Dan bila ia sudah tahu trik kalikan-lalu-tambah-satu, ia akan tersenyum — karena ia baru saja memegang bukti berumur 2.300 tahun di tangannya sendiri.
