# Миграция базы данных с Alembic

## Подготовка к запуску

1. Создайте файл `.env` со следующими переменными:
```
db_login=postgres
db_password=postgres
db_name=lawly_db
db_host=db
db_port=5432
```

2. Убедитесь, что порт 5432 не занят или измените на свободный в файле `.env`

## Запуск с Docker

```bash
# Запуск базы данных и выполнение миграций
docker-compose up

# Запуск только миграций (если БД уже запущена)
docker-compose up migration
```

## Запуск без Docker

```bash
# Настройте переменные окружения
export db_login=postgres
export db_password=postgres
export db_name=lawly_db
export db_host=localhost
export db_port=5432

# Запустите миграцию
alembic upgrade head
```
