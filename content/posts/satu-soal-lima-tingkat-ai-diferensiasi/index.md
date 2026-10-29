---
weight: 1
title: "Satu Soal, Lima Tingkat: Meminta AI Mengubah Soal yang Sama untuk Kelas yang Berbeda"
date: 2026-10-29T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Satu soal induk yang diubah AI menjadi lima tingkat kesulitan membantu saya memberi latihan yang pas untuk tiap murid — tanpa begadang menyiapkan lima perangkat soal yang berbeda."
featuredImage: "featured-image.png"
tags: ["Teknologi Pendidikan", "Kecerdasan Buatan", "Diferensiasi", "Pembelajaran Matematika"]
categories: ["Teknologi Pendidikan"]
---

Di kelas saya ada murid yang menyelesaikan soal dalam tiga menit lalu menatap langit-langit sambil menunggu teman-temannya, dan ada murid yang masih membaca soal yang sama ketika bel hampir berbunyi. Dulu saya mencoba mengatasi keadaan itu dengan membuat soal yang berbeda-beda untuk kelompok yang berbeda. Niatnya baik, hasilnya melelahkan: satu malam habis hanya untuk menyiapkan latihan, dan keesokan harinya saya mengajar dengan kepala yang sudah lelah duluan.

Belakangan saya mengubah cara itu. Saya tidak lagi membuat lima perangkat soal dari nol. Saya membuat satu soal induk yang baik, lalu meminta AI mengubahnya menjadi lima tingkat kesulitan. Bukan supaya AI yang mengajar, melainkan supaya saya punya bahan diferensiasi tanpa begadang — dan waktu saya bisa kembali dipakai untuk hal yang tidak bisa dikerjakan AI, yaitu mengamati murid satu per satu.

<!--more-->

## Satu Soal Induk, Bukan Lima Soal Berbeda

Kuncinya ada pada soal induk. Soal induk harus menguji satu konsep yang jelas, bukan campuran tiga konsep sekaligus. Misalnya, untuk materi keliling dan luas persegi panjang di kelas VII, soal induk saya berbunyi begini: "Sebuah persegi panjang memiliki panjang 12 cm dan lebar 8 cm. Hitunglah keliling dan luasnya."

Dari soal induk itu, saya meminta AI membuat lima tingkat. Tingkat pertama memakai angka yang lebih bersahabat dan hanya menanyakan satu hal, misalnya kelilingnya saja. Tingkat kedua sama dengan soal induk: keliling dan luas. Tingkat ketiga membalik pertanyaannya: luasnya diketahui, lebarnya ditanyakan. Tingkat keempat membungkus konsep yang sama ke dalam soal cerita, misalnya menghitung panjang pagar kebun atau banyak keramik untuk lantai. Tingkat kelima membuka soal itu menjadi soal bernalar: dua persegi panjang yang kelilingnya sama, apakah luasnya pasti sama? Murid diminta membuktikan jawabannya dengan contoh.

Perhatikan bahwa kelima tingkat itu tidak pernah meninggalkan konsepnya. Yang berubah hanya jalurnya: dari menghitung langsung, menjadi membalik, menjadi menerapkan, menjadi bernalar. Karena itu, ketika murid membandingkan jawabannya di akhir pelajaran, mereka masih membicarakan hal yang sama. Tidak ada yang merasa mengerjakan pelajaran lain.

## Prompt yang Saya Pakai

Prompt saya tidak panjang, tetapi selalu memuat empat hal. Pertama, soal induknya ditulis utuh. Kedua, jenjang dan materinya disebut jelas, misalnya "untuk kelas VII, materi keliling dan luas persegi panjang". Ketiga, lima tingkat itu saya deskripsikan satu per satu, bukan sekadar diminta "buatkan soal yang lebih sulit", karena tanpa deskripsi AI cenderung hanya memperbesar angkanya. Keempat, saya meminta kunci jawaban untuk tiap tingkat beserta alasan mengapa soal itu masuk tingkat tersebut.

Kalimat terakhir dalam prompt saya selalu sama: "Gunakan bahasa yang sederhana, dan jangan menambah konsep baru di luar keliling dan luas persegi panjang." Kalimat ini penting. Tanpa batasan itu, AI sering menambahkan unsur yang tidak saya minta — misalnya mengubah persegi panjang menjadi gabungan bangun — dan soal latihan berubah menjadi soal ulangan dadakan.

## Tiga Hal yang Selalu Saya Periksa Sendiri

AI menyiapkan draf, tetapi saya yang menandatangani soal itu sebelum dibagikan. Ada tiga hal yang selalu saya periksa. Pertama, kunci jawaban saya hitung ulang sendiri, tanpa terkecuali. AI bisa salah hitung, dan kesalahan itu paling berbahaya justru pada soal yang terlihat mudah, karena tidak ada yang curiga. Kedua, saya memeriksa apakah tingkatnya benar-benar naik. Kadang tingkat keempat ternyata lebih mudah daripada tingkat ketiga karena angkanya lebih bulat; kalau begitu, saya tukar urutannya atau saya ubah angkanya sendiri. Ketiga, saya memeriksa bahasanya. Soal cerita tidak boleh lebih sulit bahasanya daripada matematikanya. Kalau murid gagal bukan karena tidak paham persegi panjang melainkan karena tidak paham kalimatnya, maka soal itu gagal sebagai alat ukur.

Pemeriksaan ini memakan waktu sekitar sepuluh menit. Jauh lebih singkat daripada membuat lima perangkat soal dari nol, dan tetap menempatkan saya sebagai penentu mutu terakhir.

## Yang Berubah di Kelas Saya

Perubahan yang paling terasa bukan pada nilai, melainkan pada suasana. Murid yang cepat selesai tidak lagi menunggu lama, karena ia bisa lanjut ke tingkat berikutnya tanpa harus menunggu instruksi baru dari saya. Murid yang lambat tidak lagi merasa tertinggal, karena ia mengerjakan soal yang sama dengan teman-temannya, hanya dari jalur yang lebih landai. Dan saya tidak lagi kehabisan waktu di awal pelajaran hanya untuk membagi-bagikan lembar yang berbeda-beda; semua murid menerima lembar yang sama, lalu masing-masing mulai dari tingkat yang saya tentukan berdasarkan pengamatan saya selama ini.

Keputusan tentang siapa mulai dari tingkat mana tetap menjadi keputusan saya, bukan keputusan AI. Saya yang tahu siapa yang kemarin masih tertukar antara keliling dan luas, dan siapa yang sudah bisa menjelaskan kembali dengan kata-katanya sendiri. AI hanya menyiapkan tangganya; saya yang memutuskan anak tangga mana yang dipijak tiap murid.

Kalau Bapak dan Ibu guru ingin mencoba, mulailah dari satu soal induk saja, untuk satu pertemuan saja. Jangan langsung lima tingkat untuk satu bab penuh. Rasakan dulu sepuluh menit pemeriksaan itu, lihat dulu reaksi murid di kelas, baru putuskan apakah tangga ini layak dipakai lagi minggu depan. Teknologi yang baik, menurut pengalaman saya, bukan yang paling banyak fiturnya, melainkan yang membuat guru kembali punya waktu untuk memperhatikan muridnya.
