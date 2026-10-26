---
title: "Rusuk yang Tidak Terlihat: Menggambar Balok dengan Garis Putus-putus di TikZ"
date: 2026-10-26T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya menggambar balok seperti kotak pipih karena semua rusuk digambar sama tebal. Di tulisan ini saya membedakan rusuk yang terlihat dan yang tersembunyi dengan garis putus-putus di TikZ, supaya gambar baloknya jujur dan bisa dipakai menghitung."
featuredImage: "featured-image.png"

tags: ["TikZ", "Balok", "Bangun Ruang", "Garis Putus-putus", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu, ketika membahas bangun ruang sisi datar, saya meminta kelas VIII menggambar sebuah balok di buku tulis mereka. Hasilnya hampir seragam: satu persegi panjang, satu persegi panjang lagi yang digeser sedikit ke kanan atas, lalu empat garis penghubung di antara keduanya. Sekilas gambar itu memang mirip balok. Tetapi ketika saya bertanya, "Rusuk mana yang sebenarnya tidak kelihatan kalau balok ini kita pandang dari depan?" hampir seluruh kelas terdiam. Gambar mereka tidak memberi petunjuk apa-apa, sebab semua rusuk digambar sama: sama tebal, sama penuh, sama hitam.

Masalahnya bukan pada keterampilan menggambar anak-anak. Masalahnya pada konvensi yang tidak pernah saya ajarkan secara eksplisit. Di papan tulis saya pun selama ini menggambar balok dengan cara yang sama: semua garis penuh. Akibatnya, ketika tiba saatnya menghitung rusuk, siswa menghitung garis yang ada di gambar — dan selalu kelebihan atau kekurangan, karena mereka tidak tahu garis mana yang sesungguhnya tertutup oleh sisi depan balok. Pekan ini saya memperbaiki kebiasaan itu dengan satu aturan sederhana di TikZ: rusuk yang tertutup digambar putus-putus.

<!--more-->

## Balok punya dua belas rusuk, tidak semuanya kelihatan

Sebuah balok memiliki 12 rusuk: empat rusuk panjang, empat rusuk lebar, dan empat rusuk tinggi. Ia juga memiliki 6 sisi dan 8 titik sudut. Angka-angka ini mudah dihafal, tetapi sulit dilihat kalau gambarnya tidak jujur. Pada gambar yang saya buat pekan ini, sembilan rusuk digambar dengan garis penuh karena memang terlihat dari depan, dan tiga rusuk digambar putus-putus karena tertutup sisi depan: rusuk bawah sisi belakang, rusuk kiri sisi belakang, dan rusuk penghubung sudut kiri bawah. Sembilan tambah tiga sama dengan dua belas — dan untuk pertama kalinya, hitungan di gambar cocok dengan hitungan di definisi.

Reaksi pertama siswa justru berupa pertanyaan yang bagus: "Berarti yang putus-putus itu ada di belakang, Pak?" Tepat. Garis putus-putus bukan hiasan dan bukan garis yang belum selesai digambar. Ia adalah kode gambar: garis ini ada, tetapi pandangan kita terhalang oleh sisi depan balok. Begitu kode ini disepakati, gambar balok berubah fungsi: dari sekadar ilustrasi menjadi alat baca. Siswa tidak lagi menebak-nebak, mereka membaca.

## Menggambarnya langkah demi langkah di TikZ

Caranya saya pecah menjadi empat langkah, supaya mudah ditiru di dokumen apa pun.

Pertama, gambar sisi depan sebagai persegi panjang. Saya beri nama titik sudutnya A, B, C, dan D, berurutan dari kiri bawah memutar berlawanan arah jarum jam. Kedua, gambar sisi belakang dengan menggeser sisi depan sejauh vektor miring yang sama untuk semua titik sudut — pada gambar ini saya memakai geseran (1,5; 1,2). Titik-titik sisi belakang saya beri nama E, F, G, dan H, seletak dengan A, B, C, dan D. Ketiga, hubungkan setiap pasangan titik yang seletak: A ke E, B ke F, C ke G, dan D ke H. Keempat — dan ini langkah yang paling penting — ubah tiga rusuk yang tersembunyi menjadi garis putus-putus.

Kode intinya sesederhana ini:

```latex
% Sisi depan (terlihat penuh)
\draw[very thick] (A) -- (B) -- (C) -- (D) -- cycle;
% Rusuk penghubung yang terlihat
\draw[very thick] (B) -- (F) (C) -- (G) (D) -- (H);
% Sisi belakang: atas dan kanan terlihat, bawah dan kiri tersembunyi
\draw[very thick] (H) -- (G) -- (F);
% Tiga rusuk tersembunyi: putus-putus
\draw[very thick, dashed, red!70!black] (A) -- (E) -- (F);
\draw[very thick, dashed, red!70!black] (E) -- (H);
```

Satu catatan praktis: jangan membuat vektor geseran terlalu besar. Geseran yang terlalu jauh membuat balok tampak rebah dan miring, sedangkan geseran yang terlalu kecil membuat sisi belakang menempel pada sisi depan sehingga gambarnya sulit dibaca. Geseran sekitar sepertiga lebar sisi depan biasanya sudah cukup untuk memberi kesan kedalaman tanpa merusak bentuknya. Saya juga memberi warna merah pada garis putus-putus di awal-awal, supaya mata siswa langsung menangkap kode ini; setelah mereka terbiasa, warnanya boleh dikembalikan ke hitam.

## Tiga kesalahan yang paling sering saya lihat

Kesalahan pertama adalah menggambar semua rusuk dengan garis penuh. Baloknya memang lengkap, tetapi ia tampak seperti kerangka kawat yang tembus pandang. Siswa yang melihatnya wajar mengira semua rusuk bisa dilihat sekaligus, padahal balok asli terbuat dari sisi yang padat dan menutupi apa yang ada di belakangnya.

Kesalahan kedua adalah kebalikannya: memakai garis putus-putus untuk seluruh sisi belakang, termasuk rusuk atas dan rusuk kanan yang sebenarnya terlihat dari depan. Gambarnya memang terasa "tiga dimensi", tetapi kodenya salah, dan siswa yang meniru akan mengulang kesalahan yang sama di setiap gambar berikutnya.

Kesalahan ketiga adalah lupa memberi label ukuran. Gambar tanpa label panjang ($p$), lebar ($l$), dan tinggi ($t$) hanya menjadi pajangan. Begitu ketiga label itu ditulis — $p$ di rusuk bawah depan, $t$ di rusuk tegak depan, dan $l$ di rusuk miring penghubung — gambar yang sama langsung bisa dipakai bekerja: menghitung volume dengan $V = p \times l \times t$. Misalnya, untuk $p = 6$ cm, $l = 4$ cm, dan $t = 3$ cm, volumenya $72$ cm$^3$. Gambar yang jujur membuat soal menjadi lebih mudah, bukan lebih sulit.

## Penutup: gambar yang jujur menghemat penjelasan

Sejak memakai konvensi ini, pertanyaan di kelas berubah. Siswa tidak lagi bertanya "ini balok atau kotak, Pak?" melainkan menunjuk garis putus-putus dan berkata, "yang ini di belakang ya, Pak, makanya putus-putus." Satu kode gambar yang disepakati menghemat sepuluh menit penjelasan yang dulu selalu saya ulang setiap kali bangun ruang dibahas.

Itulah gunanya menggambar dengan TikZ bagi saya: bukan supaya gambarnya terlihat canggih, melainkan supaya gambarnya bisa dipercaya. Kalau satu garis saja berbohong, siswa akan meragukan semua garis lainnya. Kalau garisnya jujur — yang terlihat digambar penuh, yang tertutup digambar putus-putus — gambar itu sendiri yang mengajar.

> 📎 **Berkas TikZ lengkap:** [balok-rusuk-tersembunyi.tex](tex/balok-rusuk-tersembunyi.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
