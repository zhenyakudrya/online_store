import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify_code')

    def form_valid(self, form):
        verify_code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        new_user = form.save(commit=False)
        new_user.verify_key = verify_code
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Вы зарегестрировались на нашей платформе, добро пожаловать!'
                    f'Для подтверждения почты вставьте код: {verify_code} в форму.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:index'))


class CodeView(View):
    model = User
    template_name = 'users/verify_code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        verify_key = request.POST.get('verify_key')
        user = User.objects.filter(verify_key=verify_key).first()

        if user is not None and user.verify_key == verify_key:
            user.email_verify = True
            user.save()
            return redirect('users:login')