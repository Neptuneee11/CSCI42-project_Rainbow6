"""
URL configuration for abra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from Customer.views import RegisterView

urlpatterns = [
    # Default URL
    path('admin/', admin.site.urls),
    path('web/', include('web.urls', namespace='web')),
    path('bicycleScanner/', include('qrScanner.urls', namespace="qrScanner")),
    path('bicycles/', include('bicycles.urls', namespace='bicycle')),
    path('', include('web.urls', namespace='login')),
    path("accounts/", include("django.contrib.auth.urls")),

    # Account Creation URL
    path('register/', RegisterView.as_view(), name="register"),

    # Account Login URL (secretly a "login/")
    path('', include("django.contrib.auth.urls")),

    # customer profile url
    path('customer/', include('Customer.urls', namespace='customer')),

    # transactions
    path('transactions/', include('Transactions.urls', namespace='transactions')),

]
