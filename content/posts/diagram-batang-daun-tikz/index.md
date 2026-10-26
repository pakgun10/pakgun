---
title: "Batang di Kiri, Daun di Kanan: Menggambar Diagram Batang-Daun dengan TikZ"
date: 2026-10-24T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman seri statistika TikZ: diagram batang-daun menyimpan semua nilai asli di balik bentuknya yang mirip histogram, sehingga median dan sebaran data bisa dibaca tanpa kembali ke daftar nilai."
featuredImage: "featured-image.png"

tags: ["TikZ", "Statistika", "Diagram Batang-Daun", "Median", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Seri statistika kelas 8 ini sudah melewati diagram batang, histogram, poligon frekuensi, tiga garis pemusatan, dan ogive. Setiap gambar itu punya satu kekurangan yang sama: begitu datanya dikelompokkan, nilai aslinya hilang. Dari sebuah batang histogram kita tahu ada tujuh anak di interval 70–79, tetapi kita tidak tahu lagi apakah mereka mendapat 71 atau 79. Pekan ini seorang anak bertanya, "Pak, ada gambar yang bentuknya seperti histogram tapi nilainya masih kelihatan semua?" Ada. Namanya diagram batang-daun, dan ia adalah jembatan paling jujur antara daftar nilai mentah dan gambar.

Datanya saya ambil dari ulangan susulan kelas 8D: 30 nilai. Bukan data kemarin — sengaja saya pakai kelompok lain supaya anak melihat bahwa caranya sama untuk data apa pun, bukan hafalan satu tabel.

<!--more-->

## Batang itu puluhan, daun itu satuan

Aturan diagram batang-daun sederhana: pisahkan setiap nilai menjadi dua bagian. Puluhan menjadi batang, satuan menjadi daun. Nilai 74 berarti batang 7 dan daun 4. Nilai 90 berarti batang 9 dan daun 0 — daun nol tetap ditulis, karena menghilangkan nol sama saja dengan menghapus seorang anak dari data.

Langkah pertama yang selalu saya tekankan: urutkan dulu nilainya dari kecil ke besar. Menggambar batang-daun dari data yang belum urut adalah sumber kekacauan nomor satu di kelas saya. Setelah diurutkan, 30 nilai itu menjadi:

42, 47, 51, 55, 58, 60, 63, 64, 67, 69, 71, 72, 74, 75, 76, 78, 80, 81, 83, 84, 85, 87, 88, 90, 91, 93, 94, 96, 97, 99.

Lalu kelompokkan berdasarkan puluhannya:

| Batang | Daun |
|---|---|
| 4 | 2 7 |
| 5 | 1 5 8 |
| 6 | 0 3 4 7 9 |
| 7 | 1 2 4 5 6 8 |
| 8 | 0 1 3 4 5 7 8 |
| 9 | 0 1 3 4 6 7 9 |

Hitung daunnya: $2 + 3 + 5 + 6 + 7 + 7 = 30$. Cocok dengan jumlah anak. Kalau tidak cocok, pasti ada daun yang jatuh atau tertukar — dan anak-anak senang sekali menemukan kesalahan hitungnya sendiri di titik ini, sebelum gambarnya dibuat.

## Membaca median langsung dari daun

Di sinilah keunggulan diagram ini terlihat. Median 30 data terletak di antara data ke-15 dan ke-16. Hitung daun dari atas: batang 4 menyumbang 2, batang 5 menyumbang 3 (total 5), batang 6 menyumbang 5 (total 10), batang 7 menyumbang 6 (total 16). Jadi data ke-15 dan ke-16 adalah dua daun terakhir batang 7: 6 dan 8. Median $= \frac{76 + 78}{2} = 77$.

Bandingkan dengan histogram kemarin: di sana median hanya bisa ditaksir letak intervalnya. Di sini mediannya eksak, tanpa rumus tambahan, hanya dengan menghitung daun. Rata-ratanya pun bisa dicek: jumlah semua nilai $2270$, dibagi $30$, hasilnya $75{,}7$ — dekat dengan median 77, tanda sebarannya cukup simetris. Dan satu hal lagi yang tidak bisa dijawab histogram: modus. Karena tidak ada daun yang berulang pada batang yang sama dengan nilai yang sama persis — semua nilai berbeda — data ini tidak punya modus. Anak yang tadinya mengira "modus selalu ada" langsung terkoreksi oleh gambarnya sendiri.

## Menggambarnya dengan TikZ

Kunci TikZ di sini bukan kurva, melainkan perataan. Setiap baris terdiri dari tiga bagian: angka batang di kanan garis vertikal, garis pemisah, dan deretan daun dengan jarak yang sama. Saya memakai simpul-simpul pada koordinat yang sama persis untuk setiap baris, dengan daun dipisahkan $0{,}55$ cm, supaya daun pada baris yang berbeda tegak lurus satu sama lain. Garis vertikal digambar sekali, dari atas batang pertama sampai bawah batang terakhir, dan dua daun median (6 dan 8 pada batang 7) saya warnai emas supaya mata langsung berhenti di sana.

Keterangan "4 | 2 berarti 42" saya letakkan di bawah gambar, bukan di atas — pengalaman saya, keterangan kunci yang diletakkan di atas sering tidak dibaca karena anak langsung melihat gambarnya. Di bawah, ia menjadi kunci jawaban yang dibaca setelah anak mencoba membaca sendiri.

Satu jebakan kecil: daun harus selalu satu digit. Nilai 100 ke atas tidak bisa masuk skema ini tanpa kesepakatan baru — misalnya batang 10 dengan daun 0. Kalau ada anak yang nilainya 100, saya justru menjadikannya bahan diskusi: skema apa pun punya batas, dan menyadari batas itu adalah bagian dari belajar statistika, bukan kegagalannya.

## Kapan memakai yang mana

Penutup seri kecil ini saya sampaikan sebagai peta, bukan kesimpulan. Butuh gambaran cepat bentuk sebaran? Histogram. Butuh jawaban "berapa anak di bawah nilai tertentu"? Ogive. Butuh nilai asli tetap terlihat dan median bisa dibaca eksak? Diagram batang-daun. Tiga gambar, tiga pertanyaan berbeda — dan anak yang bisa memilih gambar yang tepat untuk pertanyaannya sudah belajar lebih dari sekadar menggambar.

> 📎 **Berkas TikZ lengkap:** [diagram-batang-daun.tex](tex/diagram-batang-daun.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
