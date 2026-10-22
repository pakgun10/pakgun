---
weight: 1
title: "Ketika AI Jadi Murid Pertama di Kelas Saya"
date: 2026-10-22T04:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Soal yang menurut guru sudah jelas belum tentu jelas bagi murid. Saya memakai AI sebagai murid pertama untuk menemukan kalimat soal yang ambigu, soal yang bisa ditebak tanpa paham konsep, dan soal yang kelewat sulit — sebelum lembar ulangannya dicetak."
featuredImage: "featured-image.png"

tags: ["AI", "Asesmen"]
categories: ["Teknologi Pendidikan"]

math:
  enable: true
---

Beberapa semester lalu saya mengalami kejadian yang memalukan, sekaligus berharga. Soal ulangan yang menurut saya sudah sangat jelas ternyata gagal di kelas: hampir separuh siswa mengartikan sesuatu yang sama sekali berbeda dari maksud saya. Bukan karena konsepnya sulit — kalimat soalnya yang bermakna ganda.

Sejak saat itu, sebelum satu lembar ulangan pun saya cetak, saya selalu mengujinya ke satu "murid" yang tidak pernah mengeluh dan tidak pernah tersinggung: AI yang saya minta berperan sebagai murid kelas VIII.

<!--more-->

## Bukan membuat soal, melainkan mengujinya

Perlu saya tegaskan dulu: AI di sini bukan saya suruh *membuat* soal. Pengalaman saya, soal yang dibuat murni oleh AI sering terasa asing — konteksnya tidak pernah cocok dengan keseharian anak-anak Punggur, dan tingkat kesulitannya melonjak tanpa pola. Soal tetap saya tulis sendiri, dari tujuan pembelajaran yang sudah saya tetapkan.

Baru setelah soalnya jadi, saya memanggil AI sebagai penguji. Perintahnya kira-kira begini: *"Berperanlah sebagai murid kelas VIII SMP yang kemampuan matematikanya pas-pasan. Kerjakan soal berikut, lalu ceritakan bagian mana yang membingungkan."* Prompt sesederhana itu ternyata sudah cukup untuk menyingkap kelemahan soal saya.

## Tiga jebakan yang pernah terungkap

**Pertama, soal yang bermakna ganda.** Pernah saya menulis: "Tentukan gradien garis yang melalui titik $(2,5)$ dan memotong sumbu-$x$ di titik $(-3,0)$." AI "murid" menjawab dengan benar, tetapi di akhir ia menulis: *"Saya sempat bingung, apakah garisnya memang harus melalui kedua titik itu? Kalimatnya terasa seperti dua perintah yang berbeda."* Ia benar — bagi guru, "memotong sumbu-$x$" jelas berarti melalui titik potongnya, tetapi bagi murid, dua frasa terpisah terasa seperti dua instruksi yang berbeda. Saya ubah menjadi: "Tentukan gradien garis yang melalui titik $(2,5)$ dan $(-3,0)$." Selesai — tidak ada lagi ruang tafsir.

**Kedua, soal yang bisa dijawab tanpa memahami konsepnya.** Untuk materi persamaan garis lurus saya pernah membuat soal pilihan ganda: "Manakah yang merupakan persamaan garis lurus: (a) $y = 2x + 3$, (b) $y = x^2 - 1$, (c) $xy = 4$, (d) $y = \frac{5}{x}$?" AI murid memilih (a) dan menjelaskan: *"Yang (a) paling pendek dan paling rapi, jadi itu jawabannya."* Lucu, tetapi menohok: soal saya bisa dijawab dengan tebak visual tanpa tahu apa-apa tentang pangkat variabel. Sejak itu setiap pengecoh saya buat "mirip" dengan kunci — misalnya (a) $y = 2x + 3$, (b) $y = x^2 + 3$, (c) $2x + 3y = 5$, (d) $y = \frac{3}{x}$ — sehingga hanya pemahaman konsep yang bisa memilih dengan benar.

**Ketiga, soal yang ternyata kelewat sulit untuk targetnya.** Saya pernah menyusun soal uraian: "Garis $l$ melalui $(1,2)$ dan tegak lurus garis $2x - y = 4$. Tentukan persamaan garis $l$." AI murid kelas VIII menyerah di langkah kedua: ia tahu gradien garis yang diketahui adalah $2$, tetapi hubungan "gradien garis tegak lurus adalah negatif kebalikan" belum pernah saya ajarkan secara eksplisit di kelas. Soal itu sah secara matematis, tetapi salah secara pembelajaran — menuntut sesuatu yang belum dibelajarkan. Saya pecah menjadi dua soal: satu soal mencari gradien garis yang tegak lurus, satu soal menentukan persamaannya.

## Cara saya melakukannya langkah demi langkah

1. **Tulis soal sampai selesai**, lengkap dengan kunci jawaban dan alokasi waktunya. Uji coba hanya bermakna kalau yang diuji adalah versi final.
2. **Beri AI konteks kelas yang spesifik**: "Kelas VIII SMP, baru selesai belajar persamaan garis lurus bagian gradien. Kemampuan rata-rata, kadang salah hitung pecahan." Semakin spesifik konteksnya, semakin jujur perannya sebagai murid.
3. **Minta tiga hal sekaligus**: kerjakan soalnya, tuliskan langkah berpikirnya, dan tunjukkan kalimat mana yang membingungkan — persis seperti murid sungguhan yang bercerita setelah ulangan.
4. **Perbaiki soalnya, bukan sekadar menerima jawaban AI.** Kalau AI "murid" salah paham, jangan salahkan AI-nya; salahkan kalimat saya.

## Batasannya harus dipegang

AI tetap bukan murid sungguhan. Miskonsepsi khas anak-anak — misalnya kebiasaan "pindah ruas tanpa mengubah tanda" atau panik melihat pecahan — tidak selalu muncul dalam permainannya. Hasil uji ini saya perlakukan sebagai temuan awal, bukan vonis akhir. Dan satu prinsip yang tidak pernah saya langgar: **keputusan akhir tetap di tangan guru**. AI memberi masukan, saya yang memutuskan.

## Penutup

Sejak memakai cara ini, keluhan "Pak, maksud soalnya apa?" menurun drastis di kelas saya. Waktu yang tadinya habis untuk menjelaskan maksud soal saat ulangan — waktu yang seharusnya dipakai untuk berpikir — kini kembali ke tempatnya.

Biaya metodenya hampir nol: lima menit mengobrol dengan AI sebelum mencetak. Untuk guru yang selama ini menyusun soal sendirian tanpa teman diskusi, "murid pertama" ini adalah teman diskusi yang selalu siap. Cobalah pada satu soal ulangan berikutnya; saya ingin tahu jebakan apa yang ia temukan dari soal Bapak/Ibu.
