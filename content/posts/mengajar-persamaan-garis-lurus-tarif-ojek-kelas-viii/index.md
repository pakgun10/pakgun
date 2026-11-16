---
weight: 1
title: "Dari Tarif Ojek ke Persamaan Garis: Mengajar Persamaan Garis Lurus untuk Kelas VIII"
date: 2026-11-17T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Persamaan garis lurus saya ajarkan bukan dari rumus di papan tulis, melainkan dari tarif ojek: tarif awal ditambah tarif per kilometer, sampai murid sendiri yang menemukan bentuk y = mx + c."
featuredImage: "featured-image.png"

tags: ["Persamaan Garis Lurus", "Kelas VIII", "Ide Mengajar"]
categories: ["Matematika"]

math:
  enable: true
---

Saya membuka pelajaran hari itu dengan satu pertanyaan: "Siapa di sini yang pernah naik ojek online?" Hampir semua tangan terangkat. Lalu saya lanjutkan, "Waktu memesan, kalian pernah memperhatikan tidak, tarifnya itu dihitung bagaimana?" Seorang murid menjawab, "Ada tarif awalnya, Pak. Terus tambah per kilometer." Tepat sekali. Tanpa saya sadari, murid itu baru saja membacakan persamaan garis lurus — hanya saja ia belum tahu namanya. Hari itu saya tidak menulis $y = mx + c$ di papan tulis terlebih dahulu. Saya menulis tarif ojek.

<!--more-->

## Dari satu perjalanan ke tabel

Saya tulis di papan sebuah tarif sederhana: tarif awal Rp5.000, ditambah Rp2.000 untuk setiap kilometer. Lalu saya bertanya, "Kalau jaraknya 7 km, berapa tarifnya?" Kelas menghitung bersama: $5.000 + 2.000 \times 7 = 19.000$. Seorang murid di baris belakang nyeletuk, "Kalau 1 km, Rp7.000 ya, Pak?" Saya angguk, lalu saya ajak mereka membuat tabelnya:

| Jarak (km) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Tarif (Rp) | 5.000 | 7.000 | 9.000 | 11.000 | 13.000 | 15.000 |

Pola di tabel itu langsung terlihat: setiap jarak bertambah 1 km, tarif bertambah Rp2.000. Saya uji dengan jarak yang tidak ada di tabel: 10 km. "Rp25.000, Pak," jawab seorang murid cepat. Caranya? "$5.000$ ditambah $2.000$ kali $10$." Ia sudah memakai rumus tanpa menyadarinya. Di sinilah saya berhenti sejenak dan berkata, "Nah, cara kalian menghitung barusan — itulah yang akan kita beri nama hari ini."

## Dari tabel ke rumus

Saya beri nama: $x$ untuk jarak dalam kilometer, $y$ untuk tarif dalam rupiah. Maka tarifnya bisa ditulis $y = 2000x + 5000$. Saya tanya, "Angka $2.000$ ini apa artinya?" — "Tambahan tiap kilometer, Pak." — "Dan $5.000$?" — "Tarif awal, yang dibayar walau jaraknya nol." Dua jawaban itu saya tulis di papan dengan warna berbeda, karena keduanya adalah tokoh utama dalam persamaan garis lurus.

Angka $2.000$ adalah $m$, gradien garis itu: seberapa curam tarif naik setiap kilometer bertambah. Angka $5.000$ adalah $c$, titik potong garis dengan sumbu $y$: tarif saat $x = 0$. Saya tunjukkan pada grafiknya — garis lurus yang lewat titik $(0, 5000)$ dan $(5, 15000)$. Gradiennya bisa dihitung dari dua titik itu: $\frac{15000 - 5000}{5 - 0} = \frac{10000}{5} = 2000$. Sama persis dengan tarif per kilometer. Murid yang semester lalu belajar gradien dari anak tangga kini melihat gradien yang sama muncul sebagai tarif per kilometer. Gradien ternyata bukan cuma soal tangga — ia adalah laju perubahan, apa pun yang berubah.

## Dua ojek, satu titik temu

Supaya tidak berhenti di satu rumus, saya hadirkan ojek kedua. Ojek B tarif awalnya lebih murah, Rp3.000, tetapi per kilometernya Rp2.500. Rumusnya $y = 2500x + 3000$. "Mana yang lebih murah?" Saya biarkan kelas berdebat. Ada yang bilang B, karena tarif awalnya lebih kecil. Ada yang bilang A. Saya minta mereka menghitung untuk 2 km: A $9.000$, B $8.000$ — B menang. Untuk 10 km: A $25.000$, B $28.000$ — A menang. Jadi jawabannya tergantung jarak. "Lalu di jarak berapa keduanya sama?" tanya saya.

Kami samakan kedua rumus itu: $2000x + 5000 = 2500x + 3000$. Pindahkan suku: $5000 - 3000 = 2500x - 2000x$, sehingga $2000 = 500x$ dan $x = 4$. Di jarak 4 km, tarif keduanya sama: $2000 \times 4 + 5000 = 13.000$. Di grafik, inilah titik potong dua garis: $(4, 13000)$. Murid melihat sendiri bahwa menyelesaikan dua persamaan sekaligus — yang tahun lalu terasa seperti teka-teki — ternyata sama dengan mencari titik ketika dua ojek mengenakan tarif yang sama. Di bawah 4 km pilih B, di atas 4 km pilih A. Matematika di sini bukan cuma jawaban, melainkan keputusan.

## Tiga kesalahan yang sering muncul

Ada tiga kesalahan yang hampir selalu muncul setiap kali saya mengajar topik ini. Pertama, lupa tarif awal: murid menulis $y = 2000x$ saja. Saya tanya balik, "Kalau jaraknya nol, tarifnya nol?" Mereka tertawa — aplikasi ojek tetap menagih Rp5.000 walau kita batal di tempat. Kedua, menukar $m$ dan $c$: menulis $y = 5000x + 2000$. Saya minta mereka hitung untuk 2 km: hasilnya Rp12.000, padahal tabel kita bilang Rp9.000. Angka yang tertukar membuat tarif melesat, dan murid langsung tahu ada yang salah. Ketiga, gradien dibalik: $\frac{\Delta x}{\Delta y}$ bukannya $\frac{\Delta y}{\Delta x}$. Saya suruh mereka mengecek dengan tabel: dari 0 ke 5 km tarif naik Rp10.000, jadi $\frac{10000}{5} = 2000$ per km — kalau dibalik, hasilnya $\frac{5}{10000}$, jelas bukan tarif.

## Kegiatan: murid membuat tarif sendiri

Di lima belas menit terakhir, saya balik arah. Sekarang giliran murid yang membuat "tarif" sendiri. Ada yang membuat tarif jualan gelang: modal awal Rp8.000 untuk bahan, ditambah Rp3.000 per gelang, sehingga $y = 3000x + 8000$. Lima gelang berarti Rp23.000. Ada yang membuat tarif cuci motor: Rp10.000 ditambah Rp2.000 per liter sabun. Mereka saling menukar tabelnya, lalu menebak rumus dari tabel teman — tanpa melihat rumus aslinya. Yang ditebak benar, ia yang tersenyum paling lebar. Di akhir, saya minta mereka menulis satu kalimat: "Dalam rumus saya, $m$ artinya ... dan $c$ artinya ..." Kalimat itu saya kumpulkan. Sebagian besar menulis dengan benar, dan yang keliru saya tahu persis di mana letak salah pahamnya.

Persamaan garis lurus akhirnya bukan sekadar $y = mx + c$ yang dihafal untuk ulangan. Ia adalah cerita tentang sesuatu yang punya biaya awal dan biaya per satuan — ojek, gelang, cuci motor, apa saja. Kalau murid sudah pernah merasakan sendiri angka $m$ dan $c$ itu di kehidupan mereka, rumus itu tidak lagi terasa asing ketika bertemu lagi di bab berikutnya. Ia sudah punya alamat di kepala mereka.
