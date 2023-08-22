# Foodgram
[![GitHub](https://github.com/fklska/foodgram-project-react/actions/workflows/main.yaml/badge.svg)](https://github.com/fklska/foodgram-project-react/actions/workflows/main.yaml)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/fklska_bot)

[Доступно по адресу](https://foodgram-fklska.hopto.org/)

[Документация](https://foodgram-fklska.hopto.org/api/docs/)

Данные для админки:
```
login: admin
pass: admin
```
`python manage.py csv` - добавление ингредиентов в базу

---

## Доступные эндпоинты
```
admin/
api/ ^tags/
api/ ^tags/(?P<pk>[^/.]+)/
api/ ^recipes/
api/ ^recipes/download_shopping_cart/
api/ ^recipes/(?P<pk>[^/.]+)/
api/ ^recipes/(?P<pk>[^/.]+)/favorite/
api/ ^recipes/(?P<pk>[^/.]+)/shopping_cart/
api/ ^ingredients/
api/ ^ingredients/(?P<pk>[^/.]+)/
api/ ^users/
api/ ^users/activation/
api/ ^users/me/
api/ ^users/resend_activation/
api/ ^users/reset_password/
api/ ^users/reset_password_confirm/
api/ ^users/reset_username/
api/ ^users/reset_username_confirm/
api/ ^users/set_password/
api/ ^users/set_username/
api/ ^users/subscriptions/
api/ ^users/(?P<id>[^/.]+)/
api/ ^users/(?P<id>[^/.]+)/subscribe/
api/ auth/
```
---
## Пример работы нескольких эндпоинтов

Endpoint | Response | Params 
--- | --- | ---|
`api/tags/` | `[{"id": 1,"name": "Жизнь без забот","color": "#32FFB2","slug": "akuna_matata"}]` | -
`api/ingredients` | `[{"name": "абрикосовое варенье","measurement_unit": "г","id": 1},{"name": "абрикосовое пюре","measurement_unit": "г", "id":2}]` | -
`api/ingredients?name=пюре` | `[[{"name":"пюре","measurement_unit":"по вкусу","id":1408}]` | `name=пюре`
---
## Как развернуть проект

1. Скачать репозиторий `git clone https://github.com/fklska/foodgram-project-react`
2. Запустить `docker compose up`
