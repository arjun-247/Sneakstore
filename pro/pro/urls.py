"""pro URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('men',views.men,name='men'),
    path('men_casual',views.men_casual,name='men_casual'),
    path('men_formal',views.men_formal,name='men_formal'),
    path('men_boots',views.men_boots,name='men_boots'),
    path('men_sneakers',views.men_sneakers,name='men_sneaker'),
    path('women',views.women,name='women'),
    path('women_casual',views.women_casual,name='women_casual'),
    path('women_sports',views.women_sports,name='women_sports'),
    path('women_boots',views.women_dress,name='women_dress'),
    path('kids',views.kids,name='kids'),
    path('collection',views.collection,name='collection'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('details/<int:id>/',views.details,name='details'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('checkout/',views.checkout,name='checkout'),
    path('order-complete/',views.order_complete,name='order-complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
