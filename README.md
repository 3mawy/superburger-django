# superburger-django
e-commerce api 
## Run The Project
```
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt 
```
## Run Using Docker 
```
 docker-compose up --build -d
 docker exec -it superburger-django_web_1 bash
```

## Run Migration and add mock data

```
 python manage.py migrate
 python manage.py loaddata api/fixtures/*.json

```
# API Reference
https://documenter.getpostman.com/view/13498731/2s9Xy5MqW6











## reset database data
```
 python manage.py flush
```