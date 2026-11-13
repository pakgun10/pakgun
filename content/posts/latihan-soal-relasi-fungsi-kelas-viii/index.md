---
weight: 1
title: "Satu Masukan, Satu Keluaran: Latihan Soal Relasi dan Fungsi untuk Kelas VIII"
date: 2026-11-13T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Lembar latihan relasi dan fungsi untuk kelas VIII: empat soal tentang domain, kodomain, dan range, relasi faktor dari, rumus fungsi, dan tarif ojek sebagai soal cerita, dengan pembahasan langkah demi langkah, plus dua latihan mandiri beserta kuncinya."
featuredImage: "featured-image.png"

tags: ["Relasi dan Fungsi", "Kelas VIII", "Latihan Soal"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VIII saya, ada satu kalimat yang selalu saya ucapkan sebelum bab relasi dan fungsi dimulai: "Fungsi itu seperti mesin penjual otomatis." Anak memasukkan satu koin, menekan satu tombol, dan keluar satu minuman. Tidak pernah ada tombol yang sekali ditekan mengeluarkan dua minuman sekaligus. Satu masukan, satu keluaran. Itulah fungsi.

Relasi lebih longgar dari itu. Relasi hanya menghubungkan dua himpunan, tanpa aturan satu-satu. Anak yang sama bisa menyukai dua makanan, satu makanan bisa disukai lima anak — itu relasi. Tetapi begitu setiap anak dipasangkan dengan tepat satu makanan favoritnya, relasi itu menjadi fungsi. Perbedaan inilah yang paling sering membuat anak bingung: mereka mengira semua relasi adalah fungsi, atau sebaliknya, mengira fungsi harus selalu berupa rumus.

Tiga istilah yang wajib dihafal sebelum mengerjakan soal: domain adalah himpunan asal, kodomain adalah himpunan kawan, dan range adalah himpunan hasil — anggota kodomain yang benar-benar menjadi pasangan. Kodomain boleh lebih besar dari range, karena tidak semua anggota kodomain harus terpakai.

Lembar latihan di bawah ini saya susun berurutan: membaca domain, kodomain, dan range dari pasangan berurutan, menguji relasi "faktor dari", memakai rumus fungsi, dan ditutup soal cerita tarif ojek. Empat soal dengan pembahasan, lalu dua latihan mandiri.

<!--more-->

## Sedikit yang perlu diingat sebelum mengerjakan

Sebuah relasi dari himpunan $A$ ke himpunan $B$ adalah fungsi jika setiap anggota $A$ mempunyai tepat satu pasangan di $B$. Syaratnya dua: tidak boleh ada anggota $A$ yang tidak berpasangan, dan tidak boleh ada anggota $A$ yang berpasangan dua kali. Anggota $B$ boleh menerima banyak pasangan, boleh juga tidak menerima pasangan sama sekali.

$$f(x) = 2x + 3 \quad \Rightarrow \quad f(5) = 2 \times 5 + 3 = 13$$

Rumus fungsi dibaca seperti mesin: masukkan $x$, keluarkan $f(x)$. Kalau yang diketahui hasil keluarannya, kerjakan dari belakang — persamaannya dibalik, seperti pada Soal 3.

## Soal 1 — Domain, kodomain, dan range

Diketahui relasi $R$ dari $A = \{1, 2, 3, 4\}$ ke $B = \{a, b, c\}$ dengan

$$R = \{(1, a), (2, b), (3, a), (4, c)\}$$

Tentukan domain, kodomain, dan range dari $R$. Apakah $R$ merupakan fungsi?

**Pembahasan.** Domain adalah semua anggota pertama pasangan: $\{1, 2, 3, 4\}$. Kodomain adalah seluruh himpunan $B$: $\{a, b, c\}$. Range adalah anggota $B$ yang benar-benar muncul sebagai pasangan kedua: $a$, $b$, dan $c$ ketiganya muncul, jadi range-nya $\{a, b, c\}$.

$R$ adalah fungsi, karena setiap anggota $A$ muncul tepat satu kali sebagai anggota pertama. Bahwa $a$ menjadi pasangan dari $1$ sekaligus $3$ tidak menjadi masalah: yang dilarang adalah satu anggota $A$ punya dua pasangan, bukan satu anggota $B$ menerima dua pasangan.

## Soal 2 — Relasi "faktor dari"

Diketahui $A = \{2, 3, 4, 6\}$ dan $B = \{1, 2, 3, 4, 6, 12\}$. Relasi dari $A$ ke $B$ adalah "faktor dari". Tuliskan semua pasangan berurutannya, tentukan range-nya, dan periksa apakah relasi ini merupakan fungsi.

**Pembahasan.** Pasangan $(x, y)$ termasuk dalam relasi jika $x$ adalah faktor dari $y$:

- $2$ adalah faktor dari $2, 4, 6, 12$: $(2, 2), (2, 4), (2, 6), (2, 12)$.
- $3$ adalah faktor dari $3, 6, 12$: $(3, 3), (3, 6), (3, 12)$.
- $4$ adalah faktor dari $4, 12$: $(4, 4), (4, 12)$.
- $6$ adalah faktor dari $6, 12$: $(6, 6), (6, 12)$.

Range-nya adalah semua anggota kedua yang muncul: $\{2, 3, 4, 6, 12\}$.

Relasi ini **bukan** fungsi, karena $2$ mempunyai empat pasangan sekaligus. Satu tombol ditekan, empat minuman keluar — mesinnya rusak, kata saya di kelas, dan anak-anak langsung mengerti kenapa relasi ini gagal menjadi fungsi. Perhatikan juga $1$ ada di kodomain tetapi tidak ada di range: $1$ tidak pernah menjadi pasangan siapa pun, dan itu tidak apa-apa.

## Soal 3 — Memakai rumus fungsi, maju dan mundur

Diketahui fungsi $f(x) = 2x + 3$. Hitunglah $f(5)$ dan $f(-2)$, lalu tentukan nilai $a$ jika $f(a) = 11$.

**Pembahasan.** Untuk $f(5)$, ganti $x$ dengan $5$:

$$f(5) = 2 \times 5 + 3 = 10 + 3 = 13$$

Untuk $f(-2)$, hati-hati dengan tanda minusnya:

$$f(-2) = 2 \times (-2) + 3 = -4 + 3 = -1$$

Untuk mencari $a$, balikkan arahnya — yang diketahui sekarang hasil keluarannya:

$$f(a) = 11 \quad \Rightarrow \quad 2a + 3 = 11 \quad \Rightarrow \quad 2a = 8 \quad \Rightarrow \quad a = 4$$

Cek kembali: $f(4) = 2 \times 4 + 3 = 11$, cocok. Jebakan paling umum di sini adalah anak menulis $2 \times -2$ sebagai $4$ karena luput memperhatikan tanda, dan anak yang berhenti di $2a = 8$ tanpa membagi dua.

## Soal 4 — Soal cerita: tarif ojek

Tarif ojek di dekat sekolah saya adalah Rp5.000,00 untuk naik, ditambah Rp2.000,00 untuk setiap kilometer perjalanan. Jika $x$ adalah jarak dalam kilometer dan $f(x)$ adalah tarifnya dalam rupiah, tuliskan rumus fungsinya, lalu hitung tarif untuk perjalanan 8 km dan jarak perjalanan jika tarifnya Rp31.000,00.

**Pembahasan.** Rumus fungsinya:

$$f(x) = 5000 + 2000x$$

Tarif untuk 8 km:

$$f(8) = 5000 + 2000 \times 8 = 5000 + 16000 = 21000$$

Jadi tarifnya Rp21.000,00. Untuk tarif Rp31.000,00, balikkan arahnya:

$$5000 + 2000x = 31000 \quad \Rightarrow \quad 2000x = 26000 \quad \Rightarrow \quad x = 13$$

Jadi jaraknya 13 km. Soal cerita seperti ini sengaja saya pakai sebagai penutup, karena di sinilah anak melihat bahwa $f(x)$ bukan sekadar huruf — ia adalah tarif yang mereka bayar setiap hari, dan mencari $x$ dari $f(x)$ sama dengan bertanya "uang segini cukup untuk jalan sejauh apa?"

## Latihan mandiri

Kerjakan tanpa melihat kunci, lalu cocokkan jawabanmu.

1. Diketahui $g(x) = 3x - 4$. Hitunglah $g(6)$ dan tentukan nilai $x$ jika $g(x) = 8$.
2. Relasi $S = \{(1, 2), (2, 4), (3, 6), (4, 8)\}$ dari $\{1, 2, 3, 4\}$ ke $\{2, 4, 6, 8, 10\}$. Apakah $S$ merupakan fungsi? Tuliskan domain dan range-nya.

**Kunci jawaban:**

1. $g(6) = 3 \times 6 - 4 = 14$. Dari $3x - 4 = 8$ diperoleh $3x = 12$, jadi $x = 4$.
2. Ya, $S$ merupakan fungsi: setiap anggota domain muncul tepat satu kali. Domain-nya $\{1, 2, 3, 4\}$ dan range-nya $\{2, 4, 6, 8\}$.

Kalau ada yang belum cocok, periksa dulu apakah yang tertukar adalah domain dengan range, atau kodomain dengan range — tiga istilah inilah yang paling sering bertukar tempat di kepala anak. Tuliskan ketiganya setiap kali mengerjakan soal, seperti pada empat soal di atas, dan fungsi akan terasa jauh lebih jinak.
