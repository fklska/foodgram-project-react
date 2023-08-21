# Foodgram
Доступно по [адресу](https://foodgram-fklska.hopto.org/)

[Документация](https://foodgram-fklska.hopto.org/api/docs/)

Данные для админки:
```
login: admin
pass: admin
```
---
```python manage.py csv``` - добавление ингредиентов в базу
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
