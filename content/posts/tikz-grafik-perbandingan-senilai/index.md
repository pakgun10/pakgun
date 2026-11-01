---
weight: 1
title: "Satu Garis Lurus dari Nol: Menggambar Grafik Perbandingan Senilai dengan TikZ"
date: 2026-11-02T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya hafal bahwa dua kali lipat barang berarti dua kali lipat harga, tetapi grafiknya berantakan: titik tidak segaris dan garisnya mulai dari entah mana. Dengan TikZ, skala sumbu dibuat eksplisit sehingga grafik perbandingan senilai tampil sebagai satu garis lurus yang lewat titik asal."
featuredImage: "featured-image.png"
tags: ["TikZ", "LaTeX", "Perbandingan Senilai", "Grafik", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]
math:
  enable: true
---

Pekan lalu, di kelas VII, saya menulis tabel sederhana di papan tulis: satu buku tulis harganya Rp3.000, dua buku Rp6.000, tiga buku Rp9.000, empat buku Rp12.000. Semua siswa mengangguk. Polanya jelas: jumlah buku dilipatgandakan, harga ikut terlipatgandakan. Lalu saya meminta mereka menggambar grafiknya, dan anggukan itu berubah menjadi gambar yang berantakan. Ada titik yang tidak segaris, ada sumbu tanpa skala sehingga jarak Rp3.000 dan Rp6.000 tampak sama, dan ada garis yang dimulai dari titik pertama, bukan dari titik asal. Tabelnya benar, tetapi grafiknya tidak bercerita apa-apa.

Masalahnya bukan pada pemahaman perbandingannya, melainkan pada gambarnya yang tidak dijaga. Grafik perbandingan senilai punya satu ciri yang harus terlihat oleh mata, bukan sekadar dihafal: semua titiknya jatuh pada satu garis lurus yang melewati titik asal. Kalau ciri itu tidak tampak, grafiknya gagal menjalankan tugasnya, yaitu meyakinkan siswa bahwa hubungan itu memang senilai. Pekan ini saya menggambar ulang grafik itu dengan TikZ, dan TikZ memaksa saya melakukan hal yang sering saya lewatkan di papan tulis: menuliskan skalanya dengan eksplisit.

<!--more-->

## Perbandingan senilai itu garis lurus yang lewat titik asal

Sebelum membuka kode apa pun, saya mengajak siswa menyepakati dulu tiga hal dari tabel harga buku. Pertama, harga selalu sama dengan Rp3.000 dikali jumlah buku, sehingga rumusnya $harga = 3000 \times n$. Kedua, ada satu titik yang hampir selalu dilupakan: nol buku harganya Rp0, jadi titik $(0, 0)$ ikut menjadi bagian dari data. Ketiga, karena setiap titik diperoleh dari rumus yang sama, semuanya harus jatuh pada satu garis lurus.

Titik $(0, 0)$ inilah pembeda yang paling penting. Banyak siswa menggambar garis dari titik pertama, $(1, 3000)$, seolah-olah grafik baru "lahir" di sana. Padahal garis yang tidak melewati titik asal sedang bercerita lain: ia bercerita tentang harga yang punya biaya tetap, misalnya ongkir atau uang pangkal, yang tidak ada dalam soal buku ini. Begitu siswa memahami bahwa melewati titik asal adalah ciri visual perbandingan senilai, mereka punya alat cek yang cepat: lihat garisnya, apakah ia berangkat dari nol?

## Menggambar sumbu dan titiknya di TikZ

Gambar pertama hanya memuat sumbu dan titik-titiknya, belum ada garis. Saya memakai dua keputusan skala yang ditulis terang-terangan di kode: sumbu mendatar satu buku selebar 1,2 cm, dan sumbu tegak Rp1.000 setinggi 0,55 cm. Supaya angkanya tidak berderet nol, sumbu tegak saya tulis dalam ribuan rupiah, jadi 12 pada sumbu berarti Rp12.000. Keputusan seperti ini terasa sepele, tetapi justru inilah yang membuat grafik di papan tulis sering berantakan: skalanya hanya ada di kepala guru, tidak tertulis di mana-mana.

```latex
\begin{tikzpicture}[x=1.2cm, y=0.55cm]
  % Kisi-kisi tipis sebagai latar
  \draw[step=1, gray!20, very thin] (0,0) grid (5,13);
  % Sumbu mendatar: jumlah buku
  \draw[thick,->] (0,0) -- (5.4,0) node[right] {Jumlah buku};
  % Sumbu tegak: harga dalam ribuan rupiah
  \draw[thick,->] (0,0) -- (0,13.4) node[above] {Harga (ribu rupiah)};
  % Tanda pada sumbu mendatar
  \foreach \x in {1,...,5} {
    \draw[thick] (\x,-0.15) -- (\x,0.15);
    \node[below] at (\x,-0.3) {\x};
  }
  % Tanda pada sumbu tegak, setiap 3 ribu
  \foreach \y in {3,6,9,12} {
    \draw[thick] (-0.15,\y) -- (0.15,\y);
    \node[left] at (-0.3,\y) {\y};
  }
  % Titik-titik dari tabel harga buku
  \foreach \x/\y in {1/3, 2/6, 3/9, 4/12} {
    \fill[red] (\x,\y) circle (0.09);
    \node[above right, red] at (\x,\y) {(\x,\y)};
  }
\end{tikzpicture}
```

Perhatikan perintah `\foreach` untuk tanda sumbu. Tanpa perulangan itu, saya harus menulis lima tanda mendatar dan empat tanda tegak satu per satu, dan setiap kali mengubah skala saya harus mengubah semuanya. Dengan `\foreach`, skala hanya ditulis sekali, di baris `[x=1.2cm, y=0.55cm]`, dan semua tanda mengikuti. Inilah keuntungan menggambar dengan kode: mengubah keputusan skala tidak berarti menggambar ulang dari nol.

## Menarik garisnya dan membacanya

Setelah titik-titiknya terpasang, menarik garisnya tinggal satu perintah: garis dari $(0, 0)$ melewati semua titik, sedikit diperpanjang melewati titik terakhir supaya arahnya terbaca.

```latex
% Garis perbandingan senilai: dari titik asal melewati semua titik
\draw[very thick, color=goldenrod] (0,0) -- (4.6,13.8);
```

Di kelas, saya tidak langsung memberi tahu siswa bahwa garisnya lurus. Saya meminta mereka mengamati dulu: apakah titik-titik merah itu memang segaris, dan dari mana garis itu berangkat? Barulah kami menguji garis itu dengan titik baru dari tabel yang belum digambar, misalnya 5 buku seharga Rp15.000. Titik $(5, 15)$ berada di luar kertas gambar saya, tetapi secara hitungan ia harus jatuh pada perpanjangan garis yang sama. Kalau tidak, ada yang salah, entah hitungannya atau jenis perbandingannya. Inilah fungsi grafik yang sering terlupakan: ia bukan hiasan sesudah hitungan selesai, melainkan alat untuk memeriksa hitungan itu sendiri.

## Tiga kesalahan yang sering saya lihat

Kesalahan pertama adalah skala sumbu yang tidak konsisten. Siswa menggambar jarak dari 0 ke 3 sama dengan jarak dari 3 ke 6, padahal selisihnya berbeda, atau jarak antar ribuan tidak sama rata. Akibatnya titik-titik yang seharusnya segaris tampak menyebar, dan siswa menyimpulkan bahwa perbandingannya "tidak senilai", padahal yang tidak senilai adalah gambarnya. Di TikZ kesalahan ini sulit terjadi, karena jarak ditulis sebagai angka, bukan diperkirakan dengan mata.

Kesalahan kedua adalah garis yang dimulai dari titik pertama, bukan dari titik asal. Gambar seperti ini kehilangan ciri terpentingnya. Begitu saya meminta siswa menambahkan titik $(0, 0)$ dan menarik ulang garisnya, banyak dari mereka yang langsung berkata, "Oh, ternyata harus dari nol." Satu titik kecil itu mengubah cerita gambarnya.

Kesalahan ketiga adalah satu titik yang melenceng karena salah hitung, misalnya 3 buku ditulis Rp10.000, bukan Rp9.000. Di tabel, kesalahan ini mudah lolos karena angka-angka hanya berbaris ke bawah. Di grafik, ia langsung ketahuan: satu titik merah berdiri di luar garis, seperti orang yang keluar dari barisan. Saya justru senang ketika ini terjadi, karena kelas belajar bahwa grafik bisa "mengadu" dan menunjukkan di mana letak salahnya.

## Penutup: gambar yang menjaga kejujuran hitungan

Grafik perbandingan senilai yang baik tidak perlu ramai. Ia hanya perlu tiga hal: skala yang konsisten, titik-titik yang jujur dari tabel, dan garis yang berangkat dari titik asal. TikZ membantu saya menjaga ketiganya, karena setiap keputusan harus ditulis sebagai angka sebelum gambarnya muncul. Dan ketika gambarnya sudah benar, ia bekerja sendiri di kelas: siswa tidak lagi menghafal bahwa perbandingan senilai itu "garis lurus lewat titik asal", melainkan melihatnya dengan mata kepala sendiri, lengkap dengan satu titik merah yang melenceng setiap kali ada hitungan yang salah.

> 📎 **Berkas TikZ lengkap:** [grafik-perbandingan-senilai.tex](tex/grafik-perbandingan-senilai.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
