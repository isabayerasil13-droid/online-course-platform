from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from courses import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.catalog, name="catalog"),
    path("course/<slug:slug>/", views.course_detail, name="course_detail"),
    path("course/<slug:slug>/enroll/", views.enroll, name="enroll"),
    path("lesson/<int:lesson_id>/complete/", views.toggle_lesson, name="toggle_lesson"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
