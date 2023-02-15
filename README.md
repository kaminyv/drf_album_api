# DRF Album API

Test application on the django rest framework

## Задача

Соберите с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры:

- Исполнитель
  - Название
  - Альбом
    - Год выпуска
    - Песня
      - Название
      - Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.

В качестве площадки для демонстрации АПИ подключите к нему Swagger, чтобы можно было проверить работу АПИ через Postman

Результат присылайте в виде репозитория в GitHub с инструкцией по запуску. 
Бонусом будет, если проект будет запускаться через docker compose.

## Развертывание

Клонируем проект: `git clone https://github.com/kaminyv/drf_album_api.git`

Переходим в папку проекта: `cd drf_album_api`

Копируем файл переменных среды: `cp app/.env.example app/.env`

**Развертывание через виртуальное окружение:**

- Создаем и активируем виртуальное окружение: `python3 -m venv venv && source venv/bin/activate`
- Устанавливаем пакеты: `pip install --upgrate pip && pip install -r requirements.txt`
- Генерируем секретны ключ: `python app/manage.py createsecretkey`
- Добавляем секретны ключ в файл `.env` в каталоге `app`
- Применяем миграции: `python app/manage.py migrate`
- Применяем посев начальных данных: `python app/manage.py seeding`
- Создаем супер пользователя: `python app/manage.py createsuperuser`
- Запускаем dev сервер: `python app/manage.py runserver`

**Развертывание через docker:**

- Запускаем docker compose: `docker compose up -d`
- Генерируем секретный ключ: `docker compose exec -it app python manage.py createsecretkey`
- Добавляем секретны ключ в файл `.env` в каталоге `app`
- Применяем миграции: `docker compose exec -it app python manage.py migrate`
- Применяем посев начальных данных: `docker compose exec -it app python manage.py seeding`
- Создаем супер пользователя: `docker compose exec -it app python manage.py createsuperuser`
- Перезапускаем docker compose: `docker compose restart`
 
## API

Документация находится по адресу: `http://127.0.0.1:8000/api/swagger/`
