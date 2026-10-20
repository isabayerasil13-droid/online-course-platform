# OpenStudy — онлайн курстар платформасы

Оқу жобасының шағын **жұмыс істейтін Django прототипі**. Негізгі құжаттама — [орысша README](README.md), бұл — қазақша нұсқа. Жоба таныс курс каталогтарының жалпы идеясын пайдаланады, бірақ дербес оқу прототипі.

## Қазір не жұмыс істейді?
- Жергілікті суреттері бар **6 демо-курс** (бейне емес).
- Іздеу және санат бойынша сүзгі.
- Курстың сипаттамасы және мәтіндік сабақтар.
- Тіркелу, жүйеге кіру, курсқа жазылу.
- Сабақты аяқталды деп белгілеу және оқу пайызы.
- Django әкімші панелінде курстар мен сабақтарды өзгерту.

**Әлі жоқ:** нақты видео, тесттер, бағалар, төлемдер, сертификаттар, оқытушының бөлек панелі және ашық хостинг.

## Windows-та іске қосу
```powershell
git clone https://github.com/isabayerasil13-droid/online-course-platform.git
cd online-course-platform
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py runserver
```
Сайт: **http://127.0.0.1:8000/**. Жеңіл іске қосу үшін `start_demo.bat` файлын ашыңыз. Әкімші жасау: `.\.venv\Scripts\python.exe manage.py createsuperuser`; әкімші панелі: **http://127.0.0.1:8000/admin/**.

## Жобаның құрылымы
- `config/` — Django конфигурациясы және дерекқорды қосу.
- `courses/models.py` — Course, Lesson, Enrollment, LessonProgress.
- `courses/views.py` — іздеу, тіркелу, курсқа жазылу, оқу барысы.
- `templates/` — сайт беттері.
- `static/courses/` — CSS және суреттер.
- `seed_demo.py` — бастапқы деректер.
- `courses/tests.py` — автоматты тесттер.

**Мақсатты сәулет:** Django модульдік монолиті және PostgreSQL. Жылдам жергілікті демонстрация үшін **SQLite** пайдаланылады; `DB_NAME` және тиісті айнымалылар арқылы PostgreSQL қосуға болады. Қазіргі кодта бір `courses` қолданбасы бар; жеке Django модульдеріне бөлу келесі кезеңде жоспарланған.

## Құжаттар
[Талаптар](docs/kk/01-talaptar.md) · [Сәулет](docs/kk/02-saulet.md) · [Дерекқор](docs/kk/03-derekqor.md) · [Жоспар](docs/kk/04-zhospar.md) · [Қорғау](docs/kk/05-qorgau.md) · [Командалық жұмыс](docs/kk/06-top.md) · [Іске қосу](docs/kk/07-demo.md) · [ADR](docs/adr/0001-modular-monolith.kk.md).

> Құжаттама толық жүйенің жоспарын, ал ағымдағы код қысқартылған прототипті көрсетеді.
