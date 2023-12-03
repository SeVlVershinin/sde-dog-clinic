# Бэкенд-сервис "Клиника для собак" 
Сервис "Клиника для собак", ДЗ по предмету "Основы разработки", МОВС2023

Автор: Сергей Вершинин

## Описание задачи
К нам обратился директор ветеринарной клиники и сказал: "Клинике необходим микросервис для 
хранения и обновления информации для собак!" Директор пообщался с IT-отделом, и они сверстали 
документацию в [формате OpenAPI](https://github.com/SeVlVershinin/sde-dog-clinic/blob/main/clinic.yaml)

Используя FatAPI, необходимо разработать сервис, реализующий описанный API.

## Результаты работы

Сервис упакован в **Docker-образ** и развернут по адресам: 
- http://94.139.242.35/ - развернут на собственном виртуальный сервер
- https://dog-clinic-uxbb.onrender.com (резервный) - развернут на render.com

Образ также [загружен](https://hub.docker.com/repository/docker/sevlvershinin/sde-dog-clinic/general) на Docker Hub
и может быть запущен на машине с установленным Docker c помощью команды:
```
 docker run -p 80:80 sevlvershinin/sde-dog-clinic
```

**Код сервиса** находится в данном репозитории и включает: 
- [app/main.py](https://github.com/SeVlVershinin/sde-dog-clinic/blob/main/app/main.py) - реализация API endpoints
- [data/models.py](https://github.com/SeVlVershinin/sde-dog-clinic/blob/main/data/models.py) - классы данных, с которыми работает сервис
- [data/repositories.py](https://github.com/SeVlVershinin/sde-dog-clinic/blob/main/data/repositories.py) - классы *репозиториев*, реализующих работу с хранимыми данными
- [data/test_dog_repo.py](https://github.com/SeVlVershinin/sde-dog-clinic/blob/main/data/test_dog_repo.py) - *unit-тесты* репозитория собак

## Дополнения
Для проверки соответствия реализованного сервиса исходному описанию в формате OpenAPI было получено OpenAPI описание реализованного сервиса, 
формируемые компонентами FastAPI, формате JSON. JSON был сконвертирован в формат YAML, после чего полученный YAML был сравнен с 
исходным YAML-описанием clinic.yaml. Содержательно различий в описании не было (были три мелких отличия, 
не влияющих на содержание API и связанные, скорее всего, с различиями в использовании средств генерации описания)




