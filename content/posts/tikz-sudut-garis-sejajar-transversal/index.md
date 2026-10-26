---
title: "Sehadap, Berseberangan, Sepihak: Menggambar Sudut pada Garis Sejajar dengan TikZ"
date: 2026-10-26T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya hafal nama pasangan sudut pada garis sejajar, tapi salah menunjuk pasangannya di gambar. Di tulisan ini saya menggambar satu transversal memotong dua garis sejajar dengan TikZ, lengkap dengan busur dan warna yang membedakan sehadap, berseberangan, dan sepihak."
featuredImage: "featured-image.png"

tags: ["TikZ", "Garis Sejajar", "Sudut", "Geometri", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu, di kelas VII, saya menuliskan tiga istilah di papan tulis: sehadap, berseberangan, dan sepihak. Siswa menyalinnya dengan rapi. Lalu saya menggambar dua garis sejajar yang dipotong satu garis miring dan bertanya, "Sudut yang sehadap dengan sudut ini yang mana?" Lebih dari separuh kelas menunjuk sudut yang salah. Bukan karena mereka tidak hafal definisinya, melainkan karena di gambar papan tulis saya semua sudut kelihatan sama: delapan sudut, delapan busur kecil yang identik, tanpa warna, tanpa penanda mana yang berpasangan.

Saat itulah saya sadar, masalahnya bukan pada hafalan siswa, melainkan pada gambar saya. Pasangan sudut adalah soal posisi, dan posisi hanya bisa dibaca kalau gambarnya memberi petunjuk posisi itu. Maka malam harinya saya menggambar ulang gambar yang sama dengan TikZ, kali ini dengan aturan yang saya pegang sendiri: sudut yang berpasangan harus memakai warna yang sama, dan setiap busur harus diberi label angka. Hasilnya jauh lebih mudah dibaca, dan tulisan ini adalah catatan cara membuatnya.

<!--more-->

## Kenapa gambar sudut sejajar sering menipu

Gambar garis sejajar yang dipotong transversal menghasilkan delapan sudut, dan mata kita mudah tertipu olehnya. Dua sudut yang berhadapan secara vertikal memang sama besar, tetapi itu bukan pasangan yang sedang kita cari. Siswa yang menunjuk sembarang sudut yang "kelihatannya sama besar" sebenarnya sedang memakai cara yang benar secara intuisi, tetapi salah secara posisi: mereka belum membedakan apakah sudut itu berada di sisi transversal yang sama atau berlawanan, dan apakah ia berada di daerah antara dua garis sejajar atau di luarnya.

Karena itu, sebelum menghafal nama, saya selalu mengajak siswa membaca gambar dengan tiga pertanyaan: sudutnya di atas atau di bawah garis sejajar yang mana, di kiri atau di kanan transversal, dan di dalam daerah antara dua garis atau di luarnya. Tiga pertanyaan itu saja sudah cukup untuk memilah delapan sudut menjadi pasangan-pasangan yang bermakna. Dan ketiganya jauh lebih mudah dijawab kalau gambarnya memakai warna.

## Tiga pasang sudut yang wajib dibedakan

Ambil dua garis sejajar, sebut saja garis $k$ dan garis $l$, lalu satu garis transversal $t$ yang memotong keduanya. Misalkan salah satu sudut yang terbentuk besarnya $70^\circ$. Dari satu sudut ini saja, ketujuh sudut lainnya bisa ditentukan tanpa busur derajat, asalkan kita tahu pasangannya.

Pertama, sudut sehadap: sudut yang posisinya "sama" di kedua titik potong, misalnya sama-sama di kanan atas transversal. Pasangan sehadap besarnya sama, jadi pasangannya juga $70^\circ$. Kedua, sudut berseberangan dalam: sudut yang berada di dalam daerah antara dua garis sejajar, tetapi di sisi transversal yang berlawanan. Pasangan ini juga sama besar, jadi ikut $70^\circ$. Ketiga, sudut sepihak dalam: sudut yang berada di dalam daerah antara dua garis sejajar dan di sisi transversal yang sama. Pasangan ini tidak sama, melainkan saling berpelurus, sehingga besarnya $180^\circ - 70^\circ = 110^\circ$.

Di kelas, saya tidak meminta siswa menghafal tiga kalimat itu sekaligus. Saya meminta mereka menunjuk dulu: mana yang sehadap, mana yang berseberangan, mana yang sepihak. Begitu jari mereka menunjuk dengan benar, angkanya mengikuti dengan sendirinya.

## Kode TikZ-nya: satu transversal, tiga busur

Kunci menggambar gambar ini dengan TikZ adalah memilih koordinat transversal dari sudutnya, bukan dari perkiraan mata. Saya memakai garis sejajar mendatar di $y = 0$ dan $y = 2$, dan transversal yang membentuk sudut $70^\circ$ terhadap garis mendatar. Arah transversal itu adalah $(\cos 70^\circ, \sin 70^\circ)$, kira-kira $(0{,}34; 0{,}94)$. Artinya, setiap naik $2$ satuan, transversal bergeser ke kanan sejauh $2 \times \cot 70^\circ \approx 0{,}73$. Titik potong bawah saya letakkan di $(0, 0)$, sehingga titik potong atas jatuh di $(0{,}73; 2)$. Dengan cara ini, sudut $70^\circ$ di gambar benar-benar $70^\circ$, bukan sekadar mirip.

```latex
\begin{tikzpicture}[line width=1.4pt]
  % Dua garis sejajar k dan l
  \draw ( -3,0) -- (4,0) node[right] {$k$};
  \draw (-3,2) -- (4,2) node[right] {$l$};
  % Transversal t: naik 2, geser 0,73 (cot 70 derajat)
  \draw (-0.73,-2) -- (1.27,3.5) node[above] {$t$};
  % Busur emas: sehadap, 70 derajat di kedua titik potong
  \draw[gold, line width=2pt] (0.7,0) arc[start angle=0, end angle=70, radius=0.7];
  \draw[gold, line width=2pt] (1.43,2) arc[start angle=0, end angle=70, radius=0.7];
  \node[gold] at (0.82,0.57) {$70^\circ$};
  \node[gold] at (1.55,2.57) {$70^\circ$};
  % Busur hijau: berseberangan dalam, 70 derajat
  \draw[teal, line width=2pt] (0.73,2) ++(180:0.5)
    arc[start angle=180, end angle=250, radius=0.5];
  \node[teal] at (0.03,1.51) {$70^\circ$};
  % Busur merah: sepihak dalam, 110 derajat
  \draw[red!70!black, line width=2pt] (0.73,2) ++(250:0.5)
    arc[start angle=250, end angle=360, radius=0.5];
  \node[red!70!black] at (1.22,1.30) {$110^\circ$};
\end{tikzpicture}
```

Perhatikan tiga warna pada busur di atas. Emas untuk pasangan sehadap, hijau untuk berseberangan dalam, dan merah untuk sepihak dalam. Warna bukan hiasan di sini; warna adalah cara gambar itu "berbicara" tentang pasangan. Siswa yang melihat dua busur emas langsung tahu keduanya satu pasangan, tanpa harus membaca labelnya lebih dulu. Tanda sejajar pada garis $k$ dan $l$ juga saya tambahkan dengan dua goresan pendek yang sama, supaya syarat "sejajar" itu terlihat, bukan hanya diasumsikan.

## Satu soal, tiga jawaban dari satu gambar

Gambar yang sama bisa langsung dipakai menjadi soal. Misalnya: diketahui salah satu sudut pada titik potong bawah besarnya $70^\circ$, tentukan sudut sehadapnya, sudut berseberangan dalamnya, dan sudut sepihak dalamnya pada titik potong atas. Jawabannya sudah dibahas di atas: sehadap $70^\circ$, berseberangan dalam $70^\circ$, dan sepihak dalam $110^\circ$. Tetapi yang lebih penting dari jawabannya adalah cara siswa sampai ke sana: ia menunjuk dulu, baru menghitung.

Variasi soalnya mudah dibuat dari berkas yang sama. Ubah sudutnya menjadi $55^\circ$, maka sepihaknya menjadi $125^\circ$ sementara dua pasangan lainnya tetap $55^\circ$. Ubah sudutnya menjadi $90^\circ$, maka semua pasangan menjadi $90^\circ$ dan transversalnya tegak lurus kedua garis sejajar. Satu berkas TikZ, tiga soal, dan setiap soal melatih keterampilan yang sama: membaca posisi sebelum menghitung angka.

## Penutup: gambar yang membuat jari tidak ragu

Sejak memakai gambar berwarna ini, pertanyaan "yang mana, Pak?" di kelas saya jauh berkurang. Bukan karena siswa tiba-tiba lebih pintar, melainkan karena gambarnya berhenti menuntut mereka menebak-nebak. Definisi sehadap, berseberangan, dan sepihak tetap harus dihafal, tetapi hafalan itu kini menempel pada sesuatu yang bisa ditunjuk: busur emas, busur hijau, dan busur merah.

Bagi saya, itulah fungsi gambar soal yang paling dasar: membuat posisi bisa dibaca, bukan sekadar terlihat cantik. TikZ, dengan koordinat yang bisa saya hitung dan warna yang bisa saya tetapkan, memberi saya cara untuk itu.

> 📎 **Berkas TikZ lengkap:** [sudut-garis-sejajar.tex](tex/sudut-garis-sejajar.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
