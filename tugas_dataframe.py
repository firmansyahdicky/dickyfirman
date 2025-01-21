import pandas as pd

data = {
    "kode_provinsi": [32] * 5,
    "nama_provinsi": ["Jawa Barat"] * 5,
    "kode_kabupaten_kota": [3201, 3202, 3203, 3204, 3205],
    "nama_kabupaten_kota": ["Kabupaten Bandung", "Kabupaten Bekasi", "Kota Bandung", "Kota Bekasi", "Kabupaten Bogor"],
    "jumlah_produksi_sampah": [100, 200, 150, 180, 210],
    "satuan": ["ton/hari"] * 5,
    "tahun": ["2023"] * 5
}

df = pd.DataFrame(data)

total_per_tahun = {}
for index, row in df.iterrows():
    tahun = row["tahun"]
    produksi = row["jumlah_produksi_sampah"]
    if tahun in total_per_tahun:
        total_per_tahun[tahun] += produksi
    else:
        total_per_tahun[tahun] = produksi

print("Total produksi sampah per tahun:")
print(total_per_tahun)

total_per_kota = {}
for index, row in df.iterrows():
    kota = row["nama_kabupaten_kota"]
    tahun = row["tahun"]
    produksi = row["jumlah_produksi_sampah"]
    key = (kota, tahun)
    if key in total_per_kota:
        total_per_kota[key] += produksi
    else:
        total_per_kota[key] = produksi

print("\nTotal produksi sampah per Kota/Kabupaten per tahun:")
print(total_per_kota)