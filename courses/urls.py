# courses/urls.py
from django.urls import path
from . import views
from .views import course_list, course_detail, SignUpView

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('payment/verify/', views.payment_verify, name='payment_verify'),
    path('my-courses/', views.my_courses, name='my_courses'),
]