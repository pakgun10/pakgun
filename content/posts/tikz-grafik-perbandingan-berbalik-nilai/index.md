---
title: "Bukan Garis Lurus Lagi: Menggambar Grafik Perbandingan Berbalik Nilai dengan TikZ"
date: 2026-11-09T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Grafik perbandingan senilai adalah garis lurus dari titik asal — tetapi grafik perbandingan berbalik nilai melengkung. Di tulisan ini saya menggambar kurva y = 240/x dengan TikZ, dari tabel pekerja dan hari sampai garis lurus yang menipu."
featuredImage: "featured-image.webp"

tags: ["TikZ", "Perbandingan Berbalik Nilai", "Grafik", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Senin lalu saya menggambar grafik perbandingan senilai: titik-titik harga buku yang jatuh tepat pada satu garis lurus dari titik asal. Gambar itu menenangkan — semua titik patuh pada satu garis. Hari ini saya menggambar kebalikannya, dan gambarnya tidak lagi patuh. Dua belas pekerja menyelesaikan sebuah pekerjaan dalam 20 hari. Kalau pekerjanya ditambah, harinya berkurang; kalau dikurangi, harinya bertambah. Itulah perbandingan berbalik nilai. Saya kira grafiknya tetap garis lurus, hanya miring ke bawah. Ternyata bukan — dan justru di situlah pelajarannya.

<!--more-->

## Dari tabel ke titik: hasil kali yang tidak berubah

Sebelum menggambar, saya selalu mulai dari tabel, bukan dari rumus. Pekerjaan yang sama saya hitung untuk beberapa jumlah pekerja: enam pekerja 40 hari, delapan pekerja 30 hari, sepuluh pekerja 24 hari, dua belas pekerja 20 hari, lima belas pekerja 16 hari, dua puluh pekerja 12 hari, dan tiga puluh pekerja 8 hari. Kalikan setiap baris: $6 \times 40 = 240$, $8 \times 30 = 240$, $10 \times 24 = 240$, $12 \times 20 = 240$, $15 \times 16 = 240$, $20 \times 12 = 240$, $30 \times 8 = 240$. Semuanya 240. Itulah yang tetap: hasil kali banyak pekerja dengan waktu, 240 pekerja-hari.

Dari sinilah rumusnya muncul, bukan sebaliknya. Kalau $x$ adalah banyak pekerja dan $y$ adalah waktu dalam hari, maka $x \times y = 240$, sehingga $y = \frac{240}{x}$. Saya sengaja menuliskan rumus ini sesudah tabel, karena siswa yang sudah melihat sendiri bahwa semua hasil kalinya sama akan menerima rumus itu sebagai ringkasan, bukan hafalan. Satu pekerja saja akan butuh 240 hari; enam belas pekerja butuh 15 hari, karena $240 \div 16 = 15$.

## Menggambar kurvanya dengan TikZ

Kunci gambar ini ada pada satu perintah: `plot` dengan rumus $240$ dibagi $x$. TikZ menghitung sendiri nilai $y$ untuk setiap $x$. Sumbu mendatar sampai 32 pekerja, sumbu tegak sampai 44 hari, kisi tipis setiap 4 satuan agar titiknya mudah dilacak.

```latex
\begin{tikzpicture}[x=0.24cm, y=0.15cm, font=\small]
  % Kisi tipis setiap 4 satuan
  \draw[step=4, gray!20, very thin] (0, 0) grid (32, 44);
  % Sumbu
  \draw[->, thick] (0, 0) -- (33, 0) node[below] {Banyak pekerja};
  \draw[->, thick] (0, 0) -- (0, 46) node[left] {Waktu (hari)};
  % Kurva y = 240/x
  \draw[thick, blue] plot[domain=6:32, samples=100]
    (\x, {240/\x});
  % Titik-titik dari tabel
  \foreach \x/\y in {6/40, 8/30, 10/24, 12/20,
    15/16, 16/15, 20/12, 24/10, 30/8}
    \fill (\x, \y) circle (2.5pt);
\end{tikzpicture}
```

Ada dua hal yang saya jaga di potongan kode ini. Pertama, `domain=6:32` — kurva dimulai dari $x = 6$, bukan dari nol, karena $240 \div 0$ tidak terdefinisi dan kurva ini memang tidak pernah menyentuh sumbu tegak. Kedua, `samples=100` — dengan seratus titik hitung, lengkungnya halus; kalau sampelnya terlalu sedikit, kurvanya tampak seperti garis patah-patah. Titik-titik dari tabel saya gambar dengan `\foreach`, dan yang paling penting, titik-titik itu jatuh tepat di atas kurva, karena kurva dan titik memakai rumus yang sama.

## Garis lurus yang menipu

Gambar pertama saya untuk topik ini dulu salah, dan kesalahan itu justru menjadi bahan ajar yang paling bagus. Saya menghubungkan titik $(6, 40)$ dengan titik $(30, 8)$ memakai garis lurus, karena tangan saya terbiasa menarik garis lurus. Sekilas gambarnya masuk akal: makin banyak pekerja, makin sedikit hari. Tetapi periksa titik tengahnya: garis lurus itu pada $x = 12$ berada di $y = 32$ — kemiringannya $\frac{8 - 40}{30 - 6} = -\frac{4}{3}$, sehingga pada $x = 12$ nilainya $40 - \frac{4}{3} \times 6 = 32$. Padahal tabel berkata 12 pekerja selesai dalam 20 hari, bukan 32 hari. Selisih 12 hari itu bukan kesalahan kecil.

Gambar kedua saya menaruh garis lurus itu sebagai garis putus-putus merah di atas kurva yang benar, supaya siswa melihat sendiri di mana keduanya berpisah. Di ujung kiri dan kanan keduanya bertemu, tetapi di tengah mereka berjauhan — garis lurus menggembung ke atas, kurva melengkung ke bawah. Saya menambahkan dua label pada $x = 12$: titik di kurva bertuliskan "20 hari (benar)", titik di garis putus-putus bertuliskan "32 hari (salah)".

```latex
  % Garis lurus yang SALAH, dari (6,40) ke (30,8)
  \draw[dashed, red, thick] (6, 40) -- (30, 8);
  % Titik pada x = 12: kurva benar, garis lurus salah
  \fill[blue] (12, 20) circle (2.5pt);
  \fill[red]  (12, 32) circle (2.5pt);
  \node[below right, blue] at (12, 20) {kurva: 20 hari (benar)};
  \node[above right, red]  at (12, 32) {garis lurus: 32 hari (salah)};
```

## Tiga kesalahan yang sering saya lihat

Kesalahan pertama adalah yang baru saja saya ceritakan: menggambar garis lurus karena terbiasa dengan grafik senilai. Minggu lalu garis lurus itu benar; minggu ini salah. Saya tidak menyalahkan siswa yang melakukannya — saya hanya menanyakan, "Coba cek titik tengahnya dengan tabel. Cocok tidak?"

Kesalahan kedua adalah memaksa kurva melewati titik $(0, 0)$. Pada grafik senilai, garis memang berangkat dari titik asal: nol buku, nol rupiah. Pada grafik berbalik nilai, titik asal tidak ada artinya — nol pekerja berarti pekerjaan tidak pernah selesai, dan kurva tidak pernah menyentuh kedua sumbu. Kalau ada siswa yang menggambar kurvanya sampai menabrak sumbu, saya tanyakan apa arti titik itu: berapa pekerja, berapa hari? Pertanyaan itu biasanya cukup.

Kesalahan ketiga adalah menukar sumbu: waktu ditaruh mendatar, pekerja ditaruh tegak. Hasil kalinya tetap 240, jadi gambarnya tampak benar, tetapi membaca grafik menjadi sulit. Saya membiasakan: yang diatur (pekerja) di sumbu mendatar, yang diakibatkan (waktu) di sumbu tegak, supaya semua grafik di kelas bisa dibaca dengan cara yang sama.

## Satu soal untuk dibawa ke kelas

Gambar ini langsung saya pakai untuk satu soal esok paginya. Sebuah pekerjaan selesai dalam 16 hari oleh 15 pekerja. Berapa hari pekerjaan itu selesai bila dikerjakan 18 pekerja? Hasil kalinya tetap: $15 \times 16 = 240$ pekerja-hari, sehingga $240 \div 18 = 13\frac{1}{3}$ hari, sekitar 13 hari 8 jam. Saya minta siswa mengecek di grafik: titik $(18, 13\frac{1}{3})$ harus jatuh tepat pada kurva $y = \frac{240}{x}$, karena $18 \times 13\frac{1}{3} = 240$. Soal ini sengaja memakai angka yang tidak ada di tabel, supaya siswa tidak bisa menjawab hanya dengan menghafal barisnya.

Besok, kalau Anda menggambar grafik perbandingan, coba gambar ulang dengan TikZ malam ini. Mulai dari tabel, biarkan hasil kali yang tetap itu yang menggambar kurvanya, dan taruh satu garis lurus putus-putus di sampingnya — pengingat bahwa tidak semua hubungan yang menurun itu garis lurus.

> 📎 **Berkas TikZ lengkap:** [grafik-perbandingan-berbalik-nilai.tex](tex/grafik-perbandingan-berbalik-nilai.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
