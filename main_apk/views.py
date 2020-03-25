from django.shortcuts import render
from django.views import View


class MainPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class FormView(View):
    def get(self, request):
        return render(request, 'form.html')


class FormConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')
