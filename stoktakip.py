import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class StokUygulamasi:
    def __init__(self, root):
        self.ana_pencere = root
        self.ana_pencere.title("Stok Takip Uygulaması")

        # Veritabanı bağlantısı
        self.veritabani = sqlite3.connect("stock.db")
        self.tablo_olustur()

        # Ürünleri tutan sözlük
        self.urunler = {}

        self.verileri_yukle()
        self.arayuz_olustur()

    # Veritabanı tablosunu oluşturur
    def tablo_olustur(self):
        sorgu = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER,
            min_stock INTEGER
        );
        """
        self.veritabani.execute(sorgu)
        self.veritabani.commit()

    # Verileri veritabanından yükler
    def verileri_yukle(self):
        sorgu = "SELECT * FROM products"
        cursor = self.veritabani.execute(sorgu)

        for satir in cursor:
            self.urunler[satir[1]] = {
                'miktar': satir[2],
                'min_stok': satir[3]
            }

    # Verileri veritabanına kaydeder
    def verileri_kaydet(self):
        self.veritabani.execute("DELETE FROM products")

        for urun, veri in self.urunler.items():
            sorgu = f"""
            INSERT INTO products (name, quantity, min_stock)
            VALUES ('{urun}', {veri['miktar']}, {veri['min_stok']})
            """
            self.veritabani.execute(sorgu)

        self.veritabani.commit()

    # Arayüzü oluşturur
    def arayuz_olustur(self):

        tk.Label(self.ana_pencere, text="Ürün Adı:").grid(row=0, column=0)
        self.giris_urun_adi = tk.Entry(self.ana_pencere)
        self.giris_urun_adi.grid(row=0, column=1)

        tk.Label(self.ana_pencere, text="Stok Miktarı:").grid(row=1, column=0)
        self.giris_miktar = tk.Entry(self.ana_pencere)
        self.giris_miktar.grid(row=1, column=1)

        tk.Label(self.ana_pencere, text="Minimum Stok:").grid(row=2, column=0)
        self.giris_min_stok = tk.Entry(self.ana_pencere)
        self.giris_min_stok.grid(row=2, column=1)

        tk.Button(self.ana_pencere, text="Ürün Ekle", command=self.urun_ekle)\
            .grid(row=3, column=0, columnspan=2)

        tk.Button(self.ana_pencere, text="Stok Görüntüle", command=self.stok_goster)\
            .grid(row=4, column=0, columnspan=2)

        # Filtreleme alanı
        tk.Label(self.ana_pencere, text="Ürün Filtrele:").grid(row=5, column=0)
        self.giris_filtre = tk.Entry(self.ana_pencere)
        self.giris_filtre.grid(row=5, column=1)

        tk.Button(self.ana_pencere, text="Filtrele", command=self.urun_filtrele)\
            .grid(row=6, column=0, columnspan=2)

        # Toplam stok
        self.etiket_toplam = tk.Label(self.ana_pencere, text="Toplam Stok:")
        self.etiket_toplam.grid(row=7, column=0)

        tk.Button(self.ana_pencere, text="Toplam Stok", command=self.toplam_stok)\
            .grid(row=7, column=1)

        # Ürün silme
        tk.Label(self.ana_pencere, text="Ürün Sil:").grid(row=8, column=0)
        self.giris_sil = tk.Entry(self.ana_pencere)
        self.giris_sil.grid(row=8, column=1)

        tk.Button(self.ana_pencere, text="Sil", command=self.urun_sil)\
            .grid(row=9, column=0, columnspan=2)

        # Stok azaltma
        tk.Label(self.ana_pencere, text="Stok Azalt:").grid(row=10, column=0)
        self.giris_azalt_urun = tk.Entry(self.ana_pencere)
        self.giris_azalt_urun.grid(row=10, column=1)

        tk.Label(self.ana_pencere, text="Miktar:").grid(row=11, column=0)
        self.giris_azalt_miktar = tk.Entry(self.ana_pencere)
        self.giris_azalt_miktar.grid(row=11, column=1)

        tk.Button(self.ana_pencere, text="Azalt", command=self.stok_azalt)\
            .grid(row=12, column=0, columnspan=2)

        # Tablo (Treeview)
        self.tablo = ttk.Treeview(self.ana_pencere,
                                  columns=("Ürün", "Stok", "Min"),
                                  show="headings")

        self.tablo.heading("Ürün", text="Ürün")
        self.tablo.heading("Stok", text="Stok")
        self.tablo.heading("Min", text="Min. Stok")

        self.tablo.grid(row=0, column=2, rowspan=13, padx=10)

        self.tablo_guncelle()

    # Ürün ekleme
    def urun_ekle(self):
        urun_adi = self.giris_urun_adi.get()
        miktar = int(self.giris_miktar.get())
        min_stok = int(self.giris_min_stok.get())

        if urun_adi:
            if urun_adi in self.urunler:
                self.urunler[urun_adi]['miktar'] += miktar
            else:
                self.urunler[urun_adi] = {
                    'miktar': miktar,
                    'min_stok': min_stok
                }

            messagebox.showinfo("Başarılı", "Ürün eklendi.")
            self.tablo_guncelle()

    # Stok göster
    def stok_goster(self):
        metin = ""
        for u, v in self.urunler.items():
            metin += f"{u}: {v['miktar']} (Min: {v['min_stok']})\n"

        messagebox.showinfo("Stok", metin)

    # Ürün filtreleme
    def urun_filtrele(self):
        filtre = self.giris_filtre.get()
        sonuc = ""

        for u, v in self.urunler.items():
            if filtre.lower() in u.lower():
                sonuc += f"{u}: {v['miktar']}\n"

        messagebox.showinfo("Filtre", sonuc)

    # Toplam stok
    def toplam_stok(self):
        toplam = sum(v['miktar'] for v in self.urunler.values())
        messagebox.showinfo("Toplam Stok", str(toplam))

    # Ürün silme
    def urun_sil(self):
        urun = self.giris_sil.get()

        if urun in self.urunler:
            del self.urunler[urun]
            self.tablo_guncelle()
        else:
            messagebox.showerror("Hata", "Ürün bulunamadı")

    # Stok azaltma
    def stok_azalt(self):
        urun = self.giris_azalt_urun.get()
        miktar = int(self.giris_azalt_miktar.get())

        if urun in self.urunler:
            if self.urunler[urun]['miktar'] >= miktar:
                self.urunler[urun]['miktar'] -= miktar
                self.tablo_guncelle()
            else:
                messagebox.showerror("Hata", "Yetersiz stok")

    # Tabloyu güncelle
    def tablo_guncelle(self):
        self.tablo.delete(*self.tablo.get_children())

        for u, v in self.urunler.items():
            item = self.tablo.insert("", "end", values=(u, v['miktar'], v['min_stok']))

            if v['miktar'] < v['min_stok']:
                self.tablo.item(item, tags=("dusuk",))
            else:
                self.tablo.item(item, tags=("normal",))

        self.tablo.tag_configure("dusuk", background="red", foreground="white")
        self.tablo.tag_configure("normal", background="white", foreground="black")

    # Program kapanırken kaydet
    def __del__(self):
        self.verileri_kaydet()
        self.veritabani.close()


if __name__ == "__main__":
    root = tk.Tk()
    uygulama = StokUygulamasi(root)
    root.mainloop()