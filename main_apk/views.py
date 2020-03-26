from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics

from main_apk.forms import LoginForm
from main_apk.models import DonationModel, InstitutionModel, CategoryModel
from main_apk.serializers import CategorySerializer, InstitutionSerializer


class MainPageView(View):
    def get(self, request):
        quantity = 0
        fund = 0
        fund_check = []
        inst_fund = InstitutionModel.objects.filter(type=1)
        inst_ngo = InstitutionModel.objects.filter(type=2)
        inst_other = InstitutionModel.objects.filter(type=3)
        items = DonationModel.objects.all()
        for item in items:
            quantity += item.quantity
            if item.institution.id in fund_check:
                continue
            else:
                fund += 1
        return render(request, 'index.html',
                      {'quantity': quantity, 'fund': fund, 'inst_fund': inst_fund, 'inst_ngo': inst_ngo,
                       'inst_other': inst_other})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                return redirect('register_page')
        else:
            return redirect('register_page')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        new_user = User.objects.create_user(first_name=name,
                                            last_name=surname,
                                            username=email,
                                            password=password,
                                            email=email)
        new_user.save()
        return redirect('login_page')


class FormView(View):
    def get(self, request):
        if request.user.is_authenticated:
            categories = CategoryModel.objects.all()
            institutions = InstitutionModel.objects.all()
            return render(request, 'form.html', {'categories': categories, 'institutions': institutions})
        else:
            return redirect('login_page')

    def post(self, request):
        new_donation = DonationModel()
        new_donation.quantity = request.POST['bags']
        new_donation.address = request.POST['address'] + ', ' + request.POST['postcode']
        new_donation.phone_number = request.POST['phone']
        new_donation.city = request.POST['city']
        new_donation.pick_up_date = request.POST['data']
        new_donation.pick_up_time = request.POST['time']
        new_donation.pick_up_comment = request.POST['more_info']
        new_donation.user = request.user
        new_donation.institution = InstitutionModel.objects.get(pk=request.POST['organization'])
        new_donation.save()
        for category in request.POST['categories']:
            new_donation.categories.add(CategoryModel.objects.get(pk=category))
        new_donation.save()
        return redirect('form_confirmation_page')




class FormConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main_page')


class CategoryListView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class InstitutionsListView(generics.ListCreateAPIView):
    queryset = InstitutionModel.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstitutionModel.objects.all()
    serializer_class = InstitutionSerializer
