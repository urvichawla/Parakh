from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

def Welcome(request):
    return render(request, 'welcome.html')

def StudentPage(request):
    return render(request, 'student_page.html')

def StudentSignup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            return HttpResponse("Your Password and Confirm Password are not same")
        else:
            my_user=User.objects.create_user(uname, email, pass1)
            # return HttpResponse("User has been Created Successfully.")
            my_user.save()
            return redirect('student_login')
            

            # print(uname, firstname, lastname, email, pass1, pass2)

    return render(request, 'student_signup.html')

def StudentLogin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('student_board')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'student_signin.html')

def ForgotDetails(request):
    return render(request, 'forgot_credentials.html')

def LoginAdmin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_board')
    return render(request, 'admin_login.html')

def StudentLogout(request):
    logout(request)
    return redirect('welcome')

def AdminLogout(request):
    logout(request)
    return redirect('welcome')

@login_required(login_url='student_login')
def StudentBoard(request):
    return render(request, 'student_board.html')

def StudPerformanceAnalysis(request):
    return render(request, 'student_performance_analysis.html')

def StudReport(request):
    return render(request, 'student_report.html')

def StudAccount(request):
    return render(request, 'student_account.html')

def StudExam(request):
    catData=models.QuizCategory.objects.all()
    return render(request, 'student_exam.html',{'data':catData})

@login_required
def StudexamMcq(request, cat_id):
    category=models.QuizCategory.objects.get(id=cat_id)
    questions=models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'exam_mcq.html', {'question':questions, 'category':category})

def ExamPreAssement(request):
    return render(request, 'exam_pre_assement.html')

def ExamMcq(request):
    return render(request, 'exam_mcq.html')

@login_required(login_url='admin_login')
def AdminBoard(request):
    return render(request, 'admin_board.html')

def AdminStudent(request):
    return render(request, '#')

def AdminQuestionBank(request):
    return render(request, '#')

def AdminPerformanceAnalysis(request):
    return render(request, '#')

def AdminReports(request):
    return render(request, '#')

def AdminAccount(request):
    return render(request, '#')