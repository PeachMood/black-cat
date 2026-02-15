# 🐈‍⬛ Black cat

Веб-приложение для распознавания изображений, сгенерированных искусственным интеллектом. Поможет умиляться фотографиям котят со спокойной душой.

![Иллюстрация к приложению](./project-image.png)

Проект выполнен в рамках курса: [ML-Engineering: от базы до AI-продукта](https://karpov.courses/ml-engineering).

## 🚀 Функциональность

- **Регистрация и авторизация** — создание аккаунта и безопасный вход в систему.
- **Управление балансом** — пополнение счёта, автоматическое списание за предсказания и просмотр истории транзакций.
- **Анализ изображений** — загрузка фотографий и их классификация.
- **История предсказаний** — просмотр всех предыдущих проверок с результатами.

## 💻 Модель

В основе приложения лежит предобученная модель [dima806/ai_vs_human_generated_image_detection](https://huggingface.co/dima806/ai_vs_human_generated_image_detection). Точность классификации составляет около 98%.

## 📁 Структура проекта

Проект реализован по принципам Clean Architecture, что обеспечивает гибкость, тестируемость и простоту поддержки.

### API Layer (/api)

Реализует взаимодействие с внешним миром через HTTP-интерфейс.

- `/routers` — роутеры FastAPI для эндпоинтов.
- `/schema` — Pydantic-схемы для валидации и сериализации данных.

### Domain Layer (/domain)

Содержит бизнес-логику и основные сущности приложения. Не зависит от других слоёв.

- `/models` — доменные модели.
- `/repositories` — интерфейсы для доступа к данным.
- `/services` — сервисы, реализующие бизнес-логику.

### Infrastructure Layer (/infrastructure)

Реализация взаимодействия с внешними сервисами и ресурсами.

- `/ai` — интеграция с моделью машинного обучения.
- `/database` — работа с базой данных.

## 🧰 Начало работы

### Требования

Перед началом убедитесь, что у вас установлены:

- [Docker](https://www.docker.com/products/docker-desktop/) (версия 20.10 или выше)
- Docker Compose (версия 2.0 или выше)

### Быстрый старт

#### 1. Клонирование репозитория

```bash
git clone https://github.com/PeachMood/black-cat.git
cd black-cat
```

#### 2. Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта:

Windows (PowerShell/CMD):

```bash
copy .env.template .env
```

macOS/Linux (bash/zsh):

```bash
cp .env.template .env
```

Отредактируйте `.env` и задайте свои значения:

```text
# Backend
PROJECT_NAME=Black Cat API
API_VERSION=0.0.1
DEBUG=False

# Postgres
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=
POSTGRES_DB=postgres_db
POSTGRES_PORT=5432

# RabbitMQ
RABBITMQ_USER=rabbitmq_user
RABBITMQ_PASSWORD=
RABBITMQ_VHOST=/
```

#### 3. Запуск проекта

Запуск (сборка образов при необходимости):

```bash
docker compose up --build -d
```

Проверить, что сервисы поднялись:

```bash
docker compose ps
```

#### 4. Остановка проекта

```bash
docker compose down
```

### Доступ к сервисам

После успешного запуска сервисы будут доступны по следующим адресам:

#### Nginx (прокси)

- HTTP: http://localhost

#### Backend (через Nginx)

- Health check: http://localhost/health
- Документация API: http://localhost/docs

#### RabbitMQ

- Веб-интерфейс: http://localhost:15672
- AMQP порт: localhost:5672 (для подключения приложений)
