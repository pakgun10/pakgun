---
weight: 1
title: "Dua Busur, Satu Titik: Mengkonstruksi Segitiga dari Tiga Sisinya dengan TikZ"
date: 2026-11-02T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Segitiga yang digambar kira-kira jarang punya sisi sesuai ukuran; dengan dua busur jangka dari ujung alasnya, titik sudut ketiga ditemukan, bukan ditebak — dan TikZ menggambar langkah itu persis seperti di atas kertas."
featuredImage: "featured-image.png"
tags: ["TikZ", "LaTeX", "Segitiga", "Konstruksi", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]
math:
  enable: true
---

Pernahkah Anda meminta siswa menggambar segitiga dengan sisi 6 cm, 5 cm, dan 4 cm, lalu hasilnya bermacam-macam? Ada yang menggambar segitiga bagus, tetapi ketika diukur dengan penggaris, sisinya 6 cm, 5,5 cm, dan 3 cm. Yang paling sering terjadi: siswa menggambar titik sudut ketiga dulu, kira-kira di tengah atas, lalu menghubungkannya dan berharap ukurannya cocok. Harapan itu jarang terkabul, karena titik yang diletakkan dengan perasaan tidak punya alasan untuk berjarak tepat 5 cm dari satu ujung dan 4 cm dari ujung lainnya.

Di sinilah jangka menjadi guru yang paling jujur. Jangka tidak menebak. Kalau jangka dibuka 5 cm dan ujung jarumnya ditancapkan di satu ujung alas, maka setiap titik pada busurnya berjarak tepat 5 cm dari ujung itu. Kalau jangka kedua dibuka 4 cm dari ujung alas yang lain, setiap titik pada busurnya berjarak tepat 4 cm dari ujung tersebut. Titik yang memenuhi kedua syarat sekaligus hanya ada di satu tempat: perpotongan kedua busur itu. Itulah titik sudut ketiga, ditemukan, bukan ditebak. Artikel ini menunjukkan cara menggambar langkah itu dengan TikZ, persis seperti langkah di atas kertas.

<!--more-->

## Langkah pertama: gambar alasnya dulu

Segala konstruksi dimulai dari sesuatu yang sudah pasti. Di sini yang pasti adalah alasnya: ruas garis $AB$ sepanjang 6 cm. Saya menggambarnya mendatar, dengan $A$ di kiri dan $B$ di kanan, supaya busur-busur di langkah berikutnya mudah dibaca. Titik $A$ dan $B$ saya beri nama, karena keduanya akan menjadi pusat jangka.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (6,0);
  \draw[thick] (A) -- (B);
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
\end{tikzpicture}
```

Satu kebiasaan kecil yang saya tekankan di kelas: beri nama titiknya sejak awal. Tanpa nama, penjelasan "busur dari titik ini" menjadi kabur, dan siswa yang tertinggal akan kesulitan mengikuti langkah berikutnya. Dengan nama $A$ dan $B$, kalimat "jangka berpusat di $A$" langsung punya alamat yang jelas.

## Langkah kedua: dua busur yang bertemu di satu titik

Sekarang bagian yang paling memuaskan. Dari $A$, saya menggambar busur dengan jari-jari 5 cm, yaitu panjang sisi $AC$ yang diinginkan. Dari $B$, saya menggambar busur dengan jari-jari 4 cm, yaitu panjang sisi $BC$. Di TikZ, cara paling mudah adalah menggambar dua lingkaran penuh, lalu memotong tampilannya hanya pada bagian atas alas dengan perintah `clip`. Yang tampak di gambar hanyalah busur-busur di atas alas, persis seperti goresan jangka di kertas, tanpa lingkaran penuh yang mengganggu.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (6,0);
  \draw[thick] (A) -- (B);
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \begin{scope}
    \clip (-0.5,0) rectangle (6.5,4.5);
    \draw[dashed, blue] (A) circle (5);
    \draw[dashed, red] (B) circle (4);
  \end{scope}
  \fill (3.75,3.31) circle (2pt);
  \node[above] at (3.75,3.31) {$C$};
\end{tikzpicture}
```

Perhatikan titik $C$ pada koordinat $(3{,}75;\ 3{,}31)$. Angka itu bukan tebakan saya. Titik itu berjarak 5 cm dari $A$ dan 4 cm dari $B$ sekaligus, karena ia terletak pada kedua busur. Menggeser titik itu sedikit saja sudah merusak kedua jarak itu. Inilah pelajaran yang paling berharga dari konstruksi ini: titik sudut ketiga tidak dipilih, melainkan ditemukan oleh dua syarat yang bertemu. Warna busur yang berbeda — biru untuk jangka dari $A$, merah untuk jangka dari $B$ — membantu siswa melihat syarat mana yang dipenuhi oleh busur yang mana.

## Langkah ketiga: hubungkan, lalu beri nama sisinya

Setelah titik $C$ ditemukan, sisanya mudah: hubungkan $C$ ke $A$ dan ke $B$, lalu tuliskan panjang setiap sisi di dekatnya. Segitiga $ABC$ kini lengkap, dan setiap sisinya bisa diverifikasi dengan penggaris: $AB = 6$ cm, $AC = 5$ cm, dan $BC = 4$ cm.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (6,0);
  \coordinate (C) at (3.75,3.31);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above] at (C) {$C$};
  \node[below] at (3,0) {$6$ cm};
  \node[left] at (1.9,1.65) {$5$ cm};
  \node[right] at (4.9,1.65) {$4$ cm};
\end{tikzpicture}
```

Saya sengaja menuliskan panjang sisi pada gambar jadi, bukan hanya di soal. Siswa yang melihat gambar ini tanpa membaca soal pun langsung tahu segitiga apa yang sedang dibahas. Dan kalau ia ragu, ia bisa mengukur sendiri: segitiga ini tidak meminta dipercaya, ia meminta diperiksa.

## Tiga kesalahan yang sering saya temui

Pertama, busur yang digambar terlalu pendek sehingga tidak bertemu. Ini biasanya terjadi karena siswa menggambar busur kecil di dekat ujung alas, bukan busur yang membentang ke arah tengah. Solusinya sederhana: gambar busur yang cukup panjang, melewati perkiraan letak titik potongnya, karena perpotongan itu tidak bisa ditebak posisinya sebelum busur digambar.

Kedua, jari-jari jangka yang tertukar: busur dari $A$ dibuka 4 cm, busur dari $B$ dibuka 5 cm. Segitiga yang terbentuk tetap bersisi 6 cm, 5 cm, dan 4 cm, tetapi titik $C$-nya bergeser dan nama sisinya tertukar. Ini bukan kesalahan besar, tetapi ia mengacaukan pembahasan berikutnya kalau guru membahas sisi $AC$ sementara gambar siswa menunjukkan sisi yang lain. Karena itu saya selalu meminta siswa menyebutkan dengan lantang, "Dari $A$, lima sentimeter," sebelum menggoreskan busurnya.

Ketiga, dan ini yang paling mendasar, adalah ketika dua busur sama sekali tidak bertemu. Cobalah meminta segitiga bersisi 6 cm, 3 cm, dan 2 cm. Busur dari $A$ berjari-jari 3 cm dan busur dari $B$ berjari-jari 2 cm tidak akan pernah bersentuhan, karena $3 + 2$ masih kurang dari 6. Konstruksi yang gagal ini justru hadiah: ia memperlihatkan, tanpa rumus apa pun, mengapa jumlah dua sisi segitiga harus lebih besar daripada sisi ketiganya. Kalau busurnya tidak bertemu, segitiganya memang tidak ada.

## Penutup: dari jangka ke TikZ, pesannya sama

Menggambar dengan TikZ tidak menggantikan jangka di tangan siswa. Yang ia gantikan adalah papan tulis yang gambarnya mudah bergeser dan sulit diulang dengan ukuran yang sama persis. Dengan kode di atas, gambar konstruksi yang saya tampilkan di kelas hari ini akan sama persis ketika saya tampilkan lagi minggu depan, dan sama persis ketika siswa membukanya di rumah. Tetapi pesannya tetap pesan jangka: dalam matematika, titik yang benar tidak ditebak, melainkan ditemukan dari syarat-syarat yang dipenuhi bersamaan. Sekali siswa merasakan sendiri perpotongan dua busur itu, ia tidak akan lagi menggambar segitiga dengan perasaan.

> 📎 **Berkas TikZ lengkap:** [konstruksi-segitiga-tiga-sisi.tex](tex/konstruksi-segitiga-tiga-sisi.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
