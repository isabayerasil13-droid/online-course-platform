from django.conf import settings
from django.db import models
from django.urls import reverse


class Course(models.Model):
    class Category(models.TextChoices):
        PROGRAMMING = "programming", "Программирование"
        DESIGN = "design", "Дизайн"
        BUSINESS = "business", "Маркетинг и бизнес"
        OTHER = "other", "Другое"

    class Level(models.TextChoices):
        BEGINNER = "beginner", "Начальный"
        INTERMEDIATE = "intermediate", "Средний"
        ADVANCED = "advanced", "Продвинутый"

    title = models.CharField("Название", max_length=160)
    slug = models.SlugField("Адрес", unique=True)
    description = models.TextField("Описание")
    category = models.CharField("Категория", max_length=20, choices=Category.choices, default=Category.OTHER)
    level = models.CharField("Уровень", max_length=20, choices=Level.choices, default=Level.BEGINNER)
    instructor = models.CharField("Автор", max_length=120)
    image = models.CharField("Путь к картинке (static)", max_length=150, default="courses/images/python.svg")
    duration_hours = models.PositiveSmallIntegerField("Часов", default=4)
    published = models.BooleanField("Опубликовано", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс")
    title = models.CharField("Название", max_length=160)
    summary = models.TextField("Содержание")
    position = models.PositiveSmallIntegerField("Порядок", default=1)

    class Meta:
        ordering = ["position", "id"]
        constraints = [models.UniqueConstraint(fields=["course", "position"], name="unique_lesson_position")]
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.course.title}: {self.title}"


class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="course_enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "course"], name="unique_course_enrollment")]
        verbose_name = "Запись на курс"
        verbose_name_plural = "Записи на курсы"

    def __str__(self):
        return f"{self.user} -> {self.course}"


class LessonProgress(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="completed_lessons")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["enrollment", "lesson"], name="unique_completed_lesson")]
        verbose_name = "Пройденный урок"
        verbose_name_plural = "Пройденные уроки"

    def __str__(self):
        return f"{self.enrollment}: {self.lesson.title}"
