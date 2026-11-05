---
title: "Pergeseran yang Punya Alamat: Menggambar Vektor pada Bidang Koordinat dengan TikZ"
date: 2026-11-03T18:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Memperkenalkan vektor lewat pergeseran yang sudah biasa siswa alami di kelas, lalu menggambarnya dengan TikZ agar komponen-komponennya terlihat jujur di layar."
featuredImage: "featured-image.png"
tags: ["TikZ", "vektor", "koordinat", "media pembelajaran"]
categories: ["Matematika"]
math:
  enable: true
---

Kemarin sore, sebelum bel pulau terakhir berbunyi, seorang siswa di kelas VIII bertanya sambil menunjuk bukunya, "Pak, ini kan cuma pindah tempat. Kenapa harus ditulis pakai kurung seperti itu?" Ia sedang menatap penulisan $\begin{pmatrix}3\\2\end{pmatrix}$ di contoh soal pergeseran titik. Pertanyaan itu membuat saya berhenti sejenak. Karena memang benar — bagi siswa, pergeseran adalah gerakan, bukan pasangan angka. Dan justru di sinilah vektor sebenarnya lahir: sebagai cara memberi alamat pada sebuah pergeseran.

<!--more-->

## Dari gerakan ke pasangan angka

Saya biasa memulainya dari badan. "Semuanya, berdiri. Geser tiga langkah ke kanan, dua langkah ke depan." Mereka bergerak, ada yang terbalik urutannya, ada yang salah arah, dan tawa pun muncul. Setelah semuanya berdiri di posisi yang sama, saya bertanya, "Kalau teman kalian tadi tidak melihat gerakan itu, bagaimana cara kalian menyuruhnya supaya hasilnya persis sama?"

Jawaban yang muncul biasanya bertahap. Pertama, "tiga langkah kanan, dua depan." Lalu saya tantang: kalau menghadapnya berbeda, "kanan" jadi rancu. Akhirnya muncul kesepakatan yang lebih jujur: kita butuh acuan arah yang tetap. Di kelas, acuannya dinding dan papan tulis. Di bidang koordinat, acuannya sumbu-$x$ dan sumbu-$y$. Dan begitu ada acuan, pergeseran itu bisa ditulis sebagai pasangan angka: tiga ke arah positif sumbu-$x$, dua ke arah positif sumbu-$y$ — $\begin{pmatrix}3\\2\end{pmatrix}$.

Pasangan angka itulah vektor. Ia bukan titik. Titik $(3,2)$ adalah alamat sebuah tempat; vektor $\begin{pmatrix}3\\2\end{pmatrix}$ adalah petunjuk arah dan jarak untuk bergerak. Perbedaan ini yang sering lolos dari siswa, karena keduanya memang ditulis dengan dua angka yang mirip. Di kelas saya, miskonsepsi "vektor sama dengan titik" hampir selalu muncul di jam pertama, dan saya sudah berhenti kaget.

## Menggambar yang jujur dengan TikZ

Masalahnya, gambar pergeseran di papan tulis jarang membantu. Saya menggambar panah dari titik asal ke tujuan, lalu menggambar garis putus-putus komponennya — dan karena tangan saya tidak presisi, panahnya kadang miring, panjang komponennya tidak sesuai angka yang saya tulis, dan siswa yang jeli akan protes. Di titik itu gambar berhenti menjadi alat bantu dan mulai menjadi sumber kebingungan baru.

Solusi yang saya pakai sekarang: gambar seperti itu saya buat dengan TikZ, supaya setiap panjang di gambar benar-benar setia pada angkanya. Ini bagian inti dari gambar yang saya pakai:

```latex
\draw[very thick, ->] (0,0) -- (3,2)
    node[midway, below] {$\vec{u}=(3,2)$};
\draw[dashed] (3,0) -- (3,2);   % komponen y
\draw[dashed] (0,2) -- (3,2);   % komponen x
\draw[very thick, ->] (0,0) -- (-1,4)
    node[midway, left] {$\vec{v}=(-1,4)$};
```

Hasilnya seperti di bawah ini. Perhatikan dua panah itu. Keduanya mulai dari titik asal yang sama, tapi mewakili dua pergeseran yang berbeda: $\vec{u}$ tiga satuan ke kanan dan dua ke atas, $\vec{v}$ satu satuan ke kiri dan empat ke atas.

![Dua vektor dari titik asal, dengan komponen-komponennya digambar putus-putus](gambar-vektor-koordinat.png)

Yang saya suka dari versi TikZ ini: garis putus-putusnya tidak mengelabui. Siswa bisa menghitung sendiri kotak-kotak pada grid dan memastikan bahwa panah $\vec{u}$ memang naik dua kotak setelah melangkah tiga kotak ke kanan. Kalau saya menggambar manual, mereka hanya bisa percaya pada tangan saya. Dengan gambar yang presisi, mereka bisa memverifikasi sendiri — dan kebiasaan memverifikasi gambar itu sendiri adalah bekal berharga, bukan cuma untuk vektor.

## Komponen: memecah pergeseran jadi dua langkah

Di kelas, saya menyebut garis putus-putus itu sebagai "jalur tangga". Dari titik asal, untuk mengikuti $\vec{u}$, kita bisa jalan tiga satuan dulu sepanjang sumbu-$x$, lalu berbelok naik dua satuan sejajar sumbu-$y$, lalu sampai di $U(3,2)$. Jalurnya berbentuk tangga, tapi hasil akhirnya sama persis dengan terbang lurus mengikuti panah.

Di sinilah pemahaman tentang komponen tumbuh dengan sendirinya: vektor itu tidak peduli jalurnya, ia hanya peduli pada perubahan totalnya. Tiga ke kanan lalu dua ke atas, atau dua ke atas lalu tiga ke kanan — sama saja. Ini juga landasan yang nanti, di jenjang lebih tinggi, mereka akan kenal sebagai penjumlahan vektor. Saya tidak menyebut istilahnya sekarang, tapi bibitnya sudah ditanam: pergeseran bisa digabung, dan penggabungannya bisa dihitung dari komponennya.

Untuk $\vec{v}$, komponen $-1$ memberi kesempatan menegaskan sesuatu yang lebih tua dari vektor sendiri: tanda negatif pada komponen bukan tanda "ada yang kurang", melainkan arah. Satu satuan ke kiri berarti $-1$ pada sumbu-$x$. Siswa yang sudah lelah dengan garis bilangan biasanya melihat negatif kembali sebagai arah — dan ini selalu terasa seperti reuni dua konsep yang selama ini tinggal di kamar berbeda.

## Titik, vektor, dan bidang yang sama

Setelah gambar dibahas, saya kembali ke pertanyaan siswa di pembuka. Titik $U(3,2)$ dan vektor $\begin{pmatrix}3\\2\end{pmatrix}$ memang kelihatan kembar, dan pada gambar mereka memang berhampiran. Tapi kalau kita geser titik asal — atau mulai dari titik lain, misalnya $A(1,1)$ lalu digeser oleh $\vec{u}$ — kita tiba di $B(4,3)$, bukan di $U$. Pergeserannya tetap sama; titik tujuannya berubah. Vektor adalah perpindahannya, bukan tempat berhentinya.

Pertanyaan penutup yang biasa saya berikan: "Buat satu pergeseran yang membawa kalian dari kursi kalian ke depan kelas, tulis dalam bentuk pasangan angka, lalu tukar dengan teman sebangku. Kalau dia sampai di tempat yang benar hanya dengan membaca angka kalian, pergeseran kalian sudah punya alamat yang baik." Ada yang menulis dengan lelucon, ada yang terlalu detail, ada yang kekurangan satu angka — dan justru dari pertukaran itu mereka merasakan sendiri syarat sebuah deskripsi yang cukup: arah dan jarak, keduanya, dalam dua angka.

Setahun lalu saya masih menggambar semua ini manual dan selalu ada satu-dua gambar yang menipu. Sekarang gambarnya bisa dipertanggungjawabkan, dan waktu yang dulu habis untuk membenahi papan tulis, saya pakai untuk hal yang lebih penting: mendengarkan pertanyaan seperti yang ditanyakan siswa saya kemarin sore. Karena pertanyaan seperti itu bukan tanda gagal mengajar. Itu tanda mereka sedang membangun jembatan dari gerakan ke lambang — dan tugas kita hanyalah memastikan jembatan itu punya pilar di kedua sisi.

> 📎 **Berkas TikZ lengkap:** [tikz-vektor-bidang-koordinat.tex](tex/tikz-vektor-bidang-koordinat.tex) — siap kompilasi (butuh paket `tikz`, `amsmath`, dan pustaka `arrows.meta`).
