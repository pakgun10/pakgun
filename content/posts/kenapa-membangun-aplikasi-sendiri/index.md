---
title: "Kenapa Saya Membangun Aplikasi Pembelajaran Sendiri, Bukan Cukup Pakai yang Ada"
date: 2026-10-21T09:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Banyak aplikasi pembelajaran siap pakai di luar sana. Namun dari kuis, CBT, sampai pemilih suara kelas — saya memilih membangun sendiri. Ini cerita alasan di balik portal GezyTech."
featuredImage: "featured-image.png"

tags: ["GezyTech", "Teknologi Pendidikan"]
categories: ["Teknologi Pendidikan"]

math:
  enable: true
---

Di internet tersedia ribuan aplikasi pembelajaran siap pakai. Kuis ada, LMS ada, aplikasi ujian berbasis komputer ada, bahkan tinggal daftar dan langsung jadi. Suhu kerasnya: kenapa seorang guru matematika di SMPN 1 Punggur ini rela begadang menulis kode demi membuat aplikasi yang orang lain sudah jual jadi?

<!--more-->

## Semua bermula dari soal sederhana

Pertanyaannya bukan "aplikasi apa yang bagus?", melainkan "aplikasi ini paham kaharkerja saya?". Dan hampir selalu jawabannya: tidak persis.

Contoh paling nyata: **kuis matematika**. Hampir semua platform kuis menyimpan jawaban matematika sebagai teks biasa. $2x + 3$ dianggap sama dengan $\frac{2x+3}{1}$, atau malah harus ditulis dengan format aneh yang harus dihafal siswa. Padahal di kelas, notasi matematika bukan pelengkap — ia adalah bahasanya. Saya ingin siswa mengetik jawaban yang terlihat seperti di buku, dan sistem mengertinya.

Kebutuhan-kebutuhan kecil seperti inilah yang akhirnya menumpuk menjadi keputusan besar.

## Apa saja yang akhirnya dibangun

Portal [GezyTech](https://gezytech.web.id/) tumbuh dari satu aplikasi menjadi keluarga aplikasi, masing-masing lahir dari kebutuhan nyata di kelas:

- **Aplikasi kuis** — menerima notasi matematika, bukan sekadar teks;
- **CBT (Computer-Based Test)** — untuk ulangan besar dan asesmen sumatif, dengan database sungguhan yang bisa menampung seluruh angkatan;
- **Pemilih suara / multivote** — untuk pemilihan ketua kelas dan voting kegiatan sekolah, karena pekerjaan rekap manual di kelas itu memakan waktu dan rawan salah;
- **Media matematika interaktif** — bidang koordinat, visualisasi, alat bantu mengajar yang menyala di proyektor;
- **Slide dan materi ajar** — yang bisa dibuka dari mana saja, tanpa flashdisk.

Tidak ada satu pun yang lahir karena "kayaknya keren kalau ada". Semua karena ada masalah yang harus selesai minggu itu juga.

## Keuntungan yang tidak saya duga di awal

**Pertama, aplikasi berubah secepat kebutuhan berubah.** Kurikulum bergeser, aturan asesmen berubah, kebijakan sekolah menuntut format baru — dengan aplikasi buatan sendiri, perubahan itu selesai dalam satu malam, bukan menunggu vendor atau menggelar tiket dukungan.

**Kedua, data tetap di tangan sekolah.** Nilai, jawaban, data siswa — semuanya tinggal di server yang saya kendalikan sendiri. Tidak ada pertanyaan "datanya disimpan di mana ya?", tidak ada kecemasan langganan berhenti dan data ikut hilang.

**Ketiga, saya jadi guru yang lebih paham pembelajarannya.** Ini yang paling tak terduga: membangun aplikasi soal memaksa saya mendefinisikan dengan presisi apa yang diuji, bagaimana penilaian dihitung, apa yang membuat pengecoh itu masuk akal. Kode menuntut kejelasan yang kadang bisa lolos di kepala kita. Banyak sekali pemahaman pedagogis saya yang justru terasah justru saat menerjemahkan pembelajaran menjadi logika program.

## Tentang biaya dan batas kemampuan

Saya guru, bukan insinyur perangkat lunak. Sebagian besar aplikasi di GezyTech dibangun dengan alat sederhana dan — sejak beberapa waktu ini — dibantu AI sebagai rekan kerja yang tidak kenal lelah: menuliskan kerangka kode, mencari bug, menyederhanakan hal yang rumit. Yang tidak bisa dilakukan AI adalah memutuskan *untuk apa* semuanya dibuat. Itu tetap pekerjaan guru: mengenal kelasnya, mengenal anak-anaknya, mengenal tujuannya.

Servernya pun bukan yang mewah — satu VPS kecil yang saya urus sendiri. Ternyata untuk kebutuhan satu sekolah, sederhana itu cukup.

## Untuk guru yang ingin memulai

Kalau Bapak/Ibu ingin mencoba membuat sendiri, pesan saya cuma tiga:

1. **Mulai dari masalah paling nyeri di kelas Anda** — bukan dari daftar fitur yang keren. Aplikasi pertama saya sangat kecil dan sederhana, dan itu tidak apa-apa.
2. **Manfaatkan AI dengan tuntas** — kebatan "harus bisa ngoding dulu" sudah tidak relevan lagi. Yang penting Anda tahu persis apa yang Anda mau dan bisa menilai hasilnya masuk akal atau tidak.
3. **Simpan semua di satu tempat** — kode di satu repo, data terstruktur, catatan perubahan teratur. Dua tahun kemudian Anda akan berterima kasih pada diri sendiri.

Portal GezyTech adalah bukti bahwa guru biasa — dengan niat, kesabaran, dan sedikit rasa penasaran — bisa membangun alat yang persis sesuai kebutuhan kelasnya. Bukan karena lebih pintar, tetapi karena yang paling mengenal masalah di kelas ya guru itu sendiri.

---

*Artikel ini pembuka seri cerita di balik GezyTech. Nanti saya tulis satu per satu: bagaimana CBT-nya dibangun, bagaimana kuisnya mengerti notasi matematika, dan hal-hal teknis lainnya. Nantikan di blog ini.*
