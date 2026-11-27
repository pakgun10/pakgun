---
weight: 1
title: "Mengapa Rata-rata Kelas Bisa Menipu? Pendalaman Mean, Median, dan Data Pencilan"
date: 2026-11-28T04:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman mean dan median untuk kelas VIII: mengapa satu nilai pencilan bisa menarik rata-rata menjauh dari kebanyakan murid, dan kapan nilai tengah lebih jujur mewakili kelas."
featuredImage: "featured-image.png"

tags: ["Mean", "Median", "Statistika", "Pendalaman", "Kelas VIII"]
categories: ["Matematika"]

math:
  enable: true
---

Suatu pagi di kelas VIII, saya menulis satu angka di papan tulis: 69,1. "Ini rata-rata nilai ulangan kita kemarin," kata saya. Seorang murid di baris tengah mengangkat tangan. "Pak, kok rata-rata kita 69,1, padahal nilai saya 65 dan teman-teman saya juga kebanyakan 60-an? Siapa yang nilainya 69?" Saya tersenyum, karena pertanyaan itu tepat sekali. Rata-rata memang bisa menipu — bukan karena rumusnya salah, melainkan karena satu angka yang jauh dari yang lain bisa menarik rata-rata ke arahnya, sementara kebanyakan murid justru berada jauh dari angka itu. Hari ini saya ingin mengajak Anda mengintip cara kerja tipuan itu, supaya lain kali Anda tidak langsung percaya pada satu angka.

<!--more-->

## Satu nilai 100 mengubah segalanya

Mari kita lihat data yang saya tulis di papan hari itu. Sepuluh nilai ulangan, sudah saya urutkan dari yang terkecil:

$$60,\ 62,\ 64,\ 65,\ 66,\ 67,\ 68,\ 69,\ 70,\ 100$$

Jumlah seluruhnya adalah $691$, dan karena ada 10 murid, rata-ratanya adalah $\frac{691}{10} = 69{,}1$. Sekilas tidak ada yang aneh. Tetapi perhatikan: berapa murid yang nilainya di bawah 69,1? Delapan murid. Hanya dua murid yang nilainya di atas rata-rata, dan salah satunya adalah murid yang mendapat 100. Satu nilai 100 itu menyumbang terlalu banyak pada jumlah total, sehingga rata-rata terangkat naik — padahal sembilan murid lainnya nilainya berkisar antara 60 dan 70.

Sekarang coba kita keluarkan nilai 100 itu sejenak. Sembilan nilai yang tersisa berjumlah $591$, dan rata-ratanya menjadi $\frac{591}{9} = 65{,}7$. Selisihnya 3,4 poin, hanya karena satu murid. Inilah yang dalam statistika disebut **data pencilan** atau *outlier*: satu nilai yang jauh menyimpang dari kelompoknya, dan karena rata-rata menghitung semua nilai dengan bobot yang sama, pencilan itu ikut menarik rata-rata ke arahnya. Rata-rata tidak berbohong tentang jumlah total — tetapi ia bisa berbohong tentang "murid yang biasa".

## Median: nilai tengah yang tidak bisa ditarik

Lalu adakah ukuran yang lebih tahan terhadap pencilan? Ada: **median**, atau nilai tengah. Caranya sederhana. Urutkan data dari yang terkecil, lalu ambil nilai yang berada tepat di tengah. Karena data kita berjumlah 10 — genap — maka mediannya adalah rata-rata dari dua nilai tengah, yaitu nilai ke-5 dan ke-6: $\frac{66 + 67}{2} = 66{,}5$.

Bandingkan: rata-rata 69,1, median 66,5. Median berada di tengah-tengah kelompok nilai yang sebenarnya, di antara 60 dan 70, tempat delapan dari sepuluh murid berada. Sekarang coba ganti nilai 100 itu menjadi 90, atau 80, atau bahkan 1000. Median tetap 66,5 — ia tidak peduli seberapa besar pencilan itu, karena ia hanya peduli pada posisi, bukan pada besarnya nilai. Inilah kekuatan median: ia tidak bisa ditarik oleh satu angka ekstrem.

Namun median pun bukan tanpa kelemahan. Ia mengabaikan besarnya nilai di ujung-ujung data, sehingga dua kelas dengan median sama bisa memiliki cerita yang berbeda. Kelas yang nilainya 60, 66, 67, 68, 100 dan kelas yang nilainya 64, 65, 66, 67, 68 memiliki median yang sama, 66, tetapi sebarannya jauh berbeda. Karena itu, guru yang bijak tidak memilih satu ukuran lalu membuang yang lain — ia membandingkan keduanya, dan selisih antara keduanya justru menjadi petunjuk: bila rata-rata jauh di atas median, ada pencilan besar di atas; bila jauh di bawah, ada pencilan kecil di bawah.

## Gaji rata-rata yang membuat semua orang merasa miskin

Tipuan yang sama terjadi di luar kelas, dan contoh yang paling terkenal adalah gaji. Bayangkan sebuah kantor kecil dengan sepuluh karyawan: sembilan orang bergaji Rp3.000.000 dan satu direktur bergaji Rp30.000.000. Jumlah seluruh gaji adalah Rp57.000.000, sehingga gaji rata-ratanya adalah Rp5.700.000. Bila perusahaan itu mengumumkan "gaji rata-rata karyawan kami Rp5,7 juta", sembilan dari sepuluh karyawannya akan mengernyit: gaji mereka hanya Rp3 juta. Median gaji di kantor itu adalah Rp3.000.000 — angka yang jauh lebih jujur menggambarkan karyawan yang biasa.

Contoh ini sering saya ceritakan di kelas, karena murid langsung paham mengapa berita tentang "penghasilan rata-rata" kadang terasa jauh dari kehidupan mereka. Rata-rata adalah angka yang benar secara hitungan, tetapi bisa salah secara cerita. Dan di sinilah matematika bertemu dengan kehidupan: menghitung itu mudah, tetapi memutuskan angka mana yang pantas mewakili sekelompok orang adalah soal kejujuran.

## Kegiatan lima menit di kelas

Saya biasa menutup materi ini dengan kegiatan singkat. Saya menulis sepuluh nilai di papan — seperti data di atas — lalu meminta murid menghitung rata-rata dan mediannya sendiri, kemudian menjawab satu pertanyaan: "Angka mana yang lebih adil mewakili kelas kita?" Jawaban mereka hampir selalu terbagi, dan perdebatan kecil itu justru yang saya cari. Ada yang membela rata-rata karena ia memakai semua nilai, ada yang membela median karena ia tidak bisa ditarik satu orang.

Di akhir kegiatan saya menambahkan satu pertanyaan lagi: "Kalau nilai 100 itu ternyata salah ketik dan seharusnya 70, apa yang berubah?" Mereka menghitung ulang: jumlah menjadi $661$, rata-rata menjadi $66{,}1$ — hampir sama dengan median $66{,}5$. Kelas itu pun sadar: ketika tidak ada pencilan, rata-rata dan median berdekatan dan saling menguatkan. Keduanya bercerita sama. Tetapi ketika ada pencilan, keduanya bercerita berbeda — dan tugas kita adalah mendengar kedua cerita itu sebelum mengambil kesimpulan.

Jadi, lain kali Anda melihat satu angka rata-rata — rata-rata nilai kelas, rata-rata penghasilan, rata-rata apa pun — tanyakanlah satu hal: berapa mediannya? Bila keduanya berdekatan, angka itu bisa dipercaya. Bila keduanya berjauhan, ada satu cerita yang sedang disembunyikan oleh satu angka yang terlalu besar, atau terlalu kecil. Dan murid yang bertanya "siapa yang nilainya 69?" di awal pelajaran tadi — ia sudah mengerti hal yang paling penting: angka tidak pernah bercerita sendiri. Kitalah yang harus bertanya.
