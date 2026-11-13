---
weight: 1
title: "Mengapa (a − b)(a + b) = a² − b²? Pendalaman Selisih Dua Kuadrat"
date: 2026-11-14T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman selisih dua kuadrat untuk kelas IX: membongkar mengapa (a − b)(a + b) sama dengan a² − b² lewat perkalian, potongan persegi kertas, dan tiga jebakan yang paling sering muncul."
featuredImage: "featured-image.png"

tags: ["Selisih Dua Kuadrat", "Aljabar", "Pendalaman", "Kelas IX"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas IX minggu ini, saya menulis $(a - b)(a + b) = a^2 - b^2$ di papan tulis. Seorang murid mengangkat tangan lalu bertanya, "Pak, $b^2$-nya ke mana? Kok bisa hilang begitu saja?" Kelas tertawa kecil, tetapi pertanyaannya sungguh-sungguh. Rumus ini memang terlihat seperti sulap: dua suku masuk ke dalam kurung, satu suku hilang di ujung. Saya senang dengan pertanyaan itu, karena justru di situlah letak pemahaman yang sesungguhnya. Kalau murid hanya menghafal, mereka akan menulis rumus ini dengan benar di ulangan lalu melupakannya minggu depan. Kalau mereka tahu dari mana datangnya, rumus ini akan tinggal lebih lama.

Sabtu lalu kita membongkar $(a + b)^2$ dan menemukan suku $2ab$ yang sering terlupakan. Hari ini giliran kembarannya: selisih dua kuadrat. Bedanya, di sini yang hilang bukan satu suku yang tersembunyi, melainkan dua suku yang saling menghapus. Mari kita bongkar pelan-pelan, sampai tidak ada lagi yang terasa seperti sulap.

<!--more-->

## Kalikan dulu, baru percaya

Cara pertama membuktikan rumus ini adalah cara yang paling jujur: kalikan saja. Ambil $(a - b)(a + b)$ lalu kalikan setiap suku dengan setiap suku, seperti yang sudah kita latih di perkalian bentuk aljabar.

$$(a - b)(a + b) = a \cdot a + a \cdot b - b \cdot a - b \cdot b = a^2 + ab - ab - b^2$$

Perhatikan bagian tengahnya: $+ab$ dan $-ab$. Keduanya sama besar, berlawanan tanda, dan saling menghapus. Yang tersisa tinggal $a^2 - b^2$. Jadi jawaban atas pertanyaan murid saya tadi: yang hilang bukan $b^2$. Yang hilang adalah $ab$, dua kali, dengan tanda yang berlawanan. $b^2$ tetap ada, hanya saja tandanya minus.

Saya meminta murid mengulang perkalian itu sendiri di buku mereka, tanpa melihat papan tulis. Sebagian besar berhasil, dan mereka yang berhasil itu tersenyum karena merasa menemukan sendiri. Rumus yang tadinya terasa seperti sulap ternyata hanya perkalian biasa yang ujungnya bersih.

## Persegi yang dipotong, lalu disusun ulang

Tetapi perkalian saja belum cukup. Murid perlu melihatnya. Saya menggambar sebuah persegi besar bersisi $a$ di papan tulis. Luasnya $a^2$. Lalu di salah satu sudutnya saya menggambar persegi kecil bersisi $b$, lalu saya memotongnya keluar. Sisa potongan itu berbentuk huruf L, dan luasnya adalah $a^2 - b^2$, karena luas besar dikurangi luas kecil yang terpotong.

Sekarang bagian yang menyenangkan. Bentuk L itu saya potong lagi menjadi dua persegi panjang: satu potongan berukuran $a \times (a - b)$, satu lagi berukuran $b \times (a - b)$. Lalu kedua potongan itu saya tempelkan berdampingan, ujung bertemu ujung. Yang terjadi: terbentuklah satu persegi panjang yang utuh. Panjangnya adalah $a + b$, lebarnya adalah $a - b$. Luas persegi panjang itu adalah $(a + b)(a - b)$.

Jadi $a^2 - b^2$ dan $(a - b)(a + b)$ adalah dua cara menghitung luas yang sama. Yang satu dihitung dengan mengurangkan, yang satu dihitung dengan menyusun ulang. Tidak ada sulap di sini, hanya kertas yang dipotong dan ditempel kembali. Murid yang melihat gambar itu mengangguk, karena mata mereka sudah lebih dulu percaya sebelum tangan mereka menghitung.

## Cek dengan angka

Penjelasan yang bagus harus tahan diuji angka. Ambil $a = 5$ dan $b = 3$. Sisi kiri rumus: $a^2 - b^2 = 25 - 9 = 16$. Sisi kanan: $(5 - 3)(5 + 3) = 2 \times 8 = 16$. Cocok.

Contoh kedua, $a = 10$ dan $b = 4$. Sisi kiri: $100 - 16 = 84$. Sisi kanan: $(10 - 4)(10 + 4) = 6 \times 14 = 84$. Cocok lagi.

Lalu saya menunjukkan kegunaan rumus ini di luar soal latihan: menghitung cepat. Berapa $97 \times 103$? Tanpa rumus ini, murid menghitung bersusun. Dengan rumus ini, $97 \times 103 = (100 - 3)(100 + 3) = 100^2 - 3^2 = 10000 - 9 = 9991$. Dua langkah, selesai. Begitu juga $48 \times 52 = (50 - 2)(50 + 2) = 2500 - 4 = 2496$. Murid yang tadinya menganggap rumus ini hanya hiasan di buku mulai melihatnya sebagai jalan pintas yang sungguhan. Syaratnya satu: kedua bilangan itu harus sama jauh dari satu bilangan bulat di tengahnya.

## Tiga jebakan yang paling sering muncul

Jebakan pertama adalah menulis $a^2 + b^2$. Tanda minus tertukar menjadi plus, dan jawabannya langsung salah. Cek dengan $a = 5$ dan $b = 3$: $25 + 9 = 34$, padahal $(5 - 3)(5 + 3) = 16$. Selisihnya jauh. Begitu murid memeriksa dengan angka, kesalahan tanda ini langsung ketahuan.

Jebakan kedua adalah mengira $(a - b)^2$ sama dengan $a^2 - b^2$. Ini jebakan yang paling sering saya temui, karena keduanya memang mirip di mata. Padahal $(a - b)^2 = a^2 - 2ab + b^2$, bukan $a^2 - b^2$. Cek dengan $a = 5$ dan $b = 3$: $(5 - 3)^2 = 2^2 = 4$, sedangkan $a^2 - b^2 = 16$. Jauh sekali. Saya mengingatkan murid: kuadrat dari selisih bukan selisih dari kuadrat. Dua hal itu berbeda, dan rumusnya pun berbeda.

Jebakan ketiga adalah memaksa rumus ini pada $a^2 + b^2$. Ada murid yang menulis $a^2 + b^2 = (a + b)(a - b)$, lalu heran kenapa jawabannya tidak pernah cocok. Tentu saja tidak cocok, karena $(a + b)(a - b)$ sama dengan $a^2 - b^2$, bukan $a^2 + b^2$. Jumlah dua kuadrat tidak bisa difaktorkan dengan cara ini. Saya mengatakan kepada murid: rumus itu seperti kunci, dan kunci yang benar hanya membuka pintu yang memang pas dengannya.

## Kegiatan: gunting satu persegi kertas

Kalau ada waktu sepuluh menit di akhir pelajaran, saya menyuruh murid menggunting satu persegi kertas berukuran 10 cm kali 10 cm, lalu memotong satu sudutnya menjadi persegi kecil 3 cm kali 3 cm. Sisa potongannya berbentuk L. Lalu mereka memotong L itu menjadi dua bagian dan menyusunnya menjadi persegi panjang. Mereka mengukur dengan penggaris: panjangnya 13 cm, lebarnya 7 cm, luasnya 91 cm². Dan $100 - 9$ memang 91. Hampir selalu ada yang berseru, "Lho, Pak, kok sama?" Seruan itulah yang saya tunggu. Rumus yang ditemukan lewat tangan sendiri jauh lebih lama tinggalnya daripada rumus yang didiktekan.

Selisih dua kuadrat akhirnya bukan lagi baris yang harus dihafal sebelum ulangan. Ia adalah cerita tentang persegi yang dipotong, disusun ulang, lalu diuji dengan angka sampai cocok. Dan setiap kali murid menulis $a^2 - b^2 = (a - b)(a + b)$ setelah hari itu, saya berharap mereka ingat sejenak potongan kertas di meja mereka, bukan sekadar huruf-huruf yang harus dihafal.
