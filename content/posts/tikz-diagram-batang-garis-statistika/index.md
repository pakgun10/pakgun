---
title: "Dari Satu Tabel ke Dua Diagram: Menggambar Diagram Batang dan Garis dengan TikZ"
date: 2026-10-24T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lanjutan seri statistika TikZ: menggambar diagram batang dan diagram garis dari data kelas yang nyata — dengan skala sumbu yang jujur dan pola kode yang siap pakai ulang."
featuredImage: "featured-image.png"

tags: ["TikZ", "Statistika", "Diagram Batang", "Diagram Garis", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Kemarin saya menulis tentang diagram lingkaran yang bisa berbohong kalau sektornya digambar asal-asalan — dan tentang kebiasaan baru saya: menghitung sudutnya dulu dengan TikZ sebelum menggambarnya. Artikel itu saya anggap sebagai pembuka seri. Hari ini saya melanjutkannya ke dua diagram yang paling sering muncul di buku siswa SMP: diagram batang dan diagram garis.

Data yang saya pakai nyata, hasil survei kecil di kelas 8C pekan lalu. Saya hanya bertanya satu pertanyaan: "Kalian berangkat ke sekolah naik apa?" Hasilnya: jalan kaki 8 anak, sepeda 6 anak, diantar orang tua 14 anak, dan angkutan umum 4 anak. Total 32 anak — pas satu kelas, tidak perlu dibulatkan, tidak perlu dikarang.

<!--more-->

## Diagram batang: biarkan mata membandingkan dengan jujur

Kelebihan diagram batang dibanding diagram lingkaran sebenarnya sederhana: mata kita pandai membandingkan tinggi. Tidak perlu mengira-ira sudut seperti kemarin. Tetapi kejujuran itu punya satu syarat mutlak: skala sumbu tegaknya harus mulai dari nol.

Saya pernah melanggar syarat ini, dan pelanggarannya memalukan karena terjadi di depan kelas. Waktu itu saya memproyeksikan diagram batang buatan sendiri — sumbu frekuensinya saya mulai dari angka 4 supaya gambarnya "lebih penuh". Batang "diantar orang tua" (14) jadi terlihat hampir tiga kali lipat batang "angkutan umum" (4). Seorang anak mengangkat tangan: "Pak, kok kelihatannya bedanya jauh banget, padahal 14 sama 4?" Dia benar. Selisih 10 dari skala yang dipotong 4 tampak seperti selisih 30. Sejak hari itu aturan saya sederhana: sumbu batang selalu mulai dari nol, tanpa pengecualian.

## Dari tabel ke batang: polanya sederhana

Kode TikZ untuk diagram batang sebenarnya lebih mudah daripada diagram lingkaran kemarin. Tidak ada sudut, tidak ada `arc` — hanya persegi panjang. Triknya cuma satu: tentukan dulu berapa anak yang diwakili 1 cm, lalu tinggi batang dihitung dari situ.

Dengan data kelas 8C, saya pakai skala 1 cm = 4 anak. Tinggi batangnya berarti $h = \dfrac{f}{4}$ cm. Batang "jalan kaki" yang frekuensinya 8 menjadi 2 cm, batang "diantar" yang frekuensinya 14 menjadi 3,5 cm. Polanya seperti ini:

```latex
\begin{tikzpicture}
  % sumbu
  \draw[->] (0,0) -- (7,0);   % sumbu kategori
  \draw[->] (0,0) -- (0,5);   % sumbu frekuensi
  % skala sumbu: 1 cm = 4 anak, mulai dari nol
  \foreach \y/\label in {0/0, 1/4, 2/8, 3/12, 4/16}
    \node[left] at (0,\y) {\label};
  % batang: lebar 1 cm, tinggi = frekuensi / 4
  \fill[teal!60]   (0.5,0) rectangle (1.5,2);    % jalan kaki: 8
  \fill[orange!70] (2,0)   rectangle (3,1.5);    % sepeda: 6
  \fill[blue!50]   (3.5,0) rectangle (4.5,3.5);  % diantar: 14
  \fill[red!50]    (5,0)   rectangle (6,1);      % angkot: 4
  % label kategori dan angka di atas batang
  \node at (1,2.3) {8}; \node[below] at (1,-0.2) {Jalan kaki};
  \node at (2.5,1.8) {6}; \node[below] at (2.5,-0.2) {Sepeda};
  \node at (4,3.8) {14}; \node[below] at (4,-0.2) {Diantar};
  \node at (5.5,1.3) {4}; \node[below] at (5.5,-0.2) {Angkot};
\end{tikzpicture}
```

Angka frekuensi saya tulis di atas setiap batang. Ini kebiasaan kecil yang saya anjurkan ke siswa: diagram yang baik tidak memaksa pembacanya menebak nilai dari tinggi batang — ia menuliskannya.

## Diagram garis: untuk cerita yang bergerak

Data kedua saya ambil dari catatan nilai: rata-rata ulangan harian Matematika kelas 8C, dari UH1 sampai UH5 — 68, 71, 70, 76, dan 82. Ini data waktu, dan data waktu punya bahasanya sendiri: diagram garis.

Ada satu kesalahan yang hampir selalu muncul setiap tahun: anak menggambar diagram garis untuk data kategori, misalnya menghubungkan titik "sepeda" ke titik "diantar" dengan satu garis miring. Garis itu tidak punya makna — tidak ada "perjalanan" antara sepeda dan diantar. Maka aturan yang saya tanamkan: garis hanya boleh menghubungkan titik-titik yang berurutan dalam waktu. Selain itu, jangan.

Untuk sumbunya, diagram garis boleh tidak mulai dari nol — asalkan jelas. Saya pakai rentang 60 sampai 90 dengan garis bantu tipis tiap 10 poin, sehingga kemiringan garisnya memang mencerminkan perubahannya:

```latex
\begin{tikzpicture}
  % sumbu: x = ulangan ke-, y = 60..90
  \draw[->] (0,0) -- (6.5,0);
  \draw[->] (0,0) -- (0,4);
  \foreach \y/\label in {0/60, 1/70, 2/80, 3/90}
    { \draw[dotted] (0,\y) -- (6,\y);
      \node[left] at (0,\y) {\label}; }
  % titik data: x = 1..5, y = (nilai-60)/10
  \draw[thick, blue] (1,0.8) -- (2,1.1) -- (3,1.0)
                     -- (4,1.6) -- (5,2.2);
  \foreach \x/\v in {1/68, 2/71, 3/70, 4/76, 5/82}
    { \fill[blue] (\x,{(\v-60)/10}) circle (2.5pt);
      \node[above] at (\x,{(\v-60)/10}) {\v}; }
  \foreach \x in {1,2,3,4,5}
    \node[below] at (\x,-0.2) {UH\x};
\end{tikzpicture}
```

Coba perhatikan bentuk garisnya: turun sedikit di UH3, lalu menanjak dua kali. Garis seperti itu punya cerita — dan di kelas saya, cerita itu nyata: UH3 adalah ulangan pecahan yang memang jebakan, lalu dua ulangan berikutnya naik setelah kami remedial bersama. Diagram garis yang jujur tidak hanya menampilkan angka; ia menyimpan kronologi usaha.

## Satu pola untuk dipakai ulang

Kedua gambar di atas sudah saya satukan dalam satu berkas `.tex` yang terlampir di akhir artikel. Isinya dokumen LaTeX utuh yang siap dikompilasi — dua gambar dalam satu berkas, masing-masing diberi komentar baris per baris supaya mudah diubah. Untuk memakainya di kelas sendiri, yang perlu diganti hanya tiga hal: frekuensinya, label kategorinya, dan skalanya kalau datanya jauh lebih besar. Rumus tingginya tetap sama: $h = \dfrac{f}{\text{skala}}$.

Saya tidak mengajarkan kode ini ke siswa — sama seperti artikel kemarin, ini perkakas guru. Yang sampai ke tangan siswa adalah gambarnya: di soal ulangan, di bahan ajar, dan di slide pembahasan.

## Penutup

Seri statistika ini bermula dari satu kekesalan kecil: diagram yang bohong. Ternyata memperbaikinya tidak butuh perangkat mahal — hanya butuh keberanian menghitung sebelum menggambar, dan disiplin menjaga sumbu tetap jujur. Diagram batang untuk membandingkan kategori, diagram garis untuk mengikuti waktu, diagram lingkaran untuk melihat proporsi. Tiga diagram, tiga bahasa, satu aturan yang sama: gambar harus setia pada data.

Kalau Bapak/Ibu mencoba pola di atas dan menemukan cara yang lebih ringkas — misalnya memakai `\foreach` untuk menggambar semua batang sekaligus — saya menunggu di kolom komentar. Seri ini masih berlanjut.

---

> 📎 **Berkas TikZ lengkap:** [diagram-batang-garis.tex](tex/diagram-batang-garis.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
