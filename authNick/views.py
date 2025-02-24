from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect

from authNick.models import Users
from polls.models import Question, Choice

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


def secretQuiz(request):
    user = request.user  # Отримуємо користувача

    if not user.is_authenticated:
        return redirect("welcome")  # Якщо не залогінений — перенаправити на логін

    if not user.current_question:  # Якщо у користувача немає поточного питання
        user.current_question = Question.objects.first()  # Призначити перше питання
        user.save()

    # Отримуємо варіанти відповіді для поточного питання
    choices = user.current_question.choices.all()

    return render(request, "auth/secretQuiz.html", {
        "latest_question": user.current_question,
        "choices": choices
    })

def check_answer(request):
    """Перевіряє відповідь і переходить до наступного питання"""
    if request.method == "POST":
        user = request.user  # Поточний користувач
        choice_id = request.POST.get("choice_id")
        choice = get_object_or_404(Choice, id=choice_id)

        if choice.is_correct:
            next_question = Question.objects.filter(id__gt=user.current_question.id).order_by('id').first()
            if next_question:
                user.current_question = next_question  # Переходимо до наступного питання
            else:
                user.current_question = None  # Вікторина завершена
            user.save()

        return JsonResponse({"correct": choice.is_correct})


from django.contrib.auth import login

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
        user = Users.objects.create(username=nickname)

        # Авторизуємо користувача
        login(request, user)

        # Перенаправляємо на quiz
        return redirect('selectQuiz')  # Перенаправити на quiz після успішної авторизації


def selectQuiz(request):
    return render(request, "auth/selectQuiz.html")