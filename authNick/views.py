from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from authNick.models import Users


def welcome_view(request):
    if request.method == "GET":
        return render(request, 'auth/start.html')

    elif request.method == "POST":
        nickname = request.POST.get("nickname")

        # Перевіряємо, чи існують користувачі з таким ім'ям
        existing_users = Users.objects.filter(username=nickname)

        # Видаляємо всіх користувачів без паролю
        if existing_users.exists():
            for user in existing_users:
                if not user.password:
                    user.delete()  # Видаляємо користувача без паролю

        # Створюємо нового користувача
        Users.objects.create(username=nickname)

    return render(request, 'auth/selectQuiz.html')