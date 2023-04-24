# Parser Shop
Парсер дял веб сайтов

## 1. Установка Docker

Сборка образа:
```
sudo docker build . -t parser-shop:latest
```

Запуск контейнера:
```
sudo docker run -d -t parser-dns -p 8000:8000 parser-shop:latest
```

Зависимоть Selenium, необходим запушенный контейнер образа:
```
sudo docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.8.3-20230404
```

Адрес сервера:
```
http://127.0.0.1:8000
```

Swagger документация:
```
http://127.0.0.1:8000/docs
```

## 2. Установка Docker Compose

Сборка образа и запуск контейнеров с зависимостями:
```
sudo docker compose up -d
```

## 3. Использование

Сделать пост запрос:
```
POST на адрес http://127.0.0.1:8000/get_spec_dns
```

В JSON формате передать входные данные:

```json
[
    {
        "guid": "url"
    },
    {
        "guid": "url"
    },
    {
        "guid": "url"
    }
]
```

Пример:
```json
[
    {
        "4b652aa5-4533-4bc6-b35e-ba7aaba0847d": "https://www.dns-shop.ru/product/4e71cda93012ed20/67-smartfon-apple-iphone-14-pro-max-256-gb-fioletovyj"
    },
    {
        "3d71f39a-7bd3-436f-bd65-e38115fc3dfb": "https://www.dns-shop.ru/product/86910e9ae860ed20/133-noutbuk-apple-macbook-air-seryj/"
    },
    {
        "331759d2-02a8-4387-b315-95b1eaa67afb": "https://www.dns-shop.ru/product/863fb6e721d5ed20/5-smartfon-itel-a25-16-gb-biruzovyj/characteristics/"
    }
]
```

Примечание: 
```
    Ссылка может быть принята с "/characteristics/" так и без 
```

Выходные данные:

```json
{
    "4b652aa5-4533-4bc6-b35e-ba7aaba0847d": [
        {
            "key": "Гарантия от продавца",
            "value": "12 мес."
        },
        {
            "key": "Страна-производитель",
            "value": "Китай"
        },
        {
            "key": "Тип",
            "value": "смартфон"
        }
    ],
    "3d71f39a-7bd3-436f-bd65-e38115fc3dfb": [
        {
            "key": "Гарантия от продавца",
            "value": "12 мес."
        },
        {
            "key": "Страна-производитель",
            "value": "Китай"
        },
        {
            "key": "Тип",
            "value": "ноутбук"
        },
        {
            "key": "Модель",
            "value": "Apple MacBook Air"
        }
    ]
}
```
