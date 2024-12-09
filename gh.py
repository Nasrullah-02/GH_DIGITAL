import qrcode

# URL yang ingin Anda masukkan ke dalam QR code
url = "https://nasrullah-02.github.io/GH/"

# Membuat QR code
qr = qrcode.QRCode(
    version=1,  # Ukuran QR code (1 adalah ukuran terkecil)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Tingkat koreksi kesalahan
    box_size=10,  # Ukuran setiap kotak dalam QR code
    border=4,  # Ukuran border
)

# Menambahkan data URL ke QR code
qr.add_data(url)
qr.make(fit=True)

# Membuat gambar dari QR code
img = qr.make_image(fill='black', back_color='white')

# Menyimpan gambar QR code
img.save("kode_qr.png")
