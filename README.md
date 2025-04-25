# OpenCV SDK ile Yüz Tanıma ve Koleksiyon Yönetimi

## Genel Bakış
Bu Python projesi, **opencv.fr SDK** kullanarak yüz tanıma, kişi kaydı ve koleksiyon yönetimi işlemlerini gerçekleştirir. Kullanıcılar kendi koleksiyonlarını oluşturabilir, kişileri birden fazla yüz görseli ile kaydedebilir ve verilen bir görsel üzerinden arama yaparak kişiyi ve ait olduğu koleksiyonu tespit edebilir.

## Özellikler
- Yeni yüz koleksiyonları oluşturur (örneğin: Normal Kişiler, Ünlü Kişiler)
- Kişileri birden fazla yüz görseliyle sisteme kaydeder
- Yüz araması yaparak eşleşen kişiyi ve benzerlik skorunu bulur
- Eşleşen kişinin ait olduğu koleksiyonları listeler

## Gereksinimler
```bash
pip install opencv-python python-dotenv
