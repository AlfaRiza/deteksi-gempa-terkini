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
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        time = soup.find('span', 'waktu').string.split(', ')
        waktu = time[1]
        tanggal = time[0]

        result = soup.find('div', 'col-md-6 col-xs-6 gempabumi-detail no-padding')
        magnitudo = result.findChildren('li')[1].text
        kedalaman = result.findChildren('li')[2].text
        koordinat = result.findChildren('li')[3].text.split(' - ')
        print(koordinat)
        pusat = result.findChildren('li')[4].text
        dirasakan = result.findChildren('li')[5].text
        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['lokasi'] = {'LS': koordinat[0], 'BT': koordinat[1]}
        hasil['pusat'] = pusat
        hasil['dirasakan'] = dirasakan

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
    print(f'Kedalaman : {result["kedalaman"]}')
    print(f'lokasi : LS -> {result["lokasi"]["LS"]} BT ->{result["lokasi"]["BT"]}')
    print(f'pusat gempa : {result["pusat"]}')
    print(f'dirasakan : {result["dirasakan"]}')


if __name__ == '__main__':
    print('package gempa terkini')
