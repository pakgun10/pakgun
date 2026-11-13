---
weight: 1
title: "Anggota, Irisan, dan Gabungan: Latihan Soal Himpunan untuk Kelas VII"
date: 2026-11-13T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lembar latihan himpunan untuk kelas VII: empat soal tentang anggota, irisan, gabungan, selisih, dan soal cerita dua ekstrakurikuler dengan pembahasan langkah demi langkah, plus dua latihan mandiri beserta kuncinya."
featuredImage: "featured-image.png"

tags: ["Himpunan", "Kelas VII", "Latihan Soal"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VII saya, himpunan adalah bab yang kelihatannya paling gampang di awal semester — dan paling sering diremehkan. Anak-anak cepat hafal lambang $\in$ dan $\notin$, cepat menulis daftar anggota dengan kurung kurawal, lalu merasa bab ini sudah selesai. Masalahnya muncul begitu soalnya berubah bentuk: dua himpunan digabung, diiris, lalu dibungkus soal cerita tentang ekstrakurikuler. Di titik itu banyak anak yang tidak lagi tahu mana yang harus dihitung duluan.

Kesalahan yang paling sering saya lihat ada dua. Pertama, anak menghitung gabungan dengan menjumlahkan begitu saja banyak anggota kedua himpunan, tanpa mengurangi irisannya — anggota yang sama terhitung dua kali. Kedua, anak menganggap irisan dan gabungan itu soal yang sama, hanya beda nama. Padahal bedanya besar: irisan hanya mengambil yang dimiliki bersama, gabungan mengambil semuanya.

Karena itu lembar latihan di bawah ini saya susun berurutan: mulai dari anggota, lalu irisan dan gabungan, lalu selisih dan komplemen, dan ditutup soal cerita dua ekstrakurikuler. Empat soal dengan pembahasan, lalu dua latihan mandiri.

<!--more-->

## Sedikit yang perlu diingat sebelum mengerjakan

Himpunan ditulis dengan kurung kurawal, misalnya $A = \lbrace 2, 4, 6, 8 \rbrace$. Lambang $\in$ berarti anggota, $\notin$ berarti bukan anggota, dan $n(A)$ berarti banyak anggota himpunan $A$.

Untuk dua himpunan $A$ dan $B$, irisan $A \cap B$ berisi anggota yang ada di $A$ **dan** di $B$. Gabungan $A \cup B$ berisi semua anggota $A$ **atau** $B$. Banyak anggotanya dihitung dengan rumus yang wajib dihafal:

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

Pengurang di ujung rumus itulah yang paling sering dilupakan anak. Saya selalu mengingatkan: anggota irisan sudah dihitung di $n(A)$ dan dihitung lagi di $n(B)$. Kalau tidak dikurangi sekali, ia terhitung dua kali.

## Soal 1: anggota dan banyak anggota

Diketahui $P = \lbrace 3, 6, 9, 12, 15, 18 \rbrace$. Tentukan $n(P)$, lalu tentukan benar atau salah pernyataan berikut: (a) $9 \in P$, (b) $10 \in P$, (c) $21 \notin P$.

**Pembahasan.** Himpunan $P$ berisi enam bilangan, jadi $n(P) = 6$. Pernyataan (a) benar, karena $9$ memang ada di daftar anggota $P$. Pernyataan (b) salah, karena $10$ tidak ada di dalam $P$ — yang benar adalah $10 \notin P$. Pernyataan (c) benar, karena $21$ memang tidak ada di $P$.

Jebakannya ada di (b): anak yang terburu-buru membaca $10$ sebagai kelipatan $3$ berikutnya setelah $9$, padahal kelipatan $3$ setelah $9$ adalah $12$. Himpunan tidak peduli pada pola yang kita kira — yang dihitung hanya apa yang tertulis di dalam kurung kurawal.

## Soal 2: irisan dan gabungan dua himpunan

Diketahui $A = \lbrace 1, 2, 3, 5, 7 \rbrace$ dan $B = \lbrace 2, 3, 5, 8, 10 \rbrace$. Tentukan $A \cap B$ dan $A \cup B$, lalu hitung $n(A \cup B)$ dengan rumus.

**Pembahasan.** Irisan mengambil anggota yang sama di kedua himpunan: $A \cap B = \lbrace 2, 3, 5 \rbrace$, jadi $n(A \cap B) = 3$. Gabungan mengambil semua anggota tanpa menulis dua kali yang sama: $A \cup B = \lbrace 1, 2, 3, 5, 7, 8, 10 \rbrace$, jadi $n(A \cup B) = 7$.

Dengan rumus: $n(A) = 5$ dan $n(B) = 5$, maka $n(A \cup B) = 5 + 5 - 3 = 7$. Hasilnya sama dengan cara mendaftar. Saya sengaja meminta anak menghitung dengan dua cara ini, supaya mereka percaya pada rumusnya — dan supaya mereka tahu kapan rumusnya menyelamatkan mereka, yaitu ketika anggotanya terlalu banyak untuk didaftar satu per satu.

## Soal 3: selisih dan komplemen

Diketahui semesta $U = \lbrace 1, 2, 3, \dots, 20 \rbrace$, $A$ himpunan bilangan genap, dan $B$ himpunan kelipatan $3$. Tentukan $A - B$, $B - A$, dan $A^c$.

**Pembahasan.** Pertama daftarkan anggotanya: $A = \lbrace 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 \rbrace$ dan $B = \lbrace 3, 6, 9, 12, 15, 18 \rbrace$.

Selisih $A - B$ berisi anggota $A$ yang **tidak** ada di $B$: $A - B = \lbrace 2, 4, 8, 10, 14, 16, 20 \rbrace$. Sebaliknya $B - A = \lbrace 3, 9, 15 \rbrace$. Irisannya sendiri adalah $A \cap B = \lbrace 6, 12, 18 \rbrace$ — bilangan genap yang sekaligus kelipatan $3$.

Komplemen $A^c$ berisi semua anggota semesta yang bukan anggota $A$, yaitu bilangan ganjil dari $1$ sampai $20$: $A^c = \lbrace 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 \rbrace$.

Kesalahan yang sering muncul di sini adalah anak menulis $A - B$ sama dengan $B - A$. Saya selalu menekankan: selisih tidak bisa dibalik, seperti pengurangan biasa. $10 - 4$ tidak sama dengan $4 - 10$, dan $A - B$ tidak sama dengan $B - A$.

## Soal 4: soal cerita dua ekstrakurikuler

Di kelas VII-A ada $35$ siswa. Sebanyak $20$ siswa mengikuti sepak bola, $18$ siswa mengikuti pramuka, dan $8$ siswa mengikuti keduanya. Berapa siswa yang hanya mengikuti sepak bola, berapa yang hanya mengikuti pramuka, dan berapa yang tidak mengikuti keduanya?

**Pembahasan.** Saya selalu menggambar dua lingkaran beririsan di papan tulis untuk soal seperti ini, lalu mengisi dari tengah. Yang mengikuti keduanya ada $8$ siswa — itu irisannya, ditulis di tengah.

Yang hanya sepak bola: $20 - 8 = 12$ siswa. Yang hanya pramuka: $18 - 8 = 10$ siswa. Jadi yang mengikuti paling tidak satu kegiatan ada $12 + 10 + 8 = 30$ siswa. Sisanya tidak mengikuti keduanya: $35 - 30 = 5$ siswa.

Cara cepatnya dengan rumus gabungan: $n(A \cup B) = 20 + 18 - 8 = 30$, lalu yang tidak ikut keduanya adalah $35 - 30 = 5$. Anak yang menjawab $20 + 18 = 38$ siswa mengikuti kegiatan — lebih banyak dari jumlah siswa di kelas — langsung ketahuan lupa mengurangi irisan. Angka yang mustahil itu justru bagus: ia memberi tahu kita sendiri bahwa ada langkah yang terlewat.

## Latihan mandiri

**Latihan 1.** Di kelas VII-B ada $40$ siswa. Sebanyak $24$ siswa gemar voli, $20$ siswa gemar basket, dan $12$ siswa gemar keduanya. Berapa siswa yang hanya gemar voli, berapa yang hanya gemar basket, dan berapa yang tidak gemar keduanya?

**Latihan 2.** Diketahui $U = \lbrace 1, 2, 3, \dots, 12 \rbrace$, $P$ himpunan bilangan prima, dan $Q$ himpunan kelipatan $4$. Tentukan $P \cap Q$, $P \cup Q$, dan $n(P \cup Q)$.

**Kunci.** Latihan 1: hanya voli $12$ siswa, hanya basket $8$ siswa, tidak gemar keduanya $8$ siswa. Latihan 2: $P \cap Q = \lbrace \rbrace$ (himpunan kosong), $P \cup Q = \lbrace 2, 3, 4, 5, 7, 8, 11, 12 \rbrace$, $n(P \cup Q) = 8$.

## Penutup

Himpunan terasa mudah karena lambangnya sedikit, tetapi ketelitian yang dimintanya tidak sedikit. Anak yang rajin menggambar dua lingkaran beririsan sebelum menghitung hampir tidak pernah salah di soal cerita — gambar itu memaksa mereka mengisi irisan dulu, baru yang lain. Sebaliknya anak yang langsung menjumlahkan angka di soal hampir selalu lupa menguranginya.

Kalau satu hal yang saya harapkan tertinggal dari lembar ini, itu adalah kebiasaan memeriksa jawaban dengan akal sehat: jumlah bagian-bagiannya harus sama dengan jumlah seluruhnya, dan tidak ada bagian yang lebih besar dari keseluruhannya. Kalau hitungan itu tidak klop, bukan soalnya yang salah — ada langkah yang terlewat, dan langkah itu hampir selalu irisan.
