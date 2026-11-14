---
weight: 1
title: "Mengapa Luas Trapesium Setengah Jumlah Sisi Sejajar Kali Tinggi? Pendalaman dari Dua Trapesium yang Menjadi Jajar Genjang"
date: 2026-11-14T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman luas trapesium untuk murid yang penasaran: membuktikan rumus (a + b) / 2 × t lewat dua trapesium yang digabung menjadi jajar genjang, lalu menggunakannya untuk mencari sisi dan tinggi yang belum diketahui."
featuredImage: "featured-image.png"

tags: ["Trapesium", "Pendalaman", "Geometri", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Kemarin, saat latihan menghitung luas bangun datar, seorang murid kelas VIII menatap papan tulis lama sekali. Di sana tertulis rumus luas trapesium: $L = \frac{a + b}{2} \times t$. "Pak," katanya, "kenapa trapesium pakai setengah dan pakai jumlah dua sisi? Persegi panjang kan cukup alas kali tinggi. Kenapa trapesium ribet sendiri?" Saya tersenyum, karena pertanyaan itu tepat sekali. Rumus trapesium memang terlihat lebih ribet daripada rumus persegi panjang atau jajar genjang, dan justru karena itu ia menyimpan cerita yang bagus. Hari ini saya ingin mengajak Anda mengikuti cerita itu — dan kabar baiknya, cerita ini bisa dibuktikan dengan gunting dan kertas, tanpa menghafal apa pun.

<!--more-->

## Dua trapesium yang digabung menjadi jajar genjang

Ambil selembar kertas, gambar sebuah trapesium, lalu gunting. Sebut sisi sejajar yang atas $a$ dan sisi sejajar yang bawah $b$, dan jarak tegak lurus antara kedua sisi itu adalah tingginya, $t$. Sekarang gambar satu lagi yang persis sama, lalu putar trapesium kedua 180 derajat dan tempelkan ke sisi miring trapesium yang pertama. Apa yang terjadi? Dua trapesium itu bergabung menjadi satu jajar genjang.

Perhatikan jajar genjang hasil gabungan itu. Alasnya adalah $a + b$ — sisi atas trapesium pertama bersambung dengan sisi bawah trapesium kedua yang sudah diputar, begitu pula sebaliknya. Tingginya tetap $t$, karena jarak antara kedua sisi sejajar tidak berubah. Maka luas jajar genjang itu adalah $(a + b) \times t$.

Tetapi jajar genjang itu terdiri dari dua trapesium yang sama besar. Maka luas satu trapesium pastilah setengahnya:

$$L = \frac{a + b}{2} \times t$$

Di sinilah asal "setengah" dan "jumlah dua sisi" itu: setengah karena satu trapesium hanya separuh dari jajar genjang gabungan, dan jumlah dua sisi karena alas jajar genjang itu tersusun dari kedua sisi sejajar. Bukan aturan yang dibuat-buat — melainkan akibat dari bentuknya sendiri.

## Coba dengan angka

Ambil trapesium dengan $a = 8$ cm, $b = 5$ cm, dan $t = 4$ cm. Jumlah sisi sejajarnya $8 + 5 = 13$, setengahnya $6{,}5$, lalu dikali tinggi 4:

$$L = \frac{8 + 5}{2} \times 4 = 6{,}5 \times 4 = 26 \text{ cm}^2$$

Coba satu lagi, $a = 10$ cm, $b = 6$ cm, $t = 5$ cm:

$$L = \frac{10 + 6}{2} \times 5 = 8 \times 5 = 40 \text{ cm}^2$$

Rumus ini juga bisa dibalik. Misalkan luas sebuah trapesium $54 \text{ cm}^2$, sisi sejajarnya $12$ cm dan $6$ cm, berapakah tingginya? Masukkan ke rumus: $54 = \frac{12 + 6}{2} \times t$, sehingga $54 = 9t$, dan $t = 6$ cm. Atau dibalik ke arah lain: luas $35 \text{ cm}^2$, tinggi $5$ cm, satu sisi sejajar $4$ cm, berapa sisi sejajar yang lain? $35 = \frac{a + 4}{2} \times 5$, maka $\frac{a + 4}{2} = 7$, sehingga $a + 4 = 14$ dan $a = 10$ cm. Satu rumus, tiga arah — asalkan kita tahu mana yang dicari, sisanya tinggal membalik.

## Dua jebakan yang sering muncul

Jebakan pertama: memakai kaki trapesium sebagai tinggi. Kaki adalah sisi miring trapesium, sedangkan tinggi adalah jarak tegak lurus antara kedua sisi sejajar. Keduanya hanya sama pada trapesium siku-siku. Ambil trapesium sama kaki dengan sisi sejajar $6$ cm dan $10$ cm, kaki $5$ cm, tetapi tinggi $4$ cm. Luas yang benar adalah $\frac{6 + 10}{2} \times 4 = 32 \text{ cm}^2$, bukan $\frac{6 + 10}{2} \times 5 = 40 \text{ cm}^2$. Murid yang tergesa-gesa sering mengambil angka 5 itu karena terlihat "lebih siap dipakai" — padahal tinggi harus selalu tegak lurus, dan itulah yang membuat angka 4 yang benar.

Jebakan kedua: lupa membagi dua. Hasil $(a + b) \times t$ itu luas jajar genjang gabungan, bukan luas trapesiumnya. Pada contoh pertama di atas, $13 \times 4 = 52$ adalah luas dua trapesium — dan jawaban $52 \text{ cm}^2$ untuk satu trapesium jelas kebesaran. Cara cepat memeriksanya: bila kedua sisi sejajar sama panjang, katakanlah $a = b = 7$ cm dan $t = 4$ cm, trapesium itu berubah menjadi jajar genjang, dan rumusnya memberi $\frac{7 + 7}{2} \times 4 = 28 \text{ cm}^2$, persis sama dengan $7 \times 4$. Rumus yang benar harus tetap benar pada kasus batas seperti ini — dan rumus trapesium lolos ujian itu.

## Penutup: rumus yang dipahami tidak perlu dihafal

Esok, bila ada murid yang bertanya lagi mengapa rumus trapesium memakai setengah dan jumlah dua sisi, saya tidak akan langsung menulis rumusnya di papan. Saya akan membagikan kertas, meminta mereka menggunting dua trapesium yang sama, memutar satu dan menempelkannya ke yang lain, lalu bertanya: bangun apa yang terbentuk, dan berapa alasnya? Begitu mereka melihat sendiri jajar genjang itu terbentuk, rumus $L = \frac{a + b}{2} \times t$ bukan lagi hafalan — melainkan ringkasan dari sesuatu yang sudah mereka pegang dengan tangan. Dan rumus yang dipahami seperti itu, menurut pengalaman saya, jauh lebih lama tinggalnya daripada rumus yang sekadar dicatat.
