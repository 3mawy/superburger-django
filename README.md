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
# 📁 Collection: Auth 


## End-point: signup
### Method: POST
>```
>http://localhost:8003/api/signup
>```
### Body (**raw**)

```json
{
    "username": "user1",
    "password": "password",
    "full_name": "first_name",
    "mobile_number": "01011565",
    "address": "SS1B",
    "email": "userecoom@google.com"
}
```

### Response: 200
```json
{
    "message": "Signed up Successfully!",
    "customer_email": "userecoom@google.com"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: login
### Method: POST
>```
>http://localhost:8003/login
>```
### Body (**raw**)

```json
{
    "username": "user1",
    "password": "password"
}
```

### 🔑 Authentication noauth

 


### Response: 200
```json
{
    "message": "Logged in successfully!",
    "user_id": 5,
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMzU3OTQ1LCJqdGkiOiI0OTZlMDkwYzljZGE0N2JmYWY3MDI1Mjc1ZWVjOWVkYyIsInVzZXJfaWQiOjV9.BZj2dhL2M9-yWRO0Mgn25gqcfoYu08ipyKhy3_QXhyQ"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Public 


## End-point: get categories
### Method: GET
>```
>http://localhost:8003/api/categories/
>```
### 🔑 Authentication noauth

 


### Response: 200
```json
{
    "links": {
        "next": null,
        "previous": null
    },
    "count": 2,
    "total_pages": 1,
    "results": [
        {
            "id": 1,
            "name": "chicken",
            "image": {
                "id": 15,
                "image": "http://localhost:8003/media/categories/chicken.jpeg",
                "desc": null
            }
        },
        {
            "id": 2,
            "name": "beef",
            "image": {
                "id": 16,
                "image": "http://localhost:8003/media/categories/beef.jpeg",
                "desc": null
            }
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get menu-items
### Method: GET
>```
>http://localhost:8003/menu-items/
>```
### 🔑 Authentication noauth

 


### Response: 200
```json
{
    "links": {
        "next": "http://localhost:8003/menu-items/?page=2",
        "previous": null
    },
    "count": 14,
    "total_pages": 2,
    "results": [
        {
            "id": 1,
            "name": "dad's burger",
            "name_ar": "chicken island",
            "description": "super sauce, lettuce, tomatoes, onion",
            "description_ar": "قطعه البرجر المشويه مع مزيج من شرائح الخضروات الفريش و صوص سوبر المميز",
            "active": true,
            "score": "1",
            "category": {
                "id": 2,
                "name": "beef",
                "description": "Beef Sandwiches",
                "image": 16
            },
            "sizes": [
                {
                    "id": 1,
                    "menu_item": 1,
                    "size": "large",
                    "price": "30.00"
                },
                {
                    "id": 2,
                    "menu_item": 1,
                    "size": "double",
                    "price": "50.00"
                }
            ],
            "image": {
                "id": 1,
                "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                "desc": null
            }
        },
        {
            "id": 2,
            "name": "super blue",
            "name_ar": "chicken island",
            "description": "super sauce, blue cheese, tomatoes, onion",
            "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
            "active": true,
            "score": "50",
            "category": {
                "id": 2,
                "name": "beef",
                "description": "Beef Sandwiches",
                "image": 16
            },
            "sizes": [
                {
                    "id": 1,
                    "menu_item": 2,
                    "size": "large",
                    "price": "20.00"
                },
                {
                    "id": 2,
                    "menu_item": 2,
                    "size": "double",
                    "price": "25.00"
                }
            ],
            "image": {
                "id": 2,
                "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                "desc": null
            }
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get item
### Method: GET
>```
>http://localhost:8003/menu-items/1
>```
### 🔑 Authentication noauth

 


### Response: 200
```json
{
    "id": 1,
    "name": "dad's burger",
    "name_ar": "chicken island",
    "description": "super sauce, lettuce, tomatoes, onion",
    "description_ar": "قطعه البرجر المشويه مع مزيج من شرائح الخضروات الفريش و صوص سوبر المميز",
    "active": true,
    "score": "1",
    "category": {
        "id": 2,
        "name": "beef",
        "description": "Beef Sandwiches",
        "image": 16
    },
    "sizes": [
        {
            "id": 1,
            "menu_item": 1,
            "size": "large",
            "price": "30.00"
        },
        {
            "id": 2,
            "menu_item": 1,
            "size": "double",
            "price": "50.00"
        }
    ],
    "image": {
        "id": 1,
        "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
        "desc": null
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get offers
### Method: GET
>```
>http://localhost:8003/offers/
>```
### 🔑 Authentication noauth

 


### Response: 200
```json
{
    "links": {
        "next": null,
        "previous": null
    },
    "count": 2,
    "total_pages": 1,
    "results": [
        {
            "id": 1,
            "name": "offer",
            "description": "offerof ferofferof ferofferoffer",
            "price": "40.00",
            "active": true,
            "menu_items": [
                {
                    "id": 1,
                    "name": "dad's burger",
                    "name_ar": "chicken island",
                    "description": "super sauce, lettuce, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه مع مزيج من شرائح الخضروات الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "1",
                    "image": {
                        "id": 1,
                        "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                        "desc": null
                    },
                    "category": {
                        "id": 2,
                        "name": "beef",
                        "description": "Beef Sandwiches",
                        "image": 16
                    },
                    "sizes": [
                        {
                            "id": 1,
                            "name": "large",
                            "name_ar": "لارج"
                        },
                        {
                            "id": 2,
                            "name": "double",
                            "name_ar": "دبل"
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "super blue",
                    "name_ar": "chicken island",
                    "description": "super sauce, blue cheese, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "50",
                    "image": {
                        "id": 2,
                        "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                        "desc": null
                    },
                    "category": {
                        "id": 2,
                        "name": "beef",
                        "description": "Beef Sandwiches",
                        "image": 16
                    },
                    "sizes": [
                        {
                            "id": 1,
                            "name": "large",
                            "name_ar": "لارج"
                        },
                        {
                            "id": 2,
                            "name": "double",
                            "name_ar": "دبل"
                        }
                    ]
                },
                {
                    "id": 4,
                    "name": "smoked flavor",
                    "name_ar": "chicken island",
                    "description": "smoked beef, onion rings, lettuce, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه مع شرائح السموكد بيف و حلقات البصل المقرمشه مع شرائح الطماطم الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "1",
                    "image": {
                        "id": 4,
                        "image": "http://localhost:8003/media/sandwiches/smoked_flavor.jpeg",
                        "desc": null
                    },
                    "category": {
                        "id": 2,
                        "name": "beef",
                        "description": "Beef Sandwiches",
                        "image": 16
                    },
                    "sizes": [
                        {
                            "id": 1,
                            "name": "large",
                            "name_ar": "لارج"
                        },
                        {
                            "id": 2,
                            "name": "double",
                            "name_ar": "دبل"
                        }
                    ]
                },
                {
                    "id": 6,
                    "name": "melt cheese",
                    "name_ar": "chicken island",
                    "description": "super sauce, mix cheese, lettuce, tomatoes, onion",
                    "description_ar": "ثلاثه انواع من الجبن السائحه علي قطعه البرجر المشويه بالاضافه الي شرائح البصل و الطماطم الفريش",
                    "active": true,
                    "score": "1",
                    "image": {
                        "id": 6,
                        "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                        "desc": null
                    },
                    "category": {
                        "id": 2,
                        "name": "beef",
                        "description": "Beef Sandwiches",
                        "image": 16
                    },
                    "sizes": [
                        {
                            "id": 1,
                            "name": "large",
                            "name_ar": "لارج"
                        },
                        {
                            "id": 3,
                            "name": "stuffed",
                            "name_ar": "ستافد"
                        }
                    ]
                }
            ],
            "image": {
                "id": 9,
                "image": "http://localhost:8003/media/sandwiches/marvel_chicken.jpeg",
                "desc": null
            },
            "max_offer_items": 3
        },
        {
            "id": 2,
            "name": "offer",
            "description": "offer offer offer offer",
            "price": "54.99",
            "active": false,
            "menu_items": [
                {
                    "id": 2,
                    "name": "super blue",
                    "name_ar": "chicken island",
                    "description": "super sauce, blue cheese, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "50",
                    "image": {
                        "id": 2,
                        "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                        "desc": null
                    },
                    "category": {
                        "id": 2,
                        "name": "beef",
                        "description": "Beef Sandwiches",
                        "image": 16
                    },
                    "sizes": [
                        {
                            "id": 1,
                            "name": "large",
                            "name_ar": "لارج"
                        },
                        {
                            "id": 2,
                            "name": "double",
                            "name_ar": "دبل"
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "bacon & mushrooms",
                    "name_ar": "chicken island",
                    "description": "super sauce, caramelized onion, beef bacon, tomatoes, lettuce",
                    "description_ar": "قطعه البرجر المشويه مع مزيج من شرائح الخضروات الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "56",
                    "image": {
                        "id": 3,
                        "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                        "desc": null
                    },
                    "category": {
                        "id": 2,
                        "name": "beef",
                        "description": "Beef Sandwiches",
                        "image": 16
                    },
                    "sizes": [
                        {
                            "id": 1,
                            "name": "large",
                            "name_ar": "لارج"
                        },
                        {
                            "id": 2,
                            "name": "double",
                            "name_ar": "دبل"
                        }
                    ]
                }
            ],
            "image": {
                "id": 15,
                "image": "http://localhost:8003/media/categories/chicken.jpeg",
                "desc": null
            },
            "max_offer_items": 1
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get extras
### Method: GET
>```
>http://localhost:8003/offers/2
>```
### Response: 200
```json
{
    "id": 2,
    "name": "offer",
    "description": "offer offer offer offer",
    "price": "54.99",
    "active": false,
    "menu_items": [
        {
            "id": 2,
            "name": "super blue",
            "name_ar": "chicken island",
            "description": "super sauce, blue cheese, tomatoes, onion",
            "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
            "active": true,
            "score": "50",
            "image": {
                "id": 2,
                "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                "desc": null
            },
            "category": {
                "id": 2,
                "name": "beef",
                "description": "Beef Sandwiches",
                "image": 16
            },
            "sizes": [
                {
                    "id": 1,
                    "name": "large",
                    "name_ar": "لارج"
                },
                {
                    "id": 2,
                    "name": "double",
                    "name_ar": "دبل"
                }
            ]
        },
        {
            "id": 3,
            "name": "bacon & mushrooms",
            "name_ar": "chicken island",
            "description": "super sauce, caramelized onion, beef bacon, tomatoes, lettuce",
            "description_ar": "قطعه البرجر المشويه مع مزيج من شرائح الخضروات الفريش و صوص سوبر المميز",
            "active": true,
            "score": "56",
            "image": {
                "id": 3,
                "image": "http://localhost:8003/media/sandwiches/dads_burger.jpeg",
                "desc": null
            },
            "category": {
                "id": 2,
                "name": "beef",
                "description": "Beef Sandwiches",
                "image": 16
            },
            "sizes": [
                {
                    "id": 1,
                    "name": "large",
                    "name_ar": "لارج"
                },
                {
                    "id": 2,
                    "name": "double",
                    "name_ar": "دبل"
                }
            ]
        }
    ],
    "image": {
        "id": 15,
        "image": "http://localhost:8003/media/categories/chicken.jpeg",
        "desc": null
    },
    "max_offer_items": 1
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Authenticated User 


## End-point: get current user cart
### Method: GET
>```
>localhost:8003/api/cart/
>```
### Response: 200
```json
{
    "cart": {
        "id": 3,
        "total_price": "1920.00",
        "cart_items": [
            {
                "id": 82,
                "quantity": 16,
                "item_price": "20.00",
                "total_price": "768.00",
                "comments": null,
                "extras_price": "28.0",
                "size": {
                    "id": 1,
                    "name": "large",
                    "name_ar": "لارج"
                },
                "offer": null,
                "item": {
                    "id": 2,
                    "name": "super blue",
                    "name_ar": "chicken island",
                    "description": "super sauce, blue cheese, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "50",
                    "image": 2,
                    "category": 2,
                    "sizes": [
                        1,
                        2
                    ]
                },
                "extras": [
                    {
                        "id": 4,
                        "name": "extra4",
                        "name_ar": "chicken island",
                        "price": "5.0"
                    },
                    {
                        "id": 2,
                        "name": "extra2",
                        "name_ar": "chicken island",
                        "price": "8.0"
                    },
                    {
                        "id": 1,
                        "name": "extra1",
                        "name_ar": "chicken island",
                        "price": "15.0"
                    }
                ]
            },
            {
                "id": 83,
                "quantity": 8,
                "item_price": "25.00",
                "total_price": "424.00",
                "comments": null,
                "extras_price": "28.0",
                "size": {
                    "id": 2,
                    "name": "double",
                    "name_ar": "دبل"
                },
                "offer": null,
                "item": {
                    "id": 2,
                    "name": "super blue",
                    "name_ar": "chicken island",
                    "description": "super sauce, blue cheese, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "50",
                    "image": 2,
                    "category": 2,
                    "sizes": [
                        1,
                        2
                    ]
                },
                "extras": [
                    {
                        "id": 4,
                        "name": "extra4",
                        "name_ar": "chicken island",
                        "price": "5.0"
                    },
                    {
                        "id": 2,
                        "name": "extra2",
                        "name_ar": "chicken island",
                        "price": "8.0"
                    },
                    {
                        "id": 1,
                        "name": "extra1",
                        "name_ar": "chicken island",
                        "price": "15.0"
                    }
                ]
            },
            {
                "id": 84,
                "quantity": 8,
                "item_price": "25.00",
                "total_price": "384.00",
                "comments": null,
                "extras_price": "23.0",
                "size": {
                    "id": 2,
                    "name": "double",
                    "name_ar": "دبل"
                },
                "offer": null,
                "item": {
                    "id": 2,
                    "name": "super blue",
                    "name_ar": "chicken island",
                    "description": "super sauce, blue cheese, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "50",
                    "image": 2,
                    "category": 2,
                    "sizes": [
                        1,
                        2
                    ]
                },
                "extras": [
                    {
                        "id": 2,
                        "name": "extra2",
                        "name_ar": "chicken island",
                        "price": "8.0"
                    },
                    {
                        "id": 1,
                        "name": "extra1",
                        "name_ar": "chicken island",
                        "price": "15.0"
                    }
                ]
            },
            {
                "id": 85,
                "quantity": 8,
                "item_price": "20.00",
                "total_price": "344.00",
                "comments": null,
                "extras_price": "23.0",
                "size": {
                    "id": 1,
                    "name": "large",
                    "name_ar": "لارج"
                },
                "offer": null,
                "item": {
                    "id": 2,
                    "name": "super blue",
                    "name_ar": "chicken island",
                    "description": "super sauce, blue cheese, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "50",
                    "image": 2,
                    "category": 2,
                    "sizes": [
                        1,
                        2
                    ]
                },
                "extras": [
                    {
                        "id": 2,
                        "name": "extra2",
                        "name_ar": "chicken island",
                        "price": "8.0"
                    },
                    {
                        "id": 1,
                        "name": "extra1",
                        "name_ar": "chicken island",
                        "price": "15.0"
                    }
                ]
            }
        ]
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Add to cart
endpoint to add items to the cart
### Method: POST
>```
>localhost:8003/api/cart/add
>```
### Body (**raw**)

```json
{
    "offer_id": 2,
    "quantity": 8,
    "extras": [2,1]
}
```

### Response: 200
```json
{
    "message": "Item or offer added to cart",
    "cart": {
        "id": 3,
        "total_price": "344.00",
        "cart_items": [
            {
                "id": 87,
                "quantity": 8,
                "item_price": "20.00",
                "total_price": "344.00",
                "comments": null,
                "extras_price": "23.0",
                "size": {
                    "id": 1,
                    "name": "large",
                    "name_ar": "لارج"
                },
                "offer": null,
                "item": {
                    "id": 2,
                    "name": "super blue",
                    "name_ar": "chicken island",
                    "description": "super sauce, blue cheese, tomatoes, onion",
                    "description_ar": "قطعه البرجر المشويه يضاف اليها جبن الريكفورد الشهيه مع اوراق الجرجير الفريش و صوص سوبر المميز",
                    "active": true,
                    "score": "50",
                    "image": 2,
                    "category": 2,
                    "sizes": [
                        1,
                        2
                    ]
                },
                "extras": [
                    {
                        "id": 2,
                        "name": "extra2",
                        "name_ar": "chicken island",
                        "price": "8.0"
                    },
                    {
                        "id": 1,
                        "name": "extra1",
                        "name_ar": "chicken island",
                        "price": "15.0"
                    }
                ]
            }
        ]
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: remove item from cart
remove an item from cart
### Method: DELETE
>```
>localhost:8003/api/cart/87
>```
### Response: 200
```json
{
    "message": "Item removed from cart",
    "cart": {
        "id": 3,
        "total_price": "623.92",
        "cart_items": [
            {
                "id": 88,
                "quantity": 8,
                "item_price": "54.99",
                "total_price": "623.92",
                "comments": null,
                "extras_price": "23.0",
                "size": null,
                "offer": {
                    "id": 2,
                    "name": "offer",
                    "name_ar": "chicken island",
                    "description": "offer offer offer offer",
                    "description_ar": "offerof ferofferof ferofferoffer",
                    "price": "54.99",
                    "active": false,
                    "max_offer_items": 1,
                    "image": 15,
                    "menu_items": [
                        2,
                        3
                    ]
                },
                "item": null,
                "extras": [
                    {
                        "id": 2,
                        "name": "extra2",
                        "name_ar": "chicken island",
                        "price": "8.0"
                    },
                    {
                        "id": 1,
                        "name": "extra1",
                        "name_ar": "chicken island",
                        "price": "15.0"
                    }
                ]
            }
        ]
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: clear all cart
Clear all cart items and total
### Method: DELETE
>```
>localhost:8003/api/cart/clear
>```
### Response: 200
```json
{
    "message": "Cart cleared",
    "cart": {
        "id": 3,
        "total_price": "0.00",
        "cart_items": []
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: checkout
### Method: POST
>```
>http://localhost:8003/api/order-create
>```
### Body (**raw**)

```json
{
    "placed_order": {
        "delivery": true,
        "delivery_notes": "aaaaaaaaaaaaaaaaaaaaa",
        "delivery_address": 1
    },
    "order_items": [
        {
            "quantity": 2,
            "size": 1,
            "comments": "aaaaaaahhhhhhhhhhhhaaaa",
            "item_id": 1,
            "extras": [1,2]
        },
        {
            "quantity": 4,
            "offer_id": 1,
            "extras": [1,2]
        }
    ]
}
```

### Query Params

|Param|value|
|---|---|
|message|added|


### Response: 200
```json
{
    "message": "order and order items added Successfully!",
    "customer_email": "m.adaaaavvgaas@yaaah.com",
    "order_num": 57
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: refresh token
### Method: POST
>```
>http://127.0.0.1:8003/api/token/refresh/
>```
### Body (**raw**)

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNTI0MDI2OCwianRpIjoiNmU2MWJiOTU2ZGRmNDE2NGJhYmYyYTcxNGUzMWIxNTQiLCJ1c2VyX2lkIjoxfQ.hGUgIVBd07QsN-h2N6iG24CfEKQeKa-h5LaFY2YNCCg"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get current customer data
### Method: GET
>```
>http://127.0.0.1:8003/current-customer
>```
### Response: 200
```json
{
    "message": "Authenticated user's information",
    "user": {
        "id": 3,
        "addresses": [
            {
                "id": 3,
                "address": "SS",
                "area": {
                    "id": 1,
                    "area": "ssss",
                    "delivery_fees": "15.0"
                }
            }
        ],
        "email": "m.adaaaavvgaas@yaaah.com",
        "full_name": "firsat_name",
        "mobile_number": "01011565",
        "user": 3,
        "cart": 3
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get current customer orders
### Method: GET
>```
>http://127.0.0.1:8003/api/current-customer-orders
>```
### Response: 200
```json
{
    "orders": [
        {
            "id": 1,
            "delivery": true,
            "delivery_notes": "aaaaaaaaaaaaaaaaaaaaa",
            "total_price": "220.00",
            "delivery_address": 1,
            "customer": 3,
            "order_items": [
                {
                    "id": 1,
                    "item_price": "30.00",
                    "total_price": "60.00",
                    "quantity": 2,
                    "comments": "aaaaaaahhhhhhhhhhhhaaaa",
                    "extras_price": "0.0",
                    "size": 1,
                    "placed_order": 1,
                    "offer": null,
                    "item": 1,
                    "extras": []
                },
                {
                    "id": 2,
                    "item_price": "40.00",
                    "total_price": "160.00",
                    "quantity": 4,
                    "comments": null,
                    "extras_price": "0.0",
                    "size": null,
                    "placed_order": 1,
                    "offer": 1,
                    "item": null,
                    "extras": []
                }
            ],
            "status": 1
        },
        {
            "id": 2,
            "delivery": true,
            "delivery_notes": "aaaaaaaaaaaaaaaaaaaaa",
            "total_price": "220.00",
            "delivery_address": 1,
            "customer": 3,
            "order_items": [
                {
                    "id": 3,
                    "item_price": "30.00",
                    "total_price": "60.00",
                    "quantity": 2,
                    "comments": "aaaaaaahhhhhhhhhhhhaaaa",
                    "extras_price": "0.0",
                    "size": 1,
                    "placed_order": 2,
                    "offer": null,
                    "item": 1,
                    "extras": []
                },
                {
                    "id": 4,
                    "item_price": "40.00",
                    "total_price": "160.00",
                    "quantity": 4,
                    "comments": null,
                    "extras_price": "0.0",
                    "size": null,
                    "placed_order": 2,
                    "offer": 1,
                    "item": null,
                    "extras": []
                }
            ],
            "status": 1
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Admin 





# Note: 
### PostMan docs For Better readability
https://documenter.getpostman.com/view/13498731/2s9Xy5MqW6








## reset database data
```
 python manage.py flush
```