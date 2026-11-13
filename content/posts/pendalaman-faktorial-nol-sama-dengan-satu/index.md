---
weight: 1
title: "Mengapa 0! Sama dengan 1? Pendalaman Faktorial Nol"
date: 2026-11-14T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman faktorial nol untuk murid yang penasaran: mengikuti pola 4!, 3!, 2!, 1! ke bawah, memahami perkalian kosong, dan melihat mengapa rumus kombinasi mengharuskan 0! sama dengan 1."
featuredImage: "featured-image.png"

tags: ["Faktorial", "Pendalaman", "Bilangan", "Kelas IX"]
categories: ["Matematika"]

math:
  enable: true
---

Sepulang sekolah minggu lalu, seorang murid kelas IX menghampiri saya dengan pertanyaan titipan kakaknya yang sudah SMA. "Pak, kakak saya bilang $0! = 1$. Padahal kalau $3! = 3 \times 2 \times 1 = 6$, mestinya $0!$ itu tidak ada yang dikalikan, jadi jawabannya nol, kan?" Saya tersenyum. Pertanyaan itu persis pertanyaan yang dulu juga mengganggu saya waktu pertama kali bertemu tanda seru ini. Faktorial memang tidak ada di materi SMP, tetapi pertanyaan "mengapa" seperti ini justru yang paling layak dikejar. Jawabannya bukan sekadar "memang begitu aturannya", melainkan satu-satunya nilai yang membuat semua pola tetap konsisten. Mari kita turun anak tangga demi anak tangga.

<!--more-->

## Turun satu anak tangga demi satu anak tangga

Faktorial sebuah bilangan adalah hasil kali bilangan itu dengan semua bilangan asli di bawahnya, sampai ke satu. Jadi $4! = 4 \times 3 \times 2 \times 1 = 24$, $3! = 3 \times 2 \times 1 = 6$, $2! = 2 \times 1 = 2$, dan $1! = 1$.

Sekarang perhatikan polanya dari atas ke bawah. Dari $4!$ ke $3!$, hasilnya dibagi $4$: $24 : 4 = 6$. Dari $3!$ ke $2!$, hasilnya dibagi $3$: $6 : 3 = 2$. Dari $2!$ ke $1!$, hasilnya dibagi $2$: $2 : 2 = 1$. Setiap kali turun satu anak tangga, kita membagi dengan bilangan yang kita lewati.

Kalau pola ini diteruskan satu langkah lagi, dari $1!$ ke $0!$ kita membagi dengan $1$: $1 : 1 = 1$. Jadi $0! = 1$. Bukan karena ada yang memutuskan begitu, melainkan karena itulah satu-satunya angka yang membuat tangga ini tidak patah. Kalau kita memaksakan $0! = 0$, pola pembagian itu langsung rusak: $1 : 1$ tidak mungkin menghasilkan $0$.

## Kalau tidak ada yang dikalikan, hasilnya satu

Murid saya tadi beralasan, "Tidak ada yang dikalikan, jadi hasilnya nol." Alasan ini terdengar masuk akal, tetapi keliru pada satu hal: dalam perkalian, "tidak ada" bukan berarti nol. Nol adalah hasil dari penjumlahan kosong, sedangkan hasil dari perkalian kosong adalah satu.

Bayangkan saya meminta murid mengalikan semua bilangan dalam sebuah kotak. Kalau kotaknya berisi $3$ dan $4$, hasilnya $12$. Kalau kotaknya berisi $5$ saja, hasilnya $5$. Kalau kotaknya kosong, tidak ada bilangan yang mengubah hasil — dan bilangan yang tidak mengubah hasil kali adalah $1$, karena $1 \times$ apa pun sama dengan bilangan itu sendiri. Itulah yang disebut identitas perkalian, sama seperti $0$ adalah identitas penjumlahan: $0 +$ apa pun sama dengan bilangan itu sendiri.

Pola yang sama muncul pada pangkat. Perhatikan $5^3 = 125$, $5^2 = 25$, $5^1 = 5$. Setiap turun satu pangkat, hasilnya dibagi $5$. Satu langkah lagi: $5^0 = 5 : 5 = 1$. Pangkat nol pun sama dengan satu, dengan alasan yang sama persis: itulah nilai yang menjaga pola tetap utuh.

## Bukti dari kombinasi: memilih nol dari lima

Alasan ketiga datang dari kombinasi, dan inilah yang paling meyakinkan saya. Ada berapa cara memilih nol buah kelereng dari lima kelereng? Hanya satu cara: tidak mengambil apa-apa. Jadi $C(5, 0) = 1$.

Rumus kombinasi sendiri adalah $C(n, k) = \frac{n!}{k!(n-k)!}$. Masukkan $n = 5$ dan $k = 0$:

$$C(5, 0) = \frac{5!}{0! \cdot 5!} = \frac{1}{0!}$$

Di ruas kiri kita tahu jawabannya $1$, karena memang hanya ada satu cara memilih tidak satu pun. Supaya ruas kanan juga sama dengan $1$, penyebutnya harus $1$. Artinya $0! = 1$. Kalau $0!$ bernilai $0$, rumusnya pecah: kita membagi dengan nol, dan seluruh teori kombinasi runtuh. Matematikawan tidak memilih $0! = 1$ karena malas; mereka memilihnya karena rumus-rumus lain menuntut nilai itu.

## Dua jebakan yang sering muncul

Jebakan pertama adalah mengira $0! = 0$ karena "nol kali apa pun sama dengan nol". Padahal pada $0!$ tidak ada perkalian dengan nol yang terjadi. Tidak ada faktor nol di dalamnya. Yang ada hanyalah kekosongan, dan kekosongan dalam perkalian bernilai satu.

Jebakan kedua adalah mengira $0!$ tidak terdefinisi, seperti pembagian dengan nol. Ini juga keliru. Pembagian dengan nol tidak terdefinisi karena tidak ada bilangan yang bisa mengembalikan pembagian itu. Faktorial nol justru terdefinisi dengan rapi, karena tiga jalur berbeda — pola tangga, perkalian kosong, dan rumus kombinasi — semuanya tiba di angka yang sama: satu.

## Kegiatan singkat: menghitung susunan

Di kelas, saya mengajak murid menghitung susunan huruf. Dari tiga huruf A, B, dan C, ada $3! = 6$ susunan: ABC, ACB, BAC, BCA, CAB, CBA. Dari dua huruf A dan B, ada $2! = 2$ susunan. Dari satu huruf A, ada $1! = 1$ susunan. Lalu dari nol huruf, ada berapa susunan? Ada satu: susunan kosong. Tidak ada huruf yang bisa disusun, tetapi keadaan "tidak ada susunan" itu sendiri tetap terhitung satu keadaan. Murid biasanya tertawa mendengar ini, tetapi justru di situlah letak keindahannya: kekosongan pun terhitung.

Jadi, $0! = 1$ bukan kesepakatan asal-asalan dan bukan hafalan yang harus ditelan mentah-mentah. Ia adalah satu-satunya nilai yang menjaga tiga hal sekaligus: pola tangga faktorial tetap utuh, perkalian kosong tetap bermakna, dan rumus kombinasi tetap bekerja. Kalau lain kali ada yang bertanya mengapa, jangan jawab "memang begitu". Ajak ia turun satu anak tangga, lalu biarkan polanya yang menjawab.
