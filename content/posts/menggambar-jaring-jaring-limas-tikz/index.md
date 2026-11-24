---
title: "Menggambar Jaring-Jaring Limas dengan TikZ: Satu Alas, Empat Segitiga, dan Lipatan yang Bisa Dibuktikan"
date: 2026-11-23T16:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Jaring-jaring limas sering digambar asal jadi. Dengan TikZ, saya bisa membuat gambar yang proporsional, menempel pas di titik sudutnya, dan siap dipakai ulang di soal."
featuredImage: "featured-image.png"
tags: ["TikZ", "geometri", "bangun ruang sisi datar", "jaring-jaring", "media pembelajaran"]
categories: ["Matematika"]
math:
  enable: true
---

Bapak/Ibu, kalau ditanya materi SMP mana yang paling sering digambar asal-asalan, jawaban saya pasti sama: jaring-jaring limas. Bukan karena kita tidak peduli, tapi karena menggambarnya dengan jujur itu sungguh sulit. Sisi tegak limas harus ditempelkan pas pada sisi alasnya, garis lipatannya harus bertemu tepat di titik sudut, dan panjang sisi-sisinya harus masuk akal secara geometri. Di papan tulis dengan spidol yang mulai kering, saya sudah berkali-kali menghasilkan jaring-jaring yang — kalau benar-benar dipotong dan dilipat — tidak akan pernah menjadi limas. Segitiganya terlalu tinggi, atau justru tidak bertemu di satu puncak.

Seperti tulisan-tulisan saya sebelumnya tentang jaring-jaring balok dan jaring-jaring tabung, pekerjaan menggambar ini akhirnya saya pindahkan ke TikZ. Dan jaring-jaring limas ternyata lebih mengajarkan saya sesuatu daripada dua yang lain, karena limas punya karakter yang berbeda: alasnya bisa segitiga, bisa segiempat, bisa segi banyak, sementara sisi tegaknya selalu segitiga yang bertemu di satu puncak.

<!--more-->

## Mulai dari yang paling jujur: limas segitiga

Sebelum bicara jaring-jaring, saya selalu menampilkan limasnya sendiri dulu. Limas segitiga — atau tetrahedron, kalau Bapak/Ibu suka istilah yang lebih galak — punya empat titik sudut: satu puncak dan tiga di alas. Di TikZ, puncaknya cukup satu koordinat:

```latex
\coordinate (P) at (0,3.4);
\coordinate (A) at (-2.1,-1.2);
\coordinate (B) at (2.1,-1.2);
\coordinate (C) at (0.9,0.6);
```

Kemudian sisi-sisinya saya gambar dengan garis solid untuk rusuk yang terlihat dan garis putus-putus untuk rusuk yang tersembunyi di belakang. Rusuk $AC$ yang putus-putus itu justru bagian favorit saya. Di papan tulis, siswa sering menganggap garis putus-putus sebagai "coretan bantu", padahal itu adalah rusuk sungguhan yang kebetulan tertutup badan limas. Ketika saya tunjukkan di gambar TikZ yang rapi — rusuk terlihat tebal putih, rusuk tersembunyi tipis dan terputus — mereka mulai membaca gambar bangun ruang sebagai objek tiga dimensi, bukan sekadar kumpulan segitiga.

{{< figure src="jaring-jaring-limas.png" caption="Limas segitiga dengan rusuk tersembunyi bergaris putus-putus (kiri), dan jaring-jaring limas segiempat: satu persegi di tengah dikelilingi empat segitiga (kanan)." >}}

Gambar di atas hasil kompilasi langsung dari berkas .tex yang saya sertakan di akhir tulisan ini. Tidak ada yang saya gambar tangan di aplikasi lain; setiap garis lahir dari koordinat yang bisa saya pertanggungjawabkan.

## Lalu dipotong dan dibentangkan

Bagian yang paling menarik sebenarnya adalah momen "memotong" limasnya. Bayangkan kita memotong sepanjang tiga rusuk tegaknya lalu membentangkan seluruh permukaan di atas meja. Untuk limas segiempat, hasilnya khas: satu persegi di tengah, dan empat segitiga yang menempel di keempat sisinya, semuanya bertemu di satu titik puncak yang kini berpindah ke empat tempat berbeda.

Di TikZ, bentangan ini saya susun dari koordinat alas dulu — persegi dengan titik $(K_1)$ sampai $(K_4)$ — lalu setiap segitiga tegak saya "dudukkan" di salah satu sisi persegi dengan menghitung titik puncaknya secara eksplisit:

```latex
% segitiga di sisi atas persegi, tinggi 3, puncaknya di atas
\coordinate (P) at (0, 4.5);
% segitiga di sisi kanan, puncaknya di kanan
\coordinate (Q) at (4.5, 0);
```

Perhatikan satu hal yang menurut saya penting secara pedagogis: tinggi segitiga tegak pada jaring-jaring bukan tinggi limas. Kalau limasnya punya tinggi $3$ dan alasnya persegi bersisi $3$, jarak dari puncak ke titik tengah alas adalah $3$, tapi panjang rusuk tegaknya adalah

$$
\sqrt{3^2 + \left(\tfrac{3}{2}\sqrt{2}\right)^2} = \sqrt{9 + \tfrac{9}{2}} = \sqrt{13{,}5} \approx 3{,}67 .
$$

Jadi segitiga di jaring-jaring harus punya sisi sepanjang rusuk tegak itu, bukan sepanjang tinggi limas. Nah, di papan tulis, saya jujur saja sering malas menghitung dan menggambar segitiga "kira-kira segini". Di TikZ malas seperti itu tidak terbawa, karena koordinat puncak segitiga saya tulis langsung, dan kalau salah, bentangannya kelihatan aneh begitu saya lipat kembali secara imajiner. Gambar yang dibuat dari koordinat memaksa saya jujur pada ukuran.

Ini menurut saya pelajaran yang lebih besar daripada sekadar keahlian menggambar. Media yang gambar-gambarnya tidak konsisten diam-diam mengajarkan siswa bahwa matematika itu boleh kira-kira. Sebaliknya, gambar yang jujur pada ukuran diam-diam mengajarkan bahwa setiap panjang punya alasannya. Media itu bukan penghias; ia ikut mengajar.

## Siswa yang menyadari segitiganya "sejajar"

Percakapan kelas yang paling saya ingat dari materi ini datang bukan dari soal luas permukaan, melainkan dari seorang murid yang menatap jaring-jaring di layar lalu berkata, "Bu, kok segitiganya nggak ada yang ketiban sama alasnya?" Dia memperhatikan bahwa puncak-puncak segitiga tegak menghadap ke empat arah berbeda, tidak pernah menindih persegi alas. Pertanyaan itu membuka diskusi sepuluh menit tentang mengapa demikian: kalau segitiga itu menindih alas, berarti kita belum memotongnya, limasnya masih utuh.

Saya tidak pernah menyiapkan pertanyaan itu. Ia muncul karena gambarnya rapi sampai ke detail, sehingga yang tampak "salah" di gambar-gambar asal-asalan justru jadi bahan diskusi di gambar yang jujur. Itu keuntungan yang tidak saya rencanakan, tapi sudah beberapa kali saya rasakan sejak mulai serius dengan TikZ: ketika media saya rapi, siswa menatapnya lebih lama, dan menatap lebih lama berarti bertanya lebih banyak.

## Praktik: menyesuaikan dengan limas yang dibahas

Yang saya suka dari cara kerja berkas .tex adalah mudahnya menyesuaikan. Limas di kelas saya tidak selalu limas segiempat ideal; soal di buku menyajikan limas segi lima, limas dengan alas persegi panjang, limas yang terpotong. Mengubah koordinat satu-dua titik jauh lebih cepat daripada menggambar ulang, dan konsistensi gaya — warna, ketebalan garis, jenis huruf label — tetap terjaga di seluruh lembar soal.

Kalau Bapak/Ibu ingin mencoba, tiga hal yang menurut saya perlu dijaga:

Pertama, gambar limasnya dulu sebelum jaring-jaringnya. Siswa harus melihat objek utuh sebelum melihat bentangannya, sebab jaring-jaring tanpa limas hanyalah puzzle yang belum dijawab.

Kedua, pisahkan secara visual rusuk terlihat dan tersembunyi. Di TikZ ini cuma soal menambah opsi `dashed`, tapi efeknya besar pada cara siswa membaca gambar ruang.

Ketiga, jaga supaya sisi-sisi jaring-jaring benar-benar menempel di sisi alas — bukan di dekat sisi alas. Berbagi koordinat titik sudut (`\coordinate`) yang sama antara persegi dan segitiganya adalah cara paling aman; begitu titiknya sama, menempelnya pasti pas.

## Penutup: kejujuran yang bisa dilipat

Jaring-jaring pada dasarnya adalah janji: janji bahwa kalau kertas ini dipotong dan dilipat, ia akan menjadi limas. Gambar yang tidak konsisten pada ukurannya memecah janji itu, dan siswa yang benar-benar mencoba memotongnya akan kecewa pada matematika, bukan pada penggarisnya.

Dengan TikZ, janji itu bisa saya tepati. Dan setiap kali murid memotong lembar kerja berisi jaring-jaring hasil kompilasi, lalu memegang limas kertas yang benar-benar berdiri di meja, saya merasa pekerjaan menghitung koordinat itu sudah lunas dibayar.

> 📎 **Berkas TikZ lengkap:** [tikz-jaring-jaring-limas.tex](tex/tikz-jaring-jaring-limas.tex) — siap kompilasi (butuh paket `tikz`).
