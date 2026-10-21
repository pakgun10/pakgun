---
weight: 1
title: "Menggambar Bidang Koordinat Kartesius dengan TikZ"
date: 2026-10-21T07:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Bidang koordinat yang presisi untuk soal dan bahan ajar, digambar dengan kode TikZ: sumbu, grid, titik, dan garis lurus — tanpa perlu tangkapan layar dari aplikasi lain."
featuredImage: "featured-image.png"

tags: ["LaTeX", "TikZ"]
categories: ["Matematika"]

math:
  enable: true
---

Guru matematika tidak bisa lepas dari gambar: bidang koordinat, titik, garis, grafik fungsi. Selama ini kita sering menggambarnya dengan tangan, atau mengambil tangkapan layar dari aplikasi lain lalu menempelkannya ke soal. Hasilnya kerap tidak presisi — titik meleset dari koordinatnya dan ukuran gambar berbeda-beda antarsoal.

Dengan **TikZ**, bidang koordinat digambar memakai kode. Koordinat yang ditulis adalah koordinat yang digambar, persis. Artikel ini adalah catatan langkah-langkah dasarnya.

<!--more-->

## Persiapan

TikZ adalah paket bawaan ekosistem LaTeX. Cukup tambahkan dua baris ini di preambel dokumen:

```latex
\usepackage{tikz}
```

Semua gambar kemudian ditulis di dalam lingkungan `tikzpicture`.

## Langkah 1 — Sumbu dan grid paling sederhana

Kita mulai dari bidang koordinat $-5$ sampai $5$ pada kedua sumbu:

```latex
\begin{tikzpicture}[scale=0.7]
  % grid tipis
  \draw[gray!30, step=1] (-5,-5) grid (5,5);
  % sumbu x dan y
  \draw[->, thick] (-5.5,0) -- (5.5,0) node[right] {$x$};
  \draw[->, thick] (0,-5.5) -- (0,5.5) node[above] {$y$};
  % titik asal
  \node[below left] at (0,0) {$O$};
\end{tikzpicture}
```

Tiga hal yang perlu diperhatikan:

- `scale=0.7` mengecilkan seluruh gambar tanpa mengubah koordinatnya — berguna agar gambar muat di kolom soal.
- `gray!30` artinya abu-abu 30%: cukup terlihat untuk membantu membaca titik, tidak mengganggu garis utama.
- Angka pada sumbu belum digambar. Untuk soal tingkat SMP biasanya kita tambahkan label angka di setiap titik potong grid pada sumbu.

## Langkah 2 — Menambahkan angka pada sumbu

Angka pada sumbu paling rapi dibuat dengan perulangan `\foreach`:

```latex
\foreach \x in {-5,...,5} {
  \draw (\x,0.12) -- (\x,-0.12);
  \ifnum \x=0 \else \node[below] at (\x,-0.15) {\small $\x$}; \fi
}
\foreach \y in {-5,...,5} {
  \draw (0.12,\y) -- (-0.12,\y);
  \ifnum \y=0 \else \node[left] at (-0.15,\y) {\small $\y$}; \fi
}
```

Perintah `\ifnum ... \else ... \fi` dipakai supaya angka $0$ tidak digambar dua kali di titik asal.

## Langkah 3 — Menempatkan titik dengan tepat

Inilah keunggulan TikZ: titik ditulis persis pada koordinatnya. Misalnya titik $A(3,2)$, $B(-2,4)$, dan $C(-3,-3)$:

```latex
\fill[red]   (3,2)   circle (2.5pt) node[above right] {$A(3,2)$};
\fill[blue]  (-2,4)  circle (2.5pt) node[above left]  {$B(-2,4)$};
\fill[green!60!black] (-3,-3) circle (2.5pt) node[below right] {$C(-3,-3)$};
```

`circle (2.5pt)` menggambar titiknya, sedangkan `node[...]` menuliskan labelnya pada arah yang kita pilih — tidak ada lagi label yang bertabrakan dengan titik lain karena kita yang menentukan posisinya.

## Langkah 4 — Menggambar garis melalui dua titik

Garis melalui $A(3,2)$ dan $B(-2,4)$ tinggal dihubungkan:

```latex
\draw[thick, blue] (-2,4) -- (3,2);
```

Kalau garisnya perlu diperpanjang sampai tepi bidang, gunakan `\clip` agar garis terpotong rapi mengikuti bingkai gambar:

```latex
\begin{tikzpicture}[scale=0.7]
  \clip (-5.5,-5.5) rectangle (5.5,5.5);
  % gambar bidang seperti langkah 1–3 di sini
  \draw[thick, blue] (-8,5.2) -- (8,0.4); % persamaan garisnya
\end{tikzpicture}
```

Sebagai pemeriksaan: garis melalui kedua titik itu bergradien

$$ m = \frac{2 - 4}{3 - (-2)} = \frac{-2}{5} = -\frac{2}{5} $$

dan persamaannya $y = -\dfrac{2}{5}x + \dfrac{16}{5}$. Di titik potong dengan sumbu-$y$, yaitu $(0, 3{,}2)$, garis itu bisa kita tandai khusus bila soal menanyakannya.

## Tips dari pengalaman di kelas

- **Satu templat untuk semua soal.** Simpan kode bidang koordinat kosong (langkah 1–2) sebagai templat. Untuk setiap soal, tinggal tambahkan titik dan garisnya. Hasilnya: semua gambar dalam satu perangkat soal seragam.
- **Beri warna secukupnya.** Titik dan garis yang ditanyakan beri warna berbeda dari grid, selebihnya biarkan hitam-abu agar tetap terbaca saat dicetak hitam-putih.
- **Uji cetak.** Gambar yang tampak jelas di layar belum tentu jelas di kertas fotokopi. Garis grid `gray!30` adalah batas aman dari pengalaman saya.

## Penutup

Sekali templat bidang koordinat ini jadi, menggambar soal koordinat berikutnya tinggal mengganti angka. Presisi terjaga, tampilan seragam, dan tidak ada lagi cerita titik meleset gara-gara digeser dengan tetikus. Selamat mencoba — kode di atas boleh langsung disalin dan diubah sesuai kebutuhan kelas Bapak/Ibu.
