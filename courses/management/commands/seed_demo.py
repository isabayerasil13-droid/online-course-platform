from django.core.management.base import BaseCommand
from courses.models import Course, Lesson


SAMPLES = [
    ("python-start", "Python с нуля", "Первые шаги: переменные, условия и циклы. Всё простыми словами.", "programming", "beginner", "Александр Иванов", "courses/images/python.svg", 6, [
        ("Знакомство с Python", "Python — язык программирования общего назначения. Здесь мы изучаем, где он применяется и как запустить первый скрипт."),
        ("Переменные и типы", "Переменные хранят значения. Примеры: name = 'Анна', age = 18. Типы: int, str, bool."),
        ("Условия и циклы", "if помогает выбирать действие, а for повторяет операции. Попробуйте придумать собственный пример."),
    ]),
    ("web-development", "Основы веб-разработки", "HTML, CSS и немного JavaScript для первых сайтов.", "programming", "beginner", "Елена Ким", "courses/images/web.svg", 8, [
        ("Из чего состоит сайт", "HTML задаёт структуру, CSS отвечает за внешний вид, JavaScript добавляет поведение."),
        ("Страница на HTML", "Изучите теги h1, p, a и img. Сделайте простую страницу о себе."),
        ("Стили CSS", "Измените шрифт, цвет и отступы, попробуйте flexbox."),
    ]),
    ("ui-design", "UI-дизайн для начинающих", "Композиция, цвет и интерфейсы без сложной теории.", "design", "beginner", "Мария Алексеева", "courses/images/design.svg", 5, [
        ("Что такое UI", "UI — визуальная часть интерфейса: кнопки, карточки, текст и элементы управления."),
        ("Цвет и типографика", "Ограничьте палитру, создайте понятную иерархию заголовков."),
        ("Карточка курса", "Нарисуйте карточку с названием, изображением и кнопкой."),
    ]),
    ("marketing-basic", "Интернет-маркетинг", "Как находить аудиторию и рассказывать о продукте.", "business", "beginner", "Даниил Орлов", "courses/images/marketing.svg", 4, [
        ("Целевая аудитория", "Опишите, кому нужен ваш продукт и какую проблему он решает."),
        ("Основы продвижения", "Разберитесь, чем отличаются реклама, SEO и органические публикации."),
    ]),
    ("data-basics", "Данные и аналитика", "Таблицы, графики и первые полезные выводы.", "programming", "intermediate", "Наталья Пак", "courses/images/data.svg", 7, [
        ("Зачем анализировать данные", "Собираем данные, очищаем, сравниваем и делаем выводы."),
        ("Простые метрики", "Среднее, минимум, максимум. Подумайте, что лучше отражает результат."),
        ("Понятные диаграммы", "Выбирайте тип диаграммы под вопрос: сравнение, тренд или состав."),
    ]),
    ("productivity", "Личная продуктивность", "Планирование учёбы и простые привычки.", "other", "beginner", "Алина Сергеева", "courses/images/productivity.svg", 3, [
        ("План на неделю", "Разделите большую задачу на небольшие шаги и установите реальные сроки."),
        ("Приоритеты", "Выберите три главных дела и начните с самого важного."),
    ]),
]


class Command(BaseCommand):
    help = "Создать 6 демонстрационных курсов и их текстовые уроки (повторный запуск безопасен)."

    def handle(self, *args, **options):
        added = 0
        for slug, title, description, category, level, instructor, image, hours, lessons in SAMPLES:
            course, created = Course.objects.get_or_create(slug=slug, defaults={
                "title": title, "description": description, "category": category,
                "level": level, "instructor": instructor, "image": image,
                "duration_hours": hours, "published": True,
            })
            if created:
                added += 1
            for position, (lesson_title, summary) in enumerate(lessons, 1):
                Lesson.objects.get_or_create(course=course, position=position, defaults={
                    "title": lesson_title, "summary": summary,
                })
        self.stdout.write(self.style.SUCCESS(f"Демо готово. Новых курсов: {added}. Всего: {Course.objects.count()}"))
