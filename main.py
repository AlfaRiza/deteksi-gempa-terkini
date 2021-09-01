"""
Aplikasi Deteksi Gempa
"""
from gempaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi Deteksi Gempa')
    result = ekstraksi_data()
    tampilkan_data(result)
