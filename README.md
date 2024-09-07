Установка
-
- клонировать проект
- выйти в виртуальное окружение poetry\
poetry shell
- установить зависимости\
poetry install
- создать локальную базу данных Postgres\
CREATE DATABASE имя_БД
- заполнить файл .env по образцу env_example
- выполнить миграции\
python manage.py migrate

URL
-
- список профилей пользователей\
method: GET\
/api/users/djoser/users/


- регистрация пользователя\
method: POST\
/api/users/djoser/users/


- просмотр и изменение пользователя (user-свой, admin-все)\
method: GET, PATCH, DELETE\
/api/users/djoser/users/{id}/


- изменения пароля пользователя\
method: POST\
/api/users/djoser/users/set_password/


- сброса пароля, ссылка на email\
method: POST\
/api/users/djoser/users/reset_password/


- создать объявление\
method: POST\
/api/ads/ad_create/


- список объявлений\
method: GET\
/api/ads/mylist/


- изменить объявление\
method: PATCH\
/api/ads/<pk>/update/


- изменить объявление\
method: DELETE\
/api/ads/<pk>/delete/

**Права пользователей.**

- Анонимный пользователь может:
    - получать список объявлений.
- Пользователь может:
    - получать список объявлений,
    - получать одно объявление,
    - создавать объявление,
    - редактировать и удалять свое объявление,
    - получать список комментариев,
    - создавать комментарии,
    - редактировать/удалять свои комментарии.
- Администратор может:
    - дополнительно к правам пользователя редактировать или удалять объявления и комментарии любых других пользователей.


**Docker.**

- `Dockerfile` для сборки образа приложения.
- `docker-compose.yaml` для запуска приложения и базы данных PostgreSQL.\
Запуска приложения
  - Сборка образов\
  docker-compose build
  - Запуск контейнеров\
  docker-compose up




