possible_row_names = [
	# 2020 -----
    'NUMUNE KODU:',
    'BÖLGE ADI:',
    'YER:',
    'GPS KOORDİNATLARI:',
    'TABLO:',
    'NUMUNE ALMA TARİHİ',
    'PARAMETRE', # This is kind of useless since we have 'NUMUNE ALMA TARİHİ' anyway.
    'Amonyak (mg/ L)',
    'Amonyum Azotu (mg/ L)',
    'Askıda Katı Madde (mg/ L)',
    'Biyokimyasal Oksijen İhtiyacı (mg/ L)',
    'Debi (m3/ sn)',
    'Elektriksel İletkenlik (µS/ cm)',
    'Fekal  Koliform  (CFU/ 100 mL)',
    'Fekal Koliform (CFU/ 100 mL)',
    'Fekal Streptekok (CFU/ 100 mL)',
    'Işık Geçirgenliği (M)',
    'Kimyasal Oksijen İhtiyacı (mg/ L)',
    'Klorofil-A (µg/ L)',
    'Koku (TON)',
    'Nitrat Azotu (mg/ L)',
    'Nitrit Azotu (mg/ L)',
    'O2 (%)',
    'Orta Fosfat (mg/ L)',
    'Renk (Pt-Co)',
    'Sıcaklık (0C)',
    'Toplam Azot (mg/ L)',
    'Toplam Fenol (mg/ L)',
    'Toplam Fosfor (mg/ L)',
    'Toplam Kjeldahl Azotu (mg/ L)',
    'Toplam Koliform  (CFU/ 100 mL)',
    'Toplam Pestisid (mg/ L)',
    'Tuzluluk (‰)',
    'Yağ-Gres (mg/ L)',
    'pH',
    'Çözünmüş Oksijen (mg/ L)',
    'İletkenlik (µS/ cm)',
    # 2018 -----
    'ÖÇKB Adı',
    'Yer',
    'GPS Koordinatları',
    'TVKGM Numune Kodu',
    'DOKAY Numune Kayıt Numarası',
    'Numune Alma Tarihi',
    'Parametre', # Useless, ignore.
    'Amonyak (mg/L)',
    'Amonyum Azotu (mg/L)',
    'Askıda Katı Madde (mg/L)',
    'Biyokimyasal Oksijen İhtiyacı (mg/L)',
    'Debi (m3/gün)',
    'Debi (m3/sn)',
    'Elektriksel İletkenlik (μs/cm)',
    'Fekal Koliform \n(CFU/ 100mL)',
    'Fekal Koliform (CFU/ 100mL)',
    'Fekal Koliform (CFU/100mL)',
    'FekalStreptekok \n(CFU/ 100mL)',
    'FekalStreptekok (CFU/ 100mL)',
    'Işık Geçirgenliği (m)',
    'Kimyasal Oksijen İhtiyacı (mg/L)',
    'Klorofil-a (μg/L)',
    'Koku (TON)',
    'Nitrat Azotu (mg/L)',
    'Nitrit Azotu (mg/L)',
    'O2 (%)',
    'Renk (Pt-Co)',
    'Sıcaklık (0C)',
    'Sıcaklık (oC)',
    'Sıcaklık(0C)',
    'Toplam Azot (mg/L)',
    'Toplam Azot (μg/L)',
    'Toplam Fenol (mg/L)',
    'Toplam Fosfor (mg/L)',
    'Toplam Fosfor (μg/L)',
    'Toplam Kjeldahl Azotu (mg/L)',
    'Toplam Koliform \n(CFU/ 100mL)',
    'Toplam Koliform (CFU/ 100mL)',
    'Toplam Koliform (CFU/100mL)',
    'Toplam Pestisit (mg/L)',
    'Tuzluluk (‰)',
    'Yağ-Gres (mg/L)',
    'pH',
    'Çözünmüş Oksijen (mg/L)',
    'İletkenlik (μs/cm)',
]

headers = {
	"numune" : ['NUMUNE KODU:', 'TVKGM Numune Kodu'],
	"bolge" : ['BÖLGE ADI:', 'ÖÇKB Adı'],
	"yer" : ['YER:', 'Yer'],
	"koord" : ['GPS KOORDİNATLARI:', 'GPS Koordinatları'],
	"tarih" : ['NUMUNE ALMA TARİHİ', 'Numune Alma Tarihi']
}

reading_types = [
    # 2020 -----
    'Amonyak (mg/ L)',
    'Amonyum Azotu (mg/ L)',
    'Askıda Katı Madde (mg/ L)',
    'Biyokimyasal Oksijen İhtiyacı (mg/ L)',
    'Debi (m3/ sn)',
    'Elektriksel İletkenlik (µS/ cm)',
    'Fekal  Koliform  (CFU/ 100 mL)',
    'Fekal Koliform (CFU/ 100 mL)',
    'Fekal Streptekok (CFU/ 100 mL)',
    'Işık Geçirgenliği (M)',
    'Kimyasal Oksijen İhtiyacı (mg/ L)',
    'Klorofil-A (µg/ L)',
    'Koku (TON)',
    'Nitrat Azotu (mg/ L)',
    'Nitrit Azotu (mg/ L)',
    'O2 (%)',
    'Orta Fosfat (mg/ L)',
    'Renk (Pt-Co)',
    'Sıcaklık (0C)',
    'Toplam Azot (mg/ L)',
    'Toplam Fenol (mg/ L)',
    'Toplam Fosfor (mg/ L)',
    'Toplam Kjeldahl Azotu (mg/ L)',
    'Toplam Koliform  (CFU/ 100 mL)',
    'Toplam Pestisid (mg/ L)',
    'Tuzluluk (‰)',
    'Yağ-Gres (mg/ L)',
    'pH',
    'Çözünmüş Oksijen (mg/ L)',
    'İletkenlik (µS/ cm)'
    # 2018 -----
    'Amonyak (mg/L)',
    'Amonyum Azotu (mg/L)',
    'Askıda Katı Madde (mg/L)',
    'Biyokimyasal Oksijen İhtiyacı (mg/L)',
    'Debi (m3/gün)',
    'Debi (m3/sn)',
    'Elektriksel İletkenlik (μs/cm)',
    'Fekal Koliform \n(CFU/ 100mL)',
    'Fekal Koliform (CFU/ 100mL)',
    'Fekal Koliform (CFU/100mL)',
    'FekalStreptekok \n(CFU/ 100mL)',
    'FekalStreptekok (CFU/ 100mL)',
    'Işık Geçirgenliği (m)',
    'Kimyasal Oksijen İhtiyacı (mg/L)',
    'Klorofil-a (μg/L)',
    'Koku (TON)',
    'Nitrat Azotu (mg/L)',
    'Nitrit Azotu (mg/L)',
    'O2 (%)',
    'Renk (Pt-Co)',
    'Sıcaklık (0C)',
    'Sıcaklık (oC)',
    'Sıcaklık(0C)',
    'Toplam Azot (mg/L)',
    'Toplam Azot (μg/L)',
    'Toplam Fenol (mg/L)',
    'Toplam Fosfor (mg/L)',
    'Toplam Fosfor (μg/L)',
    'Toplam Kjeldahl Azotu (mg/L)',
    'Toplam Koliform \n(CFU/ 100mL)',
    'Toplam Koliform (CFU/ 100mL)',
    'Toplam Koliform (CFU/100mL)',
    'Toplam Pestisit (mg/L)',
    'Tuzluluk (‰)',
    'Yağ-Gres (mg/L)',
    'pH',
    'Çözünmüş Oksijen (mg/L)',
    'İletkenlik (μs/cm)'
]

rightmost_cells = ['YSKY Ek-5 Tablo.2\n(Su Kalite Sınıfları)', 'DLS-4374', 'Y.S.K.Y.-Ek1', 'KAAY-EK IV', 'YSKY Ek-6 Tablo.9']
