class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # ссылка на путь до базы данных
    SECRET_KEY = '7d2c3a6aa3289de651a7e54da187'  # секретный ключ для подписи сеансовых cookie-файлов

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "badrhymes@yandex.ru" # email должен быть в utils.py
    MAIL_PASSWORD = "Ybrjkfif1"
    # # настройки: почта/все настройки/почтовые программы

    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = "korostylev.ov@gmail.com"
    # MAIL_PASSWORD = ""


