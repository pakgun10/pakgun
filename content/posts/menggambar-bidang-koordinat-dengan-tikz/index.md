---
weight: 1
title: "Membuat Bidang Koordinat yang Presisi dengan TikZ"
date: 2026-10-21T07:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pengalaman menyusun gambar bidang koordinat untuk soal persamaan garis lurus memakai TikZ: kanvas, sumbu berangka, titik, dan garis — semua diketik sebagai kode, bukan digeser dengan tetikus."
featuredImage: "featured-image.png"

tags: ["LaTeX", "TikZ"]
categories: ["Matematika"]

math:
  enable: true
---

Bagian yang paling lama saat saya menyusun soal persamaan garis lurus biasanya bukan soalnya — melainkan gambarnya. Titik digeser sedikit meleset, garis kurang lurus, lalu gambar soal nomor satu dan nomor dua ukurannya tidak sama. Sejak memakai TikZ, pekerjaan itu berubah total: gambar tidak lagi digambar, melainkan *ditulis*.

<!--more-->

## Gagasan dasarnya: gambar adalah kode

TikZ adalah paket gambar untuk LaTeX. Kita mendeskripsikan gambar dengan perintah teks, dan komputer yang menggambarnya dengan teliti. Akibatnya sederhana dan menguntungkan guru:

- Koordinat $(4,1)$ akan selalu tepat di $(4,1)$, tidak bergeser setengah mili pun.
- Satu gambar yang sudah jadi bisa dipakai ulang untuk sepuluh soal berikutnya — cukup ganti angkanya.
- Hasil cetaknya tajam pada ukuran berapa pun, karena gambarnya vektor.

Menyiapkannya cukup satu baris di preambel dokumen:

```latex
\usepackage{tikz}
```

## Kanvas pertama: petak dan dua sumbu

Contoh di bawah memakai rentang $-6$ sampai $6$. Petak-petak tipis digambar lebih dulu, baru disusul sumbu $x$ dan sumbu $y$ yang lebih tebal:

```latex
\begin{tikzpicture}[scale=0.62]
  % petak pembantu
  \draw[gray!25] (-6,-6) grid (6,6);
  % kedua sumbu
  \draw[->, very thick] (-6.4,0) -- (6.4,0);
  \draw[->, very thick] (0,-6.4) -- (0,6.4);
  \node at (6.4,-0.45) {$x$};
  \node at (0.45,6.4) {$y$};
  \node at (-0.4,-0.45) {$0$};
\end{tikzpicture}
```

Perhatikan pilihan `scale=0.62`. Semua koordinat tetap ditulis dalam satuan matematika, sedangkan skala hanya mengatur besar gambar di kertas. Untuk naskah soal dua kolom, skala sekitar $0{,}6$ biasanya pas.

## Memberi angka pada sumbu

Mengisi angka satu per satu melelahkan, jadi serahkan pada perulangan. Perintah berikut menulis angka $-6$ sampai $6$ pada kedua sumbu sekaligus, melewatkan angka nol yang sudah ditulis sebelumnya:

```latex
\foreach \n in {-6,...,-1,1,2,...,6} {
  \node[below] at (\n,0) {\footnotesize $\n$};
  \node[left]  at (0,\n) {\footnotesize $\n$};
}
```

Tanda centang kecil pada tiap posisi bisa ditambahkan bila perlu, tetapi untuk bahan ajar SMP angka saja umumnya sudah cukup jelas dibaca siswa.

## Menaruh titik dan membaca posisinya

Misalkan soal meminta siswa membaca koordinat titik $P$ dan $Q$, dengan $P(4,1)$ dan $Q(-2,5)$. Kodenya benar-benar hanya menuliskan kedua pasangan bilangan itu:

```latex
\fill[red!70!black] (4,1) circle (3pt);
\node[below right] at (4,1) {$P(4,1)$};
\fill[blue!70!black] (-2,5) circle (3pt);
\node[above left] at (-2,5) {$Q(-2,5)$};
```

Urutan pengerjaan soal pun berubah menjadi lebih jujur: saya menentukan dulu titiknya di kunci jawaban, lalu kode menggambar persis titik yang sama di lembar soal. Tidak ada lagi kunci yang berbeda dengan gambar.

## Menarik garis dan memeriksa gradiennya

Menghubungkan $P$ dan $Q$ cukup dengan satu perintah:

```latex
\draw[very thick, orange!80!black] (-2,5) -- (4,1);
```

Hasilnya bisa langsung kita periksa dengan hitungan gradien:

$$ m = \frac{1 - 5}{4 - (-2)} = \frac{-4}{6} = -\frac{2}{3} $$

Gradien negatif terlihat masuk akal di gambar: garis turun dari kiri ke kanan. Pemeriksaan silang semacam ini — antara hitungan dan gambar — jauh lebih mudah dilakukan ketika gambar lahir dari angka, bukan dari perkiraan mata. Bila garis harus tampil penuh sampai pinggir kanvas, bungkus seluruh gambar dengan `\clip` berbentuk persegi agar ujung garis terpotong rapi.

## Alternatif lain: memakai pgfplots

Ada jalan kedua yang layak dicoba, yaitu paket **pgfplots** (ditambahkan dengan `\usepackage{pgfplots}`). Berbeda dengan cara manual di atas, di sini kita tidak menggambar sumbu dan petak sendiri — cukup deklarasikan rentang dan datanya, sisanya dikerjakan paket:

```latex
\begin{tikzpicture}
  \begin{axis}[
      axis lines = middle,
      grid = both,
      xmin = -6, xmax = 6,
      ymin = -6, ymax = 6,
      xlabel = $x$, ylabel = $y$,
      width = 9cm, height = 9cm]
    \addplot[only marks, mark = *, red]
      coordinates {(4,1) (-2,5)};
    \addplot[very thick, blue]
      coordinates {(-2,5) (4,1)};
  \end{axis}
\end{tikzpicture}
```

Pendekatan deklaratif ini terasa lebih ringkas untuk grafik fungsi, misalnya saat menggambar parabola atau garis dari persamaannya langsung. Kelemahannya, kendali halus seperti letak label titik tidak sebebas cara manual. Di bahan ajar saya keduanya hidup berdampingan: pgfplots untuk grafik fungsi, TikZ manual untuk soal membaca koordinat titik.

## Contoh utuh: dari gambar menjadi soal

Supaya tidak berhenti sebagai teori, berikut alur yang biasa saya jalani saat menyiapkan satu nomor soal. Anggap kita ingin menguji apakah siswa mampu membaca koordinat, menentukan gradien, lalu menyusun persamaan garisnya.

Pertama, saya tetapkan dua titik yang perhitungannya bersih: $R(5,-1)$ dan $S(-3,3)$. Gradiennya $m = \frac{-1-3}{5-(-3)} = -\frac{1}{2}$, dan dengan mensubstitusi titik $S$ diperoleh persamaan $y = -\frac{1}{2}x + \frac{3}{2}$. Semua ini saya hitung *sebelum* menggambar apa pun — kertas coretan tetap raja untuk tahap berpikir.

Kedua, gambarnya tinggal mengikuti angka yang sudah pasti itu:

```latex
\fill[black] (5,-1) circle (3pt) node[below right] {$R$};
\fill[black] (-3,3) circle (3pt) node[above left] {$S$};
\draw[very thick] (-3,3) -- (5,-1);
```

Ketiga, barulah kalimat soalnya ditulis mengelilingi gambar: (a) tuliskan koordinat titik $R$ dan $S$, (b) hitunglah gradien garis yang melalui keduanya, (c) tentukan persamaan garis tersebut. Urutan terbalik seperti ini — jawaban dulu, gambar menyusul, pertanyaan terakhir — menghilangkan kebiasaan lama memperbaiki kunci jawaban gara-gara gambar yang terlanjur digeser. Pengalaman saya, satu nomor soal koordinat selesai dalam waktu kurang dari sepuluh menit dengan cara ini, dan gambarnya siap dipakai kembali tahun ajaran berikutnya.

## Kebiasaan yang membuat pekerjaan berikutnya ringan

Setelah beberapa kali menyusun soal, saya menyimpan satu berkas templat berisi kanvas kosong versi di atas. Tiga kebiasaan ini yang paling terasa manfaatnya:

1. **Pisahkan templat dari isi.** Kanvas, sumbu, dan angka tidak pernah berubah; yang berganti hanya titik dan garisnya.
2. **Sediakan versi hitam-putih.** Warna membantu di layar proyektor, tetapi lembar soal umumnya difotokopi — pastikan titik tetap bisa dibedakan tanpa warna, misalnya dengan bentuk penanda berbeda.
3. **Namai berkas gambar menurut soalnya.** Nama seperti `koordinat-nomor03.tex` jauh lebih mudah ditemukan semester depan daripada `gambar-baru-final2.tex`.

## Reaksi siswa saat pertama melihatnya

Ada kejadian kecil yang membuat saya mantap memakai cara ini. Suatu pagi di kelas VIII, lembar latihan dibagikan dan seorang murid mengangkat tangan hanya untuk bertanya, "Pak, gambarnya kok rapi sekali, seperti dari buku?" Selama ini mereka menerima gambar hasil gambar tangan saya di kertas buram — kadang sumbunya miring, kadang angka nolnya bertumpuk dengan angka pada sumbu tegak.

Sejak gambar dibuat dengan kode, keluhan semacam itu hilang. Murid yang duduk di bangku paling belakang pun masih bisa membaca koordinat dengan jelas, dan ketika ada yang protes karena merasa titiknya seharusnya bergeser satu petak, kami bisa memeriksa bersama-sama: yang dibaca murid itu salah, atau gambar sayalah yang keliru. Hampir selalu gambar yang menang, karena ia lahir dari angka yang sudah dipikirkan matang-matang malam sebelumnya di rumah.

## Penutup

Buat saya, keuntungan terbesar TikZ bukan gambarnya yang rapi, melainkan keyakinan bahwa gambar dan kunci jawaban tidak akan pernah bertengkar. Sekali templatnya jadi, menyusun soal koordinat berikutnya tinggal mengganti beberapa angka — dan waktu yang tadinya habis untuk menggeser-geser titik bisa dipakai memikirkan soalnya itu sendiri.

Templat dalam artikel ini sudah saya bagikan ke grup MGMP matematika kami, dan beberapa rekan mulai mencobanya untuk ulangan harian di sekolah masing-masing. Kalau Bapak/Ibu guru juga mencobanya dan menemukan cara yang lebih ringkas, saya senang sekali mendengar ceritanya — ilmu memang seharusnya berputar seperti itu, dari satu kelas ke kelas berikutnya.


---

> 📎 **Berkas TikZ lengkap:** [bidang-koordinat.tex](tex/bidang-koordinat.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
