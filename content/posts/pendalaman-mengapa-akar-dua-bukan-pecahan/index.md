---
weight: 1
title: "Mengapa √2 Tidak Bisa Ditulis sebagai Pecahan? Pendalaman Bilangan Irasional"
date: 2026-11-07T16:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman bilangan irasional untuk kelas VIII: membuktikan mengapa √2 tidak akan pernah sama dengan pecahan mana pun, lewat bukti genap dan ganjil yang hanya butuh satu kontradiksi."
featuredImage: "featured-image.png"

tags: ["Bilangan Irasional", "Pendalaman", "Kelas VIII", "Teori Bilangan"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VIII saya, kami sedang menghitung sisi miring segitiga siku-siku. Saya menggambar segitiga yang kedua sisi tegaknya sama-sama 1 satuan, lalu bertanya, "Berapa panjang sisi miringnya?" Seorang murid menjawab cepat, "Akar dua, Pak." "Berapa nilainya?" tanya saya lagi. Ia menekan kalkulator, lalu membaca, "Satu koma empat satu empat dua..." Lalu ia berhenti dan menatap saya. "Pak, ujungnya di mana?"

Pertanyaan itu lebih dalam dari yang ia kira. Hari itu kelas saya menemukan bahwa ada bilangan yang tidak bisa ditulis sebagai pecahan, sekeras apa pun kita mencarinya. Artikel ini adalah pendalaman dari materi bilangan yang sudah kita pelajari sebelumnya: kalau kemarin kita berlatih membedakan bilangan rasional dan irasional, hari ini kita membuktikan sendiri mengapa $\sqrt{2}$ tidak akan pernah sama dengan pecahan mana pun, dan mengapa kepastian itu justru membebaskan.

<!--more-->

## Mencari pecahan yang cocok

Sebelum membuktikan, kami mencoba dulu. Kalau $\sqrt{2}$ memang sama dengan suatu pecahan, pecahan itu pasti bisa ditemukan. Kami mulai dari yang kasar: $\frac{7}{5} = 1,4$. Kuadratnya $\frac{49}{25} = 1,96$ — masih kurang dari 2. Lalu $\frac{17}{12} \approx 1,4167$. Kuadratnya $\frac{289}{144} \approx 2,007$ — sekarang kelebihan. Kami mempersempit: $\frac{41}{29} \approx 1,4138$, kuadratnya $\frac{1681}{841} \approx 1,9988$ — kurang sedikit. Lalu $\frac{99}{70} \approx 1,41429$, kuadratnya $\frac{9801}{4900} \approx 2,0002$ — lebih sedikit.

Polanya jelas: setiap pecahan bisa didekatkan, tetapi tidak pernah tepat. Selisihnya mengecil, tetapi tidak pernah nol. Bahkan dengan desimal pun begitu: $1,41^2 = 1,9881$ dan $1,42^2 = 2,0164$, jadi $\sqrt{2}$ terjepit di antara 1,41 dan 1,42, tetapi tidak pernah sama dengan bilangan desimal berujung mana pun. Murid saya bertanya, "Mungkin pecahannya saja yang belum ketemu, Pak?" Pertanyaan yang bagus. Dan justru karena itu, tebakan harus diganti dengan bukti.

## Bukti yang hanya butuh bilangan genap dan ganjil

Andaikan saja $\sqrt{2}$ bisa ditulis sebagai pecahan $\frac{p}{q}$, dengan $p$ dan $q$ bilangan asli dan pecahan itu sudah paling sederhana — artinya $p$ dan $q$ tidak punya pembagi bersama selain 1. Ini asumsi yang wajar: setiap pecahan bisa disederhanakan sampai FPB pembilang dan penyebutnya 1.

Kalau $\sqrt{2} = \frac{p}{q}$, maka dengan menguadratkan kedua ruas, $2 = \frac{p^2}{q^2}$, atau $p^2 = 2q^2$. Jadi $p^2$ adalah dua kali suatu bilangan — $p^2$ pasti genap. Dan kalau kuadrat suatu bilangan genap, bilangannya sendiri pasti genap: kuadrat bilangan ganjil selalu ganjil. Jadi $p$ genap. Tulis $p = 2k$ untuk suatu bilangan asli $k$.

Masukkan kembali: $(2k)^2 = 2q^2$, jadi $4k^2 = 2q^2$, dan setelah dibagi 2, $q^2 = 2k^2$. Sekarang giliran $q^2$ yang genap, sehingga $q$ pun genap.

Inilah bentroknya. Kita mengandaikan $p$ dan $q$ tidak punya pembagi bersama selain 1, tetapi pembuktian ini memaksa $p$ dan $q$ sama-sama genap — keduanya bisa dibagi 2. Asumsi awal kita runtuh. Karena asumsi itu yang runtuh, kesimpulannya: tidak ada pecahan $\frac{p}{q}$ yang sama dengan $\sqrt{2}$, betapa pun besar pembilang dan penyebutnya.

## Apa artinya bagi garis bilangan

Jadi $\sqrt{2}$ adalah bilangan irasional: bilangan yang tidak bisa ditulis sebagai perbandingan dua bilangan bulat. Desimalnya berjalan tanpa ujung dan tanpa pola yang berulang: $1,4142135623730951\ldots$ — digit-digit itu terus berlanjut tanpa pernah mengulang satu pola tetap.

Bandingkan dengan $\frac{1}{3} = 0,333\ldots$ — desimalnya juga tak berujung, tetapi polanya berulang: angka 3 terus. Bilangan seperti itu tetap rasional, karena ada pecahannya. Pada $\sqrt{2}$, tidak ada pola yang berulang dan tidak ada pecahan yang menunggu di ujung pencarian.

Ini juga berarti garis bilangan punya titik-titik yang tidak bisa ditempati pecahan mana pun. Titik $\sqrt{2}$ ada di sana — bisa kita tunjuk dengan jangka dan penggaris lewat segitiga yang kedua kakinya 1 — tetapi tidak ada pecahan yang tepat menempati titik itu. Pecahan hanya bisa mendekat, sedekat apa pun, tanpa pernah sampai.

## Tiga jebakan yang sering muncul

Jebakan pertama: mengira angka kalkulator adalah nilai $\sqrt{2}$ yang sebenarnya. Kalkulator menampilkan 1,41421356, tetapi itu hanya pendekatan sepuluh digit. Kalau dikuadratkan, $1,41421356^2 = 1,999999993\ldots$ — nyaris 2, tetapi bukan 2. Kalkulator memotong, bukan menyelesaikan.

Jebakan kedua: mengira semua desimal panjang adalah pecahan. Murid sering menyamakan "desimalnya panjang" dengan "pasti ada pecahannya". Padahal yang menentukan adalah pola: desimal berulang selalu punya pecahan, desimal yang tidak berulang dan tidak berakhir tidak punya.

Jebakan ketiga: mengira bukti di atas hanya permainan kata. Padahal justru sebaliknya: bukti itu menunjukkan bahwa kegagalan menemukan pecahan bukan karena kita kurang gigih, melainkan karena pecahan itu memang tidak ada. Matematika membedakan dua hal itu — belum ketemu dan tidak ada — dan bukti adalah alat yang membedakannya.

## Kegiatan di kelas: lomba pecahan terdekat

Supaya murid merasakannya sendiri, saya mengadakan lomba kecil. Setiap kelompok mencari pecahan yang kuadratnya paling dekat dengan 2, dengan pembilang dan penyebut masing-masing tidak lebih dari 100. Mereka mulai dari $\frac{7}{5}$ dan $\frac{17}{12}$, lalu menemukan $\frac{41}{29}$ dan $\frac{99}{70}$. Kelompok yang menemukan $\frac{99}{70}$ bersorak — kuadratnya $2,0002$, selisih hanya $0,0002$ dari 2.

Tetapi setelah sorak itu, saya meminta mereka membuktikan: adakah pecahan yang kuadratnya tepat 2? Di sinilah bukti genap-ganjil tadi masuk. Lomba mencari pecahan berubah menjadi pemahaman: mendekat tanpa batas itu mungkin, tetapi sampai tepat itu mustahil. Dan justru dari kemustahilan itulah lahir satu kelompok bilangan baru: bilangan irasional.

## Penutup

$\sqrt{2}$ mengajari kelas saya satu hal yang lebih besar dari sekadar satu bilangan: bahwa "belum ketemu" dan "tidak ada" adalah dua pernyataan yang berbeda, dan matematika punya cara untuk membuktikannya. Sebuah pecahan boleh mendekati $\sqrt{2}$ sedekat apa pun, tetapi titik itu sendiri hanya dimiliki oleh bilangan irasional. Dan ketika murid bertanya lagi, "Pak, ujungnya di mana?" — sekarang saya bisa menjawab, "Tidak ada ujungnya. Dan ketiadaan ujung itu justru yang membuat bilangan ini istimewa."
