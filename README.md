# Blog Gunanto

Blog pribadi **Gunanto, S.Pd.** — guru Matematika SMPN 1 Punggur, Lampung Tengah.
Dibangun dengan **Hugo + tema DoIt** (stack yang sama dengan blog referensi aantriono.com):
tulisan ditulis sebagai file Markdown, Hugo mengubahnya menjadi situs statis (HTML/CSS/JS murni, tanpa database), lalu di-online-kan lewat **Cloudflare Pages**.

- Tema terang/gelap, pencarian Fuse.js, rumus matematika KaTeX, daftar isi otomatis — semua bawaan tema DoIt (lisensi MIT).
- Alamat situs: `https://pakgun.gezytech.web.id/` (diatur di `config/_default/hugo.toml`, tetap — diatur di `config/_default/hugo.toml`).

## Struktur folder

| Folder | Isi |
|---|---|
| `content/posts/` | Semua artikel. Satu artikel = satu folder berisi `index.md` + `featured-image.png` |
| `content/about/` | Halaman "Tentang Saya" |
| `config/_default/` | Pengaturan situs: `params.toml` (identitas, penulis, footer), `menu.toml` (menu atas), `hugo.toml` (judul & alamat situs) |
| `themes/DoIt/` | Tema DoIt (sudah ditanam di repo ini, tidak perlu diunduh lagi) |
| `assets/images/` & `static/` | Foto profil (avatar) dan favicon |
| `public/` | Hasil build — **tidak perlu di-commit**, dibuat otomatis oleh Cloudflare Pages |

## Menulis artikel baru

1. Buat folder baru di `content/posts/`, namanya pakai huruf kecil dan tanda hubung, contoh: `content/posts/cara-membuat-soal/`
2. Di dalamnya buat file `index.md`:

```markdown
---
title: "Judul Artikel"
date: 2026-10-21T07:00:00+07:00
draft: false
authors: ["Gunanto"]
description: "Ringkasan satu kalimat untuk Google dan pratinjau."
featuredImage: "featured-image.png"

tags: ["LaTeX"]
categories: ["Matematika"]

math:
  enable: true
---

Paragraf pembuka artikel.

<!--more-->

Isi artikel selanjutnya...
```

3. Taruh gambar sampul bernama `featured-image.png` (ukuran ideal 1200×630) di folder yang sama.
4. Tanggal `date` jangan di masa depan — artikel bertanggal masa depan tidak diterbitkan Hugo.
5. Commit dan push ke GitHub → Cloudflare Pages otomatis menerbitkannya.

## Build di komputer sendiri (opsional)

Butuh Hugo versi **extended** ≥ 0.122 (blog ini diuji dengan 0.168.0):

```bash
hugo server          # pratinjau lokal di http://localhost:1313
hugo --gc --minify   # build final ke folder public/
```

## Deploy ke Cloudflare Pages

Panduan lengkap langkah demi langkah ada di [DEPLOY.md](DEPLOY.md).
Ringkasnya: buat repo GitHub dari folder ini → di dashboard Cloudflare pilih
**Workers & Pages → Create → Pages → Connect to Git** → pilih repo →
framework preset **Hugo**, build command `hugo --gc --minify`, output `public`,
environment variable `HUGO_VERSION = 0.168.0` → Deploy. Setelah itu setiap
push ke GitHub langsung online otomatis.

## Catatan

- Komentar (Utterances) sudah disiapkan di konfigurasi tetapi **belum aktif** — aktifkan setelah ada repo GitHub khusus komentar, caranya di `config/_default/params.toml` pada bagian `[page.comment.utterances]`.
- Kode verifikasi Google Search Console masih kosong (`[verification] google` di `params.toml`) — isi setelah situs online dan didaftarkan ke Search Console.
