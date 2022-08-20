from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from . import models

# Create your views here.
def index_page(request):
    print("request is accepted")
    return render(request, "main/index.html", {})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("main:profile_page"))

        return render(request, "main/login.html", {"error": "Неправильный логин/пароль"})
    return render(request, "main/login.html", {})

def helpdesk_page(request, pk):
    comments = models.Comment.objects.get(pk=pk)

    if request.method == "GET":
        return render(request, "main/helpdesk_page.html", {"comments": comments})
    else:
        author = request.POST.get("author", None)
        comment_text = request.POST.get("comment", None)
        models.Comment.objects.create(
            author=author,
            comment_text=comment_text,
        )

        return redirect(reverse("main:helpdesk_page", args=(pk,)))

def profile_page(request):
    """
    Контроллер, отвечающий за логику:
    - отображения профиля пользователя
    - изменения данных пользователя
    Пользователь должен быть аутентифицирован
    """

    if request.user.is_authenticated:
        # изменение данных пользователя при POST запросе
        if request.method == "POST":
            password = request.POST.get("password", None)
            first_name = request.POST.get("first_name", None)
            last_name = request.POST.get("last_name", None)

            user = request.user

            if password:
                user.set_password(password)

            if first_name:
                user.first_name = first_name

            if last_name:
                user.last_name = last_name

            user.save(update_fields=['password', 'first_name', 'last_name'])

            # если было изменение пароля, значит перенаправить на страницу аутентификации
            # так как сессия должна быть пересоздана
            if password:
                return redirect(reverse("main:login_page"))

            return redirect(reverse("main:profile_page"))

        # возвратить страницу профиля при GET запросе
        return render(request, "main/profile.html", {})
    return redirect(reverse("main:login_page"))


def logout_view(request):
    logout(request)
    return redirect(reverse("main:index_page"))


def register_page(request):
    if request.method == "POST":
        try:
            # QWErty123
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            email = request.POST.get("email", None)
            first_name = request.POST.get("first_name", None)
            last_name = request.POST.get("last_name", None)
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            return redirect(reverse("main:login_page"))
        except Exception as exc:
            print("при создании пользователя произошла ошибка", request.POST, exc)
            error = {
                "error_code": exc,
                "message": "Проверьте корректность введенных данных"
            }
            return render(request, "main/register.html", {"error": error})

    return render(request, "main/register.html", {})


def profile_delete_view(request):
    if request.user.is_authenticated:
        try:
            user = request.user
            user.delete()
            return redirect(reverse('main:index_page'))
        except Exception as exc:
            print(f"при удалении пользователя {request.user.pk} произошла ошибка", exc)
        return redirect(reverse('main:profile_page'))

    # Если пользователь не аутентифицирован, перенаправить на страницу логина
    return redirect(reverse('main:login_page'))

def drivers_page(request):
    return render(request, "main/drivers.html", {})

def drivers_application_page(request):
    return render(request, "main/drivers_application.html", {})

def passengers_page(request):
    return render(request, "main/passengers.html", {})

def helpdesk_page(request):
    return render(request, "main/helpdesk_page.html", {})