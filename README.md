# clockram

Instagram hesabınızın profil fotoğrafını o anki saate ayarlar. Max hata payı 5 saniyedir, bunu siz değiştirebilirsiniz.


[ KURULUM ]

Kodu çalıştırmak için Python yüklemeniz gerekiyor. Python yükledikten sonra pip aracını yükleyeceksiniz. Pip aracı gerekli modülleri yüklemeniz için gerekiyor:

pip install requests
pip install Pillow


Her şeyi yüklediyseniz geriye config dosyasını ayarlamak kalıyor. Config dosyasında username ve password yazan kısım instagram hesabınızın kullanıcı adı ve şifresi. background_color, oluşturulacak resmin arkaplanının renk kodları. text_color ise text'in rengi. Bu kısmı değiştirmek isterseniz aşağıda verdiğim siteden rgb renk kodları alıp parantez işaretlerini köşeli parantezle değiştireceksiniz.

https://www.w3schools.com/colors/colors_rgb.asp

Örnek:
(0, 0, 0) -> [0, 0, 0]

Delay yazan kısım ise saati kaç saniyede bir kontrol edeceğiniz, eğer pc'nizde çalıştıracaksanız 5 yapabilirsiniz.


[ TEKNİK DETAYLAR ]

+ Program instagram'a sadece bir kere giriş yapıyor, böylece instagram'dan ban yemiyorsunuz.

+ Eğer saat değişmişse profil fotoğrafını değiştiriyor.

+ Yüklenecek profil fotoğrafını Pillow ile anlık olarak oluşturuyor, saçma sapan bir sürü dosya ile uğraşmıyorsunuz (ben <3 Python)

+ Json tuple desteklemediği için renk kodlarını list olarak aldım, kod çalışırken tuple'a çeviriyorum.
