# IF2123 Aljabar Linier dan Geometri
Pengenalan wajah (Face Recognition) adalah teknologi biometrik yang bisa dipakai untuk mengidentifikasi wajah seseorang. Program pengenalan wajah melibatkan kumpulan citra wajah yang sudah disimpan pada database. Kumpulan citra tersebut akan digunakan dengan representasi matriks. Kemudian akan dihitung sebuah matriks Eigenface. Program pengenalan wajah dapat dibagi menjadi 2 tahap berbeda yaitu tahap training dan pencocokkan. Pada tahap training, akan diberikan kumpulan data set berupa citra wajah. Citra wajah tersebut akan dinormalisasi dari RGB ke Grayscale (matriks), hasil normalisasi akan digunakan dalam perhitungan eigenface. Seperti namanya, matriks eigenface menggunakan eigenvector dalam pembentukannya.

# Deployment

# Struktur Folder
Berikut ini adalah struktur folder dari project ini:

* Folder 'test' berisi test image dan dataset yang digunakan
* Folder 'doc' berisi laporan tugas ini
* Folder 'src' berisi source program.

# Teknologi
Pada project ini, teknologi yang digunakan adalah

* Python
* Numpy
* OS
* Tkinter

# Cara menggunakan

1. Pastikan sudah menginstall 'VSCode'
2. Clone repository dari git ke repository local
3. Buka folder hasil clone di 'VSCode'
4. Buka dan jalankan 'gui.py'
5. Setelah GUI berhasil dijalankan, klik icon folder pada textbox untuk meng-input file test image dan folder dataset
6. Klik tombol "Generate", lalu program akan melakukan proses pencocokkan
7. Setelah proses selesai, hasil gambar yang paling mendekati test image akan ditampilkan pada slot "Closest Result"

# Prosedur Pengenalan Wajah

1. 

# Catatan
