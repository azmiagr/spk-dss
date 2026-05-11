# spk-dss

SPK DSS adalah project Python untuk membangun sistem pendukung keputusan rekomendasi laptop. Project ini memakai SQLAlchemy sebagai ORM, Alembic untuk database migration, MariaDB sebagai database, dan Flask sebagai dependency web framework.

## Tech Stack

- Python 3.9+
- Flask
- SQLAlchemy
- Alembic
- MariaDB
- PyMySQL
- python-dotenv

## Struktur Folder

```txt
application/
```

Folder untuk layer application/use case. Nantinya cocok dipakai untuk service yang mengatur alur bisnis aplikasi.

```txt
domain/
```

Folder untuk domain logic dan entity murni. Saat ini berisi entity katalog laptop.

```txt
infrastructure/
```

Folder untuk detail teknis aplikasi, seperti koneksi database dan model ORM.

```txt
infrastructure/database/
```

Berisi konfigurasi database:

- `base.py`: deklarasi `Base` SQLAlchemy.
- `config.py`: membaca `.env` dan membuat database URL.
- `session.py`: membuat SQLAlchemy engine dan session.
- `models/`: semua model tabel database.

```txt
alembic/
```

Folder migration Alembic. File migration ada di `alembic/versions/`.

```txt
main.py
```

Entry point aplikasi. Saat ini masih kosong dan bisa dikembangkan sesuai kebutuhan aplikasi.

## Cara Setup Project

Clone repository:

```bash
git clone <repository-url>
cd spk-dss
```

Buat virtual environment:

```bash
python3 -m venv venv
```

Aktifkan virtual environment:

```bash
source venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

## Setup Environment

Buat file `.env` di root project:

```bash
cp .env.example .env
```

Kalau `.env.example` belum ada, buat `.env` manual dengan isi berikut:

```env
DB_CONNECTION=mariadb
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=spk-dss
DB_USERNAME=root
DB_PASSWORD=your_database_password
```

Sesuaikan `DB_USERNAME` dan `DB_PASSWORD` dengan user MariaDB lokal masing-masing.

Catatan: karena nama database `spk-dss` memakai tanda minus, beberapa command MariaDB perlu memakai backtick. Kalau ingin lebih simpel, kamu bisa memakai nama database `spk_dss` dan menyesuaikan `DB_DATABASE`.

## Setup Database MariaDB

Pastikan MariaDB sudah berjalan, lalu buat database:

```bash
mariadb -u root -p -e "CREATE DATABASE IF NOT EXISTS \`spk-dss\` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

Kalau memakai nama database `spk_dss`, command-nya bisa lebih sederhana:

```bash
mariadb -u root -p -e "CREATE DATABASE IF NOT EXISTS spk_dss CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

## Menjalankan Migration

Cek status Alembic:

```bash
alembic current
```

Jalankan migration terbaru:

```bash
alembic upgrade head
```

Cek tabel yang sudah dibuat:

```bash
mariadb -u root -p -e "USE \`spk-dss\`; SHOW TABLES;"
```

## Menjalankan Aplikasi

Pastikan virtual environment aktif:

```bash
source venv/bin/activate
```

Jalankan aplikasi:

```bash
python main.py
```

Aplikasi akan berjalan di:

```txt
http://127.0.0.1:5000
```

Endpoint yang bisa dicoba:

```txt
GET /
GET /health
GET /db-check
```

`/db-check` dipakai untuk memastikan aplikasi bisa terhubung ke MariaDB sesuai konfigurasi `.env`.

## Membuat Migration Baru

Setiap kali model SQLAlchemy berubah, buat revision baru:

```bash
alembic revision --autogenerate -m "describe changes"
```

Sebelum menjalankan migration, buka file baru di `alembic/versions/` dan pastikan isi `upgrade()` dan `downgrade()` sudah masuk akal.

Setelah itu jalankan:

```bash
alembic upgrade head
```

Pola penting:

```bash
alembic revision --autogenerate -m "message"
alembic upgrade head
```

Jangan membuat revision baru lagi sebelum database berada di revision terbaru, karena Alembic bisa menampilkan error:

```txt
Target database is not up to date.
```

## Troubleshooting

Kalau muncul error:

```txt
Can't load plugin: sqlalchemy.dialects:driver
```

Pastikan `alembic.ini` tidak lagi memakai URL default:

```ini
sqlalchemy.url = driver://user:pass@localhost/dbname
```

Kalau muncul error:

```txt
Access denied for user
```

Periksa kembali `DB_USERNAME` dan `DB_PASSWORD` di `.env`, lalu pastikan user tersebut punya akses ke database.

Kalau `revision --autogenerate` membuat migration yang berisi `drop_table()` padahal seharusnya membuat tabel, pastikan `alembic/env.py` meng-import semua model:

```python
from infrastructure.database.base import Base
from infrastructure.database.config import get_database_url
import infrastructure.database.models
```

## File Yang Tidak Masuk Git

Folder dan file berikut tidak perlu di-commit:

```txt
venv/
.env
__pycache__/
*.pyc
```

Dependency project tetap dicatat di `requirements.txt`, bukan dengan meng-commit folder `venv/`.
