---
weight: 1
title: "Mengapa Volume Kerucut Hanya Sepertiga Volume Tabung? Pendalaman Bangun Ruang Sisi Lengkung"
date: 2026-11-07T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Pendalaman bangun ruang sisi lengkung untuk kelas IX: membuktikan lewat percobaan pasir dan hitungan mengapa volume kerucut selalu sepertiga volume tabung yang alas dan tingginya sama."
featuredImage: "featured-image.png"

tags: ["Volume Kerucut", "Pendalaman", "Kelas IX", "Bangun Ruang Sisi Lengkung"]
categories: ["Matematika"]

math:
  enable: true
---

Di kelas IX saya, kami baru saja selesai menghitung volume tabung. Rumusnya sudah menempel di kepala murid: luas alas dikali tinggi. Lalu saya menggambar sebuah kerucut di papan tulis, dengan alas dan tinggi yang sama persis dengan tabung tadi, dan menuliskan rumusnya. Seorang murid di bangku kedua mengangkat tangan. "Pak, kenapa kerucut dapat jatah sepertiga? Kenapa tidak setengah? Kan kerucut itu tabung yang mengecil ke atas?"

Saya diam sejenak, karena pertanyaannya memang bagus. Sepertiga itu angka yang aneh. Setengah terasa wajar: kerucut kan seperti tabung yang dipotong miring dari dua sisi. Tetapi matematika tidak tunduk pada perasaan wajar. Artikel ini adalah pendalaman dari materi bangun ruang sisi lengkung yang sudah kita pelajari: hari ini kita membuktikan sendiri — dengan pasir, dengan hitungan, dan dengan satu analogi — mengapa volume kerucut selalu sepertiga volume tabung yang alas dan tingginya sama.

<!--more-->

## Tiga kerucut mengisi satu tabung

Bukti pertama tidak butuh rumus sama sekali. Saya membawa dua wadah dari karton: sebuah tabung terbuka dan sebuah kerucut terbuka, dengan jari-jari alas yang sama dan tinggi yang sama. Di depan kelas, saya meminta seorang murid mengisi kerucut itu dengan beras sampai penuh, lalu menuangkannya ke dalam tabung. Satu kerucut penuh: tabung baru terisi sepertiga. Kerucut kedua: dua pertiga. Kerucut ketiga: tabung penuh, pas, tidak tumpah.

Kelas terdiam sebentar, lalu ramai. Tidak ada yang perlu dihafal dari percobaan itu, karena mata mereka sendiri yang melihat: tiga kerucut sama dengan satu tabung. Kalau besok mereka lupa rumusnya, mereka masih ingat gambar tiga tuangan beras itu. Dan justru karena itu saya selalu menyarankan: kalau ada kesempatan, buat wadah kartonnya bersama murid. Kerucut yang mereka gunting dan lem sendiri jauh lebih lama tinggal di ingatan daripada rumus yang mereka salin dari papan tulis.

## Menghitungnya dengan rumus

Percobaan memberi keyakinan, tetapi hitungan memberi kepastian angka. Rumus volume kerucut adalah

$$V = \frac{1}{3} \pi r^2 t$$

dengan $r$ jari-jari alas dan $t$ tinggi kerucut. Perhatikan bahwa $\pi r^2 t$ adalah volume tabung yang alas dan tingginya sama — jadi rumus kerucut itu sebenarnya berkata: ambil volume tabungnya, lalu bagi tiga.

Contoh pertama, angka yang ramah. Sebuah kerucut berjari-jari $3$ cm dan tinggi $6$ cm. Volume tabung yang sama alas dan tingginya adalah $3,14 \times 3^2 \times 6 = 3,14 \times 9 \times 6 = 169,56$ cm³. Maka volume kerucutnya $\frac{1}{3} \times 169,56 = 56,52$ cm³.

Contoh kedua, angka yang menguji ketelitian. Sebuah kerucut berjari-jari $7$ cm dan tinggi $10$ cm. Karena jari-jarinya kelipatan $7$, saya memakai $\pi = \frac{22}{7}$. Volume tabungnya $\frac{22}{7} \times 7^2 \times 10 = \frac{22}{7} \times 49 \times 10 = 1540$ cm³. Maka volume kerucutnya $\frac{1540}{3} = 513\frac{1}{3}$ cm³, atau sekitar $513,33$ cm³. Murid yang menulis $513$ saja saya minta menambahkan koma dan tiga-tiganya: pembagian tiga yang tidak habis itu bukan kesalahan, melainkan sifat angkanya.

## Mengapa sepertiga, bukan setengah?

Inilah bagian yang paling saya sukai, karena jawabannya memakai sesuatu yang sudah mereka kenal: luas segitiga. Luas segitiga adalah setengah dari luas persegi panjang yang alas dan tingginya sama. Mengapa setengah? Karena segitiga adalah persegi panjang yang meruncing ke satu titik pada satu sisi. Satu arah peruncingan, faktornya setengah.

Kerucut meruncing ke satu titik juga — tetapi ke segala arah, melingkar penuh. Limas segiempat pun begitu: volumenya sepertiga dari balok yang alas dan tingginya sama. Polanya konsisten: bangun yang meruncing ke satu titik dari seluruh sisi alasnya mendapat jatah sepertiga dari bangun tegaknya. Saya tekankan kepada murid bahwa ini cara merasakan, bukan bukti formal — bukti formalnya menunggu di jenjang berikutnya, dengan cara mengiris bangun itu lapis demi lapis. Tetapi rasa yang benar itu penting: rumus yang dipahami sebagai pola akan lebih lama tinggal daripada rumus yang dihafal sebagai bunyi.

## Tiga jebakan yang paling sering muncul

Setelah pola dipahami, barulah saya menunjukkan tiga jebakan yang selalu muncul di latihan. Jebakan pertama, lupa mengalikan sepertiga. Hasilnya langsung tiga kali lipat dari jawaban benar — kesalahan yang paling mahal dan paling mudah dicegah: tulis $\frac{1}{3}$ di awal, sebelum menghitung apa pun.

Jebakan kedua, memakai diameter sebagai jari-jari. Soal sering memberi diameter, misalnya $14$ cm, dan murid langsung memasukkan $14$ ke $r^2$. Padahal jari-jarinya $7$ cm. Karena jari-jari dikuadratkan, kesalahan ini membuat volume menjadi empat kali lipat. Aturan saya di kelas: begitu membaca soal, lingkari dulu yang diketahui — diameter atau jari-jari — baru menghitung.

Jebakan ketiga, memakai garis pelukis sebagai tinggi. Garis pelukis adalah sisi miring kerucut, bukan tingginya. Sebuah kerucut dengan garis pelukis $10$ cm dan jari-jari $6$ cm tidak memiliki tinggi $10$ cm. Tingginya harus dicari dulu dengan Pythagoras: $t = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8$ cm. Barulah volumenya $\frac{1}{3} \times 3,14 \times 6^2 \times 8 = \frac{1}{3} \times 904,32 = 301,44$ cm³. Angka $6$, $8$, $10$ itu tripel Pythagoras yang sudah mereka kenal — kebetulan yang menyenangkan, bukan kebetulan yang saya rencanakan.

## Kalau ukurannya berubah, volumenya berubah berapa?

Pendalaman yang sesungguhnya adalah ketika murid mulai bertanya sendiri. Bagaimana kalau jari-jarinya dilipatgandakan? Kerucut pertama tadi berjari-jari $3$ cm, tinggi $6$ cm, volumenya $56,52$ cm³. Kalau jari-jarinya menjadi $6$ cm dengan tinggi tetap, volumenya $\frac{1}{3} \times 3,14 \times 6^2 \times 6 = 226,08$ cm³ — tepat empat kali lipat, karena jari-jari dikuadratkan dalam rumus.

Bagaimana kalau semua ukuran menjadi setengahnya? Kerucut kecil berjari-jari $1,5$ cm dan tinggi $3$ cm volumenya $\frac{1}{3} \times 3,14 \times 1,5^2 \times 3 = 7,065$ cm³. Itu seperdelapan dari $56,52$ cm³, karena setiap ukuran dikali setengah dan ada tiga ukuran yang dikalikan: setengah pangkat tiga sama dengan seperdelapan. Murid yang menemukan sendiri pola seperdelapan ini biasanya tersenyum — mereka baru saja memegang satu ide besar matematika: volume berubah menurut pangkat tiga dari perubahan ukuran.

Jadi, sepertiga itu bukan angka yang dijatuhkan dari langit. Ia bisa dilihat lewat tiga tuangan beras, dihitung lewat dua contoh angka, dirasakan lewat analogi segitiga, dan diuji lewat perubahan ukuran. Murid saya yang bertanya di awal tadi akhirnya mengangguk. "Jadi kerucut itu tabung yang mengecil, Pak — tapi mengecil ke segala arah, makanya jatahnya sepertiga, bukan setengah." Saya tidak bisa merangkumnya lebih baik dari itu. Kadang, pendalaman terbaik adalah ketika guru berhenti menjelaskan dan murid yang menjelaskan kembali.
