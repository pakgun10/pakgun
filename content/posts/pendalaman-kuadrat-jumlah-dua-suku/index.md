---
weight: 1
title: "Mengapa (a + b)² Bukan a² + b²? Pendalaman Kuadrat Jumlah Dua Suku"
date: 2026-11-07T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman aljabar untuk kelas VIII: membongkar mengapa (a + b)² tidak sama dengan a² + b² lewat persegi yang dipotong, memeriksa dengan angka, dan dua jebakan yang paling sering muncul di soal."
featuredImage: "featured-image.png"

tags: ["Kuadrat Jumlah", "Aljabar", "Pendalaman", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VIII saya minggu ini, saya menulis $(a + b)^2$ di papan tulis lalu bertanya, "Ini sama dengan apa?" Hampir seluruh kelas menjawab serempak, " $a^2 + b^2$, Pak!" Jawabannya keluar begitu cepat dan yakin, sampai saya sempat ragu untuk membantahnya. Saya pun menulis angka di bawahnya: $a = 2$ dan $b = 3$. "Coba hitung," kata saya. Sisi kiri, $(2 + 3)^2 = 5^2 = 25$. Sisi kanan, $2^2 + 3^2 = 4 + 9 = 13$. Kelas mendadak hening. Dua puluh lima tidak sama dengan tiga belas. Ada sesuatu yang hilang di tengah jalan, dan hari itu kami sepakat mencarinya bersama-sama.

Artikel ini adalah pendalaman dari latihan aljabar yang sudah kita kerjakan sebelumnya. Kalau kemarin kita berlatih menghitung, hari ini kita mencari tahu mengapa jawaban yang tampak masuk akal itu ternyata salah, dan apa yang sebenarnya terjadi di dalam tanda kurung itu.

<!--more-->

## Jebakan yang tampak masuk akal

Mengapa jawaban $a^2 + b^2$ terasa begitu benar? Karena pola pikirnya meniru sesuatu yang memang benar. Kita sudah hafal bahwa $2 \times (a + b) = 2a + 2b$: pengali di luar kurung masuk dan mengenai setiap suku di dalamnya. Otak kita lalu menarik kesimpulan yang sama untuk pangkat: pangkat di luar kurung pasti masuk dan mengenai setiap suku juga. Sayangnya, perkalian dan pemangkatan tidak bekerja dengan cara yang sama.

Pangkat dua itu bukan perintah "pangkatkan setiap suku", melainkan perintah "kalikan bentuk itu dengan dirinya sendiri". $(a + b)^2$ artinya $(a + b) \times (a + b)$, dan perkalian dua jumlah ini tidak bisa diselesaikan dengan membagikan pangkat ke dalam. Begitu murid melihat tulisan $(a + b)(a + b)$, sebagian dari mereka mulai curiga: ada perkalian silang yang belum dihitung. Kecurigaan itu tepat. Yang hilang itu bersembunyi di persilangan tersebut.

## Bukti dari selembar kertas: persegi besar

Cara paling jujur untuk melihat yang hilang itu adalah dengan menggambar. Saya menggambar sebuah persegi besar dengan sisi $(a + b)$ di papan tulis. Luasnya tentu saja $(a + b)^2$. Lalu saya memotong sisi persegi itu menjadi dua bagian, $a$ dan $b$, dan menarik garis pemotong ke dalam sehingga persegi besar itu terbelah menjadi empat potong.

Potong pertama adalah persegi kecil bersisi $a$, luasnya $a^2$. Potong kedua adalah persegi kecil bersisi $b$, luasnya $b^2$. Lalu ada dua potong lagi, keduanya persegi panjang berukuran $a \times b$. Dua potong inilah yang hilang dari jawaban kelas tadi. Luas persegi besar itu ternyata $a^2 + ab + ab + b^2$, atau $a^2 + 2ab + b^2$. Suku $2ab$ itulah yang selama ini tidak ikut terhitung.

Saya meminta murid membayangkan persegi itu sebagai halaman rumah. Bagian $a^2$ adalah rumahnya, bagian $b^2$ adalah kebun kecilnya, dan dua persegi panjang $ab$ adalah teras di depan dan di samping. Kalau terasnya tidak dihitung, luas halaman yang dilaporkan pasti kurang. Tidak ada yang salah dengan $a^2$ dan $b^2$; yang salah adalah mengira keduanya sudah mencakup seluruh halaman. Begitu gambar ini terlihat, jawaban $a^2 + b^2$ kehilangan pesonanya. Ia bukan jawaban yang salah total, ia hanya jawaban yang tidak lengkap.

## Cek dengan angka

Penjelasan yang bagus harus tahan diuji angka. Ambil $a = 2$ dan $b = 3$ seperti di awal pelajaran. Rumus lengkapnya memberi $(2 + 3)^2 = 2^2 + 2 \times 2 \times 3 + 3^2 = 4 + 12 + 9 = 25$. Sama persis dengan $5^2$. Suku yang hilang itu, $2ab = 12$, adalah selisih antara 25 dan 13, dan sekarang kita tahu dari mana asalnya.

Contoh kedua, $a = 5$ dan $b = 1$. Sisi kiri, $(5 + 1)^2 = 36$. Rumus lengkapnya, $25 + 2 \times 5 \times 1 + 1 = 25 + 10 + 1 = 36$. Cocok lagi. Perhatikan bahwa $2ab$ di sini hanya 10, jauh lebih kecil daripada $a^2$ yang 25. Makin kecil salah satu suku, makin kecil pula suku yang hilang, dan makin mudah kita tertipu mengira $a^2 + b^2$ sudah cukup. Ketika $b$ kecil, jawabannya memang nyaris benar, dan justru di situlah jebakannya: kesalahan kecil yang nyaris tidak terasa adalah kesalahan yang paling lama bertahan.

## Rumus lengkapnya, dan kembarannya

Setelah pembuktian gambar dan angka, rumus lengkapnya boleh ditulis dengan tenang: $(a + b)^2 = a^2 + 2ab + b^2$. Saya menyuruh murid menghafal bentuk ini bukan sebagai baris baru, melainkan sebagai gambar: satu persegi besar, satu persegi kecil, dan dua persegi panjang. Rumus yang punya gambar di kepala jauh lebih sulit dilupakan daripada rumus yang hanya dihafal bunyinya.

Rumus ini punya kembaran yang lahir dari gambar yang sama. Kalau tandanya minus, $(a - b)^2 = a^2 - 2ab + b^2$. Cek dengan $a = 5$ dan $b = 2$: sisi kiri $(5 - 2)^2 = 9$, sisi kanan $25 - 20 + 4 = 9$. Cocok. Jebakan di sini kebalikannya: murid yang sudah hafal rumus plus kadang menulis $(a - b)^2 = a^2 - 2ab - b^2$, dengan tanda minus juga pada $b^2$. Padahal $b^2$ selalu positif, karena kuadrat bilangan apa pun tidak pernah negatif. Gambarnya membantu lagi: persegi kecil $b^2$ tetap ada sebagai luas, tidak peduli tandanya plus atau minus.

## Kegiatan: gunting empat potong kertas

Kalau ada waktu sepuluh menit di akhir pelajaran, saya menyuruh murid menggunting satu persegi kertas, lalu membaginya menjadi empat potong seperti gambar di papan: dua persegi kecil dan dua persegi panjang. Mereka menamai setiap potong dengan luasnya, $a^2$, $b^2$, $ab$, dan $ab$, lalu menyusunnya kembali menjadi persegi besar. Tidak perlu rapi. Yang penting mereka melihat sendiri bahwa keempat potong itu harus ada semua; kalau satu persegi panjang disembunyikan, persegi besarnya tidak akan utuh.

Hampir selalu ada yang berseru, "Lho, Pak, ternyata memang kurang satu!" Seruan itulah yang saya tunggu. Kesalahan yang ditemukan sendiri dengan gunting dan kertas jauh lebih lama tinggalnya daripada kesalahan yang dikoreksi dengan coretan merah di buku latihan.

$(a + b)^2$ akhirnya bukan lagi sekadar baris di buku catatan. Ia adalah cerita tentang satu persegi besar yang terdiri dari empat potong, dan tentang jawaban yang tampak masuk akal tetapi tidak lengkap. Dan setiap kali murid menulis $a^2 + 2ab + b^2$ setelah hari itu, saya berharap mereka ingat sejenak potongan kertas di meja mereka, bukan sekadar huruf-huruf yang harus dihafal sebelum ulangan.
