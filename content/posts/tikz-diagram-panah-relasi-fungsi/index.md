---
title: "Dua Himpunan, Satu Panah: Menggambar Diagram Panah Relasi dengan TikZ"
date: 2026-10-26T16:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya sering menggambar diagram panah relasi seperti spaghetti: panahnya bersilangan, arahnya terbalik, dan tidak jelas mana domain dan mana kodomain. Di tulisan ini saya menggambar diagram panah yang rapi dengan TikZ — dua oval, anggota yang sejajar, dan panah yang hanya berjalan satu arah."
featuredImage: "featured-image.png"

tags: ["TikZ", "Relasi", "Fungsi", "Diagram Panah", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Di kelas VIII, saat bab relasi dan fungsi, saya meminta siswa menggambar diagram panah dari sebuah relasi sederhana: empat anak dan hobi mereka. Hasilnya bermacam-macam. Ada yang menggambar panah dari kanan ke kiri, ada yang panahnya bersilangan seperti benang kusut, dan ada yang menggambar satu oval saja lalu menulis semua nama di dalamnya. Ketika saya bertanya, "Yang mana domainnya?" jawabannya ragu-ragu, karena gambarnya sendiri tidak menjawab pertanyaan itu.

Masalahnya bukan pada konsep relasinya. Siswa sudah paham bahwa Rani gemar membaca dan Sinta gemar menari. Masalahnya ada pada gambarnya: diagram panah yang buruk menyembunyikan aturan yang sebenarnya sudah mereka pahami. Maka malam harinya saya menggambar ulang diagram itu dengan TikZ, dengan tiga aturan yang saya pegang teguh: domain selalu di kiri, kodomain selalu di kanan, dan panah hanya berjalan dari kiri ke kanan. Tulisan ini adalah catatan cara membuatnya.

<!--more-->

## Kenapa diagram panah lebih sulit dari kelihatannya

Diagram panah kelihatannya sepele: dua oval dan beberapa garis berujung panah. Tetapi justru karena sepele, siswa menggambarnya tanpa rencana. Mereka menulis nama-nama dulu, baru menarik panah sesuka hati, sehingga panah yang seharusnya sejajar malah saling menyilang. Begitu panah bersilangan, membaca diagram menjadi pekerjaan menelusuri benang, bukan membaca aturan.

Kuncinya adalah menempatkan anggota kedua himpunan pada ketinggian yang sama sebelum menarik panah apa pun. Anggota yang berpasangan harus sejajar: kalau Rani di baris pertama kiri, maka "Membaca" harus di baris pertama kanan. Panah yang menghubungkan dua titik yang sejajar akan mendatar dan rapi; panah yang menghubungkan baris pertama dengan baris keempat pasti miring dan rawan bersilangan dengan panah lain. Jadi, urutan penulisan anggota di dalam oval bukanlah hiasan — ia adalah setengah dari pekerjaannya.

## Relasi pertama: dua oval dan satu aturan

Ambil relasi "gemar" antara himpunan $A = \lbrace \text{Rani, Sinta, Tono, Wati} \rbrace$ dan himpunan $B = \lbrace \text{Membaca, Menari, Melukis, Berenang} \rbrace$. Aturannya: Rani gemar membaca, Sinta gemar menari, Tono gemar melukis, dan Wati gemar berenang. Empat pasangan, empat panah, tidak ada yang bersilangan.

Saya menggambar dua elips: satu di kiri untuk $A$, satu di kanan untuk $B$. Di dalam setiap elips, anggota ditulis dengan titik di depannya, dari atas ke bawah, dalam urutan yang sama dengan urutan pasangannya. Baru setelah itu panah ditarik:

```latex
% Dua elips: domain di kiri, kodomain di kanan
\draw[thick, fill=blue!10] (0,0) ellipse (1.4 and 2.2);
\draw[thick, fill=green!10] (5,0) ellipse (1.4 and 2.2);
\node[above] at (0,2.2) {$A$};
\node[above] at (5,2.2) {$B$};

% Anggota himpunan A (kiri), dari atas ke bawah
\node (a1) at (0,1.5) {$\bullet$ Rani};
\node (a2) at (0,0.5) {$\bullet$ Sinta};
\node (a3) at (0,-0.5) {$\bullet$ Tono};
\node (a4) at (0,-1.5) {$\bullet$ Wati};

% Anggota himpunan B (kanan), sejajar dengan pasangannya
\node (b1) at (5,1.5) {$\bullet$ Membaca};
\node (b2) at (5,0.5) {$\bullet$ Menari};
\node (b3) at (5,-0.5) {$\bullet$ Melukis};
\node (b4) at (5,-1.5) {$\bullet$ Berenang};

% Panah: selalu dari kiri ke kanan, sejajar
\draw[->, thick] (a1) -- (b1);
\draw[->, thick] (a2) -- (b2);
\draw[->, thick] (a3) -- (b3);
\draw[->, thick] (a4) -- (b4);
```

Perhatikan satu hal kecil yang sering dilupakan siswa: nama himpunan $A$ dan $B$ ditulis di atas elipsnya. Tanpa nama itu, dua oval hanyalah dua gambar, bukan dua himpunan. Dan aturan relasinya — dalam hal ini "gemar" — sebaiknya ditulis di bawah atau di atas diagram, supaya pembaca tidak perlu menebak apa arti panah itu.

## Dari relasi ke fungsi: satu anggota, satu panah

Setelah diagram relasi rapi, saya mengajukan pertanyaan lanjutan: apakah relasi ini juga sebuah fungsi? Di sinilah diagram panah menunjukkan kekuatannya. Pada diagram, jawabannya bisa dibaca tanpa menghitung apa pun: sebuah relasi adalah fungsi bila setiap anggota domain mempunyai tepat satu panah keluar — tidak boleh kosong, tidak boleh bercabang.

Contoh fungsi yang mudah digambar adalah relasi "setengah dari" antara $A = \lbrace 1, 2, 3, 4 \rbrace$ dan $B = \lbrace 2, 4, 6, 8 \rbrace$: $1 \to 2$, $2 \to 4$, $3 \to 6$, dan $4 \to 8$. Setiap anggota $A$ tepat satu panah, sehingga diagramnya empat garis mendatar yang rapi.

Lalu saya mengubah satu hal saja: Sinta ternyata gemar menari dan melukis sekaligus. Pada diagram relasi hobi tadi, dari titik Sinta kini keluar dua panah, satu ke Menari dan satu ke Melukis. Relasinya tetap sah sebagai relasi, tetapi ia bukan lagi fungsi, karena satu anggota domain mempunyai dua panah keluar. Siswa yang tadinya menghafal definisi fungsi sebagai kalimat panjang kini bisa melihatnya: fungsi itu diagram yang dari setiap titik kirinya keluar tepat satu panah.

## Tiga kesalahan yang paling sering saya temui

Kesalahan pertama adalah panah terbalik: siswa menggambar panah dari kodomain ke domain, misalnya dari "Membaca" ke "Rani", karena mereka membaca pasangan dari kanan. Saya mengatasinya dengan aturan yang tidak bisa ditawar: panah selalu berangkat dari domain, dari kiri ke kanan, tanpa kecuali. Kalau panahnya mengarah ke kiri, gambarnya salah, apa pun isi pasangannya.

Kesalahan kedua adalah anggota yang tidak sejajar dengan pasangannya, sehingga panah-panah saling menyilang. Obatnya sudah dibahas di atas: susun dulu urutan anggota di kedua oval sebelum menarik panah, dan letakkan pasangan pada baris yang sama.

Kesalahan ketiga adalah lupa menuliskan aturan relasi dan nama himpunan. Diagram tanpa nama himpunan dan tanpa aturan adalah gambar yang bisu: ia menunjukkan panah-panah, tetapi tidak mengatakan apa arti panah itu. Saya selalu meminta siswa menuliskan $A$, $B$, dan aturan relasinya — "gemar", "setengah dari", "faktor dari" — sebelum mereka merasa diagramnya selesai.

Di kelas, saya kini memproyeksikan dua diagram berdampingan: di kiri diagram relasi hobi yang setiap titiknya tepat satu panah, di kanan diagram yang sama tetapi Sinta mempunyai dua panah. Lalu saya bertanya satu hal saja: diagram mana yang merupakan fungsi, dan dari mana kamu tahu? Siswa tidak lagi menjawab dengan hafalan. Mereka menunjuk titik Sinta yang bercabang itu dan berkata, "Yang kanan bukan fungsi, Pak, karena dari Sinta keluar dua panah." Begitu jawabannya terbaca dari gambar, definisinya mengikuti dengan sendirinya.

Berkas TikZ lengkap ketiga gambar di atas bisa diunduh di bawah ini. Silakan ubah nama anggota dan aturan relasinya dan lihat bagaimana diagramnya ikut berubah.

> 📎 **Berkas TikZ lengkap:** [diagram-panah-relasi.tex](tex/diagram-panah-relasi.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
