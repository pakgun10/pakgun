---
weight: 1
title: "Mengapa Luas Lingkaran Sama dengan πr²? Pendalaman Rumus yang Sering Dihafal Saja"
date: 2026-11-07T00:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman rumus luas lingkaran untuk kelas VIII: membongkar mengapa luasnya πr² lewat potongan pizza yang disusun jadi persegi panjang, memeriksa dengan angka, dan tiga jebakan yang paling sering muncul di soal."
featuredImage: "featured-image.png"

tags: ["Luas Lingkaran", "Lingkaran", "Pendalaman", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas VIII saya minggu ini, satu pertanyaan sederhana membuat saya menutup spidol dan duduk di tepi meja. Seorang murid mengangkat tangan lalu bertanya, "Pak, kenapa luas lingkaran itu $\pi r^2$? Kenapa bukan $\pi r$ saja, seperti keliling yang $2\pi r$?" Kelas mendadak hening. Bukan karena mereka tidak tahu jawabannya, melainkan karena mereka sadar: selama ini mereka menghafal rumus itu tanpa pernah benar-benar tahu dari mana datangnya. Saya pun mengaku di depan kelas: dulu saya juga menghafalnya begitu saja. Hari itu kami sepakat membongkarnya bersama-sama, dan ternyata membongkar rumus ini jauh lebih menyenangkan daripada menghafalnya.

Artikel ini adalah pendalaman dari latihan keliling dan luas lingkaran yang sudah kita kerjakan sebelumnya. Kalau kemarin kita berlatih menghitung, hari ini kita mencari tahu mengapa rumusnya berbentuk seperti itu, dan kapan rasa yakin itu boleh dipercaya.

<!--more-->

## Potong lingkaran seperti pizza

Cara paling jujur untuk memahami luas lingkaran adalah dengan mengguntingnya. Saya membayangkan sebuah lingkaran sebagai pizza bundar. Potong pizza itu menjadi juring-juring yang sama besar, seperti potongan pizza biasa. Makin banyak potongannya, makin ramping setiap juringnya. Kalau potongannya hanya empat, juringnya masih gemuk dan melengkung jelas. Kalau potongannya enam belas, setiap juring sudah hampir menyerupai segitiga yang ramping.

Sekarang susun juring-juring itu berselang-seling: satu menghadap ke atas, satu menghadap ke bawah, begitu seterusnya, seperti menyusun potongan pizza menjadi satu baris. Yang terjadi mengejutkan: susunan itu hampir membentuk persegi panjang. Sisi atas dan bawahnya memang masih sedikit bergelombang, tetapi makin banyak juringnya, makin lurus gelombang itu, dan bentuknya makin mirip persegi panjang sungguhan. Di sinilah letak keindahannya: luas lingkaran yang melengkung itu ternyata sama dengan luas persegi panjang yang sisi-sisinya bisa kita ukur.

## Dari setengah keliling ke rumus

Begitu susunannya menyerupai persegi panjang, pertanyaannya tinggal dua: berapa panjangnya, dan berapa lebarnya? Lebarnya mudah dijawab: setiap juring tingginya sama dengan jari-jari lingkaran, jadi lebar persegi panjang itu adalah $r$. Panjangnya sedikit lebih licik. Sisi panjang persegi panjang itu tersusun dari busur-busur juring, dan jumlah semua busur di sisi atas sama dengan setengah keliling lingkaran. Keliling lingkaran adalah $2\pi r$, jadi setengahnya adalah $\pi r$.

Maka luas persegi panjang itu adalah panjang kali lebar, yaitu $\pi r \times r$, yang sama dengan $\pi r^2$. Rumus yang selama ini dihafal itu ternyata bukan datang dari langit. Ia adalah luas persegi panjang yang tersembunyi di dalam lingkaran. Begitu murid melihatnya, pertanyaan "kenapa pangkat dua?" terjawab sendiri: karena ada dua kali $r$ yang berperan, satu dari setengah keliling dan satu lagi dari lebar. Satu $r$ datang dari keliling, satu $r$ datang dari jari-jari, dan keduanya bertemu dalam perkalian.

## Cek dengan angka

Penjelasan yang bagus harus tahan diuji angka. Ambil lingkaran berjari-jari 7 cm. Pakai $\pi = \frac{22}{7}$ karena 7 habis dibagi 7. Luasnya adalah $\frac{22}{7} \times 7^2 = \frac{22}{7} \times 49 = 22 \times 7 = 154$ cm². Sekarang bayangkan potongan pizzanya: setengah kelilingnya adalah $\frac{22}{7} \times 7 = 22$ cm, dan lebarnya 7 cm, sehingga luas persegi panjangnya $22 \times 7 = 154$ cm². Sama persis. Angka itu cocok bukan karena kebetulan, melainkan karena keduanya memang menghitung luas yang sama dengan cara yang berbeda.

Contoh kedua, jari-jari 10 cm dengan $\pi = 3{,}14$. Luasnya $3{,}14 \times 10^2 = 3{,}14 \times 100 = 314$ cm². Setengah kelilingnya $3{,}14 \times 10 = 31{,}4$ cm, lebarnya 10 cm, dan $31{,}4 \times 10 = 314$ cm². Lagi-lagi cocok. Saya meminta murid mencoba satu jari-jari lain sendiri di buku mereka, dan hampir semua menemukan kecocokan yang sama. Rumus yang tadinya terasa seperti hafalan berubah menjadi sesuatu yang bisa mereka buktikan dengan tangan mereka sendiri.

## Tiga jebakan yang paling sering muncul

Jebakan pertama adalah memakai diameter sebagai jari-jari. Soal memberi diameter 14 cm, murid langsung menghitung $\frac{22}{7} \times 14^2 = 616$ cm². Padahal jari-jarinya hanya 7 cm, dan jawaban yang benar adalah 154 cm². Jawaban yang salah itu empat kali lipat dari yang benar, karena $14^2$ adalah empat kali $7^2$. Begitu murid sadar bahwa mengkuadratkan menggandakan kesalahan, mereka mulai memeriksa dulu: yang diketahui ini jari-jari atau diameter?

Jebakan kedua adalah lupa mengkuadratkan. Murid menghitung $3{,}14 \times 10 = 31{,}4$ cm² untuk jari-jari 10 cm, lalu heran kenapa jawabannya terasa terlalu kecil. Itu karena yang dihitung baru setengah keliling, bukan luas. Luas butuh $r^2$, bukan $r$. Saya mengingatkan mereka dengan pertanyaan yang sama seperti di awal pelajaran: kalau hanya $\pi r$, itu keliling, bukan luas.

Jebakan ketiga adalah memilih $\pi$ yang salah. Aturan praktisnya sederhana: kalau jari-jarinya kelipatan 7, pakai $\frac{22}{7}$ supaya hitungannya bersih. Kalau bukan kelipatan 7, pakai 3,14. Murid yang memakai 3,14 untuk jari-jari 7 akan mendapat 153,86 cm², tidak salah secara konsep tetapi berantakan dan rawan salah hitung di tengah jalan. Memilih $\pi$ yang tepat adalah separuh pekerjaan.

## Kegiatan: gunting satu lingkaran kertas

Kalau ada waktu sepuluh menit di akhir pelajaran, saya menyuruh murid menggunting satu lingkaran kertas menjadi delapan juring, lalu menyusunnya seperti yang saya ceritakan. Tidak perlu rapi. Yang penting mereka melihat sendiri bahwa susunan juring itu mendekati persegi panjang, mengukur panjang dan lebarnya dengan penggaris, lalu mengalikannya dan membandingkannya dengan $\pi r^2$. Hampir selalu ada yang berseru, "Lho, Pak, kok sama?" Seruan itulah yang saya tunggu. Rumus yang ditemukan sendiri jauh lebih lama tinggalnya daripada rumus yang didiktekan.

Rumus luas lingkaran akhirnya bukan lagi sekadar baris di buku catatan. Ia adalah cerita tentang pizza yang dipotong, disusun ulang, dan diukur kembali. Dan setiap kali murid menulis $\pi r^2$ setelah hari itu, saya berharap mereka ingat sejenak potongan pizza di meja mereka, bukan sekadar huruf-huruf yang harus dihafal sebelum ulangan.
