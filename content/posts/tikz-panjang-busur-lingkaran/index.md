---
title: "Satu Busur, Satu Sudut Pusat: Menggambar Panjang Busur Lingkaran dengan TikZ"
date: 2026-11-09T20:01:00+07:00
draft: false
authors: ["Gunanto"]
description: "Panjang busur lingkaran ternyata sebanding dengan sudut pusatnya: seperempat lingkaran berarti seperempat keliling. Di tulisan ini saya menggambar busur 90 derajat berjari-jari 7 cm dengan TikZ — dan hasilnya 11 cm, tanpa penggaris lengkung sama sekali."
featuredImage: "featured-image.png"

tags: ["TikZ", "Lingkaran", "Panjang Busur", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Pekan lalu di kelas VIII, saya menggambar sebuah lingkaran di papan tulis, menandai dua titik $A$ dan $B$ pada kelilingnya, lalu bertanya, "Berapa panjang lengkung dari $A$ ke $B$ ini?" Seorang murid mengangkat penggarisnya dan mencoba menempelkannya ke lengkungan itu. Penggarisnya lurus, lengkungnya tidak mau lurus — ia menyerah sambil tertawa. Murid lain menebak 7 cm, karena jari-jarinya 7 cm, seolah-olah panjang busur sama dengan jari-jari. Dua jawaban itu menunjukkan hal yang sama: busur adalah benda yang belum pernah mereka ukur dengan cara yang benar. Malam harinya saya menggambar ulang gambar itu dengan TikZ, supaya besok pagi murid saya melihat sendiri bahwa panjang busur tidak perlu diukur dengan penggaris lengkung — cukup dihitung dari sudut pusatnya.

<!--more-->

## Panjang busur sebanding dengan sudut pusat

Busur adalah bagian dari keliling lingkaran. Kalau sudut pusatnya satu putaran penuh, 360 derajat, busurnya adalah seluruh keliling: $2\pi r$. Kalau sudut pusatnya hanya sebagian, busurnya pun sebagian itu juga. Itulah seluruh idenya, dan rumusnya mengikuti langsung:

$$ \text{panjang busur} = \frac{\theta}{360^{\circ}} \times 2\pi r $$

dengan $\theta$ sudut pusat dalam derajat dan $r$ jari-jari lingkaran.

Contoh pertama saya memakai sudut yang paling ramah: 90 derajat, seperempat putaran, dengan jari-jari 7 cm. Keliling penuh lingkaran itu adalah $2 \times \frac{22}{7} \times 7 = 44$ cm, dan seperempatnya adalah 11 cm. Hitungan lengkapnya:

$$ \text{busur } AB = \frac{90^{\circ}}{360^{\circ}} \times 2 \times \frac{22}{7} \times 7 = \frac{1}{4} \times 44 = 11 \text{ cm} $$

Saya sengaja memilih jari-jari 7 cm supaya $\pi$ bisa diganti $\frac{22}{7}$ dan angka 7-nya saling menghapus — murid cukup melihat bahwa seperempat lingkaran berarti seperempat keliling, tanpa berhadapan dengan desimal panjang. Angka itu mudah dicek: empat busur seperti itu menutup satu lingkaran penuh, $4 \times 11 = 44$ cm, persis kelilingnya.

## Menggambar busur 90 derajat di TikZ

Gambar pertama saya sederhana saja: satu lingkaran, dua jari-jari, dan busur yang ditebalkan dengan warna emas. Saya meletakkan pusat $O$ di $(0,0)$, titik $A$ di $(3,0)$, dan titik $B$ di $(0,3)$. Jarak $OA$ dan $OB$ sama-sama 3 satuan gambar — mewakili jari-jari 7 cm pada soal; skalanya tidak penting, yang penting sudutnya 90 derajat.

Perintah kuncinya adalah `arc`: `(A) arc (0:90:3)` berarti mulai dari titik $A$, gambar busur berjari-jari 3 dari sudut 0 derajat sampai 90 derajat, diukur dari pusat lingkaran — jadi busur itu persis mengikuti kelilingnya. Lingkaran penuhnya saya gambar tipis-tipis, lalu busur $AB$ saya gambar ulang tebal berwarna emas, supaya mata langsung tahu bagian mana yang dibicarakan. Juring $OAB$ saya beri arsiran tipis warna yang sama, supaya sudut pusat dan busurnya terlihat sebagai satu paket.

Satu detail kecil: tanda siku-siku di dekat pusat. Sudut 90 derajat saya tandai dengan kotak kecil di titik $O$, bukan busur sudut biasa, supaya murid langsung membacanya tanpa perlu membaca label angka.

```latex
\begin{tikzpicture}[scale=1.0, font=\large]
  % Pusat O, titik A di sudut 0 derajat, B di sudut 90 derajat
  \coordinate (O) at (0, 0);
  \coordinate (A) at (3, 0);
  \coordinate (B) at (0, 3);

  % Lingkaran penuh (tipis) dan juring OAB (arsiran tipis)
  \draw[thin] (O) circle (3);
  \fill[accent, opacity=0.15] (O) -- (A) arc (0:90:3) -- cycle;

  % Dua jari-jari OA dan OB
  \draw[thick] (O) -- (A);
  \draw[thick] (O) -- (B);
  % Busur AB: garis tebal berwarna emas
  \draw[very thick, accent] (A) arc (0:90:3);

  % Tanda siku-siku di pusat O
  \draw (0.5, 0) -- (0.5, 0.5) -- (0, 0.5);

  % Nama titik dan label
  \node[below right] at (O) {$O$};
  \node[below] at (A) {$A$};
  \node[left] at (B) {$B$};
  \node[below] at (1.5, 0) {$r$};
  \node at (0.85, 0.85) {$90^{\circ}$};
  \node[accent] at (2.55, 2.55) {busur $AB$};
\end{tikzpicture}
```

Label "busur $AB$" saya letakkan di arah 45 derajat, di luar lingkaran — tepat di tengah busur, tanpa menutupi garisnya. Kalau diletakkan di dalam juring, ia akan bertabrakan dengan arsiran dan angka sudutnya.

## Busur 120 derajat dan angka yang tetap rapi

Gambar kedua memakai sudut 120 derajat dan jari-jari 21 cm, supaya murid melihat rumusnya bekerja untuk sudut yang bukan seperempat lingkaran. Titik $A$ tetap di $(3,0)$, tetapi titik $B$ sekarang di arah 120 derajat: $(-1{,}5; 2{,}598)$ — hasil cosinus dan sinus 120 derajat dikali 3, saya tulis langsung sebagai koordinat supaya pembaca berkas TikZ saya tidak perlu menghitung ulang.

Hitungannya tetap rapi karena 21 adalah kelipatan 7:

$$ \text{busur } AB = \frac{120^{\circ}}{360^{\circ}} \times 2 \times \frac{22}{7} \times 21 = \frac{1}{3} \times 132 = 44 \text{ cm} $$

Yang saya tekankan di kelas adalah pola pemilihannya: jari-jari kelipatan 7 membuat $\pi = \frac{22}{7}$ bekerja bersih, dan sudut yang membagi 360 dengan rapi — 90, 120, 60, 180 — membuat pecahannya sederhana. Bukan karena soal yang bagus harus memakai angka cantik, melainkan karena di contoh pertama murid harus melihat polanya, bukan berjuang dengan kalkulator. Angka yang berantakan boleh datang kemudian, setelah polanya tertanam.

## Tiga kesalahan yang paling sering saya lihat

Kesalahan pertama: memakai diameter sebagai jari-jari. Murid melihat angka 14 cm pada soal, langsung memasukkannya sebagai $r$, padahal itu diameter. Hasilnya dua kali lipat dari yang benar. Saya selalu meminta mereka menulis dulu "$r = \dots$" sebelum menyentuh rumus, dan memeriksa apakah angka itu jarak pusat ke keliling, bukan dari satu sisi ke sisi lain.

Kesalahan kedua: lupa membagi dengan 360. Murid mengalikan sudut dengan $2\pi r$ begitu saja, tanpa pecahan $\frac{\theta}{360^{\circ}}$. Hasilnya bisa ratusan sentimeter untuk busur yang jelas hanya sebagian kecil lingkaran. Obatnya sederhana: tanyakan "busur ini lebih panjang atau lebih pendek dari keliling penuh?" Kalau lebih panjang, pasti ada yang salah.

Kesalahan ketiga: memakai $\pi = 3{,}14$ untuk jari-jari kelipatan 7. Bukan salah secara matematika — hanya kurang rapi, dan pembulatan di tengah jalan bisa menggeser jawaban akhir. Aturan praktis saya: jari-jari kelipatan 7, pakai $\frac{22}{7}$; kalau bukan, pakai $3{,}14$. Bukan hukum alam, hanya cara menjaga angka tetap bersahabat.

## Satu soal untuk dibawa pulang

Sebuah lingkaran berjari-jari 21 cm. Berapa panjang busur yang sudut pusatnya 60 derajat? Kerjakan dengan $\pi = \frac{22}{7}$, dan sebelum menghitung, tebak dulu: lebih pendek dari 44 cm contoh sebelumnya, atau lebih panjang? Jawabannya 22 cm — seperenam dari keliling 132 cm — karena sudutnya hanya setengah sudut contoh kedua, dengan jari-jari yang sama.

Gambar busur yang baik tidak menggantikan rumus, tetapi membuat rumus itu punya wajah. Begitu murid melihat busur emas itu menempel pada keliling dan sudut pusat yang mengaturnya, pecahan $\frac{\theta}{360^{\circ}}$ berhenti menjadi simbol asing — ia menjadi sesuatu yang mereka lihat: sebagian dari satu putaran penuh.

> 📎 **Berkas TikZ lengkap:** [panjang-busur-lingkaran.tex](tex/panjang-busur-lingkaran.tex) — dokumen siap kompilasi (butuh paket `tikz`). Silakan ganti angka-angkanya untuk dokumen Anda sendiri.
