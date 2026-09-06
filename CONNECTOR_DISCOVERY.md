# Docebo Connector — Discovery & Vendor API Specification

**Официальный сайт:** https://www.docebo.com  
**Базовый эндпоинт API:** `https://<tenant>.docebosaas.com/learn/v1`  
**Схема авторизации:** OAuth 2.0 Bearer Token (Authorization Code / Client Credentials)

## Поддерживаемые сущности API
- курсы (/courses)
- пользователи (/users)
- зачисления на курсы (/enrollments)
- планы обучения (/learningplans)

## Архитектурные требования
- Использование безопасного клиента с контролем таймаутов, повторных попыток (backoff) и обработкой rate limit.
- Валидация входных данных через Pydantic-схемы без утечки чувствительных полей в логи.
- Тестовая точка проверки подключения: `GET /learn/v1/courses`.
