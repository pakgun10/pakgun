---
title: "Membangun Aplikasi Pembelajaran Sendiri: Cerita di Balik GezyTech"
date: 2026-10-21T09:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Aplikasi pembelajaran siap pakai banyak tersedia, tetapi saya memilih membangun sendiri — dari kuis, CBT, sampai pemilih suara kelas. Ini cerita alasan di balik portal GezyTech."
featuredImage: "featured-image.png"

tags: ["GezyTech", "Teknologi Pendidikan"]
categories: ["Teknologi Pendidikan"]

math:
  enable: true
---

Di internet tersedia ribuan aplikasi pembelajaran siap pakai. Kuis ada, LMS ada, aplikasi ujian berbasis komputer ada — tinggal daftar, langsung jadi. Lalu muncul pertanyaan yang sering saya dengar dari rekan-rekan guru: kenapa seorang guru matematika di SMPN 1 Punggur ini rela begadang menulis kode, demi membuat aplikasi yang orang lain sudah jadi membuatnya?

<!--more-->

## Semua bermula dari satu kegelisahan sederhana

Pertanyaan yang saya pegang sebenarnya bukan "aplikasi apa yang bagus?", melainkan "aplikasi ini paham cara kerja saya?". Dan hampir selalu jawabannya: belum persis.

Contoh paling nyata: **kuis matematika**. Hampir semua platform kuis menyimpan jawaban matematika sebagai teks biasa. $2x + 3$ dianggap sama dengan $\frac{2x+3}{1}$, atau malah siswa harus menulis dengan format aneh yang harus dihafal dulu. Padahal di kelas, notasi matematika bukan pelengkap — ia adalah bahasanya. Saya ingin siswa mengetik jawaban yang tampilannya seperti di buku, dan sistem mengertinya dengan benar.

Kebutuhan-kebutuhan kecil semacam ini diam-diam menumpuk, sampai akhirnya menjadi satu keputusan besar: ya sudah, buat sendiri.

## Apa saja yang akhirnya jadi

Portal [GezyTech](https://gezytech.web.id/) tumbuh dari satu aplikasi menjadi keluarga aplikasi. Masing-masing lahir dari kebutuhan nyata di kelas, bukan dari daftar keinginan:

- **Aplikasi kuis** — menerima notasi matematika, bukan sekadar teks;
- **CBT (Computer-Based Test)** — untuk ulangan besar dan asesmen sumatif, dengan database sungguhan yang sanggup menampung seluruh angkatan;
- **Pemilih suara / multivote** — untuk pemilihan ketua kelas dan voting kegiatan sekolah, karena rekap manual di kelas itu lama dan rawan salah hitung;
- **Media matematika interaktif** — bidang koordinat, visualisasi, alat bantu mengajar yang tampil bagus di proyektor;
- **Slide dan materi ajar** — yang bisa dibuka dari mana saja, tanpa harus bawa flashdisk.

Tidak ada satu pun yang lahir karena "kayaknya keren kalau ada". Semuanya karena ada masalah yang harus selesai minggu itu juga.

## Keuntungan yang tidak saya duga di awal

**Pertama, aplikasi berubah secepat kebutuhan berubah.** Kurikulum bergeser, aturan asesmen berubah, kebijakan sekolah menuntut format baru — dengan aplikasi buatan sendiri, perubahan itu selesai dalam satu malam. Tidak perlu menunggu vendor, tidak perlu mengirim tiket dukungan lalu menunggu balasan.

**Kedua, data tetap di tangan sekolah.** Nilai, jawaban, data siswa — semuanya tersimpan di server yang saya kendalikan sendiri. Tidak ada pertanyaan menggeliti "datanya disimpan di mana ya?", tidak ada kecemasan langganan berhenti lalu data ikut menghilang.

**Ketiga, saya justru jadi guru yang lebih paham pembelajarannya.** Ini yang paling tidak terduga. Membangun aplikasi soal memaksa saya mendefinisikan dengan presisi: apa yang diuji, bagaimana nilainya dihitung, apa yang membuat pengecoh itu masuk akal. Kode tidak menerima keraguan — ia menuntut kejelasan yang kadang bisa lolos begitu saja di kepala kita. Banyak pemahaman pedagogis saya yang justru terasah saat menerjemahkan pembelajaran menjadi logika program.

## Soal biaya dan batas kemampuan

Saya guru, bukan insinyur perangkat lunak — dan itu perlu dikatakan dari awal. Sebagian besar aplikasi di GezyTech dibangun dengan alat-alat sederhana, dan belakangan ini dibantu AI sebagai rekan kerja yang tidak kenal lewat: menuliskan kerangka kode, mencari bug, menyederhanakan bagian yang rumit. Tetapi yang tidak bisa dilakukan AI adalah memutuskan *untuk apa* semuanya dibuat. Itu tetap pekerjaan guru: mengenal kelasnya, mengenal anak-anaknya, mengenal tujuannya.

Servernya pun bukan yang mewah — sekadar satu VPS kecil yang saya urus sendiri. Ternyata untuk kebutuhan satu sekolah, sederhana itu cukup.

## Untuk guru yang ingin memulai

Kalau Bapak/Ibu ingin mencoba membuat sendiri, pesan saya cuma tiga:

1. **Mulai dari masalah paling menyiksa di kelas Anda** — bukan dari daftar fitur yang keren. Aplikasi pertama saya sangat kecil dan sederhana, dan itu tidak apa-apa; yang penting masalahnya selesai.
2. **Manfaatkan AI dengan tuntas** — anggapan "harus bisa ngoding dulu" sudah tidak relevan lagi. Yang penting Anda tahu persis apa yang Anda mau, dan bisa menilai hasilnya masuk akal atau tidak.
3. **Simpan semua di satu tempat** — kode di satu repo, data terstruktur, catatan perubahan rapi. Dua tahun kemudian, Anda akan berterima kasih pada diri sendiri yang dulu teliti.

Portal GezyTech adalah bukti bahwa guru biasa — dengan niat, kesabaran, dan sedikit rasa penasaran — bisa membangun alat yang persis sesuai kebutuhan kelasnya. Bukan karena kami lebih pintar, tetapi karena yang paling mengenal masalah di kelas memang gurunya sendiri.

---

*Artikel ini pembuka seri cerita di balik GezyTech. Nanti saya tulis satu per satu: bagaimana CBT-nya dibangun, bagaimana kuisnya bisa mengerti notasi matematika, dan hal-hal teknis lainnya. Pantau terus blog ini.*
