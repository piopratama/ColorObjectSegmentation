Usulan langkah
1. rgb->hsv(tugas 3 color space)
2. operasi range thressholding pada hsv (tugas 2 pointwise)
3. bitwise_and (tugas 2 pointwise)
4. erosi dan dilasi untuk menghilangkan noise, memisahkan objek yang menempel, atau menyatukan beberapa 
piksel yang memang membentuk suatu objek
5. Terakhir dengan memanfaatkan algoritma connected component untuk menghitung jumlah objek

Future Work :
1. metode ini masih perlu pengembangan yang lebih baik misalnya bagaimana cara untuk mengetahui
jumlah warna dalam gambar pada presepsi manusia secara otomatis tanpa secara eksplisit diprogram(tidak dengan manual if else).
Misalkan warna warna seperti hsv1(0, 5%, 50%), hsv2(3, 7%, 50%), hsv3(0, 100%, 50%),
bagi komputer maka hsv1 dan hsv2 mungkin dianggap berbeda, namun bagi manusia mungkin kedua warna tersebut
dikatakan sama yaitu merah gelap. Tujuannya agar tidak perlu lagi melakukan setting parameter batas
pada hsv untuk mengekstrak warna yang diinginkan, karena program akan tahu warna-warna apa saja yang ada menurut
presepsi manusia, dan menetapkan batasnya secara otomatis. 
(mungkin clustering dapat dipertimbangkan, tapi bagaimana menentukan nilai k secara otomatis ?)
2. perhitungan jumlah saat ini hanya melihat piksel yang terhubung dan tidak pada algoritma connected component,
jadi tidak memperhatikan apakah objek tersebut permen atau tidak(bahkan sebuah piksel yang terisolasi bisa saja dianggap permen), 
untuk itu perlu operasi lain untuk penghitungan objek yang lebih akurat misalnya dengan contour
untuk memperkirakan shape dari objek untuk mengetahui apakah objek tersebut dapat dikatakan permen atau tidak
3. sebuah objek mungkin saja memiliki hue yang berbeda pada setiap sisinya karena itu dibutuhkan metode tertentu
untuk mengetahui apakah piksel yang berbeda tersebut adalah bagian dari sebuah objek atau tidak

Untuk memudahkan pekerjaan maka digunakan Library
OpenCV.js : Image processing library, untuk memudahkan operasi pengolahan citra.
Jquery.js : Javascript library untuk memudahkan mengakses DOM
Bootstrap : User interface

Installasi
1. copy folder 1829101040
2. double click main.html atau drag and drop main.html pada browser

penggunaan
1. load gambar
2. atur parameter hsv, erosi, dilasi
3. jumlah objek akan langsung dihitung

untuk penggunaan program lebih jelas pada tutorial.mp4 di folder 1829101040

pada folder ini juga terdapat program dengan bahasa python namun memerlukan beberapa instalasi tambahan (python/readme.txt).