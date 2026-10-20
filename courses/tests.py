from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Course, Enrollment, Lesson, LessonProgress


class CourseFlowTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="student", password="StrongDemoPass123!")
        cls.other = User.objects.create_user(username="other", password="StrongDemoPass123!")
        cls.course = Course.objects.create(
            title="Python", slug="python-demo", description="Описание",
            instructor="Преподаватель", published=True,
        )
        cls.lesson = Lesson.objects.create(course=cls.course, title="Урок 1", summary="Учебный текст", position=1)

    def test_catalog_and_detail_are_public(self):
        self.assertContains(self.client.get(reverse("catalog")), "Python")
        self.assertContains(self.client.get(self.course.get_absolute_url()), "Урок 1")

    def test_enrollment_requires_login_and_post(self):
        url = reverse("enroll", args=[self.course.slug])
        self.assertEqual(self.client.get(url).status_code, 302)  # login_required
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(url).status_code, 405)
        self.client.post(url)
        self.assertEqual(Enrollment.objects.filter(user=self.user, course=self.course).count(), 1)
        self.client.post(url)
        self.assertEqual(Enrollment.objects.filter(user=self.user, course=self.course).count(), 1)

    def test_progress_requires_own_enrollment(self):
        Enrollment.objects.create(user=self.other, course=self.course)
        self.client.force_login(self.user)
        url = reverse("toggle_lesson", args=[self.lesson.id])
        self.assertEqual(self.client.post(url).status_code, 404)
        self.assertFalse(LessonProgress.objects.exists())
        Enrollment.objects.create(user=self.user, course=self.course)
        self.assertEqual(self.client.post(url).status_code, 302)
        self.assertEqual(LessonProgress.objects.count(), 1)
        self.assertContains(self.client.get(reverse("my_courses")), "100%")
        self.client.post(url)
        self.assertEqual(LessonProgress.objects.count(), 0)

    def test_unpublished_courses_hidden(self):
        self.course.published = False
        self.course.save()
        self.assertNotContains(self.client.get(reverse("catalog")), self.course.title)
        self.assertEqual(self.client.get(self.course.get_absolute_url()).status_code, 404)

    def test_registration(self):
        response = self.client.post(reverse("register"), {
            "username": "newstudent",
            "password1": "ValidDemoPassword321!",
            "password2": "ValidDemoPassword321!",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newstudent").exists())
