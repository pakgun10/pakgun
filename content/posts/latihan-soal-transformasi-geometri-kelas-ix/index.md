---
weight: 1
title: "Geser, Cerminkan, Putar, Perbesar: Latihan Soal Transformasi Geometri untuk Kelas IX"
date: 2026-11-20T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lembar latihan transformasi geometri untuk kelas IX: translasi, refleksi, rotasi, dan dilatasi, masing-masing satu soal dengan pembahasan yang menunjukkan gerakannya, plus dua latihan mandiri beserta kuncinya."
featuredImage: "featured-image.png"

tags: ["Transformasi Geometri", "Kelas IX", "Latihan Soal"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas IX saya, transformasi geometri adalah bab yang paling gampang dibuat mainan — dan paling gampang membuat anak salah arah. Geser sedikit, bayangannya pindah. Cerminkan sekali, kiri dan kanan bertukar. Putar sembilan puluh derajat, yang tadinya mendatar jadi tegak. Perbesar dua kali, luasnya jadi empat kali. Empat gerakan, empat aturan, dan hampir semua kesalahan anak berasal dari satu hal: mereka menghafal rumusnya, tetapi tidak membayangkan gerakannya.

Karena itu lembar latihan kali ini saya susun satu gerakan demi satu gerakan. Satu soal untuk translasi, satu untuk refleksi, satu untuk rotasi, satu untuk dilatasi — masing-masing dengan pembahasan yang menunjukkan gerakannya, bukan sekadar rumusnya. Empat soal dengan pembahasan, lalu dua latihan mandiri di akhir.

<!--more-->

## Sedikit yang perlu diingat sebelum mengerjakan

Empat gerakan ini mengubah posisi titik, bukan bentuknya — kecuali dilatasi yang mengubah ukuran. Translasi menggeser titik sejauh $(a, b)$: $(x, y) \to (x + a, y + b)$. Refleksi mencerminkan titik: terhadap sumbu $X$, tanda $y$ berubah; terhadap sumbu $Y$, tanda $x$ berubah; terhadap garis $y = x$, $x$ dan $y$ bertukar tempat. Rotasi $90^\circ$ berlawanan arah jarum jam terhadap pusat $O(0, 0)$: $(x, y) \to (-y, x)$; rotasi $180^\circ$: $(x, y) \to (-x, -y)$. Dilatasi dengan pusat $O$ dan faktor skala $k$: $(x, y) \to (kx, ky)$ — dan luas bayangan menjadi $k^2$ kali luas aslinya.

## Soal 1 — Translasi: geser dulu, baru catat

Titik $A(2, 3)$ ditranslasikan oleh $T(4, -1)$. Tentukan bayangan titik $A$. Kemudian tentukan bayangan titik $B(-1, 5)$ oleh translasi $T(-3, 2)$.

**Pembahasan.** Translasi hanya menambah: absis ditambah $a$, ordinat ditambah $b$. Untuk titik $A$:

$$A' = (2 + 4, 3 + (-1)) = (6, 2)$$

Untuk titik $B$:

$$B' = (-1 + (-3), 5 + 2) = (-4, 7)$$

Dua jebakan yang paling sering saya temukan: anak menulis $3 - 1$ sebagai $4$ karena lupa bahwa $T$ yang kedua bernilai negatif, dan anak menukar $a$ dengan $b$ — $4$ dipakai untuk ordinat. Cara menghindarinya sederhana: tulis dulu $x + a$ dan $y + b$ secara terpisah, baru hitung. Translasi tidak pernah mengubah bentuk atau ukuran, hanya memindahkan tempat — jadi kalau bayanganmu mendadak berubah ukuran, itu tandanya ada yang keliru di tempat lain.

## Soal 2 — Refleksi: cermin membalik satu tanda

Segitiga $ABC$ dengan $A(1, 1)$, $B(4, 1)$, dan $C(1, 3)$ dicerminkan terhadap sumbu $Y$. Tentukan koordinat bayangannya, lalu tentukan bayangan titik $P(3, -4)$ jika dicerminkan terhadap sumbu $X$.

**Pembahasan.** Cermin terhadap sumbu $Y$ membalik tanda $x$, sedangkan $y$ tetap:

$$A'(-1, 1), \quad B'(-4, 1), \quad C'(-1, 3)$$

Perhatikan segitiganya: sisi $AB$ yang tadinya dari $x = 1$ sampai $x = 4$ kini dari $x = -1$ sampai $x = -4$ — panjangnya tetap $3$, hanya pindah ke kiri sumbu $Y$. Untuk titik $P$, cermin terhadap sumbu $X$ membalik tanda $y$:

$$P' = (3, 4)$$

Jebakan klasiknya: anak mencerminkan terhadap sumbu $Y$ tetapi membalik $y$, atau mencerminkan terhadap sumbu $X$ tetapi membalik $x$. Ingat-ingat dengan kalimat ini: cermin sumbu $Y$ itu seperti berdiri di depan cermin yang dipasang tegak — kiri dan kanan bertukar, atas dan bawah tetap. Dan satu lagi: cermin terhadap garis $y = x$ menukar $x$ dengan $y$ — titik $(4, 1)$ menjadi $(1, 4)$.

## Soal 3 — Rotasi: putar, jangan digeser

Titik $Q(3, 2)$ dirotasi $90^\circ$ berlawanan arah jarum jam terhadap pusat $O(0, 0)$. Tentukan bayangannya. Kemudian tentukan bayangan titik $R(4, -1)$ jika dirotasi $180^\circ$ terhadap pusat yang sama.

**Pembahasan.** Rotasi $90^\circ$ berlawanan arah jarum jam menukar $x$ dan $y$, lalu membalik tanda $x$ yang baru:

$$Q' = (-2, 3)$$

Cek dengan membayangkan gerakannya: titik $(3, 2)$ berada di kuadran I, dekat sumbu $X$. Diputar seperempat putaran ke kiri, ia mendarat di kuadran II, dekat sumbu $Y$ — dan $(-2, 3)$ memang di kuadran II. Kalau hasilmu masih di kuadran I, arah putarmu pasti terbalik.

Rotasi $180^\circ$ lebih mudah: kedua tanda berubah:

$$R' = (-4, 1)$$

Jebakan yang paling sering: anak memakai rumus rotasi searah jarum jam $(x, y) \to (y, -x)$ untuk soal yang meminta berlawanan arah. Hasilnya $(2, -3)$ — masih di kuadran IV, jelas bukan bayangan putaran ke kiri. Sebelum menghitung, tentukan dulu kuadran hasil putaranmu; itu pemeriksaan gratis yang menyelamatkan banyak jawaban.

## Soal 4 — Dilatasi: diperbesar tiga kali, luasnya sembilan kali

Segitiga $DEF$ dengan $D(1, 2)$, $E(3, 2)$, dan $F(1, 5)$ didilatasi dengan pusat $O(0, 0)$ dan faktor skala $k = 3$. Tentukan koordinat bayangannya dan perbandingan luas bayangan terhadap luas segitiga semula.

**Pembahasan.** Dilatasi mengalikan kedua koordinat dengan $k$:

$$D'(3, 6), \quad E'(9, 6), \quad F'(3, 15)$$

Luas segitiga semula: alas $DE = 2$ dan tinggi dari $F$ ke garis $DE$ adalah $3$, jadi

$$L = \frac{1}{2} \times 2 \times 3 = 3$$

Luas bayangannya: alas $D'E' = 6$ dan tingginya $9$, jadi

$$L' = \frac{1}{2} \times 6 \times 9 = 27$$

Perbandingannya $27 : 3 = 9 : 1$ — sembilan kali, bukan tiga kali. Inilah yang paling sering luput: faktor skala $k$ memperbesar panjang $k$ kali, tetapi luas membesar $k^2$ kali. Anak yang menjawab "tiga kali" biasanya hanya mengingat $k = 3$ tanpa memeriksa apakah yang ditanya panjang atau luas. Kalau faktor skalanya pecahan, misalnya $k = \frac{1}{2}$, titik $(6, -4)$ menjadi $(3, -2)$ — diperkecil, bukan diperbesar, tetapi aturannya sama: kalikan kedua koordinatnya.

## Latihan mandiri

Kerjakan tanpa melihat kunci, lalu cocokkan jawabanmu.

1. Titik $M(-3, 4)$ ditranslasikan oleh $T(5, -6)$. Tentukan bayangan titik $M$.
2. Titik $N(5, -2)$ dirotasi $90^\circ$ searah jarum jam terhadap pusat $O(0, 0)$. Tentukan bayangannya.

**Kunci jawaban:**

1. $M' = (-3 + 5, 4 + (-6)) = (2, -2)$.
2. Rotasi $90^\circ$ searah jarum jam: $(x, y) \to (y, -x)$, jadi $N' = (-2, -5)$.

Empat gerakan ini akan muncul lagi di kelas IX — pada kesebangunan, pada grafik fungsi, bahkan pada soal-soal cerita yang tidak menyebut kata transformasi sama sekali. Kalau satu gerakan sudah terasa di tanganmu, tiga gerakan lainnya tinggal mengikuti. Selamat berlatih, dan kalau bayanganmu mendarat di kuadran yang salah, jangan dihapus dulu — tanyakan pada dirimu sendiri: gerakannya ke arah mana?
