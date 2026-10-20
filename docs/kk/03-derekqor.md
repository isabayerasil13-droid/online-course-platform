# 3. PostgreSQL, деректер моделі және Django ORM

## Таңдалған ДҚБЖ
**PostgreSQL** — реляциялық дерекқорды басқару жүйесі (ДҚБЖ). Платформада деректер тығыз байланысты: оқытушы → курстар, курс → сабақтар, сабақ → тапсырмалар, студент ↔ курстар, студент → жауаптар мен бағалар. PostgreSQL сыртқы кілттерді, транзакцияларды және тұтастық шектеулерін қолдайды.

- **Дерекқор** — сақталған ақпарат.
- **ДҚБЖ** — дерекқорды басқаратын бағдарлама.
- **PostgreSQL** — таңдалған реляциялық ДҚБЖ.
- **Django ORM** — Python модельдерінен SQL сұрауларын құратын құрал.

**SQLite** шағын прототиптерге ыңғайлы, бірақ файлдық БД топтық серверлік жүйеге қолайсыз. **MongoDB** құжаттық деректермен жұмыс істейді; көптеген өзара байланысқан кестелері бар бұл жобада PostgreSQL қолайлырақ. Нақты өнімділік салыстыруы жүргізілген жоқ.

## Алдын ала жобаланған кестелер
| Модель | Өрістер |
|---|---|
| `User` | id, username, email, password_hash (Django), role, created_at |
| `Category` | id, name |
| `Course` | id, title, description, teacher_id, category_id, created_at, is_published |
| `Lesson` | id, course_id, title, content, video_url, order |
| `Enrollment` | id, student_id, course_id, enrolled_at, status |
| `Assignment` | id, lesson_id, title, description, deadline, max_score |
| `Submission` | id, assignment_id, student_id, answer, submitted_at, score, feedback |
| `Progress` | id, student_id, lesson_id, completed, completed_at |

Пікірлер, түсіндірмелер, материалдар мен тесттердің егжей-тегжейлі схемасы келесі кезеңде нақтыланады.

## Байланыстар
- Бір оқытушыда көптеген курс бар: `User 1:N Course`.
- Бір санатта көп курс бар: `Category 1:N Course`.
- Бір курста көп сабақ бар: `Course 1:N Lesson`.
- Бір сабақта көп тапсырма бар: `Lesson 1:N Assignment`.
- Студенттер мен курстар арасында **көптен-көпке** байланыс бар; ол `Enrollment` аралық кестесі арқылы жүзеге асады.
- `Submission` студентті және тапсырманы; `Progress` студентті және сабақты байланыстырады.

## Жоспарланған деректер тұтастығы
`Enrollment` үшін `(student_id, course_id)`, `Progress` үшін `(student_id, lesson_id)` жұптарының бірегейлігі. Баға 0 мен тапсырмадағы максимал ұпайдың арасында болуы тиіс. Рөлдерге қолжетімділік Django деңгейінде тексеріледі.

## Django ORM мысалы (жобалық үлгі)
```python
from django.conf import settings
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

# Course.objects.filter(teacher=request.user)
```
Кейін `python manage.py makemigrations` және `python manage.py migrate` командалары орындалады. **Қазір нақты модельдер мен миграциялар жасалған жоқ.**

[ER диаграммасы](../DIAGRAMS.md).
