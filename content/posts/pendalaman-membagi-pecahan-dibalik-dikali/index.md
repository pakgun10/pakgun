---
weight: 1
title: "Mengapa Membagi Pecahan Harus Dibalik dan Dikali? Pendalaman Pembagian Pecahan"
date: 2026-10-31T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman pembagian pecahan untuk kelas VII: mengapa membagi dengan pecahan sama dengan mengalikan kebalikannya, dibuktikan lewat arti membagi dan cek balik — bukan sekadar hafalan dibalik lalu dikali."
featuredImage: "featured-image.png"

tags: ["Pecahan", "Pembagian Pecahan", "Bilangan Rasional", "Kelas VII"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VII saya, ada satu prosedur yang dihafal dengan sangat lancar tetapi dipahami dengan sangat tipis: membagi pecahan. Tulis soalnya, balik pecahan kedua, ganti bagi menjadi kali, lalu hitung. Jawabannya sering benar. Tetapi ketika saya bertanya, "Kenapa dibalik, Nak?" kelas mendadak sunyi. Ada yang menjawab jujur, "Kata buku begitu, Pak." Jawaban itu bukan salah murid. Itu tanda bahwa kita mengajar langkahnya tanpa mengajar alasannya.

Artikel ini adalah pendalaman pembagian pecahan. Kita tidak akan menambah aturan baru. Kita akan membongkar satu aturan yang paling sering dihafal itu, sampai murid melihat sendiri mengapa membalik itu masuk akal, bukan sekadar perintah.

<!--more-->

## Membagi itu bertanya: berapa kali muat?

Semua pembagian, dari bilangan bulat sampai pecahan, sebenarnya menanyakan hal yang sama: berapa kali pembagi muat di dalam bilangan yang dibagi? Kalau soalnya $12 \div 3$, kita bertanya berapa kali $3$ muat dalam $12$. Jawabannya $4$, dan tidak ada yang memperdebatkannya karena kita bisa menghitungnya dengan jari.

Sekarang ganti soalnya menjadi pecahan:

$$\frac{3}{4} \div \frac{1}{2} = ?$$

Pertanyaannya tetap sama: berapa kali $\frac{1}{2}$ muat dalam $\frac{3}{4}$? Gambarlah sebuah persegi panjang, arsir $\frac{3}{4}$ bagiannya, lalu potong daerah yang diarsir itu menjadi potongan-potongan sebesar $\frac{1}{2}$. Kita mendapat satu potong utuh, dan sisanya tinggal $\frac{1}{4}$ — tepat setengah dari satu potong $\frac{1}{2}$. Jadi jawabannya satu setengah potong, alias $\frac{3}{2}$. Hasil ini bisa dicek dengan prosedur hafalan: $\frac{3}{4} \times \frac{2}{1} = \frac{6}{4} = \frac{3}{2}$. Sama. Tetapi sekarang murid tahu bahwa $\frac{3}{2}$ bukan angka yang jatuh dari langit. Ia adalah jawaban dari pertanyaan "berapa kali muat".

Cara berpikir ini juga menjelaskan mengapa membagi dengan pecahan bisa menghasilkan bilangan yang lebih besar dari bilangan yang dibagi. Membagi $5$ dengan $\frac{2}{5}$ berarti bertanya berapa potong sepanjang $\frac{2}{5}$ meter yang bisa dipotong dari pita sepanjang $5$ meter. Karena potongannya lebih pendek dari satu meter, jumlah potongannya tentu lebih banyak dari $5$. Hitungannya membenarkan intuisi itu:

$$5 \div \frac{2}{5} = 5 \times \frac{5}{2} = \frac{25}{2} = 12{,}5$$

Dua belas potong penuh, ditambah setengah potong lagi. Murid yang memahami "berapa kali muat" tidak akan lagi terkejut melihat hasil bagi yang lebih besar dari bilangan semula.

## Mengapa dibalik? Bukti dari cek balik

Gambar memang meyakinkan, tetapi matematika butuh alasan yang berlaku umum, bukan hanya untuk satu contoh. Alasan itu datang dari hubungan antara pembagian dan perkalian: membagi adalah kebalikan dari mengalikan. Kalau $a \div b = c$, maka $c \times b = a$. Inilah kunci pembuktiannya.

Misalkan hasil yang kita cari kita beri nama $x$:

$$\frac{2}{3} \div \frac{4}{9} = x$$

Menurut hubungan di atas, $x$ dikali pembagi harus mengembalikan bilangan yang dibagi:

$$x \times \frac{4}{9} = \frac{2}{3}$$

Agar $x$ berdiri sendiri, kita perlu menghilangkan $\frac{4}{9}$. Caranya adalah mengalikan kedua ruas dengan kebalikan $\frac{4}{9}$, yaitu $\frac{9}{4}$, karena $\frac{4}{9} \times \frac{9}{4} = 1$:

$$x = \frac{2}{3} \times \frac{9}{4} = \frac{18}{12} = \frac{3}{2}$$

Di sinilah "dibalik lalu dikali" itu lahir. Ia bukan aturan yang dibuat-buat. Ia adalah konsekuensi dari satu fakta sederhana: mengalikan suatu pecahan dengan kebalikannya menghasilkan $1$, dan mengalikan dengan $1$ tidak mengubah nilai. Ketika murid melihat langkah ini sekali saja dengan sungguh-sungguh, prosedur hafalan itu berubah menjadi prosedur yang beralasan.

Satu contoh lagi yang saya suka karena hasilnya bulat dan memberi rasa puas: $\frac{5}{6} \div \frac{5}{12}$. Balik pecahan kedua, kalikan, sederhanakan:

$$\frac{5}{6} \times \frac{12}{5} = \frac{60}{30} = 2$$

Cek baliknya langsung terlihat: $2 \times \frac{5}{12} = \frac{10}{12} = \frac{5}{6}$. Cocok. Saya selalu meminta murid melakukan cek balik ini pada satu soal setiap latihan. Kebiasaan kecil itu membuat mereka punya cara sendiri untuk memverifikasi jawaban, tanpa menunggu saya membenarkan.

## Dua jebakan yang paling sering muncul

Jebakan pertama: membalik pecahan yang salah. Banyak murid membalik pecahan pertama, atau membalik keduanya. Padahal yang dibalik hanyalah pembagi, yaitu pecahan kedua. Saya mengingatkan mereka dengan kalimat pendek: "Yang membagi yang berbalik." Pada soal $\frac{3}{5} \div \frac{2}{7}$, yang berbalik adalah $\frac{2}{7}$ menjadi $\frac{7}{2}$, sehingga hasilnya $\frac{3}{5} \times \frac{7}{2} = \frac{21}{10}$. Kalau yang dibalik justru $\frac{3}{5}$, jawabannya melenceng jauh dan cek baliknya tidak akan cocok.

Jebakan kedua: membalik tetapi lupa mengganti tanda bagi menjadi kali. Ini tampak sepele, tetapi justru di sinilah letak maknanya: membalik tanpa mengganti operasi sama saja dengan tidak melakukan apa-apa. Saya mengajarkan keduanya sebagai satu paket yang tidak boleh dipisah: balik pembaginya, ganti operasinya, baru hitung. Dan satu kebiasaan tambahan yang menghemat banyak kesalahan: sederhanakan dengan coret silang sebelum mengalikan, supaya angkanya tetap kecil dan mudah dikendalikan.

## Di kelas saya: memotong kertas sebelum menghitung

Sebelum masuk ke simbol apa pun, saya membagikan kertas berwarna dan meminta kelompok memotongnya. Tugasnya sederhana: dari kertas $\frac{3}{4}$ bagian, buatlah potongan sebesar $\frac{1}{4}$ bagian, lalu hitung ada berapa potong. Semua kelompok menjawab $3$ tanpa rumus apa pun, karena mereka melihatnya dengan tangan sendiri. Baru setelah itu saya menulis soalnya di papan: $\frac{3}{4} \div \frac{1}{4} = 3$. Ketika simbol akhirnya muncul, ia menamai pengalaman yang sudah mereka miliki, bukan menggantikannya.

Urutan ini penting. Kalau rumus datang duluan, murid menghafal gerakan tangan. Kalau pengalaman datang duluan, rumus menjadi ringkasan dari sesuatu yang sudah mereka yakini. Pembagian pecahan yang diajarkan dengan urutan seperti ini jarang sekali tertukar, karena murid punya dua jangkar sekaligus: gambar di kepala mereka dan alasan di atas kertas.

## Penutup

Membagi pecahan tidak harus diajarkan sebagai mantra "dibalik lalu dikali". Di balik mantra itu ada pertanyaan yang sangat manusiawi — berapa kali muat — dan ada bukti yang sangat rapi — mengalikan dengan kebalikan menghasilkan satu. Kalau murid kita sudah memegang keduanya, prosedur itu tidak akan lagi rapuh. Ia akan bertahan ketika soalnya berubah bentuk, ketika angkanya tidak lagi cantik, dan ketika tidak ada guru di samping mereka untuk membenarkan. Dan bukankah itu tujuan kita mengajar: bukan murid yang bisa menjawab hari ini, melainkan murid yang masih bisa menjawab ketika kita sudah tidak ada di depan kelas?
