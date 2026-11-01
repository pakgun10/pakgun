---
title: "Dua Diagonal yang Berpotongan Tegak Lurus: Menggambar Belah Ketupat dan Layang-Layang dengan TikZ"
date: 2026-10-31T09:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Belah ketupat dan layang-layang sering tertukar di gambar soal. Cerita menggambar keduanya dengan TikZ, dengan diagonal yang benar-benar berpotongan tegak lurus."
featuredImage: "featured-image.png"

tags: ["TikZ", "Belah Ketupat", "Layang-Layang", "Geometri", "Bangun Datar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Minggu lalu saya memberi soal hitung luas belah ketupat. Soalnya sederhana: diagonal-diagonalnya 10 cm dan 8 cm, berapa luasnya? Di lembar itu saya sertakan gambar belah ketupat yang saya buat cepat di pengolah kata — dan di gambar itulah masalah muncul. Seorang siswa, saya sebut Nadia, datang ke meja saya sambil membawa lembar soalnya.

"Pak, ini kok kelihatannya layang-layang?" Saya menengok gambarnya. Benar pula. Belah ketupat yang saya buat itu punya sisi yang panjangnya tidak sama — dua sisi atas terlihat lebih pendek daripada dua sisi bawah. Yang saya maksud belah ketupat justru tampak seperti layang-layang. Nadia lalu menambahkan pertanyaan yang lebih menyakitkan: "Kalau bentuknya salah, diagonalnya masih lurus nggak, Pak?"

<!--more-->

## Dua Bangun yang Sering Tertukar

Belah ketupat dan layang-layang memang kerabat dekat, dan justru karena itu mudah tertukar — terutama di gambar yang dibuat asal. Sifat yang menyatukan mereka: **keduanya punya diagonal yang berpotongan tegak lurus**. Perbedaannya ada pada sisi dan diagonalnya.

Pada belah ketupat, keempat sisinya sama panjang, dan kedua diagonalnya saling membagi dua sama panjang. Pada layang-layang, ada dua pasang sisi berdekatan yang sama panjang, dan hanya **satu** diagonal yang membagi diagonal lainnya jadi dua bagian sama panjang — yaitu diagonal utamanya, diagonal yang dilalui "sumbu" layang-layang itu.

Luas keduanya dihitung dengan rumus yang sama:

$$L = \frac{d_1 \cdot d_2}{2}$$

Rumus ini punya cerita geometris yang indah: kalau diagonal-diagonal itu membagi bangun jadi empat segitiga siku-siku, luas bangunnya adalah jumlah luas keempat segitiga itu — dan hasilnya selalu setengah hasil kali diagonal. Anak-anak tidak akan melihat cerita itu kalau gambar di soalnya tidak jujur: diagonal yang tidak tegak lurus, sisi yang panjangnya tidak konsisten.

Jadi minggu ini saya menggambar ulang keduanya dengan TikZ. Koordinat yang jujur membuat sisi sama panjang dan diagonal tegak lurus bukan lagi soal keberuntungan tangan.

## Menggambar Belah Ketupat dari Diagonalnya

Cara paling aman menggambar belah ketupat adalah **mulai dari diagonalnya**, bukan dari titik-titik sudutnya. Saya letakkan titik potong diagonal di titik asal, diagonal mendatar $d_1 = 10$ satuan, diagonal tegak $d_2 = 8$ satuan. Maka empat titik sudutnya:

- $A = (5, 0)$ dan $C = (-5, 0)$ — ujung diagonal mendatar,
- $B = (0, 4)$ dan $D = (0, -4)$ — ujung diagonal tegak.

Perhatikan: jarak dari titik potong ke setiap sudut adalah setengah diagonal masing-masing. Dengan koordinat seperti ini, sisi $AB = \sqrt{5^2 + 4^2} = \sqrt{41}$, dan karena simetri, keempat sisinya otomatis sama panjang. Sifat bangunnya dijamin oleh aritmetika koordinatnya sendiri. Di TikZ:

```latex
\begin{tikzpicture}[scale=0.5]
  % titik sudut dari setengah diagonal
  \coordinate (A) at ( 5, 0);
  \coordinate (B) at ( 0, 4);
  \coordinate (C) at (-5, 0);
  \coordinate (D) at ( 0,-4);
  \coordinate (O) at ( 0, 0);

  \draw[very thick, fill=yellow!20] (A) -- (B) -- (C) -- (D) -- cycle;

  % diagonal
  \draw[dashed] (C) -- (A) node[midway, below] {$d_1 = 10$};
  \draw[dashed] (D) -- (B) node[midway, right] {$d_2 = 8$};
  \draw (O) node[below left] {$O$};

  \foreach \p/\pos in {A/right, B/above, C/left, D/below}
    \draw (\p) node[\pos] {$\p$};
\end{tikzpicture}
```

Tanda tanda (label) huruf sudut di kode itu mengikuti posisi sebenarnya di gambar — sudut kanan diberi label di kanan, sudut atas di atas. Sepintas sepele, tapi kesalahan posisi label adalah cara paling cepat membuat gambar yang benar punya cerita yang salah.

## Layang-Layang: Satu Diagonal yang Membagi

Untuk layang-layang, saya mulai juga dari diagonal. Diagonal utama (mendatar kali ini, mengikuti orientasi layang-layang yang biasa ditemukan siswa — seperti mainan yang diikat tali lalu diterbangkan) panjangnya $d_1 = 12$ satuan. Diagonal kedua panjangnya $d_2 = 8$ satuan, tapi titik potongnya **tidak di tengah** diagonal utama: misalnya di 3 satuan dari ujung kiri, sehingga membagi diagonal utama jadi bagian 3 dan 9.

Koordinatnya:

- $P = (9, 0)$ dan $R = (-3, 0)$ — ujung diagonal utama,
- $Q = (6, 4)$ dan $S = (6, -4)$ — ujung diagonal kedua.

Diagonal kedua melalui $(6, 0)$, tegak lurus terhadap diagonal utama, tetapi jelas tidak di tengah $PR$ (titik tengahnya di $(3, 0)$). Dari koordinat ini: $PQ = \sqrt{3^2 + 4^2} = 5$ dan $PS = 5$ — dua sisi berdekatan yang sama panjang. Lalu $QR = \sqrt{9^2 + 4^2} = \sqrt{97}$ dan $RS = \sqrt{97}$ — pasangan berdekatan kedua. Sifat layang-layang terbaca langsung dari angka-angkanya.

```latex
\begin{tikzpicture}[scale=0.5]
  \coordinate (P) at ( 9, 0);
  \coordinate (Q) at ( 6, 4);
  \coordinate (R) at (-3, 0);
  \coordinate (S) at ( 6,-4);
  \coordinate (T) at ( 6, 0);  % titik potong diagonal

  \draw[very thick, fill=cyan!10] (P) -- (Q) -- (R) -- (S) -- cycle;

  \draw[dashed] (R) -- (P) node[midway, above] {$d_1 = 12$};
  \draw[dashed] (S) -- (Q) node[midway, right] {$d_2 = 8$};

  % penanda bahwa T tidak di tengah PR
  \draw (R) -- (T) node[midway, below] {$9$};
  \draw (T) -- (P) node[midway, below] {$3$};
  \draw (T) node[below right] {$T$};

  \foreach \p/\pos in {P/right, Q/above, R/left, S/below}
    \draw (\p) node[\pos] {$\p$};
\end{tikzpicture}
```

Bagian favorit saya justru penanda angka 9 dan 3 itu. Kalau siswa melihat sendiri bahwa diagonal yang satu membagi diagonal lainnya tidak sama panjang, perbedaan belah ketupat dan layang-layang tidak perlu dihafal lagi — dia tinggal membedakan dua gambar yang jujur.

## Memeriksa Ulang dengan Distansi

Kebiasaan yang sekarang saya jalankan setiap menggambar bangun dengan sifat khusus: setelah selesai, saya ukur ulang gambar hasil kompilasi. Di belah ketupat, saya cek jarak keempat sisi memang sama. Di layang-layang, saya cek dua hal: pasangan sisi sama panjang, dan titik potong diagonal benar-benar tidak di tengah diagonal utamanya. Kalau salah satu gagal, berarti koordinat saya yang keliru — bukan gambar yang "kurang bagus".

Cara paling cepat, saya tempelkan penghitungan jarak di komentar kode:

```latex
% Verifikasi: PQ = sqrt(3^2+4^2) = 5, PS = 5, QR = RS = sqrt(97)
% PT:TR = 3:9 (T bukan titik tengah PR) -> benar layang-layang
```

Dua baris komentar itu terasa berlebihan, tapi ia menyelamatkan saya dari pengulangan insiden Nadia. Gambar soal adalah bagian dari soal. Kalau gambarnya berdusta tentang sifat bangunnya, siswa yang teliti akan kebingungan, dan siswa yang tidak teliti akan belajar bahwa gambar matematika boleh asal.

## Refleksi di Ujung Minggu

Yang mengganggu saya dari insiden minggu lalu bukan salahnya sendiri — semua orang pernah menggambar asal. Yang mengganggu adalah betapa lama kesalahan itu lolos: lembar soal beredar, dikerjakan, dikumpulkan, dikoreksi, dan tidak ada satu pun yang menegur bahwa gambar itu salah bentuk. Kecuali satu siswa yang berani datang ke meja saya.

Sejak itu saya menaruh dua pertanyaan kecil di jurnal mengajar saya setiap kali membuat gambar soal baru: *sifat apa yang harus terlihat di gambar ini?* dan *apakah koordinat saya menjamin sifat itu?* Belah ketupat harus terlihat belah ketupat sebelum angkanya dibaca. Layang-layang harus punya titik potong diagonal yang jelas tidak di tengah.

TikZ tidak membuat saya menjadi guru yang lebih pintar. Tapi ia membuat gambar-gambar saya berhenti berbohong — dan itu sudah cukup untuk mengubah suasana di kelas.

> 📎 **Berkas TikZ lengkap:** [tikz-belah-ketupat-layang-layang.tex](tex/tikz-belah-ketupat-layang-layang.tex) — siap kompilasi (butuh paket `tikz`).
