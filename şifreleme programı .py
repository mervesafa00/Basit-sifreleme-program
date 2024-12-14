uname = "Merve Safa"
passwd = "h,sklDnlS."

sayac = 3
while sayac!=0:
    sayac -=1
    username = input("Kullanıcı adınızı girin : ")
    if uname != username :
        print(f"Kullanıcı adı yanlış , kalan deneme hakkınız {sayac}  ")
    if uname == username:
        password = input("Şirenizi girin : ")
        if passwd == password:
            print("Hoş geldiniz")
        else:
            print(f"Şifre Yanlış,kalan deneme hakkınız {sayac}")



