## Тестовая работа

В проекте есть следующие модели

####Район города
Имеет название и ID

####Категория
Имеет название и ID

####Сеть предприятий
Имеет название и ID

####Предприятие
Имеет ID, название, описание, принадлежность к одной сети, принадлежность к району (одному или нескольким), список товаров\услуг с ценами (цены могут быть различны в разных предприятиях)

####Товар\услуга
Имеет ID, название и принадлежит к определенной категории
 

### Шаблон наполнения файла .env: 

 

``` 

SECRET_KEY=yoursecretkey # указываем свой секретный ключ

DEBUG = False # True если нужен режим отладки

DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql 

DB_NAME=postgres # имя базы данных 

POSTGRES_USER=postgres # логин для подключения к базе данных 

POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой) 

DB_HOST=db # название сервиса (контейнера) 

DB_PORT=5432 # порт для подключения к БД  

``` 

 

 

### Как запустить проект: 

 

Клонировать репозиторий и перейти в него в командной строке: 

``` 

git clone https://github.com/DominusMortem/testSpiderGroup.git 

``` 

 
Перейти в каталог
``` 

cd test_spider_group/infra 

``` 

Создать контейнеры 

``` 

docker-compose up -d --build 

``` 

После запуска контейнеров выполнить команды 

``` 

docker-compose exec web python manage.py migrate 

docker-compose exec web python manage.py createsuperuser 

docker-compose exec web python manage.py collectstatic --no-input 

``` 

Для наполнения базы данных разместите файл data.json в папке test_spider_group\spidergroup: 

``` 

docker-compose exec web python manage.py loaddata fixtures.json 

``` 

 

### Технологии: 

Python 3.10 

Django 3.2.15

Django REST Framework 3.13.1

PostrgeSQL 

Gunicorn

Nginx 

 

# Алгоритм регистрации пользователей 


Запросы к API начинаются с ```/api/```

Для получения токена перейти по адресу
```
/token/login/
```
И передать ```'email' и 'password'```

### Примеры запросов: 




 /districts/: 

GET 

Получение списка всех районов 


``` 
[
   { 
     "id": int, 
     "name": "string", 
   }
] 
``` 

 /districts/<district_id>/organizations/: 

GET 

Получение списка всех организаций в районе

```  
[ 
  { 
    "id": int, 
    "name": "string", 
    "description": "string",
    "network": "string",
    "district": [ 
      { 
        "id": int, 
        "name": "string" 
      } 
    ]
    "product": [ 
      { 
         "id": int, 
         "product": [ 
          { 
            "id": int, 
            "name": "string",
            "category": [ 
          { 
            "id": int, 
            "name": "string" 
          } 
        ], 
          } 
        ],
         "price": int
      }
    ]
  } 
] 

```

/product/: 

GET 

Получить список всех продуктов.

``` 
[ 
  { 
    "id": int, 
    "name": "string", 
    "category": [ 
      { 
        "id": int, 
        "name": "string", 
      } 
    ] 
  } 
] 
``` 

POST 

Добавить новый продукт. 

``` 
{ 
  "name": "string", 
  "category": [ 
    "name": string" 
  ], 
} 
``` 
