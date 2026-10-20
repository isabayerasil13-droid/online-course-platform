# OpenStudy — платформа онлайн-курсов

**Учебный Django-проект:** небольшой рабочий прототип платформы онлайн-курсов. Основная документация — **на русском**, есть [қазақша нұсқа](README_KK.md). Вдохновлён привычными каталогами курсов (например, Stepik/Udemy), но это самостоятельная учебная реализация, не копия.

## Что можно попробовать
- Просмотреть каталог из **6 демо-курсов** с локальными картинками вместо видеоплееров.
- Найти курс по названию/описанию и отфильтровать по категории.
- Открыть курс и прочитать текстовые уроки.
- Зарегистрироваться, войти, записаться на курс.
- Отметить пройденные уроки и посмотреть процент в **«Моё обучение»**.
- Добавить/изменить курсы и уроки через встроенную **Django admin**.

**Пока нет:** настоящего видео, оценок, тестов, оплаты, сертификатов и отдельной страницы преподавателя. Время работы прототипа — локальный сервер, публичный сайт не развёрнут.

## Запуск за несколько команд (Windows PowerShell)
```powershell
git clone https://github.com/isabayerasil13-droid/online-course-platform.git
cd online-course-platform
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py runserver
```
Открыть **http://127.0.0.1:8000/**. Сценарий для быстрого запуска на Windows: `start_demo.bat` (двойной щелчок). Создать администратора: `.\.venv\Scripts\python.exe manage.py createsuperuser`, затем открыть **http://127.0.0.1:8000/admin/**.

[Подробная инструкция на русском](docs/ru/07-demo.md) · [Қазақша іске қосу](docs/kk/07-demo.md)

## Структура
| Каталог / файл | Назначение |
|---|---|
| `config/` | Настройки Django, маршруты, подключение СУБД |
| `courses/models.py` | Course, Lesson, Enrollment, LessonProgress |
| `courses/views.py` | Каталог, поиск, запись, прогресс, регистрация |
| `courses/admin.py` | Интерфейс управления контентом |
| `courses/management/commands/seed_demo.py` | Создание шести демо-курсов |
| `templates/` | HTML-страницы |
| `static/courses/` | CSS и локальные SVG-картинки |
| `courses/tests.py` | Тесты базовых действий |

## Архитектура и база
**Целевая архитектура:** модульный монолит Django + PostgreSQL. Для лёгкой локальной демонстрации сейчас используется **SQLite**; PostgreSQL поддерживается настройками через `DB_NAME` и другие переменные среды + `requirements-postgres.txt`. Код MVP собран в одном Django-приложении `courses`, а полноценное разделение на отдельные модули — следующий этап, подробно описанный в ADR.

## Лабораторная — документация RU / KK
| Русский (основные документы) | Қазақша |
|---|---|
| [Идея и требования](docs/ru/01-requirements.md) | [Идея және талаптар](docs/kk/01-talaptar.md) |
| [Архитектура и оценка](docs/ru/02-architecture.md) | [Сәулет және бағалау](docs/kk/02-saulet.md) |
| [База данных](docs/ru/03-database.md) | [Дерекқор](docs/kk/03-derekqor.md) |
| [План разработки](docs/ru/04-roadmap.md) | [Жұмыс жоспары](docs/kk/04-zhospar.md) |
| [Как защитить проект](docs/ru/05-defense.md) | [Қорғау](docs/kk/05-qorgau.md) |
| [Командная работа](docs/ru/06-team.md) | [Команда](docs/kk/06-top.md) |
| [Как запустить и показать MVP](docs/ru/07-demo.md) | [MVP іске қосу](docs/kk/07-demo.md) |
| [ADR — архитектурное решение](docs/adr/0001-modular-monolith.ru.md) | [ADR — сәулеттік шешім](docs/adr/0001-modular-monolith.kk.md) |

Дополнительно: [Диаграммы](docs/DIAGRAMS.md) · [Состояние проекта](PROJECT_STATE.md) · [Правила командной работы](CONTRIBUTING.md).

> **Важно для защиты:** документация описывает целевую архитектуру, а код — сокращённый рабочий прототип. Не выдавайте нереализованные функции за готовые.
