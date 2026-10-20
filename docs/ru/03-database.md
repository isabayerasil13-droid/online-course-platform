# 3. PostgreSQL, модель данных и Django ORM

## Выбранная СУБД
**PostgreSQL** — реляционная система управления базами данных. Данные проекта связаны: преподаватель → курсы, курс → уроки, урок → задания, студент ↔ курсы, студент → ответы и оценки. PostgreSQL поддерживает внешние ключи, ограничения целостности, транзакции и запросы по отношениям.

- **База данных** — хранимая информация.
- **СУБД** — программное обеспечение, управляющее базой.
- **PostgreSQL** — наша СУБД.
- **Django ORM** — слой, формирующий SQL-запросы из Python-моделей.

### Сравнение
**SQLite:** подходит для простых прототипов и локальных упражнений, но общий файл БД неудобен для командного/серверного окружения.
**MongoDB:** документная БД; для многочисленных реляционных связей этого проекта PostgreSQL естественнее.
Выбор основан на структуре данных и учебной инфраструктуре; сравнительных бенчмарков не было.

## Предварительные сущности
Схема концептуальная: названия/типы окончательно закрепим при создании Django-моделей.

| Сущность | Поля |
|---|---|
| `User` | id, username, email, password_hash (Django), role, created_at |
| `Category` | id, name |
| `Course` | id, title, description, teacher_id, category_id, created_at, is_published |
| `Lesson` | id, course_id, title, content, video_url, order |
| `Enrollment` | id, student_id, course_id, enrolled_at, status |
| `Assignment` | id, lesson_id, title, description, deadline, max_score |
| `Submission` | id, assignment_id, student_id, answer, submitted_at, score, feedback |
| `Progress` | id, student_id, lesson_id, completed, completed_at |

Из исходного задания также запланированы `Review`, комментарии, материалы и тесты, но их подробная схема пока не зафиксирована.

## Связи
- `User (teacher) 1:N Course`.
- `Category 1:N Course`.
- `Course 1:N Lesson`.
- `Lesson 1:N Assignment`.
- `User (student) N:M Course` через `Enrollment`.
- `User (student) 1:N Submission`; `Assignment 1:N Submission`.
- `User (student) 1:N Progress`; `Lesson 1:N Progress`.

## Правила целостности (предлагается)
- Уникальность пары `(student_id, course_id)` в Enrollment.
- Уникальность пары `(student_id, lesson_id)` в Progress.
- Проверка `0 <= score <= max_score` на уровне валидации/БД после уточнения модели.
- Индексы для внешних ключей и частых запросов.
- Разграничение ролей и прав на уровне Django.
- Использовать кастомную модель пользователя с самого начала, если проекту требуется поле роли.

## Django ORM — учебный пример
```python
from django.conf import settings
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

# Пример запроса:
# Course.objects.filter(teacher=request.user)
```

В будущем команды `python manage.py makemigrations` и `python manage.py migrate` создадут таблицы в настроенной БД. **Сейчас ни модели, ни миграции не выполнялись.**

[ER-диаграмма](../DIAGRAMS.md).
