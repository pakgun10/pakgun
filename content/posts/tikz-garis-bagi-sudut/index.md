---
title: "Garis Bagi Sudut yang Bisa Dibuktikan dengan Jangka: Konstruksi dan TikZ"
date: 2026-11-01T19:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Mengajari siswa menggambar garis bagi sudut dengan jangka, lalu mempertanggungjawabkannya lagi dengan TikZ — dua konstruksi yang saling menguatkan."
featuredImage: "featured-image.png"
tags: ["TikZ", "Konstruksi", "Geometri"]
categories: ["Matematika"]
math:
  enable: true
---

Kelas 7C hari itu baru saja menerima jangka. Bukan jangka besar untuk guru di papan, tapi jangka kecil murah yang saya beli sekotak — yang matanya agak liar kalau diputar terlalu cepat. Saya tulis satu soal di papan: *gambarlah garis yang membagi sudut 60 derajat menjadi dua bagian sama besar*. Tanpa busur derajat.

Hampir seketika ada yang mengangkat tangan. "Bu, bagaimana caranya kalau tidak boleh pakai busur?" Pertanyaan itu sebenarnya inti dari seluruh pertemuan, dan saya sengaja tidak menjawabnya lebih dulu. Saya biarkan hening beberapa detik. Di pojok kelas, seorang siswa sudah mulai mencoba-coba menarik garis di tengah-tengah sudutnya, menebak-nebak posisinya. Kelihatannya benar di mata, tapi saya tahu betul seberapa licik sifat "kelihatannya benar" dalam geometri.

<!--more-->

## Masalah Lama yang Saya Alami Sendiri

Jujur saja, dulu saya sendiri mengajarkan garis bagi sudut sebagai resep: *buka jangka, tancapkan di titik sudut, buat busur, lalu dari dua titik perpotongan buat dua busur lagi yang berpotongan, tarik garisnya*. Siswa meniru lima langkah itu, hasilnya jadi, ulangan berjalan lancar. Tapi setiap kali saya tanya "kenapa cara itu bekerja?", jawabannya biasanya diatup, dilihat-lihat, lalu diam.

Sebenarnya masalahnya bukan pada siswa. Masalahnya pada saya yang mengajarkan prosedurnya saja tanpa memperlihatkan buktinya. Garis bagi sudut adalah salah satu konstruksi yang paling indah karena buktinya bisa *dilihat*, bukan dihafal. Dan berkat dua lingkaran sama jari-jari, bukti itu cukup sederhana untuk siswa SMP.

Makanya tahun ini saya mencoba cara lain: menggambar bersama-sama, membongkar kenapa tiap busur ada, lalu — karena saya memang suka — menggambarnya ulang dengan TikZ agar versi rapi dan jujurnya ikut masuk ke lembar kerja siswa.

## Konstruksinya, Langkah demi Langkah

Mari kita buat sudut $AOB$ — sebut saja besarnya $60^\circ$, sudut yang ramah. Konstruksinya seperti ini:

1. Tancapkan jangka di titik $O$, buka jangka dengan jari-jari sembarang — sebut $r$. Buat busur yang memotong kedua kaki sudut. Sebut titik potongnya $P$ (di sisi $OB$) dan $Q$ (di sisi $OA$).
2. Tancapkan jangka di $P$ dan di $Q$, dengan jari-jari yang **sama** — ini penting — buat dua busur yang saling berpotongan. Titik potongnya kita beri nama $M$.
3. Tarik garis $OM$. Itulah garis bagi sudut kita.

Langkah kedua itulah yang paling sering disalahpahami siswa. Ada yang membuka jangka lagi dengan ukuran baru, ada yang lupa bahwa dua busur itu harus ditarik dari *dua titik berbeda*. Kalau jangka kecilnya liar, dua busurnya tidak bertemu dan muncul pertanyaan klasik: "Bu, busurnya tidak ketemu."

## Kenapa Cara Itu Bekerja

Di sinilah bagian yang paling saya nikmati di kelas. Setelah gambar jadi, saya tanyakan: apa yang bisa kita pastikan tentang segitiga $OPM$ dan $OQM$?

Perhatikan bersama-sama:

- $OP = OQ$, karena keduanya jari-jari busur yang sama dari langkah pertama, keduanya sama dengan $r$.
- $PM = QM$, karena busur di langkah kedua dibuat dengan jari-jari yang sama — sebut saja $s$.
- $OM$ adalah sisi bersama kedua segitiga.

Tiga sisi sama berarti kedua segitiga **kongruen** — siswa baru saja memakai kriteria SSS yang mereka pelajari sebelumnya, kali ini untuk keperluan yang terasa nyata. Dan karena segitiganya kongruen, sudut yang bersesuaian juga sama besar:

$$\angle POM = \angle QOM$$

Itulah arti kata garis bagi: satu garis, dua sudut sama besar. Bukan keajaiban resep, tapi konsekuensi dari dua lingkaran yang jari-jarinya dipaksa sama. Kalau siswa membuka jangka dengan ukuran berbeda di langkah kedua, syarat $PM = QM$ runtuh — dan memang saat itu di kelas 7C, satu kelompok yang busurnya tidak bertemu menemukan sendiri bahwa jangka mereka "tergeser" saat diputar. Bukti dan pengalaman bertemu di satu titik.

{{< figure src="konstruksi-garis-bagi.png" title="Konstruksi garis bagi sudut: dua busur pertama dari O, dua busur kedua dari P dan Q, lalu garis OM." >}}

## Merawat Konstruksi yang Sama di TikZ

Setelah sesi jangka, biasanya saya menuliskan versi rapi di lembar kerja. Dan di sini TikZ punya keistimewaan yang tidak dimiliki jangka liar: koordinatnya dihitung, bukan ditebak. Saya bisa menaruh $O$ di titik asal, kaki sudut di sudut $30^\circ$ dan $-30^\circ$, lalu meminta TikZ menggambar busur dengan jari-jari yang persis sama.

Potongan intinya kira-kira begini:

```latex
\coordinate (O) at (0,0);
\coordinate (P) at (30:4);   % di kaki atas
\coordinate (Q) at (-30:4);  % di kaki bawah
\draw (O) -- (P);
\draw (O) -- (Q);
% busur pertama dari O, jari-jari sama
\draw (30:2) arc (30:-30:2);
% titik M di garis bagi, sudut 0 derajat
\coordinate (M) at (0:4.5);
\draw[dashed] (O) -- (M);
% dua busur kedua, dari P dan Q, jari-jari sama
\draw (P) arc (0:60:3);
\draw (Q) arc (-60:0:3);
```

Yang saya hargai dari konstruksi ini: karena kedua busur kedua memakai jari-jari yang sama ($s = 3$ dalam contoh), titik potongnya *otomatis* jatuh tepat di garis bagi. Kalau saya iseng mengganti satu jari-jari saja, titik potongnya bergeser — dan pembaca lembar kerja langsung melihat bahwa gambar itu berhenti jujur. Jangka liar di kelas dan koordinat yang salah di TikZ ternyata mengajarkan pelajaran yang sama: konstruksi menuntut kesetiaan pada jari-jari.

Berkas TikZ lengkap yang bisa langsung dikompilasi saya sertakan di akhir tulisan ini, lengkap dengan label $P$, $Q$, $M$, tanda kesamaan sisi, dan busur kecil penanda dua sudut yang sama besar.

## Apa yang Berubah di Kelas

Tidak ada revolusi. Beberapa siswa tetap lebih senang menghafal lima langkah, dan itu wajar. Tapi ada satu perubahan yang menurut saya layak dicatat: saat saya meminta mereka menjelaskan langkah kedua kepada teman sebangku, tidak ada lagi yang berkata "gitu aja caranya". Yang muncul malah kalimat seperti "jangkanya harus sama, nanti segitiganya kembar, sudutnya ikut sama." Kalimat seperti itu tidak bisa lahir dari hafalan.

Dan menariknya, ketika minggu berikutnya kami bertemu soal garis bagi yang berada di dalam segitiga — yang memotong sisi di titik tengah hanya pada kasus istimewa — beberapa siswa langsung berkomentar bahwa "yang di tengah itu sudutnya, bukan sisinya". Pembedaan kecil seperti itu biasanya butuh koreksi berulang-ulang; kali ini mereka yang menegur diri sendiri.

## Menutup dengan Satu Keputusan Kecil

Kalau ada satu hal yang saya pertahankan dari pertemuan 7C itu, mungkin begini: jangan mengajarkan konstruksi hanya sebagai rangkaian gerakan tangan. Setiap langkah jangka itu ada alasan geometrisnya, dan alasan itu tidak perlu rumit untuk diperlihatkan. Dua segitiga kembar yang lahir dari dua jari-jari yang sama — itu saja sudah cukup.

Sementara TikZ di sisi lain bukan pengganti jangka. Jangka mengajarkan hati-hati, TikZ mengajarkan ketelitian yang bisa dipertanggungjawabkan. Keduanya memakai kosakata yang sama: jari-jari, busur, titik potong. Kalau siswa pernah memegang keduanya, mereka punya dua bahasa untuk mengatakan hal yang sama — dan itu, menurut saya, salah satu definisi paling sederhana dari belajar matematika.

> 📎 **Berkas TikZ lengkap:** [tikz-garis-bagi-sudut.tex](tex/tikz-garis-bagi-sudut.tex) — siap kompilasi (butuh paket `tikz`).
