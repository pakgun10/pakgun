---
title: "Ubin yang Tak Bertemu Kecuali di Sudut: Menggambar Tesselasi Heksagon dengan TikZ"
date: 2026-11-04T18:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Tesselasi heksagon adalah cara paling enak membicarakan sudut dan pola sekaligus — dari lantai masjid sampai sarang lebah, lalu digambar dengan TikZ yang bisa dihitung siswa."
featuredImage: "featured-image.png"
tags: ["TikZ", "tesselasi", "heksagon", "geometri"]
categories: ["Matematika"]
math:
  enable: true
---

Saat istirahat, ada siswa yang mengamati lantai koridor sekolah lalu bertanya, "Pak, kenapa keramiknya kotak semua? Kenapa nggak ada yang bentuk sarang lebah?" Saya senang sekali mendengar pertanyaan itu, karena di baliknya ada salah satu ide paling indah dalam geometri: tesselasi — cara menyusubiksa bentuk-bentuk sampai menutup bidang tanpa celah dan tanpa tumpang tindih. Dan heksagon, seperti dalam pertanyaannya, adalah tokoh paling menarik dalam cerita ini.

<!--more-->

## Kenapa heksagon layak diundang

Bicara tesselasi berarti bicara sudut dalam. Syaratnya sederhana untuk disampaikan ke siswa SMP: pada satu titik pertemuan, semua sudut yang bertemu harus berjumlah tepat $360^\circ$ — tidak boleh lebih (ada tumpang tindih), tidak boleh kurang (ada celah). Heksagon beraturan punya sudut dalam $120^\circ$, jadi tiga heksagon bertemu di satu titik: $3 \times 120^\circ = 360^\circ$. Pas sempurna.

Saya selalu membandingkannya dengan tetangga-tetangganya. Segitiga sama sisi punya sudut $60^\circ$, dan enam segitiga bisa bertemu di satu titik. Persegi punya sudut $90^\circ$, dan empat persegi cocok. Tapi pentagon beraturan? Sudut dalamnya $108^\circ$. Tiga buah menjumlah $324^\circ$ — kurang, ada celah. Empat buah melebihi $360^\circ$ — tidak muat. Pentagon beraturan dilarang masuk pesta ini, dan siswa biasanya tidak menyangka itu: bentuknya terlihat "rapi", kok ditolak?

Hanya ada tiga bangun beraturan yang bisa menutup bidang sendirian — segitiga, persegi, heksagon — dan siswa bisa menemukan ketiganya sendiri hanya dengan berhitung di atas satu syarat sederhana. Jenis pembelajaran yang membuat saya tetap semangat.

## Menggambarnya dengan jujur pada sudutnya

Menggambar tesselasi heksagon di papan tulis adalah pekerjaan yang menghukum ketidaktelitian. Heksagon kedua harus menempel tepat pada sisi heksagon pertama, dan begitu terus; satu derajat yang miring akan terlihat lama-lama sebagai celah yang memalukan. Dengan TikZ, saya cukup menuliskan satu heksagon dan perintah pengulangannya, dengan jarak geser yang dihitung dari geometri heksagon itu sendiri:

```latex
\foreach \i in {-4,...,3}
  \foreach \j in {-4,...,3}{
    \begin{scope}[shift={(1.5*\i, {2.598076*\j
        + mod(abs(\i),2)*1.299038})}]
      \draw[thick] (0:1) \foreach \a in {60,120,...,300}
        { -- (\a:1)} -- cycle;
    \end{scope}}
```

Angka-angka yang menarik perhatian siswa justru di baris pergeseran. Heksagon dengan jari-jari 1 punya lebar $1{,}5$ antar pusat yang bersisian secara horizontal, dan tinggi antar barisnya $\frac{3\sqrt{3}}{2} \approx 2{,}598076$ — persis angka yang muncul di kode. Bahkan offset setengah baris ($1{,}299038$, yaitu separuh dari $2{,}598076$) pada kolom bergantian juga lahir dari geometri yang sama. Tidak ada angka asal: semuanya bisa diturunkan siswa dengan trigonometri sederhana atau bahkan dengan mengetahui bahwa tinggi heksagon dari titik datar ke titik datar adalah $\sqrt{3}$.

Hasil gambarnya seperti ini:

![Tesselasi heksagon beraturan; setiap heksagon berbagi tiga tetangga di sudut-sudutnya](tesselasi-heksagon.png)

Sekali lagi, gambar yang dihasilkan prosedur ini tidak bisa mengelabui. Kalau formula pergeserannya salah, gambar langsung jujur: muncul celah atau tumpang tindih. Justru di titik itu gambar menjadi alat diagnosis, bukan sekadar hiasan. Saya pernah sengaja menunjukkan versi yang pergeseran barisnya salah — dan siswa langsung berteriak menemukan kesalahannya. Mereka mengoreksi matematikanya dengan matanya.

## Menebar dan menghitung tetangga

Dari gambar utuh, saya biasanya meminta siswa menelusuri satu heksagon dan menghitung tetangganya. Ada enam heksagon yang menempel pada keenam sisinya — tapi ada juga tetangga yang hanya "bertemu di satu titik sudut", tanpa berbagi sisi. Pada gambar di atas saya tandai salah satu: dari satu heksagon, tetangga lewat sudut ada tiga. Perbedaan "berbagi sisi" versus "berbagi titik" ini terdengar sepele, tapi ia adalah pintu masuk ke ide keterhubungan dan penghitungan yang nantinya muncul lagi di banyak tempat, termasuk saat mereka kelak bertemu pola bilangan.

Percakapan ini juga selalu melahirkan contoh dari dunia nyata. Sarang lebah, yang oleh siswa sering disebut lebih dulu daripada yang saya duga, adalah contoh klasiknya — dan justru menarik karena heksagon bukan pilihan sembarangan: di antara tiga tesselasi beraturan, heksagon menutup bidang paling hemat "dinding" per luas yang dilindungi. Saya tidak mengklaim lebah menghitung; saya hanya mengajak siswa menghitung, dan membiarkan angka bicara.

## Kembali ke lantai koridor

Di akhir sesi, saya kembali ke pertanyaan siswa tadi: kenapa keramik sekolah kotak semua? Jawaban yang terbaik datang dari siswa sendiri setelah eksperimen kecil dengan kertas gunting: potong persegi memang paling mudah dan paling sedikit sisa potongannya. Heksagon mungkin lebih hemat dinding dalam dunia lebah, tapi menggunting heksagon dari selembar kertas meninggalkan banyak potongan sisa di antara sudut-sudutnya. Matematika menyediakan kemungkinan; manusia menimbang praktisnya.

Dan di titik itulah pelajaran ini menurut saya berhasil. Siswa pulang membawa satu hal yang lebih dari rumus: kesadaran bahwa lantai, langit-langit, kain, dan sarang lebah adalah kertas ujian geometri yang menyebar di sekitar mereka — dan bahwa dengan sedikit perhitungan sudut, mereka kini bisa membacanya. Kalau sorenya ada yang menatap keramik rumahnya lebih lama dari biasanya, saya anggap pelajaran hari itu sudah tuntas.

> 📎 **Berkas TikZ lengkap:** [tesselasi-heksagon.tex](tex/tesselasi-heksagon.tex) — siap kompilasi (butuh paket `tikz` dan `xcolor`).
