from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import RegistrationForm
from .models import Course, Enrollment, Lesson, LessonProgress


def catalog(request):
    courses = Course.objects.filter(published=True).prefetch_related("lessons")
    query = request.GET.get("q", "").strip()[:100]
    category = request.GET.get("category", "")
    if query:
        courses = courses.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if category in Course.Category.values:
        courses = courses.filter(category=category)
    return render(request, "courses/catalog.html", {
        "courses": courses,
        "query": query,
        "selected_category": category,
        "categories": Course.Category.choices,
    })


def course_detail(request, slug):
    course = get_object_or_404(Course.objects.prefetch_related("lessons"), slug=slug, published=True)
    enrollment = None
    done_ids = set()
    if request.user.is_authenticated:
        enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
        if enrollment:
            done_ids = set(enrollment.completed_lessons.values_list("lesson_id", flat=True))
    return render(request, "courses/detail.html", {
        "course": course,
        "enrollment": enrollment,
        "done_ids": done_ids,
    })


@login_required
@require_POST
def enroll(request, slug):
    course = get_object_or_404(Course, slug=slug, published=True)
    _enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, "Вы записались на курс. Можно начинать!")
    else:
        messages.info(request, "Вы уже записаны на этот курс.")
    return redirect(course.get_absolute_url())


@login_required
@require_POST
def toggle_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id, course__published=True)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=lesson.course)
    progress, created = LessonProgress.objects.get_or_create(enrollment=enrollment, lesson=lesson)
    if not created:
        progress.delete()
        messages.info(request, "Отметка о прохождении снята.")
    else:
        messages.success(request, "Урок отмечен как пройденный.")
    return redirect(lesson.course.get_absolute_url())


@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related("course").prefetch_related(
        "course__lessons", "completed_lessons"
    ).order_by("-enrolled_at")
    cards = []
    for enrollment in enrollments:
        total = len(enrollment.course.lessons.all())
        done = len(enrollment.completed_lessons.all())
        cards.append({"enrollment": enrollment, "done": done, "total": total, "percentage": round(100 * done / total) if total else 0})
    return render(request, "courses/my_courses.html", {"cards": cards})


def register(request):
    if request.user.is_authenticated:
        return redirect("my_courses")
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Аккаунт создан!")
        return redirect("catalog")
    return render(request, "registration/register.html", {"form": form})
