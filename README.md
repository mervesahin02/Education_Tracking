# Education_Tracking
Bu proje, **BTK Akademi** bünyesindeki eğitim süreçlerini dijital ortamda yönetmek ve izlemek için geliştirilen bir masaüstü yazılım sistemidir. Amaç, eğitimlerin planlama, takip ve raporlama süreçlerini merkezi ve kullanıcı dostu bir platform aracılığıyla yönetilebilir kılmaktır.

## Proje Amacı
- Eğitim süreçlerinin **standartlaştırılması**
- Katılımcı ve eğitmen bilgilerinin merkezi veri tabanında tutulması
- Her eğitimin durumunun aşama bazlı olarak izlenmesi
- Otomatik **raporlamalar** ve **sertifika yönetimi**
- Çevrimiçi / Yüz yüze eğitim ayrımıyla gelişmiş takip imkânı

## Sistem Mimarisi

### ER Diyagramı

Eğitim, kullanıcı, katılım, geri bildirim, aşamalar ve sertifikalar arasındaki ilişki aşağıdaki gibi modellenmiştir:
![ChatGPT Image 6 May 2025 11_30_39](https://github.com/user-attachments/assets/a9c92597-1d39-4e22-aefc-0ce36a0f85c4)

## Uygulama Akışı

Uygulamanın temel ekranları ve kullanıcı etkileşim akışı aşağıdaki gibidir:

![Ekran görüntüsü 2025-05-07 093925](https://github.com/user-attachments/assets/278192af-3fd4-416d-9047-b66a61c1dff3)


1. **Giriş Ekranı** – Kullanıcı adı ve şifre ile JWT doğrulaması yapılır.
2. **Ana Menü** – Eğitim arama, eğitim ekleme ve tüm eğitimlerin listelenmesi.
3. **Eğitim Ekleme** – Çevrimiçi veya yüz yüze seçenekleri ile form bazlı ekleme.
4. **Kartlı Görünüm** – Havuzdan tamamlanmaya kadar tüm aşamalar için eğitimlerin durum bazlı kart görünümü.

## Eğitim Aşamaları

Eğitim kartları; Havuz, Plan, Anlaşma, İlan, İptal, Gerçekleşme, Teslim, Ön Kontrol, Kontrol, Medya, Ödemeler, TGvTD, Tamamlanan gibi aşamalarda görüntülenir. Her aşama, ilgili işlem adımlarının tamamlanma durumuna göre otomatik geçiş yapabilir.
