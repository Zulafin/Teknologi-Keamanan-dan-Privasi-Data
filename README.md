# Teknologi-Keamanan-dan-Privasi-Data

## Tugas 1
Membuat suatu aplikasi untuk implementasi simetrik kriptogtafi, yaitu Shift Chiper, Vigenere Chiper, Substitution Chiper, dan Transposition Chiper. Untuk aplikasi Shift Chiper menggunakan 2 digit terakhir NIM dan untuk Vigenere Chiper menggunakan 3 digit terakhir NIM.

## Penjelasan
### Shift Chiper
Kode program akan menampilkan sebuah GUI dengan tiga buah text entry box, dua buah label, dan dua buah button. User dapat memasukkan plaintext/ciphertext dan kunci (dalam bentuk integer) pada text entry box. Jika user memilih tombol "Encrypt", maka plaintext yang dimasukkan akan dienkripsi menggunakan shift cipher dengan kunci yang diberikan. Hasil enkripsi akan ditampilkan pada text entry box "Result". Jika user memilih tombol "Decrypt", maka ciphertext yang dimasukkan akan didekripsi menggunakan shift cipher dengan kunci yang diberikan. Hasil dekripsi akan ditampilkan pada text entry box "Result".
### Vigenere Chiper
Kode program akan menghasilkan GUI sederhana yang memiliki tiga input field (Plaintext, Key, dan Ciphertext) serta dua button untuk melakukan encrypt dan decrypt.
### Substitution Chiper
Dalam aplikasi ini, digunakan dictionary untuk menyimpan penggantian huruf pada Substitution Cipher. Kemudian, terdapat fungsi substitution_cipher untuk melakukan penggantian huruf berdasarkan dictionary tersebut. Aplikasi GUI ini memiliki dua entry field, yaitu untuk plainteks dan cipherteks, serta tombol "Encrypt" dan "Decrypt" untuk melakukan enkripsi dan deskripsi.
### Transposition Chiper
Pada method __init__, kita membuat label dan text box untuk input dan output, serta button untuk enkripsi dan dekripsi. Method __encrypt dan decrypt__, kita mengambil input dari text box, menghitung kunci (dalam hal ini, panjang teks dibagi 2), dan melakukan transpose dengan menggunakan method __transpose__. Method __transpose__, kita melakukan transpose dengan cara membangun list of string sepanjang kunci, lalu mengisi setiap string pada list tersebut dengan karakter-karakter dari teks input sesuai dengan aturan transpose.
