import requests
from bs4 import BeautifulSoup


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

    try:
        content = requests.get('https://bmkg.go.id/')
    except:
        return None
    if content.status_code == 200 :
        soup = BeautifulSoup(content)
        print()
        hasil = dict()
        hasil['tanggal'] = '01 September 2021'
        hasil['waktu'] = '14:50:35 WIB'
        hasil['magnitudo'] = 5
        hasil['lokasi'] = {'LS': 3.97, 'BT': 122.47}
        hasil['pusat'] = 'berada di darat 0.5 km Tenggara Puuwatu, Kota Kendari'
        hasil['dirasakan'] = '(Skala MMI): III-IV Kendari'

        return hasil
    else:
        None


def tampilkan_data(result):
    if result is None:
        print("Data tidak ada")
        return
    print("Gempa terakhir berdasarkan BMKG")
    print(f'Tanggal : {result["tanggal"]}')
    print(f'Waktu : {result["waktu"]}')
    print(f'Magnitudo : {result["magnitudo"]} km')
    print(f'lokasi : LS -> {result["lokasi"]["LS"]} BT ->{result["lokasi"]["BT"]}')
    print(f'pusat gempa : {result["pusat"]}')
    print(f'dirasakan : {result["dirasakan"]}')

if __name__ == '__main__':
    print('package gempa terkini')