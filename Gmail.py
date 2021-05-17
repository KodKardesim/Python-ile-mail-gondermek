import smtplib

mail_adresi = "kodkardesim@gmail.com"  # Kendi mail adresiniz
sifre = "sifreniz"  # Şifreniz

mail = smtplib.SMTP("smtp.gmail.com", 587)  # Gmail sunucusuna bağlantı tanımladık.
mail.starttls()  # Bağlantıyı başlattık.

mail.login(mail_adresi, sifre)  # Giriş yaptık.

alici = "kodkardesim@gmail.com"     # Mail göndermek istediğiniz alıcının mail adresi

baslik = "Python ile Mail gönderimi hakkında"
text = "Bu postumuzda Python ile mail göndermeyi gördük, like atmayı unutmayın!"
mesaj = f"Subject:{baslik}\n{text}"

mail.sendmail(mail_adresi, alici, mesaj.encode("utf-8"))
print("Mail gönderildi!")
