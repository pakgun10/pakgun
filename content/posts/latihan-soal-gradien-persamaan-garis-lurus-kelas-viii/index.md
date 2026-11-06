---
weight: 1
title: "Miring ke Mana? Latihan Soal Gradien dan Persamaan Garis Lurus untuk Kelas VIII"
date: 2026-11-06T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lembar latihan soal gradien dan persamaan garis lurus untuk kelas VIII: empat soal dengan pembahasan langkah demi langkah — gradien dua titik, persamaan garis, garis tegak lurus, dan titik potong sumbu — plus dua latihan mandiri beserta kuncinya."
featuredImage: "featured-image.png"

tags: ["Gradien", "Persamaan Garis Lurus", "Soal Latihan", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Suatu hari saya menggambar sebuah garis miring di papan tulis, lalu bertanya, "Gradien garis ini berapa?" Seorang murid menjawab dengan yakin, "Naik dua, geser satu, Pak." Saya tanya balik, "Naiknya yang mana, gesernya yang mana?" Ia menunjuk ke kanan, lalu ke atas, lalu ragu. Jawabannya benar setengah: ia tahu garis itu naik, tetapi ia belum tahu angka mana yang dibagi angka mana. Di situlah saya sadar, gradien jarang gagal karena rumusnya sulit — rumusnya cuma satu baris. Yang membuat murid salah adalah arah: mana yang naik, mana yang geser, dan mana yang harus di atas.

Gradien itu bahasa sederhananya kemiringan: kalau kita berjalan satu langkah ke kanan, berapa langkah kita naik atau turun? Angka itu yang menentukan apakah garisnya menanjak, menurun, datar, atau tegak. Empat soal di bawah ini saya susun supaya murid merasakan sendiri arti angka itu, bukan sekadar menghafal rumusnya, lalu dua latihan mandiri di akhir dengan kuncinya.

<!--more-->

## Apa itu gradien, dan mengapa tandanya penting

Sebelum masuk ke soal, saya menulis satu rumus di papan: $m = \dfrac{\Delta y}{\Delta x}$, dibaca "perubahan $y$ dibagi perubahan $x$". Kalau sebuah garis melalui dua titik $(x_1, y_1)$ dan $(x_2, y_2)$, maka $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.

Tanda gradien itu bercerita. Gradien positif berarti garis menanjak ke kanan — makin ke kanan, makin tinggi. Gradien negatif berarti garis menurun ke kanan. Gradien nol berarti garisnya datar, dan garis tegak tidak punya gradien sama sekali. Saya selalu minta murid menebak dulu tandanya sebelum menghitung: "Garisnya naik atau turun?" Tebakan itu sering menyelamatkan mereka dari jawaban yang kebalik tanda.

## Soal 1: gradien dari dua titik

Tentukan gradien garis yang melalui titik $A(2, 3)$ dan $B(6, 11)$.

**Pembahasan.** Ambil $A$ sebagai titik pertama dan $B$ sebagai titik kedua. Perubahan $y$ adalah $11 - 3 = 8$, perubahan $x$ adalah $6 - 2 = 4$. Maka

$$m = \frac{11 - 3}{6 - 2} = \frac{8}{4} = 2.$$

Artinya, setiap kita berjalan 1 langkah ke kanan, garis ini naik 2 langkah. Jebakan yang paling sering muncul di soal ini adalah mengurangkan secara terbalik: $3 - 11$ di atas dan $2 - 6$ di bawah. Hasilnya tetap $2$ karena dua tanda negatif saling menghapus, tetapi kalau hanya satu yang terbalik — misalnya $11 - 3$ di atas dan $2 - 6$ di bawah — jawabannya jadi $-2$, dan garis yang menanjak tiba-tiba ditulis menurun. Aturan saya: kurangkan dengan urutan yang sama di atas dan di bawah, dan selalu mulai dari titik yang sama.

## Soal 2: persamaan garis dari satu titik dan gradien

Tentukan persamaan garis yang melalui titik $(1, 5)$ dan bergradien $3$.

**Pembahasan.** Kita pakai bentuk titik-gradien: $y - y_1 = m(x - x_1)$. Masukkan $x_1 = 1$, $y_1 = 5$, dan $m = 3$:

$$y - 5 = 3(x - 1).$$

Kalikan ruas kanan: $y - 5 = 3x - 3$. Pindahkan $-5$ ke kanan: $y = 3x + 2$. Jadi persamaan garisnya $y = 3x + 2$.

Saya selalu minta murid menguji jawabannya: masukkan $x = 1$ ke $y = 3x + 2$, hasilnya $y = 5$ — tepat titik yang diketahui. Kalau tidak cocok, pasti ada yang salah di tengah jalan. Uji satu titik ini cuma butuh lima detik, tetapi menyelamatkan banyak jawaban. Perhatikan juga angka $2$ di ujung persamaan: itulah titik potong garis dengan sumbu $Y$, karena saat $x = 0$, $y = 2$.

## Soal 3: garis yang tegak lurus

Diketahui garis $g: 2x + 3y = 12$. Tentukan persamaan garis yang tegak lurus $g$ dan melalui titik $(0, 4)$.

**Pembahasan.** Pertama, cari gradien garis $g$. Ubah ke bentuk $y = mx + c$: $3y = -2x + 12$, sehingga $y = -\frac{2}{3}x + 4$. Jadi gradien $g$ adalah $m_1 = -\frac{2}{3}$.

Dua garis tegak lurus kalau hasil kali gradiennya $-1$, jadi gradien garis yang dicari adalah kebalikan negatif dari $-\frac{2}{3}$, yaitu $m_2 = \frac{3}{2}$. Garis itu melalui $(0, 4)$, jadi langsung tulis $y = \frac{3}{2}x + 4$.

Jebakan di soal ini ada dua. Pertama, murid sering menulis gradien garis yang tegak lurus sama dengan gradien garis asalnya — padahal gradien yang sama itu syarat garis **sejajar**, bukan tegak lurus. Kedua, membalik pecahan tanpa membalik tanda: kebalikan dari $-\frac{2}{3}$ bukan $-\frac{3}{2}$, melainkan $\frac{3}{2}$. Saya mengajarkan cara mengingatnya: "balik pecahannya, balik tandanya." Kalau salah satunya tertinggal, jawabannya pasti meleset.

## Soal 4: titik potong dengan sumbu

Tentukan titik potong garis $y = -2x + 8$ dengan sumbu $X$ dan sumbu $Y$.

**Pembahasan.** Titik potong dengan sumbu $X$ adalah titik yang $y$-nya nol. Masukkan $y = 0$: $0 = -2x + 8$, sehingga $2x = 8$ dan $x = 4$. Titik potongnya $(4, 0)$.

Titik potong dengan sumbu $Y$ adalah titik yang $x$-nya nol. Masukkan $x = 0$: $y = 8$. Titik potongnya $(0, 8)$.

Jebakan klasik di sini adalah tertukar: murid memasukkan $x = 0$ untuk mencari potong sumbu $X$, atau sebaliknya. Cara saya menghindarinya: ucapkan dulu, "Di sumbu $X$, $y$-nya nol; di sumbu $Y$, $x$-nya nol." Kalimat itu diulang sampai jadi kebiasaan, karena soal titik potong akan muncul lagi di bab fungsi, di SPLDV, dan di grafik apa pun.

## Latihan mandiri

Coba kerjakan sendiri, lalu cocokkan dengan kunci di bawah.

**1.** Tentukan gradien garis yang melalui titik $(-1, 4)$ dan $(3, -4)$.

**2.** Tentukan persamaan garis yang melalui titik $(2, -3)$ dan bergradien $-4$.

**Kunci:** 1. $m = -2$; 2. $y = -4x + 5$.

Soal pertama latihan mandiri sengaja memakai bilangan negatif, karena di situlah murid paling sering salah tanda: $m = \frac{-4 - 4}{3 - (-1)} = \frac{-8}{4} = -2$. Soal kedua menguji ketelitian saat mengalikan bilangan negatif: $y + 3 = -4(x - 2)$, sehingga $y = -4x + 8 - 3 = -4x + 5$.

Gradien bukan sekadar angka di depan $x$. Ia adalah cerita tentang arah: ke mana garis itu pergi setiap kali kita melangkah ke kanan. Kalau murid sudah bisa membaca cerita itu — naik atau turun, curam atau landai, sejajar atau tegak lurus — maka persamaan garis berhenti menjadi hafalan dan mulai menjadi gambar yang bisa mereka bayangkan. Dan gambar yang bisa dibayangkan, biasanya tidak mudah dilupakan.
