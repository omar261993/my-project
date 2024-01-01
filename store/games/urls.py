from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('details/<int:id>/',views.product_details,name='product'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
]
