# 7. MVP іске қосу және көрсету

## Жасалған мүмкіндіктер
Django негізіндегі **OpenStudy** прототипі: 6 үлгі курс, іздеу мен санаттар, жергілікті суреті бар курс карточкасы, бейнесіз мәтіндік сабақтар, тіркелу және жүйеге кіру, курсқа жазылу, сабақтың аяқталғанын белгілеу, «Менің оқуым» бетіндегі прогресс пайызы және Django әкімші панелі.

**Жоқ:** нақты бейне, файл жүктеу, тесттер мен бағалар, төлем, оқытушының бөлек интерфейсі, сертификаттар, жалпыға ортақ хостинг.

## Windows-та іске қосу (PowerShell)
```powershell
git clone https://github.com/isabayerasil13-droid/online-course-platform.git
cd online-course-platform
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py runserver
```
Python 3.10+ басқа нұсқасы болса, `py -3.13` орнына `py` қолдануға болады. Браузерде **http://127.0.0.1:8000/** ашыңыз.

Әкімші жасау:
```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```
Әкімші панелі: **http://127.0.0.1:8000/admin/**.

## Командаға қалай көрсету керек?
1. Басты беттегі алты курс, іздеу және санат бойынша сүзгі.
2. Курсты ашу: ▶ белгісі бар сурет — **бейне емес**, тек көрнекі үлгі.
3. Тіркелу/жүйеге кіру және курсқа жазылу.
4. Сабақтағы «Отметить ✓» батырмасымен аяқталғанын белгілеу.
5. «Моё обучение» бетінде пайыздық прогресті көрсету.
6. Әкімші панелінде курс пен сабақтарды қосу/өзгерту.

## Жоба құрылымы
`config/` — параметрлер мен URL; `courses/models.py` — Course, Lesson, Enrollment, LessonProgress; `courses/views.py` — логика; `templates/` — HTML; `static/courses/` — дизайн және суреттер; `seed_demo.py` — үлгі деректер; `courses/tests.py` — автоматты тексерулер.

## Дерекқор
Жылдам демонстрация үшін **SQLite** қолданылады. Сәулеттік мақсат — **PostgreSQL**. Оған көшу үшін `requirements-postgres.txt` орнатып, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` айнымалыларын баптап, миграцияларды іске қосу керек; SQLite ішіндегі ақпарат автоматты түрде көшпейді.

Тексеру:
```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
```

Бұл — тек жергілікті оқу прототипі, **дайын production жүйесі емес**.
