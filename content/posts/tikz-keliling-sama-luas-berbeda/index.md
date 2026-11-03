---
title: "Pagar yang Sama, Luas yang Berbeda: Menjelajah Keliling Tetap dengan TikZ"
date: 2026-11-01T15:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Soal pagar 24 meter yang saya kira selesai dalam lima menit ternyata menyembunyikan sebuah puncak: keenam kebun berkeliling sama yang digambar TikZ, dan parabola yang menjelaskan kenapa persegi selalu menang."
featuredImage: "featured-image.png"
tags: ["TikZ", "Keliling", "Luas", "Persegi Panjang", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]
math:
  enable: true
---

Minggu lalu, di kelas VIII, saya memberikan satu soal yang saya kira akan selesai dalam lima menit. "Bapak punya kawat pagar sepanjang 24 meter. Kawat itu dipakai mengelilingi kebun berbentuk persegi panjang. Berapa panjang dan lebarnya supaya luas kebun paling besar?" Kelas langsung ramai menghitung, dan memang lima menit kemudian jawaban mulai berdatangan. Panjang 5, lebar 7, luas 35 meter persegi — itu yang paling banyak muncul. Jawaban itu benar menurut kunci. Tetapi ketika saya bertanya balik, "Siapa yang bisa meyakinkan saya bahwa tidak ada kebun lain yang luasnya lebih dari 35?", kelas yang tadinya ramai tiba-tiba hening.

Ada yang menyerah dengan senyum, ada yang membuka lagi bukunya, dan seorang siswa di baris belakang bergumam, "Lha, yang ditanya toh cuma satu jawaban, Pak." Di situlah letak masalahnya. Selama ini kebanyakan soal yang mereka kenal memang berhenti di satu jawaban: hitung, tulis, selesai. Soal tadi berbeda — ia tidak meminta satu jawaban, melainkan meminta keyakinan bahwa tidak ada jawaban lain yang lebih baik. Dan keyakinan semacam itu tidak lahir dari satu kali hitungan; ia lahir dari melihat seluruh kemungkinannya.

<!--more-->

## Satu pagar, banyak kebun

Karena kelilingnya tetap 24 meter, panjang dan lebar kebun tidak bisa dipilih bebas. Kalau panjangnya $p$ dan lebarnya $l$, syaratnya:

$$2(p + l) = 24 \quad\Rightarrow\quad p + l = 12$$

Setiap pasangan bilangan yang berjumlah 12 adalah satu kandidat kebun: panjang 11 lebar 1, panjang 10 lebar 2, dan seterusnya sampai panjang 6 lebar 6. Enam kandidat itu saya daftarkan beserta luasnya: $11 \times 1 = 11$, $10 \times 2 = 20$, $9 \times 3 = 27$, $8 \times 4 = 32$, $7 \times 5 = 35$, dan $6 \times 6 = 36$.

Tabel seperti ini biasa digambar siswa. Tetapi angka di tabel tidak berbicara sekuat bentuk. Maka malam harinya saya menggambar keenam kebun itu dengan TikZ, sejajar dalam satu baris, dengan satu aturan yang tidak bisa ditawar: skala gambarnya harus benar-benar proporsional. Kebun $11 \times 1$ harus terlihat gepeng, kebun $6 \times 6$ harus terlihat nyaris persegi, dan luas yang tampak di layar harus sesuai angka di tabel. Kalau gambar tidak setia pada ukuran, ia hanya akan mengulang kebiasaan lama: menggambar asal terlihat.

```latex
\begin{tikzpicture}[x=0.55cm, y=0.55cm]
  % keenam kebun, keliling semuanya 24 m (p + l = 6 satuan)
  \draw[aksen, thick] (0,0) rectangle (5.5,0.5);
  \node[white, font=\footnotesize] at (2.75,0.25) {$11\times1$};
  \node[white, font=\footnotesize, below] at (2.75,0) {$L=11$};
  \draw[aksen, thick] (6.5,0) rectangle (11.5,1);
  \node[white, font=\footnotesize] at (9,0.5) {$10\times2$};
  \node[white, font=\footnotesize, below] at (9,0) {$L=20$};
  % ... pola yang sama untuk 9x3, 8x4, 7x5, dan 6x6
\end{tikzpicture}
```

![Enam kebun dengan pagar yang sama panjang, tetapi luas yang berbeda](gambar-kebun-keliling-sama.png)
*Keenam kebun memakai pagar 24 meter yang sama. Dari kiri ke kanan luasnya terus bertambah — dan bentuknya makin mendekati persegi.*

Gambar itu sering membuat kelas terdiam sejenak, bukan karena rumit, melainkan karena jujur. Pagar yang sama panjang bisa memagari kebun seluas 11 meter persegi, tetapi bisa juga 36 meter persegi — lebih dari tiga kali lipat — tanpa menambah seinci pun kawat. Yang berubah bukan panjang pagarnya, melainkan cara kawat itu membagi dirinya menjadi panjang dan lebar.

## Kenapa justru persegi yang menang

Dari tabel itu muncul pola yang menarik. Setiap kali panjang dikurangi satu dan lebar ditambah satu, luasnya naik — tetapi kenaikannya makin kecil. Dari 11 ke 20 naik 9, dari 20 ke 27 naik 7, dari 27 ke 32 naik 5, dari 32 ke 35 naik 3, dan dari 35 ke 36 tinggal naik 1. Kenaikan yang semakin melambat ini adalah tanda bahwa luas punya puncak. Dan dalam daftar ini tidak ada kandidat lagi setelah $6 \times 6$, karena kebun $5 \times 7$ sebenarnya sama saja dengan kebun $7 \times 5$ — kita hanya membacanya dari arah yang berlainan.

Untuk melihat puncaknya dengan mata, saya mengubah daftar menjadi grafik. Luas kebun ternyata bergantung pada panjangnya:

$$L(p) = p \times (12 - p) = 12p - p^2$$

Kalau $p$ berjalan dari 0 sampai 12, luasnya naik, mencapai puncak di $p = 6$ dengan $L = 36$, lalu turun kembali. Bentuk kurvanya mereka akan kenal lebih dekat di kelas IX: parabola.

```latex
\begin{tikzpicture}[x=0.6cm, y=0.13cm]
  \draw[->, white] (-0.5,0) -- (12.9,0) node[below left, white] {$p$};
  \draw[->, white] (0,-1.5) -- (0,41) node[below left, white] {$L$};
  \draw[white!40, dashed] (6,0) -- (6,36) -- (0,36);
  \draw[aksen, very thick, domain=0:12, samples=120] plot (\x, {12*\x - \x*\x});
  \foreach \p in {1,...,11} {
    \pgfmathsetmacro\y{12*\p - \p*\p}
    \fill[aksen] (\p,\y) circle (2.2pt);
  }
  \node[white, font=\footnotesize, above right] at (6,36) {$L_{\text{maks}} = 36$};
\end{tikzpicture}
```

![Grafik luas kebun terhadap panjangnya: parabola dengan puncak di panjang 6 meter](gambar-parabola-luas.png)
*Luas sebagai fungsi panjang, $L(p) = 12p - p^2$. Puncaknya jatuh tepat di $p = 6$ — saat kebun berubah menjadi persegi.*

Bagi saya, grafik ini adalah jembatan yang tidak ingin saya lewatkan. Di kelas VIII, soal ini masih bisa tuntas dengan tabel dan grafik titik-titik. Di kelas IX, ketika fungsi kuadrat datang, saya menampilkan kurva yang sama lagi: $12p - p^2$ adalah $-p^2 + 12p$ dengan $a = -1$, parabola yang terbuka ke bawah, dan titik puncaknya $p = -\frac{b}{2a} = 6$. Yang dulu mereka temukan lewat daftar dan gambar, kini muncul kembali sebagai rumus. Rumus itu tidak lagi terasa turun dari langit, karena mereka sudah pernah melihat puncaknya sendiri sebelum tahu namanya.

## Dua jawaban yang membuka diskusi

Setelah beberapa kali mengajarkan soal ini, ada dua jawaban siswa yang paling sering memicu diskusi panjang.

Pertama, "Pak, $6 \times 6$ itu bukan persegi panjang." Keluhan ini selalu muncul, dan selalu saya syukuri. Di sinilah definisi dibedah di depan kelas: syarat persegi panjang hanyalah sisi berhadapan sama panjang dan keempat sudutnya siku. Persegi memenuhi semua syarat itu — maka persegi adalah persegi panjang, sebuah persegi panjang yang istimewa. Jika kita menolak persegi dari daftar kandidat, kita membuang justru kebun yang paling luas. Siswa yang tadinya yakin 6×6 "curang" biasanya berubah pikiran setelah menyadari bahwa aturan persegi panjang tidak mensyaratkan sisi-sisinya berbeda.

Kedua, siswa yang menjawab 35 dan percaya itu maksimal karena "kelihatannya paling besar di antara yang lain". Kalimat "kelihatannya" adalah pintu masuk yang bagus untuk menguji soal yang sama dengan pagar berbeda. Coba pagar 30 meter: kini $p + l = 15$, dan puncaknya tidak lagi jatuh di bilangan bulat — kebun $7 \times 8$ luasnya 56, padahal kebun $7{,}5 \times 7{,}5$ luasnya $56{,}25$. Kalau panjang boleh tidak bulat, persegi tetap menang; kalau panjang harus bulat, kita berhenti di kandidat bulat terdekat. Percakapan seperti inilah yang menggeser kelas dari "mencari jawaban" menjadi "mencari alasan" — dan grafik TikZ itu selalu siap dipanggil sebagai saksi.

## Penutup: soal yang menyembunyikan puncak

Soal pagar 24 meter itu kini menjadi salah satu soal favorit saya, justru karena saya pernah menganggapnya sepele. Ia terlihat seperti soal hitungan biasa, tetapi menyimpan dua pelajaran yang jarang muncul bersamaan: bahwa daftar kemungkinan bisa dibaca sebagai pola, dan bahwa pola itu berupa puncak yang bisa digambar.

Kalau Bapak dan Ibu ingin mencobanya di kelas, saran saya sederhana: jangan berhenti di jawaban 5×7. Minta siswa menuliskan semua kandidat kebunnya, lalu biarkan mereka sendiri yang menyadari kenaikan luasnya yang makin melambat. Gambar keenam kebunnya — yang seperti di artikel ini, dengan skala yang jujur — baru setelah mereka selesai menghitung, bukan sebelum. Puncak yang ditemukan sendiri selalu lebih meyakinkan daripada puncak yang ditunjuk.

> 📎 **Berkas TikZ lengkap:** [keliling-sama-luas-berbeda.tex](tex/keliling-sama-luas-berbeda.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti panjang pagarnya untuk membuat variasi soal Anda sendiri.
