---
title: "Sudut Siku-Siku yang Selalu Muncul: Teorema Thales dengan TikZ"
date: 2026-11-15T19:30:00+07:00
draft: false
authors: ["Gunanto"]
description: "Sebuah percobaan kecil dengan jangka dan benang di kelas berakhir dengan penemuan yang mengejutkan siswa: sudut yang menghadap diameter selalu siku-siku. Di artikel ini saya mengajak Bapak/Ibu menggambar teorema Thales dengan TikZ, gambar demi gambar."
featuredImage: "featured-image.png"
tags: ["TikZ", "Geometri", "Lingkaran", "Sudut Keliling"]
categories: ["Matematika"]
math:
  enable: true
---

Ada satu momen di kelas yang tidak pernah saya bosankan: momen ketika siswa menemukan sendiri sesuatu yang sebenarnya sudah mereka "hafal" bertahun-tahun. Persisnya seperti itu yang terjadi beberapa waktu lalu, ketika kelas VIII saya sedang menyusuri materi lingkaran. Kita sedang bicara tentang sudut keliling, dan saya melempar satu pertanyaan sederhana yang jawabannya justru membuat seisi kelas berbisik: "Lho, kok bisa?"

Sebelum sampai ke TikZ-nya, izinkan saya bercerita dulu bagaimana pertanyaan itu muncul. Karena menurut pengalaman saya, teorema yang ditemukan siswa sendiri akan tinggal jauh lebih lama daripada teorema yang dibacakan dari buku.

<!--more-->

## Pertanyaan yang Muncul dari Seutas Benang

Hari itu saya membawa benang, paku push, dan papan korbek ke kelas. Di papan korbek itu saya tusukkan satu paku sebagai titik pusat, lalu satu paku lagi di tepi lingkaran yang terbentuk benang. Dua titik saja. Kemudian saya minta dua siswa maju: satu memegang paku ketiga yang boleh digeser-geser di sepanjang tepi lingkaran, dan tugasnya sederhana — tali benang kedua dihubungkan dari dua paku tepi ke paku yang ia pegang, membentuk segitiga.

"Perhatikan sudut di paku yang kamu pegang," kata saya. "Geser pelan-pelan, dan katakan kalau sudut itu terasa berubah."

Rani, siswa yang memegang paku itu, menggerakkan tangannya pelan-pelan di sepanjang tepi lingkaran. Lalu ia berhenti. "Pak, di sini sudutnya seperti siku-siku," katanya ragu-ragu. Saya menyuruhnya geser lagi, ke kiri, ke kanan, ke bawah. Dan setiap kali paku ketiga itu berhenti di mana saja di tepi lingkaran — asalkan tidak di antara dua paku pertama — sudut di paku itu kembali terlihat siku-siku.

"Setiap kali, Pak," ujar Rani, matanya mulai berbinar. "Kok bisa sama terus?"

Di titik itu, saya tidak buru-buru menjawab. Saya justru menuliskan di papan tulis apa yang baru saja kelasnya temukan: *kalau satu sisi segitiga adalah diameter lingkaran, dan titik ketiga berada di lingkaran, maka sudut yang menghadap diameter selalu $90^\circ$*. Nama teoremanya: Teorema Thales. Tetapi nama itu bisa ditulis belakangan — yang penting sore itu, penemuan itu milik Rani dan teman-temannya, bukan milik buku.

## Kenapa Ini Penting untuk Digambar dengan Jujur

Masalahnya, teorema yang sering digambar asal-asalan justru teorema seperti ini. Saya sering melihat lembar kerja atau slide yang menggambar segitiga di dalam lingkaran dengan titik ketiga hampir berimpit dengan ujung diameter — sehingga sudut yang seharusnya siku-siku tampak lancip kecil. Siswa yang jeli akan terkecoh: gambar mengatakan satu hal, teorema mengatakan hal lain. Dan seperti tulisan saya sebelumnya tentang bangun datar, saya percaya gambar pada soal harus jujur: kalau teorema mengatakan siku-siku, gambarnya harus benar-benar terlihat siku-siku.

[[diagram-thales.png]]
*Dua titik berbeda di lingkaran, C dan D, keduanya membentuk sudut $90^\circ$ yang menghadap diameter AB.*

Berikut gambar yang biasa saya pakai di lembar kerja. Ada satu lingkaran dengan pusat $O$, diameter $AB$, dan dua titik berbeda di lingkaran — $C$ di atas dan $D$ di bawah. Kedua segitiga $ABC$ dan $ABD$ sama-sama memiliki sudut $90^\circ$ yang menghadap diameter yang sama.

## Kode TikZ-nya

Inilah kode yang menghasilkan gambar di atas. Bagian yang paling sering saya perhatikan adalah kotak siku di titik $C$: saya tidak menggambar persegi kecil dengan koordinat hard-coded, melainkan menghitungnya dari kaki segitiga itu sendiri dengan library `calc`, sehingga kotaknya selalu tegak lurus terhadap kedua sisi, apa pun bentuk lingkarannya.

```latex
\coordinate (O) at (0,0);
\coordinate (A) at (-1.6,0);
\coordinate (B) at (1.6,0);
\coordinate (C) at (110:1.6);
\coordinate (D) at (250:1.6);

\draw[thick, white!60] (O) circle (1.6);
\draw[very thick, acc] (A) -- (B);        % diameter
\draw[very thick, white] (A) -- (C) -- (B);
\draw[thick, sec] (A) -- (D) -- (B);

% kotak siku di C, mengikuti arah kaki segitiga
\coordinate (P) at ($(C)!0.10!(A)$);
\coordinate (Q) at ($(C)!0.10!(B)$);
\coordinate (R) at ($(P)+(Q)-(C)$);
\draw[acc, thick] (P) -- (R) -- (Q);
```

Trik kecil di baris `($(P)+(Q)-(C)$)` adalah cara TikZ menghitung sudut paralelogram: titik $R$ diperoleh dengan "menambahkan arah $C \to P$ dan arah $C \to Q$". Hasilnya, empat titik $C$, $P$, $R$, $Q$ membentuk persegi panjang kecil yang secara otomatis menandai sudut siku di $C$. Saya menemukan pola ini setelah beberapa kali gagal dengan cara manual — dan sejak itu saya selalu memakainya untuk menandai sudut siku di gambar soal geometri.

Sesuatu yang juga saya senangi dari kode ini: koordinat $C$ dan $D$ ditulis dalam notasi kutub `(110:1.6)` dan `(250:1.6)`. Keduanya berjarak sama dari pusat (di lingkaran), dan asalnya $110^\circ$ serta $250^\circ$ — selisihnya $180^\circ$, artinya $C$, $O$, dan $D$ segaris. Dua titik itu berhadapan di lingkaran, dan keduanya tetap "menyaksikan" diameter dengan sudut yang sama: $90^\circ$.

## Menghubungkan dengan Sudut Pusat

Bapak/Ibu mungkin ingat tulisan saya sebelumnya tentang sudut pusat dan sudut keliling. Teorema Thales sebenarnya kasus khusus yang indah dari teorema itu: sudut pusat yang menghadap diameter adalah $180^\circ$, dan sudut keliling selalu setengah dari sudut pusat yang menghadap busur yang sama. Maka:

$$\angle ACB = \frac{1}{2} \times 180^\circ = 90^\circ$$

Saya senang sekali ketika siswa bisa melihat sendiri alur ini. Di kelas, kami membuktikannya dengan menggambar garis bantu $OC$, sehingga terbentuk dua segitiga sama kaki ($OC = OA = OB$, semua jari-jari). Kalau $\alpha$ adalah sudut di $A$, maka sudut di $O$ pada segitiga kecil itu juga $\alpha$, sehingga sudut pusat segmen itu $180^\circ - 2\alpha$. Perhitungan yang sama untuk segmen sebelahnya, lalu kedua sudut pusat dijumlahkan menjadi $180^\circ$. Dari situ diperoleh $\alpha + \beta = 90^\circ$, dan karena $\alpha + \beta$ persis sudut di $C$...

...sudut di $C$ memang $90^\circ$. Kita sampai di sana tanpa sekali pun "percaya" gambar, tanpa mengukur dengan busur derajat. Aljabar sederhana dan jari-jari yang sama panjang — itu saja.

## Kegunaannya di Soal

Setelah teorema ini ditemukan dan dibuktikan, soal-soal berikutnya terasa lebih hidup. Contoh soal yang saya suka: "Sebuah segitiga siku-siku memiliki sisi miring 13 cm. Salah satu kaki sisi siku-sikunya 5 cm. Kalau segitiga itu diletakkan di dalam setengah lingkaran, berapa radius lingkaran itu?" Siswa yang paham Thales akan langsung berpikir: sisi miring segitiga siku-siku *adalah* diameter lingkaran yang melaluinya — jadi radiusnya $\frac{13}{2} = 6{,}5$ cm. Pythagoras bahkan tidak diperlukan untuk menjawab pertanyaan radius, karena sisi miring sudah diketahui.

Soal seperti ini mengajarkan sesuatu yang lebih dalam daripada rumus: bahwa bangun-bangun geometri saling berhubungan. Segitiga siku-siku dan lingkaran bukan dua bab yang terpisah di buku — mereka bertemu di satu titik yang sama, tepat di sudut siku itu.

## Penutup: Gambar yang Setia pada Teorema

Sore itu, setelah Rani dan kelasnya menemukan teorema Thales dengan benang dan paku, saya pulang dan menghabiskan waktu menulis kode TikZ untuk gambar yang mereka lihat di papan korbek. Saya ingin semua lembar kerja berikutnya punya gambar yang tidak mengkhianati temuan mereka: sudut yang benar-benar siku, titik yang benar-benar di lingkaran, label yang tidak menyesatkan.

Karena pada akhirnya, menggambar geometri dengan TikZ bukan sekadar kerjaan teknis. Ini bentuk rasa hormat saya kepada proses berpikir siswa. Mereka sudah bekerja keras menemukan pola; tugas saya memastikan gambar yang saya berikan tidak merusak temuan itu.

> 📎 **Berkas TikZ lengkap:** [tikz-teorema-thales-diameter.tex](tex/tikz-teorema-thales-diameter.tex) — siap kompilasi (butuh paket `tikz` dan `amsmath`).
