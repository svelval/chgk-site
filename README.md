
# Установка пакетов

* Установите [python3](https://www.python.org/downloads/)
* Установите [docker](https://docs.docker.com/engine/install). <br>
Важно! В `Windows` могут быть проблемы с установкой/обновлением WSL. Для исправления установите Docker 4.28.0. 

# Подготовка виртуальной среды
* Создайте файл **.env** в корне проекта
```
SECRET_KEY = 'секретный ключ'
DEBUG = 1
ALLOWED_HOSTS =  '127.0.0.1 localhost'
LANGUAGE_CODE = ru
TIME_ZONE = Europe/Moscow

POSTGRES_HOST = 127.0.0.1
POSTGRES_DB = payment_service
POSTGRES_USER = payment_service
POSTGRES_PASSWORD = 12345
POSTGRES_PORT = 5432

REDIS_HOST = 127.0.0.1
REDIS_PORT = 6379
REDIS_PASSWORD = 12345
```
* Для создания **секретного ключа**, выполните данные команды
```
# Linux/MacOS
pip3 install django
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Windows
pip install django
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```


# Подготовка MAKE-файла
#### Windows
* Скачайте MinGW для Windows: https://sourceforge.net/projects/mingw/
* ![minGW install](https://miro.medium.com/v2/resize:fit:750/format:webp/1*N-uy3dVJy0xXCPEgcmKNNQ.jpeg)
* Зайдите в настройки компьютера -> Дополнительные параметры системы -> Переменные среды 
![img](https://miro.medium.com/v2/resize:fit:640/format:webp/1*vmbCAM8Tuz9QC7a00ZlTaQ.jpeg)
* В <b>Системные переменные</b> найдите `Path` и дважды кликните по нему
![img](https://miro.medium.com/v2/resize:fit:786/format:webp/1*UdDdSSGo52XPe244eqaxnA.jpeg)
* Нажмите <b>Создать</b> и укажите путь `C:\MinGW\bin`
![img](https://miro.medium.com/v2/resize:fit:786/format:webp/1*vzIWTK4bGOJOD2t6a2GxSA.jpeg)
* Запустите командную строку от имени администратора и введите команду `mingw-get install mingw32-make`
![img](https://miro.medium.com/v2/resize:fit:786/format:webp/1*808g-SdrlD8PUlXoCWbylw.jpeg)
* Проверьте, прошла ли установка успешно с помощью команды `mingw32-make — version`
* Чтобы использовать имя `make` в командах, перейдите в папку `C:\MinGW\bin` и переименуйте файл `mingw32-make.exe` в `make.exe`
![img](https://miro.medium.com/v2/resize:fit:786/format:webp/1*KiewmLqoeN7EbgrCTjXZSw.jpeg)
* Перезапустите свою IDE, если она была запущена

# Запуск БД
```
docker compose up
```
или
```
make db-up
```

# Остановка БД
```
docker compose down
```
или
```
make db-down
```

# Запуск сервера
```
make django-server
```

# Создание миграций
```
make migrations
```

# Применение миграций
```
make migrate
```

# Запуск shell
```
make shell
```

# Создание суперпользователя
```
make createsuperuser
```
