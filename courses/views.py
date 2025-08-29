# courses/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm # UserCreationForm 추가
from django.urls import reverse_lazy # reverse_lazy 추가
from django.views import generic # generic view 추가
from .models import Course
from django.shortcuts import redirect
from .models import Course, Enrollment
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm

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


@login_required
@csrf_exempt  # CSRF 보호를 임시로 비활성화 (실제 서비스에서는 다른 방식 사용)
def payment_verify(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        imp_uid = data.get('imp_uid')
        course_id = data.get('course_id')

        # 여기에 포트원 API를 호출해서 실제 결제 금액을 확인하는 로직이 들어갑니다.
        # 지금은 일단 성공했다고 가정하고 넘어갑니다.

        course = get_object_or_404(Course, pk=course_id)
        Enrollment.objects.get_or_create(student=request.user, course=course)

        return JsonResponse({'status': 'success', 'message': '결제가 확인되었습니다.'})

    return JsonResponse({'status': 'error', 'message': '잘못된 요청입니다.'}, status=400)

@login_required # 당연히 로그인한 사용자만 볼 수 있어야 합니다.
def my_courses(request):
    # 현재 로그인한 유저가 수강신청한 Enrollment 기록들을 모두 가져옵니다.
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm # 이 부분을 수정!
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'