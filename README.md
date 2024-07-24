# API для Yatube

> Проект "API для Yatube" представляет собой API для социальной сети, разработанный с использованием Django и Django REST framework. Этот API предоставляет возможность пользователям создавать, просматривать и взаимодействовать с постами, комментариями, группами и подписками. API требует аутентификации и авторизации с использованием JWT-токенов (Djoser), что гарантирует сохранность и конфиденциальность пользовательских данных.

## Установка
1. Клонируйте репозиторий на свой компьютер:
```
git clone git@github.com:SHURSHALO/api_yatube.git
```
2. Создайте виртуальное окружение и активируйте его:
```
py -3.9 -m venv venv
```
```
source venv/Scripts/activate
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Примените миграции:
```
python manage.py migrate
```
5. Создайте суперпользователя:
```
python manage.py createsuperuser
```
6. Запустите сервер:
```
python manage.py runserver
```
Документация доступна по: http://127.0.0.1:8000/redoc/

## Использование

API имеет следующие эндпоинты:

api/v1/api-token-auth/ (POST): Получение токена по логину и паролю.

api/v1/posts/ (GET, POST): Получение списка всех постов или создание нового поста.

api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): Получение, редактирование или удаление поста по ID.

api/v1/groups/ (GET): Получение списка всех групп.

api/v1/groups/{group_id}/ (GET): Получение информации о группе по ID.

api/v1/posts/{post_id}/comments/ (GET, POST): Получение списка всех комментариев для поста с указанным ID или создание нового комментария для данного поста.

api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): Получение, редактирование или удаление комментария по ID для поста с указанным ID.

API требует аутентификации по токену. Аутентифицированные пользователи могут редактировать и удалять только свой собственный контент. Попытка изменения чужого контента будет приводить к ошибке 403 Forbidden.

