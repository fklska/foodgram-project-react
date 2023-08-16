# Foodgram
## Установка
1. ```git clone git@github.com:fklska/foodgram-project-react.git```
2. ```docker compose up```
3. Внутри контейнера backend
```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py csv
```
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
