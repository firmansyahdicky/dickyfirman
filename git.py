data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480,
        }
    }
}

for lokasi, data in data_panen.items():
    print(f"{lokasi} - {data['nama_lokasi']}: {data['hasil_panen']}")

jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung dari lokasi2: {jagung_lokasi2}")

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")

jumlah_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
jumlah_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print(f"Jumlah hasil panen padi per lokasi: {jumlah_padi}")
print(f"Jumlah hasil panen kedelai per lokasi: {jumlah_kedelai}")

for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")

with open("data_panen_output.txt", "w") as file:
    file.write("Seluruh data:\n")
    for lokasi, data in data_panen.items():
        file.write(f"{lokasi} - {data['nama_lokasi']}: {data['hasil_panen']}\n")
    file.write(f"\nJumlah hasil panen jagung dari lokasi2: {jagung_lokasi2}\n")
    file.write(f"Nama lokasi dari lokasi3: {nama_lokasi3}\n")
    file.write(f"\nJumlah hasil panen padi per lokasi: {jumlah_padi}\n")
    file.write(f"Jumlah hasil panen kedelai per lokasi: {jumlah_kedelai}\n")
