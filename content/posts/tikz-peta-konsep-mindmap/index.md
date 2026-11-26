---
title: "Peta Konsep yang Bercabang Rapi: Menggambar Hubungan Antarmateri dengan TikZ"
date: 2026-11-21T20:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Peta konsep sering berantakan karena digambar pakai rasa. Dengan TikZ, posisi node, cabang, dan anak panah hubungan bisa diatur sejajar dan bisa dipertanggungjawabkan."
featuredImage: "featured-image.png"
tags: ["TikZ", "LaTeX", "peta konsep", "bahan ajar"]
categories: ["Matematika"]
math:
  enable: true
---

Ada satu momen yang hampir selalu terulang setiap kali saya menyiapkan bahan ajar untuk bengkel belajar. Ujung pembahasan itu selalu peta konsep. Semua materi yang sudah berjalan sepanjang kelas harus dipetakan: bilangan, aljabar, geometri, pengukuran, statistika, peluang. Awalnya peta itu memang alat belajar. Tapi lama-lama saya menyadari bahwa peta konsep itu juga alat refleksi. Kalau saya tidak sanggup menggambar hubungan antarmateri dengan jujur, artinya ada bongkahan pengalaman belajar yang belum saya pahami sendiri.

<!--more-->

## Peta Konsep yang Digambar Pakai Rasa

Tahun-tahun awal, peta konsep saya seperti itu: digambar pakai rasa. Di papan tulis atau di kertas, saya meletakkan kotak-kotak materi lalu menyambungnya dengan garis. Hasilnya, sesekali ada cabang yang tertutup kotak lain, anak panah hubungan yang miring ke arah yang tidak jelas, atau kotak yang jauh sekali padahal itu konsep bersebelahan.

Siswa biasanya tidak protes. Mereka menyalin apa adanya. Tapi di akhir kelas, ada yang bertanya, "Pak, ini kenapa Pecahan ke sana, bukan ke Bilangan Bulat?" Pertanyaan itu bagus, dan pertanyaan seperti itu hanya muncul kalau ada sesuatu yang menurut mereka kurang pas di peta. Menurut saya itu bukan kesalahan siswa. Itu tanda bahwa gambar peta belum cukup akurat untuk dijadikan acuan belajar.

Jadi masalahnya bukan pada peta konsep sebagai ide. Masalahnya pada rasa. Rasa bisa bagus di mata pembuatnya, tapi tidak bisa dijadikan standar. TikZ menawarkan cara lain: posisi ditentukan koordinat, cabang ditarik dari node ke node, hubungan digambar dengan anak panah yang eksplisit. Kalau ada yang kurang pas, yang diperbaiki bukan rasa, tapi angkanya.

## Struktur Dasar: Node dan Anak Panah

Peta konsep di TikZ pada dasarnya cuma dua komponen: node untuk kotak materi, dan `\draw[->]` untuk hubungan antarmateri. Saya cenderung mulai dari akar besar di tengah atau di atas, lalu node cabang diatur dengan koordinat yang bisa dihitung, bukan ditebak.

Potongan minimumnya kira-kira seperti ini:

```latex
\begin{tikzpicture}[
  konsep/.style={draw, rounded corners, fill=#1!20, minimum width=3cm,
                 minimum height=0.9cm, font=\small},
]
  \node[konsep=blue] (A) at (0,0) {Pecahan};
  \node[konsep=teal] (B) at (4,0) {Bilangan Desimal};
  \draw[->] (A) -- (B) node[midway, above, font=\footnotesize] {bentuk lain};
\end{tikzpicture}
```

Di sini kotak *Pecahan* dan *Bilangan Desimal* diletakkan bersebelahan dengan jarak tetap, dan hubungan "bentuk lain" dijabarkan sebagai label di atas panah. Label hubungan ini penting. Peta konsep yang baik tidak berhenti pada garis penghubung, tapi memberi kata hubungan: *adalah bagian dari*, *berubah menjadi*, *diciri utamanya*, atau *berbeda pada*. Tanpa kata hubungan, anak panah hanya dinding tanpa pintu.

## Aturan Jarak yang Bisa Saya Pertahankan

Yang membuat peta konsep di TikZ lebih bisa dipertanggungjawabkan daripada yang digambar tangan adalah aturan jaraknya. Saya memegang beberapa aturan sederhana:

- Node dalam satu tingkat pakai spasi vertikal yang sama. Kalau di tingkat kelas VII ada dua node, di tingkat kelas VIII juga dua node, jarak antar barisnya sama.
- Node sekelompok materi (misalnya *Bilangan*, *Pecahan*, *Bilangan Bulat*) dicangkup dalam kelompok dengan jarak horizontal yang konsisten.
- Anak panah hubungan tidak ditarik sewenang-wenang. Kalau hubungan bersifat *berasal dari*, arah anak panahnya konsisten dari node awal ke node akhir, bukan dua kali bolak-balik.
- Label hubungan selalu di tengah panah, pakai `node[midway, ...]`. Label di sekitar ujung panah mudah bertabrakan dengan node lain.

Aturan-aturan ini terasa berlebihan kalau cuma satu-dua node. Tapi ketika peta konsep sudah memuat belasan kotak materi, aturan jarak adalah yang menjaga gambar tetap bisa dibaca. Tanpa aturan, yang terjadi biasanya dua node terlalu dekat dan anak panahnya saling menyilang.

## Satu Contoh yang Saya Pakai di Kelas

Untuk materi pecahan, peta konsep yang saya pakai kira-kira seperti ini: *Pecahan* di tengah, bercabang ke *Pecahan Senilai*, *Pecahan Desimal*, dan *Operasi Pecahan*, dengan hubungan antarmateri dijabarkan lewat anak panah berlabel.

{{< figure src="peta-konsep-pecahan.png" title="Peta konsep materi pecahan dengan node dan anak panah berlabel" >}}

Kalau dihitung ulang dengan matematika yang benar, gambar ini tidak cuma bergaya, tapi juga bisa dipertanggungjawabkan: posisi kotak, arah panah, dan label hubungan konsisten dengan aturan jarak di atas. Kalau ada satu node yang harus digeser, yang diganti cuma koordinatnya — tidak perlu menggeser semuanya.

Saya cenderung menaruh label hubungan di atas anak panah, bukan di tengah kotak. Dengan begitu, kalau jumlah node bertambah dan peta harus diubah, label tidak ikut bertabrakan.

## Beda Peta Konsep dengan Skema Ringkasan Biasa

Ada satu kebiasaan lama yang saya tinggalkan setelah pakai TikZ. Saya dulu sering menyebut semua gambar kotak-kotak bercabang itu peta konsep, padahal sebenarnya skema ringkasan. Beda di satu hal: skema ringkasan mengelompokkan, peta konsep menyambung. Peta konsep tanpa label hubungan justru jadi skema ringkasan yang mengenakan panah.

Kalau kelas saya sedang butuh peta konsep yang benar-benar menegaskan hubungan antarmateri, saya tetap pakai TikZ. Kalau yang dibutuhkan cuma ringkasan visual dari suatu subbab, skema ringkasan biasa juga cukup. Yang penting jangan campur: peta konsep butuh panah berlabel, dan panah berlabel butuh struktur koordinat yang bisa dipegang.

## Untuk Guru yang Mau Mencoba

Kalau Bapak/Ibu baru mulai pakai TikZ untuk peta konsep, saya sarankan mulai dari peta konsep yang dipegang satu materi saja dulu. Setelah itu baru digabung. Kalau langsung mencoba menggambar semua materi dari kelas VII sampai IX dalam satu gambar, biasanya yang terjadi koordinatnya tidak teratur lagi dan gambar sulit diperbaiki.

Dua tips praktis dari pengalaman saya:

1. Pakai `tikzstyle` atau style node di awal `\begin{tikzpicture}[...]`, bukan pakai atribut di setiap node. Dengan begitu, kalau bentuk node harus diubah, cukup diubah di satu tempat.
2. Kalau peta konsep sudah lebih dari sepuluh node, pisahkan gambar dengan paket `tikzpicture` di dalam `figure` berbeda, jangan dipaksakan satu gambar. Pembaca peta konsep yang berantakan lebih sulit dijadikan bahan ajar daripada dua gambar kecil yang rapi.

Kedua tips ini sederhana, tapi konsisten menyelamatkan saya dari kebiasaan lama: menaruh semua node di satu gambar, lalu bingung sendiri mencari jarak yang pas.

## Penutup: Dari Rasa ke Standar

Dulu saya menggambar peta konsep seperti menggambar denah rumah dari ingatan. Sekarang saya menggambar peta konsep seperti menulis rumus — dengan aturan yang bisa dipegang. Perubahan ini kecil, tapi efeknya terasa: peta konsep yang dulu sering ditanya-tanya siswa, sekarang jarang dipertanyakan arahnya. Kalau ada yang bertanya, pertanyaannya biasanya bukan "kok panahnya ke sana", tapi "Pak, kenapa hubungannya begini?" — dan pertanyaan seperti itu justru yang saya harapkan muncul di kelas.

> 📎 **Berkas TikZ lengkap:** [tikz-peta-konsep.tex](tex/tikz-peta-konsep.tex) — siap kompilasi (butuh paket `tikz`).
