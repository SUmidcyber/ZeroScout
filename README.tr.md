<div align="center">

# 🦅 ZeroScout
### Otonom Yerel & Bulut Tehdit Avcısı

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Win%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge)](https://github.com/yourusername/zeroscout)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-red?style=for-the-badge)](https://github.com/yourusername/zeroscout)

<p align="center">
  <b>"Sadece dosya taramayın. Savaş alanını görselleştirin."</b>
</p>

[🇺🇸 İngilizce Dökümantasyon İçin Tıklayın (Read in English)](README.md)

</div>

---

## 🚀 ZeroScout Nedir?

**ZeroScout**, Olay Müdahale Uzmanları (DFIR), SOC Analistleri ve Zararlı Yazılım Araştırmacıları için tasarlanmış yeni nesil bir tehdit avcılığı çatısıdır.

"Kara Kutu" (Black Box) gibi davranan geleneksel antivirüs tarayıcılarının aksine, ZeroScout bir **Siber Savunma Karargahı** görevi görür. Saldırı yüzeyini canlı bir **Savaş Odası'nda** görselleştirir, genetik kod analizi (ImpHash/SSDeep) kullanarak arkasındaki **APT Grubunu** tanımlar ve otomatik olarak **YARA & SIGMA** savunma kuralları üretir.

Aşağıdaki şekilde **Hibrit Mimari** ile çalışır:
1.  **Yerel Avcı (Çevrimdışı Mod):** İnternet erişimi olmadan, gelişmiş sezgisel yöntemler, entropi analizi ve Windows Defender entegrasyonu ile 0. gün tehditlerini tespit eder.
2.  **Bulut Güçlü (Çevrimiçi Mod):** Yüksek performanslı **ZeroScout Bulut Motoru** ile kusursuz entegrasyon sağlayarak askeri düzeyde sandbox analizi sunar.

---

## ⚡ Temel Yetenekler

### 🌍 1. Canlı Savaş Odası Görselleştirmesi
ZeroScout, ikil (binary) dosyalardan C2 (Komuta Kontrol) IP'lerini sıyırır ve ağ trafiğini doğrudan terminalinizde canlı bir **ASCII Dünya Haritasında** görselleştirir.
> *Saldırının nereden geldiğini anlık olarak görün.*

### 🧬 2. Genetik Atıf (DNA Analizi)
Yeni zararlı yazılım varyantı mı? ZeroScout, **Kod DNA'sını (ImpHash)** ve TTP davranışlarını analiz ederek dosyanın arkasındaki aktörü tanımlar.
> *"Bu dosya bilinmiyor, ancak DNA'sı %92 güvenle **Lazarus Grubu** ile eşleşiyor."*

### 🛡️ 3. Otonom Savunma Mimarı
Manuel tespit kuralları yazmayı bırakın. ZeroScout anında konuşlandırılabilir savunma kodları üretir:
* **YARA Kuralları:** Uç nokta taraması için.
* **SIGMA Kuralları:** SIEM (Olay Yönetimi) korelasyonu için.

### 🔍 4. Toplu Av Modu
Tüm bir dizini (örn: İndirilenler klasörü, USB Sürücü) saniyeler içinde tarayın. ZeroScout gürültüyü filtreler ve yalnızca belirli nedenlerle (örn: "Yüksek Entropi", "Proses Enjeksiyonu") yüksek riskli eserleri vurgular.

---

## 📸 İstihbarat Paneli (Demo)

ZeroScout, birden çok istihbarat akışını birleştiren kapsamlı, etkileşimli bir terminal paneli sağlar.

### 🎥 Canlı Savaş Odası Akışı (Video/GIF Demo Önerilir)
Panelin dinamik yapısı nedeniyle, bu özelliğin README'nizde **video veya GIF** kullanılarak sergilenmesi şiddetle tavsiye edilir.

> *Örnek Video:* [ZeroScout Canlı Savaş Odasını Aksiyonda İzle](assets/zeroscout_demo.gif)

### 🧬 Genetik Atıf Özeti
```plaintext
╭──────────────────────────────────── 🧬 GENETİK ATIF ─────────────────────────────────────╮
│ AKTÖR: [Yüksek Riskli Tehdit Aktörü]                                                    │
│ GÜVEN ORANI: 92% [██████████████████░]                                                  │
│ Analiz: Kod DNA'sı (ImpHash) ve TTP davranışları bilinen APT28 profilleriyle eşleşiyor. │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
````

-----

## 📦 Kurulum

Bu projeyi bir Python paketi olarak kurmak, tüm bağımlılıkları otomatik olarak yükler ve CLI aracını kullanıma hazır hale getirir.

```bash
# 1. Depoyu klonlayın
git clone https://github.com/SUmidcyber/ZeroScout.git
cd ZeroScout

# 2. Bağımlılıkları yükleyin
# Bu komut, ZeroScout'u sisteminizde bir komut olarak erişilebilir kılar.
pip install .

# Veya sadece geliştirme ve test için:
# pip install -r requirements.txt 

# 3. Avlanmaya hazır!
python -m zeroscout.cli scan "zararli_yazilim.exe"
```

-----

## 🎮 Kullanım Kılavuzu

### 1\. Derin Analiz (Sıfır Gün Avcılığı)

Savaş Odasını açmak ve savunma kurallarını oluşturmak için tek bir dosyayı analiz edin.

```bash
python -m zeroscout.cli scan "C:\Kullanicilar\Admin\Masaustu\supheli.exe"
```

### 2\. Toplu Avcılık (Dizin Taraması)

Binlerce dosya arasındaki gizli tehditleri hızla bulmak için bir klasörü tarayın.

```bash
python -m zeroscout.cli scan "C:\Windows\System32"
```

### 3\. Bulut Motorunu Bağlama (Opsiyonel - API Anahtarı)

ZeroScout Bulut Motoru'nu kullanmak için **`ZEROSCOUT_API_KEY`** ortam değişkenini ayarlamanız gerekir. Anahtar bulunamazsa, sistem otomatik olarak **Yerel Avcı Moduna** geçer.

```bash
# Windows (PowerShell)
$env:ZEROSCOUT_API_KEY="api_anahtariniz_buraya"

# Linux / Mac
export ZEROSCOUT_API_KEY="api_anahtariniz_buraya"
```

-----

## 🏗️ Teknik Mimari

| Bileşen | Teknoloji | Amaç |
| :--- | :--- | :--- |
| **Çekirdek Motor** | Python 3 | Ana mantık ve CLI (Komut Satırı) yönetimi. |
| **Görsel Arayüz** | Rich Kütüphanesi | Panel tarzı terminal arayüzü. |
| **Statik Analiz** | Pefile & Math | Entropi hesaplama, Başlık analizi, ImpHash. |
| **İmzalar** | YARA & Regex | Dizi (string), IP adresleri ve desenlerin tanımlanması. |
| **Bulut Köprüsü** | REST API | Sandbox Motoruna bağlantı. |

-----

## 📜 Yasal Uyarı

**ZeroScout sadece eğitim ve savunma amaçlıdır.** Bu aracın herhangi bir yanlış kullanımından yazarlar sorumlu değildir. Zararlı yazılımları her zaman izole edilmiş bir ortamda (Sanal Makine) analiz ediniz.

-----


**Geliştirici: Umid Mammadov**

*ZeroScout Teknolojileri*

