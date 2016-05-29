
# Dokumentasi Platform Akuisisi Data Sensor (DATACQ)
`Versi 1.0-beta`


# Pengembang: `Vicky Vernando Dasta`

Tentang:
-------------------

DATACQ merupakan platform pengumpul data sensor berbasis pada teknologi Arduino, Raspberry Pi, Python, Flask. Platform ini bertujuan untuk mengautomasi kerja pengumpulan data yang dihasilkan dari sensor dengan antar muka web yang bersifat multiplatform, sehingga dapat digunakan di semua perangkat, baik PC (personal computer), Laptop, Tablet, Smartphone. 

Instalasi:
--------------------

- a) Raspberry Pi 

-- unduh berkas https://downloads.raspberrypi.org/raspbian_latest

-- kemudian copy berkas image raspbian ke SD card berukuran minimal 2GiB menggunakan rufus/etc

-- boot raspberry pi kemudian masukkan credential default pi/raspberry

-- install dependensi: `sudo bash install.sh`

b) Arduino

pustaka arduino-json sudah dibundle kedalam pustaka datacq, untuk mengupload kode sumber:

`ino build && ino upload`


HOWTO 
------

- a) automatisasi dan background process

pada saat raspberry pi dijalankan, datacq otomatis akan langsung berjalan di background. Untuk melakukan pengecekan apakah proses datacq server dan pengumumpul data berjalan atau tidak:

sudo supervisorctl 

- status

- antar muka

1. Menu “Files”

Jelajah berkas CSV yang sudah digenerate oleh sistem. Pada bagian ini terdapat tombol “hapus” yang berfungsi untuk menghapus berkas junk. Kemudian tombol “unduh” berguna untuk mengunduh berkas CSV.

2. Indikator ukuran file

Indikator ukuran file menggunakan satuan KiB, satuan ini membulatkan 1024*1024 byte data dari berkas CSV.

3. Menu “Find”

Halaman ini berguna untuk mencari file dengan timestamp tertentu
Masukkan kata kunci pada kotak pencarian, kemudian tekan tombol “cari berkas”.



Copyright & License
------------------

  * Copyright 2016, Vicky Vernando Dasta
  * License: MIT
