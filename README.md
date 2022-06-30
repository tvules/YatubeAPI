<h1 align="center">Yatube API (REST)</h1>

## О проекте

Yatube API - это RESTful API для учебного проекта Yatube, который был разработан при обучении в Yandex Practicum.

### Возможности

- Создавать посты
- Комментировать
- Подписываться на авторов

Дополнительные возможности описаны в redoc-документации `/redoc`

### Технологии

- Django
- Django REST framework
- JWTAuthentication (Djoser)
- Redoc

## Установка

1. Клонируйте репозиторий:
 ```
 git clone https://github.com/tvules/api_final_yatube.git
 ```
2. Установить виртуальное окружение и активировать его:
```
 python3 -m venv venv
 ```
 ```
 source venv/bin/activate
 ```
3. Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python3 manage.py migrate
```
5. Запустить сервер командой
```
python3 manage.py runserver
```