---
weight: 1
title: "Mengapa 1 Bukan Bilangan Prima? Pendalaman Definisi yang Sering Dianggap Sepele"
date: 2026-11-07T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman bilangan prima untuk kelas VII: membongkar mengapa 1 bukan bilangan prima meski hanya bisa dibagi 1 dan dirinya sendiri, dan mengapa definisi itu dibuat demi keunikan faktorisasi."
featuredImage: "featured-image.png"

tags: ["Bilangan Prima", "Pendalaman", "Kelas VII", "Teori Bilangan"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VII saya, kami sedang mengelompokkan bilangan 1 sampai 20 menjadi bilangan prima dan bukan prima. Saya menulis angka 1 di papan tulis, lalu bertanya, "Yang ini masuk mana?" Seorang murid mengangkat tangan dengan yakin, "Prima, Pak. Satu hanya bisa dibagi satu dan dirinya sendiri." Logikanya terdengar rapi, bahkan hampir tidak bisa dibantah. Tapi saya menahan diri untuk tidak langsung membenarkan. "Coba kita hitung dulu," kata saya, "ada berapa pembagi yang dimiliki angka 1?"

Hari itu kelas saya menemukan bahwa definisi yang kelihatan sepele bisa menyimpan alasan yang dalam. Artikel ini adalah pendalaman dari materi bilangan prima yang sudah kita pelajari sebelumnya. Kalau kemarin kita berlatih menentukan mana yang prima dan mana yang bukan, hari ini kita mencari tahu mengapa angka 1 ditolak masuk ke dalam kelompok bilangan prima, dan mengapa penolakan itu bukan sekadar aturan yang dibuat-buat.

<!--more-->

## Apa sebenarnya kata definisi

Definisi bilangan prima yang dipakai di buku berbunyi begini: bilangan prima adalah bilangan asli yang lebih besar dari 1 dan hanya memiliki tepat dua pembagi, yaitu 1 dan dirinya sendiri. Perhatikan dua syaratnya. Pertama, bilangannya harus lebih besar dari 1. Kedua, pembaginya harus tepat dua dan berbeda.

Angka 2 memenuhi keduanya. Pembaginya adalah 1 dan 2, tepat dua pembagi yang berbeda. Angka 3 juga: pembaginya 1 dan 3. Angka 5: pembaginya 1 dan 5. Angka 7: pembaginya 1 dan 7. Semua lolos.

Sekarang angka 1. Pembaginya siapa saja? Hanya angka 1 itu sendiri. Kalau kita menulis daftar pembagi 1, daftarnya hanya berisi satu nama: $1$. Syarat kedua meminta tepat dua pembagi yang berbeda, dan angka 1 hanya punya satu. Ia gagal bukan karena pembaginya terlalu banyak, melainkan karena terlalu sedikit.

Di sinilah jebakan logika murid saya tadi. Kalimat "hanya bisa dibagi 1 dan dirinya sendiri" memang benar untuk angka 1, tetapi untuk angka 1, "1" dan "dirinya sendiri" adalah orang yang sama. Syarat definisi meminta dua pembagi yang berbeda, dan angka 1 tidak bisa menyediakan dua nama yang berbeda. Ibarat diminta membawa dua orang saksi yang berbeda, lalu kita membawa satu orang yang sama dua kali. Tidak lolos.

## Mengapa definisinya dibuat seperti itu

Pertanyaan berikutnya tentu saja: mengapa matematikawan membuat definisi yang mengecualikan angka 1? Apakah mereka sekadar tidak suka angka 1? Jawabannya ada pada sebuah teorema besar yang menjadi fondasi teori bilangan: setiap bilangan asli yang lebih besar dari 1 dapat ditulis sebagai perkalian bilangan-bilangan prima dengan cara yang tunggal, kalau urutannya diabaikan.

Ambil angka 12. Faktorisasi primanya adalah $2 \times 2 \times 3$. Hanya itu. Tidak ada cara lain. Angka 30 faktorisasi primanya $2 \times 3 \times 5$, tunggal juga. Keunikan inilah yang membuat bilangan prima menjadi "bata penyusun" semua bilangan: setiap bilangan punya satu resep penyusun yang pasti.

Sekarang bayangkan kalau angka 1 dianggap prima. Faktorisasi 12 tidak lagi tunggal. Kita bisa menulis $12 = 2 \times 2 \times 3$, tetapi juga $12 = 1 \times 2 \times 2 \times 3$, dan $12 = 1 \times 1 \times 2 \times 2 \times 3$, dan seterusnya tanpa ujung. Pohon faktor tidak pernah selesai digambar. Keunikan yang menjadi kekuatan teorema itu runtuh hanya karena satu angka ikut masuk ke dalam kelompok prima.

Jadi pengecualian angka 1 bukan aturan yang dibuat asal-asalan. Definisi itu dirancang supaya teorema besar tentang faktorisasi tetap rapi dan berlaku. Matematika memang sering begitu: sebuah definisi yang kelihatan cerewet ternyata dibuat untuk melindungi sebuah kebenaran yang lebih besar.

## Dua jebakan yang sering muncul

Jebakan pertama sudah kita bahas: mengira angka 1 prima karena kalimat "hanya bisa dibagi 1 dan dirinya sendiri" terdengar cocok untuknya. Obatnya sederhana: minta murid menulis daftar pembaginya dan menghitungnya. Begitu daftar itu hanya berisi satu nama, mereka sendiri yang akan melihat bahwa syarat "tepat dua pembagi yang berbeda" tidak terpenuhi.

Jebakan kedua adalah mengira semua bilangan ganjil itu prima. Angka 9 ganjil, tetapi pembaginya 1, 3, dan 9 — tiga pembagi, bukan prima. Angka 15 ganjil, pembaginya 1, 3, 5, dan 15. Ganjil saja tidak cukup; yang menentukan adalah jumlah pembaginya.

Jebakan ketiga adalah kebalikannya: mengira angka 2 bukan prima karena ia genap. Padahal 2 adalah satu-satunya bilangan prima yang genap, dan ia genap justru karena pembaginya hanya 1 dan 2. Setiap bilangan genap lain selalu punya pembagi 2 sebagai tambahan, sehingga pembaginya minimal tiga. Jadi keganjilan bukan syarat prima, dan kegenapan bukan penghalang prima. Yang menjadi patokan selalu jumlah pembagi yang berbeda.

## Kegiatan di kelas: kartu pembagi

Supaya murid tidak sekadar menghafal, saya memberi mereka kegiatan sederhana. Setiap kelompok mendapat kartu-kartu bertuliskan bilangan 1 sampai 20. Tugas mereka: tulis semua pembagi setiap bilangan, lalu kelompokkan kartu itu berdasarkan banyaknya pembagi.

Hasilnya selalu menarik. Kartu angka 1 berdiri sendiri di kelompok "satu pembagi". Kartu 2, 3, 5, 7, 11, 13, 17, dan 19 berkumpul di kelompok "dua pembagi". Sisanya, seperti 4, 6, 8, 9, 10, 12, dan seterusnya, masuk kelompok "lebih dari dua pembagi". Murid melihat sendiri bahwa angka 1 tidak punya teman di kelompok mana pun: ia bukan prima, tetapi juga bukan komposit. Ia satu-satunya penghuni kelompoknya sendiri.

Dari kegiatan itu, satu kesimpulan muncul dengan sendirinya: bilangan prima adalah bilangan dengan tepat dua pembagi, bilangan komposit adalah bilangan dengan lebih dari dua pembagi, dan angka 1 berada di luar keduanya. Tidak ada yang perlu dihafal dengan paksa, karena polanya sudah terlihat di meja mereka.

## Penutup

Angka 1 bukan bilangan prima bukan karena matematikawan membencinya, melainkan karena definisi prima dirancang untuk menjaga keunikan faktorisasi. Satu angka yang dibiarkan masuk akan meruntuhkan kepastian bahwa setiap bilangan punya satu resep penyusun yang tunggal. Dan ketika murid bertanya "mengapa", jawaban terbaik bukan "karena begitu aturannya", melainkan "karena kalau tidak begitu, sesuatu yang besar akan rusak".
