from django.urls import path,include
from .import views

urlpatterns = [
  path('register/', views.RegisterUser,name='signup' ),
  path('login/', views.login_view,name='login' ),
  path('profile/', views.profile,name='profile' ),
  path('logout/', views.logout_view,name='logout' ),
    
]