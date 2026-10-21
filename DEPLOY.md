# Panduan Deploy — GitHub + Cloudflare Pages

Ikuti urut dari atas. Bagian A dikerjakan sekali saja; setelah itu blog
online otomatis setiap ada push baru ke GitHub.

## Bagian A — Taruh kode di GitHub

1. Buka https://github.com/new (login sebagai **pakgun10**).
2. Isi **Repository name**, misalnya `blog-gunanto`. Pilih **Public**. Jangan centang "Add a README". Klik **Create repository**.
3. Di komputer, dari folder proyek ini jalankan:

```bash
git remote add origin https://github.com/pakgun10/blog-gunanto.git
git push -u origin main
```

   (Folder ini sudah berupa repo git lokal dengan commit pertama, tinggal push.
   Bila nama repo berbeda, sesuaikan alamat `origin` di atas.)

## Bagian B — Hubungkan ke Cloudflare Pages

1. Buka https://dash.cloudflare.com → login akun Cloudflare Bapak.
2. Menu kiri: **Workers & Pages** → tombol **Create** → tab **Pages** → **Connect to Git**.
3. Pilih akun GitHub **pakgun10**, lalu pilih repo `blog-gunanto`. Klik **Begin setup**.
4. Isi pengaturan build persis seperti ini:

   | Pengaturan | Isi |
   |---|---|
   | Project name | `blog-gunanto` (akan jadi alamat `blog-gunanto.pages.dev`) |
   | Production branch | `main` |
   | Framework preset | **Hugo** |
   | Build command | `hugo --gc --minify` |
   | Build output directory | `public` |
   | Root directory | *(kosongkan)* |

5. Masih di layar yang sama, buka **Environment variables** → tambahkan:

   | Nama | Nilai |
   |---|---|
   | `HUGO_VERSION` | `0.168.0` |

6. Klik **Save and Deploy**. Tunggu ±1 menit sampai muncul tulisan sukses.
   Blog langsung bisa dibuka di `https://blog-gunanto.pages.dev`.

## Bagian C — Pasang domain sendiri (blog.gezytech.web.id)

Lewati bagian ini bila cukup memakai alamat `pages.dev`.

1. Di Cloudflare, buka project Pages tadi → tab **Custom domains** → **Set up a custom domain**.
2. Ketik `blog.gezytech.web.id` → **Continue** → **Activate domain**.
   Karena domain `gezytech.web.id` sudah dikelola Cloudflare, DNS-nya dibuat otomatis.
3. Ganti `baseURL` di `config/_default/hugo.toml` bila alamat final berbeda dari `https://blog.gezytech.web.id/`, lalu commit + push.

## Setelah online

- **Menulis artikel baru:** tambah folder di `content/posts/` (lihat README.md), commit, push — selesai, tidak ada langkah deploy manual.
- **Cek status deploy:** dashboard Cloudflare → project → tab **Deployments**.
- **Gagal build?** Penyebab tersering: variabel `HUGO_VERSION` belum dipasang, atau tanggal artikel ada di masa depan.
