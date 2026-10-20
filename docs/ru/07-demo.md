# 7. Быстрый запуск и показ MVP

## Что сделано
Рабочий прототип **OpenStudy** на Django: каталог из шести примеров, поиск и категории, карточки курса с локальной картинкой-заглушкой, описания текстовых уроков, регистрация и вход, запись на курс, отметки прохождения и процент прогресса в «Моём обучении», админ-панель для добавления курсов и уроков.

**Не реализовано:** видео, загрузки файлов, реальные тесты, оценки, платежи, отдельный интерфейс преподавателя, сертификаты и публичный хостинг.

## Запуск на Windows (PowerShell)
```powershell
git clone https://github.com/isabayerasil13-droid/online-course-platform.git
cd online-course-platform
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py runserver
```
Если у вас другая версия Python 3.10+, замените `py -3.13` на `py`.
Откройте **http://127.0.0.1:8000/**.

Для доступа к Django admin (управление курсами) в отдельном терминале создайте администратора:
```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```
После этого войдите на **http://127.0.0.1:8000/admin/**.

## На macOS/Linux
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py seed_demo
.venv/bin/python manage.py runserver
```

## Как показать преподавателю/команде
1. Главная: 6 курсов с локальными иллюстрациями, фильтр и поиск.
2. Откройте курс: обложка с значком ▶ — **это заглушка, не видео**; ниже текстовые уроки.
3. Зарегистрируйтесь или войдите.
4. Нажмите «Записаться на курс».
5. Нажмите «Отметить ✓» на одном уроке.
6. В «Моё обучение» посмотрите процент выполнения.
7. Войдите в `/admin/` под суперпользователем и покажите добавление/редактирование курса и уроков.

## Как устроено
- `config/` — настройки, маршруты и подключение базы.
- `courses/models.py` — 4 модели: Course, Lesson, Enrollment, LessonProgress.
- `courses/views.py` — поиск, каталог, запись, прогресс, регистрация.
- `templates/` — HTML-страницы.
- `static/courses/` — оформление и картинки-заглушки.
- `courses/management/commands/seed_demo.py` — 6 примеров.
- `courses/tests.py` — автоматические тесты основных сценариев.

## SQLite или PostgreSQL?
Для мгновенного локального запуска используется **SQLite** (файл `db.sqlite3`, который не коммитится). В проекте **предусмотрен PostgreSQL**: установите `requirements-postgres.txt`, задайте переменные `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` и выполните миграции. Это смена СУБД для отдельной БД: данные из SQLite автоматически не переносятся.

## Проверка
```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
```

> Демонстрационная версия рассчитана на локальную разработку, **не на production**. Для публикации нужно добавить безопасную конфигурацию, сервер, домен и обеспечить постоянное хранение БД.
