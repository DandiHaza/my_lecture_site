# courses/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "name", "email", "birth_date")
        labels = {
            'username': '사용자 아이디',
            'name': '이름',
            'email': '이메일 주소',
            'birth_date': '생년월일 (YYYY-MM-DD)',
        }