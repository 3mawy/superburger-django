# superburger-django

## Run The Project
```
python3 -m venv env
source env/bin/activate
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












## reset database data
```
 python manage.py flush
```