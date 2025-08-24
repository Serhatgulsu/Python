import oracledb
import pandas as pd

conn = oracledb.connect(user="TARIFE", password="9K0m6m8X",
                host="10.0.31.160", port=1521, service_name="pdbq1.quicksigorta.local")
cursor = conn.cursor()

csv_dosyasi = "ANLIKHASAR.csv"  
df = pd.read_csv(csv_dosyasi,sep=(';'))

df.columns = ['Dosya_Kısım_No','Rucu_Oranı','Ihbar_Tutar','Net_Maliyet']

tablo_adi = "TARIFE.ANLIKHASAR"  # Oracle tablo adını belirtin

"""Tabloyu silip sadece csv içindekiler yüklemek istersen bu commenti açmalısın
cursor.execute(f"TRUNCATE TABLE {tablo_adi}")
conn.commit()
"""


sorgu_tablo_olustur = f"""
CREATE TABLE {tablo_adi} (
    {', '.join([f'{col} VARCHAR2(4000)' for col in df.columns])}
)
"""

try:
    cursor.execute(sorgu_tablo_olustur)
    print(f"Tablo '{tablo_adi}' başarıyla oluşturuldu.")
except oracledb.DatabaseError as e:
    print(f"Tablo zaten var veya başka bir hata: {e}")


sorgu_insert = f"""
INSERT INTO {tablo_adi} ({', '.join(df.columns)})
VALUES ({', '.join([':' + str(i + 1) for i in range(len(df.columns))])})
"""

veriler = [tuple(row) for row in df.itertuples(index=False, name=None)]

try:
    cursor.executemany(sorgu_insert, veriler)
    conn.commit()
    print(f"{len(veriler)} kayıt başarıyla '{tablo_adi}' tablosuna eklendi.")
except oracledb.DatabaseError as e:
    print(f"Veri ekleme hatası: {e}")

cursor.close()
conn.close()
