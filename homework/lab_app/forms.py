from django import forms
from lab_app.models import Review, Film
from django.contrib.auth.models import User


# Форма регистрации
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'awaiting'}
            ),
        }


# Форма авторизации
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'awaiting'}
            ),
        }


# Форма добавления продукта
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Film
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'awaiting'}
            ),
        }


# Форма создания отзыва
class PostReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'awaiting'}
            ),
        }
