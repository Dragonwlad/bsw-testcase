# BSW Testcase

Проект `BSW Testcase` представляет собой сервис для управления ставками и событиями, используя PostgreSQL и RabbitMQ для обмена данными. Этот проект построен на FastAPI и включает микросервисы, взаимодействующие через асинхронные HTTP и очереди сообщений.

## Содержание

- [Описание](#описание)
- [Технологии](#технологии)
- [Установка](#установка)
- [Переменные окружения](#переменные-окружения)
- [Запуск приложения](#запуск-приложения)
- [API Эндпоинты](#api-эндпоинты)
- [Автор](#автор)

## Описание

Проект реализует API для управления ставками на события, которые передаются и обрабатываются через очередь сообщений RabbitMQ. Проект поддерживает создание, валидацию и хранение данных о ставках и событиях, что позволяет легко интегрировать этот функционал в другие приложения или интерфейсы.

## Технологии

- **Python 3.10**
- **FastAPI** — для создания API
- **PostgreSQL** — для хранения данных
- **RabbitMQ** — для обмена сообщениями между сервисами
- **Docker и Docker Compose** — для контейнеризации
- **Pydantic** — для валидации данных
- **Aiohttp** — для асинхронного HTTP-клиента

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone git@github.com:Dragonwlad/bsw-testcase.git
   cd bsw-testcase

	2.	Убедитесь, что у вас установлены Docker и Docker Compose.
	3.	Создайте файл .env в корневой директории и добавьте необходимые переменные окружения (см. ниже).

Переменные окружения

Создайте файл .env в корневой директории проекта по шаблону .env.example

Запуск приложения

Для запуска всех сервисов выполните команду:

docker-compose up --build

Это развернет контейнеры для всех сервисов, включая PostgreSQL, RabbitMQ и микросервисы line-provider и bet-maker.

Доступ к сервисам

	•	RabbitMQ Management — http://localhost:15672
	•	line-provider API — http://localhost:8080/docs
	•	bet-maker API — http://localhost:8000/docs

API Эндпоинты

Некоторые основные эндпоинты:

Line Provider

	•	GET /events — Получить список доступных событий

Bet Maker

	•	POST /bet — Создать ставку на событие

Более подробная документация доступна по адресу /docs для каждого сервиса, где можно тестировать эндпоинты через Swagger UI.

Автор

Этот проект создан и поддерживается Dragonwlad.
