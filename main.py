"""
Aplikasi Deteksi Gempa
"""


def ekstraksi_data():
    """
    Tanggal : 01 September 2021,
    Waktu : 14:50:35 WIB
    Magnitudo : 3.6
    Kedalaman : 5 km
    Lokasi : 3.97 LS - 122.47 BT
    Pusat gempa : berada di darat 0.5 km Tenggara Puuwatu, Kota Kendari
    Dirasakan : (Skala MMI): III-IV Kendari
    """
    hasil = dict()
    hasil['tanggal'] = '01 September 2021'
    hasil['waktu'] = '14:50:35 WIB'
    hasil['magnitudo'] = 5
    hasil['lokasi'] = {'LS': 3.97, 'BT': 122.47}
    hasil['pusat'] = 'berada di darat 0.5 km Tenggara Puuwatu, Kota Kendari'
    hasil['dirasakan'] = '(Skala MMI): III-IV Kendari'

    return hasil


def tampilkan_data(result):
    print("Gempa terakhir berdasarkan BMKG")
    print(f'Tanggal : {result["tanggal"]}')
    print(f'Waktu : {result["waktu"]}')
    print(f'Magnitudo : {result["magnitudo"]} km')
    print(f'lokasi : LS -> {result["lokasi"]["LS"]} BT ->{result["lokasi"]["BT"]}')
    print(f'pusat gempa : {result["pusat"]}')
    print(f'dirasakan : {result["dirasakan"]}')


if __name__ == '__main__':
    print('Aplikasi Deteksi Gempa')
    result = ekstraksi_data()
    tampilkan_data(result)
