# 📦 Stok Takip Uygulaması

Bu proje, yerel bir işletmenin veya kişisel envanterin kolayca yönetilebilmesi için geliştirilmiş, **Python**, **Tkinter** ve **SQLite** tabanlı bir masaüstü stok takip otomasyonudur. 

Uygulama, modern bir arayüz (Treeview) sunarak ürünlerin anlık durumunu listeler ve kritik stok seviyelerinin altına düşen ürünleri görsel olarak kullanıcıya bildirir.

---

## ✨ Özellikler

* **Ürün Ekleme & Güncelleme:** Yeni ürün adı, stok miktarı ve minimum stok sınırı girilerek envantere ekleme yapılabilir. Eğer ürün zaten mevcutsa, girilen miktar eski stoğun üzerine otomatik eklenir.
* **Anlık Tablo Görünümü (Treeview):** Tüm ürünler sağ taraftaki dinamik tabloda listelenir.
* **🚨 Kritik Stok Uyarısı:** Stok miktarı, belirlenen minimum stok seviyesinin altına düşen ürünlerin satırları otomatik olarak **kırmızı** renge boyanarak dikkat çeker.
* **Ürün Filtreleme:** Ürün adı üzerinden dinamik arama ve filtreleme yapılabilir.
* **Stok Azaltma:** Satış veya kullanım durumlarında, ürünlerin envanter miktarı güvenli bir şekilde düşürülür (Yetersiz stok kontrolü mevcuttur).
* **Ürün Silme:** Envanterden tamamen çıkarılmak istenen ürünler kolayca silinebilir.
* **Genel Raporlama:** Tek tıkla tüm envanterdeki toplam ürün sayısını görebilme.
* **💾 Otomatik Veri Kaydı:** Uygulama kapatılırken veriler otomatik olarak `stock.db` SQLite veritabanına güvenli bir şekilde işlenir ve sonraki açılışta otomatik yüklenir.

---

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Arayüz (GUI):** Tkinter & ttk (Treeview)
* **Veritabanı:** SQLite3

---

## 🚀 Nasıl Çalıştırılır?

Projenin bilgisayarınızda çalışması için Python'ın yüklü olması yeterlidir. Ekstra bir kütüphane kurulumuna (pip) gerek yoktur.

1. Bu depoyu (repository) bilgisayarınıza indirin veya klonlayın:
   ```bash
   git clone [https://github.com/mustafademir-ai/stoktakip.git](https://github.com/mustafademir-ai/stoktakip.git)
   ```
2. Proje klasörüne giriş yapın:
   ```bash
   cd stoktakip
   ```
3. Uygulamayı çalıştırın:
   ```bash
   python stoktakip.py
   ```
