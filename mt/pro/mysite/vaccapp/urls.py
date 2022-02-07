from . import views
from django.urls import path
app_name='vaccapp'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('booking/',views.booking,name='booking'),
    path('details/',views.details,name='details'),
    path('final/',views.final,name='final'),
    path('logout/',views.logout,name='logout'),
]