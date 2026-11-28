---
weight: 1
title: "Mengapa Bilangan Fibonacci Muncul di Mana-mana? Pendalaman Barisan yang Tumbuh dari Penjumlahan"
date: 2026-11-28T16:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman barisan Fibonacci untuk kelas VIII: dari soal kelinci tahun 1202, rasio yang mendekati 1,618, sampai spiraling bunga matahari dan cara menaiki tangga — semuanya lahir dari satu aturan penjumlahan yang sama."
featuredImage: "featured-image.png"

tags: ["Barisan Fibonacci", "Pendalaman", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Ada satu barisan bilangan yang murid saya temukan di tiga tempat yang tampaknya tidak berhubungan. Pertama di soal kelinci dari buku tua. Kedua di foto bunga matahari yang saya tunjukkan di proyektor. Ketiga di segitiga Pascal yang sudah mereka hafal polanya. Barisannya sama: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89$. "Pak, kok bisa sama?" tanya seorang murid. Saya dulu juga mengira itu kebetulan, atau trik buku. Ternyata bukan. Di balik barisan itu ada satu aturan yang sangat sederhana, dan aturan yang sama itulah yang bersembunyi di ketiganya. Barisan ini bernama barisan Fibonacci, dari nama Leonardo Fibonacci, matematikawan Italia yang menuliskannya pada tahun 1202.

<!--more-->

## Aturannya hanya satu: jumlahkan dua suku sebelumnya

Aturan barisan Fibonacci hanya satu kalimat: setiap suku adalah jumlah dari dua suku sebelumnya. Ditulis dengan rumus:

$$F_n = F_{n-1} + F_{n-2}$$

dengan dua suku pertama $F_1 = 1$ dan $F_2 = 1$. Dari situ semuanya mengalir sendiri: $F_3 = 1 + 1 = 2$, $F_4 = 1 + 2 = 3$, $F_5 = 2 + 3 = 5$, $F_6 = 3 + 5 = 8$, $F_7 = 5 + 8 = 13$, $F_8 = 8 + 13 = 21$, dan seterusnya. Tidak ada rumus kuadrat, tidak ada pangkat — hanya penjumlahan berulang. Justru di situlah letak keindahannya.

Di kelas, saya selalu meminta murid melanjutkan sendiri sampai suku kedua belas sebelum saya menulis jawabannya di papan. Mereka biasanya lancar sampai $34$ dan $55$, lalu mulai ragu di $89$ dan $144$. Keraguan itu bagus, karena di situlah mereka sadar bahwa barisan ini tumbuh makin cepat: selisih dua suku yang berurutan juga membesar, sebab selisih itu sendiri adalah suku sebelumnya. Barisan yang tumbuh dari penjumlahannya sendiri tidak pernah melambat.

## Soal kelinci dari tahun 1202

Fibonacci sendiri tidak menemukan barisan ini di bunga atau di langit. Ia menemukannya di soal kelinci. Soalnya begini: sepasang kelinci yang baru lahir butuh satu bulan untuk dewasa. Setelah dewasa, setiap bulan sepasang kelinci melahirkan sepasang anak. Berapa pasang kelinci pada bulan kedua belas?

Mari kita hitung bersama. Bulan pertama: $1$ pasang, masih kecil. Bulan kedua: $1$ pasang, baru dewasa. Bulan ketiga: $2$ pasang — yang lama melahirkan sepasang anak. Bulan keempat: $3$ pasang — yang dewasa melahirkan lagi, anak bulan lalu belum dewasa. Bulan kelima: $5$ pasang. Bulan keenam: $8$ pasang. Polanya terlihat: jumlah pasangan bulan ini sama dengan jumlah bulan lalu ditambah jumlah pasangan yang sudah dewasa — dan pasangan yang sudah dewasa itu persis sama banyaknya dengan jumlah pasangan dua bulan lalu. Maka jumlahnya mengikuti aturan yang sama: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144$. Pada bulan kedua belas ada $144$ pasang kelinci.

Tentu saja kelinci sungguhan tidak beranak seperti jam. Soal ini bukan soal peternakan; ini soal pola. Yang penting bukan kelincinya, melainkan gagasan bahwa pertumbuhan hari ini bergantung pada dua keadaan sebelumnya, bukan hanya satu. Setiap kali pertumbuhan mengikuti cara itu — yang baru lahir dari yang dewasa, yang dewasa lahir dari yang lebih dulu — barisan Fibonacci akan muncul.

## Rasio yang diam-diam mendekati 1,618

Ada satu hal lagi yang membuat barisan ini istimewa, dan baru terlihat bila kita membagi suku yang berurutan. Perhatikan hasilnya: $\frac{2}{1} = 2$; $\frac{3}{2} = 1,5$; $\frac{5}{3} \approx 1,667$; $\frac{8}{5} = 1,6$; $\frac{13}{8} = 1,625$; $\frac{21}{13} \approx 1,615$; $\frac{34}{21} \approx 1,619$; $\frac{55}{34} \approx 1,618$; $\frac{89}{55} \approx 1,618$. Rasio itu bergoyang naik-turun, tetapi goyangannya makin kecil dan makin dekat ke satu bilangan: kira-kira $1,618$. Bilangan itu bernama rasio emas, dan ditulis dengan huruf Yunani phi:

$$\varphi = \frac{1 + \sqrt{5}}{2} \approx 1,618$$

Mengapa rasio itu berhenti di $1,618$ dan bukan di bilangan lain? Jawabannya bisa dicari dari aturan barisannya sendiri. Andaikan rasio suku berurutan itu stabil di suatu bilangan $r$. Dari aturan $F_{n+1} = F_n + F_{n-1}$, bagilah kedua ruas dengan $F_n$: ruas kiri menjadi $r$, ruas kanan menjadi $1 + \frac{1}{r}$. Maka $r = 1 + \frac{1}{r}$, atau $r^2 = r + 1$. Persamaan kuadrat $r^2 - r - 1 = 0$ itu akarnya yang positif adalah $\frac{1 + \sqrt{5}}{2}$ — persis $1,618$. Jadi rasio emas itu bukan ditempel dari luar; ia sudah terkandung di dalam aturan penjumlahan barisan itu sendiri. Ini salah satu momen favorit saya di kelas: ketika murid melihat bahwa sebuah bilangan "indah" ternyata bisa dibuktikan dari aturan yang mereka tulis sendiri.

## Di mana barisan ini bersembunyi

Sekarang kembali ke bunga matahari. Bila kita menghitung spiral bijinya, jumlah spiral yang berputar ke kiri dan ke kanan biasanya dua bilangan Fibonacci yang berurutan: $34$ dan $55$, atau $55$ dan $89$. Pada kerucut pinus, pasangannya lebih kecil: $8$ dan $13$. Pada kelopak bunga, lili sering punya $3$ kelopak, buttercup $5$ kelopak, dan aster $13$ atau $21$ kelopak. Bukan sulap — tumbuhan yang tumbuh dengan menambahkan bagian baru di atas bagian lama secara alami menyusun spiral dalam jumlah Fibonacci, karena itulah cara biji-biji itu berdesakan paling rapat tanpa saling menutupi.

Segitiga Pascal pun menyimpannya. Bila kita menjumlahkan bilangan-bilangan pada diagonal miring segitiga Pascal — satu bilangan, lalu dua bilangan, lalu tiga bilangan, dan seterusnya — hasilnya adalah $1, 1, 2, 3, 5, 8, 13$. Barisan yang sama lagi. Bukan karena Pascal dan Fibonacci berjanji, melainkan karena keduanya dibangun dari penjumlahan yang sama: segitiga Pascal dibentuk dengan menjumlahkan dua bilangan di atasnya, dan Fibonacci dibentuk dengan menjumlahkan dua suku sebelumnya. Aturan yang sama, wujud yang berbeda.

## Kegiatan lima menit: menaiki tangga

Untuk membuat pola ini terasa di tangan, saya memakai tangga di depan kelas. Pertanyaannya: ada berapa cara menaiki tangga dengan langkah satu atau dua anak tangga sekaligus? Satu anak tangga: $1$ cara. Dua anak tangga: $2$ cara — langsung dua, atau satu-satu. Tiga anak tangga: $3$ cara. Empat anak tangga: $5$ cara. Lima anak tangga: $8$ cara. Lagi-lagi $1, 2, 3, 5, 8$.

Alasannya sama seperti kelinci: cara menaiki $n$ anak tangga adalah jumlah dari cara menaiki $n - 1$ anak tangga — bila langkah terakhir satu tangga — ditambah cara menaiki $n - 2$ anak tangga — bila langkah terakhir dua tangga. Aturan yang sama, tempat yang sama sekali berbeda. Murid saya biasanya terdiam sebentar saat menyadari ini, lalu ada yang berkata: "Jadi Fibonacci itu di mana-mana karena aturannya di mana-mana." Tepat sekali. Itulah kalimat penutup terbaik untuk barisan ini, dan bukan saya yang mengatakannya — murid saya sendiri.

Pada akhirnya, Fibonacci mengajarkan satu hal yang lebih besar daripada barisannya: pola yang tampak ajaib sering kali hanya aturan sederhana yang bekerja dengan sabar, berulang-ulang. Tugas kita sebagai guru bukan membuat murid terpesona oleh keajaibannya, melainkan menunjukkan aturan di baliknya — supaya mereka berani mencari aturan serupa di soal berikutnya, di bunga berikutnya, di tangga berikutnya.
