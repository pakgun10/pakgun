---
title: "Ogif: Garis yang Menghubungkan Titik Tengah Kelas"
date: 2026-10-30T16:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Setelah histogram, ogif sering digambar sembarangan: garis yang melompat antar batang. Catatan kecil tentang menggambar ogif yang jujur pada interval kelasnya dengan TikZ."
featuredImage: "featured-image.png"
tags: ["TikZ", "Statistika", "Data Berkelompok"]
categories: ["Matematika"]
math:
  enable: true
---

Minggu lalu saya membagikan lembar data tinggi badan siswa kelas VIII yang sudah dikelompokkan ke dalam interval. Tugasnya klasik: buat tabel distribusi frekuensi, lalu gambar histogramnya. Sebagian besar anak selesai dengan lumayan rapi. Tapi ketika saya berkeliling, ada satu gambar yang membuat saya berhenti di sisi meja Raka. Histogramnya benar, tapi di atasnya ada garis patah-patah kuning yang menghubungkan puncak setiap batang. Saya tanya, "Ini garis apa, Rak?"

"Itu ogif, Pak. Bu catatan bilang ogif itu garis," jawabnya mantap.

Di situ saya sadar ada yang tidak beres selama ini. Bukan pada Raka — dia hanya mengulang apa yang pernah dilihatnya. Kesalahan itu milik kita para penggambar: diagram yang sering ditempel berdampingan di buku paket sampai terlihat seperti satu paket yang sama. Padahal ogif dan poligon frekuensi itu dua hal yang berbeda, dan perbedaannya bukan sekadar warna garis.

<!--more-->

## Apa Bedanya dari Poligon Frekuensi?

Dulu punya saya juga rancu. Poligon frekuensi menghubungkan puncak-puncak batang histogram, dan titik yang dihubungkan adalah titik tengah tiap kelas. Ogif — singkatan dari *ogive*, kurva pengambaran — pada hakikatnya menggambar sesuatu yang lain: frekuensi kumulatif. Setiap titik pada ogif menjawab pertanyaan "ada berapa data yang nilainya sampai batas atas kelas ini?"

Karena itu ogif selalu naik, tidak pernah turun. Menariknya, banyak gambar ogif di materi ajar yang beredar justru naik-turun seperti gunung — persis bentuk poligon frekuensi yang diberi label salah. Saya sendiri pernah membuat kesalahan itu di lembar kerja beberapa tahun lalu, dan tidak ada yang protes. Siswa menyalin. Kesalahan itu ikut terosalin turun-temurun.

Jadi kalau saya mau menggambar ogif yang jujur, ada dua syarat yang tidak bisa ditawar: datanya frekuensi kumulatif, dan titiknya diletakkan di batas atas interval — bukan di titik tengah. Kalau kelasnya $41-45$, $46-50$, dan seterusnya, maka titik ogif untuk kelas pertama diletakkan di $45$, bukan di $43$.

## Data yang Saya Pakai

Ambil contoh data nilai ulangan harian 40 siswa yang sudah dikelompokkan:

| Interval | Frekuensi | Frekuensi Kumulatif |
|----------|-----------|---------------------|
| 41–45    | 2         | 2                   |
| 46–50    | 4         | 6                   |
| 51–55    | 6         | 12                  |
| 56–60    | 5         | 17                  |
| 61–65    | 3         | 20                  |

Ada enam kelas. Titik-titik ogifnya ada di $(45,2)$, $(50,6)$, $(55,12)$, $(60,17)$, dan $(65,20)$. Perhatikan: jumlah titiknya satu lebih sedikit daripada jumlah kelas, karena ogif biasanya dimulai dari batas bawah kelas pertama dengan frekuensi kumulatif nol, yaitu titik $(40,0)$.

Begitu data kumulatifnya ini, bentuk kurvanya otomatis berbeda dari histogram. Ia hanya naik. Kalau ada yang bertanya kenapa garisnya sampai mendatar di ujung, jawabannya sederhana: tidak ada siswa baru lagi yang masuk hitungan.

## Menggambarnya dengan TikZ

Seperti biasa, saya ingin gambar soal atau bahan ajar saya yang jujur secara geometri. Ini potongan kode yang saya pakai:

```latex
\begin{tikzpicture}[x=1.6cm,y=0.8cm]
  % sumbu
  \draw[thick,->] (-0.5,0) -- (6.5,0) node[below] {Nilai};
  \draw[thick,->] (0,-0.5) -- (0,6) node[left] {Frekuensi kumulatif};
  % titik ogif di batas atas interval
  \coordinate (P0) at (0,0);
  \coordinate (P1) at (1,0.4);
  \coordinate (P2) at (2,1.2);
  \coordinate (P3) at (3,2.4);
  \coordinate (P4) at (4,3.4);
  \coordinate (P5) at (5,4);
  \draw[very thick,aksen] (P0) -- (P1) -- (P2) -- (P3) -- (P4) -- (P5);
  \foreach \i in {0,...,5}
    \fill[aksen] (P\i) circle (2.5pt);
\end{tikzpicture}
```

Ada dua keputusan kecil yang saya ambil di sini dan ingin saya garis bawahi.

Pertama, skala sumbu $y$ saya buat lebih gepeng daripada sumbu $x$ (`y=0.8cm` sementara `x=1.6cm`). Ini murni soal estetika: kalau keduanya sama, kurva ogif untuk data yang frekuensi kumulatifnya naik pelan akan terlihat terlalu curam, dan siswa bisa terkecoh menyangka datanya "meledak" di kelas tertentu. Skala yang tidak simetris ini bukan pemalsuan data — histogram juga kita gambar dengan sumbu yang proporsional — tapi ia membuat bentuk kurva tidak menipu mata.

Kedua, saya sengaja tidak menggambar histogram di belakang ogif dalam gambar yang sama. Di buku, keduanya sering ditumpuk, dan saya paham maksud edukatifnya. Tapi pengalaman saya di kelas, siswa justru bingung membedakan garis yang naik-turun (poligon frekuensi) dengan garis yang hanya naik (ogif) kalau keduanya muncul serentak dengan warna mirip. Lebih aman dua gambar terpisah, dibandingkan berdampingan dengan label yang bisa tertukar.

## Titik di Batas Atas, Bukan Titik Tengah

Ini bagian yang paling sering "ngawur" di gambar-gambar yang beredar. Karena ogif menggambar frekuensi kumulatif "sampai nilai sekian", titiknya wajib diletakkan di batas atas interval. Kalau saya taruh di titik tengah, saya sedang mengklaim bahwa siswa ke-2 dalam kelas $41-45$ memiliki nilai tepat $43$ — padahal data kita sudah dikelompokkan, nilai individualnya tidak kita ketahui.

Perhatikan juga bahwa batas atas suatu kelas dan batas bawah kelas berikutnya harus berimpit. Kelas $41-45$ dan $46-50$ punya batas yang tidak sambung ($45$ lalu $46$). Supaya ogif tidak punya lubang di $45{,}5$, saya biasanya menulis kelas dengan batas tepat: $40{,}5-45{,}5$, $45{,}5-50{,}5$, dan seterusnya. Ini terlihat sepele, tapi justru di sinilah letak "kejujuran" gambar ogif. Kalau batasnya bolong, garis kita memotong daerah yang datanya tidak jelas milik siapa.

## Kapan Ogif Berguna di Kelas?

Saya jujur: ogif bukan diagram yang akan sering dipakai siswa di kehidupan sehari-hari. Tapi justru karena itu ia punya nilai pembelajaran yang unik. Ogif memaksa siswa berpikir tentang *akumulasi* — konsep yang kelak muncul lagi di banyak tempat: total penghasilan bersaldo, total jarak tempuh perjalanan, jumlah kasus yang bertambah tiap minggu.

Di kelas, saya biasanya menutup pembahasan dengan satu pertanyaan yang menjebak: "Dari ogif ini, ada berapa siswa yang nilainya lebih dari $55$?" Anak yang paham akan membaca titik $(55,12)$, lalu mengurangkan: $20 - 12 = 8$ siswa. Anak yang belum paham biasanya mencari "batang" yang tidak ada. Pertanyaan semacam ini lebih tajam daripada sekadar meminta mereka menggambar ulang, karena ia menguji apakah garis itu benar-benar mereka baca sebagai data kumulatif, atau hanya sebagai bentuk yang enak dilihat.

Sampai sekarang, setiap kali saya menggambar ogif untuk bahan ajar, saya teringat kembali Raka dan garis kuningnya. Diagram statistika itu tidak hanya soal bentuk; ia soal janji. Histogram berjanji menunjukkan sebaran. Ogif berjanji menunjukkan akumulasi. Kalau gambar kita melanggar janjinya sendiri, kita tidak sedang menggambar matematika — kita sedang menggambar kesalahpahaman, dengan rapi.

> 📎 **Berkas TikZ lengkap:** [tikz-ogif.tex](tex/tikz-ogif.tex) — siap kompilasi (butuh paket `tikz`).
