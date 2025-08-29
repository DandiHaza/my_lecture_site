# courses/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm # UserCreationForm 추가
from django.urls import reverse_lazy # reverse_lazy 추가
from django.views import generic # generic view 추가
from .models import Course
from django.shortcuts import redirect
from .models import Course, Enrollment

@login_required
def course_list(request):
    courses = Course.objects.all()
    # 아래 경로가 정확히 'courses/course_list.html' 인지 확인!
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()

    # 해당 강의에 속한 레슨들을 가져옵니다.
    lessons = course.lessons.all()

    context = {
        'course': course,
        'is_enrolled': is_enrolled,
        'lessons': lessons,  # 레슨 목록을 context에 추가!
    }
    return render(request, 'courses/course_detail.html', context)

@login_required # 로그인한 사용자만 수강 신청 가능
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # 이미 수강신청 했는지 확인. 안했다면 새로 생성.
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('course_detail', course_id=course.id) # 수강신청 후 상세페이지로 다시 돌아감

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # 회원가입 성공 시 로그인 페이지로 이동
    template_name = 'registration/signup.html'