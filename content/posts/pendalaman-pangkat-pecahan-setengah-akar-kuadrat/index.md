---
weight: 1
title: "Mengapa a Pangkat Setengah Sama dengan Akar Kuadrat a? Pendalaman Pangkat Pecahan"
date: 2026-11-28T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman pangkat pecahan untuk kelas IX: membuktikan a pangkat setengah sama dengan akar kuadrat a lewat sifat perkalian pangkat, lalu menggunakannya untuk menghindari jebakan a pangkat setengah disangka a dibagi dua."
featuredImage: "featured-image.png"

tags: ["Bilangan Berpangkat", "Pendalaman", "Kelas IX"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas IX, setiap kali sampai di bilangan berpangkat, ada satu pertanyaan yang hampir selalu muncul dari bangku tengah. "Pak, pangkat itu kan artinya dikali berulang. Kalau pangkatnya setengah, dikalinya setengah kali? Bagaimana caranya?" Saya suka sekali pertanyaan itu, karena ia jujur: murid saya sedang memegang definisi pangkat yang sudah ia kenal — perkalian berulang — lalu mendapati definisi itu tidak bisa dipakai begitu saja untuk pangkat pecahan. Memang tidak bisa. Pangkat setengah tidak lahir dari definisi perkalian berulang. Ia lahir dari sebuah tuntutan: sifat-sifat pangkat yang sudah kita kenal harus tetap berlaku, apa pun pangkatnya.

<!--more-->

## Pangkat setengah lahir dari aturan, bukan dari hafalan

Sifat yang paling sering kita pakai adalah sifat perkalian pangkat: bilangan berpangkat yang dikalikan dengan bilangan berpangkat yang sama basisnya, pangkatnya dijumlahkan. Ditulis dengan rumus:

$$a^m \times a^n = a^{m+n}$$

Sifat ini sudah kita buktikan untuk pangkat bilangan bulat, dan kita memakainya setiap hari: $2^3 \times 2^2 = 2^5$, karena tiga faktor 2 ditambah dua faktor 2 menjadi lima faktor 2. Sekarang, mari kita menuntut sifat yang sama tetap berlaku untuk pangkat setengah. Apa jadinya bila $a^{1/2}$ dikalikan dengan dirinya sendiri?

$$a^{1/2} \times a^{1/2} = a^{1/2 + 1/2} = a^1 = a$$

Hasilnya $a$. Artinya, $a^{1/2}$ adalah bilangan yang bila dikalikan dengan dirinya sendiri menghasilkan $a$. Dan itu persis definisi akar kuadrat: $\sqrt{a}$ adalah bilangan yang kuadratnya sama dengan $a$. Karena itu, keduanya harus sama:

$$a^{1/2} = \sqrt{a}$$

Cobalah dengan angka. $9^{1/2} = 3$, karena $3 \times 3 = 9$. $25^{1/2} = 5$, karena $5 \times 5 = 25$. $16^{1/2} = 4$ dan $100^{1/2} = 10$. Tidak ada yang perlu dihafal di sini: pangkat setengah adalah nama lain dari akar kuadrat, dan nama itu diberikan oleh sifat pangkat itu sendiri, bukan oleh saya sebagai guru.

## Uji dengan sifat yang lain

Bukti yang baik adalah bukti yang tahan diuji dari arah lain. Mari kita uji kesamaan ini dengan sifat pangkat yang kedua, yaitu pangkat dari pangkat: $(a^m)^n = a^{m \times n}$. Bila $a^{1/2}$ memang sama dengan $\sqrt{a}$, maka mengkuadratkannya harus mengembalikan $a$:

$$\left(a^{1/2}\right)^2 = a^{1/2 \times 2} = a^1 = a$$

Benar. Dan $(\sqrt{a})^2 = a$ juga benar, sesuai definisi akar. Kedua jalan itu bertemu di tempat yang sama, dan itulah tanda sebuah kesamaan yang kokoh: ia tidak bergantung pada satu sifat saja.

Pola yang sama berlaku untuk pangkat sepertiga. Bila $a^{1/3}$ dikalikan dengan dirinya sendiri tiga kali, sifat perkalian pangkat berkata hasilnya $a^{1/3 + 1/3 + 1/3} = a^1 = a$. Jadi $a^{1/3}$ adalah bilangan yang bila dikalikan tiga kali menghasilkan $a$ — itulah akar pangkat tiga:

$$a^{1/3} = \sqrt[3]{a}$$

Contohnya: $8^{1/3} = 2$ karena $2 \times 2 \times 2 = 8$; $27^{1/3} = 3$; $125^{1/3} = 5$. Bahkan pangkat seperempat pun mengikuti pola yang sama: $81^{1/4} = 3$, karena $3 \times 3 \times 3 \times 3 = 81$. Secara umum, $a^{1/n}$ adalah akar pangkat $n$ dari $a$. Satu pola, banyak contoh — dan semuanya berasal dari satu sifat yang sama.

## Tiga jebakan yang sering muncul

Pertama, $a^{1/2}$ bukan $a$ dibagi dua. Ini jebakan yang paling sering saya temukan di lembar jawaban. $9^{1/2} = 3$, bukan $4,5$. Pangkat $1/2$ bukan perintah membagi bilangan itu menjadi dua; ia adalah perintah mencari bilangan yang kuadratnya sama dengan bilangan itu. Setiap kali ada murid yang menulis $9^{1/2} = 4,5$, saya memintanya memeriksa balik: apakah $4,5 \times 4,5$ sama dengan $9$? Tidak — hasilnya $20,25$. Pemeriksaan balik seperti ini murah dan ampuh, dan saya memakainya untuk hampir semua soal pangkat.

Kedua, $2^{1/2}$ bukan $1$. Murid kadang berpikir "setengah dari 2 adalah 1, jadi $2^{1/2} = 1$". Padahal $2^{1/2} = \sqrt{2}$, dan $\sqrt{2}$ kira-kira $1,414$ — bilangan yang kuadratnya $2$. Angka $1$ tidak lolos pemeriksaan balik, karena $1 \times 1 = 1$, bukan $2$. Di sinilah saya selalu mengingatkan: pangkat pecahan bukan setengah dari bilangannya, melainkan setengah dari "langkah" menuju bilangan itu lewat perkalian.

Ketiga, tanda negatif pada pangkat jangan dicampur dengan tanda negatif pada bilangan. $a^{-1/2}$ bukan $-\sqrt{a}$ dan bukan pula $\sqrt{-a}$. Sifat pangkat negatif berkata $a^{-m} = \frac{1}{a^m}$, sehingga:

$$a^{-1/2} = \frac{1}{a^{1/2}} = \frac{1}{\sqrt{a}}$$

Contohnya: $4^{-1/2} = \frac{1}{2}$, karena $\sqrt{4} = 2$; $9^{-1/2} = \frac{1}{3}$. Tanda minus di pangkat hanya membalik bilangan menjadi pecahan — ia tidak pernah mengubah bilangan di dalam akar menjadi negatif.

## Kegiatan lima menit di kelas

Untuk membuat pola ini melekat, saya memakai kartu pasangan. Di satu kartu saya tulis $16^{1/2}$, di kartu lain $4$; di satu kartu $27^{1/3}$, di kartu lain $3$; di satu kartu $81^{1/4}$, di kartu lain $3$ lagi — sengaja saya beri dua kartu yang jawabannya sama, supaya murid tidak bisa menebak dari sisa kartu. Murid memasangkan kartu-kartu itu di meja, lalu memeriksa pasangannya dengan cara yang sudah kita sepakati: kalikan jawaban itu dengan dirinya sendiri, apakah kembali ke bilangan semula? Lima menit, tanpa alat apa pun, dan pola $a^{1/n} = \sqrt[n]{a}$ biasanya sudah mereka ucapkan sendiri sebelum saya menulisnya di papan.

Ada satu pertanyaan penutup yang selalu saya lemparkan sebelum bel berbunyi: kalau $a^{1/2} = \sqrt{a}$, lalu $a^{2/3}$ sama dengan apa? Jawabannya mengikuti pola yang sama — $a^{2/3} = \left(a^{1/3}\right)^2 = \left(\sqrt[3]{a}\right)^2$ — tetapi saya sengaja tidak membahasnya tuntas hari itu. Biarlah menjadi pekerjaan rumah yang mereka bawa pulang dengan rasa penasaran, bukan dengan rasa takut. Karena pada akhirnya, pangkat pecahan mengajarkan satu hal yang lebih besar daripada rumusnya: dalam matematika, definisi baru tidak dibuat seenaknya — ia dibuat supaya aturan lama tetap berlaku.
