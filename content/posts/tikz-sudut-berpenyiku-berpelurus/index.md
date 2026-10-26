---
title: "Berpenyiku dan Berpelurus: Menggambar Dua Pasang Sudut yang Sering Tertukar dengan TikZ"
date: 2026-10-26T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Di kelas VII, sudut berpenyiku dan berpelurus adalah dua pasangan yang paling sering tertukar: satu berjumlah 90 derajat, satu lagi 180 derajat, tetapi gambarnya di papan tulis sering tampak sama. Di tulisan ini saya menggambar keduanya dengan TikZ — busur yang berbeda, label yang jelas, dan satu contoh hitung untuk masing-masing."
featuredImage: "featured-image.png"

tags: ["TikZ", "Sudut", "Berpenyiku", "Berpelurus", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu, di kelas VII, saya menulis dua soal di papan tulis. Soal pertama: sebuah sudut besarnya $35^{\circ}$, tentukan penyikunya. Soal kedua: sebuah sudut besarnya $125^{\circ}$, tentukan pelurusnya. Jawaban yang masuk bermacam-macam, dan yang paling menarik bukanlah jawaban yang salah hitung, melainkan jawaban yang tertukar pasangannya: penyiku dijawab $55^{\circ}$ — itu benar — tetapi pelurus dijawab $65^{\circ}$, seolah-olah kedua soal itu memakai patokan yang sama. Ada juga yang menjawab penyiku $145^{\circ}$, karena ia memakai patokan garis lurus untuk soal yang seharusnya memakai patokan siku-siku.

Di sinilah saya merasa gambar di papan tulis ikut bersalah. Ketika saya menggambar kedua pasangan itu dengan kapur, keduanya tampak seperti dua sudut yang berdampingan, tanpa penanda yang membedakan mana yang jumlahnya $90^{\circ}$ dan mana yang $180^{\circ}$. Siswa menghafal definisinya, tetapi matanya tidak pernah melihat perbedaannya. Maka malam harinya saya menggambar ulang keduanya dengan TikZ, dengan satu aturan: patokannya harus terlihat di dalam gambar. Tulisan ini adalah catatan cara membuatnya.

<!--more-->

## Kenapa dua pasangan ini mudah tertukar

Namanya mirip, bunyinya mirip, dan keduanya sama-sama soal "pasangan sudut yang jumlahnya sekian". Di kepala siswa, "berpenyiku" dan "berpelurus" akhirnya melebur menjadi satu gagasan kabur: dua sudut yang kalau dijumlahkan menghasilkan sesuatu. Angka patokannya — $90^{\circ}$ atau $180^{\circ}$ — menjadi detail yang gampang tertukar, karena tidak ada gambar yang menguncinya.

Padahal patokan itu punya bentuk yang sangat berbeda. Sudut $90^{\circ}$ adalah siku-siku: bentuknya seperti sudut meja, tegak dan tegas. Sudut $180^{\circ}$ adalah garis lurus: bentuknya seperti jalan yang tidak berbelok sama sekali. Kalau gambar kita menunjukkan kedua bentuk patokan itu dengan jelas, siswa tidak perlu lagi menebak-nebak angka mana yang dipakai soal. Mereka cukup melihat gambarnya: ada tanda siku-sikukah, atau ada garis lurus?

Karena itu, kedua gambar di bawah ini selalu dimulai dari patokannya: berpenyiku dari siku-siku, berpelurus dari garis lurus. Patokan dulu, pasangan kemudian.

## Pasangan pertama: berpenyiku, jumlahnya $90^{\circ}$

Dua sudut dikatakan berpenyiku bila jumlahnya $90^{\circ}$. Ambil contoh yang tadi muncul di kelas: sudut pertama $35^{\circ}$, maka penyikunya adalah $90^{\circ} - 35^{\circ} = 55^{\circ}$. Keduanya, bila digabung, tepat mengisi satu siku-siku.

Saya menggambarnya dari titik sudut $O$. Dari $O$ saya tarik sinar mendatar ke kanan dan sinar tegak ke atas — inilah siku-sikunya, lengkap dengan tanda kotak kecil di sudutnya. Tanda kotak itu bukan hiasan; ia adalah pesan visual bahwa patokan gambar ini adalah $90^{\circ}$. Baru kemudian saya tarik sinar ketiga dari $O$ dengan kemiringan $35^{\circ}$ dari sinar mendatar. Sinar ini membagi siku-siku menjadi dua sudut: $35^{\circ}$ di bawah dan $55^{\circ}$ di atasnya.

```latex
% Siku-siku sebagai patokan: sinar mendatar dan sinar tegak
\coordinate (O) at (0,0);
\draw[thick] (O) -- (4,0);
\draw[thick] (O) -- (0,4);
% Tanda kotak siku-siku di sudut O
\draw[thick] (0.5,0) -- (0.5,0.5) -- (0,0.5);
% Sinar pembagi dengan kemiringan 35 derajat
\draw[thick] (O) -- (3.28,2.29);
% Busur dan label kedua sudut
\draw (O) ++(0:1) arc (0:35:1);
\node at (1.25,0.35) {$35^{\circ}$};
\draw (O) ++(35:1.4) arc (35:90:1.4);
\node at (0.55,1.55) {$55^{\circ}$};
```

Perhatikan bahwa kedua busur digambar dengan jari-jari yang berbeda: busur $35^{\circ}$ lebih dekat ke titik $O$, busur $55^{\circ}$ lebih jauh. Ini sengaja, supaya labelnya tidak bertumpuk dan kedua sudut terbaca sebagai dua wilayah yang terpisah, meskipun keduanya berbagi titik sudut yang sama.

Contoh lain: sudut $48^{\circ}$ penyikunya $90^{\circ} - 48^{\circ} = 42^{\circ}$ — kurangkan dari $90^{\circ}$, karena patokannya siku-siku.

## Pasangan kedua: berpelurus, jumlahnya $180^{\circ}$

Dua sudut dikatakan berpelurus bila jumlahnya $180^{\circ}$. Contoh dari kelas tadi: sudut pertama $125^{\circ}$, maka pelurusnya adalah $180^{\circ} - 125^{\circ} = 55^{\circ}$. Keduanya, bila digabung, tepat membentuk satu garis lurus.

Gambarnya dimulai dari garis lurus, bukan dari siku-siku. Dari titik sudut $O$ saya tarik sinar ke kiri dan sinar ke kanan sehingga keduanya membentuk satu garis mendatar. Lalu saya tarik sinar ketiga dari $O$ ke arah kanan atas, dengan kemiringan $55^{\circ}$ dari sinar kanan. Sinar ini membagi garis lurus menjadi dua sudut: $55^{\circ}$ di kanan dan $125^{\circ}$ di kiri.

```latex
% Garis lurus sebagai patokan: sinar ke kiri dan ke kanan
\coordinate (O) at (0,0);
\draw[thick] (O) -- (-4,0);
\draw[thick] (O) -- (4,0);
% Sinar pembagi dengan kemiringan 55 derajat dari kanan
\draw[thick] (O) -- (2.29,3.28);
% Busur dan label kedua sudut
\draw (O) ++(0:1) arc (0:55:1);
\node at (1.2,0.45) {$55^{\circ}$};
\draw (O) ++(55:1.4) arc (55:180:1.4);
\node at (-1.1,1.15) {$125^{\circ}$};
```

Bandingkan gambar ini dengan gambar berpenyiku di atas. Bedanya langsung terlihat: di sini tidak ada tanda kotak siku-siku, karena patokannya bukan siku-siku; yang ada adalah garis lurus yang membentang dari kiri ke kanan. Begitu siswa melihat garis lurus itu, mereka tahu patokannya $180^{\circ}$, sehingga yang harus dikurangkan adalah $180^{\circ}$, bukan $90^{\circ}$.

Latihan cepat di kelas: sudut $72^{\circ}$ pelurusnya $180^{\circ} - 72^{\circ} = 108^{\circ}$. Saya tidak lagi mendengar jawaban $18^{\circ}$ yang lahir dari patokan yang tertukar.

## Tiga kesalahan yang paling sering saya temui

Kesalahan pertama adalah menukar patokannya: penyiku dihitung dari $180^{\circ}$ dan pelurus dari $90^{\circ}$. Obatnya adalah gambar: sebelum menghitung, siswa saya minta menggambar dulu patokannya — kotak siku-siku atau garis lurus — dan menuliskan angka patokan itu di samping gambar. Hitungan baru dimulai setelah patokannya tertulis.

Kesalahan kedua adalah menggambar kedua pasangan dengan cara yang sama persis, misalnya keduanya digambar sebagai dua sudut yang berdampingan tanpa patokan. Gambar seperti itu tidak membantu apa-apa, karena ia menyembunyikan justru informasi yang paling penting: jumlahnya $90^{\circ}$ atau $180^{\circ}$? Gambar yang baik selalu memuat patokannya.

Kesalahan ketiga adalah melupakan satuan derajat: jawaban "55" tanpa $^{\circ}$ mudah tercampur dengan panjang sisi di soal-soal berikutnya. Saya membiasakan siswa selalu menuliskan $^{\circ}$ pada setiap jawaban sudut.

Di kelas, saya kini memproyeksikan kedua gambar ini berdampingan: di kiri siku-siku yang terbagi menjadi $35^{\circ}$ dan $55^{\circ}$, di kanan garis lurus yang terbagi menjadi $125^{\circ}$ dan $55^{\circ}$. Lalu saya bertanya satu hal saja: gambar mana yang patokannya $90^{\circ}$, dan dari mana kamu tahu? Siswa tidak lagi menjawab dengan hafalan. Mereka menunjuk tanda kotak siku-siku di gambar kiri dan garis lurus di gambar kanan, lalu berkata, "Yang kiri penyiku, Pak, karena ada kotak siku-sikunya." Begitu patokannya terbaca dari gambar, rumusnya mengikuti dengan sendirinya.

> 📎 **Berkas TikZ lengkap:** [sudut-berpenyiku-berpelurus.tex](tex/sudut-berpenyiku-berpelurus.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
