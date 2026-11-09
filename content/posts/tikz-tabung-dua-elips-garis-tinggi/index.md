---
title: "Dua Elips dan Satu Persegi Panjang: Menggambar Tabung dengan TikZ"
date: 2026-11-09T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Tabung yang saya gambar di papan tulis selalu terlihat miring: elips atas dan bawah tidak sejajar, dan siswa bingung mana alas mana tutup. Di tulisan ini saya menggambar tabung dengan TikZ — dua elips, dua garis tegak, dan satu garis tinggi — supaya gambarnya rapi sebelum soal volumenya dibahas."
featuredImage: "featured-image.png"

tags: ["TikZ", "Tabung", "Bangun Ruang", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu saya mengajar volume tabung di kelas IX. Soalnya sederhana: sebuah tabung berjari-jari $7$ cm dan tinggi $10$ cm, berapa volumenya? Sebelum sampai ke angka, saya menggambar tabungnya dulu di papan tulis — dan di situlah masalahnya mulai. Elips atas saya lebih lebar daripada elips bawah, garis tegaknya miring ke dalam, dan seorang siswa di bangku tengah bertanya, "Pak, itu alasnya yang atas atau yang bawah?" Saya tertawa, tetapi di dalam hati saya tahu: kalau gambarnya saja membingungkan, bagaimana siswa bisa percaya pada rumus yang saya tulis di sebelahnya? Malam harinya saya menggambar ulang tabung itu dengan TikZ, dan tulisan ini adalah catatan caranya.

<!--more-->

## Tabung itu dua lingkaran dan satu persegi panjang

Sebelum menulis kode, saya selalu mengingatkan diri sendiri tentang bentuk tabung. Tabung tegak terdiri dari tiga bagian: alas berupa lingkaran, tutup berupa lingkaran yang sama besar dan sejajar dengan alas, serta selimut berupa persegi panjang yang digulung. Kalau dilihat dari depan, kedua lingkaran itu tidak tampak sebagai lingkaran lagi, melainkan sebagai elips yang pipih. Selimutnya tampak sebagai dua garis tegak yang menghubungkan ujung-ujung elips atas dan elips bawah. Jadi, menggambar tabung di TikZ sebenarnya hanya butuh tiga unsur: dua elips, dua garis tegak, dan satu keputusan — seberapa pipih elipsnya.

Saya memakai jari-jari $2$ cm untuk elips dan tinggi $4$ cm untuk tabungnya. Elips atas saya letakkan di titik $(0, 2)$ dan elips bawah di titik $(0, -2)$, keduanya dengan lebar $2$ dan tinggi $0{,}6$. Angka $0{,}6$ ini saya pilih karena cukup pipih untuk terlihat seperti lingkaran yang dilihat dari depan. Kalau elipsnya terlalu gemuk, tabungnya terlihat seperti mangkuk; kalau terlalu pipih, alas dan tutupnya hampir tidak terlihat.

## Elips atas utuh, elips bawah setengah

Inilah bagian yang paling sering salah digambar, termasuk oleh saya sendiri di papan tulis. Elips atas digambar utuh, karena seluruh tepinya terlihat dari depan. Elips bawah berbeda: hanya setengah bagian depannya yang terlihat, sedangkan setengah bagian belakangnya tersembunyi di dalam tabung. Bagian yang tersembunyi itu digambar dengan garis putus-putus — persis seperti rusuk balok yang tersembunyi, yang pernah saya bahas di tulisan tentang balok.

```latex
\begin{tikzpicture}[scale=1.0]
  % Elips atas: digambar utuh
  \draw[thick] (0, 2) ellipse (2 and 0.6);
  % Dua garis tegak selimut
  \draw[thick] (-2, 2) -- (-2, -2);
  \draw[thick] (2, 2) -- (2, -2);
  % Elips bawah, bagian belakang (tersembunyi): garis putus-putus
  \draw[thick, dashed] (2, -2) arc (0:180:2 and 0.6);
  % Elips bawah, bagian depan (terlihat): garis penuh
  \draw[thick] (-2, -2) arc (180:360:2 and 0.6);
\end{tikzpicture}
```

Perhatikan dua baris terakhir. Busur dari sudut $0$ sampai $180$ derajat menggambar setengah bagian atas elips bawah — bagian yang berada di dalam tabung, sehingga saya beri garis putus-putus. Busur dari $180$ sampai $360$ derajat menggambar setengah bagian bawah — bagian depan yang terlihat, sehingga garisnya penuh. Dua busur ini berawal dan berakhir di titik yang sama, yaitu $(-2, -2)$ dan $(2, -2)$, dan kedua titik itulah yang juga menjadi ujung garis tegak selimut. Kalau titik-titik ini tidak bertemu, gambarnya akan bocor di sudut, dan siswa yang teliti pasti menunjuknya.

## Menandai jari-jari dan tinggi

Tabung polos sudah cukup untuk mengenal bentuknya, tetapi untuk soal volume saya butuh label: jari-jari $r$ dan tinggi $t$. Jari-jari saya gambar sebagai garis dari pusat elips atas ke ujung kanannya, tepat di atas elips, supaya jelas bahwa $r$ adalah jari-jari lingkaran alas. Tinggi saya gambar sebagai garis putus-putus di tengah tabung, dari pusat elips atas ke pusat elips bawah, dengan label $t$ di sampingnya. Saya sengaja memakai garis putus-putus untuk tinggi, karena garis itu berada di dalam tabung dan tidak terlihat dari luar — sama seperti bagian belakang elips bawah.

```latex
\begin{tikzpicture}[scale=1.0]
  % Elips atas utuh
  \draw[thick] (0, 2) ellipse (2 and 0.6);
  % Dua garis tegak selimut
  \draw[thick] (-2, 2) -- (-2, -2);
  \draw[thick] (2, 2) -- (2, -2);
  % Elips bawah: belakang putus-putus, depan penuh
  \draw[thick, dashed] (2, -2) arc (0:180:2 and 0.6);
  \draw[thick] (-2, -2) arc (180:360:2 and 0.6);
  % Jari-jari: dari pusat elips atas ke ujung kanan
  \fill (0, 2) circle (0.06);
  \draw[thick] (0, 2) -- (2, 2);
  \node[above] at (1, 2) {$r$};
  % Tinggi: garis putus-putus di tengah tabung
  \draw[thick, dashed] (0, 2) -- (0, -2);
  \node[right] at (0.15, 0) {$t$};
\end{tikzpicture}
```

Titik kecil di pusat elips atas saya tambahkan supaya jelas dari mana garis $r$ berawal. Tanpa titik itu, garis jari-jari tampak melayang dan siswa bisa mengira $r$ diukur dari tepi elips, bukan dari pusatnya. Detail kecil seperti ini yang membedakan gambar yang sekadar jadi dengan gambar yang bisa dipakai mengajar.

## Tiga kesalahan yang paling sering saya lihat

Setelah beberapa kali menggambar tabung, saya mencatat tiga kesalahan yang selalu berulang. Pertama, elips atas dan bawah digambar dengan lebar yang berbeda. Akibatnya tabung terlihat miring, seperti kaleng yang penyok. Obatnya sederhana: pakai satu nilai yang sama untuk lebar kedua elips, dalam contoh saya $2$, dan jangan mengubahnya di tengah jalan. Kedua, garis tegak tidak menyinggung elips di titik terlebarnya. Garis yang ditarik terlalu ke dalam membuat ujung elips menjorok keluar seperti telinga; garis yang ditarik terlalu ke luar membuat selimut terlepas dari alasnya. Garis tegak harus berawal dan berakhir tepat di $(-2, 2)$, $(2, 2)$, $(-2, -2)$, dan $(2, -2)$ — titik-titik terlebar kedua elips. Ketiga, bagian belakang elips bawah digambar dengan garis penuh. Tabungnya memang tetap terlihat seperti tabung, tetapi siswa kehilangan petunjuk mana bagian yang tersembunyi, dan ketika nanti mereka menggambar balok atau prisma, mereka mengulang kesalahan yang sama: semua garis digambar penuh, semua rusuk dianggap terlihat.

## Satu soal untuk menutup gambarnya

Gambar yang rapi baru berguna kalau dipakai menghitung. Saya tutup pelajaran dengan satu soal yang angkanya saya pilih supaya hitungannya bersih: sebuah tabung berjari-jari $7$ cm dan tinggi $10$ cm. Berapa volumenya? Rumusnya $V = \pi r^2 t$, dan karena $r = 7$ kelipatan $7$, saya memakai $\pi = \frac{22}{7}$:

$$V = \frac{22}{7} \times 7^2 \times 10 = \frac{22}{7} \times 49 \times 10 = 22 \times 7 \times 10 = 1540 \text{ cm}^3$$

Saya meminta siswa memeriksa sendiri satu hal sebelum menulis jawaban akhir: apakah $7^2$ sama dengan $49$, dan apakah $49$ dibagi $7$ sama dengan $7$. Dua pemeriksaan kecil itu menyelamatkan mereka dari kesalahan yang paling sering terjadi pada soal ini, yaitu memakai diameter sebagai jari-jari dan lupa menguadratkan $r$. Gambar tabung yang sudah berlabel $r$ dan $t$ membantu di sini: siswa bisa menunjuk garis $r$ pada gambar dan memastikan bahwa angka $7$ yang mereka pakai memang jari-jari, bukan diameter.

Sejak memakai gambar TikZ ini, pertanyaan "Pak, alasnya yang mana?" tidak pernah muncul lagi. Gambar yang rapi ternyata bukan hiasan: ia membuat soal volume menjadi soal tentang angka, bukan soal menebak-nebak gambar. Dan bagi saya, itulah gunanya menggambar dengan teliti — supaya waktu di kelas habis untuk berpikir, bukan untuk membetulkan gambar.

> 📎 **Berkas TikZ lengkap:** [tabung-dua-elips.tex](tex/tabung-dua-elips.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
