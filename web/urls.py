"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from www import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about1',views.about,name='about'),
    path('products',views.products,name='products'),
    path('contact',views.contactData,name='contact'),
    path('custom',views.custom,name='custom'),
    path('unknown',views.unknown,name='unknown'),
    path('facilities',views.facilities,name='facilities'),
    path('c',views.C,name='C'),
    path('B',views.B,name='B'),
    path('readmore/<int:id>',views.readmore,name='readmore'),
    path('register',views.register,name='register'),
    path('login/',views.loginview,name='login'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('cart/<int:id>',views.cart1,name='cart'),
    path('logout',views.logoutview,name='logout'),
    path('showcart',views.showcart,name='showcart'),
    path('deletecart/<int:id>',views.deletecart,name='deletecart'),
    path('sendmail',views.send_mail,name='sendmail'),
    path('order',views.order,name='order'),
    path('search',views.search,name='search'),
]
