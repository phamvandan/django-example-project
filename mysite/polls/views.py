from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Question

def check_user(user):
    print('Check user information here')
    return True

def authen_and_login(request):
    # user = authenticate(request, username='nhanvien', password='')
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

@require_http_methods(['POST'])
def des(request, id):
    return HttpResponse('Your id=' + str(id))

def login_controller(request):
    return HttpResponse("Please Login")

def logout_controller(request):
    return HttpResponse("Logged Out")

def get_session_info(request):
    session = request.session
    # set session
    session['username'] = 'dan'
    session['password'] = '123'
    # get session
    session_info = ''
    session_info = session['username'] + session['password'] + 
    return HttpResponse(session_info)