---
weight: 1
title: "Dua Busur Lagi, Sudut Terbagi Dua: Menggambar Garis Bagi Sudut dengan TikZ"
date: 2026-11-02T16:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Membagi sudut menjadi dua sama besar tidak harus dengan mengukur lalu menghitung: dua busur jangka yang berpotongan sudah cukup menemukan garis baginya, dan TikZ bisa menggambar setiap langkah itu persis seperti di atas kertas."
featuredImage: "featured-image.png"
tags: ["TikZ", "LaTeX", "Sudut", "Konstruksi", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]
math:
  enable: true
---

Pekan lalu, di kelas VII, saya meminta siswa membagi sebuah sudut menjadi dua bagian yang sama besar. Hampir semua langsung meraih busur derajat: ukur sudutnya, bagi dua angkanya, lalu tandai hasilnya. Cara itu tidak salah, dan untuk banyak keperluan ia cukup. Tetapi ada satu hal yang hilang dari cara itu: siswa tidak pernah melihat *mengapa* garis yang ia tarik memang membagi sudut itu sama rata. Ia hanya percaya pada angka yang ia hitung.

Karena itu, di pertemuan berikutnya, saya mengajak kelas itu mencoba cara yang lebih tua: konstruksi dengan jangka. Tidak ada busur derajat sama sekali. Yang ada hanya jangka, penggaris, dan tiga busur yang saling bertemu. Ketika garis bagi itu akhirnya tertarik, seorang siswa berkomentar pelan, "Oh, ternyata jangka yang menemukan titiknya, Pak." Komentar itulah yang membuat saya menulis artikel ini. Dengan TikZ, setiap langkah konstruksi itu bisa digambar persis seperti langkah di atas kertas, lengkap dengan busur-busnya yang masih terlihat.

<!--more-->

## Langkah pertama: gambar sudutnya dulu

Segala konstruksi dimulai dari sesuatu yang sudah pasti: sebuah sudut. Saya memakai sudut $60^\circ$ di titik $A$, dengan satu kaki mendatar ke kanan dan satu kaki miring ke atas. Saya sengaja memakai sudut yang besarnya enak dibaca, supaya siswa bisa memeriksa sendiri bahwa hasil akhirnya memang dua sudut $30^\circ$. Titik $A$ saya beri nama sejak awal, karena ia akan menjadi pusat jangka pada langkah berikutnya, dan semua penjelasan akan merujuk kepadanya.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2.5,4.33);
  \draw[thick] (A) -- (B);
  \draw[thick] (A) -- (C);
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above] at (C) {$C$};
\end{tikzpicture}
```

Satu kebiasaan yang saya tekankan di kelas: gambar kakinya cukup panjang, supaya busur pada langkah berikutnya tampil utuh dan mudah diikuti.

## Langkah kedua: satu busur dari titik sudut

Sekarang jangka mulai bekerja. Jarum jangka ditancapkan di $A$, lalu jangka dibuka selebar 3 cm dan digoreskan memotong kedua kaki sudut. Di atas kertas, goresan itu berupa satu busur yang menghubungkan kedua kaki. Di TikZ, saya menggambarnya sebagai lingkaran penuh yang dipotong tampilannya hanya pada bagian di dalam sudut, supaya yang tampak hanyalah busur itu, persis seperti goresan jangka.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2.5,4.33);
  \draw[thick] (A) -- (B);
  \draw[thick] (A) -- (C);
  \begin{scope}
    \clip (A) -- (B) -- (C) -- cycle;
    \draw[dashed, blue] (A) circle (3);
  \end{scope}
  \fill (3,0) circle (2pt);
  \fill (1.5,2.598) circle (2pt);
  \node[below] at (3,0) {$P$};
  \node[left] at (1.5,2.598) {$Q$};
\end{tikzpicture}
```

Busur itu memotong kaki mendatar di titik $P$ dan kaki miring di titik $Q$. Dua titik inilah kunci seluruh konstruksi. Karena keduanya terletak pada busur yang sama dengan pusat $A$, jarak $AP$ sama dengan jarak $AQ$, yaitu 3 cm. Kesamaan jarak inilah yang nanti menjamin kedua belahan sudut itu sama besar. Saya meminta siswa menandai $P$ dan $Q$ dengan jelas, karena langkah berikutnya berpusat pada kedua titik itu, bukan lagi pada $A$.

## Langkah ketiga: dua busur yang saling memotong

Inilah langkah yang paling memuaskan untuk dilihat. Jangka dipindahkan ke $P$, dibuka dengan lebar yang sama seperti sebelumnya, lalu digoreskan ke dalam sudut. Kemudian hal yang sama dilakukan dari $Q$, dengan lebar jangka yang tidak diubah. Kedua goresan itu bertemu di satu titik di dalam sudut, yang saya namai $R$. Di TikZ, kedua busur itu saya gambar dengan perintah yang sama seperti sebelumnya: lingkaran penuh yang dipotong tampilannya.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2.5,4.33);
  \draw[thick] (A) -- (B);
  \draw[thick] (A) -- (C);
  \begin{scope}
    \clip (0,-0.5) rectangle (6,5);
    \draw[dashed, red] (3,0) circle (3);
    \draw[dashed, red] (1.5,2.598) circle (3);
  \end{scope}
  \fill (3,0) circle (2pt);
  \fill (1.5,2.598) circle (2pt);
  \fill (4.5,2.598) circle (2pt);
  \node[below] at (3,0) {$P$};
  \node[left] at (1.5,2.598) {$Q$};
  \node[right] at (4.5,2.598) {$R$};
\end{tikzpicture}
```

Perhatikan bahwa titik $R$ berada di $(4{,}5;\ 2{,}598)$. Angka itu bukan tebakan: jarak $R$ ke $P$ tepat 3 cm, dan jarak $R$ ke $Q$ juga tepat 3 cm, karena kedua busur digambar dengan lebar jangka yang sama. Di kelas, saya sengaja menunjukkan perhitungan ini, supaya siswa melihat bahwa $R$ ditemukan oleh jangka, bukan dipilih sesuka hati. Kalau lebar jangka diubah di tengah jalan, kedua busur itu bisa tidak bertemu sama sekali, atau bertemu di tempat yang salah.

## Langkah keempat: tarik garisnya dari titik sudut

Langkah terakhir adalah yang paling sederhana, tetapi paling sering dikerjakan tergesa-gesa: tarik garis dari $A$ melalui $R$, dan teruskan sedikit melewatinya. Garis itulah garis bagi sudut. Ia membagi sudut $60^\circ$ menjadi dua sudut $30^\circ$, dan saya menandainya dengan dua tanda busur kecil yang sama di kedua belahan, supaya kesamaannya terlihat tanpa harus mengukur lagi.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2.5,4.33);
  \draw[thick] (A) -- (B);
  \draw[thick] (A) -- (C);
  \draw[thick, blue] (A) -- (5.196,3);
  \fill (3,0) circle (2pt);
  \fill (1.5,2.598) circle (2pt);
  \fill (4.5,2.598) circle (2pt);
  \node[below] at (3,0) {$P$};
  \node[left] at (1.5,2.598) {$Q$};
  \node[right] at (4.5,2.598) {$R$};
\end{tikzpicture}
```

Mengapa garis ini dijamin membagi sudut sama rata? Jawabannya ada pada dua segitiga yang terbentuk: segitiga $APR$ dan segitiga $AQR$. Ketiga sisinya sama panjang berpasangan: $AP = AQ$ karena keduanya jari-jari busur pertama, $PR = QR$ karena keduanya jari-jari busur kedua, dan $AR$ adalah sisi bersama. Dua segitiga yang ketiga sisinya sama panjang adalah kongruen, sehingga sudut di $A$ pada keduanya pun sama besar. Inilah momen yang saya tunggu di kelas: ketika siswa menyadari bahwa kekongruenan yang selama ini hanya ia hafal, ternyata sedang bekerja di depan matanya.

## Tiga kesalahan yang paling sering saya temui

Selama mengajar konstruksi ini, tiga kesalahan muncul berulang-ulang. Pertama, lebar jangka diubah antara busur pertama dan busur kedua, sehingga $PR$ tidak lagi sama dengan $QR$ dan garis yang tertarik meleset dari tengah. Kedua, busur kedua dibuka terlalu kecil, sehingga kedua busur tidak saling berpotongan dan siswa kebingungan mencari $R$ yang tidak ada. Ketiga, garis bagi ditarik dari $R$ ke arah sembarang, bukan dari $A$ melalui $R$ — padahal garis bagi harus berpangkal di titik sudut. Ketiga kesalahan ini mudah dicegah dengan satu kalimat yang saya ulang setiap tahun: jangka tidak boleh diubah lebarnya sampai $R$ ditemukan.

Konstruksi garis bagi sudut ini adalah pintu masuk yang baik menuju konstruksi lain, seperti membagi ruas garis atau mengkonstruksi segitiga dari tiga sisinya. Polanya sama: satu titik ditemukan oleh perpotongan dua busur, bukan oleh tebakan mata. Begitu siswa merasakan sendiri bahwa jangka bisa menemukan titik yang tepat, ia mulai memandang jangka bukan lagi sebagai alat menggambar lingkaran, melainkan sebagai alat berpikir.

📎 **Berkas TikZ lengkap:** [garis-bagi-sudut.tex](tex/garis-bagi-sudut.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
