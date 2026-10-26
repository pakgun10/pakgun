---
title: "Tinggi, Berat, Bagi: Menggambar Tiga Garis Istimewa Segitiga dengan TikZ"
date: 2026-10-26T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya mengira garis tinggi, garis berat, dan garis bagi segitiga itu tiga nama untuk satu garis yang sama. Di tulisan ini saya menggambar ketiganya pada satu segitiga dengan TikZ, lengkap dengan tanda siku, tanda sama panjang, dan busur yang membedakan ketiganya."
featuredImage: "featured-image.png"

tags: ["TikZ", "Segitiga", "Garis Istimewa", "Geometri", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu, di kelas VII, saya menggambar segitiga di papan tulis, lalu menarik tiga garis dari titik-titik sudutnya ke sisi-sisi di hadapannya. "Tiga garis ini namanya apa?" tanya saya. Seorang siswa menjawab yakin, "Semuanya garis tinggi, Pak." Yang lain menimpali, "Bukan, itu garis berat." Yang ketiga berkata pelan, "Kayaknya sama semua, Pak, cuma beda nama."

Jawaban itu sebenarnya jujur. Di papan tulis saya, ketiga garis itu memang kelihatan sama: tiga ruas garis dari titik sudut menuju sisi di hadapannya, tanpa tanda apa pun yang membedakan mana yang tegak lurus, mana yang berhenti tepat di tengah sisi, dan mana yang membagi sudut menjadi dua sama besar. Siswa tidak salah melihat; gambar sayalah yang tidak memberi petunjuk. Maka malam harinya saya menggambar ulang satu segitiga dengan TikZ, dengan aturan yang saya pegang sendiri: setiap garis harus membawa penandanya sendiri. Tulisan ini adalah catatan cara membuatnya.

<!--more-->

## Kenapa tiga garis ini mudah tertukar

Ketiga garis itu berangkat dari tempat yang sama dan berhenti di tempat yang sama: dari sebuah titik sudut ke sisi di hadapannya. Yang membedakan hanyalah syarat berhentinya. Garis tinggi berhenti saat ia tegak lurus terhadap sisi di hadapannya. Garis berat berhenti saat ia tepat membagi sisi itu menjadi dua sama panjang. Garis bagi tidak peduli di mana ia berhenti di sisi; ia peduli pada sudut tempatnya berangkat, yang harus terbagi menjadi dua sama besar.

Kalau ketiga syarat itu tidak digambar, siswa hanya melihat tiga garis yang mirip, dan menghafal namanya menjadi pekerjaan sia-sia. Karena itu, sebelum menyebut nama, saya mengajak siswa membaca penandanya: tanda siku, tanda sama panjang, atau busur yang terbagi dua. Tiga penanda itu saja sudah cukup untuk memilah ketiganya.

## Garis tinggi: yang berhenti tegak lurus

Ambil segitiga $ABC$ dengan alas $AB = 6$ cm dan titik $C$ berada $4$ cm di atas alas. Garis tinggi dari $C$ adalah ruas garis dari $C$ yang tegak lurus terhadap alas, dan kaki tingginya, sebut saja $D$, adalah titik di mana garis itu menyentuh alas. Dari sini luasnya langsung bisa dihitung: $L = \frac{1}{2} \times AB \times CD = \frac{1}{2} \times 6 \times 4 = 12$ cm$^2$.

Kunci menggambarnya dengan TikZ adalah koordinat yang membuat kaki tinggi mudah ditemukan. Saya meletakkan $A = (0, 0)$, $B = (6, 0)$, dan $C = (2, 4)$, sehingga alasnya mendatar dan kaki tinggi dari $C$ tinggal dijatuhkan lurus ke bawah: $D = (2, 0)$. Garis tingginya saya gambar putus-putus merah, lengkap dengan tanda siku kecil di $D$:

```latex
\coordinate (A) at (0,0);
\coordinate (B) at (6,0);
\coordinate (C) at (2,4);
\coordinate (D) at (2,0); % kaki tinggi dari C
\draw[thick] (A) -- (B) -- (C) -- cycle;
\draw[dashed, red, thick] (C) -- (D);
% tanda siku di D
\draw[red, thick] (D) ++(0.35,0) -- ++(0,0.35) -- ++(-0.35,0);
```

Catatan: pada segitiga tumpul, garis tinggi dari titik sudut lancip jatuh di luar segitiga. Itu sifatnya, bukan kesalahan gambar.

## Garis berat: yang berhenti tepat di tengah

Garis berat dari $A$ adalah ruas garis dari $A$ ke titik tengah sisi $BC$. Pada segitiga yang sama, titik tengah $BC$ adalah $\left(\frac{6+2}{2}, \frac{0+4}{2}\right) = (4, 2)$. Saya menggambarnya berwarna biru, dan pada sisi $BC$ saya bubuhkan dua tanda strip kecil yang sama pada kedua potongannya, supaya terbaca bahwa sisi itu terbagi dua sama panjang.

Di TikZ, titik tengah tidak perlu dihitung dengan tangan; pustaka `calc` menyediakan sintaks `($(B)!0.5!(C)$)`, titik di tengah-tengah ruas $BC$:

```latex
\usetikzlibrary{calc}
\coordinate (M) at ($(B)!0.5!(C)$); % titik tengah BC
\draw[blue, thick] (A) -- (M);
```

Pesan saya di kelas: titik tengah harus dihitung, bukan dikira-kira. Siswa yang menaruh titik tengah dengan perkiraan mata akan menggambar garis berat yang meleset. Padahal sifatnya sangat teratur: ketiga garis berat bertemu di satu titik, yaitu titik berat, yang membagi setiap garis berat dengan perbandingan $2 : 1$ — bagian dekat titik sudut dua kali bagian dekat sisi. Sifat itu hanya terlihat kalau titik tengahnya tepat.

## Garis bagi: yang membagi sudut sama besar

Garis bagi dari $A$ adalah ruas garis dari $A$ yang membagi sudut $A$ menjadi dua sama besar. Pada segitiga ini, sudut $A$ terbentuk antara sisi $AB$ yang mendatar dan sisi $AC$ yang miring. Besar sudutnya adalah $\arctan\frac{4}{2} \approx 63{,}4^\circ$, sehingga garis baginya membaginya menjadi dua sudut yang masing-masing $\approx 31{,}7^\circ$. Busur di sudut $A$ yang terbagi dua oleh garis bagi adalah penanda yang wajib ada; tanpanya, garis bagi sulit dibedakan dari garis berat.

Untuk menggambarnya, saya memakai cara praktis yang bisa diceritakan ke siswa: garis bagi membagi sisi di hadapannya dengan perbandingan yang sama dengan sisi-sisi pengapit sudutnya. Karena $AB = 6$ dan $AC = \sqrt{2^2 + 4^2} \approx 4{,}47$, titik bagi pada $BC$ membagi $BC$ dengan perbandingan $6 : 4{,}47$ dan jatuh di kira-kira $(3{,}71; 2{,}29)$. Di TikZ saya cukup menggambar ruas dari $A$ ke titik itu dengan warna hijau, lalu busur sudut $A$ yang dibelah garis bagi menjadi dua sama besar:

```latex
\coordinate (N) at (3.71,2.29); % titik bagi pada BC
\draw[green!60!black, thick] (A) -- (N);
% busur sudut A, dibelah garis bagi menjadi dua sama besar
\draw[green!60!black, thick] (A) ++(0.9,0) arc (0:63.4:0.9);
```

Seperti garis berat, ketiga garis bagi segitiga juga bertemu di satu titik: pusat lingkaran dalam segitiga, lingkaran yang menyinggung ketiga sisi dari dalam. Tiga garis dari tiga sudut berbeda ternyata sepakat bertemu di satu titik yang sama.

## Satu segitiga, tiga warna, tiga penanda

Di kelas, saya kini memproyeksikan satu segitiga dengan tiga garis berwarna berbeda: merah putus-putus untuk tinggi dengan tanda sikunya, biru untuk berat dengan tanda sama panjangnya, hijau untuk bagi dengan busurnya yang terbagi dua. Saya meminta siswa menunjuk dulu, baru menyebut nama: mana yang tegak lurus, mana yang membagi sisi sama panjang, mana yang membagi sudut sama besar. Begitu penandanya terbaca, namanya mengikuti dengan sendirinya.

Berkas TikZ lengkap ketiga gambar di atas bisa diunduh di bawah ini. Silakan ubah koordinat titik-titik sudutnya dan lihat bagaimana ketiga garis itu ikut berubah, sementara penandanya tetap membedakan mereka.

> 📎 **Berkas TikZ lengkap:** [garis-istimewa-segitiga.tex](tex/garis-istimewa-segitiga.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
