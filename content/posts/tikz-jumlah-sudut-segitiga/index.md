---
weight: 1
title: "Tiga Sudut, Satu Garis Lurus: Bukti Jumlah Sudut Segitiga dengan TikZ"
date: 2026-11-02T08:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya hafal bahwa jumlah sudut segitiga adalah 180 derajat, tetapi belum percaya sampai ia melihatnya sendiri: tiga sudut yang dipotong dari satu segitiga, dijajarkan, dan ternyata tepat membentuk satu garis lurus."
featuredImage: "featured-image.png"
tags: ["TikZ", "LaTeX", "Segitiga", "Sudut", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]
math:
  enable: true
---

Pekan lalu, di kelas VII, seorang siswa mengangkat tangan di tengah pelajaran segitiga dan bertanya dengan jujur, "Pak, kok bisa pas 180 derajat? Siapa yang mengatur supaya jumlahnya selalu segitu?" Saya tersenyum, karena pertanyaannya tepat sekali. Di buku, kalimat itu tertulis sebagai fakta: jumlah sudut dalam segitiga adalah $180^\circ$. Siswa menghafalnya, menggunakannya untuk mencari sudut yang belum diketahui, dan mendapat nilai bagus. Tetapi menghafal bukanlah percaya. Selama ia belum melihat sendiri mengapa jumlahnya selalu pas, kalimat itu hanya terasa seperti aturan yang diturunkan dari langit, bukan sesuatu yang masuk akal.

Saya tidak menjawabnya dengan dalil yang lebih panjang. Saya mengajak kelas itu menggambar satu segitiga, mengukur ketiga sudutnya, lalu memotong dan menempelkannya berjajar. Hasilnya, seperti yang akan saya tunjukkan dengan TikZ, adalah satu garis lurus — dan garis lurus besar sudutnya $180^\circ$. Bukti ini tidak memakai rumus apa pun, hanya gunting, tempelan, dan mata yang memperhatikan.

<!--more-->

## Segitiga yang sudutnya diukur dulu

Langkah pertama adalah menggambar satu segitiga yang sudutnya tidak istimewa sama sekali. Saya sengaja tidak memakai segitiga siku-siku atau segitiga sama sisi, karena siswa sering mengira aturan 180 derajat hanya berlaku untuk segitiga yang "cantik". Segitiga yang saya gambar punya tiga sudut yang berbeda-beda: $61^\circ$, $45^\circ$, dan $74^\circ$. Kalau dijumlahkan, $61 + 45 + 74 = 180$, tepat. Tetapi di titik ini, jumlah itu masih sekadar hitungan di atas kertas, belum menjadi keyakinan.

Dengan TikZ, segitiga beserta tanda sudutnya saya gambar seperti ini. Setiap sudut diberi warna berbeda: biru untuk sudut $A$, merah untuk sudut $B$, dan emas untuk sudut $C$. Pewarnaan ini bukan hiasan: warna itulah yang membuat siswa bisa mengikuti jejak setiap sudut ketika ketiganya dipindahkan ke garis lurus.

```latex
\begin{tikzpicture}
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (1.8,3.2);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above] at (C) {$C$};
  \pic[draw, fill=blue!20, angle radius=0.8cm, "$61^\circ$"]
    {angle = B--A--C};
  \pic[draw, fill=red!20, angle radius=0.8cm, "$45^\circ$"]
    {angle = C--B--A};
  \pic[draw, fill=goldenrod!30, angle radius=0.8cm, "$74^\circ$"]
    {angle = A--C--B};
\end{tikzpicture}
```

Perintah `\pic` dengan pustaka `angles` mengerjakan bagian tersulit kalau digambar manual: menggambar busur tepat di antara dua sisi yang bertemu di satu titik. Saya hanya menyebutkan tiga titiknya, misalnya `B--A--C` untuk sudut di $A$. Karena segitiganya digambar dari koordinat, besar sudut yang tertulis memang sesuai bentuknya, bukan tempelan angka.

## Memotong ketiga sudut dan menempelkannya berjajar

Inilah bagian yang membuat kelas itu diam sejenak. Bayangkan ketiga sudut segitiga tadi dipotong dengan gunting, lalu ditempelkan satu demi satu di atas satu garis lurus, tanpa celah dan tanpa tumpang tindih. Sudut biru $61^\circ$ paling kiri, sudut merah $45^\circ$ di tengah, dan sudut emas $74^\circ$ menutup barisan di kanan. Ketika potongan terakhir ditempelkan, sisi terluarnya jatuh tepat di atas garis lurus itu, tidak kurang dan tidak lebih.

Gambar kedua menunjukkan hasil tempelan itu. Tiga juring berwarna dijajarkan dari satu titik yang sama di atas garis: juring biru sampai $119^\circ$, juring merah melanjutkannya sampai $74^\circ$, dan juring emas menutupnya sampai $0^\circ$. Ketiganya bersama-sama menutupi tepat setengah lingkaran, dan setengah lingkaran adalah $180^\circ$. Tidak ada yang perlu dihafal di sini, karena mata sudah melihatnya.

```latex
\begin{tikzpicture}
  \coordinate (O) at (0,0);
  \coordinate (P180) at (-1.8,0);
  \coordinate (P119) at (-0.87,1.57);
  \coordinate (P74) at (0.50,1.73);
  \coordinate (P0) at (1.8,0);
  \draw[thick] (-2.2,0) -- (2.2,0);
  \fill[blue!30] (O) -- (P119) arc (119:180:1.8) -- cycle;
  \fill[red!30] (O) -- (P74) arc (74:119:1.8) -- cycle;
  \fill[goldenrod!40] (O) -- (P0) arc (0:74:1.8) -- cycle;
  \draw[thick] (O) -- (P180);
  \draw[thick] (O) -- (P119);
  \draw[thick] (O) -- (P74);
  \draw[thick] (O) -- (P0);
\end{tikzpicture}
```

Satu hal teknis yang patut diperhatikan pada kode juring di atas: busur setiap juring ditulis dari sudut yang lebih kecil ke sudut yang lebih besar, misalnya `arc (119:180:1.8)` untuk juring biru. TikZ menggambar busur berlawanan arah jarum jam, sehingga urutan yang terbalik akan menghasilkan juring yang memutar jauh mengitari lingkaran, bukan potongan kecil yang kita maksud. Kesalahan kecil ini hasilnya besar, dan saya sendiri pernah mengalaminya.

Di kelas, saya tidak mulai dari gambar TikZ ini. Saya mulai dari kertas: setiap kelompok menggunting segitiga dari kertas bekas, mewarnai ketiga sudutnya, lalu menempelkannya di buku. Baru setelah mereka melihat garis lurus itu terbentuk di tangan mereka sendiri, saya menampilkan gambar TikZ-nya di layar. TikZ di sini bukan pengganti pengalaman menggunting, melainkan cara mengabadikannya menjadi bahan ajar rapi yang bisa dipakai ulang tahun depan.

## Tiga kesalahan yang sering saya temui

Pertama, siswa mengukur sudut dengan busur derajat yang titik pusatnya tidak tepat di titik sudut. Hasilnya meleset beberapa derajat, jumlahnya menjadi 178 atau 183, lalu ia menyimpulkan aturannya salah. Padahal yang salah adalah pengukurannya. Sebelum membicarakan bukti apa pun, saya selalu memeriksa cara mereka meletakkan busur: titik pusat tepat di titik sudut, dan garis nol berimpit dengan salah satu sisi.

Kedua, siswa mengira aturan ini hanya berlaku untuk segitiga tertentu. "Kalau segitiganya lancip semua, Pak, apa tetap 180?" Pertanyaan seperti ini justru bagus, karena membuka jalan untuk mencoba segitiga lain: segitiga tumpul, siku-siku, atau yang sangat gepeng. Di TikZ, mencoba segitiga lain semudah mengubah satu koordinat. Setelah tiga segitiga berbeda semuanya menghasilkan garis lurus yang sama, kecurigaan itu pelan-pelan hilang.

Ketiga, siswa mencampuradukkan sudut dalam dengan sudut luar segitiga. Ketika satu sisi diperpanjang, sudut yang terbentuk di luar itu sering ikut dihitung ke dalam jumlah 180 derajat, padahal ia bukan bagian dari tiga sudut dalam. Di sinilah warna pada gambar pertama kembali membantu: hanya tiga warna itulah yang boleh dipotong dan ditempelkan.

## Penutup: dari hafalan menjadi keyakinan

Siswa yang bertanya pekan lalu itu kini tidak lagi bertanya siapa yang mengatur jumlahnya selalu pas. Ia sudah melihat sendiri jawabannya, bukan karena saya mengatakannya dengan lebih meyakinkan, melainkan karena tangannya sendiri yang memotong dan menempelkan. Itulah bedanya menghafal dan memahami: hafalan berhenti pada kalimatnya, pemahaman berhenti pada buktinya.

Kalau Bapak dan Ibu mengajar materi ini minggu depan, saran saya sederhana: beri waktu sepuluh menit untuk menggunting sebelum memberi rumus. Biarkan siswa yang menemukan garis lurusnya. Gambar TikZ di artikel ini bisa dipakai sebagai penutup pelajaran atau lembar kerja cetak. Aturan yang ditemukan sendiri selalu lebih lama tinggalnya daripada aturan yang sekadar didiktekan.

📎 **Berkas TikZ lengkap:** [jumlah-sudut-segitiga.tex](tex/jumlah-sudut-segitiga.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
