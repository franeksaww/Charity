"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from main_apk.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', MainPageView.as_view(), name='main_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('form/', FormView.as_view(), name='form_page'),
    path('form_confirmation/', FormConfirmationView.as_view(), name='form_confirmation_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # rest_api
    path('api/category/', CategoryListView.as_view(), name='category_all'),
    path('api/category/<int:id>', CategoryView.as_view(), name='category_details'),
    path('api/institution/', InstitutionsListView.as_view(), name='institutions_all'),
    path('api/institution/<int:id>', InstitutionsView.as_view(), name='institutions_details'),
    path('api/donations/', DonationsListView.as_view(), name='donations'),
    path('api/donations/<int:id>', DonationView.as_view(), name='donations-details'),

    # user
    path('profile/', ProfileView.as_view(), name='profile'),
    path('donations/', UserDonationsView.as_view(), name='donations'),
    re_path(r'^donations/(?P<pk>[0-9]*)/$', UserDonationDetailView.as_view(), name='donation_detail'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('change_status/<int:id>', ChangeStatusView.as_view(), name='change_status'),
    path('change_passwd/', PasswordChangeView.as_view(), name='password_change'),
]
