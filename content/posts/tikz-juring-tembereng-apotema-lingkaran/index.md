---
title: "Juring, Tembereng, dan Apotema: Tiga Bagian Lingkaran yang Sering Tertukar"
date: 2026-10-26T12:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Siswa saya menyebut satu daerah arsiran lingkaran dengan tiga nama sekaligus: juring, tembereng, dan apotema. Di tulisan ini saya menggambar ketiganya dengan TikZ — juring sebagai potongan dari pusat, tembereng sebagai daerah antara tali busur dan busur, dan apotema sebagai jarak tegak lurus dari pusat ke tali busur — lengkap dengan angka yang bisa dihitung."
featuredImage: "featured-image.png"

tags: ["TikZ", "Lingkaran", "Juring", "Tembereng", "Apotema", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Di kelas VIII, saat bab lingkaran, saya menggambar satu lingkaran di papan tulis, menarik dua jari-jari dari pusatnya, lalu menambahkan sebuah tali busur. Saya mengarsir satu daerah di dalam lingkaran itu dan bertanya, "Daerah yang diarsir ini namanya apa?" Seorang siswa menjawab yakin, "Juring, Pak." Yang lain berkata, "Tembereng." Yang ketiga menambahkan, "Apotema, Pak, kan garisnya dari tengah." Tiga nama untuk satu arsiran, dan ketiganya diucapkan dengan keyakinan yang sama.

Jawaban itu membuat saya berhenti sejenak. Mereka bukan tidak menghafal; mereka menghafal tiga istilah yang bunyinya mirip, untuk tiga benda yang letaknya memang berdekatan di dalam satu lingkaran yang sama. Di papan tulis saya, arsiran itu tidak punya batas yang tegas: apakah ia dibatasi dua jari-jari, atau satu tali busur dan satu busur, atau malah sebuah garis dari pusat? Maka malam harinya saya menggambar ulang lingkaran itu dengan TikZ, dengan satu aturan: setiap bagian harus punya batas dan warnanya sendiri. Tulisan ini adalah catatan cara membuatnya.

<!--more-->

## Kenapa tiga bagian ini mudah tertukar

Ketiga bagian itu tinggal di wilayah yang sama: di dalam lingkaran, di sekitar satu busur yang sama. Juring dibatasi oleh dua jari-jari dan busur di antara keduanya, seperti potongan piza yang titiknya ada di pusat. Tembereng dibatasi oleh satu tali busur dan busur di hadapannya, seperti potongan pinggir piza yang sudah terpotong dari titik pusatnya. Apotema bahkan bukan daerah sama sekali: ia adalah ruas garis, jarak terpendek dari pusat lingkaran ke tali busur, yang selalu tegak lurus terhadap tali busur itu.

Kalau ketiganya digambar sekaligus tanpa warna dan tanpa penanda, siswa hanya melihat satu lingkaran penuh garis dan arsiran, lalu menebak nama dari bunyinya. Karena itu, sebelum menyebut nama, saya mengajak siswa membaca batasnya dulu: apakah daerah itu menyentuh pusat lingkaran atau tidak, dan apakah yang ditunjuk itu daerah atau garis.

## Juring: potongan yang titiknya di pusat

Juring adalah daerah yang dibatasi dua jari-jari dan busur di antara keduanya. Ciri yang paling mudah diingat: juring selalu menyentuh pusat lingkaran, karena kedua jari-jarinya bertemu di sana. Ambil lingkaran berjari-jari $3$ cm dan sudut pusat $60^\circ$. Luas juringnya adalah bagian dari luas lingkaran yang sebanding dengan sudutnya: $L = \frac{60^\circ}{360^\circ} \times \pi \times 3^2 = \frac{1}{6} \times 9\pi = 1{,}5\pi \approx 4{,}71$ cm$^2$.

Saya meletakkan pusat di $O = (0, 0)$, satu jari-jari mendatar ke $A = (3, 0)$, dan jari-jari kedua membentuk sudut $60^\circ$ ke $B = (1{,}5; 2{,}6)$:

```latex
\coordinate (O) at (0,0);
\coordinate (A) at (3,0);
\coordinate (B) at (1.5,2.6); % sudut 60 derajat dari OA
\fill[orange!30] (O) -- (A) arc (0:60:3) -- cycle;
\draw[thick] (O) -- (A);
\draw[thick] (O) -- (B);
\draw[thick] (A) arc (0:60:3);
```

Perintah `arc (0:60:3)` adalah kuncinya: busur digambar dari sudut $0^\circ$ sampai $60^\circ$ dengan jari-jari $3$, sehingga busur itu tepat menghubungkan ujung kedua jari-jari. Karena arsiran oranye itu menyentuh titik $O$, siswa langsung melihat: inilah potongan yang titiknya di pusat.

## Tembereng: daerah antara tali busur dan busur

Tembereng adalah daerah yang dibatasi satu tali busur dan busur di hadapannya. Ciri yang membedakannya dari juring: tembereng tidak menyentuh pusat lingkaran sama sekali. Ia adalah "sisa" juring setelah segitiga yang dibentuk dua jari-jari dan tali busur itu diambil.

Ambil lingkaran yang sama, berjari-jari $3$ cm, tetapi kini sudut pusatnya $120^\circ$, dari $30^\circ$ sampai $150^\circ$. Luas juringnya $\frac{120^\circ}{360^\circ} \times \pi \times 3^2 = 3\pi \approx 9{,}42$ cm$^2$. Segitiga yang dibentuk pusat dan tali busurnya luasnya $\frac{1}{2} \times 3 \times 3 \times \sin 120^\circ \approx 3{,}90$ cm$^2$. Maka luas temberengnya kira-kira $9{,}42 - 3{,}90 = 5{,}52$ cm$^2$.

Di TikZ, tembereng digambar dengan mengisi daerah antara busur dan tali busurnya. Tali busur menghubungkan $A = (2{,}6; 1{,}5)$ dan $B = (-2{,}6; 1{,}5)$, dan busur $120^\circ$ melengkung di atasnya:

```latex
\coordinate (A) at (2.6,1.5);
\coordinate (B) at (-2.6,1.5);
\fill[blue!20] (A) arc (30:150:3) -- cycle;
\draw[thick] (A) -- (B); % tali busur
\draw[thick] (A) arc (30:150:3);
```

Perintah `arc (30:150:3)` menggambar busur dari $A$ ke $B$ melewati atas, lalu `-- cycle` menutup daerah itu dengan garis lurus kembali ke $A$, dan garis lurus itulah tali busurnya. Arsiran biru itu tidak menyentuh pusat sama sekali, dan justru di situlah letak pelajarannya: kalau arsiran tidak menyentuh pusat, ia bukan juring.

## Apotema: garis tegak lurus dari pusat ke tali busur

Apotema adalah ruas garis dari pusat lingkaran yang tegak lurus terhadap tali busur. Ia bukan daerah, dan karena itu tidak pernah diarsir; ia digambar sebagai garis, lengkap dengan tanda siku di tempat ia bertemu tali busur. Apotema selalu membagi tali busur menjadi dua sama panjang, sehingga ia membentuk segitiga siku-siku bersama jari-jari dan setengah tali busur.

Contoh yang paling enak dihitung memakai tripel Pythagoras $3$-$4$-$5$. Ambil lingkaran berjari-jari $5$ cm dan tali busur sepanjang $8$ cm. Setengah tali busurnya $4$ cm, jari-jarinya $5$ cm, maka apotemanya $\sqrt{5^2 - 4^2} = \sqrt{25 - 16} = 3$ cm. Angka yang bulat, dan siswa bisa memeriksanya sendiri tanpa kalkulator.

Di TikZ saya meletakkan pusat di $O = (0, 0)$ dan tali busur mendatar pada $y = 3$, dari $A = (-4, 3)$ ke $B = (4, 3)$. Apotemanya adalah ruas dari $O$ ke titik tengah tali busur, $M = (0, 3)$, dan tanda siku kecil di $M$ menandai tegak lurusnya:

```latex
\coordinate (O) at (0,0);
\coordinate (A) at (-4,3);
\coordinate (B) at (4,3);
\coordinate (M) at (0,3); % titik tengah tali busur
\draw[thick] (O) -- (A);
\draw[thick] (A) -- (B);
\draw[red, thick] (O) -- (M); % apotema
\draw[red, thick] (M) ++(-0.3,0) -- ++(0,-0.3) -- ++(0.3,0); % tanda siku
\node[left] at (O) {$O$};
\node[above] at (M) {$M$};
```

Garis merah dari pusat ke tengah tali busur, dengan tanda siku di ujungnya, adalah gambar apotema yang tidak mungkin tertukar dengan arsiran juring atau tembereng. Dan karena panjangnya $3$ cm pada contoh ini, siswa bisa langsung mengaitkannya dengan hitungan Pythagoras yang baru saja mereka pelajari.

## Satu lingkaran, tiga warna, tiga pertanyaan

Di kelas, saya kini memproyeksikan satu lingkaran dengan tiga penanda berbeda: juring oranye yang menyentuh pusat, tembereng biru yang tidak menyentuh pusat, dan apotema merah yang berupa garis tegak lurus dengan tanda sikunya. Lalu saya mengajukan tiga pertanyaan tanpa menyebut nama apa pun: apakah daerah ini menyentuh pusat, apakah yang ditunjuk ini daerah atau garis, dan apakah garis ini tegak lurus terhadap tali busur? Begitu jawabannya terbaca dari gambar, namanya mengikuti dengan sendirinya.

Berkas TikZ lengkap ketiga gambar di atas bisa diunduh di bawah ini. Silakan ubah jari-jari dan sudut pusatnya dan lihat bagaimana luasnya ikut berubah.

> 📎 **Berkas TikZ lengkap:** [juring-tembereng-apotema.tex](tex/juring-tembereng-apotema.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
