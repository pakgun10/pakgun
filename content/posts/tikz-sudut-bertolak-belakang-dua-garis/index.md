---
title: "Bertolak Belakang Sama Besar: Menggambar Dua Garis Berpotongan dengan TikZ"
date: 2026-11-09T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Dua garis berpotongan membentuk empat sudut, tetapi hanya ada dua ukuran: yang berhadapan sama besar. Di tulisan ini saya menggambarnya dengan TikZ — dua garis, empat label, dan tanda busur yang membuat pasangan sudutnya langsung terlihat."
featuredImage: "featured-image.png"

tags: ["TikZ", "Garis dan Sudut", "Sudut Bertolak Belakang", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu, di kelas VII, saya menggambar dua garis berpotongan di papan tulis dan menulis empat sudut di sekeliling titik potongnya. Lalu saya bertanya, "Berapa banyak ukuran sudut yang berbeda di gambar ini?" Sebagian besar siswa menjawab empat. Ada yang menjawab tiga. Hanya dua siswa yang menjawab dua — dan mereka benar. Empat sudut, tetapi hanya dua ukuran, karena sudut yang saling berhadapan selalu sama besar. Itulah sudut bertolak belakang, dan malam harinya saya menggambar ulang gambar papan tulis itu dengan TikZ supaya besok pagi gambarnya rapi, labelnya tidak bertabrakan, dan pasangan sudutnya langsung terlihat dari tanda busurnya.

<!--more-->

## Dua garis, empat sudut, dua ukuran

Bayangkan dua garis lurus yang saling berpotongan di satu titik $O$. Sebut garis pertama $AB$ dan garis kedua $CD$, dengan $O$ di tengah-tengah. Empat sudut terbentuk di sekeliling $O$: $\angle AOC$ di kiri atas, $\angle COB$ di kanan atas, $\angle BOD$ di kanan bawah, dan $\angle DOA$ di kiri bawah. Sudut yang berhadapan — $\angle AOC$ dengan $\angle BOD$, dan $\angle COB$ dengan $\angle DOA$ — disebut sudut bertolak belakang. Pasangan yang berdampingan, misalnya $\angle AOC$ dengan $\angle COB$, disebut sudut berpelurus karena keduanya membentuk garis lurus.

Kesamaannya bisa dibuktikan dengan satu baris penalaran. Garis $AB$ adalah garis lurus, sehingga $\angle AOC + \angle COB = 180^{\circ}$. Garis $CD$ juga garis lurus, sehingga $\angle BOD + \angle COB = 180^{\circ}$. Kedua jumlah itu sama, dan keduanya memuat $\angle COB$ yang sama, maka $\angle AOC$ harus sama dengan $\angle BOD$. Tidak ada yang perlu dihafal di sini: kalau dua sudut sama-sama berpelurus dengan sudut yang sama, keduanya sama besar. Saya menuliskan bukti pendek ini di papan sebelum menggambar, karena gambar tanpa alasan hanya menjadi hiasan — sedangkan alasan tanpa gambar sering tidak menempel di kepala siswa.

Angka konkretnya saya pilih yang mudah diingat: sudut kanan atas $50^{\circ}$. Maka sudut kiri bawah — pasangan bertolak belakangnya — juga $50^{\circ}$, tanpa perlu mengukur lagi. Dua sudut lainnya adalah $180^{\circ} - 50^{\circ} = 130^{\circ}$. Empat sudut, dua ukuran: $50^{\circ}$, $130^{\circ}$, $50^{\circ}$, $130^{\circ}$.

## Menggambar dua garis berpotongan di TikZ

Kunci gambar ini adalah memilih kemiringan garis kedua supaya sudutnya tepat $50^{\circ}$. Saya membuat garis pertama mendatar, lalu garis kedua saya tarik dengan sudut $50^{\circ}$ memakai koordinat polar TikZ — titik $(50:3.5)$ berarti jarak $3{,}5$ cm dari titik asal dengan arah $50^{\circ}$. Dengan begitu saya tidak perlu menghitung koordinat $x$ dan $y$ sendiri, dan sudut di gambar dijamin sama dengan sudut yang saya tulis di label.

```latex
\begin{tikzpicture}[scale=1.0, font=\large]
  % Titik potong O di tengah
  \coordinate (O) at (0, 0);
  % Garis AB mendatar
  \draw[thick] (-3.5, 0) -- (3.5, 0);
  % Garis CD miring 50 derajat, ditulis dengan koordinat polar
  \draw[thick] (230:3.5) -- (50:3.5);
  % Titik potong
  \fill (O) circle (2pt);
  \node[below right] at (O) {$O$};
  % Label ujung-ujung garis
  \node[left]  at (-3.5, 0) {$A$};
  \node[right] at (3.5, 0)  {$B$};
  \node[above] at (50:3.8)  {$C$};
  \node[below] at (230:3.8) {$D$};
\end{tikzpicture}
```

Perhatikan label $C$ dan $D$ saya letakkan sedikit di luar ujung garis, pada jarak $3{,}8$ cm, supaya tidak menempel pada garisnya. Label $O$ saya letakkan di kanan bawah titik potong, bukan tepat di titiknya, karena titik hitam kecil itu sudah cukup sebagai penanda.

## Menandai pasangan sudut dengan busur

Gambar dua garis saja belum cukup: siswa masih harus menebak sudut mana yang sama dengan yang mana. Di sinilah tanda busur bekerja. Sudut $50^{\circ}$ saya tandai dengan satu busur, sudut $130^{\circ}$ dengan dua busur. Konvensinya sederhana dan konsisten: busur yang sama artinya sudut yang sama besar. Saya memakai perintah `arc` dengan sudut awal dan akhir yang sama persis dengan arah garisnya — busur $0^{\circ}$ sampai $50^{\circ}$ untuk sudut kanan atas, dan busur $180^{\circ}$ sampai $230^{\circ}$ untuk pasangan bertolak belakangnya di kiri bawah.

```latex
  % Busur TUNGGAL untuk pasangan sudut 50 derajat
  \draw (O) ++(0:0.8)   arc (0:50:0.8);
  \draw (O) ++(180:0.8) arc (180:230:0.8);
  \node at (25:1.2)  {$50^{\circ}$};
  \node at (205:1.2) {$50^{\circ}$};
  % Busur GANDA untuk pasangan sudut 130 derajat
  \draw (O) ++(50:1.05)  arc (50:180:1.05);
  \draw (O) ++(50:1.25)  arc (50:180:1.25);
  \draw (O) ++(230:1.05) arc (230:360:1.05);
  \draw (O) ++(230:1.25) arc (230:360:1.25);
  \node at (115:1.6) {$130^{\circ}$};
  \node at (295:1.6) {$130^{\circ}$};
```

Ada dua hal yang saya jaga di potongan kode ini. Pertama, busur ganda saya gambar pada dua jari-jari yang berbeda, $1{,}05$ cm dan $1{,}25$ cm, supaya keduanya terlihat sebagai dua garis yang sejajar, bukan satu garis yang kebetulan tebal. Kedua, label $130^{\circ}$ saya letakkan pada jarak $1{,}6$ cm — di luar busur terluar — supaya angkanya tidak terjepit di antara dua busur.

## Satu soal untuk dibawa ke kelas

Gambar ini langsung saya pakai untuk satu soal esok paginya. Dua garis berpotongan, satu sudutnya dinyatakan dalam $x$: sudut kanan atas $(2x + 10)^{\circ}$ dan sudut kiri bawah $(3x - 20)^{\circ}$. Karena keduanya bertolak belakang, keduanya sama besar, sehingga $2x + 10 = 3x - 20$ dan $x = 30$. Sudutnya menjadi $2 \times 30 + 10 = 70^{\circ}$, dan dua sudut lainnya $180^{\circ} - 70^{\circ} = 110^{\circ}$. Saya sengaja memakai $x$ di soal ini, bukan angka jadi, supaya siswa tidak bisa menjawab hanya dengan membaca gambar — mereka harus memakai sifat bertolak belakang itu sebagai persamaan.

Kesalahan yang paling sering muncul di soal seperti ini bukan pada aljabarnya, melainkan pada pasangannya: siswa menyamakan $(2x + 10)^{\circ}$ dengan sudut yang berdampingan, lalu menulis $2x + 10 + 3x - 20 = 180$. Jawabannya memang keluar, tetapi sudutnya salah — dan gambar dengan busur tunggal dan ganda itulah yang menolong: sebelum menulis persamaan, saya minta siswa menunjuk dulu pasangan busur yang sama di gambar. Kalau busurnya sama, persamaannya sama dengan; kalau busurnya berbeda, persamaannya berjumlah $180^{\circ}$. Satu gambar yang benar menghemat sepuluh menit penjelasan.

Besok, kalau Anda menggambar dua garis berpotongan di papan tulis, coba gambar ulang dengan TikZ malam ini. Pilih satu sudut yang Anda suka, beri tanda busur pada pasangannya, dan biarkan gambar itu yang menjelaskan — bahwa di sekeliling satu titik potong, yang berhadapan tidak pernah berbeda.

> 📎 **Berkas TikZ lengkap:** [sudut-bertolak-belakang.tex](tex/sudut-bertolak-belakang.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
