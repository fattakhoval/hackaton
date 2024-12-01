# hackaton-front

## Запуск проекта через docker-compose

Для начала нужно переименовать файлы:
 - example.env -> .env
 - pg.example.env -> pg.env

И указать в них нужные данные для запуска проета

Устанавливает dokcer, docker-compose

Пишем команду в консоль (если у вас linux)

```shell
sudo docker compose up --build 
```
в зависимости от версии docker команда может быть другой
```shell
sudo docker-compose up --build 
```

Ждем-с пока проект соберется

После можно переходить по ссылке "http://localhost:3000"
