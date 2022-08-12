from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Question

def check_user(user):
    print('Check user information here')
    return True

def authen_and_login(request):
    # user = authenticate(request, username='nhanvien', password='phamvandan@5698')
    user = authenticate(request, username='dan', password='dan')
    if user is not None:
        login(request, user)
        return HttpResponse("welcome" + user.get_username())
    else:
        return HttpResponse("login failure")

@login_required
@user_passes_test(check_user)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# @login_required
@permission_required('polls.view_question', raise_exception=True)
def show_questions(request):
    print(Question.objects.all())
    return HttpResponse("Yeah, you have permission view question")

def des(request, id):
    return HttpResponse('Your id=' + str(id))

def login_controller(request):
    return HttpResponse("Please Login")

def logout_controller(request):
    return HttpResponse("Logged Out")