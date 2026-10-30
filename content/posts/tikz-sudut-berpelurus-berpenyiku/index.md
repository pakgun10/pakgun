---
title: "Dua Sudut yang Berpelurus di Satu Garis: Menggambar Sudut Berpelurus dan Berpenyiku dengan TikZ"
date: 2026-10-30T14:35:00+07:00
draft: false
authors: ["Gunanto"]
description: "Sudut berpelurus dan berpenyiku sering tertukar di kepala siswa. Cerita mengajarkan bedanya lewat gambar TikZ yang jujur pada garis lurus dan jumlah sudutnya."
featuredImage: "featured-image.png"

tags: ["TikZ", "Sudut", "Berpelurus", "Berpenyiku", "Geometri", "Bahan Ajar"]
categories: ["Matematika", "TikZ"]

math:
  enable: true
---

Kemarin di kelas VII saya memberikan soal yang kelihatannya sepele: satu garis lurus, satu sinar keluar dari titik di garis itu, dan sudut kecilnya $55^\circ$. Pertanyaannya cuma satu — berapakah sudut satunya? Soal seperti ini saya biasa gunakan sebagai pemanasan lima menit sebelum masuk materi baru.

Jawaban yang muncul di papan tulis para siswa terbagi dua kubu. Kubu pertama menulis $125^\circ$, kubu kedua menulis $35^\circ$. Dua-duanya percaya diri. Ketika saya tanya alasannya, kubu pertama bilang "karena jumlahnya 180, Pak", dan kubu kedua bilang "karena jumlahnya 90". Dua kelompok itu sama-sama tahu bahwa ada "jumlah yang tetap" — yang mereka tidak sepakat hanyalah angkanya 180 atau 90.

Di titik itulah saya sadar: masalahnya bukan mereka tidak hafal. Mereka hafal dua istilah itu, *berpelurus* dan *berpenyiku*, tapi keduanya tersimpan di kepala sebagai satu kantong yang sama, "sudut yang dijumlah jadi tertentu". Yang belum melekat adalah gambarannya.

<!--more-->

## Dua Kantong yang Tertukar

Coba perhatikan betapa mudahnya keduanya tertukar. Kata-katanya mirip — sama-sama diawali "ber-", sama-sama dua suku kata setelahnya. Rumusnya mirip — dua bilangan yang dijumlah. Bahkan soal-soalnya mirip — hampir selalu digambar sebagai satu garis lurus dengan satu sinar, bedanya hanya seberapa miring sinar itu.

Padahal kalau kita perhatikan sinarnya, perbedaannya terlihat mata. Dua sudut berpelurus duduk di atas **garis lurus** yang utuh: garisnya tidak patah, sinar hanya membelahnya menjadi dua bagian, dan jumlah keduanya harus tepat $180^\circ$ karena memang bentuk aslinya garis lurus. Sedangkan dua sudut berpenyiku tidak butuh garis lurus yang utuh — keduanya hanya berkumpul membentuk satu **sudut siku-siku**, dan jumlahnya $90^\circ$ karena itulah arti siku-siku itu sendiri.

{{< figure src="gambar-berpelurus-berpenyiku.png" caption="Kiri: dua sudut berpelurus di atas satu garis lurus (jumlah 180°). Kanan: dua sudut berpenyiku yang menyusun satu sudut siku-siku (jumlah 90°)." >}}

Nah, di gambar inilah saya ingin berhenti sejenak. Perhatikan sisi kanan: sinarnya saya buat miring $62^\circ$ — sengaja bukan $45^\circ$, supaya siswa tidak mengira sudut berpenyiku selalu harus tampak "setengah-setengah" yang simetris. $62^\circ$ dan $28^\circ$ sama-sama penyiku, sekalipun bentuknya asimetris dan matanya sempat protes "kok yang kecil banget, Pak?". Justru protes seperti itu tanda bahwa mereka sedang melihat, bukan sekadar menghafal.

## Menggambar yang Jujur dengan TikZ

Seperti kebiasaan saya belakangan, gambar ini saya buat dengan TikZ. Bukan sekadar gaya-gayaan — gambar yang asal dibuat di pengolah kata sering "berbohong": sudut yang tertulis $125^\circ$ digambar lebih kecil dari $90^\circ$, atau sinar yang tertulis miring $62^\circ$ digambar tegak lurus sempurna. Dengan TikZ, posisi sinar saya hitung langsung dari sudutnya, sehingga yang tertulis pasti yang tergambar.

Trik utamanya sederhana: posisi ujung sinar dihitung dengan fungsi trigonometri. Untuk sinar $55^\circ$ dengan panjang 3,4 cm dari titik sudut $(3,0)$:

```latex
\draw[thick,aksen] (3,0) -- (3+3.4*cos 55, 3.4*sin 55);
```

Koordinat `3+3.4*cos 55` dan `3.4*sin 55` dihitung TikZ sendiri, jadi sinar itu *harus* benar-benar miring $55^\circ$ — tidak ada ruang untuk tangan yang goyah. Busur penanda sudutnya pun mengikuti sudut yang sama:

```latex
\draw[aksen!70] (4.3,0) arc (0:55:1.3);
\draw[white!70] (3+1.6*cos 55,1.6*sin 55) arc (55:180:1.6);
```

Busur pertama menandai sudut $55^\circ$ dari garis horizontal, busur kedua meneruskan dari $55^\circ$ sampai $180^\circ$ — dan melihat kedua busur itu bersambung menjadi setengah lingkaran penuh di atas garis lurus, siswa *melihat* mengapa jumlahnya $180^\circ$, bukan sekadar diberi tahu.

Untuk kasus berpenyiku, logikanya sama; bedanya saya tidak menggambar garis yang tersambung penuh sampai ujung, dan saya pilih pasangan $62^\circ$ dan $28^\circ$ yang jumlahnya pas $90^\circ$.

Berikut kode lengkap untuk kedua gambar tersebut (versi utuh, siap kompilasi, ada di tautan berkas di akhir artikel):

```latex
\documentclass[tikz]{standalone}
\definecolor{bg}{HTML}{171D2B}
\definecolor{aksen}{HTML}{F7B538}
\begin{document}
\pagecolor{bg}
\begin{tikzpicture}[line cap=round,line join=round]
  % dua sudut berpelurus
  \draw[thick,white] (-0.5,0) -- (6.5,0);
  \draw[thick,aksen] (3,0) -- (3+3.4*cos 55, 3.4*sin 55);
  \draw[aksen!70] (4.3,0) arc (0:55:1.3);
  \draw[white!70] (3+1.6*cos 55,1.6*sin 55) arc (55:180:1.6);
  % dua sudut berpenyiku
  \draw[thick,white] (9,0) -- (14.5,0);
  \draw[thick,aksen] (11.5,0) -- (11.5+3.2*cos 62, 3.2*sin 62);
  \draw[aksen!70] (12.6,0) arc (0:62:1.1);
  \draw[white!70] (11.5+1.5*cos 62,1.5*sin 62) arc (62:180:1.5);
\end{tikzpicture}
\end{document}
```

## Dari Melihat ke Menalar

Setelah gambar itu saya tempel di layar, kelas berubah nadanya. Kubu yang tadi menjawab $35^\circ$ segera mengakui: "Oh, yang jumlahnya 90 itu kalau sinarnya sama garisnya bikin siku, Pak. Di soal ini tidak siku." Saya tidak perlu menegur siapa pun; gambarnya yang bekerja.

Tapi saya tidak berhenti di situ. Kesalahan klasik berikutnya menunggu: siswa lupa bahwa "berpelurus" tidak selalu dua sudut — bisa tiga. Garis lurus yang ditusuk dua sinar menghasilkan tiga sudut yang tetap harus berjumlah $180^\circ$. Kalau pemahaman siswa dibangun di atas *gambar garis lurus yang jujur*, perluasan ke tiga sudut itu terasa alami. Kalau dibangun di atas hafalan "dua sudut = 180", perluasan itu jadi jebakan baru.

Makanya di latihan lanjutan, saya sengaja memberi variasi: sudut berpelurus dengan tiga pecahan sudut, sudut berpenyiku yang salah satu sisinya vertikal ke atas, bahkan soal yang gambarnya sengaja tidak skala. Justru pada soal yang gambarnya tidak skala, siswa dipaksa kembali ke penalaran: jumlahnya tetap $180^\circ$ atau $90^\circ$ bukan karena terlihat, tapi karena definisinya.

## Penutup: Gambar Sebagai Guru Kedua

Saya makin yakin bahwa banyak miskonsepsi matematika di SMP sebenarnya miskonsepsi *visual*. Istilah sudah masuk, rumus sudah hafal, tapi gambar yang tersimpan di kepala salah — atau tidak pernah terbentuk sama sekali. Tugas kita sebagai guru bukan mengganti hafalan dengan hafalan baru, tapi memberi mata mereka gambar yang bisa dipercaya.

TikZ membantu saya jujur pada siswa: sudut yang tertulis $55^\circ$ benar-benar $55^\circ$, garis yang tertulis lurus benar-benar lurus, dan dua sudut yang tertulis berpenyiku benar-benar bertemu di siku. Ketika gambar dan angka tidak pernah saling menyangkal, siswa tinggal dengan satu pekerjaan yang paling penting: menalar.

> 📎 **Berkas TikZ lengkap:** [tikz-sudut-berpelurus-berpenyiku.tex](tex/tikz-sudut-berpelurus-berpenyiku.tex) — siap kompilasi (butuh paket `tikz`).
